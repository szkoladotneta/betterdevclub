import requests
import re
import json
import uuid
import os
import sys

# Constants
BASE_URL = "https://riverside.com"
LOGIN_PAGE_URL = f"{BASE_URL}/login"
LOGIN_API_URL = f"{BASE_URL}/login-react"
PROJECTS_API_URL = f"{BASE_URL}/api/v4/projects/studio/kajetan-duszyskis-studio"
CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "credentials.json")
TRANSCRIPTIONS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "transcriptions", "raw")
TRANSCRIPTION_API_BASE = f"{BASE_URL}/api/v4/transcriptions/editableWithVoiceActivity"
PROJECT_CLIPS_API_TEMPLATE = BASE_URL + "/api/v4/projects/{project_id}/clips/made-for-you"

def load_credentials():
    if not os.path.exists(CREDENTIALS_PATH):
        print(f"Error: Credentials file not found at {CREDENTIALS_PATH}")
        print("Please create it with the following format:")
        print('{\n    "email": "your_email",\n    "password": "your_password"\n}')
        sys.exit(1)
    
    with open(CREDENTIALS_PATH, "r") as f:
        return json.load(f)

def get_riverside_version(session):
    print(f"Fetching {LOGIN_PAGE_URL} to find env.js...")
    try:
        response = session.get(LOGIN_PAGE_URL, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching login page: {e}")
        return None

    # Step 2: Extract URL to env.js
    env_js_match = re.search(r'src=["\']([^"\']+\/env\.js(?:\?[^"\']+)?)["\']', response.text)
    env_js_url = env_js_match.group(1) if env_js_match else None
    
    if not env_js_url:
        print("Could not find env.js URL in HTML via regex. Trying app.riverside.com/env.js")
        env_js_url = "https://app.riverside.com/env.js"
    elif not env_js_url.startswith('http'):
        path_prefix = "https://app.riverside.com" if "app.riverside.com" in response.url else BASE_URL
        env_js_url = f"{path_prefix}{env_js_url}" if env_js_url.startswith('/') else f"{path_prefix}/{env_js_url}"

    print(f"Fetching env.js from {env_js_url}...")
    try:
        env_response = session.get(env_js_url, timeout=10)
        env_response.raise_for_status()
        env_content = env_response.text
    except Exception as e:
        print(f"Error fetching env.js: {e}")
        return None

    # Step 3: Parse variable about riverside version
    version_match = re.search(r'VERSION_TAG["\']?\s*[:=]\s*["\']([^"\']+)["\']', env_content)
    if not version_match:
        version_match = re.search(r'version["\']?\s*[:=]\s*["\']([^"\']+)["\']', env_content)
    
    version_tag = version_match.group(1) if version_match else "6.107.212"
    print(f"Detected version: {version_tag}")
    return version_tag

def login(session, email, password, version_tag):
    print("Logging in...")
    riverside_id = str(uuid.uuid4())
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': BASE_URL,
        'pragma': 'no-cache',
        'referer': f'{LOGIN_PAGE_URL}?redirect=%2Fdashboard%2Fproductions',
        'riverside-id': riverside_id,
        'riverside-version-env': 'production',
        'riverside-version-tag': version_tag,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
    }

    payload = {
        "email": email,
        "password": password,
        "redirect": "/dashboard/productions"
    }

    try:
        response = session.post(LOGIN_API_URL, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            print("Login successful.")
            return True, headers
        else:
            print(f"Login failed ({response.status_code}): {response.text}")
            return False, headers
    except Exception as e:
        print(f"Error during login: {e}")
        return False, headers

def download_transcription(session, headers, session_id, episode_num):
    url = f"{TRANSCRIPTION_API_BASE}/{session_id}"
    print(f"Downloading transcription for episode {episode_num} (Session: {session_id})...")
    
    try:
        response = session.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            filename = f"{episode_num}.json"
            filepath = os.path.join(TRANSCRIPTIONS_DIR, filename)
            
            os.makedirs(TRANSCRIPTIONS_DIR, exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(response.json(), f, indent=2)
            print(f"Successfully saved to {filepath}")
            return True
        else:
            print(f"Failed to download transcription ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"Error downloading transcription: {e}")
    return False

def get_session_id_for_project(session, headers, project_id):
    url = PROJECT_CLIPS_API_TEMPLATE.format(project_id=project_id)
    params = {'offset': '0', 'limit': '200'}
    try:
        response = session.get(url, params=params, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            clips = data.get("clips", [])
            if clips and len(clips) > 0:
                # Look for sessionId in clips[0]['take']
                take = clips[0].get("take", {})
                session_id = take.get("sessionId")
                if session_id:
                    return session_id
        else:
            print(f"Failed to fetch project clips ({response.status_code})")
    except Exception as e:
        print(f"Error fetching project clips: {e}")
    return None

def check_missing_transcriptions(session, headers, projects):
    print("\nChecking for missing transcriptions...")
    if not os.path.exists(TRANSCRIPTIONS_DIR):
        print(f"Creating directory {TRANSCRIPTIONS_DIR}...")
        os.makedirs(TRANSCRIPTIONS_DIR, exist_ok=True)

    for project in projects:
        title = project.get("title", "")
        project_id = project.get("_id")
        print(f"Checking project: {title} (ID: {project_id})")
        match = re.search(r'#(\d+)', title)
        if match:
            episode_num = match.group(1).zfill(3)
            filename = f"{episode_num}.json"
            filepath = os.path.join(TRANSCRIPTIONS_DIR, filename)
            
            if not os.path.exists(filepath):
                print(f"Missing: {title} ({filename})")
                
                # Fetch sessionId using the new project clips API
                session_id = get_session_id_for_project(session, headers, project_id)
                
                if session_id:
                    download_transcription(session, headers, session_id, episode_num)
                else:
                    print(f"Could not find sessionId for {title} (Project ID: {project_id}).")
    
    print("\nFinished checking transcriptions.")

def run():
    creds = load_credentials()
    session = requests.Session()
    session.headers.update({
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
    })

    version_tag = get_riverside_version(session)
    if not version_tag:
        sys.exit(1)

    success, headers = login(session, creds["email"], creds["password"], version_tag)
    
    # Update headers for the API call
    headers.update({
        'referer': f'{BASE_URL}/dashboard/studios/kajetan-duszyskis-studio/projects',
    })

    print(f"Fetching projects from {PROJECTS_API_URL}...")
    params = {
        'offset': '0',
        'limit': '5',
        'sortBy': 'createdAt',
        'orderBy': 'desc'
    }

    try:
        response = session.get(PROJECTS_API_URL, params=params, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            print("Successfully fetched projects.")
            check_missing_transcriptions(session, headers, data.get("projects", []))
        else:
            print(f"Failed to fetch projects ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"Error fetching projects: {e}")

if __name__ == "__main__":
    run()

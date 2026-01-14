import os
import re
import json
import hashlib

# Configuration
INPUT_FILE = "index.html"
OUTPUT_DIR = "episodes" # We'll put them in a folder
EPISODES_FILE = "episodes.json"
SPEAKERS_FILE = "speakers.json"

def calculate_version(files):
    hasher = hashlib.md5()
    for file_path in files:
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                hasher.update(f.read())
    return hasher.hexdigest()[:10]

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Get data version
data_version = calculate_version([EPISODES_FILE, SPEAKERS_FILE])
print(f"Data version calculated: {data_version}")

# Read the template
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    template = f.read()

# Auto-update version string in index.html to match data hash
# Look for: const version = "any_version";
template = re.sub(r'const version = ".*?";', f'const version = "{data_version}";', template)

# Save updated template back to index.html so it persists
with open(INPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(template)

# Load episodes data and filter published ones
with open(EPISODES_FILE, 'r', encoding='utf-8') as f:
    all_episodes = json.load(f)
    episodes = [ep for ep in all_episodes if not ep.get('notPublished', False)]

def update_meta(content, episode):
    # Update Meta Tags
    meta_updates = {
        r'<title>.*?</title>': f"<title>BetterDevClub | {episode['title']}</title>",
        r'<meta property="og:title" content=".*?">': f'<meta property="og:title" content="{episode["title"]}">',
        r'<meta property="og:description" content=".*?">': f'<meta property="og:description" content="{episode["desc"]}">',
        r'<meta name="description" content=".*?">': f'<meta name="description" content="{episode["desc"]}">',
        r'<meta property="og:image" content=".*?">': f'<meta property="og:image" content="https://i.ytimg.com/vi/{episode["youtubeId"]}/maxresdefault.jpg">' if episode.get("youtubeId") else '',
    }
    
    for pattern, replacement in meta_updates.items():
        content = re.sub(pattern, replacement, content)
    return content

def fix_paths(content):
    # Fix relative paths (since we are in /episodes/ folder)
    # This regex avoids paths that start with /, http, or #
    content = re.sub(r'src="(?!(/|http))', 'src="../', content)
    content = re.sub(r'href="(?!(/|http|#))', 'href="../', content)
    return content

def get_template_html(template_id):
    """Extracts the inner HTML of a <template> tag from the index.html file."""
    match = re.search(f'<template id="{template_id}">(.*?)</template>', template, re.DOTALL)
    return match.group(1).strip() if match else ""

EPISODE_ITEM_TEMPLATE = get_template_html("ssr-episode-item")
EPISODE_DETAIL_TEMPLATE = get_template_html("ssr-episode-detail")

def generate_episode_list_html(episodes):
    html = '<div class="flex flex-col gap-6 mb-12">'
    for ep in episodes:
        tags_html = "".join([f'<span class="px-3 py-1 rounded-full bg-slate-100 dark:bg-white/5 text-slate-500 dark:text-slate-400 text-[11px] font-bold uppercase tracking-wider">{t}</span>' for t in ep['tags']])
        item = EPISODE_ITEM_TEMPLATE.replace('{{NUM}}', ep['num'])\
                                   .replace('{{DATE}}', ep['date'])\
                                   .replace('{{TITLE}}', ep['title'])\
                                   .replace('{{DESC}}', ep['desc'])\
                                   .replace('{{TAGS}}', tags_html)
        html += item
    html += '</div>'
    return html

def generate_episode_ssr_html(episode):
    return EPISODE_DETAIL_TEMPLATE.replace('{{NUM}}', episode['num'])\
                                  .replace('{{TITLE}}', episode['title'])\
                                  .replace('{{DATE}}', episode['date'])\
                                  .replace('{{DURATION}}', episode['duration'])\
                                  .replace('{{DESC}}', episode['desc'])

def generate_page(episode):
    output_filename = f"episode-{episode['num']}.html"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    # Customize the content
    content = update_meta(template, episode)
    
    # Inject Initial Route (without .html suffix for clean URLs)
    route_script = f'<script>window.INITIAL_ROUTE = "/episodes/episode-{episode["num"]}";</script>'
    content = content.replace('</head>', f'    {route_script}\n</head>')
    
    # Inject Episode-Specific SSR (instead of the episode list)
    episode_ssr = generate_episode_ssr_html(episode)
    content = content.replace('<div id="root"></div>', f'<div id="root">{episode_ssr}</div>')
    
    content = fix_paths(content)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated: {output_path}")

def generate_episodes_index(episodes):
    output_path = os.path.join(OUTPUT_DIR, "index.html")
    
    # Basic meta for episodes list
    meta_data = {
        "title": "BetterDevClub | All Episodes",
        "desc": f"Archive of {len(episodes)} podcast episodes for modern developers.",
        "ogImage": episodes[0].get("ogImage", "")
    }
    
    content = update_meta(template, meta_data)
    
    # Inject Initial Route
    route_script = f'<script>window.INITIAL_ROUTE = "/episodes";</script>'
    content = content.replace('</head>', f'    {route_script}\n</head>')
    
    # Inject SSR Content
    ssr_html = f"""
    <div class="max-w-[960px] mx-auto px-4 py-12">
        <div class="mb-12">
            <h1 class="text-slate-900 dark:text-white text-5xl font-black leading-tight tracking-[-0.033em] mb-4">Episodes Archive</h1>
            <p class="text-slate-500 dark:text-slate-400 text-lg font-normal leading-relaxed max-w-2xl">
                Deep dives into software development, engineering leadership, and career growth. Browsing through {len(episodes)}+ episodes curated for the modern developer.
            </p>
        </div>
        {generate_episode_list_html(episodes)}
    </div>"""
    
    content = content.replace('<div id="root"></div>', f'<div id="root">{ssr_html}</div>')
    
    content = fix_paths(content)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated: {output_path}")

# Run generator
for ep in episodes:
    generate_page(ep)

generate_episodes_index(episodes)

print("\nSuccess! Sub-pages created in /episodes/ folder.")
print("Sharing links will now look like: https://yourdomain.com/episodes/episode-155")

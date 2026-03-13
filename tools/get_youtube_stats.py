import json
import os
import csv
import sys
from dotenv import load_dotenv
from googleapiclient.discovery import build

def get_youtube_stats(api_key, video_ids):
    """Fetches statistics for a list of YouTube video IDs."""
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # YouTube API allows up to 50 IDs per request
    stats = []
    for i in range(0, len(video_ids), 50):
        chunk = video_ids[i:i + 50]
        request = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(chunk)
        )
        response = request.execute()
        
        for item in response.get('items', []):
            snippet = item['snippet']
            statistics = item['statistics']
            
            stats.append({
                'id': item['id'],
                'title': snippet.get('title', ''),
                'publishedAt': snippet.get('publishedAt', ''),
                'viewCount': int(statistics.get('viewCount', 0)),
                'likeCount': int(statistics.get('likeCount', 0)),
                'commentCount': int(statistics.get('commentCount', 0)),
                'description': snippet.get('description', '').replace('\n', ' '),
                'tags': ", ".join(snippet.get('tags', [])),
            })
    return stats

def main():
    # Load environment variables from youtube.env
    env_path = os.path.join(os.path.dirname(__file__), 'youtube.env')
    load_dotenv(env_path)
    
    # Configuration
    api_key = os.environ.get('YOUTUBE_API_KEY')
    if not api_key:
        print(f"Error: YOUTUBE_API_KEY not found in {env_path}")
        sys.exit(1)

    episodes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'episodes.json'))
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'youtube_stats.csv'))

    if not os.path.exists(episodes_path):
        print(f"Error: {episodes_path} not found.")
        sys.exit(1)

    # Read IDs from episodes.json
    with open(episodes_path, 'r', encoding='utf-8') as f:
        episodes = json.load(f)
    
    video_ids = [ep.get('youtubeId') for ep in episodes if ep.get('youtubeId')]
    
    if not video_ids:
        print("No YouTube IDs found in episodes.json.")
        sys.exit(0)

    print(f"Fetching stats for {len(video_ids)} videos...")
    
    try:
        stats = get_youtube_stats(api_key, video_ids)
        
        # Sort by view count descending
        stats.sort(key=lambda x: x['viewCount'], reverse=True)

        if not stats:
            print("No data returned from YouTube API.")
            sys.exit(0)

        # Write to CSV
        keys = stats[0].keys()
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(stats)

        print(f"Success! Statistics saved to {output_path}")
        print("\nNOTE: CTR (Click-Through Rate) and AVD (Average View Duration) require ")
        print("the YouTube Analytics API (OAuth2), which is more complex than the Data API (API Key).")
        print("Data API only provides public metrics like Views, Likes, Tags, and Descriptions.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

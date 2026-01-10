import json
import os
import glob

def format_timestamp(ms):
    total_seconds = ms // 1000
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    return f"{minutes:02d}:{seconds:02d}"

def process_transcription(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    all_sentences = []
    
    speakers = data['data']['speakers']
    for speaker in speakers:
        name = speaker['name']
        for sentence in speaker['sentences']:
            words = sentence.get('editedWords') or sentence.get('words')
            if not words:
                continue
            
            # Find the first word that has a timestamp
            first_word_timestamp = None
            for w in words:
                if len(w) >= 2 and isinstance(w[1], (int, float)):
                    first_word_timestamp = w[1]
                    break
            
            if first_word_timestamp is None:
                continue
                
            text = " ".join([w[0] for w in words if w[0] and w[0] != "⁓"]).strip()
            if not text:
                continue
                
            all_sentences.append({
                'timestamp': first_word_timestamp,
                'speaker': name,
                'text': text
            })
    
    # Sort all sentences by timestamp
    all_sentences.sort(key=lambda x: x['timestamp'])
    
    # Optional: Normalize timestamps if the first one is not 0
    if all_sentences:
        offset = all_sentences[0]['timestamp']
        for s in all_sentences:
            s['timestamp'] -= offset
            
    # Group consecutive sentences by the same speaker
    grouped = []
    if all_sentences:
        current_speaker = all_sentences[0]['speaker']
        current_time = format_timestamp(all_sentences[0]['timestamp'])
        current_text = all_sentences[0]['text']
        
        for i in range(1, len(all_sentences)):
            next_s = all_sentences[i]
            if next_s['speaker'] == current_speaker:
                current_text += " " + next_s['text']
            else:
                grouped.append({
                    "speaker": current_speaker,
                    "time": current_time,
                    "text": current_text
                })
                current_speaker = next_s['speaker']
                current_time = format_timestamp(next_s['timestamp'])
                current_text = next_s['text']
        
        grouped.append({
            "speaker": current_speaker,
            "time": current_time,
            "text": current_text
        })
        
    return {"transcript": grouped}

def run():
    # Use absolute paths or relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    input_dir = os.path.join(project_root, 'transcriptions', 'raw')
    output_dir = os.path.join(project_root, 'transcriptions')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    files = glob.glob(os.path.join(input_dir, '*.json'))
    processed_count = 0
    for file_path in files:
        filename = os.path.basename(file_path)
        output_path = os.path.join(output_dir, filename)
        
        if os.path.exists(output_path):
            print(f"Skipping {filename} (already exists)")
            continue
            
        print(f"Processing {filename}...")
        result = process_transcription(file_path)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        processed_count += 1
            
    print(f"Done! Processed {processed_count} new files.")

if __name__ == "__main__":
    run()

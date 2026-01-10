import json

def format_timestamp(ms):
    total_seconds = ms // 1000
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    return f"[{minutes:02d}:{seconds:02d}]"

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
                'name': name,
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
    grouped_sentences = []
    if all_sentences:
        current_group = all_sentences[0]
        for i in range(1, len(all_sentences)):
            next_s = all_sentences[i]
            # If same speaker and they are relatively close (e.g. within 5 seconds)
            # Actually, standard transcripts often just group any consecutive turns by same speaker.
            if next_s['name'] == current_group['name']:
                current_group['text'] += " " + next_s['text']
            else:
                grouped_sentences.append(current_group)
                current_group = next_s
        grouped_sentences.append(current_group)

    output_lines = []
    for s in grouped_sentences:
        ts = format_timestamp(s['timestamp'])
        output_lines.append(f"{ts}[{s['name']}] {s['text']}")
        
    return "\n".join(output_lines)

if __name__ == "__main__":
    result = process_transcription('Untitled-1.json')
    with open('transkrypcja_edycja.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    print("Transkrypcja wygenerowana w pliku transkrypcja_edycja.txt")

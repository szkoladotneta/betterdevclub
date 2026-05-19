import sys
import os
import re

if len(sys.argv) < 2:
    print("Usage: python fix.py <path_to_transcription_json>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    r'\bkajtak\b': 'Kajetan',
    r'\bKrzywdy\b': 'Krzywdy', 
    r'\bkrod\b': 'Claude',
    r'\bkrodem\b': 'Claudem',
    r'\bkaretana\b': 'Kajetana',
    r'\bkopilot\b': 'Copilot',
    r'\bkopilota\b': 'Copilota',
    r'\bkopilotem\b': 'Copilotem',
    r'\bkopilocie\b': 'Copilocie',
    r'\bejszur\b': 'Azure',
    r'\bazur\b': 'Azure',
    r'\bEJA\b': 'AI',
    r'\bAI-em\b': 'AI',
    r'\bper partner\b': 'pair-partner',
    r'\bpre partner\b': 'pair-partner',
    r'\bper-programming\b': 'pair programming',
    r'\bper programming\b': 'pair programming',
    r'\bperowaliśmy\b': 'pairowaliśmy',
    r'\brelicach\b': 'Railsach',
    r'\brelsowych\b': 'railsowych',
    r'\bdotytowców\b': 'dotnetowców',
    r'\bkolu\b': 'callu',
    r'\basygnoliczną\b': 'asynchroniczną',
    r'\bARK NC\b': 'Arkency',
    r'\barkency\b': 'Arkency',
    r'\bArkansas\b': 'Arkency',
    r'\bPetył\b': 'Piotr'
}

for old, new in replacements.items():
    content = re.sub(old, new, content, flags=re.IGNORECASE)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done fixing transcription '{file_path}'")

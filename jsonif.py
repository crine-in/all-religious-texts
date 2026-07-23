import re
import json

INPUT_FILE = "isha.txt"
OUTPUT_FILE = "isha.json"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    content = f.read().strip()

pattern = re.compile(
    r"(.*?)\|\|\s*IsUp_(\d+)\s*\|\|",
    re.DOTALL
)

verses = []

for idx, match in enumerate(pattern.finditer(content), start=1):
    text = match.group(1).strip()

    # Remove extra blank lines
    text = re.sub(r"\n\s*\n+", "\n", text)

    verse = int(match.group(2))

    verses.append({
        "chapter_id": 1,
        "chapter_number": 1,
        "externalId": idx,
        "id": idx,
        "title": f"Verse {idx}",
        "verse": verse,
        "text": text
    })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(verses, f, ensure_ascii=False, indent=4)

print(f"Converted {len(verses)} verses.")

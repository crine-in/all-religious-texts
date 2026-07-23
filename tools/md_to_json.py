import re
import json
import argparse
import hashlib
from pathlib import Path

def convert_md_to_json(input_path: Path, output_path: Path):
    """Parses Markdown lists or headings of verses into JSON format."""
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.splitlines()
    verses = []
    current_chapter = 1
    verse_counter = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            # Heading indicates chapter
            match = re.search(r"\d+", line)
            if match:
                current_chapter = int(match.group(0))
                verse_counter = 0
            continue
        
        verse_counter += 1
        checksum = hashlib.sha256(line.encode("utf-8")).hexdigest()
        verses.append({
            "id": f"md:text:{current_chapter}.{verse_counter}",
            "externalId": len(verses) + 1,
            "religion": "Generic",
            "collection": "Markdown Ingestion",
            "book": input_path.stem.title(),
            "chapter": current_chapter,
            "verse": verse_counter,
            "citation": f"{current_chapter}.{verse_counter}",
            "language": "English",
            "script": "Latin",
            "text": line,
            "license": "Public Domain",
            "source": input_path.name,
            "checksum": checksum
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(verses, f, ensure_ascii=False, indent=2)

    print(f"Parsed {len(verses)} verses from Markdown file {input_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to ART JSON")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    convert_md_to_json(args.input, args.output)

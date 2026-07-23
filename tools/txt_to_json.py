import re
import json
import argparse
import hashlib
from pathlib import Path

def convert_txt_to_json(input_path: Path, output_path: Path, book_title: str, religion: str, collection: str, language: str, script: str):
    """Parses plain text scriptures into ART verse schema JSON."""
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # Pattern supporting || Verse_1 || or standard verse markers
    pattern = re.compile(r"(.*?)\|\|\s*([A-Za-z0-9_]+)_(\d+)\s*\|\|", re.DOTALL)
    matches = list(pattern.finditer(content))
    
    verses = []
    if matches:
        for idx, match in enumerate(matches, start=1):
            text = match.group(1).strip()
            text = re.sub(r"\n\s*\n+", "\n", text)
            verse_num = int(match.group(3))
            
            checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()
            
            verses.append({
                "id": f"{religion.lower()}:{collection.lower()}:{book_title.lower().replace(' ', '-')}:1.1.{verse_num}",
                "externalId": idx,
                "religion": religion,
                "collection": collection,
                "book": book_title,
                "chapter": 1,
                "verse": verse_num,
                "citation": f"1.1.{verse_num}",
                "language": language,
                "script": script,
                "text": text,
                "license": "Public Domain",
                "source": str(input_path.name),
                "checksum": checksum
            })
    else:
        # Fallback line-by-line parsing
        lines = [l.strip() for l in content.splitlines() if l.strip()]
        for idx, line in enumerate(lines, start=1):
            checksum = hashlib.sha256(line.encode("utf-8")).hexdigest()
            verses.append({
                "id": f"{religion.lower()}:{collection.lower()}:{book_title.lower().replace(' ', '-')}:1.1.{idx}",
                "externalId": idx,
                "religion": religion,
                "collection": collection,
                "book": book_title,
                "chapter": 1,
                "verse": idx,
                "citation": f"1.1.{idx}",
                "language": language,
                "script": script,
                "text": line,
                "license": "Public Domain",
                "source": str(input_path.name),
                "checksum": checksum
            })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(verses, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(verses)} verses from {input_path} to {output_path}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert TXT scripture file to ART JSON schema.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--book", default="Sample Scripture")
    parser.add_argument("--religion", default="Hinduism")
    parser.add_argument("--collection", default="Upanishads")
    parser.add_argument("--language", default="Sanskrit")
    parser.add_argument("--script", default="IAST")
    args = parser.parse_args()

    convert_txt_to_json(args.input, args.output, args.book, args.religion, args.collection, args.language, args.script)

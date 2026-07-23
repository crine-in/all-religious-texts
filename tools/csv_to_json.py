import csv
import json
import argparse
import hashlib
from pathlib import Path

def convert_csv_to_json(input_path: Path, output_path: Path):
    """Parses tabular CSV files into ART verse schema JSON."""
    verses = []
    with open(input_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            text = row.get("text", "").strip()
            ch = int(row.get("chapter", 1))
            v = int(row.get("verse", idx))
            
            checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()
            verses.append({
                "id": f"csv:text:{ch}.{v}",
                "externalId": idx,
                "religion": row.get("religion", "Generic"),
                "collection": row.get("collection", "CSV Ingestion"),
                "book": row.get("book", input_path.stem.title()),
                "chapter": ch,
                "verse": v,
                "citation": f"{ch}.{v}",
                "language": row.get("language", "English"),
                "script": row.get("script", "Latin"),
                "text": text,
                "license": row.get("license", "Public Domain"),
                "source": input_path.name,
                "checksum": checksum
            })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(verses, f, ensure_ascii=False, indent=2)

    print(f"Parsed {len(verses)} verses from CSV file {input_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert CSV to ART JSON")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    convert_csv_to_json(args.input, args.output)

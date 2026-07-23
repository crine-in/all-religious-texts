import json
import hashlib
import argparse
from pathlib import Path

def enrich_draft_json(input_file: Path, output_file: Path, book_title: str, collection: str = "Principal Upanishads", religion: str = "Hinduism", language: str = "Sanskrit", script: str = "IAST"):
    """
    Enriches a draft scripture JSON file (e.g. isha.json or katha.json) 
    into the canonical ART schemas/verse.schema.json format.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        draft_verses = json.load(f)

    book_slug = book_title.lower().replace(" ", "-")
    enriched_verses = []

    for idx, item in enumerate(draft_verses, start=1):
        ch = item.get("chapter_number", item.get("chapter_id", 1))
        v = item.get("verse", idx)
        text = item.get("text", "").strip()

        verse_id = f"{religion.lower()}:{collection.lower().replace(' ', '-')}:{book_slug}:{ch}.{v}"
        checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()

        enriched = {
            "id": verse_id,
            "externalId": idx,
            "religion": religion,
            "collection": collection,
            "book": book_title,
            "chapter": ch,
            "verse": v,
            "citation": f"{ch}.{v}",
            "language": language,
            "script": script,
            "text": text,
            "license": "Public Domain",
            "source": f"Reference file: {input_file.name}",
            "checksum": checksum
        }
        enriched_verses.append(enriched)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(enriched_verses, f, ensure_ascii=False, indent=2)

    print(f"Successfully enriched {len(enriched_verses)} verses from {input_file.name} -> {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enrich draft JSON (isha.json, katha.json) to ART verse schema.")
    parser.add_argument("--input", required=True, type=Path, help="Input draft file (e.g. isha.json)")
    parser.add_argument("--output", required=True, type=Path, help="Output enriched file path")
    parser.add_argument("--book", required=True, type=str, help="Book title (e.g. 'Isha Upanishad')")
    parser.add_argument("--collection", default="Principal Upanishads", type=str)
    parser.add_argument("--religion", default="Hinduism", type=str)
    args = parser.parse_args()

    enrich_draft_json(args.input, args.output, args.book, args.collection, args.religion)

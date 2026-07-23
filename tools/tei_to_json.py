import xml.etree.ElementTree as ET
import json
import argparse
import hashlib
from pathlib import Path

def convert_tei_to_json(input_path: Path, output_path: Path):
    """Parses TEI P5 XML digital humanities markup into ART verse schema JSON."""
    ns = {"tei": "http://www.tei-c.org/ns/1.0"}
    tree = ET.parse(input_path)
    root = tree.getroot()
    
    verses = []
    # Search for TEI verse elements (<l> or <seg> or <p>)
    nodes = root.findall(".//tei:l", ns) or root.findall(".//l")
    
    for idx, node in enumerate(nodes, start=1):
        text = "".join(node.itertext()).strip()
        if not text:
            continue
        checksum = hashlib.sha256(text.encode("utf-8")).hexdigest()
        verses.append({
            "id": f"tei:text:1.{idx}",
            "externalId": idx,
            "religion": "Generic",
            "collection": "TEI Corpus",
            "book": input_path.stem.title(),
            "chapter": 1,
            "verse": idx,
            "citation": f"1.{idx}",
            "language": "Latin",
            "script": "Latin",
            "text": text,
            "license": "Public Domain",
            "source": input_path.name,
            "checksum": checksum
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(verses, f, ensure_ascii=False, indent=2)

    print(f"Parsed {len(verses)} TEI elements from {input_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert TEI XML to ART JSON")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    convert_tei_to_json(args.input, args.output)

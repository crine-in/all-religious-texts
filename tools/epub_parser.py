import argparse
from pathlib import Path

def parse_epub(input_path: Path):
    """Stub specification for EPUB ebook extraction."""
    print(f"EPUB Ingestion Utility: Processing {input_path}")
    print("EPUB parsing requires zipfile & ebooklib to extract XHTML content chapters.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    parse_epub(args.input)

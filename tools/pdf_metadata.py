import argparse
from pathlib import Path

def extract_pdf_metadata(input_path: Path):
    """Stub specification for PDF metadata and digitised manuscript header extraction."""
    print(f"PDF Metadata Extractor: Extracting headers from {input_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    extract_pdf_metadata(args.input)

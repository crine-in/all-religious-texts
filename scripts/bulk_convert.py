import subprocess
from pathlib import Path

def bulk_convert(input_dir: Path, output_dir: Path):
    """Batch processes raw text/xml files into ART JSON schema."""
    output_dir.mkdir(parents=True, exist_ok=True)
    raw_files = list(input_dir.glob("*.txt"))
    
    print(f"Bulk processing {len(raw_files)} files from {input_dir} -> {output_dir}...")
    for txt in raw_files:
        out_json = output_dir / f"{txt.stem}.json"
        cmd = ["python3", "tools/txt_to_json.py", "--input", str(txt), "--output", str(out_json)]
        subprocess.run(cmd)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3:
        bulk_convert(Path(sys.argv[1]), Path(sys.argv[2]))
    else:
        print("Usage: python bulk_convert.py <input_dir> <output_dir>")

import json
from pathlib import Path

def query_verses_by_citation(json_file: Path, target_citation: str):
    """Example Python code demonstrating dataset querying."""
    with open(json_file, "r", encoding="utf-8") as f:
        verses = json.load(f)
        
    for verse in verses:
        if verse.get("citation") == target_citation:
            return verse
    return None

if __name__ == "__main__":
    sample_file = Path(__file__).parent.parent / "isha.json"
    if sample_file.exists():
        result = query_verses_by_citation(sample_file, "1")
        print("Query Result for Citation 1:")
        print(json.dumps(result, indent=2, ensure_ascii=False))

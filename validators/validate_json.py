import json
import sys
from pathlib import Path

def validate_json_syntax(repo_root: Path) -> bool:
    """Verifies that all .json files in the repository contain valid JSON."""
    all_valid = True
    json_files = list(repo_root.glob("**/*.json"))
    
    # Filter out hidden or build paths
    json_files = [p for p in json_files if ".git" not in p.parts and "node_modules" not in p.parts and "venv" not in p.parts]
    
    print(f"Checking syntax of {len(json_files)} JSON files...")
    for json_path in json_files:
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            print(f"❌ JSON Syntax Error in {json_path}: {e}")
            all_valid = False
            
    if all_valid:
        print("✅ All JSON files passed syntax validation.")
    return all_valid

if __name__ == "__main__":
    root = Path(__file__).parent.parent
    success = validate_json_syntax(root)
    sys.exit(0 if success else 1)

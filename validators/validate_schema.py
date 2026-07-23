import json
import sys
from pathlib import Path
import jsonschema

def validate_schemas(repo_root: Path) -> bool:
    """Validates schema files in schemas/ and metadata registries in metadata/."""
    all_valid = True
    schemas_dir = repo_root / "schemas"
    metadata_dir = repo_root / "metadata"
    
    # 1. Validate meta-schemas of schemas/*.schema.json
    schema_files = list(schemas_dir.glob("*.schema.json"))
    print(f"Validating {len(schema_files)} JSON schemas...")
    for sf in schema_files:
        try:
            with open(sf, "r", encoding="utf-8") as f:
                schema_data = json.load(f)
            jsonschema.Draft202012Validator.check_schema(schema_data)
        except Exception as e:
            print(f"❌ Invalid JSON Schema {sf.name}: {e}")
            all_valid = False

    # 2. Validate metadata registries if applicable
    religions_file = metadata_dir / "religions.json"
    if religions_file.exists():
        try:
            with open(religions_file, "r", encoding="utf-8") as f:
                religions = json.load(f)
            assert isinstance(religions, list), "religions.json must be an array"
            for item in religions:
                assert "id" in item and "name" in item, f"Missing id or name in {item}"
        except Exception as e:
            print(f"❌ Invalid metadata/religions.json: {e}")
            all_valid = False

    if all_valid:
        print("✅ Schema validation completed successfully.")
    return all_valid

if __name__ == "__main__":
    root = Path(__file__).parent.parent
    success = validate_schemas(root)
    sys.exit(0 if success else 1)

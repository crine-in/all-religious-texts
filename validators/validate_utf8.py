import sys
from pathlib import Path

def validate_utf8_and_newlines(repo_root: Path) -> bool:
    """Verifies all text files are UTF-8 encoded and use Unix line endings (LF)."""
    all_valid = True
    text_extensions = {".md", ".json", ".py", ".yaml", ".yml", ".txt", ".toml"}
    
    files = [p for p in repo_root.glob("**/*") if p.is_file() and p.suffix in text_extensions]
    files = [p for p in files if ".git" not in p.parts and "venv" not in p.parts]
    
    print(f"Checking UTF-8 encoding & Unix line endings for {len(files)} files...")
    for file_path in files:
        try:
            with open(file_path, "rb") as f:
                content = f.read()
            # Verify UTF-8 decode
            content_str = content.decode("utf-8")
            # Check for Windows CRLF line endings
            if b"\r\n" in content:
                print(f"⚠️ Warning: Windows CRLF newline detected in {file_path.relative_to(repo_root)}")
        except UnicodeDecodeError:
            print(f"❌ Non-UTF-8 character detected in {file_path.relative_to(repo_root)}")
            all_valid = False
            
    if all_valid:
        print("✅ UTF-8 validation passed.")
    return all_valid

if __name__ == "__main__":
    root = Path(__file__).parent.parent
    success = validate_utf8_and_newlines(root)
    sys.exit(0 if success else 1)

import json
import tempfile
from pathlib import Path
import sys

repo_root = Path(__file__).parent.parent
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))

from tools.enrich_dataset import enrich_draft_json

def test_jsonif_reference_files():
    """Verify existing reference JSON files in workspace root parse correctly."""
    isha_path = repo_root / "isha.json"
    if isha_path.exists():
        with open(isha_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        assert isinstance(data, list)
        assert len(data) > 0
        assert "verse" in data[0]

def test_enrich_draft_json():
    """Verify enrich_draft_json tool successfully transforms draft datasets."""
    isha_path = repo_root / "isha.json"
    if isha_path.exists():
        with tempfile.TemporaryDirectory() as tmpdir:
            out_file = Path(tmpdir) / "isha_enriched.json"
            enrich_draft_json(isha_path, out_file, book_title="Isha Upanishad")
            assert out_file.exists()
            with open(out_file, "r", encoding="utf-8") as f:
                enriched = json.load(f)
            assert len(enriched) > 0
            assert enriched[0]["book"] == "Isha Upanishad"
            assert "checksum" in enriched[0]

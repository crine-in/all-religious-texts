# ADDING NEW SCRIPTURES GUIDE

**Organization**: CRINE ([www.crine.in](https://www.crine.in))

---

## Step-by-Step Developer Workflow

This guide demonstrates how to process draft scripture datasets (such as reference files [`isha.json`](/isha.json) and [`katha.json`](/katha.json)) and contribute them to the ecosystem.

### Step 1: Clone Repository & Setup Environment
```bash
git clone https://github.com/crine-in/all-religious-texts.git
cd all-religious-texts
pip install -r requirements.txt
```

### Step 2: Prepare or Locate Draft Dataset
Draft datasets (e.g. `isha.json`, `katha.json`) contain raw verse entries:
```json
[
  {
    "chapter_number": 1,
    "verse": 1,
    "text": "īśā vāsyam idaṃ sarvaṃ..."
  }
]
```

### Step 3: Run Enrichment Tool
Enrich raw drafts using `tools/enrich_dataset.py`:
```bash
python3 tools/enrich_dataset.py \
  --input isha.json \
  --output examples/isha_enriched.json \
  --book "Isha Upanishad" \
  --collection "Principal Upanishads" \
  --religion "Hinduism"
```

### Step 4: Run Validation Suite
Confirm compliance against `schemas/verse.schema.json`:
```bash
python3 validators/run_all.py
pytest tests/
```

### Step 5: Submit Contribution
Push branch and create a Pull Request on GitHub.

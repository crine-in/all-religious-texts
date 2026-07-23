# CONTRIBUTING TO ALL RELIGIOUS TEXTS

Thank you for your interest in contributing to **`all-religious-texts`** and the **All Religious Texts (ART)** ecosystem maintained by **CRINE** ([www.crine.in](https://www.crine.in)).

---

## Code of Conduct

All contributors must adhere to our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Respectful, constructive, and inclusive collaboration is strictly enforced.

---

## How You Can Contribute

1. **Schema & Architecture Improvements**: Enhance JSON schemas, add validation rules, or optimize validation performance.
2. **Ingestion & Conversion Tooling**: Write or improve tools in `tools/` and `scripts/` (e.g. parser for new formats like TEI XML, USFM, EPUB, PDF).
3. **SDK Development**: Improve package stubs and SDK specifications for JavaScript/TypeScript, Python, Go, Rust, and Flutter in `packages/`.
4. **Documentation**: Clarify guides in `docs/`, expand examples in `examples/`, or fix typos.

---

## Development Workflow

### 1. Fork & Clone

```bash
git clone https://github.com/crine-in/all-religious-texts.git
cd all-religious-texts
```

### 2. Environment Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Making Changes

* Use descriptive branch names: `feat/add-tei-parser`, `fix/verse-schema-validation`, `docs/update-api-spec`.
* Adhere to strict naming conventions:
  * Directories: `lowercase-kebab-case`
  * Schemas: `name.schema.json`
  * Python files: `snake_case.py`
  * JSON master metadata: `lowercase-plural.json`

### 4. Running Validation & Tests

Before submitting a Pull Request, all validation scripts and unit tests must pass:

```bash
python3 validators/run_all.py
pytest tests/
```

### 5. Commit Standards

We enforce Conventional Commits:

```text
feat(schema): add support for alternate verse numbering in verse.schema.json
fix(validator): resolve UTF-8 encoding issue on Windows paths
docs(api): update OpenAPI spec for verse search pagination
```

### 6. Submitting a Pull Request

* Fill out the PR template completely.
* Link related GitHub issues.
* Ensure CI checks pass cleanly.

---

## Questions?

Feel free to open an issue or start a GitHub Discussion on [github.com/crine-in/all-religious-texts](https://github.com/crine-in/all-religious-texts).

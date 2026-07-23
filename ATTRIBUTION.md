# ATTRIBUTION & PROVENANCE STANDARDS

**Organization**: CRINE ([github.com/crine-in](https://github.com/crine-in) | [www.crine.in](https://www.crine.in))

---

## Mission

Transparency and scholarly rigor are foundational pillars of the **All Religious Texts (ART)** ecosystem. Every scripture, commentary, translation, and metadata record cataloged in this ecosystem must provide complete, verifiable provenance.

---

## Attribution Requirements

When importing or contributing any textual edition to an ART ecosystem repository:

1. **Source Transparency**: Provide direct URLs to digital archives (e.g. GRETIL, Internet Archive, Sacred Texts Archive, Perseus Digital Library, Wikisource, GitHub repositories).
2. **Translator & Editor Credit**: Explicitly state translators, commentators, and digital transcription editors.
3. **Edition History**: Note the specific print or digital edition, recension, manuscript family, or critical edition used.
4. **Digitization Notes**: Document any automated OCR, spelling normalization, character encoding conversions (e.g., ASCII to UTF-8, Velthuis to IAST), or verse alignment adjustments made during ingestion.

---

## Standard Attribution Schema

Every dataset folder must include an `ATTRIBUTION.md` alongside its `metadata.json`:

```markdown
# Attribution & Provenance: [Text Title]

## Original Source
* **Title**: Katha Upanishad
* **Author / Attributed To**: Sage Katha (Traditional)
* **Language**: Sanskrit
* **Script**: IAST (International Alphabet of Sanskrit Transliteration)

## Digital Source & Provenance
* **Source Archive**: Digital Corpus of Sanskrit / GRETIL
* **Source URL**: http://gretil.sub.uni-goettingen.de/
* **Retrieval Date**: 2026-07-23
* **License**: Public Domain

## Processing Notes
* Converted to standardized UTF-8 JSON schema using `tools/txt_to_json.py`.
* Verified verse numbering matches 1.1.1 to 2.3.18.
```

---

## Academic & Open Source Credits

The ART ecosystem acknowledges and thanks pioneering open-access archives:
* **GRETIL** (Göttingen Register of Electronic Texts in Indian Languages)
* **Sacred Texts Archive** (Internet Sacred Text Archive)
* **Project Gutenberg**
* **Wikisource**
* **Perseus Digital Library** (Tufts University)
* **SuttaCentral** (Early Buddhist Texts)
* **Tanzil Project** (Quranic Arabic Text)
* **Sefaria** (Jewish Library)

---

## Citing ART in Research or Applications

When using datasets or schemas from the ART ecosystem in academic papers, websites, or software applications, please cite:

```text
CRINE. (2026). All Religious Texts (ART) Ecosystem Specification & Standardized Archive. 
GitHub: https://github.com/crine-in/all-religious-texts 
Website: https://www.crine.in
```

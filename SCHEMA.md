# SCHEMA SPECIFICATION OVERVIEW

**Organization**: CRINE ([github.com/crine-in](https://github.com/crine-in) | [www.crine.in](https://www.crine.in))

---

## Universal Schema Architecture

The **All Religious Texts (ART)** ecosystem uses strict [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/release-notes) definitions to guarantee machine readability, structural predictability, and API readiness across all sacred literature.

Schemas are located in `schemas/`:

| Schema File | Purpose |
| :--- | :--- |
| **`verse.schema.json`** | Canonical representation of individual verses, lines, or stanzas. |
| **`book.schema.json`** | Structural metadata for a sacred book, scripture, or treatise. |
| **`translation.schema.json`** | Metadata and alignment for translations across languages. |
| **`commentary.schema.json`** | Exegesis, commentary, and scholia linked to verses. |
| **`metadata.schema.json`** | Master book-level metadata, provenance, and license details. |
| **`license.schema.json`** | Licensing and copyright status validation. |
| **`cross-reference.schema.json`**| Parallel verses, thematic connections, and inter-textual links. |
| **`contributor.schema.json`** | Scholar, translator, editor, and archivist metadata. |
| **`language.schema.json`** | ISO 639-1 / 639-3 language metadata. |
| **`script.schema.json`** | ISO 15924 script codes and transliteration standards. |
| **`edition.schema.json`** | Manuscript, critical edition, and recension tracking. |

---

## 1. Universal Verse Schema Structure

### Core Fields

```json
{
  "id": "string (Required - Universal identifier, e.g. hinduism:upanishads:katha:1.1.1)",
  "externalId": "integer (Required - Sequential index within file)",
  "religion": "string (Required - Registered religion name)",
  "collection": "string (Required - Collection name)",
  "book": "string (Required - Book title)",
  "canto": "integer | null (Optional)",
  "chapter": "integer (Required - Chapter number)",
  "section": "integer | null (Optional)",
  "verse": "integer (Required - Verse number within chapter)",
  "subVerse": "integer | null (Optional - Line or sub-verse stanza)",
  "citation": "string (Required - Standard textual citation string, e.g. '1.1.1')",
  "language": "string (Required - Language name)",
  "script": "string (Required - Script code or name)",
  "text": "string (Required - Complete text of the verse)",
  "license": "string (Required - Text license)",
  "source": "string (Required - Source archive/edition)",
  "attribution": "string | null (Optional)",
  "translator": "string | null (Optional)",
  "edition": "string | null (Optional)",
  "checksum": "string (Required - SHA-256 hash of verse text)",
  "lastUpdated": "string (ISO 8601 Timestamp)"
}
```

### Advanced Optional Extension Fields

* **`footnotes`**: Array of footnote strings or objects.
* **`crossReferences`**: Array of target verse IDs or citations.
* **`audio`**: Audio file references (URL or path).
* **`embedding`**: Vector embedding vector (array of floats) for RAG/semantic search.
* **`keywords`**: Semantic keywords or tags.

---

## 2. Validation

All files in `data/` across ecosystem repos must validate against `schemas/verse.schema.json` and `schemas/metadata.schema.json`.

To run schema validation locally:

```bash
python3 validators/validate_schema.py
```

# Initialize the `all-religious-texts` Repository

You are an elite Staff Software Engineer, Data Architect, Open Source Maintainer, Digital Archivist, DevOps Engineer, Technical Writer, and Information Architect.

Your objective is to create the complete foundation for a GitHub repository named:

# all-religious-texts

GitHub Organization:
**CRINE** (github/crine-in, www.crine.in)

Repository Description:

> The world's largest open-source collection of religious texts.

The repository should be engineered as if it will become one of GitHub's most important open datasets over the next 20+ years.

This is **not** simply a collection of text files.

It is a structured, standardized, developer-first, machine-readable digital archive of humanity's religious literature.

Think of it as:

* Project Gutenberg for religion
* Common Crawl for scriptures
* Unicode Consortium for sacred texts
* Linux Foundation quality standards
* Kubernetes-level documentation
* MDN-level developer experience

Everything must be production quality.

---

# CORE MISSION

Build the definitive open repository for:

* Sacred scriptures
* Canonical texts
* Religious literature
* Public-domain translations
* Creative Commons translations
* Metadata
* Cross references
* Verse mappings
* Multiple scripts
* Multiple languages
* APIs
* Validation
* Search
* AI applications
* Academic research
* Mobile apps
* Websites
* LLMs

The repository should eventually support every religion and every publicly distributable sacred text.

---

# PHILOSOPHY

The repository should always prioritize:

Consistency

Accuracy

Source transparency

Licensing clarity

Developer friendliness

Machine readability

Human readability

Long-term maintainability

Backward compatibility

Community contributions

Documentation

Predictable structure

Scalability

---

# LICENSE

Repository

MIT License

Original metadata created by this repository

CC BY 4.0

Imported texts

Must preserve their original licenses.

Never overwrite licenses.

Never assume texts are public domain.

Every imported work must include:

* source
* attribution
* license
* provenance
* retrieval date
* conversion notes

---

# DIRECTORY STRUCTURE

Design a clean enterprise-grade repository.

The AI should improve this where appropriate.

```text
all-religious-texts/

README.md
LICENSE
ATTRIBUTION.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
ROADMAP.md
CHANGELOG.md
DATA_LICENSE.md
SCHEMA.md

.github/
docs/
schemas/
scripts/
validators/
tools/
tests/
examples/
api/
packages/
metadata/
data/
```

Every directory should have a clearly documented purpose.

---

# DATA STRUCTURE

Hierarchy

Religion

↓

Collection

↓

Book

↓

Language

↓

Script

↓

Edition

↓

Translation

↓

Verse Data

Example

```text
data/

hinduism/

upanishads/

katha-upanishad/

metadata.json

LICENSE

ATTRIBUTION.md

sources.md

iast.json

devanagari.json

english/

max-muller.json

swami-gambhirananda.json
```

This hierarchy should scale indefinitely.

---

# SUPPORTED RELIGIONS

Initialize folders for major traditions including:

Hinduism

Buddhism

Jainism

Sikhism

Christianity

Islam

Judaism

Zoroastrianism

Baháʼí Faith

Taoism

Confucianism

Shinto

Ancient Egyptian Religion

Greek Religion

Roman Religion

Norse Religion

Chinese Folk Religion

African Traditional Religions

Indigenous Traditions

Other Religions

The architecture should support unlimited future additions.

---

# SUPPORTED COLLECTIONS

Examples

Vedas

Upanishads

Bhagavad Gita

Mahabharata

Ramayana

Puranas

Agamas

Tantras

Tripitaka

Dhammapada

Guru Granth Sahib

Bible

Quran

Hadith

Torah

Mishnah

Talmud

Avesta

Tao Te Ching

Analects

Book of Mormon

Dead Sea Scrolls

Nag Hammadi Library

Apocrypha

Many more.

---

# UNIVERSAL VERSE SCHEMA

Design a schema that works for every religion.

Example

```json
{
    "id": 1,
    "externalId": 1,
    "book": "Katha Upanishad",
    "religion": "Hinduism",
    "collection": "Principal Upanishads",
    "chapter": 1,
    "section": 1,
    "verse": 1,
    "citation": "1.1",
    "language": "Sanskrit",
    "script": "IAST",
    "text": "...",
    "license": "Public Domain",
    "source": "...",
    "translator": null,
    "edition": null
}
```

Support optional fields for:

footnotes

cross references

parallel verses

alternate numbering

keywords

themes

commentary

audio

images

AI embeddings

semantic IDs

UUIDs

---

# BOOK METADATA

Each scripture should contain:

title

original title

alternate names

religion

collection

language

script

author

traditional attribution

date

era

place of origin

canonical status

chapters

sections

verses

recension

edition

license

source

contributors

checksum

last updated

---

# SCHEMAS

Generate JSON Schemas for:

verse

book

translation

commentary

metadata

license

cross references

contributors

language

script

edition

All schemas must validate automatically.

---

# VALIDATION

Generate validation tools that verify:

JSON validity

schema compliance

duplicate IDs

duplicate citations

missing verses

invalid numbering

UTF-8 encoding

newline consistency

filename consistency

folder consistency

license fields

source fields

metadata completeness

Run these through GitHub Actions.

---

# TOOLING

Create utilities for:

TXT → JSON

XML → JSON

HTML → JSON

Markdown → JSON

CSV → JSON

TEI XML → JSON

EPUB parsing

PDF metadata extraction

JSON formatting

Verse numbering

Schema validation

License validation

Broken links

Checksum generation

Bulk conversion

---

# DOCUMENTATION

Generate production-quality documentation.

README

Architecture

Folder Structure

Schemas

Contributing

Adding New Scriptures

Adding New Languages

Licensing

Validation

API

Examples

FAQ

Roadmap

Developer Guide

Style Guide

Data Standards

Documentation should be clear enough for a first-time contributor to add a new text without external guidance.

---

# CONTRIBUTING

Write extensive contribution guidelines covering:

Repository philosophy

Naming conventions

Directory layout

Formatting rules

Commit standards

Pull request requirements

Licensing requirements

Source verification

Review process

Validation process

---

# API

Prepare the repository for a future REST API.

Document endpoints such as:

/religions

/collections

/books

/books/{id}

/verses

/search

/random

/translations

/commentaries

Do not implement the backend yet.

Only provide specifications and examples.

---

# SEARCH

Design metadata suitable for:

SQLite

PostgreSQL

ElasticSearch

Meilisearch

Typesense

Vector databases

Semantic search

Full-text search

---

# PACKAGES

Prepare the repository to later publish:

JavaScript SDK

Python SDK

Go SDK

Rust SDK

Flutter package

without restructuring the repository.

---

# GITHUB

Configure:

Issue templates

Feature request template

Bug report template

Pull request template

Labels

CODEOWNERS

Dependabot

GitHub Actions

Automatic validation

Automatic formatting

Automatic release generation

---

# QUALITY STANDARDS

Everything should pass:

JSON Schema validation

Markdown lint

Link validation

UTF-8 validation

File naming validation

Folder naming validation

Spell check

Formatting checks

---

# STYLE GUIDE

Use:

lowercase folders

kebab-case

UTF-8 everywhere

Unix newlines

Consistent indentation

Predictable filenames

Stable identifiers

Deterministic ordering

Avoid duplication wherever possible.

---

# FUTURE ROADMAP

Architect the repository so it can later support:

Millions of verses

Thousands of books

Hundreds of languages

Thousands of contributors

Large media assets (kept in separate repositories)

AI embeddings

SQL Databases

Knowledge graphs

Linked Open Data

RDF exports

GraphQL

REST APIs

Offline datasets

Dataset releases

Docker images

NPM packages

PyPI packages

Crates.io packages

Static documentation site

Interactive website

---

# OUTPUT

Generate the repository as if it is ready to be published immediately.

Produce:

* Complete directory tree
* Repository documentation
* Every Markdown file
* JSON Schemas
* Example datasets
* Validation scripts
* GitHub Actions workflows
* Issue templates
* Pull request templates
* Metadata standards
* Style guides
* Contributor documentation
* Architecture documentation
* Roadmap
* Licensing documentation
* API specifications
* Sample conversion utilities

The result should resemble a mature open-source foundation project rather than a newly created repository. Every generated file should be internally consistent, production-ready, and immediately usable.

# Repository Ecosystem

This repository is the **foundational repository** for the entire **All Religious Texts (ART)** ecosystem.

It defines the universal standards, schemas, directory conventions, metadata specifications, validation rules, licensing guidelines, documentation standards, and contributor workflows that every future repository must follow.

This repository itself should contain representative datasets and examples, but it is **not intended to permanently store every religious text**. Instead, it serves as the canonical specification and entry point for the ecosystem.

Future repositories will inherit the standards established here. Examples include:

* `art-hinduism`
* `art-buddhism`
* `art-jainism`
* `art-sikhism`
* `art-christianity`
* `art-islam`
* `art-judaism`
* `art-zoroastrianism`
* `art-taoism`
* `art-confucianism`
* `art-shinto`
* `art-indigenous`
* `art-translations`
* `art-audio`
* `art-manuscripts`

Every repository in the ART ecosystem must remain fully compatible with the schemas, validation tools, metadata standards, licensing model, and directory conventions defined by this repository. Any future changes to these standards should originate here and propagate throughout the ecosystem.

Design this repository as if it were the equivalent of a language specification or protocol standard: stable, well-documented, versioned, backward-compatible whenever practical, and trusted as the authoritative reference implementation for all ART repositories.

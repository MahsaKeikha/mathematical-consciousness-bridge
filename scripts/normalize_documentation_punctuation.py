"""Normalize forbidden Unicode dash punctuation in reader-facing documentation.

The public documentation contract intentionally avoids Unicode en dash and em dash
characters. Reader-facing Markdown, HTML, SVG, and text files use the ASCII hyphen
instead so generated and hand-edited publication surfaces stay consistent.

This normalizer deliberately does not trim or otherwise reformat whitespace. Generated
SVGs are byte-reproducible artifacts, and changing path-data spacing would create
publication drift unrelated to the punctuation policy.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"

FORBIDDEN_DASHES = ("\u2013", "\u2014")
DOCUMENT_SUFFIXES = {".md", ".html", ".svg", ".txt"}


def documentation_files() -> list[Path]:
    files: list[Path] = []
    for name in ("README.md", "START_HERE.md", "CITATION.md"):
        path = ROOT / name
        if path.exists():
            files.append(path)

    for base in (DOCS, WEBSITE):
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and path.suffix.lower() in DOCUMENT_SUFFIXES:
                files.append(path)
    return sorted(set(files))


def normalize(text: str) -> str:
    for dash in FORBIDDEN_DASHES:
        text = text.replace(dash, "-")
    return text


def main() -> None:
    changed: list[str] = []
    for path in documentation_files():
        original = path.read_text(encoding="utf-8")
        updated = normalize(original)
        if updated == original:
            continue
        path.write_text(updated, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())

    if changed:
        print("[documentation] normalized forbidden dash punctuation:")
        for path in changed:
            print(f"  - {path}")
    else:
        print("[documentation] dash punctuation already normalized")


if __name__ == "__main__":
    main()

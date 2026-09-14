from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = {"\u2013": "EN DASH", "\u2014": "EM DASH"}


def documentation_files() -> list[Path]:
    files: list[Path] = []
    for name in ("README.md", "START_HERE.md", "CITATION.md"):
        path = ROOT / name
        if path.exists():
            files.append(path)

    for base_name in ("docs", "website"):
        base = ROOT / base_name
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".md", ".html", ".svg", ".txt"}:
                files.append(path)
    return sorted(set(files))


def test_reader_facing_documentation_has_no_en_dash_or_em_dash() -> None:
    violations: list[str] = []
    for path in documentation_files():
        text = path.read_text(encoding="utf-8")
        for char, label in FORBIDDEN.items():
            if char in text:
                line = text[: text.index(char)].count("\n") + 1
                violations.append(f"{path.relative_to(ROOT)}:{line}: {label}")
    assert not violations, "Forbidden Unicode dash characters found:\n" + "\n".join(violations)

"""Repair P89 navigation and normalize reader documentation punctuation."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"

FORBIDDEN_DASHES = ("\u2013", "\u2014")


def write_if_changed(path: Path, text: str, changed: list[str]) -> None:
    original = path.read_text(encoding="utf-8")
    if original != text:
        path.write_text(text, encoding="utf-8")
        changed.append(path.relative_to(ROOT).as_posix())


def repair_navigation(changed: list[str]) -> None:
    path = DOCS / "research_navigation.md"
    text = path.read_text(encoding="utf-8")

    if "For P89:" not in text:
        pattern = re.compile(
            r"For P88:\n\n\| What you want \| Direct link \|\n"
            r"\| --- \| --- \|\n.*?(?=\n\nP88 is a conditional model separation result)",
            re.DOTALL,
        )
        replacement = """For P89:\n\n| What you want | Direct link |\n| --- | --- |\n| The theorem and proof | [P89 proposition](proposition_89_complete_linear_parity_duality.md) |\n| Equation and method provenance | [P89 provenance](p89_equation_provenance.md) |\n| Implementation | [`complete_linear_parity_duality.py`](../src/consciousness_bridge/complete_linear_parity_duality.py) |\n| Regression tests | [`test_complete_linear_parity_duality.py`](../tests/test_complete_linear_parity_duality.py) |\n| Figure | [P89 theorem figure](figures/p89_complete_linear_parity_duality.svg) |\n| Repository reproduction | [Reproducibility Guide](reproducibility.md) |"""
        text, count = pattern.subn(replacement, text, count=1)
        if count != 1:
            raise RuntimeError("research navigation P88 audit block was not found")

    text = text.replace(
        "P88 is a conditional model separation result for the declared P75 target-measurement family. It does not identify the latent state with consciousness, establish nonphysicality, or close the final bridge from physical description to experience.",
        "P89 is a conditional model-separation result for the declared P75 target-measurement family. It closes the declared real linear parity-functional class only; it does not identify the latent state with consciousness, establish nonphysicality, exhaust nonlinear model constraints, or close the final bridge from physical description to experience.",
    )
    write_if_changed(path, text, changed)


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
            if path.is_file() and path.suffix.lower() in {".md", ".html", ".svg", ".txt"}:
                files.append(path)
    return sorted(set(files))


def normalize_documentation_punctuation(changed: list[str]) -> None:
    for path in documentation_files():
        text = path.read_text(encoding="utf-8")
        normalized = text
        for dash in FORBIDDEN_DASHES:
            normalized = normalized.replace(dash, "-")
        normalized = re.sub(r"[ \t]+(?=\n|$)", "", normalized)
        write_if_changed(path, normalized, changed)


def main() -> None:
    changed: list[str] = []
    repair_navigation(changed)
    normalize_documentation_punctuation(changed)
    if changed:
        print("[p89 repair] updated:")
        for path in changed:
            print(f"  - {path}")
    else:
        print("[p89 repair] already synchronized")


if __name__ == "__main__":
    main()

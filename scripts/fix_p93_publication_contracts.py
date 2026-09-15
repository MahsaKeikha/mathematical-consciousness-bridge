"""Narrow post-promotion fixes for the P93 publication migration.

This temporary feature-branch helper repairs exact reader-facing labels that
are outside the main P93 frontier block but are required by the canonical
figure publication synchronizer. It is deleted in the generated migration
commit and never reaches main.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _replace(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if old in text:
        text = text.replace(old, new)
        target.write_text(text, encoding="utf-8")


def main() -> None:
    _replace("website/index.html", "Explore all 92 results", "Explore all 93 results")
    _replace(
        "website/index.html",
        "P92 current theorem frontier · v0.82.0",
        "P93 current theorem frontier · v0.82.0",
    )
    print("[P93] narrow publication labels repaired")


if __name__ == "__main__":
    main()

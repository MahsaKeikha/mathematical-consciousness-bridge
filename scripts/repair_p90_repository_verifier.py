"""Advance stale repository-verifier figure contracts from P89 to P90."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "verify_repository.py"


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    replacements = (
        (
            '    if not current_figure.endswith(\n        "p89_complete_linear_parity_duality.svg"\n    ):\n        raise RuntimeError("figure manifest does not point to the canonical P88 SVG")',
            '    if not current_figure.endswith(\n        "p90_exact_nonlinear_rank_one_separation.svg"\n    ):\n        raise RuntimeError("figure manifest does not point to the canonical P90 SVG")',
        ),
        (
            '    p89 = visual_atlas.index(\'id="p89-frontier"\')\n    p88 = visual_atlas.index(\'id="p88-frontier"\')\n    p87 = visual_atlas.index(\'id="p87-frontier"\')\n    if not (p89 < p88 < p87):\n        raise RuntimeError("Visual Atlas does not lead with the current P89 figure")',
            '    p90 = visual_atlas.index(\'id="p90-frontier"\')\n    p89 = visual_atlas.index(\'id="p89-frontier"\')\n    p88 = visual_atlas.index(\'id="p88-frontier"\')\n    if not (p90 < p89 < p88):\n        raise RuntimeError("Visual Atlas does not lead with the current P90 figure")',
        ),
    )
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
    stale = (
        '"p89_complete_linear_parity_duality.svg"\n    ):\n        raise RuntimeError("figure manifest does not point to the canonical P88 SVG")',
        'Visual Atlas does not lead with the current P89 figure',
    )
    if any(token in text for token in stale):
        raise RuntimeError("stale P89 repository verifier figure contract remains")
    TARGET.write_text(text, encoding="utf-8")
    print("P90 repository verifier figure contracts repaired")


if __name__ == "__main__":
    main()

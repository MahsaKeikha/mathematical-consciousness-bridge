from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAILED_RECORD = ROOT / "docs" / "detailed_proposition_record.md"
VISUAL_ATLAS = ROOT / "website" / "visual-atlas.html"
VERIFY = ROOT / "scripts" / "verify_repository.py"


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _frontier() -> int:
    match = re.search(r'CURRENT_FRONTIER = "P(\d+)"', _text(VERIFY))
    assert match, "verify_repository.py must declare CURRENT_FRONTIER"
    return int(match.group(1))


def _version() -> str:
    match = re.search(r'CURRENT_VERSION = "([^"]+)"', _text(VERIFY))
    assert match, "verify_repository.py must declare CURRENT_VERSION"
    return match.group(1)


def test_readme_is_a_reader_first_scientific_front_door() -> None:
    text = _text(README)
    frontier = _frontier()
    required = (
        "# Mathematical Consciousness Bridge",
        "START_HERE.md",
        "docs/research_map.md",
        "docs/detailed_proposition_record.md",
        "docs/theorem_roadmap.md",
        "docs/figure_catalog.md",
        "docs/reproducibility.md",
        f"current public theorem frontier is **P{frontier}**",
        f"v{_version()}",
        "physical-to-experiential bridge",
        "The bridge remains an open scientific problem.",
    )
    for marker in required:
        assert marker in text, marker


def test_readme_keeps_scientific_architecture_and_current_frontier_visible() -> None:
    text = _text(README)
    frontier = _frontier()
    assert "docs/figures/research_architecture.svg" in text
    assert f"docs/figures/p{frontier}_" in text
    assert "Figure 1. Scientific architecture of the project." in text
    assert f"Figure 2. P{frontier}" in text
    assert "conditional model-separation theorem" in text
    assert "does not identify consciousness" in text


def test_complete_proposition_chronology_lives_in_detailed_record() -> None:
    text = _text(DETAILED_RECORD)
    frontier = _frontier()
    assert f"Complete P1 to P{frontier} chronology" in text
    for number in range(1, frontier + 1):
        assert re.search(rf"\bP{number}\b", text), f"P{number} missing from detailed record"


def test_visual_atlas_carries_the_full_figure_publication_layer() -> None:
    text = _text(VISUAL_ATLAS)
    frontier = _frontier()
    assert f"current-frontier-visual: P{frontier}" in text
    assert f'id="p{frontier}-frontier"' in text
    assert "How to read every figure" in text
    assert "Scientific status" in text


def test_readme_does_not_duplicate_the_full_technical_record() -> None:
    text = _text(README)
    assert "docs/detailed_proposition_record.md" in text
    assert "docs/theorem_roadmap.md" in text
    assert "docs/figure_catalog.md" in text
    assert text.count("## ") < 20
    assert "You do **not** need to read the propositions in order" in text

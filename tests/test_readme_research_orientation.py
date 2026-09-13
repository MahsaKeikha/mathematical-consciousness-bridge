import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = ROOT / "START_HERE.md"
DETAIL = ROOT / "docs/detailed_proposition_record.md"


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers)


def test_readme_is_compact_gateway_to_current_frontier():
    text = README.read_text(encoding="utf-8")
    assert len(text) < 12_000
    assert "The current public theorem frontier is **P88**" in text
    assert "formal release remains **v0.82.0**" in text
    for target in (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/figure_catalog.md",
        "docs/detailed_proposition_record.md",
        "docs/theorem_roadmap.md",
        "docs/reproducibility.md",
    ):
        assert target in text


def test_reader_gateway_preserves_scientific_boundaries():
    text = README.read_text(encoding="utf-8").lower()
    for phrase in (
        "does **not** claim",
        "proves that consciousness is nonphysical",
        "final bridge from physical description to experience has been solved",
        "bridge remains an open scientific problem",
    ):
        assert phrase in text


def test_detailed_record_tracks_complete_dynamic_frontier():
    detail = DETAIL.read_text(encoding="utf-8")
    frontier = _frontier()
    assert frontier == 88
    assert f"Complete P1 to P{frontier} chronology" in detail
    assert "Propositions **P1-P10**" in detail
    assert "**P88**" in detail
    assert "208,560 exact functionals" in detail
    assert "L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64" in detail


def test_start_here_matches_public_identity():
    text = START.read_text(encoding="utf-8")
    assert "88" in text
    assert "P88" in text
    assert "v0.82.0" in text

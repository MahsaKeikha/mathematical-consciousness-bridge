import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAIL = ROOT / "docs/detailed_proposition_record.md"
CATALOG = ROOT / "docs/figure_catalog.md"


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers)


def test_readme_routes_visual_depth_instead_of_embedding_full_atlas():
    text = README.read_text(encoding="utf-8")
    assert "docs/figure_catalog.md" in text
    assert "docs/detailed_proposition_record.md" in text
    assert "docs/theorem_roadmap.md" in text
    assert len(text) < 12_000


def test_figure_catalog_contains_current_frontier_figure_and_status():
    text = CATALOG.read_text(encoding="utf-8")
    assert "p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg" in text
    assert "208,560" in text
    assert "Scientific status." in text or "Scientific status:" in text


def test_detailed_proposition_chronology_reaches_dynamic_frontier():
    readme = README.read_text(encoding="utf-8")
    detail = DETAIL.read_text(encoding="utf-8")
    frontier = _frontier()
    assert frontier == 88
    assert "docs/detailed_proposition_record.md" in readme
    assert f"Complete P1 to P{frontier} chronology" in detail
    assert "**P88**" in detail


def test_readme_declares_scientific_status_boundaries():
    text = README.read_text(encoding="utf-8")
    required = (
        "does **not** claim",
        "proves that consciousness is nonphysical",
        "final bridge from physical description to experience has been solved",
        "The bridge remains an open scientific problem.",
    )
    for phrase in required:
        assert phrase in text

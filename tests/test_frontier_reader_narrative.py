import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"


def _frontier() -> int:
    numbers: list[int] = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def test_current_frontier_is_consistent_across_reader_surfaces() -> None:
    frontier = _frontier()
    previous = frontier - 1

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    homepage = (WEBSITE / "index.html").read_text(encoding="utf-8")
    atlas = (WEBSITE / "visual-atlas.html").read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    implementation = (WEBSITE / "implementation.html").read_text(encoding="utf-8")

    assert f"Public theorem frontier | **P{frontier}**" in readme
    assert f"Proposition-level results | **{frontier}**" in readme

    assert f"Explore all {frontier} results" in homepage
    assert f"<strong>{frontier}</strong><span>proposition-level results</span>" in homepage
    assert f"<strong>P{frontier}</strong><span>current theorem frontier</span>" in homepage
    assert f"The {frontier}-result program" in homepage
    assert f"P75-P{frontier}" in homepage
    assert f"P71-P{frontier}:" in homepage
    assert f"The {previous}-result program" not in homepage

    assert atlas.count("Current theorem frontier") == 1
    assert f"Current theorem frontier · P{frontier}" in atlas
    assert f"Current theorem frontier · P{previous}" not in atlas

    assert f"current documented theorem frontier is **P{frontier}**" in roadmap
    assert f"After P{frontier}" in roadmap
    assert f"current documented theorem frontier is **P{frontier}**" in navigation
    assert f"| P{frontier} |" in navigation
    assert f"P77-P{frontier}" in implementation


def test_current_frontier_figure_is_visible_on_homepage_and_visual_atlas() -> None:
    frontier = _frontier()
    homepage = (WEBSITE / "index.html").read_text(encoding="utf-8")
    atlas = (WEBSITE / "visual-atlas.html").read_text(encoding="utf-8")

    frontier_figures = sorted((DOCS / "figures").glob(f"p{frontier}_*.svg"))
    assert frontier_figures, f"no theorem figure found for P{frontier}"

    names = [path.name for path in frontier_figures]
    assert any(name in homepage for name in names)
    assert any(name in atlas for name in names)


def test_current_frontier_has_proof_provenance_and_navigation_links() -> None:
    frontier = _frontier()
    proposition_files = sorted(DOCS.glob(f"proposition_{frontier}_*.md"))
    assert len(proposition_files) == 1
    proof = proposition_files[0]

    provenance = DOCS / f"p{frontier}_equation_provenance.md"
    assert provenance.is_file()

    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    homepage = (WEBSITE / "index.html").read_text(encoding="utf-8")

    for surface in (navigation, roadmap, homepage):
        assert proof.name in surface
    assert provenance.name in navigation
    assert provenance.name in roadmap

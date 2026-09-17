from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIENTATION = (ROOT / "website" / "research-orientation.js").read_text(encoding="utf-8")
PAGE_LINKS = (ROOT / "website" / "research-iii-page-figures.js").read_text(encoding="utf-8")


def test_research_three_page_loads_results_link_enhancement() -> None:
    assert "function loadResearchIIIPageFigures()" in ORIENTATION
    assert "currentFile() !== 'measurement-science.html'" in ORIENTATION
    assert "research-iii-page-figures.js" in ORIENTATION
    assert "loadResearchIIIPageFigures();" in ORIENTATION


def test_research_three_page_links_to_complete_results_without_replacing_figures() -> None:
    assert "Open all Research III results and figures" in PAGE_LINKS
    assert "visual-atlas.html#research-iii-complete-figure-gallery" in PAGE_LINKS
    assert "Open complete Research III source record" in PAGE_LINKS
    assert "sources.html#research-iii-source-visual-anchor" in PAGE_LINKS
    assert "grid.innerHTML" not in PAGE_LINKS
    assert "All 9 canonical Research III scientific figures" not in PAGE_LINKS

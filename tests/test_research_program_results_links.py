from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIENTATION = (ROOT / "website" / "research-orientation.js").read_text(encoding="utf-8")
RESULT_LINKS = (ROOT / "website" / "research-results-links.js").read_text(encoding="utf-8")


def test_all_three_research_pages_load_results_links() -> None:
    assert "function loadResearchResultsLinks()" in ORIENTATION
    for page in (
        "observer-research.html",
        "research-map.html",
        "measurement-science.html",
    ):
        assert page in ORIENTATION
    assert "research-results-links.js" in ORIENTATION
    assert "loadResearchResultsLinks();" in ORIENTATION


def test_research_i_links_to_complete_current_record() -> None:
    assert "View all Research I results" in RESULT_LINKS
    assert "sources.html#research-i-source-program" in RESULT_LINKS
    assert "visual-atlas.html#research-i-complete-figure-gallery" in RESULT_LINKS
    assert "58 proposition-level results" in RESULT_LINKS


def test_research_ii_links_to_complete_p1_p100_navigator() -> None:
    assert "View all Research II results" in RESULT_LINKS
    assert "research-map.html#complete-proposition-navigator" in RESULT_LINKS
    assert "sources.html#complete-source-sequence" in RESULT_LINKS
    assert "P1-P100 proposition navigator" in RESULT_LINKS


def test_research_iii_links_to_complete_current_record() -> None:
    assert "View all Research III results" in RESULT_LINKS
    assert "sources.html#research-iii-source-program" in RESULT_LINKS
    assert "visual-atlas.html#research-iii-complete-figure-gallery" in RESULT_LINKS
    assert "measurement-science record" in RESULT_LINKS

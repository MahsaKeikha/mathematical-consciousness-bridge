from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_research_three_snapshot_banner_is_removed_only_at_render_time() -> None:
    script = _read("website/research-orientation.js")

    assert "function removeRedundantResearchThreeSnapshot()" in script
    assert "currentFile() !== 'measurement-science.html'" in script
    assert "Verified repository snapshot" in script
    assert "The public page is pinned to the completed foundational framework" in script
    assert "section.remove();" in script
    assert "removeRedundantResearchThreeSnapshot();" in script


def test_research_three_source_content_remains_intact() -> None:
    page = _read("website/measurement-science.html")

    # The source remains auditable and synchronized; only the redundant visual
    # banner is removed from the rendered Research III page.
    assert "Verified repository snapshot" in page
    assert "Central measurement question" in page
    assert "Five measurement targets" in page
    assert "Consciousness Evidence Profile" in page
    assert "Phenomenal structure measurement" in page
    assert "Software and reproducibility" in page
    assert "3cf9202977953644c980246c1f3e46a3514b3a4a" in page


def test_banner_removal_does_not_apply_to_other_reader_pages() -> None:
    script = _read("website/research-orientation.js")

    start = script.index("function removeRedundantResearchThreeSnapshot()")
    end = script.index("function renderScientificOrientation()")
    function_body = script[start:end]

    assert "measurement-science.html" in function_body
    assert "observer-research.html" not in function_body
    assert "research-map.html" not in function_body
    assert "visual-atlas.html" not in function_body

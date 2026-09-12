from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_shared_reader_experience_style_is_built_into_pages() -> None:
    css = _text("website/reader-experience-v2.css")
    prepare = _text("scripts/prepare_website.py")
    assert "--figure-reading-max: 980px" in css
    assert "max-height: min(72vh" in css
    assert ".reader-primer-grid" in css
    assert "READER_EXPERIENCE_STYLE_TAG" in prepare
    assert '"reader-experience-v2.css"' in prepare


def test_first_reader_surfaces_match_p84_frontier() -> None:
    start = _text("website/start-here.html")
    research_map = _text("website/research-map.html")
    assert "The 84 propositions by scientific role" in start
    assert "You do not need to read 84 proofs in order" in start
    assert "complete 84-result dependency structure" in start
    assert "Physical descriptor" in start
    assert "Observation channel" in start
    assert "through Proposition 84" in research_map
    assert "Eighty-four results" in research_map
    assert "<strong>84</strong>" in research_map
    assert "P73-P84" in research_map


def test_visual_atlas_uses_public_paths_and_readable_display_rules() -> None:
    atlas = _text("website/visual-atlas.html")
    assert "../docs/" not in atlas
    assert "Figures are intentionally capped at a readable page size" in atlas
    assert "p81_projection_event_model_separation.svg" in atlas
    assert 'loading="lazy"' in atlas
    assert "theorem-figure-shell" in atlas


def test_reader_and_figure_standards_are_documented() -> None:
    reader = _text("docs/reader_experience_and_visual_standard.md")
    figures = _text("docs/figure_caption_and_description_standard.md")
    assert "## Visual size standard" in reader
    assert "## Display-size standard" in figures
    assert "760 to 980 CSS pixels" in reader
    assert "Never solve overflow by making text tiny" in reader

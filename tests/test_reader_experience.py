import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _frontier() -> int:
    verifier = _text("scripts/verify_repository.py")
    match = re.search(r'CURRENT_FRONTIER = "P(\d+)"', verifier)
    assert match
    return int(match.group(1))


def test_shared_reader_experience_style_is_built_into_pages() -> None:
    css = _text("website/reader-experience-v2.css")
    prepare = _text("scripts/prepare_website.py")
    assert "--figure-reading-max: 980px" in css
    assert "max-height: min(72vh" in css
    assert ".reader-primer-grid" in css
    assert "READER_EXPERIENCE_STYLE_TAG" in prepare
    assert '"reader-experience-v2.css"' in prepare
    assert "Site-wide grid containment contract:" in css
    assert ".implementation-links > *" in css
    assert "overflow-wrap: anywhere" in css


def test_first_reader_surfaces_match_current_frontier() -> None:
    current = _frontier()
    start = _text("website/start-here.html")
    research_map = _text("website/research-map.html")
    plain = _text("website/plain-language.html")

    assert f"the {current}-result theorem program and current P{current} frontier" in start
    assert f"<strong>{current}</strong><span>proposition-level results</span>" in start
    assert f"<strong>P{current}</strong><span>current theorem frontier</span>" in start
    assert f"You do not need to read {current} proofs in order" in start
    assert f"complete {current}-result dependency structure" in start
    assert 'id="research-origin"' in start
    assert "10.1016/j.chaos.2015.03.014" in start
    assert "Physical descriptor" in start
    assert "Observation channel" in start

    assert f"through Proposition {current}" in research_map
    assert f"<strong>{current}</strong><span>proposition-level results</span>" in research_map
    assert f'id="p{current}-research-map"' in research_map

    assert f"<strong>{current}</strong><span>Research II proposition-level results</span>" in plain
    assert f"<strong>P{current}</strong><span>current Research II theorem frontier</span>" in plain
    assert f"What the {current} results are doing" in plain
    assert f"Current exact frontier · P{current}" in plain


def test_no_reader_facing_html_page_advertises_an_older_frontier_as_current() -> None:
    current = _frontier()
    offenders: dict[str, list[str]] = {}
    for path in sorted((ROOT / "website").glob("*.html")):
        text = path.read_text(encoding="utf-8")
        hits: list[str] = []
        for number in range(max(1, current - 5), current):
            stale_tokens = (
                f"current P{number} frontier",
                f"Current frontier · P{number}",
                f"current theorem frontier</span>",
            )
            for token in stale_tokens[:2]:
                if token in text:
                    hits.append(token)
        if hits:
            offenders[path.name] = hits
    assert not offenders, offenders


def test_visual_atlas_uses_public_paths_and_readable_display_rules() -> None:
    atlas = _text("website/visual-atlas.html")
    assert "../docs/" not in atlas
    assert "Figures are intentionally capped at a readable page size" in atlas
    assert "p81_projection_event_model_separation.svg" in atlas
    assert 'loading="lazy"' in atlas
    assert "theorem-figure-shell" in atlas
    assert atlas.count("<h2>How to read every figure</h2>") == 1


def test_reader_and_figure_standards_are_documented() -> None:
    reader = _text("docs/reader_experience_and_visual_standard.md")
    figures = _text("docs/figure_caption_and_description_standard.md")
    assert "## Visual size standard" in reader
    assert "## Display-size standard" in figures
    assert "760 to 980 CSS pixels" in reader
    assert "Never solve overflow by making text tiny" in reader


def test_figure_enrichment_generator_preserves_canonical_reader_key() -> None:
    source = _text("scripts/enrich_figure_documentation.py")
    ast.parse(source)
    assert "legacy_reading_key" in source
    assert "reading_key" in source
    assert "Figures are intentionally capped at a readable page size" in source
    assert "reader_experience_and_visual_standard.md" in source
    assert 'text.replace(legacy_reading_key, reading_key, 1)' in source


def test_repository_verifier_tracks_current_frontier_and_complete_chain() -> None:
    current = _frontier()
    verifier = _text("scripts/verify_repository.py")
    assert f'CURRENT_FRONTIER = "P{current}"' in verifier
    assert f"for number in range(1, {current + 1}):" in verifier
    assert '"docs/reader_experience_and_visual_standard.md"' in verifier
    assert f'"docs/proposition_{current}_' in verifier

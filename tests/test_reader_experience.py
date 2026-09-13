import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def _frontier() -> int:
    numbers: list[int] = []
    for path in (ROOT / "docs").glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


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
    frontier = _frontier()
    start = _text("website/start-here.html")
    research_map = _text("website/research-map.html")
    plain = _text("website/plain-language.html")

    assert f"{frontier}-result theorem program and current P{frontier} frontier" in start
    assert f"P78-P{frontier} progressively tighten global separation" in start
    assert f"P{frontier} is the current exact frontier." in start
    assert f">Read P{frontier}</a>" in start
    assert 'id="research-origin"' in start
    assert "10.1016/j.chaos.2015.03.014" in start
    assert f"The {frontier} propositions by scientific role" in start
    assert f"You do not need to read {frontier} proofs in order" in start
    assert f"complete {frontier}-result dependency structure" in start
    assert "Physical descriptor" in start
    assert "Observation channel" in start

    assert f"through Proposition {frontier}" in research_map
    assert f"<strong>{frontier}</strong>" in research_map
    assert f"P73-P{frontier}" in research_map

    assert f"<strong>{frontier}</strong><span>proposition-level results</span>" in plain
    assert f"<strong>P{frontier}</strong><span>current theorem frontier</span>" in plain
    assert f"What the {frontier} results are doing" in plain
    assert f"P75-P{frontier}" in plain
    assert f"actual P{frontier} research frontier" in plain
    assert f"shows how all {frontier} results connect" in plain


def test_no_reader_facing_html_page_advertises_older_frontier_as_current() -> None:
    frontier = _frontier()
    stale_current_frontier_tokens: list[str] = []
    for number in range(84, frontier):
        stale_current_frontier_tokens.extend(
            (
                f"{number}-result theorem program and current P{number} frontier",
                f"<strong>P{number}</strong><span>current theorem frontier</span>",
                f"current P{number} frontier",
                f"actual P{number} research frontier",
                f"What the {number} results are doing",
                f"shows how all {number} results connect",
                f"The {number} propositions by scientific role",
                f"complete {number}-result dependency structure",
                f"You do not need to read {number} proofs in order",
            )
        )

    offenders: dict[str, list[str]] = {}
    for path in sorted((ROOT / "website").glob("*.html")):
        text = path.read_text(encoding="utf-8")
        hits = [token for token in stale_current_frontier_tokens if token in text]
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


def test_repository_verifier_tracks_current_frontier_and_all_propositions() -> None:
    frontier = _frontier()
    verifier = _text("scripts/verify_repository.py")
    assert f'CURRENT_FRONTIER = "P{frontier}"' in verifier
    assert (
        f"for number in range(1, {frontier + 1}):" in verifier
        or "for number in range(1, int(CURRENT_FRONTIER[1:]) + 1):" in verifier
    )
    assert '"docs/reader_experience_and_visual_standard.md"' in verifier
    assert f'"docs/proposition_{frontier}_' in verifier

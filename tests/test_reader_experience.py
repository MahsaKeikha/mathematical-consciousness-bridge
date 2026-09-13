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


def test_reader_first_surfaces_match_current_frontier_without_becoming_archives() -> None:
    frontier = _frontier()
    readme = _text("README.md")
    start = _text("START_HERE.md")
    website_home = _text("website/index.html")
    website_start = _text("website/start-here.html")
    research_map = _text("website/research-map.html")

    for source in (readme, start, website_home, website_start, research_map):
        assert f"P{frontier}" in source
        assert "physical-to-experiential bridge" in source.lower()

    assert len(readme.encode("utf-8")) < 25000
    assert len(start.encode("utf-8")) < 25000
    assert "Start in one click" in readme
    assert "Start with the question, not the 88 propositions" in website_start
    assert "See the scientific structure without reading 88 proofs in order" in research_map

    # The public landing pages should feature the current frontier, not stack
    # several historical frontier graphics at equal visual weight.
    assert website_home.count("p88_heldout_selected_parity_functional_certification.svg") >= 1
    assert "p87_exact_bounded_primitive_quad_projection_parity.svg" not in website_home
    assert "p86_exact_minimally_weighted_quad_projection_parity.svg" not in website_home


def test_first_reader_surfaces_offer_progressive_disclosure_routes() -> None:
    readme = _text("README.md")
    start = _text("START_HERE.md")
    home = _text("website/index.html")

    required_readme_routes = (
        "START_HERE.md",
        "docs/research_architecture.md",
        "docs/research_traceability_index.md",
        "docs/theorem_roadmap.md",
        "docs/figure_catalog.md",
        "docs/reproducibility.md",
    )
    for route in required_readme_routes:
        assert route in readme

    for token in (
        "scientific question",
        "assumptions",
        "theorem",
        "implementation",
        "tests",
        "provenance",
        "scientific boundary",
    ):
        assert token in start.lower()

    assert "Start with the idea" in home
    assert "Explore the research map" in home
    assert "Browse the visual atlas" in home
    assert "Traceability Index" in home


def test_no_reader_facing_html_page_advertises_older_frontier_as_current() -> None:
    frontier = _frontier()
    stale_current_frontier_tokens: list[str] = []
    for number in range(1, frontier):
        stale_current_frontier_tokens.extend(
            (
                f"current P{number} frontier",
                f"current theorem frontier · P{number}",
                f"Current theorem frontier: P{number}",
                f"<strong>P{number}</strong><span>current theorem frontier</span>",
            )
        )

    offenders: dict[str, list[str]] = {}
    for path in sorted((ROOT / "website").glob("*.html")):
        text = path.read_text(encoding="utf-8")
        hits = [token for token in stale_current_frontier_tokens if token in text]
        if hits:
            offenders[path.name] = hits
    assert not offenders, offenders


def test_reader_and_publication_standards_are_documented() -> None:
    reader = _text("docs/reader_experience_and_visual_standard.md")
    figures = _text("docs/figure_caption_and_description_standard.md")
    publication = _text("docs/publication_page_standard.md")

    assert "## Visual size standard" in reader
    assert "## Display-size standard" in figures
    assert "rigor should increase as the reader goes deeper" in publication
    assert "## 2. Use progressive disclosure" in publication
    assert "theorem → provenance → implementation → tests → figure → reproduction" in publication
    assert "## 12. The homepage is not the archive" in publication


def test_visual_atlas_remains_the_deep_visual_archive() -> None:
    atlas = _text("website/visual-atlas.html")
    assert "../docs/" not in atlas
    assert "Figures are intentionally capped at a readable page size" in atlas
    assert "p81_projection_event_model_separation.svg" in atlas
    assert 'loading="lazy"' in atlas
    assert "theorem-figure-shell" in atlas


def test_figure_enrichment_generator_preserves_canonical_reader_key() -> None:
    source = _text("scripts/enrich_figure_documentation.py")
    ast.parse(source)
    assert "legacy_reading_key" in source
    assert "reading_key" in source
    assert "Figures are intentionally capped at a readable page size" in source
    assert "reader_experience_and_visual_standard.md" in source


def test_repository_verifier_tracks_current_frontier_and_reader_standards() -> None:
    frontier = _frontier()
    verifier = _text("scripts/verify_repository.py")
    assert f'CURRENT_FRONTIER = "P{frontier}"' in verifier
    assert (
        f"for number in range(1, {frontier + 1}):" in verifier
        or "for number in range(1, int(CURRENT_FRONTIER[1:]) + 1):" in verifier
    )
    assert '"docs/reader_experience_and_visual_standard.md"' in verifier

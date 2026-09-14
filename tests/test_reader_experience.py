import ast
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
    assert "Site-wide grid containment contract:" in css
    assert ".implementation-links > *" in css
    assert "overflow-wrap: anywhere" in css


def test_first_reader_surfaces_match_p88_frontier() -> None:
    start = _text("website/start-here.html")
    research_map = _text("website/research-map.html")
    plain = _text("website/plain-language.html")

    assert "88-result theorem program and current P88 frontier" in start
    assert "P78-P88 progressively tighten global separation" in start
    assert "P88 is the current exact frontier." in start
    assert "Current frontier · P85" not in start
    assert "Current theorem frontier · P86" not in start
    assert "L85 = 0 &lt; L86 = 1/192" in start
    assert ">Read P88</a>" in start
    assert 'id="research-origin"' in start
    assert "10.1016/j.chaos.2015.03.014" in start
    assert "The 88 propositions by scientific role" in start
    assert "You do not need to read 88 proofs in order" in start
    assert "complete 88-result dependency structure" in start
    assert "Physical descriptor" in start
    assert "Observation channel" in start

    assert "through Proposition 88" in research_map
    assert "Eighty-eight results" in research_map
    assert "<strong>88</strong>" in research_map
    assert "P73-P88" in research_map

    assert "<strong>88</strong><span>Research II proposition-level results</span>" in plain
    assert "<strong>P88</strong><span>current Research II theorem frontier</span>" in plain
    assert "What the 88 results are doing" in plain
    assert "P75-P88" in plain
    assert "actual P88 research frontier" in plain
    assert "shows how all 88 results connect" in plain

    stale = (
        "87-result theorem program and current P87 frontier",
        "<strong>87</strong><span>proposition-level results</span>",
        "<strong>P87</strong><span>current theorem frontier</span>",
        "actual P87 research frontier",
    )
    for token in stale:
        assert token not in start
        assert token not in research_map
        assert token not in plain


def test_no_reader_facing_html_page_advertises_pre_p88_as_current() -> None:
    stale_current_frontier_tokens = (
        "87-result theorem program and current P87 frontier",
        "Current theorem frontier · P87",
        "<strong>87</strong><span>proposition-level results</span>",
        "<strong>P87</strong><span>current theorem frontier</span>",
        "current P87 frontier",
        "actual P87 research frontier",
        "What the 87 results are doing",
        "shows how all 87 results connect",
        "through Proposition 87",
        "Eighty-seven results",
        "The 87 propositions by scientific role",
        "complete 87-result dependency structure",
        "You do not need to read 87 proofs in order",
        "86-result theorem program and current P86 frontier",
        "Current theorem frontier · P86",
        "<strong>86</strong><span>proposition-level results</span>",
        "<strong>P86</strong><span>current theorem frontier</span>",
        "current P86 frontier",
        "actual P86 research frontier",
        "What the 86 results are doing",
        "shows how all 86 results connect",
        "through Proposition 86",
        "Eighty-six results",
        "The 86 propositions by scientific role",
        "complete 86-result dependency structure",
        "You do not need to read 86 proofs in order",
        "Current frontier · P85",
        "<strong>85</strong><span>proposition-level results</span>",
        "<strong>P85</strong><span>current theorem frontier</span>",
        "current P85 frontier",
        "actual P85 research frontier",
        "What the 85 results are doing",
        "shows how all 85 results connect",
        "through Proposition 85",
        "Eighty-five results",
        "Open all 85 results",
        "The 85 propositions by scientific role",
        "complete 85-result dependency structure",
        "You do not need to read 85 proofs in order",
        "<strong>84</strong><span>proposition-level results</span>",
        "<strong>P84</strong><span>current theorem frontier</span>",
        "current P84 frontier",
        "actual P84 research frontier",
        "What the 84 results are doing",
        "shows how all 84 results connect",
        "shows how all 83 results connect",
        "through Proposition 84",
        "Eighty-four results",
        "Open all 84 results",
        "The 84 propositions by scientific role",
        "complete 84-result dependency structure",
        "You do not need to read 84 proofs in order",
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


def test_repository_verifier_tracks_p88_and_all_88_propositions() -> None:
    verifier = _text("scripts/verify_repository.py")
    assert 'CURRENT_FRONTIER = "P88"' in verifier
    assert "for number in range(1, 89):" in verifier
    assert '"docs/reader_experience_and_visual_standard.md"' in verifier
    assert '"docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md"' in verifier


def test_overview_orients_first_time_reader_before_theorem_frontier() -> None:
    overview = _text("website/index.html")
    assert overview.count('id="project-journey"') == 1
    assert overview.index('id="project-journey"') < overview.index('id="p88-frontier"')
    assert "The whole research program in three stages" in overview
    assert "<span>Research I</span>" in overview
    assert "<span>Research II</span>" in overview
    assert "<span>Research III</span>" in overview
    assert "Research I identifies a physical subsystem candidate" in overview
    assert "None of these stages by itself establishes the final physical-to-experiential bridge." in overview

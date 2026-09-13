import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MAP = ROOT / "website/research-map.html"
HOME = ROOT / "website/index.html"
START = ROOT / "website/start-here.html"


def _frontier() -> int:
    numbers: list[int] = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def test_research_map_starts_with_orientation_before_deep_layers():
    text = MAP.read_text(encoding="utf-8")
    hero = text.index('<section class="hero compact-hero">')
    orientation = text.index('id="orientation"')
    physical = text.index('id="physical-foundation"')
    target = text.index('id="target-side"')
    frontier = text.index('id="p88-reader-frontier"')
    assert hero < orientation < physical < target < frontier


def test_research_map_exposes_status_and_major_scientific_layers():
    text = MAP.read_text(encoding="utf-8")
    frontier = _frontier()
    required = [
        "Proved results",
        "Conditional results",
        "Open bridge target",
        "P1-P10",
        "P11-P18",
        "P19-P24",
        "P25-P44",
        "P45-P70",
        "P71-P74",
        "P75-P87",
        f"P{frontier}",
        "physical-to-experiential bridge",
    ]
    for token in required:
        assert token in text, token


def test_research_map_is_question_led_not_proposition_dump():
    text = MAP.read_text(encoding="utf-8")
    assert "What physical description are we actually talking about?" in text
    assert "Does the declared physical descriptor preserve every distinction" in text
    assert "Before testing a bridge, can the target itself be trusted?" in text
    assert "Can the declared target-measurement model actually reproduce the observed law?" in text
    assert "Can a discovery-selected result survive independent data?" in text
    assert "Complete proposition index" not in text


def test_research_map_gives_direct_audit_paths_without_listing_every_file():
    text = MAP.read_text(encoding="utf-8")
    required = [
        "research_traceability_index.md",
        "theorem_roadmap.md",
        "research_navigation.md",
        "equation_and_citation_map.md",
        "visual-atlas.html",
        "src/consciousness_bridge",
        "proposition_19_fundamental_physical_sufficiency.md",
        "proposition_71_target_provenance_noncircularity.md",
        "proposition_75_target_model_adequacy_overidentification.md",
        "proposition_78_certified_continuous_model_separation.md",
        "proposition_79_certified_sampling_radius.md",
        "p82_equation_provenance.md",
        "p83_equation_provenance.md",
        "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",
        "proposition_88_heldout_selected_parity_functional_certification.md",
    ]
    for token in required:
        assert token in text, token


def test_current_frontier_is_visually_unique_on_home_and_start_pages():
    frontier = _frontier()
    home = HOME.read_text(encoding="utf-8")
    start = START.read_text(encoding="utf-8")

    assert f"Current theorem frontier · P{frontier}" in home
    assert f"Current theorem frontier · P{frontier}" in start
    assert "p88_heldout_selected_parity_functional_certification.svg" in home
    assert "p88_heldout_selected_parity_functional_certification.svg" in start
    assert "p87_exact_bounded_primitive_quad_projection_parity.svg" not in home
    assert "p86_exact_minimally_weighted_quad_projection_parity.svg" not in home


def test_p88_reader_frontier_preserves_selection_and_box_specific_boundaries():
    text = MAP.read_text(encoding="utf-8")
    section = text[text.index('id="p88-reader-frontier"') : text.index("</main>")]
    assert "independent validation" in section
    assert "39,600-way functional union bound" in section
    assert "1063" in section
    assert "box-specific" in section
    assert "discovery/validation independence" in section


def test_start_page_preserves_research_origin_and_reader_primer():
    text = START.read_text(encoding="utf-8")
    assert 'id="reader-primer"' in text
    assert 'id="research-origin"' in text
    assert "10.1016/j.chaos.2015.03.014" in text
    assert "arXiv:1401.1219" in text
    assert "Physical descriptor" in text
    assert "Observation channel" in text

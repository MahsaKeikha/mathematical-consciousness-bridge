import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"
DOCS = ROOT / "docs"


def _frontier() -> int:
    numbers = []
    for path in DOCS.glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    assert numbers
    return max(numbers)


def test_research_map_starts_with_orientation_before_stage_details():
    text = MAP.read_text(encoding="utf-8")
    frontier = _frontier()
    hero = text.index(f"Eighty-four results, one dependency-aware scientific program")
    orientation = text.index("How to read this research")
    stage_one = text.index("I · Formal bridge foundations")
    assert frontier == 84
    assert hero < orientation < stage_one


def test_research_map_exposes_status_and_all_ten_stage_ranges():
    text = MAP.read_text(encoding="utf-8")
    required = [
        "Proved results",
        "Conditional results",
        "Open bridge target",
        "P1-P10",
        "P11-P18",
        "P19-P24",
        "P71",
        "P72",
        "P73-P76",
        "P25-P37",
        "P38-P44",
        "P45-P53",
        "P54-P70",
        "Ten-stage scientific path",
    ]
    for token in required:
        assert token in text, token


def test_research_map_gives_direct_audit_paths():
    text = MAP.read_text(encoding="utf-8")
    required = [
        "theorem_roadmap.md",
        "research_navigation.md",
        "equation_and_citation_map.md",
        "visual-atlas.html",
        "tests/",
        "src/consciousness_bridge/",
        "proposition_71_target_provenance_noncircularity.md",
        "proposition_72_target_measurement_channel_robustness.md",
        "proposition_73_target_channel_identifiability.md",
        "proposition_74_finite_sample_target_channel_recovery.md",
        "proposition_75_target_model_adequacy_overidentification.md",
        "proposition_76_finite_sample_target_model_adequacy.md",
        "proposition_77_full_law_model_set_separation.md",
        "proposition_78_certified_continuous_model_separation.md",
        "proposition_79_certified_sampling_radius.md",
        "proposition_80_simplex_coupled_model_separation.md",
        "proposition_81_projection_event_model_separation.md",
        "p82_equation_provenance.md",
        "proposition_82_exact_nested_projection_contrast.md",
        "p83_equation_provenance.md",
        "proposition_83_exact_projection_parity.md",
        "p84_equation_provenance.md",
        "proposition_84_exact_joint_projection_parity_contrast.md",
        "joint_projection_parity_contrast_separation.py",
        "test_joint_projection_parity_contrast_separation.py",
    ]
    for token in required:
        assert token in text, token


def test_research_map_presents_p77_through_current_frontier_in_dependency_order():
    text = MAP.read_text(encoding="utf-8")
    frontier_number = _frontier()
    assert f"through Proposition {frontier_number}" in text
    frontier = text.index('id="continuous-model-frontier"')

    positions = []
    for proposition in range(77, frontier_number + 1):
        positions.append(text.index(f"Open P{proposition} →", frontier))
    assert positions == sorted(positions)

    assert text.count("P78: Certified continuous P75 model separation") == 1
    assert text.count("How is P77 made rigorous for the continuous P75 family?") == 1
    assert "only the certified global lower bound can feed the P77 rejection gate" in text
    assert "Simplex coupling" in text
    assert "256 genuinely new residual events" in text
    assert "P81 = 1/16 to P82 = 1/12" in text
    assert "L82 = 0 and L83 = 1/16" in text
    assert "L83 = 0 and L84 = 1/32" in text
    assert "220 genuinely coupled contrasts" in text
    assert text.index('id="p84-frontier"') < text.index("</main>")


def test_p84_frontier_is_unique_and_structurally_inside_main():
    text = MAP.read_text(encoding="utf-8")
    main_open = text.index("<main>")
    main_close = text.index("</main>")
    p84 = text.index('id="p84-frontier"')
    assert text.count('id="p84-frontier"') == 1
    assert main_open < p84 < main_close
    assert "Open P84 →" not in text[main_close:]


def test_continuous_frontier_keeps_p82_p83_and_p84_provenance_auditable():
    text = MAP.read_text(encoding="utf-8")
    frontier = text.index('id="continuous-model-frontier"')
    main_close = text.index("</main>", frontier)
    frontier_text = text[frontier:main_close]
    assert "p82_equation_provenance.md" in frontier_text
    assert "p83_equation_provenance.md" in frontier_text
    assert "p84_equation_provenance.md" in frontier_text

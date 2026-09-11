from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"


def test_research_map_starts_with_orientation_before_stage_details():
    text = MAP.read_text(encoding="utf-8")
    hero = text.index("Eighty results, one dependency-aware scientific program")
    orientation = text.index("How to read this research")
    stage_one = text.index("I · Formal bridge foundations")
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
    ]
    for token in required:
        assert token in text, token


def test_research_map_presents_p77_through_p80_in_dependency_order():
    text = MAP.read_text(encoding="utf-8")
    assert "through Proposition 80" in text

    p77 = text.index("IV-G · Full-law model-set separation")
    p78 = text.index("IV-H · Certified continuous-family separation")
    p79 = text.index("IV-I · Certified sampling radius")
    p80 = text.index("IV-J · Tighter continuous-family relaxation")
    assert p77 < p78 < p79 < p80

    assert text.count("P78: How is P77 made rigorous for the continuous P75 family?") == 1
    assert "only the certified global lower bound can feed the P77 rejection gate" in text
    assert "P80 tightens the continuous lower bound" in text

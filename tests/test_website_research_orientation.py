from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"


def test_research_map_starts_with_orientation_before_stage_details():
    text = MAP.read_text(encoding="utf-8")
    hero = text.index("Eighty-two results, one dependency-aware scientific program")
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
        "p82_equation_provenance.md",
        "proposition_82_exact_nested_projection_contrast.md",
        "proposition_81_projection_event_model_separation.md",
    ]
    for token in required:
        assert token in text, token


def test_research_map_presents_p77_through_p82_in_dependency_order():
    text = MAP.read_text(encoding="utf-8")
    assert "through Proposition 82" in text
    frontier = text.index('id="continuous-model-frontier"')
    p77 = text.index("Open P77 →", frontier)
    p78 = text.index("Open P78 →", frontier)
    p79 = text.index("Open P79 →", frontier)
    p80 = text.index("Open P80 →", frontier)
    p81 = text.index("Open P81 →", frontier)
    p82 = text.index("Open P82 →", frontier)
    assert p77 < p78 < p79 < p80 < p81 < p82

    assert text.count("P78: Certified continuous P75 model separation") == 1
    assert text.count("How is P77 made rigorous for the continuous P75 family?") == 1
    assert "only the certified global lower bound can feed the P77 rejection gate" in text
    assert "Simplex coupling" in text
    assert "256 genuinely new residual events" in text
    assert "P81 = 1/16 to P82 = 1/12" in text

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"


def test_research_map_starts_with_orientation_before_stage_details():
    text = MAP.read_text(encoding="utf-8")
    hero = text.index("Seventy-six results, one dependency-aware scientific program")
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
    ]
    for token in required:
        assert token in text, token

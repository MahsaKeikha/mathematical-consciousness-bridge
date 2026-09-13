from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"


def test_research_map_starts_with_orientation_before_stage_details():
    text = MAP.read_text(encoding="utf-8")
    hero = text.index("Eighty-eight results, one dependency-aware scientific program")
    orientation = text.index("How to read this research")
    stage_one = text.index("I · Formal bridge foundations")
    assert hero < orientation < stage_one


def test_research_map_exposes_current_status_and_stage_ranges():
    text = MAP.read_text(encoding="utf-8")
    for token in (
        "Proved results",
        "Conditional results",
        "Open bridge target",
        "P1-P10",
        "P11-P18",
        "P19-P24",
        "P71",
        "P72",
        "P73-P88",
        "P25-P37",
        "P38-P44",
        "P45-P60",
        "P61-P70",
        "Ten-stage scientific path",
    ):
        assert token in text


def test_research_map_exposes_current_p88_audit_path():
    text = MAP.read_text(encoding="utf-8")
    for token in (
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
        "p88_equation_provenance.md",
        "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        "index.html#p88-frontier",
        "208,560",
        "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64",
    ):
        assert token in text


def test_research_map_keeps_previous_frontiers_as_history():
    text = MAP.read_text(encoding="utf-8")
    assert "through Proposition 88" in text
    assert "P85 tests exact three-event shared-parameter parity functionals" in text
    assert "P86 adds exact minimally weighted four-event functionals" in text
    assert "39,600" in text
    assert "P88" in text
    assert text.index("P87") < text.index("P88", text.index("P87"))

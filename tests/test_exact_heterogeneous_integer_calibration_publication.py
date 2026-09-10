from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p63_is_visible_on_calibration_frontier_page():
    text = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")
    for token in (
        "P63 exact unequal-cost integer calibration",
        "p63_exact_heterogeneous_integer_calibration.svg",
        "exact_heterogeneous_integer_calibration.py",
        "test_exact_heterogeneous_integer_calibration.py",
    ):
        assert token in text


def test_p63_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P63](proposition_63_exact_heterogeneous_integer_calibration.md)" in roadmap
    assert "| P63 | [Exact heterogeneous-cost integer calibration]" in navigation
    assert "# 52. P63 exact heterogeneous-cost integer calibration" in equations

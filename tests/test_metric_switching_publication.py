from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p54_is_visible_on_main_research_page():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "**Proposition 54**",
        "p54_metric_switching_cost_residual_scheduling.svg",
        "metric_switching_residual_schedule.py",
        "test_metric_switching_residual_schedule.py",
    ):
        assert token in text


def test_p54_is_in_roadmap_navigation_and_equation_map():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P54](proposition_54_metric_switching_cost_residual_scheduling.md)" in roadmap
    assert "| P54 | [Metric switching-cost residual scheduling]" in navigation
    assert "# 43. P54 metric switching-cost residual scheduling" in equations

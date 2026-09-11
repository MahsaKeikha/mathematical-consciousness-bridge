from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p57_is_visible_on_main_page():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "**Proposition 57**",
        "p57_switching_metric_perturbation.svg",
        "switching_metric_perturbation.py",
        "test_switching_metric_perturbation.py",
    ):
        assert token in text


def test_p57_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P57](proposition_57_switching_metric_perturbation.md)" in roadmap
    assert "| P57 | [Switching-metric perturbation stability]" in navigation
    assert "# 46. P57 switching-metric perturbation stability" in equations

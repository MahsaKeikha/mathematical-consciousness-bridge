from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p55_is_visible_on_main_page():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "P55 - pruning-aware metric switching-cost monotonicity",
        "p55_pruning_aware_switching_monotonicity.svg",
        "pruning_aware_switching_monotonicity.py",
        "test_pruning_aware_switching_monotonicity.py",
    ):
        assert token in text


def test_p55_is_in_public_research_maps():
    roadmap = (ROOT / "docs" / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (ROOT / "docs" / "research_navigation.md").read_text(encoding="utf-8")
    equations = (ROOT / "docs" / "equation_and_citation_map.md").read_text(encoding="utf-8")
    assert "[P55](proposition_55_pruning_aware_switching_monotonicity.md)" in roadmap
    assert "| P55 | [Pruning-aware metric switching-cost monotonicity]" in navigation
    assert "# 44. P55 pruning-aware metric switching-cost monotonicity" in equations

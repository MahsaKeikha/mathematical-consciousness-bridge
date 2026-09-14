from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p62_is_visible_on_calibration_frontier_page():
    text = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")
    for token in (
        "# P62. Heterogeneous-cost transition calibration",
        "p62_heterogeneous_cost_transition_calibration.svg",
        "heterogeneous_cost_transition_calibration.py",
        "test_heterogeneous_cost_transition_calibration.py",
    ):
        assert token in text

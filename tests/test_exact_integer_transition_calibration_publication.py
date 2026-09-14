from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p61_is_visible_on_calibration_frontier_page():
    text = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")
    for token in (
        "# P61. Exact integer transition-calibration allocation",
        "p61_exact_integer_transition_calibration.svg",
        "exact_integer_transition_calibration.py",
        "test_exact_integer_transition_calibration.py",
    ):
        assert token in text

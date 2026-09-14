from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_p63_is_visible_on_calibration_frontier_page():
    text = (ROOT / "docs/calibration_optimization_frontier_p61_p70.md").read_text(encoding="utf-8")
    for token in (
        "# P63. Exact heterogeneous-cost integer calibration",
        "p63_exact_heterogeneous_integer_calibration.svg",
        "exact_heterogeneous_integer_calibration.py",
        "test_exact_heterogeneous_integer_calibration.py",
    ):
        assert token in text

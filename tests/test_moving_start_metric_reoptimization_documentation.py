from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_56_moving_start_metric_reoptimization_stability.md"
FIGURE = ROOT / "docs" / "figures" / "p56_moving_start_metric_reoptimization_stability.svg"


def test_p56_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 56A",
        "Proposition 56B",
        "Proposition 56C",
        "Proposition 56D",
        "1-Lipschitz",
        "strict-decrease certificate",
        "Scientific boundary",
    ):
        assert phrase in text


def test_p56_visual_and_proof_to_code_path_are_public():
    text = DOC.read_text(encoding="utf-8")
    for token in (
        "moving_start_metric_reoptimization.py",
        "test_moving_start_metric_reoptimization.py",
        "p56_moving_start_metric_reoptimization_stability.svg",
    ):
        assert token in text
    assert FIGURE.exists()

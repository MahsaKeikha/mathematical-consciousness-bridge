from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_55_pruning_aware_switching_monotonicity.md"
FIGURE = ROOT / "docs" / "figures" / "p55_pruning_aware_switching_monotonicity.svg"


def test_p55_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 55A",
        "Proposition 55B",
        "Proposition 55C",
        "Proposition 55D",
        "exact optimal cost-release decomposition",
        "Scientific boundary",
    ):
        assert phrase in text


def test_p55_visual_and_proof_to_code_path_are_public():
    text = DOC.read_text(encoding="utf-8")
    for token in (
        "pruning_aware_switching_monotonicity.py",
        "test_pruning_aware_switching_monotonicity.py",
        "p55_pruning_aware_switching_monotonicity.svg",
    ):
        assert token in text
    assert FIGURE.exists()

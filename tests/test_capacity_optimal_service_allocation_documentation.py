from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_52_capacity_optimal_service_allocation.md"
FIGURE = ROOT / "docs" / "figures" / "p52_capacity_optimal_service_allocation.svg"


def test_p52_documentation_exposes_exact_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 52A",
        "Proposition 52B",
        "Proposition 52C",
        "Exact discrete unit-capacity result",
        "Scientific boundary",
    ):
        assert phrase in text


def test_p52_visual_and_proof_to_code_path_are_public():
    assert FIGURE.exists()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "p52_capacity_optimal_service_allocation.svg",
        "capacity_optimal_service_allocation.py",
        "test_capacity_optimal_service_allocation.py",
        "**Proposition 52**",
    ):
        assert token in readme

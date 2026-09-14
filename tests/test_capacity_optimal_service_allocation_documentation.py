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

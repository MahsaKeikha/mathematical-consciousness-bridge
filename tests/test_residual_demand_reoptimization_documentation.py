from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_53_residual_demand_reoptimization.md"
FIGURE = ROOT / "docs" / "figures" / "p53_residual_demand_reoptimization.svg"


def test_p53_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 53A",
        "Proposition 53B",
        "Proposition 53C",
        "Pruning-only release",
        "Dynamic reallocation law",
        "What P53 does not prove",
    ):
        assert phrase in text

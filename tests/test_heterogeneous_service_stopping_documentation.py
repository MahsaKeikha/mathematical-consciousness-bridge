from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_51_heterogeneous_service_rate_stopping.md"
FIGURE = ROOT / "docs" / "figures" / "p51_heterogeneous_service_rate_stopping.svg"


def test_p51_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 51A",
        "Proposition 51B",
        "Proposition 51C",
        "P50 is an exact special case",
        "Finite-window rate interpretation",
        "Scientific boundary",
    ):
        assert phrase in text

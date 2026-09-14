from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_48_gap_dependent_stopping_complexity.md"
FIGURE = ROOT / "docs" / "figures" / "p48_gap_dependent_stopping_complexity.svg"


def test_p48_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 48A",
        "Proposition 48B",
        "Proposition 48C",
        "Zero-gap boundary",
        "Measurement-cost bound",
        "What P48 does not prove",
    ):
        assert phrase in text

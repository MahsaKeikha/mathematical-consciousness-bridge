from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "proposition_49_dyadic_stopping_overhead.md"
FIGURE = ROOT / "docs" / "figures" / "p49_dyadic_stopping_overhead.svg"


def test_p49_documentation_exposes_core_results():
    text = DOC.read_text(encoding="utf-8")
    for phrase in (
        "Proposition 49A",
        "Proposition 49B",
        "Proposition 49C",
        "Zero-gap boundary is preserved",
        "Certification-look complexity",
        "Scientific boundary",
    ):
        assert phrase in text

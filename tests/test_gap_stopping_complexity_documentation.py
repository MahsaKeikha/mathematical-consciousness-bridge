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


def test_p48_layered_publication_route() -> None:
    root = Path(__file__).resolve().parents[1]
    proof = root / "docs" / "proposition_48_gap_dependent_stopping_complexity.md"
    figure = root / "docs" / "figures" / "p48_gap_dependent_stopping_complexity.svg"
    source = root / "src" / "consciousness_bridge" / "gap_stopping_complexity.py"
    algorithm_test = root / "tests" / "test_gap_stopping_complexity.py"
    record = (root / "docs" / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (root / "docs" / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (root / "README.md").read_text(encoding="utf-8")

    for artifact in (proof, figure, source, algorithm_test):
        assert artifact.is_file(), artifact
    assert proof.name in record
    assert figure.name in catalog
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme

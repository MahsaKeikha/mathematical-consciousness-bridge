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


def test_p51_visual_and_proof_to_code_path_are_public():
    assert FIGURE.exists()
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for token in (
        "p51_heterogeneous_service_rate_stopping.svg",
        "heterogeneous_service_stopping.py",
        "test_heterogeneous_service_stopping.py",
        "**Proposition 51**",
    ):
        assert token in readme

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "docs" / "proposition_45_shared_preparation_graph_allocation.md"
FIGURE = ROOT / "docs" / "figures" / "p45_shared_preparation_graph_allocation.svg"


def test_p45_proof_exposes_core_graph_allocation_equations():
    text = PROOF.read_text(encoding="utf-8")
    required = (
        "2(\\varepsilon_i+\\varepsilon_j)",
        "2L_e(r_i+r_j)",
        "\\frac{w_{Y,i}}{\\varepsilon_i^3}",
        "\\sum_{e\\ni i}\\lambda_e",
        "C_e^*",
        "P44 post-selection",
    )
    for token in required:
        assert token in text


def test_p45_publication_map_exists_and_states_boundary():
    text = FIGURE.read_text(encoding="utf-8")
    assert "P45: shared-preparation graph allocation" in text
    assert "quantum incompleteness" in text
    assert "consciousness" in text

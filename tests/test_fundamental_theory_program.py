from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PROGRAM = ROOT / "docs" / "fundamental_theory_consciousness_program.md"
MAP = ROOT / "docs" / "figures" / "fundamental_theory_consciousness_map.svg"


def test_main_page_exposes_fundamental_theory_interface():
    text = README.read_text(encoding="utf-8")

    required = (
        "# 4.4 Fundamental theory / Theory-of-Everything interface",
        "fundamental_theory_consciousness_map.svg",
        "There is currently **no experimentally established Theory of Everything**",
        "T(\\Omega)=\\bigl(G(\\Omega),Q(\\Omega),C(\\Omega)\\bigr)",
        "d_{\\mathrm{TOE}}^{\\perp}",
    )
    for phrase in required:
        assert phrase in text


def test_my_big_toe_is_not_presented_as_scientific_fact():
    text = README.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")

    assert "Thomas W. Campbell" in text
    assert "not treated as established scientific facts" in text
    assert "speculative, falsifiable antecedent" in text
    assert "not established scientific facts" in program
    assert "speculative falsifiable proposal" in program


def test_program_defines_exact_factorization_failure_and_controls():
    text = PROGRAM.read_text(encoding="utf-8")

    assert "E=B_T\\circ T" in text
    assert "\\Omega\\sim_T\\Omega'" in text
    assert "d_{\\mathrm{TOE}}^{\\perp}" in text
    assert "R_{E|T}" in text
    assert "No-free-metaphysics rule" in text
    assert "The last possibility matters" in text


def test_fundamental_theory_map_is_valid_svg_with_scientific_boundary():
    text = MAP.read_text(encoding="utf-8")

    assert "<svg" in text
    assert "Fundamental Theory to Consciousness" in text
    assert "Complete declared physical map" in text
    assert "Bridge factorization / residual test" in text
    assert "would not by itself prove" in text

from pathlib import Path

DOC = Path("docs/proposition_71_target_provenance_noncircularity.md")
SOURCE = Path("src/consciousness_bridge/target_provenance_noncircularity.py")
TEST = Path("tests/test_target_provenance_noncircularity.py")
FIGURE = Path("docs/figures/p71_target_provenance_noncircularity.svg")


def test_p71_research_artifacts_exist() -> None:
    for path in (DOC, SOURCE, TEST, FIGURE):
        assert path.is_file(), f"missing P71 artifact: {path}"


def test_p71_document_states_core_non_circularity_results() -> None:
    text = DOC.read_text(encoding="utf-8")

    required = (
        "Proposition 71: target-provenance non-circularity",
        "E_h=h\\circ T",
        "I(E_h;\\Omega\\mid T)=0",
        "P71C: learned-target corollary",
        "I(\\widehat E;\\Omega\\mid T,D)=0",
        "P71D: target-provenance non-identifiability theorem",
        "P(\\omega,t,e)",
        "protocol requirement",
        "log 2\\approx0.6931",
        "p71_target_provenance_noncircularity.svg",
        "target_provenance_noncircularity.py",
        "test_target_provenance_noncircularity.py",
    )
    for token in required:
        assert token in text, f"P71 document missing: {token}"


def test_p71_source_keeps_provenance_boundary_explicit() -> None:
    text = SOURCE.read_text(encoding="utf-8")

    required = (
        "deterministic_descriptor_target_certificate",
        "stochastic_descriptor_channel_certificate",
        "independently_declared_target_residual",
        "structurally_vacuous",
        "structurally_screened_off",
        "does not infer conceptual independence from observed data",
    )
    for token in required:
        assert token in text, f"P71 source missing boundary token: {token}"

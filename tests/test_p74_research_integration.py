from pathlib import Path

DOC = Path("docs/proposition_74_finite_sample_target_channel_recovery.md")
SOURCE = Path("src/consciousness_bridge/finite_sample_target_channel_recovery.py")
TEST = Path("tests/test_finite_sample_target_channel_recovery.py")
FIGURE = Path("docs/figures/p74_finite_sample_target_channel_recovery.svg")
PROVENANCE = Path("docs/p74_equation_provenance.md")


def test_p74_research_artifacts_exist() -> None:
    for path in (DOC, SOURCE, TEST, FIGURE, PROVENANCE):
        assert path.is_file(), f"missing P74 artifact: {path}"


def test_p74_document_states_finite_sample_theorem_and_boundary() -> None:
    text = DOC.read_text(encoding="utf-8")
    required = (
        "Proposition 74: finite-sample target-channel recovery certification",
        "\\varepsilon_n(\\alpha)",
        "3\\delta_n",
        "13\\delta_n",
        "P73 nondegeneracy is not certified by these finite data",
        "q_L",
        "q_U",
        "\\gamma_{1,L}",
        "1152\\log(16/\\alpha)",
        "not an optimal sample-complexity theorem",
        "does not test the conditional-independence assumption itself",
        "physical-to-experiential bridge remains open",
        "finite_sample_target_channel_recovery.py",
    )
    for token in required:
        assert token in text, f"P74 document missing: {token}"


def test_p74_provenance_separates_standard_tools_from_local_assembly() -> None:
    text = PROVENANCE.read_text(encoding="utf-8")
    required = (
        "Hoeffding concentration",
        "standard mathematics",
        "repository-specific contribution",
        "P71 target provenance",
        "P72 measurement stability",
        "P73 population channel identification",
        "P74 finite-sample channel certification",
        "not certified by the current data",
    )
    for token in required:
        assert token in text, f"P74 provenance missing: {token}"


def test_p74_source_exposes_certificate_api_and_scope() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    required = (
        "FiniteSampleTargetChannelCertificate",
        "categorical_cell_linf_radius",
        "categorical_joint_l1_radius",
        "finite_sample_three_view_certificate",
        "sufficient_nondegeneracy_sample_size",
        "does not validate conditional independence",
        "identify the latent state with consciousness",
    )
    for token in required:
        assert token in text, f"P74 source missing: {token}"

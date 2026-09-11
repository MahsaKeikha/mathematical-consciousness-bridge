from pathlib import Path

DOC = Path("docs/proposition_72_target_measurement_channel_robustness.md")
SOURCE = Path("src/consciousness_bridge/target_measurement_channel_robustness.py")
TEST = Path("tests/test_target_measurement_channel_robustness.py")
FIGURE = Path("docs/figures/p72_target_measurement_channel_robustness.svg")


def test_p72_research_artifacts_exist() -> None:
    for path in (DOC, SOURCE, TEST, FIGURE):
        assert path.is_file(), f"missing P72 artifact: {path}"


def test_p72_document_states_measurement_transfer_theorems() -> None:
    text = DOC.read_text(encoding="utf-8")
    required = (
        "Proposition 72: target-measurement channel robustness",
        "Y\\perp\\!\\!\\!\\perp\\Omega\\mid(E^\\star,T)",
        "I(Y;\\Omega\\mid T)",
        "I(E^\\star;\\Omega\\mid T)",
        "P72B: the converse fails",
        "\\gamma_t",
        "\\ker K_t\\cap\\mathcal H=\\{0\\}",
        "|1-2\\eta|",
        "P72D: finite-sample lower confidence bound",
        "P72E: sufficient sample size",
        "target_measurement_channel_robustness.py",
        "p72_target_measurement_channel_robustness.svg",
    )
    for token in required:
        assert token in text, f"P72 document missing: {token}"


def test_p72_source_keeps_scientific_boundary_explicit() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    required = (
        "target_measurement_residual_certificate",
        "target_channel_tv_transfer",
        "binary_symmetric_target_transfer",
        "finite_observed_tv_lower_bound",
        "sufficient_equal_sample_size_for_latent_gap",
        "does not establish that",
        "ground truth experience",
    )
    for token in required:
        assert token in text, f"P72 source missing boundary token: {token}"


def test_p72_explicitly_preserves_p71_provenance_requirement() -> None:
    text = DOC.read_text(encoding="utf-8")
    assert "P71 provenance requirement" in text
    assert "P72 assumes that provenance hurdle has been addressed" in text
    assert "does not claim that such a channel can always be inferred" in text

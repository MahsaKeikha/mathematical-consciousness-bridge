from pathlib import Path

DOC = Path("docs/proposition_73_target_channel_identifiability.md")
SOURCE = Path("src/consciousness_bridge/target_channel_identifiability.py")
TEST = Path("tests/test_target_channel_identifiability.py")
FIGURE = Path("docs/figures/p73_target_channel_identifiability.svg")


def test_p73_research_artifacts_exist() -> None:
    for path in (DOC, SOURCE, TEST, FIGURE):
        assert path.is_file(), f"missing P73 artifact: {path}"


def test_p73_document_states_identifiability_and_boundary_results() -> None:
    text = DOC.read_text(encoding="utf-8")
    required = (
        "Proposition 73: three-view target-channel identifiability",
        "C_{ij}=b_ib_jv",
        "M_{123}=-2mv",
        "m^2=\\frac{q}{q+4}",
        "\\gamma_j=|b_j|",
        "\\gamma_{123}\\ge\\max",
        "two-view non-identifiability theorem",
        "(b_1,b_2)=(0.60,0.60)",
        "(b_1,b_2)=(0.45,0.80)",
        "10.2307/2346806",
        "10.1214/09-AOS689",
        "not assumed to be consciousness",
        "target_channel_identifiability.py",
    )
    for token in required:
        assert token in text, f"P73 document missing: {token}"


def test_p73_source_preserves_model_and_semantic_boundaries() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    required = (
        "recover_three_view_binary_model",
        "joint_channel_stability",
        "binary_channel_stability",
        "unique up to the global latent-label swap",
        "does not interpret the latent state as consciousness",
        "two-view non-identifiability",
    )
    for token in required:
        assert token in text, f"P73 source missing boundary token: {token}"

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p73_core_research_artifacts_exist():
    for path in (
        "docs/proposition_73_three_view_target_channel_identifiability.md",
        "docs/p73_equation_provenance.md",
        "docs/figures/p73_three_view_target_channel_identifiability.svg",
        "src/consciousness_bridge/three_view_target_channel_identifiability.py",
        "tests/test_three_view_target_channel_identifiability.py",
    ):
        assert (ROOT / path).exists(), path


def test_p73_proof_exposes_positive_negative_and_finite_results():
    text = _read("docs/proposition_73_three_view_target_channel_identifiability.md")
    for token in (
        "Proposition 73A: two heterogeneous views are not individually identifiable",
        "Proposition 73B: three nondegenerate views identify the stability magnitudes",
        "Proposition 73C: signed reliability has one unavoidable global orientation ambiguity",
        "Proposition 73D: finite-sample stability intervals",
        "Proposition 73E: handoff to P72",
        "m_{ij}=r_i r_j",
        "physical-to-experiential bridge remains open",
    ):
        assert token in text


def test_p73_proof_has_direct_code_test_figure_and_provenance_links():
    text = _read("docs/proposition_73_three_view_target_channel_identifiability.md")
    for token in (
        "../src/consciousness_bridge/three_view_target_channel_identifiability.py",
        "../tests/test_three_view_target_channel_identifiability.py",
        "figures/p73_three_view_target_channel_identifiability.svg",
        "p73_equation_provenance.md",
    ):
        assert token in text


def test_p73_provenance_separates_standard_math_from_repository_role():
    text = _read("docs/p73_equation_provenance.md")
    for token in (
        "Standard mathematical ingredients",
        "Repository-original role",
        "Identifiability boundary",
        "10.2307/2346806",
        "10.1214/09-AOS689",
        "Hoeffding",
        "P71 target provenance",
        "P72 target-channel robustness",
        "P73 channel-stability identifiability",
    ):
        assert token in text

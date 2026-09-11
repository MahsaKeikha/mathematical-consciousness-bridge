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
        "tests/test_p73_interval_bounds.py",
        "tests/test_p73_figure_geometry.py",
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


def test_p73_is_integrated_across_public_research_surfaces():
    required = {
        "README.md": [
            "73 proposition-level results",
            "v0.73.0",
            "proposition_73_three_view_target_channel_identifiability.md",
            "p73_three_view_target_channel_identifiability.svg",
        ],
        "docs/theorem_roadmap.md": [
            "current documented theorem frontier is **P73**",
            "[P73](proposition_73_three_view_target_channel_identifiability.md)",
        ],
        "docs/research_navigation.md": [
            "current documented theorem frontier is **P73**",
            "| P73 | [Three-view target-channel identifiability]",
        ],
        "docs/detailed_proposition_record.md": [
            "Complete P1 to P73 chronology",
            "**P73** addresses one assumption left open by P72",
        ],
        "website/index.html": [
            "<strong>73</strong><span>proposition-level results</span>",
            "v0.73.0",
            "p73_three_view_target_channel_identifiability.svg",
        ],
        "website/research-map.html": [
            "P73: When can target-channel stability be identified?",
            "P71-P73 are target-side methodology results, not calibration theorems",
        ],
        "website/visual-atlas.html": [
            "p73_three_view_target_channel_identifiability.svg",
            "P73: three-view channel-stability identification",
        ],
        "CITATION.cff": [
            "version: 0.73.0",
            "current documented theorem frontier is P73",
        ],
        "CITATION.bib": ["version      = {0.73.0}", "frontier: P73"],
        "CITATION.md": ["Version 0.73.0", "Proposition 73"],
        "pyproject.toml": [
            'version = "0.73.0"',
            "three-view target-channel identifiability",
        ],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing P73 publication token: {token}"


def test_p73_publication_keeps_calibration_branch_separate():
    readme = _read("README.md")
    roadmap = _read("docs/theorem_roadmap.md")
    navigation = _read("docs/research_navigation.md")
    calibration = _read("docs/calibration_optimization_frontier_p61_p70.md")

    assert "P61-P70" in readme
    assert "P61-P70" in roadmap
    assert "P61-P70" in navigation
    assert "Proposition 70" in calibration
    assert "P71-P73" in readme
    assert "P71, P72, and P73" in roadmap

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p69_is_preserved_in_public_record():
    required = {
        "docs/calibration_optimization_frontier_p61_p70.md": ["Proposition 69", "p69_dual_optimal_multiplier.svg"],
        "docs/theorem_roadmap.md": ["P69", "proposition_69_dual_optimal_multiplier.md"],
        "docs/research_navigation.md": ["proposition_69_dual_optimal_multiplier.md"],
        "docs/equation_and_citation_map.md": ["P69 certified dual-optimal multiplier search", "Q_{\\rm low}\\le q^*\\le Q_{\\rm up}"],
        "CHANGELOG.md": ["# 0.69.0 - 2026-09-10", "P69 certified dual-optimal multiplier search"],
    }
    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P69 token: {token}"


def test_p69_permanent_proof_code_visual_and_tests_exist():
    for path in [
        "docs/proposition_69_dual_optimal_multiplier.md",
        "docs/figures/p69_dual_optimal_multiplier.svg",
        "src/consciousness_bridge/dual_optimal_multiplier.py",
        "tests/test_dual_optimal_multiplier.py",
        "tests/test_p69_figure_geometry.py",
    ]:
        assert (ROOT / path).exists(), path


def test_temporary_p69_publication_machinery_is_absent():
    assert not (ROOT / "scripts/publish_p69.py").exists()
    assert not (ROOT / ".github/workflows/publish-p69.yml").exists()

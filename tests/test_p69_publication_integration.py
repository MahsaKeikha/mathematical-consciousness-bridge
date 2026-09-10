from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p69_is_integrated_across_public_record():
    required = {
        "README.md": [
            "version-0.69.0-2563eb",
            "69 proposition-level results",
            "Latest proved extension: P69 certified dual-optimal multiplier search",
            "p69_dual_optimal_multiplier.svg",
            "P1 through P69 with explicit dependency branches",
        ],
        "docs/theorem_roadmap.md": [
            "P69",
            "proposition_69_dual_optimal_multiplier.md",
            "p69_dual_optimal_multiplier.svg",
            "proved dual-optimization certificate",
        ],
        "docs/research_navigation.md": [
            "P1 through P69",
            "proposition_69_dual_optimal_multiplier.md",
        ],
        "docs/equation_and_citation_map.md": [
            "# 58. P69 certified dual-optimal multiplier search",
            "\\partial^+q(\\lambda)",
            "Q_{\\rm low}\\le q^*\\le Q_{\\rm up}",
            "does not assume \\(q^*=U_{\\rm int}^*(B)\\)",
        ],
        "website/index.html": [
            "<strong>69</strong><span>proposition-level results</span>",
            "<strong>v0.69.0</strong><span>current documented release</span>",
            "P69",
            "docs/figures/p69_dual_optimal_multiplier.svg",
        ],
        "website/research-map.html": [
            "Sixty-nine results",
            "P54-P69",
            "P62-P69",
            "P69 certified optimization of the dual multiplier family",
        ],
        "CITATION.cff": [
            "version: 0.69.0",
            "certified dual multiplier optimization",
        ],
        "pyproject.toml": [
            'version = "0.69.0"',
            "certified dual multiplier optimization",
        ],
        "CHANGELOG.md": [
            "# 0.69.0 - 2026-09-10",
            "P69 certified dual-optimal multiplier search",
        ],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing P69 publication token: {token}"


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

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p68_is_integrated_across_public_record():
    required = {
        "README.md": [
            "version-0.68.0-2563eb",
            "68 proposition-level results",
            "Latest proved extension: P68 Lagrangian optimality gap certificate",
            "p68_lagrangian_optimality_gap.svg",
            "P1 through P68 with explicit dependency branches",
        ],
        "docs/theorem_roadmap.md": [
            "P68",
            "proposition_68_lagrangian_optimality_gap.md",
            "p68_lagrangian_optimality_gap.svg",
            "proved Lagrangian gap certificate",
        ],
        "docs/research_navigation.md": [
            "P1 through P68",
            "proposition_68_lagrangian_optimality_gap.md",
        ],
        "docs/equation_and_citation_map.md": [
            "# 57. P68 Lagrangian optimality gap certificate",
            "q(\\lambda)\\le U_{\\rm int}^*(B)",
            "P67 is the zero-gap special case",
        ],
        "website/index.html": [
            "<strong>68</strong><span>proposition-level results</span>",
            "<strong>v0.68.0</strong><span>current documented release</span>",
            "P68",
            "docs/figures/p68_lagrangian_optimality_gap.svg",
        ],
        "website/research-map.html": [
            "Sixty-eight results",
            "P54-P68",
            "P62-P68",
            "P68 quantitative Lagrangian gap bound",
        ],
        "CITATION.cff": [
            "version: 0.68.0",
            "Lagrangian optimality gap certification",
        ],
        "pyproject.toml": [
            'version = "0.68.0"',
            "Lagrangian optimality gap certification",
        ],
        "CHANGELOG.md": [
            "# 0.68.0 - 2026-09-10",
            "P68 Lagrangian optimality gap certificate",
        ],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing P68 publication token: {token}"


def test_p68_permanent_proof_code_visual_and_tests_exist():
    for path in [
        "docs/proposition_68_lagrangian_optimality_gap.md",
        "docs/figures/p68_lagrangian_optimality_gap.svg",
        "src/consciousness_bridge/lagrangian_optimality_gap.py",
        "tests/test_lagrangian_optimality_gap.py",
        "tests/test_p68_figure_geometry.py",
    ]:
        assert (ROOT / path).exists(), path


def test_temporary_p68_publication_machinery_is_absent():
    assert not (ROOT / "scripts/publish_p68.py").exists()
    assert not (ROOT / ".github/workflows/publish-p68.yml").exists()

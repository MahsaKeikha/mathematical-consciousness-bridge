from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p67_is_integrated_across_public_record():
    required = {
        "README.md": [
            "version-0.67.0-2563eb",
            "67 proposition-level results",
            "Latest proved extension: P67 global integer optimality certificate",
            "p67_global_integer_optimality_certificate.svg",
            "P1 through P67 with explicit dependency branches",
        ],
        "docs/theorem_roadmap.md": [
            "P67",
            "proposition_67_global_integer_optimality_certificate.md",
            "p67_global_integer_optimality_certificate.svg",
            "proved global-optimality certificate",
        ],
        "docs/research_navigation.md": [
            "P1 through P67",
            "proposition_67_global_integer_optimality_certificate.md",
        ],
        "docs/equation_and_citation_map.md": [
            "# 56. P67 global integer optimality certificate",
            "\\Delta_e(j)",
            "U(k)=U_{\\rm int}^*(B)",
            "Failure of the interval test is inconclusive",
        ],
        "website/index.html": [
            "<strong>67</strong><span>proposition-level results</span>",
            "<strong>v0.67.0</strong><span>current documented release</span>",
            "P67",
            "docs/figures/p67_global_integer_optimality_certificate.svg",
        ],
        "website/research-map.html": ["P54-P67", "P62-P67", "P58-P67"],
        "CITATION.cff": ["version: 0.67.0", "global integer optimality certification"],
        "pyproject.toml": ['version = "0.67.0"', "global integer optimality certification"],
        "CHANGELOG.md": ["# 0.67.0 - 2026-09-10", "P67 global integer optimality certificate"],
    }

    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing P67 publication token: {token}"


def test_p67_permanent_proof_code_visual_and_tests_exist():
    for path in [
        "docs/proposition_67_global_integer_optimality_certificate.md",
        "docs/figures/p67_global_integer_optimality_certificate.svg",
        "src/consciousness_bridge/global_integer_optimality_certificate.py",
        "tests/test_global_integer_optimality_certificate.py",
        "tests/test_p67_figure_geometry.py",
    ]:
        assert (ROOT / path).exists(), path


def test_temporary_p67_publication_machinery_is_absent():
    assert not (ROOT / "scripts/publish_p67.py").exists()
    assert not (ROOT / ".github/workflows/publish-p67.yml").exists()

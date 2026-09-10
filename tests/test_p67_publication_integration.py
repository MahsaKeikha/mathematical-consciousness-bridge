from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p67_is_preserved_in_public_record():
    required = {
        "README.md": ["Proposition 67", "p67_global_integer_optimality_certificate.svg"],
        "docs/theorem_roadmap.md": ["P67", "proposition_67_global_integer_optimality_certificate.md"],
        "docs/research_navigation.md": ["proposition_67_global_integer_optimality_certificate.md"],
        "docs/equation_and_citation_map.md": ["P67 global integer optimality certificate", "\\Delta_e(j)"],
        "CHANGELOG.md": ["# 0.67.0 - 2026-09-10", "P67 global integer optimality certificate"],
    }
    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P67 token: {token}"


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

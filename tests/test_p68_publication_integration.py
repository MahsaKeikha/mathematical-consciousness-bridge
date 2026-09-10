from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_p68_is_preserved_in_public_record():
    required = {
        "README.md": ["Proposition 68", "p68_lagrangian_optimality_gap.svg"],
        "docs/theorem_roadmap.md": ["P68", "proposition_68_lagrangian_optimality_gap.md"],
        "docs/research_navigation.md": ["proposition_68_lagrangian_optimality_gap.md"],
        "docs/equation_and_citation_map.md": ["P68 Lagrangian optimality gap certificate", "q(\\lambda)"],
        "CHANGELOG.md": ["# 0.68.0 - 2026-09-10", "P68 Lagrangian optimality gap certificate"],
    }
    for path, tokens in required.items():
        text = _read(path)
        for token in tokens:
            assert token in text, f"{path} missing historical P68 token: {token}"


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

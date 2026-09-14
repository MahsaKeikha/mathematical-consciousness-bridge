from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


def test_choose_your_path_table_links_current_reader_layers() -> None:
    text = README.read_text(encoding="utf-8")
    required_links = (
        "[Start Here](START_HERE.md)",
        "[Research Map](docs/research_map.md)",
        "[Figure Catalog](docs/figure_catalog.md)",
        "[Technical Research Architecture](docs/research_architecture.md)",
        "[Theorem Roadmap](docs/theorem_roadmap.md)",
        "[Detailed Proposition Record](docs/detailed_proposition_record.md)",
        "[Equation and Citation Map](docs/equation_and_citation_map.md)",
        "[Reproducibility Guide](docs/reproducibility.md)",
        "[Glossary](docs/glossary.md)",
    )
    for link in required_links:
        assert link in text


def test_readme_exposes_current_frontier_without_recreating_internal_paper_sections() -> None:
    text = README.read_text(encoding="utf-8")
    assert "[Read the current frontier](docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md)" in text
    assert "# Abstract" not in text
    assert "# 1. Mathematical formulation of the bridge problem" not in text
    assert "# Detailed proposition record" not in text

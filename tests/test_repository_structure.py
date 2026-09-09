from pathlib import Path


def test_core_research_documents_exist():
    root = Path(__file__).resolve().parents[1]
    required = [
        root / "README.md",
        root / "docs" / "bridge_problem.md",
        root / "docs" / "physical_foundation.md",
        root / "docs" / "proposition_1_representation_invariance.md",
        root / "docs" / "equation_and_citation_map.md",
        root / "docs" / "axiom_ledger.md",
        root / "docs" / "theorem_roadmap.md",
        root / "docs" / "falsification_program.md",
        root / "docs" / "research_architecture.md",
        root / "docs" / "literature_map.md",
        root / "references.bib",
        root / "CITATION.cff",
    ]
    missing = [str(path.relative_to(root)) for path in required if not path.exists()]
    assert not missing, f"Missing research documents: {missing}"

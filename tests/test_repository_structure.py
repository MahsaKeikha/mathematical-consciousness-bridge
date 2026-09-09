from pathlib import Path


def test_core_research_documents_exist():
    root = Path(__file__).resolve().parents[1]
    required = [
        root / "README.md",
        root / "CHANGELOG.md",
        root / "docs" / "bridge_problem.md",
        root / "docs" / "physical_foundation.md",
        root / "docs" / "candidate_theory_families.md",
        root / "docs" / "proposition_1_representation_invariance.md",
        root / "docs" / "proposition_2_bridge_identifiability.md",
        root / "docs" / "proposition_3_bridge_equivalence_classes.md",
        root / "docs" / "proposition_4_discriminating_experiment_design.md",
        root / "docs" / "proposition_5_feature_sufficiency.md",
        root / "docs" / "proposition_6_canonical_bridge_signature.md",
        root / "docs" / "proposition_7_experimental_signature_recovery.md",
        root / "docs" / "proposition_8_robust_signature_recovery.md",
        root / "docs" / "proposition_9_categorical_sample_complexity.md",
        root / "docs" / "proposition_10_robust_experiment_design.md",
        root / "docs" / "universal_proof_target.md",
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

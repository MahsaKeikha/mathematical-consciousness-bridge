from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = (ROOT / "website" / "three-program-evidence.js").read_text(encoding="utf-8")
ORIENTATION = (ROOT / "website" / "research-orientation.js").read_text(encoding="utf-8")


RESEARCH_I_FIGURES = (
    "worldtube_baseline.png",
    "worldtube_phase_diagram.png",
    "finite_sample_benchmark.png",
    "symbolic_recovery_region.png",
    "perturbed_recovery_region.png",
    "gaussian_screen_calibration.png",
    "structural_null_screen.png",
    "trajectory_coupled_screen_calibration.png",
    "relative_covariance_calibration.png",
    "cross_fitted_relative_calibration.png",
    "drift_robust_relative_calibration.png",
    "calibrated_drift_comparison.png",
    "multi_regime_coupled_calibration.png",
    "dependent_gaussian_calibration.png",
    "dependent_centered_gaussian_calibration.png",
    "estimated_ar1_calibration.png",
    "nuisance_projection_calibration.svg",
    "estimated_ar1_nuisance_projection.svg",
    "design_specific_ar1_envelope.svg",
    "weighted_wishart_matrix_chernoff.svg",
    "uniform_matrix_chernoff_ar1.svg",
    "compact_temporal_family.svg",
    "calibrated_temporal_family.svg",
    "evalue_temporal_confidence_set.svg",
    "certified_evalue_outer_cover.svg",
    "physical_relaxation_sampling.svg",
    "physical_relaxation_markov.svg",
    "irregular_relaxation_evalue_calibration.svg",
    "two_scale_irregular_tau_cover.svg",
    "quadratic_relaxation_calibration.svg",
    "innovation_whitened_target.svg",
    "robust_innovation_whitened_target.svg",
    "observer_bridge_dimension_audit.svg",
)


RESEARCH_III_FIGURES = (
    "measurement_architecture.svg",
    "structural_measurement_pipeline.svg",
    "claim_ladder.svg",
)


def test_research_i_complete_33_figure_inventory_is_rendered() -> None:
    assert len(RESEARCH_I_FIGURES) == 33
    assert "All 33 Research I scientific result figures" in EVIDENCE
    assert "33 / 33 visible" in EVIDENCE
    for figure in RESEARCH_I_FIGURES:
        assert figure in EVIDENCE


def test_research_iii_complete_figure_directory_is_explicit() -> None:
    assert "Complete Research III figure set: 3 / 3 visible above." in EVIDENCE
    for figure in RESEARCH_III_FIGURES:
        assert figure in EVIDENCE


def test_research_i_source_manifest_exposes_formal_and_machine_records() -> None:
    required = (
        "docs/visual_research_guide.md",
        "docs/research_index.md",
        "docs/physics_mathematics_citation_map.md",
        "docs/reproducible_results.md",
        "docs/assumption_ledger.md",
        "docs/proposition_44_nuisance_projection.md",
        "docs/proposition_58_observer_bridge.md",
        "finite_sample_results.json",
        "robust_innovation_whitened_target.json",
        "observer_bridge_dimension_audit.json",
    )
    assert "research-i-source-manifest" in EVIDENCE
    for token in required:
        assert token in EVIDENCE


def test_research_iii_source_manifest_exposes_full_specification_path() -> None:
    required = (
        "docs/epistemic-boundaries.md",
        "docs/measurement-framework.md",
        "docs/measurement-instrument-spec.md",
        "docs/assumption-registry.md",
        "docs/protocol-phase1.md",
        "docs/statistical-validation.md",
        "docs/partial-identification.md",
        "docs/phenomenal-structure.md",
        "docs/falsification-matrix.md",
        "docs/reproducibility.md",
        "schemas/cep.schema.json",
        "schemas/claim.schema.json",
        "scripts/verify_repository_policy.py",
    )
    assert "research-iii-source-manifest" in EVIDENCE
    for token in required:
        assert token in EVIDENCE


def test_atlas_and_sources_load_the_evidence_expansion() -> None:
    assert "three-program-evidence.js" in ORIENTATION
    assert "visual-atlas.html" in ORIENTATION
    assert "sources.html" in ORIENTATION
    assert "#research-i-complete-figure-gallery" in ORIENTATION
    assert "#research-i-source-manifest" in ORIENTATION
    assert "#research-iii-source-manifest" in ORIENTATION

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


CANONICAL_MAIN_PAGE_FIGURES = (
    "research_architecture.svg",
    "multiscale_physical_hierarchy.svg",
    "equation_evidence_map.svg",
    "state_space_dynamics_map.svg",
    "thermodynamics_information_processing.svg",
    "quantum_bridge_completeness_map.svg",
    "physics_mathematics_atlas.svg",
    "information_geometry_response_manifold.svg",
    "universal_proof_ladder.svg",
    "theorem_roadmap.svg",
    "causal_structure_anatomy.svg",
    "p12_collision_map.svg",
    "p13_component_irredundancy.svg",
    "p14_temporal_continuation.svg",
    "p15_finite_sample_temporal_certification.svg",
    "p16_composition_coupling.svg",
    "p17_coarse_graining_refinement.svg",
    "p18_scale_sufficiency_certificate.svg",
    "p19_fundamental_physical_sufficiency.svg",
    "p20_finite_sample_residual_certificate.svg",
    "p21_descriptor_refinement_residual_persistence.svg",
    "p22_simultaneous_refinement_chain_certification.svg",
    "p23_adaptive_descriptor_selection_certification.svg",
    "p24_anytime_adaptive_refinement_certification.svg",
    "p25_directed_influence_scale_certification.svg",
    "p26_partition_irreducibility_scale_certification.svg",
    "p27_partition_lattice_node_aggregation.svg",
    "p28_intervention_node_aggregation_compatibility.svg",
    "p29_response_geometry_node_aggregation.svg",
    "observer_to_bridge_handoff.svg",
    "conscious_state_measurement_map.svg",
    "theory_comparison_map.svg",
    "spaceflight_extreme_environment_map.svg",
)


def test_main_page_contains_complete_quantitative_figure_sequence():
    text = README.read_text(encoding="utf-8")

    for index in range(1, 41):
        token = f"q{index:02d}_"
        assert token in text, f"README is missing quantitative figure Q{index:02d}"


def test_main_page_contains_complete_quantum_figure_sequence():
    text = README.read_text(encoding="utf-8")

    for index in range(1, 19):
        token = f"qm{index:02d}_"
        assert token in text, f"README is missing quantum figure QM{index:02d}"


def test_main_page_contains_canonical_scientific_maps():
    text = README.read_text(encoding="utf-8")

    for figure in CANONICAL_MAIN_PAGE_FIGURES:
        assert figure in text, f"README is missing canonical figure {figure}"


def test_main_page_exposes_entire_proposition_chain():
    text = README.read_text(encoding="utf-8")

    for index in range(1, 30):
        assert f"**P{index}**" in text, f"README is missing proposition P{index}"


def test_main_page_declares_scientific_status_boundaries():
    text = README.read_text(encoding="utf-8")

    required_phrases = (
        "Synthetic example",
        "Open bridge problem",
        "does **not** assume that a physical quantity is consciousness",
        "Quantum mechanics does not by itself imply consciousness",
        "Reproducibility and audit path",
        "Numerical validation facts",
    )
    for phrase in required_phrases:
        assert phrase in text, f"README is missing scientific-boundary text: {phrase}"

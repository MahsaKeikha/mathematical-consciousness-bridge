from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAIL = ROOT / "docs" / "detailed_proposition_record.md"


CURATED_MAIN_PAGE_FIGURES = (
    "research_architecture.svg",
    "universal_proof_ladder.svg",
    "theorem_roadmap.svg",
    "conscious_state_measurement_map.svg",
    "fundamental_theory_consciousness_map.svg",
    "causal_structure_anatomy.svg",
    "information_geometry_response_manifold.svg",
    "p12_collision_map.svg",
    "p14_temporal_continuation.svg",
    "p18_scale_sufficiency_certificate.svg",
    "multiscale_physical_hierarchy.svg",
    "p20_finite_sample_residual_certificate.svg",
    "p71_target_provenance_noncircularity.svg",
    "p72_target_measurement_channel_robustness.svg",
    "p73_target_channel_identifiability.svg",
    "observer_to_bridge_handoff.svg",
    "quantum_bridge_completeness_map.svg",
    "p38_quantum_operational_sufficiency.svg",
    "p41_trace_ball_quantum_envelope.svg",
    "p47_sequential_graph_refinement.svg",
    "theory_comparison_map.svg",
    "equation_evidence_map.svg",
)


def test_main_page_contains_curated_scientific_figure_sequence():
    text = README.read_text(encoding="utf-8")
    for figure in CURATED_MAIN_PAGE_FIGURES:
        assert figure in text, f"README is missing curated figure {figure}"


def test_main_page_links_complete_visual_atlases_instead_of_embedding_them():
    text = README.read_text(encoding="utf-8")
    required = (
        "website/visual-atlas.html",
        "docs/quantitative_physics_mathematics_atlas.md",
        "docs/quantum_foundations_and_bridge_test.md",
        "docs/calibration_optimization_frontier_p61_p70.md",
        "Q01-Q40",
        "QM01-QM18",
    )
    for token in required:
        assert token in text

    q_tokens = sum(f"q{index:02d}_" in text for index in range(1, 41))
    qm_tokens = sum(f"qm{index:02d}_" in text for index in range(1, 19))
    assert q_tokens < 10
    assert qm_tokens < 10


def test_detailed_proposition_chronology_is_externalized():
    readme = README.read_text(encoding="utf-8")
    detail = DETAIL.read_text(encoding="utf-8")

    assert "docs/detailed_proposition_record.md" in readme
    assert "Open the complete P1 to P73 chronology" not in readme
    assert "Complete P1 to P73 chronology" in detail
    assert "Propositions **P1-P10**" in detail
    assert "**P70** makes the resulting certificate diagnostic rather than opaque" in detail
    assert "**P71** returns from the downstream calibration branch" in detail
    assert "**P72** adds the next target-side obligation" in detail
    assert "**P73** closes the population identifiability step" in detail


def test_main_page_declares_scientific_status_boundaries():
    text = README.read_text(encoding="utf-8")
    required_phrases = (
        "Synthetic example",
        "Open bridge problem",
        "**does not assume that a physical quantity is consciousness**",
        "Quantum mechanics does not by itself imply consciousness",
        "Reproducibility and audit path",
        "Numerical validation facts",
        "A passing test proves only",
        "target-construction protocol",
        "the way that target is observed",
        "reliability of that observation",
    )
    for phrase in required_phrases:
        assert phrase in text, f"README is missing scientific-boundary text: {phrase}"


def test_every_curated_figure_has_reader_interpretation():
    text = README.read_text(encoding="utf-8")
    assert text.count("**Figure ") >= len(CURATED_MAIN_PAGE_FIGURES)
    assert "The arrows are logical dependencies" in text
    assert "These are physical candidates to be tested for sufficiency" in text
    assert "The scientific conclusion is conditional" in text

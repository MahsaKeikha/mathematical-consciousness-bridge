import re
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
    "p74_finite_sample_target_channel_recovery.svg",
    "p75_target_model_adequacy_overidentification.svg",
    "p76_finite_sample_target_model_adequacy.svg",
    "p77_full_law_model_set_separation.svg",
    "p78_certified_continuous_model_separation.svg",
    "observer_to_bridge_handoff.svg",
    "quantum_bridge_completeness_map.svg",
    "p38_quantum_operational_sufficiency.svg",
    "p41_trace_ball_quantum_envelope.svg",
    "p47_sequential_graph_refinement.svg",
    "theory_comparison_map.svg",
    "equation_evidence_map.svg",
)


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers)






def test_detailed_proposition_chronology_is_externalized():
    readme = README.read_text(encoding="utf-8")
    detail = DETAIL.read_text(encoding="utf-8")
    frontier = _frontier()

    assert "docs/detailed_proposition_record.md" in readme
    assert f"Open the complete P1 to P{frontier} chronology" not in readme
    assert f"Complete P1 to P{frontier} chronology" in detail
    assert "Propositions **P1-P10**" in detail
    assert "**P70** makes the resulting certificate diagnostic rather than opaque" in detail
    assert "**P71** returns from the downstream calibration branch" in detail
    assert "**P72** adds the next target-side obligation" in detail
    assert "**P73** closes the population identifiability step" in detail
    assert "**P74** converts the P73 population inversion into a finite-sample confidence certificate" in detail
    assert "**P75** separates target-channel identifiability from target-model adequacy" in detail
    assert "**P76** converts the tracked P75 population adequacy restrictions" in detail
    assert "**P77** closes the finite-data full-law gap left explicit by P76" in detail
    assert "**P78** supplies the continuous-family optimization certificate required by P77" in detail

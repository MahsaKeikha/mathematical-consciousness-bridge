from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"


def test_research_map_gives_direct_audit_paths():
    text = MAP.read_text(encoding="utf-8")
    required = [
        "theorem_roadmap.md",
        "research_navigation.md",
        "equation_and_citation_map.md",
        "visual-atlas.html",
        "proposition_71_target_provenance_noncircularity.md",
        "proposition_72_target_measurement_channel_robustness.md",
        "proposition_73_target_channel_identifiability.md",
        "proposition_77_full_law_model_set_separation.md",
        "proposition_78_certified_continuous_model_separation.md",
        "proposition_79_certified_sampling_radius.md",
        "proposition_80_simplex_coupled_model_separation.md",
        "proposition_81_projection_event_model_separation.md",
        "proposition_82_exact_nested_projection_contrast.md",
        "proposition_83_exact_projection_parity.md",
        "proposition_84_exact_projection_parity_contrast.md",
        "proposition_85_exact_triple_projection_parity_functional.md",
        "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md",
        "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
        "proposition_89_complete_linear_parity_duality.md",
        "proposition_90_exact_nonlinear_rank_one_separation.md",
        "proposition_91_mixed_prevalence_rank_two_flattening_separation.md",
        "proposition_92_exact_global_mixed_prevalence_distance.md",
        "p92_equation_provenance.md",
        "proposition_93_localized_sign_coherence_rejection.md",
        "p93_equation_provenance.md",
        'index.html#p93-frontier',
    ]
    for token in required:
        assert token in text, token

    assert "P73-P76" in text
    assert "P74 adds finite-data recovery" in text
    assert "P75 introduces fourth-view overidentification" in text
    assert "P76 turns its necessary restrictions into finite-sample rejection certificates" in text
    assert 'index.html#p91-frontier' not in text
    assert 'index.html#p88-frontier' not in text


def test_current_and_previous_nonlinear_frontiers_are_structurally_inside_main():
    text = MAP.read_text(encoding="utf-8")
    main_open = text.index("<main>")
    main_close = text.index("</main>")
    p90 = text.index('id="p90-research-map"')
    p91 = text.index('id="p91-research-map"')
    p93 = text.index('id="p93-research-map"')
    p92 = text.index('id="p92-research-map"')

    assert text.count('id="p90-research-map"') == 1
    assert text.count('id="p91-research-map"') == 1
    assert text.count('id="p92-research-map"') == 1
    assert text.count('id="p93-research-map"') == 1
    assert main_open < p90 < p91 < p93 < p92 < main_close
    assert "Historical P90 checkpoint" in text[p90:p91]
    assert "Current Research II theorem frontier" not in text[p90:p91]
    assert "Current Research II theorem frontier" not in text[p91:p93]
    assert "P93 · Localized finite-sample nonlinear rejection" in text[p93:p92]
    assert "Historical exact population checkpoint · P92" in text[p92:main_close]


def test_continuous_frontier_keeps_lineage_and_current_provenance_auditable():
    text = MAP.read_text(encoding="utf-8")
    frontier = text.index('id="continuous-model-frontier"')
    frontier_close = text.index("</section>", frontier)
    frontier_text = text[frontier:frontier_close]

    assert "proposition_82_exact_nested_projection_contrast.md" in frontier_text
    assert "proposition_83_exact_projection_parity.md" in frontier_text
    assert "proposition_90_exact_nonlinear_rank_one_separation.md" in frontier_text
    assert "proposition_91_mixed_prevalence_rank_two_flattening_separation.md" in frontier_text
    assert "p91_equation_provenance.md" in frontier_text or "p92_equation_provenance.md" in text
    assert "proposition_92_exact_global_mixed_prevalence_distance.md" in text
    assert "p92_equation_provenance.md" in text or "p92_equation_provenance.md" in text
    assert "proposition_92_exact_global_mixed_prevalence_distance.md" in text
    assert "p92_equation_provenance.md" in text

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
        "p91_equation_provenance.md",
        "test_mixed_prevalence_rank_two_flattening_separation.py",
        'index.html#p91-frontier',
    ]
    for token in required:
        assert token in text, token

    # P74-P76 are represented as the recovery-and-test stage on this orientation
    # page; their detailed file-level audit paths live in the theorem roadmap and
    # equation/citation map linked above.
    assert "P73-P76" in text
    assert "P74 adds finite-data recovery" in text
    assert "P75 introduces fourth-view overidentification" in text
    assert "P76 turns its necessary restrictions into finite-sample rejection certificates" in text

    assert 'index.html#p89-frontier' not in text
    assert 'index.html#p88-frontier' not in text


def test_current_and_previous_nonlinear_frontiers_are_structurally_inside_main():
    text = MAP.read_text(encoding="utf-8")
    main_open = text.index("<main>")
    main_close = text.index("</main>")
    p90 = text.index('id="p90-research-map"')
    p91 = text.index('id="p91-research-map"')
    p90_text = text[p90:p91]
    p91_text = text[p91:main_close]

    assert text.count('id="p90-research-map"') == 1
    assert text.count('id="p91-research-map"') == 1
    assert main_open < p90 < p91 < main_close
    assert "Historical P90 checkpoint" in p90_text
    assert "Current Research II theorem frontier" not in p90_text
    assert "Current Research II theorem frontier · P91" in p91_text


def test_continuous_frontier_keeps_lineage_and_current_provenance_auditable():
    text = MAP.read_text(encoding="utf-8")
    frontier = text.index('id="continuous-model-frontier"')
    frontier_close = text.index("</section>", frontier)
    frontier_text = text[frontier:frontier_close]

    assert "proposition_82_exact_nested_projection_contrast.md" in frontier_text
    assert "proposition_83_exact_projection_parity.md" in frontier_text
    assert "proposition_90_exact_nonlinear_rank_one_separation.md" in frontier_text
    assert "proposition_91_mixed_prevalence_rank_two_flattening_separation.md" in frontier_text
    assert "p91_equation_provenance.md" in frontier_text

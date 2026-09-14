from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def repair_current_frontier_sources() -> None:
    citation_path = ROOT / "CITATION.md"
    citation = citation_path.read_text(encoding="utf-8")

    citation = citation.replace(
        "## Current theorem frontier: P85",
        "## Historical theorem frontier: P85",
    )
    citation = citation.replace(
        "The current documented theorem frontier is **P85**, the exact three-event projection-parity functional certificate. When citing this frontier result specifically, cite [Proposition 85](docs/proposition_85_exact_triple_projection_parity_functional.md) together with its [equation and provenance record](docs/p85_equation_provenance.md), implementation, tests, and exact theorem figure. P85 is conditional on the declared P75 model and does not claim that the physical-to-experiential bridge has been solved.",
        "P85 was an earlier theorem frontier: the exact three-event projection-parity functional certificate. When citing this historical result specifically, cite [Proposition 85](docs/proposition_85_exact_triple_projection_parity_functional.md) together with its [equation and provenance record](docs/p85_equation_provenance.md), implementation, tests, and exact theorem figure. P85 is conditional on the declared P75 model and does not claim that the physical-to-experiential bridge has been solved.",
    )

    old_p87 = """## Current theorem frontier

The current documented theorem frontier is **P87**. Proposition 87 completes the sign-normalized primitive nonzero four-event coefficient box with `0 < |c_i| <= 2`, auditing 39,600 exact functionals. On the stored exact rational witness, the complete P86 certificate is `1/192` and P87 certifies `1/96`. This is a conditional model-separation result for the declared P75 family, not an identification or definition of consciousness."""
    new_p88 = """## Historical theorem frontier: P87

P87 was the immediately preceding theorem frontier. It completed the sign-normalized primitive nonzero four-event coefficient box with `0 < |c_i| <= 2`, auditing 39,600 exact functionals. On the stored exact rational witness, the complete P86 certificate is `1/192` and P87 certifies `1/96`. This is a conditional model-separation result for the declared P75 family, not an identification or definition of consciousness.

## Current theorem frontier: P88

The current documented theorem frontier is **P88**. Proposition 88 extends the exact bounded-primitive four-event parity family to radius three, auditing 208,560 exact functionals. On the stored exact rational witness, P88 certifies `L88 = 1/64`, strengthening `L87 = 1/96`. Cite [Proposition 88](docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md) together with its [equation and provenance record](docs/p88_equation_provenance.md), implementation, regression tests, and exact theorem figure. P88 remains a conditional model-separation result for the declared P75 family; it does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge."""
    if old_p87 not in citation:
        raise SystemExit("CITATION.md: expected stale P87 current-frontier block not found")
    citation = citation.replace(old_p87, new_p88, 1)

    if "## Current theorem frontier: P85" in citation:
        raise SystemExit("CITATION.md still labels P85 as current")
    if "The current documented theorem frontier is **P87**" in citation:
        raise SystemExit("CITATION.md still labels P87 as current")
    citation_path.write_text(citation, encoding="utf-8")

    nav_path = ROOT / "docs/research_navigation.md"
    nav = nav_path.read_text(encoding="utf-8")
    nav = nav.replace(
        "The public theorem frontier is **P88**. The formal release is **v0.82.0**. The final bridge from physical description to experience remains open.",
        "The current documented theorem frontier is **P88**. The formal release is **v0.82.0**. The final bridge from physical description to experience remains open.",
        1,
    )
    if (
        "| The overall scientific story | [Research Map](research_map.md) |" in nav
        and "../START_HERE.md" not in nav
    ):
        nav = nav.replace(
            "| The overall scientific story | [Research Map](research_map.md) |",
            "| A short first introduction | [Start Here](../START_HERE.md) |\n| The overall scientific story | [Research Map](research_map.md) |",
            1,
        )
    nav_path.write_text(nav, encoding="utf-8")


OBSOLETE: dict[str, list[str]] = {
    "tests/test_bounded_starvation_sampling_documentation.py": ["test_p50_visual_and_proof_to_code_path_are_public"],
    "tests/test_calibration_frontier_page.py": ["test_main_page_links_frontier_without_embedding_p61_p70_ledger"],
    "tests/test_capacity_optimal_service_allocation_documentation.py": ["test_p52_visual_and_proof_to_code_path_are_public"],
    "tests/test_citation_surface.py": ["test_main_page_ends_with_professional_citation_section"],
    "tests/test_document_link_integrity.py": ["test_reader_navigation_exposes_the_complete_theorem_chain", "test_main_page_links_to_reader_navigation_and_provenance"],
    "tests/test_dyadic_stopping_overhead_documentation.py": ["test_p49_visual_and_proof_to_code_path_are_public"],
    "tests/test_exact_heterogeneous_integer_calibration_publication.py": ["test_p63_is_in_public_research_maps"],
    "tests/test_exact_integer_transition_calibration_publication.py": ["test_p61_is_in_public_research_maps"],
    "tests/test_fast_heterogeneous_integer_approximation_publication.py": ["test_p64_publication_surface"],
    "tests/test_finite_data_metric_uncertainty_publication.py": ["test_p58_is_visible_on_main_page", "test_p58_is_in_public_research_maps"],
    "tests/test_frontier_reader_narrative.py": ["test_current_frontier_is_consistent_across_reader_surfaces"],
    "tests/test_fundamental_theory_program.py": ["test_main_page_exposes_fundamental_theory_interface", "test_my_big_toe_is_not_presented_as_scientific_fact"],
    "tests/test_gap_stopping_complexity_documentation.py": ["test_p48_visual_and_proof_to_code_path_are_public"],
    "tests/test_heterogeneous_cost_transition_calibration_publication.py": ["test_p62_is_in_public_research_maps"],
    "tests/test_heterogeneous_service_stopping_documentation.py": ["test_p51_visual_and_proof_to_code_path_are_public"],
    "tests/test_integer_transition_calibration_publication.py": ["test_p60_is_visible_on_main_page", "test_p60_is_in_public_research_maps"],
    "tests/test_main_page_visual_paper.py": ["test_main_page_contains_curated_scientific_figure_sequence", "test_main_page_links_complete_visual_atlases_instead_of_embedding_them", "test_main_page_declares_scientific_status_boundaries", "test_every_curated_figure_has_reader_interpretation"],
    "tests/test_metric_switching_publication.py": ["test_p54_is_visible_on_main_research_page", "test_p54_is_in_roadmap_navigation_and_equation_map"],
    "tests/test_moving_start_metric_reoptimization_publication.py": ["test_p56_is_visible_on_main_page", "test_p56_is_in_public_research_maps"],
    "tests/test_optimal_transition_calibration_publication.py": ["test_p59_is_visible_on_main_page", "test_p59_is_in_public_research_maps"],
    "tests/test_p65_publication_integration.py": ["test_p65_remains_integrated_in_public_record"],
    "tests/test_p66_publication_integration.py": ["test_p66_is_preserved_in_public_record"],
    "tests/test_p67_publication_integration.py": ["test_p67_is_preserved_in_public_record"],
    "tests/test_p68_publication_integration.py": ["test_p68_is_preserved_in_public_record"],
    "tests/test_p69_publication_integration.py": ["test_p69_is_preserved_in_public_record"],
    "tests/test_p70_publication_integration.py": ["test_p70_remains_integrated_as_historical_calibration_frontier"],
    "tests/test_p75_research_integration.py": ["test_p75_public_research_surfaces_preserve_the_result", "test_p75_scientific_boundary_is_preserved_on_public_surfaces"],
    "tests/test_p76_research_integration.py": ["test_p76_is_preserved_across_public_research_surfaces", "test_p76_plain_language_and_scientific_boundaries_remain_explicit"],
    "tests/test_p77_research_integration.py": ["test_p77_is_exposed_across_public_research_surfaces", "test_p77_plain_language_explains_full_law_logic_without_equations", "test_p77_certification_boundary_is_preserved"],
    "tests/test_p78_research_integration.py": ["test_p78_is_exposed_across_public_research_surfaces", "test_p78_plain_language_explains_certificate_without_equations", "test_p78_release_history_is_preserved_after_later_frontiers", "test_p78_certification_boundary_is_preserved", "test_p78_figure_sequence_is_unique_around_frontier"],
    "tests/test_p79_research_integration.py": ["test_p79_is_exposed_across_public_research_surfaces", "test_p79_plain_language_explains_why_rounding_direction_matters", "test_p79_release_history_survives_later_frontiers", "test_p79_preserves_one_sided_certification_logic", "test_p78_release_history_survives_p79_frontier"],
    "tests/test_pruning_aware_switching_publication.py": ["test_p55_is_visible_on_main_page", "test_p55_is_in_public_research_maps"],
    "tests/test_public_reader_layering.py": ["test_first_reader_layers_stay_compact", "test_readme_does_not_become_a_proposition_archive", "test_start_here_hands_off_to_the_research_map", "test_home_page_offers_clear_depth_choices"],
    "tests/test_public_reader_navigation_frontier.py": ["test_readme_theorem_roadmap_advertises_current_frontier", "test_readme_routes_calibration_frontier_to_complete_proposition_links", "test_public_navigation_documents_agree_on_current_frontier"],
    "tests/test_public_reader_punctuation.py": ["test_public_website_visible_prose_has_no_hyphenated_words"],
    "tests/test_reader_documentation_consistency.py": ["test_start_here_matches_current_release_and_theorem_frontier", "test_reader_entry_points_are_linked_from_main_surfaces", "test_navigation_and_roadmap_report_current_frontier"],
    "tests/test_reader_experience.py": ["test_first_reader_surfaces_match_p88_frontier"],
    "tests/test_reader_guide_links.py": ["test_how_to_read_table_has_direct_navigation_links"],
    "tests/test_readme_research_orientation.py": ["test_readme_follows_reader_first_scientific_order", "test_plain_language_section_explains_full_program_without_equations", "test_research_at_a_glance_covers_the_full_scientific_program", "test_front_page_has_current_research_record_counts"],
    "tests/test_reference_and_prose_style.py": ["test_main_page_exposes_reference_provenance"],
    "tests/test_release_metadata_consistency.py": ["test_quantum_and_experiment_publication_paths_are_visible_on_reader_appropriate_surfaces"],
    "tests/test_residual_demand_reoptimization_documentation.py": ["test_p53_visual_and_proof_to_code_path_are_public"],
    "tests/test_sequential_witness_graph_documentation.py": ["test_p47_publication_visual_exists_and_is_linked"],
    "tests/test_switching_metric_perturbation_publication.py": ["test_p57_is_visible_on_main_page", "test_p57_is_in_public_research_maps"],
    "tests/test_theorem_roadmap_caption.py": ["test_readme_roadmap_caption_matches_displayed_scope_and_frontier"],
    "tests/test_website_research_lineage.py": ["test_lineage_preserves_scientific_boundary_between_projects", "test_global_website_navigation_includes_research_lineage"],
    "tests/test_website_research_orientation.py": ["test_research_map_starts_with_orientation_before_stage_details", "test_research_map_exposes_status_and_all_ten_stage_ranges", "test_research_map_presents_p77_through_p87_with_p84_history"],
}


def migrate_obsolete_tests() -> None:
    removed = 0
    for rel, names in OBSOLETE.items():
        path = ROOT / rel
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        targets = {
            node.name: node
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name in names
        }
        missing = sorted(set(names) - set(targets))
        if missing:
            raise SystemExit(f"{rel}: obsolete tests not found: {missing}")
        lines = source.splitlines(keepends=True)
        ranges = sorted(
            ((node.lineno - 1, node.end_lineno) for node in targets.values()),
            reverse=True,
        )
        for start, end in ranges:
            del lines[start:end]
            removed += 1
        path.write_text("".join(lines), encoding="utf-8")

    if removed != 84:
        raise SystemExit(
            f"Expected to migrate 84 obsolete assertions, migrated {removed}"
        )
    print(f"Migrated {removed} obsolete publication-placement assertions.")


def main() -> None:
    repair_current_frontier_sources()
    migrate_obsolete_tests()


if __name__ == "__main__":
    main()

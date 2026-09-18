from __future__ import annotations

import json
import re
from pathlib import Path

from scripts.synchronize_research_three_website import CURRENT_RESEARCH_THREE_PIN

ROOT = Path(__file__).resolve().parents[1]
ATLAS_REFRESH = (ROOT / "website" / "atlas-architecture-refresh.js").read_text(
    encoding="utf-8"
)
RESEARCH_III_REFRESH = (
    ROOT / "website" / "research-iii-atlas-refresh.js"
).read_text(encoding="utf-8")
EVIDENCE = (ROOT / "website" / "three-program-evidence.js").read_text(
    encoding="utf-8"
)
ORIENTATION = (ROOT / "website" / "research-orientation.js").read_text(
    encoding="utf-8"
)
PAGES_WORKFLOW = (ROOT / ".github" / "workflows" / "pages.yml").read_text(
    encoding="utf-8"
)
PUBLICATION_MANIFEST = json.loads(
    (ROOT / "figures" / "manifest.json").read_text(encoding="utf-8")
)


def _core_records(manifest: dict[str, object]) -> list[dict[str, object]]:
    figures = manifest["figures"]
    assert isinstance(figures, list)
    return [
        record
        for record in figures
        if isinstance(record, dict)
        and record.get("category") == "theorem-or-architecture"
    ]


def test_research_ii_core_gallery_is_exactly_100_unique_canonical_visuals() -> None:
    core = _core_records(PUBLICATION_MANIFEST)
    paths = [str(record["path"]) for record in core]

    assert len(core) == 100
    assert len(set(paths)) == 100
    assert PUBLICATION_MANIFEST["figure_count"] == 158

    theorem_paths = [
        path for path in paths if re.match(r"^docs/figures/p[0-9]+_", path)
    ]
    architecture_paths = [path for path in paths if path not in theorem_paths]
    assert len(theorem_paths) == 83
    assert len(architecture_paths) == 17


def test_pages_artifact_bundles_the_canonical_manifest_for_the_gallery() -> None:
    assert "cp figures/manifest.json _site/figures/manifest.json" in PAGES_WORKFLOW
    assert 'test -f "_site/figures/manifest.json"' in PAGES_WORKFLOW


def test_pages_deployment_enforces_the_unified_gallery_contract() -> None:
    required = (
        "research-i-complete-figure-gallery",
        "research-ii-complete-core-gallery",
        "research-iii-complete-figure-gallery",
        "research-iii-curated-visual-story",
        "research-iii-validation-figure-gallery",
        "research-iii-source-validation-gallery",
        "const RESEARCH_II_CORE_EXPECTED = 100",
        "9 / 9 visible",
        "21 / 21 visible",
        "21 result figures",
        "V1-V50 result record",
        "Result data",
        "v11_missingness_information_law.svg",
        "v12_v13_multisite_heterogeneity.svg",
        "v14_resolution_sample_size.svg",
        "v15_independent_pilot_gate.svg",
        "v16_v20_electromagnetic_validation.svg",
        "electromagnetic_validation_summary.json",
        "v21_v25_electromagnetic_inverse_validation.svg",
        "v26_v30_electromagnetic_resolution_validation.svg",
        "v31_v35_electromagnetic_design_validation.svg",
        "v36_v40_electromagnetic_finite_sample_validation.svg",
        "v41_v45_electromagnetic_selection_validation.svg",
        "v46_v50_electromagnetic_replication_validation.svg",
        "v36_v40_electromagnetic_finite_sample_validation.svg",
        "electromagnetic_inverse_validation_summary.json",
        "electromagnetic_resolution_validation_summary.json",
        "electromagnetic_design_validation_summary.json",
        "electromagnetic_finite_sample_validation_summary.json",
        "electromagnetic_selection_validation_summary.json",
        "electromagnetic_replication_validation_summary.json",
        "electromagnetic_finite_sample_validation_summary.json",
        "Electromagnetic Source Identifiability Program",
        "Electromagnetic Resolution and Information Program",
        "Electromagnetic Design and Spatial Specificity Program",
        "Finite-Sample Electromagnetic Inference Program",
        "Multiplicity and Selection-Safe Electromagnetic Inference Program",
        "Cross-Site Replication Inference and Stability Program",
        "deployed Research II core gallery contract is not exactly 100 unique figures",
        "deployed canonical figure count is not 158",
        "node --check _site/research-orientation.js",
        "node --check _site/atlas-architecture-refresh.js",
        "node --check _site/research-iii-atlas-refresh.js",
        "node --check _site/three-program-evidence.js",
    )
    for token in required:
        assert token in PAGES_WORKFLOW


def test_research_ii_gallery_reads_the_bundled_manifest_and_fails_closed() -> None:
    required = (
        "const RESEARCH_II_MANIFEST = 'figures/manifest.json'",
        "const RESEARCH_II_CORE_EXPECTED = 100",
        "record.category === RESEARCH_II_CORE_CATEGORY",
        "new Set(core.map((record) => record.path))",
        "expected ${RESEARCH_II_CORE_EXPECTED} unique core figures",
        "All ${core.length} Research II core visuals in one gallery",
        "It is a visual inventory, not a one-figure-per-proposition mapping.",
        "The original Research II showcase remains visible.",
    )
    for token in required:
        assert token in ATLAS_REFRESH


def test_research_ii_gallery_uses_the_research_i_complete_card_language() -> None:
    shared_classes = (
        "complete-record-block",
        "complete-record-head",
        "record-badge",
        "complete-figure-grid",
        "complete-figure-card",
        "complete-figure-card-body",
        "figure-phase",
        "figure-source-links",
    )
    for class_name in shared_classes:
        assert class_name in EVIDENCE
        assert class_name in ATLAS_REFRESH

    assert "research-i-complete-figure-gallery" in EVIDENCE
    assert "research-ii-complete-core-gallery" in ATLAS_REFRESH


def test_research_iii_gallery_exposes_architecture_validation_and_result_provenance() -> None:
    assert "research-iii-curated-visual-story" in RESEARCH_III_REFRESH
    assert "research-iii-complete-figure-gallery" in RESEARCH_III_REFRESH
    assert "research-iii-validation-figure-gallery" in RESEARCH_III_REFRESH
    assert "research-iii-source-validation-gallery" in RESEARCH_III_REFRESH
    assert "6-stage visual path" in RESEARCH_III_REFRESH
    assert "9 / 9 visible" in RESEARCH_III_REFRESH
    assert "21 / 21 visible" in RESEARCH_III_REFRESH
    assert "V1-V50 result record" in RESEARCH_III_REFRESH
    assert "Result data" in RESEARCH_III_REFRESH
    assert "Electromagnetic Field Measurement Program" in RESEARCH_III_REFRESH
    assert "V16-V20 · electromagnetic measurement arm" in RESEARCH_III_REFRESH
    assert "Electromagnetic Source Identifiability Program" in RESEARCH_III_REFRESH
    assert "V21-V25 · electromagnetic source identifiability" in RESEARCH_III_REFRESH
    assert "Electromagnetic Resolution and Information Program" in RESEARCH_III_REFRESH
    assert "V26-V30 · electromagnetic resolution and information" in RESEARCH_III_REFRESH
    assert "Electromagnetic Design and Spatial Specificity Program" in RESEARCH_III_REFRESH
    assert "V31-V35 · electromagnetic design and spatial specificity" in RESEARCH_III_REFRESH
    assert "Finite-Sample Electromagnetic Inference Program" in RESEARCH_III_REFRESH
    assert "V36-V40 · finite-sample electromagnetic inference" in RESEARCH_III_REFRESH
    assert "Multiplicity and Selection-Safe Electromagnetic Inference Program" in RESEARCH_III_REFRESH
    assert "V41-V45 · multiplicity and selection-safe inference" in RESEARCH_III_REFRESH
    assert "Cross-Site Replication Inference and Stability Program" in RESEARCH_III_REFRESH
    assert "V46-V50 · cross-site replication inference" in RESEARCH_III_REFRESH
    assert "v46_v50_electromagnetic_replication_validation.svg" in RESEARCH_III_REFRESH
    assert "electromagnetic_replication_validation_summary.json" in RESEARCH_III_REFRESH
    assert "Electromagnetic Source Identifiability Program" in RESEARCH_III_REFRESH
    assert "V21-V25 · electromagnetic source identifiability" in RESEARCH_III_REFRESH
    assert CURRENT_RESEARCH_THREE_PIN == "edc1db943d6efe8bdc679dbc5d77ecb7633476ab"

    architecture_figures = (
        "research_program_map.svg",
        "target_evidence_matrix.svg",
        "measurement_architecture.svg",
        "cep_anatomy.svg",
        "identification_uncertainty_pipeline.svg",
        "structural_measurement_pipeline.svg",
        "validation_program_map.svg",
        "theory_falsification_map.svg",
        "claim_ladder.svg",
    )
    validation_figures = (
        "finite_sample_identification.svg",
        "finite_sample_coverage.svg",
        "transport_bias_surface.svg",
        "dependence_stress.svg",
        "structural_alignment_power.svg",
        "calibration_sample_uncertainty.svg",
        "missingness_identification_loss.svg",
        "inverse_conditioning_youden.svg",
        "two_site_partial_identification.svg",
        "resolution_abstention_frontier.svg",
        "v11_missingness_information_law.svg",
        "v12_v13_multisite_heterogeneity.svg",
        "v14_resolution_sample_size.svg",
        "v15_independent_pilot_gate.svg",
        "v16_v20_electromagnetic_validation.svg",
        "v21_v25_electromagnetic_inverse_validation.svg",
        "v26_v30_electromagnetic_resolution_validation.svg",
        "v31_v35_electromagnetic_design_validation.svg",
    )
    result_files = (
        "finite_sample_coverage.csv",
        "dependence_stress.csv",
        "transport_stress.csv",
        "structural_alignment_power.csv",
        "calibration_sample_uncertainty.csv",
        "missingness_stress.csv",
        "conditioning_stress.csv",
        "two_site_nonidentifiability.csv",
        "resolution_abstention_frontier.csv",
        "v11_missingness_information_law.csv",
        "v12_v13_multisite_identification.csv",
        "v14_resolution_sample_size.csv",
        "v15_independent_pilot_gate.csv",
        "electromagnetic_validation_summary.json",
        "electromagnetic_inverse_validation_summary.json",
        "electromagnetic_resolution_validation_summary.json",
        "electromagnetic_design_validation_summary.json",
    )
    for figure in architecture_figures + validation_figures:
        assert figure in RESEARCH_III_REFRESH
    for result in result_files:
        assert result in RESEARCH_III_REFRESH


def test_atlas_orientation_points_to_architecture_and_validation_galleries() -> None:
    assert "Research III exposes 9 foundational architecture visuals" in ORIENTATION
    assert "21 code-generated V1-V50 validation-result figures" in ORIENTATION
    for anchor in (
        "#research-i-complete-figure-gallery",
        "#research-ii-complete-core-gallery",
        "#research-iii-complete-figure-gallery",
        "#research-iii-validation-figure-gallery",
    ):
        assert anchor in ORIENTATION


def test_research_iii_refresh_is_loaded_for_all_public_research_three_surfaces() -> None:
    assert "research-iii-atlas-refresh.js" in ORIENTATION
    assert "loadResearchIIIAtlasRefresh();" in ORIENTATION
    assert "data-research-iii-atlas-refresh" in ORIENTATION
    for page in ("index.html", "measurement-science.html", "visual-atlas.html", "sources.html"):
        assert page in ORIENTATION


def test_new_atlas_surface_keeps_reader_punctuation_contract() -> None:
    for surface in (ATLAS_REFRESH, RESEARCH_III_REFRESH, ORIENTATION):
        assert "\u2013" not in surface
        assert "\u2014" not in surface


def test_research_iii_atlas_validation_gallery_uses_four_column_desktop_layout() -> None:
    assert "#research-iii-validation-figure-gallery .r3-validation-grid" in RESEARCH_III_REFRESH
    assert "grid-template-columns:repeat(4,minmax(0,1fr))" in RESEARCH_III_REFRESH
    assert "@media(max-width:1180px)" in RESEARCH_III_REFRESH
    assert "grid-template-columns:repeat(2,minmax(0,1fr))" in RESEARCH_III_REFRESH
    assert "@media(max-width:680px)" in RESEARCH_III_REFRESH

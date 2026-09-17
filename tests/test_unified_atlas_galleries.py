from __future__ import annotations

import json
import re
from pathlib import Path

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
RESEARCH_III_PIN = "a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee"


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
        "10 / 10 visible",
        "resolution_abstention_frontier.svg",
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


def test_research_iii_gallery_exposes_architecture_and_validation_records() -> None:
    assert "research-iii-curated-visual-story" in RESEARCH_III_REFRESH
    assert "research-iii-complete-figure-gallery" in RESEARCH_III_REFRESH
    assert "research-iii-validation-figure-gallery" in RESEARCH_III_REFRESH
    assert "research-iii-source-validation-gallery" in RESEARCH_III_REFRESH
    assert "6-stage visual path" in RESEARCH_III_REFRESH
    assert "9 / 9 visible" in RESEARCH_III_REFRESH
    assert "10 / 10 visible" in RESEARCH_III_REFRESH
    assert RESEARCH_III_PIN in RESEARCH_III_REFRESH

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
    )
    for figure in architecture_figures + validation_figures:
        assert figure in RESEARCH_III_REFRESH


def test_atlas_orientation_points_to_architecture_and_validation_galleries() -> None:
    assert "Research III now exposes 9 foundational architecture visuals" in ORIENTATION
    assert "10 code-generated V1-V10 validation-result figures" in ORIENTATION
    for anchor in (
        "#research-i-complete-figure-gallery",
        "#research-ii-complete-core-gallery",
        "#research-iii-complete-figure-gallery",
        "#research-iii-validation-figure-gallery",
    ):
        assert anchor in ORIENTATION


def test_research_iii_refresh_is_loaded_for_atlas_and_sources() -> None:
    assert "research-iii-atlas-refresh.js" in ORIENTATION
    assert "loadResearchIIIAtlasRefresh();" in ORIENTATION
    assert "dataset.researchIiiAtlasRefresh" in ORIENTATION
    assert "page !== 'visual-atlas.html' && page !== 'sources.html'" in ORIENTATION


def test_new_atlas_surface_keeps_reader_punctuation_contract() -> None:
    for surface in (ATLAS_REFRESH, RESEARCH_III_REFRESH, ORIENTATION):
        assert "\u2013" not in surface
        assert "\u2014" not in surface

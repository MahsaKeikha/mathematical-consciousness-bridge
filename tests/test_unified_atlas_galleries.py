from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS_REFRESH = (ROOT / "website" / "atlas-architecture-refresh.js").read_text(
    encoding="utf-8"
)
EVIDENCE = (ROOT / "website" / "three-program-evidence.js").read_text(
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


def test_research_iii_gallery_is_complete_and_pinned() -> None:
    assert "research-iii-complete-figure-gallery" in ATLAS_REFRESH
    assert "3 / 3 visible" in ATLAS_REFRESH
    assert "1ceea4c428d835ec9a8a417cbf238d9bcfe1d7c3" in ATLAS_REFRESH
    for figure in (
        "measurement_architecture.svg",
        "structural_measurement_pipeline.svg",
        "claim_ladder.svg",
    ):
        assert figure in ATLAS_REFRESH


def test_new_atlas_surface_keeps_reader_punctuation_contract() -> None:
    assert "\u2013" not in ATLAS_REFRESH
    assert "\u2014" not in ATLAS_REFRESH

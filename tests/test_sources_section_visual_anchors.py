from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUALS = (ROOT / "website" / "source-section-visuals.js").read_text(
    encoding="utf-8"
)
ORIENTATION = (ROOT / "website" / "research-orientation.js").read_text(
    encoding="utf-8"
)


def test_sources_page_has_one_visual_anchor_per_research_program() -> None:
    required = (
        "research-i-source-visual-anchor",
        "research-ii-source-visual-anchor",
        "research-iii-source-visual-anchor",
    )
    for token in required:
        assert token in VISUALS
        assert token in ORIENTATION


def test_sources_visuals_use_scientific_project_figures() -> None:
    required = (
        "worldtube_phase_diagram.png",
        "figures/research_architecture.svg",
        "docs/figures/measurement_architecture.svg",
    )
    for token in required:
        assert token in VISUALS


def test_sources_research_iii_visual_uses_validated_pin() -> None:
    assert "d93e768d9a7d6054ff208de2a1b9c14e79192bc5" in VISUALS
    assert "consciousness-measurement-science/${MEASUREMENT_PIN}" in VISUALS
    assert "blob/${MEASUREMENT_PIN}/docs/measurement-framework.md" in VISUALS


def test_sources_research_iii_exposes_complete_nine_figure_record() -> None:
    assert "research-iii-source-curated-visual-story" in VISUALS
    assert "research-iii-source-complete-figure-gallery" in VISUALS
    assert "6-stage source path" in VISUALS
    assert "9 / 9 visible" in VISUALS

    figures = (
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
    for figure in figures:
        assert figure in VISUALS


def test_sources_research_iii_cards_link_context_and_exact_figure_source() -> None:
    assert "data-research-iii-source-figure" in VISUALS
    assert "Scientific context" in VISUALS
    assert "Figure source" in VISUALS
    assert "${record.context}" in VISUALS
    assert "docs/figures/${record.file}" in VISUALS
    assert "docs/visual-research-guide.md" in VISUALS
    assert "docs/figure-catalog.md" in VISUALS


def test_sources_research_iii_offers_readable_full_resolution_svg_views() -> None:
    assert "Open full-resolution SVG" in VISUALS
    assert "researchIIIRawHref" in VISUALS
    assert "${MEASUREMENT_RAW}/docs/figures/${record.file}" in VISUALS
    assert 'target="_blank"' in VISUALS
    assert 'rel="noopener noreferrer"' in VISUALS
    assert "GitHub's compact SVG preview" in VISUALS


def test_sources_research_iii_preview_geometry_is_reader_sized() -> None:
    assert "minmax(470px,1fr)" in VISUALS
    assert "height:360px" in VISUALS
    assert "min-height:360px" in VISUALS
    assert "max-height:520px" in VISUALS
    assert "min-height:500px" in VISUALS


def test_sources_visuals_are_inserted_before_source_card_catalogs() -> None:
    assert "section.querySelector('.program-record-grid')" in VISUALS
    assert "metrics.insertAdjacentElement('afterend', figure)" in VISUALS
    assert "section.querySelector('.program-source-grid')" in VISUALS
    assert "sourceCatalog" in VISUALS


def test_sources_visual_loader_is_scoped_to_sources_page() -> None:
    assert "source-section-visuals.js" in ORIENTATION
    assert "currentFile() !== 'sources.html'" in ORIENTATION
    assert "loadSourceSectionVisuals();" in ORIENTATION


def test_sources_visual_surface_keeps_reader_punctuation_contract() -> None:
    assert "\u2013" not in VISUALS
    assert "\u2014" not in VISUALS

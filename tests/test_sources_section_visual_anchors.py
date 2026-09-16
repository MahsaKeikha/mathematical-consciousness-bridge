from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VISUALS = (ROOT / "website" / "source-section-visuals.js").read_text(encoding="utf-8")
ORIENTATION = (ROOT / "website" / "research-orientation.js").read_text(encoding="utf-8")


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


def test_sources_visuals_are_inserted_before_source_card_catalogs() -> None:
    assert "section.querySelector('.program-record-grid')" in VISUALS
    assert "metrics.insertAdjacentElement('afterend', figure)" in VISUALS
    assert "section.querySelector('.program-source-grid')" in VISUALS


def test_sources_visual_loader_is_scoped_to_sources_page() -> None:
    assert "source-section-visuals.js" in ORIENTATION
    assert "currentFile() !== 'sources.html'" in ORIENTATION
    assert "loadSourceSectionVisuals();" in ORIENTATION

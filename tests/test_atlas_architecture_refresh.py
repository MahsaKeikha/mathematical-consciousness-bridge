from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFRESH = (ROOT / "website" / "atlas-architecture-refresh.js").read_text(
    encoding="utf-8"
)
SOURCES_VISUALS = (ROOT / "website" / "source-section-visuals.js").read_text(
    encoding="utf-8"
)


def test_atlas_refresh_pins_validated_research_iii_sources() -> None:
    assert "383a6cdab720b3f87c17191b7c98bd6828213b72" in REFRESH
    assert "consciousness-measurement-science/main/docs/figures/" in REFRESH
    assert "pinResearchIIIVisualSources" in REFRESH
    assert "currentFile() !== 'visual-atlas.html'" in REFRESH


def test_atlas_refresh_reuses_existing_card_styles_without_sizing_overrides() -> None:
    required = (
        "complete-record-block",
        "complete-figure-grid",
        "complete-figure-card",
        "complete-figure-card-body",
        "figure-phase",
        "figure-source-links",
    )
    for token in required:
        assert token in REFRESH

    forbidden = (
        "createElement('style')",
        'createElement("style")',
        "classList.add",
        "atlas-architecture-current",
        "max-height",
        "object-fit",
        "style.width",
        "style.height",
        "research_architecture.svg?v=",
    )
    for token in forbidden:
        assert token not in REFRESH


def test_atlas_refresh_collapses_only_the_detailed_research_ii_archive() -> None:
    assert "research-ii-frontier-archive" in REFRESH
    assert "research-ii-detailed-archive" in REFRESH
    assert "collapsed-by-default" in REFRESH
    assert "hashchange" in REFRESH
    assert "details.open = true" in REFRESH


def test_sources_research_ii_keeps_versioned_architecture_asset() -> None:
    assert "figures/research_architecture.svg?v=20260916-color-safe" in SOURCES_VISUALS
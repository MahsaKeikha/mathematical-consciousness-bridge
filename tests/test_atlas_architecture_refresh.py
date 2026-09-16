from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFRESH = (ROOT / "website" / "atlas-architecture-refresh.js").read_text(
    encoding="utf-8"
)
ORIENTATION = (ROOT / "website" / "research-orientation.js").read_text(
    encoding="utf-8"
)
SOURCES_VISUALS = (ROOT / "website" / "source-section-visuals.js").read_text(
    encoding="utf-8"
)


def test_atlas_architecture_uses_versioned_local_asset() -> None:
    assert "figures/research_architecture.svg?v=20260916-color-safe" in REFRESH
    assert "research_architecture.svg" in REFRESH
    assert "atlas-architecture-current" in REFRESH


def test_atlas_architecture_uses_standard_figure_card_limits() -> None:
    assert "var(--figure-card-media-max, 980px)" in REFRESH
    assert "max-height: 530px" in REFRESH
    assert "object-fit: contain" in REFRESH


def test_atlas_refresh_is_loaded_only_on_visual_atlas() -> None:
    assert "atlas-architecture-refresh.js" in ORIENTATION
    assert "currentFile() !== 'visual-atlas.html'" in ORIENTATION
    assert "loadAtlasArchitectureRefresh();" in ORIENTATION


def test_sources_research_ii_uses_same_versioned_architecture_asset() -> None:
    assert "figures/research_architecture.svg?v=20260916-color-safe" in SOURCES_VISUALS

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFRESH = (ROOT / "website" / "atlas-architecture-refresh.js").read_text(
    encoding="utf-8"
)
SOURCES_VISUALS = (ROOT / "website" / "source-section-visuals.js").read_text(
    encoding="utf-8"
)


def test_atlas_runtime_override_is_disabled() -> None:
    assert "Intentionally no runtime Atlas mutations" in REFRESH
    forbidden = (
        "querySelectorAll(",
        "image.src =",
        "atlas-architecture-current",
        "max-height: 530px",
        "object-fit: contain",
    )
    for token in forbidden:
        assert token not in REFRESH


def test_sources_research_ii_keeps_versioned_architecture_asset() -> None:
    assert "figures/research_architecture.svg?v=20260916-color-safe" in SOURCES_VISUALS

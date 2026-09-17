from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG_NS = "{http://www.w3.org/2000/svg}"
CURATED_ARROW_FIGURES = (
    ROOT / "docs" / "figures" / "research_architecture.svg",
    ROOT / "docs" / "figures" / "p100_anytime_sequential_eprocess.svg",
    ROOT / "website" / "research-ii-sufficiency-falsification-overview.svg",
    ROOT / "website" / "p100-anytime-valid-sequence-overview.svg",
)


def test_curated_arrowheads_are_absolute_and_restrained() -> None:
    for figure in CURATED_ARROW_FIGURES:
        root = ET.parse(figure).getroot()
        markers = list(root.iter(f"{SVG_NS}marker"))
        assert markers, f"{figure.name} must declare an SVG marker"
        for marker in markers:
            assert marker.attrib.get("markerUnits") == "userSpaceOnUse", (
                f"{figure.name} marker {marker.attrib.get('id')} must keep a fixed "
                "visual size instead of scaling with connector stroke width"
            )
            assert float(marker.attrib["markerWidth"]) <= 10.0
            assert float(marker.attrib["markerHeight"]) <= 10.0


def test_curated_connectors_use_round_professional_line_geometry() -> None:
    for figure in CURATED_ARROW_FIGURES:
        text = figure.read_text(encoding="utf-8")
        assert 'marker-end="url(#arrow)"' in text
        assert "markerUnits=\"strokeWidth\"" not in text
        assert "stroke-linecap:round" in text or 'stroke-linecap="round"' in text


def test_p100_theorem_figure_does_not_use_oversized_manual_arrow_polygons() -> None:
    figure = ROOT / "docs" / "figures" / "p100_anytime_sequential_eprocess.svg"
    root = ET.parse(figure).getroot()
    assert not list(root.iter(f"{SVG_NS}polygon"))

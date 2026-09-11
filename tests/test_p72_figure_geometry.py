import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p72_target_measurement_channel_robustness.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p72_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()

    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p72_svg_contains_theorem_and_measurement_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)

    required = (
        "P72 Target Measurement Channel Robustness",
        "I(Y; Omega | T) ≤ I(E*; Omega | T)",
        "I(E*; Omega | T) = log 2",
        "I(Y; Omega | T) = 0",
        "TV(Y) = |1 - 2 eta| TV(E*)",
        "TV(E*a, E*b) ≥ TV(Ya, Yb) ≥ LY",
        "sample burden diverges",
        "not an assumed definition of consciousness",
    )
    for token in required:
        assert token in text


def test_p72_svg_keeps_coordinates_inside_declared_canvas() -> None:
    root = ET.parse(FIGURE).getroot()

    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p79_bounded_target_view_dependence.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p79_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p79_svg_contains_bounded_dependence_logic() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P79 Robust Rejection Under Bounded Target-View Dependence",
        "True conditional law",
        "Product projection",
        "Dependence defect",
        "Declared dependence budget",
        "Population consequence",
        "d(P, M_P75) <= rho",
        "Budget must be independent of the rejection discrepancy",
        "P78 certified lower bound",
        "sampling epsilon + dependence rho",
        "L > epsilon + rho",
        "Non-rejection is inconclusive",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text


def test_p79_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p78_certified_continuous_model_separation.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p78_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p78_svg_contains_certified_continuous_separation_logic() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P78 Certified Continuous Model Separation",
        "P75 parameter cube: [0,1]^9",
        "Exact cell enclosure",
        "Certified box lower bound",
        "Exact Fraction arithmetic",
        "Global certified lower bound",
        "Candidate upper bound",
        "Certified bracket",
        "A best fit alone supplies only the upper side",
        "P77 rejection handoff",
        "valid sampling-radius upper bound",
        "Non-rejection is not model acceptance",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text


def test_p78_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

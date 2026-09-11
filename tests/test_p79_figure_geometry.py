import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p79_joint_statistical_computational_power.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p79_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p79_svg_contains_joint_power_logic() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P79 Joint Statistical-Computational Power",
        "Three-way certified decision",
        "certified rejection",
        "explicit overlap witness",
        "unresolved bracket",
        "Separation budget",
        "Delta_0 > eps_a + eps_b + eta",
        "Type I <= alpha, power >= 1-beta",
        "Sample-computation tradeoff",
        "Prospective guarantee, not model acceptance",
        "prespecified or independently justified",
        "does not prove low power",
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

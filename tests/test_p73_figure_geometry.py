import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p73_target_channel_identifiability.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p73_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p73_svg_contains_recovery_and_nonidentifiability_results() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P73 Three-View Target-Channel Identifiability",
        "Cij = bi bj v",
        "M123 = -2 m v b1 b2 b3",
        "m² = q / (q + 4)",
        "gamma_j = |b_j|",
        "gamma_123 ≥ max",
        "Two views are not enough in general",
        "same product 0.36, same observed law",
        "does not identify the latent class with consciousness",
    )
    for token in required:
        assert token in text


def test_p73_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

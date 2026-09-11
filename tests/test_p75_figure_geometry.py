import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p75_target_model_adequacy_overidentification.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p75_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p75_svg_contains_adequacy_logic_and_scientific_boundary() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P75 Target-Model Adequacy and Four-View Overidentification",
        "7 = 7  |  generically just-identified",
        "15 - 9 = 6 overidentifying degrees",
        "Covariance tetrads",
        "C12 C34 = C13 C24",
        "q123 = q124 = q134 = q234",
        "M1234 = (1 + q) C12 C34",
        "reconstruct all 16 cells",
        "Passing means model compatibility, not truth",
        "does not identify the latent state with consciousness",
    )
    for token in required:
        assert token in text


def test_p75_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

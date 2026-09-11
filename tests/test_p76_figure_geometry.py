import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p76_finite_sample_target_model_adequacy.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p76_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p76_svg_contains_finite_rejection_logic_and_boundary() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P76 Finite-Sample Target-Model Adequacy Rejection",
        "Sixteen-cell IID data",
        "Shared confidence event",
        "Moment confidence box",
        "P75 polynomial intervals",
        "2 tetrad constraints",
        "3 cross-triple constraints",
        "3 fourth-moment constraints",
        "|D_hat| > 12 delta",
        "No rejection is not acceptance",
        "does not identify the latent state with consciousness",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text


def test_p76_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

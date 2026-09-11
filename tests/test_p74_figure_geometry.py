import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p74_finite_sample_target_channel_recovery.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p74_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p74_svg_contains_certificate_and_failure_boundary() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P74 Finite-Sample Target-Channel Recovery",
        "8-cell empirical law P_hat",
        "|C_hat - C| <= 3 delta",
        "|M_hat - M| <= 13 delta",
        "Nondegeneracy gate",
        "NOT CERTIFIED",
        "qL = LM^2 / (U12 U13 U23)",
        "gamma_1,L = sqrt( L12 L13 / (vU U23) )",
        "does not validate conditional independence",
        "does not identify the latent state with consciousness",
    )
    for token in required:
        assert token in text


def test_p74_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

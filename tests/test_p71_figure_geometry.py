import xml.etree.ElementTree as ET
from pathlib import Path


FIGURE = Path("docs/figures/p71_target_provenance_noncircularity.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p71_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()

    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "720"
    assert root.attrib["viewBox"] == "0 0 1200 720"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p71_svg_contains_theorem_and_synthetic_residual_labels() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)

    required = (
        "P71 Target-Provenance Non-Circularity",
        "Descriptor-derived target",
        "Separately declared synthetic target",
        "E = h(T)",
        "I(E; Omega | T) = 0",
        "same T, different E",
        "log 2 = 0.6931 nats",
        "synthetic counterexample variable",
    )
    for token in required:
        assert token in text


def test_p71_svg_keeps_content_inside_declared_canvas() -> None:
    root = ET.parse(FIGURE).getroot()

    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 720.0

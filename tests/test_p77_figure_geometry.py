import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p77_full_law_model_set_separation.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_p77_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"


def test_p77_svg_contains_full_law_separation_logic_and_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P77 Finite-Sample Full-Law Model-Set Separation",
        "P76: interpretable necessary constraints",
        "P77: complete declared model-set separation",
        "Declared model set M",
        "empirical law P_hat",
        "confidence region Cn",
        "certified lower bound L > sampling radius",
        "A candidate best-fit model gives an upper bound on distance",
        "cannot by itself certify rejection",
        "Non-rejection is not model acceptance",
        "does not identify the latent state with consciousness",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text


def test_p77_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

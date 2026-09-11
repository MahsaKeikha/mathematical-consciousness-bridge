import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p72_target_measurement_channel_robustness.svg")
SVG_NS = "http://www.w3.org/2000/svg"


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def _number(value: str) -> float:
    return float(value.replace("px", ""))


def _group(root: ET.Element, group_id: str) -> ET.Element:
    for node in root.findall(f".//{{{SVG_NS}}}g"):
        if node.attrib.get("id") == group_id:
            return node
    raise AssertionError(f"missing SVG group: {group_id}")


def test_p72_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    desc = root.find(f"{{{SVG_NS}}}desc")
    assert desc is not None and desc.text is not None
    for token in (
        "follow the attached state-to-target-to-observation arrows",
        "can weaken or erase evidence",
        "not an assumed definition of consciousness",
    ):
        assert token in desc.text


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


def test_p72_all_rectangles_and_explicit_coordinates_fit_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for rect in root.findall(f".//{{{SVG_NS}}}rect"):
        x = _number(rect.attrib.get("x", "0"))
        y = _number(rect.attrib.get("y", "0"))
        width = _number(rect.attrib["width"])
        height = _number(rect.attrib["height"])
        assert x + width <= 1200
        assert y + height <= 760

    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= _number(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= _number(node.attrib[coordinate]) <= 760.0


def test_p72_internal_channel_arrows_are_attached_and_unambiguous() -> None:
    root = ET.parse(FIGURE).getroot()
    panel = _group(root, "data-processing-panel")
    connectors = [
        node
        for node in panel.findall(f"{{{SVG_NS}}}path")
        if node.attrib.get("marker-end") == "url(#arrow)"
    ]
    assert {node.attrib["d"] for node in connectors} == {
        "M195 227 L273 227",
        "M400 227 L473 227",
    }
    assert len(connectors) == 2


def test_p72_finite_sample_panel_wraps_explanatory_copy() -> None:
    root = ET.parse(FIGURE).getroot()
    panel = _group(root, "finite-sample-panel")
    lines = ["".join(node.itertext()) for node in panel.findall(f"{{{SVG_NS}}}text")]
    assert "Two same-T cases with categorical observed target Y." in lines
    assert "Declared observed-target alphabet size: dY." in lines
    assert "If gamma ≥ gamma0 and latent gap ≥ DeltaE, a sufficient bound is" in lines
    baselines = [
        _number(node.attrib["y"])
        for node in panel.findall(f"{{{SVG_NS}}}text")
    ]
    assert max(baselines) <= 696
    assert 700 - max(baselines) >= 4

import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p74_finite_sample_target_channel_recovery.svg")
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


def test_p74_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    title = root.find(f"{{{SVG_NS}}}title")
    desc = root.find(f"{{{SVG_NS}}}desc")
    assert title is not None and title.text is not None and "P74" in title.text
    assert desc is not None and desc.text is not None
    for token in (
        "four attached top-row stages",
        "Gate failure means not certified by the current data",
        "does not validate conditional independence",
    ):
        assert token in desc.text


def test_p74_svg_contains_certificate_and_failure_boundary() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P74 Finite-Sample Target-Channel Recovery",
        "8-cell empirical law P_hat",
        "|C_hat - C| <= 3 delta",
        "|M_hat - M| <= 13 delta",
        "Nondegeneracy",
        "NOT CERTIFIED",
        "qL = LM^2 / (U12 U13 U23)",
        "gamma_1,L = sqrt( L12 L13 / (vU U23) )",
        "does not validate conditional independence",
        "does not identify the latent state with consciousness",
    )
    for token in required:
        assert token in text


def test_p74_all_rectangles_and_coordinates_stay_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for rect in root.findall(f".//{{{SVG_NS}}}rect"):
        x = _number(rect.attrib.get("x", "0"))
        y = _number(rect.attrib.get("y", "0"))
        width = _number(rect.attrib["width"])
        height = _number(rect.attrib["height"])
        assert 0 <= x <= 1200
        assert 0 <= y <= 760
        assert x + width <= 1200
        assert y + height <= 760

    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= _number(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= _number(node.attrib[coordinate]) <= 760.0


def test_p74_narrow_stage_headings_are_deliberately_wrapped() -> None:
    root = ET.parse(FIGURE).getroot()
    confidence = _group(root, "confidence-event-panel")
    gate = _group(root, "nondegeneracy-gate-panel")

    confidence_lines = [
        "".join(node.itertext()) for node in confidence.findall(f"{{{SVG_NS}}}text")
    ]
    gate_lines = [
        "".join(node.itertext()) for node in gate.findall(f"{{{SVG_NS}}}text")
    ]
    assert "2. One shared" in confidence_lines
    assert "confidence event" in confidence_lines
    assert "3. Nondegeneracy" in gate_lines
    assert "gate" in gate_lines
    assert "Do not invert through a" in gate_lines
    assert "near-zero denominator." in gate_lines


def test_p74_top_stage_connectors_follow_card_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()
    connectors = [
        node
        for node in root.findall(f"{{{SVG_NS}}}path")
        if node.attrib.get("marker-end") == "url(#arrow)"
    ]
    assert {node.attrib["d"] for node in connectors} == {
        "M300 240 L334 240",
        "M580 240 L614 240",
        "M860 240 L894 240",
    }
    assert len(connectors) == 3
    for connector in connectors:
        assert connector.attrib["stroke-width"] == "3"
        assert connector.attrib["fill"] == "none"


def test_p74_lower_panels_preserve_safe_text_margins() -> None:
    root = ET.parse(FIGURE).getroot()
    for group_id in ("inversion-panel", "meaning-panel"):
        panel = _group(root, group_id)
        baselines = [
            _number(node.attrib["y"])
            for node in panel.findall(f"{{{SVG_NS}}}text")
        ]
        assert max(baselines) <= 634
        assert 640 - max(baselines) >= 6

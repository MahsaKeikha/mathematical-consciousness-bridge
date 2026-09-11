import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p76_finite_sample_target_model_adequacy.svg")
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


def test_p76_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    desc = root.find(f"{{{SVG_NS}}}desc")
    assert desc is not None and desc.text is not None
    for token in (
        "four attached top-row stages",
        "one-sided finite-sample falsification procedure",
        "not a model-acceptance rule",
    ):
        assert token in desc.text


def test_p76_svg_contains_finite_rejection_logic_and_boundary() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P76 Finite-Sample Target-Model Adequacy Rejection",
        "Sixteen-cell",
        "Shared",
        "Moment",
        "P75 polynomial",
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


def test_p76_all_rectangles_and_coordinates_stay_inside_canvas() -> None:
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


def test_p76_top_headings_are_wrapped_for_narrow_cards() -> None:
    root = ET.parse(FIGURE).getroot()
    expected = {
        "data-panel": ("1. Sixteen-cell", "IID data"),
        "confidence-panel": ("2. Shared", "confidence event"),
        "moment-panel": ("3. Moment", "confidence box"),
        "constraint-panel": ("4. P75 polynomial", "intervals"),
    }
    for group_id, required_lines in expected.items():
        panel = _group(root, group_id)
        lines = [
            "".join(node.itertext()) for node in panel.findall(f"{{{SVG_NS}}}text")
        ]
        for line in required_lines:
            assert line in lines
        baselines = [
            _number(node.attrib["y"])
            for node in panel.findall(f"{{{SVG_NS}}}text")
        ]
        assert max(baselines) <= 316
        assert 346 - max(baselines) >= 30


def test_p76_top_connectors_are_aligned_between_stage_cards() -> None:
    root = ET.parse(FIGURE).getroot()
    connectors = [
        node
        for node in root.findall(f"{{{SVG_NS}}}path")
        if node.attrib.get("marker-end") == "url(#arrow)"
    ]
    assert {node.attrib["d"] for node in connectors} == {
        "M300 237 L334 237",
        "M580 237 L614 237",
        "M860 237 L894 237",
    }
    assert len(connectors) == 3


def test_p76_outcome_panels_keep_long_reason_text_wrapped() -> None:
    root = ET.parse(FIGURE).getroot()
    nonrejection = _group(root, "nonrejection-panel")
    lines = [
        "".join(node.itertext())
        for node in nonrejection.findall(f"{{{SVG_NS}}}text")
    ]
    assert "finite sample | small violation | untracked misspecification" in lines
    assert "P75 full-law adequacy remains a stronger population audit." in lines
    baselines = [
        _number(node.attrib["y"])
        for node in nonrejection.findall(f"{{{SVG_NS}}}text")
    ]
    assert max(baselines) <= 596
    assert 624 - max(baselines) >= 28

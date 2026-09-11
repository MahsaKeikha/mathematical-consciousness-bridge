import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p75_target_model_adequacy_overidentification.svg")
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


def test_p75_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    title = root.find(f"{{{SVG_NS}}}title")
    description = root.find(f"{{{SVG_NS}}}desc")
    assert title is not None and title.text is not None
    assert description is not None and description.text is not None
    assert "P75" in title.text
    for token in (
        "parameter identifiability from model adequacy",
        "six overidentifying degrees of freedom",
        "follow the attached arrows",
        "Passing means compatibility",
        "not identification of the latent state with consciousness",
    ):
        assert token in description.text


def test_p75_svg_contains_adequacy_logic_and_scientific_boundary() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P75 Target-Model Adequacy and Four-View Overidentification",
        "7 = 7 | generically just-identified",
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


def test_p75_all_rectangles_fit_inside_canvas() -> None:
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


def test_p75_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= _number(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= _number(node.attrib[coordinate]) <= 760.0


def test_p75_top_panel_copy_is_wrapped_with_safe_bottom_margin() -> None:
    root = ET.parse(FIGURE).getroot()
    three = _group(root, "three-view-panel")
    four = _group(root, "four-view-panel")

    three_lines = ["".join(node.itertext()) for node in three.findall(f"{{{SVG_NS}}}text")]
    four_lines = ["".join(node.itertext()) for node in four.findall(f"{{{SVG_NS}}}text")]

    assert "P73 can recover parameters on the admissible" in three_lines
    assert "nondegenerate region." in three_lines
    assert "The declared target model can now be falsified," in four_lines
    assert "rather than only fitted." in four_lines

    for panel in (three, four):
        baselines = [
            _number(node.attrib["y"])
            for node in panel.findall(f"{{{SVG_NS}}}text")
        ]
        assert max(baselines) <= 375
        assert 388 - max(baselines) >= 13


def test_p75_connectors_are_attached_to_panels_and_lower_stage() -> None:
    root = ET.parse(FIGURE).getroot()
    connectors = [
        node
        for node in root.findall(f"{{{SVG_NS}}}path")
        if node.attrib.get("marker-end") == "url(#arrow)"
    ]
    assert len(connectors) == 2
    assert {node.attrib["d"] for node in connectors} == {
        "M316 388 L316 424",
        "M884 388 L884 424",
    }

    # Both arrows originate exactly at the bottom edge of the upper cards.
    # Their arrowheads terminate immediately against the lower panel at y=430.
    for connector in connectors:
        assert connector.attrib["stroke-width"] == "3"
        assert connector.attrib["fill"] == "none"

    lower_panel = _group(root, "adequacy-obligations-panel")
    lower_rect = lower_panel.find(f"{{{SVG_NS}}}rect")
    assert lower_rect is not None
    assert _number(lower_rect.attrib["y"]) == 430

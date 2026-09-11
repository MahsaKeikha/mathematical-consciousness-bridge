import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p78_certified_continuous_model_separation.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _find_text(root: ET.Element, token: str) -> ET.Element:
    for node in root.iter():
        if _local_name(node.tag) == "text" and token in "".join(node.itertext()):
            return node
    raise AssertionError(f"missing text node containing {token!r}")


def _find_rect(root: ET.Element, x: float, y: float) -> ET.Element:
    for node in root.iter():
        if _local_name(node.tag) != "rect":
            continue
        if float(node.attrib.get("x", -1)) == x and float(node.attrib.get("y", -1)) == y:
            return node
    raise AssertionError(f"missing rect at {(x, y)}")


def test_p78_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    text = _all_text(root)
    assert "What this figure shows:" in text
    assert "How to read it:" in text
    assert "Main takeaway:" in text
    assert "Scientific status:" in text


def test_p78_svg_contains_certified_continuous_separation_logic() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P78 Certified Continuous Model Separation",
        "P75 parameter cube: [0,1]^9",
        "Exact cell enclosure",
        "Certified box lower bound",
        "Exact Fraction arithmetic",
        "Global certified lower bound",
        "Candidate upper bound",
        "Certified bracket",
        "A best fit alone supplies only the upper side",
        "P77 rejection handoff",
        "valid sampling-radius upper bound",
        "Non-rejection is not model acceptance",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text


def test_p78_stage_connectors_attach_to_neighboring_panel_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()
    stage1 = _find_rect(root, 68.0, 140.0)
    stage2 = _find_rect(root, 432.0, 140.0)
    stage3 = _find_rect(root, 806.0, 140.0)

    assert float(stage1.attrib["x"]) + float(stage1.attrib["width"]) == 386.0
    assert float(stage2.attrib["x"]) == 432.0
    assert float(stage2.attrib["x"]) + float(stage2.attrib["width"]) == 760.0
    assert float(stage3.attrib["x"]) == 806.0

    expected = {("386", "432"), ("760", "806")}
    found: set[tuple[str, str]] = set()
    for node in root.iter():
        if _local_name(node.tag) != "line":
            continue
        pair = (node.attrib.get("x1", ""), node.attrib.get("x2", ""))
        if pair in expected and node.attrib.get("y1") == "337" and node.attrib.get("y2") == "337":
            assert node.attrib.get("marker-end") == "url(#arrow)"
            found.add(pair)

    assert found == expected


def test_p78_wrapped_explanations_stay_inside_their_cards() -> None:
    root = ET.parse(FIGURE).getroot()

    bound_card = _find_rect(root, 468.0, 344.0)
    left = float(bound_card.attrib["x"])
    right = left + float(bound_card.attrib["width"])
    top = float(bound_card.attrib["y"])
    bottom = top + float(bound_card.attrib["height"])
    for token in (
        "Certified box lower bound",
        "L(B) = max_x dist(P_hat(x), I_x(B))",
        "Every model law in B is at least L(B) away.",
    ):
        node = _find_text(root, token)
        x = float(node.attrib["x"])
        y = float(node.attrib["y"])
        assert left + 15 <= x <= right - 15
        assert top + 20 <= y <= bottom - 5

    bracket = _find_rect(root, 840.0, 424.0)
    bracket_bottom = float(bracket.attrib["y"]) + float(bracket.attrib["height"])
    for token in (
        "Certified bracket",
        "L_global <= d_inf(P_hat,M) <= U",
        "A best fit alone supplies only the upper side.",
    ):
        assert float(_find_text(root, token).attrib["y"]) < bracket_bottom

    handoff = _find_rect(root, 68.0, 566.0)
    handoff_bottom = float(handoff.attrib["y"]) + float(handoff.attrib["height"])
    assert float(_find_text(root, "Strict separation is required").attrib["y"]) < handoff_bottom


def test_p78_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

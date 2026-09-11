import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p77_full_law_model_set_separation.svg")


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


def test_p77_svg_has_publication_canvas_and_accessibility_metadata() -> None:
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


def test_p77_audit_transition_arrow_attaches_to_panel_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()
    left = _find_rect(root, 68.0, 138.0)
    right = _find_rect(root, 574.0, 138.0)
    left_edge = float(left.attrib["x"])
    left_right_edge = left_edge + float(left.attrib["width"])
    right_left_edge = float(right.attrib["x"])

    transition = None
    for node in root.iter():
        if _local_name(node.tag) != "line":
            continue
        if (
            node.attrib.get("x1") == "524"
            and node.attrib.get("x2") == "574"
            and node.attrib.get("y1") == "338"
            and node.attrib.get("y2") == "338"
        ):
            transition = node
            break

    assert transition is not None
    assert left_right_edge == 524.0
    assert right_left_edge == 574.0
    assert transition.attrib.get("marker-end") == "url(#arrow)"


def test_p77_wrapped_limitation_and_boundary_text_stay_inside_cards() -> None:
    root = ET.parse(FIGURE).getroot()

    limitation = _find_rect(root, 96.0, 352.0)
    limit_left = float(limitation.attrib["x"])
    limit_right = limit_left + float(limitation.attrib["width"])
    limit_top = float(limitation.attrib["y"])
    limit_bottom = limit_top + float(limitation.attrib["height"])

    for token in (
        "A law may satisfy every tracked equation and still fail",
        "membership in the complete declared model set.",
    ):
        node = _find_text(root, token)
        x = float(node.attrib["x"])
        y = float(node.attrib["y"])
        assert limit_left + 15 <= x <= limit_right - 15
        assert limit_top + 20 <= y <= limit_bottom - 5

    bottom = _find_rect(root, 68.0, 570.0)
    bottom_limit = float(bottom.attrib["y"]) + float(bottom.attrib["height"])
    for token in (
        "A candidate best-fit model gives an upper bound on distance.",
        "It cannot by itself certify rejection",
        "Non-rejection is not model acceptance.",
    ):
        assert float(_find_text(root, token).attrib["y"]) < bottom_limit


def test_p77_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

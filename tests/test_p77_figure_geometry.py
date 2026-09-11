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


def _find_by_id(root: ET.Element, element_id: str) -> ET.Element:
    for node in root.iter():
        if node.attrib.get("id") == element_id:
            return node
    raise AssertionError(f"missing element id={element_id!r}")


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

    transition = _find_by_id(root, "full-law-audit")
    assert _local_name(transition.tag) == "line"
    assert transition.attrib["x1"] == "524"
    assert transition.attrib["x2"] == "574"
    assert transition.attrib["y1"] == "338"
    assert transition.attrib["y2"] == "338"
    assert left_right_edge == 524.0
    assert right_left_edge == 574.0
    assert transition.attrib.get("marker-end") == "url(#arrow)"


def test_p77_constraint_cards_have_safe_padding_and_attached_connectors() -> None:
    root = ET.parse(FIGURE).getroot()
    limitation = _find_by_id(root, "p76-limitation")
    limitation_top = float(limitation.attrib["y"])

    cards = (
        ("p76-tetrads", "tetrad-to-limit"),
        ("p76-cross-triple", "cross-to-limit"),
        ("p76-fourth-moment", "moment-to-limit"),
    )
    for card_id, connector_id in cards:
        card = _find_by_id(root, card_id)
        connector = _find_by_id(root, connector_id)
        card_bottom = float(card.attrib["y"]) + float(card.attrib["height"])
        card_left = float(card.attrib["x"])
        card_right = card_left + float(card.attrib["width"])

        assert float(connector.attrib["y1"]) == card_bottom
        assert float(connector.attrib["y2"]) == limitation_top
        assert float(connector.attrib["x1"]) == float(connector.attrib["x2"])
        assert card_left + 20 <= float(connector.attrib["x1"]) <= card_right - 20
        assert connector.attrib.get("marker-end") == "url(#arrow)"

    fourth = _find_by_id(root, "p76-fourth-moment")
    fourth_left = float(fourth.attrib["x"])
    fourth_right = fourth_left + float(fourth.attrib["width"])
    for token in ("Fourth moment", "H123, H124", "H134"):
        node = _find_text(root, token)
        x = float(node.attrib["x"])
        assert fourth_left + 18 <= x <= fourth_right - 18
        assert node.attrib.get("text-anchor") == "middle"


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


def test_p77_certified_gap_touches_both_geometric_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()
    model = _find_by_id(root, "declared-model-set")
    confidence = _find_by_id(root, "confidence-region")
    gap = _find_by_id(root, "certified-gap")

    assert "930 328" in model.attrib["d"]
    assert gap.attrib["x1"] == "930"
    assert gap.attrib["y1"] == "328"
    assert gap.attrib["y2"] == "328"

    circle_left = float(confidence.attrib["cx"]) - float(confidence.attrib["r"])
    assert circle_left == 994.0
    assert float(gap.attrib["x2"]) == circle_left

    note = _find_by_id(root, "gap-note")
    note_right = float(note.attrib["x"]) + float(note.attrib["width"])
    assert note_right < float(confidence.attrib["cx"])


def test_p77_p77_panel_uses_deliberate_wrapping_for_long_explanations() -> None:
    root = ET.parse(FIGURE).getroot()
    right_panel = _find_by_id(root, "p77-panel")
    panel_left = float(right_panel.attrib["x"])
    panel_right = panel_left + float(right_panel.attrib["width"])

    for token in (
        "Reject only when the entire confidence region is disjoint",
        "from the entire declared model set.",
        "certified lower bound L > sampling radius",
        "=> Cn intersect M = empty",
    ):
        node = _find_text(root, token)
        x = float(node.attrib["x"])
        assert panel_left + 25 <= x <= panel_right - 25


def test_p77_svg_keeps_explicit_coordinates_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

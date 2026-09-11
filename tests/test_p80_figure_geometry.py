import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p80_simplex_coupled_model_separation.svg")


def _number(value: str) -> float:
    return float(value.replace("px", ""))


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def _find_rect(root: ET.Element, x: float, y: float) -> ET.Element:
    for node in root.iter():
        if _local_name(node.tag) != "rect":
            continue
        if _number(node.attrib.get("x", "-1")) == x and _number(node.attrib.get("y", "-1")) == y:
            return node
    raise AssertionError(f"missing rect at {(x, y)}")


def _find_text(root: ET.Element, token: str) -> ET.Element:
    for node in root.iter():
        if _local_name(node.tag) == "text" and token in "".join(node.itertext()):
            return node
    raise AssertionError(f"missing text containing {token!r}")


def test_p80_figure_has_accessible_title_and_description() -> None:
    root = ET.parse(FIGURE).getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}
    title = root.find("svg:title", ns)
    description = root.find("svg:desc", ns)

    assert title is not None
    assert title.text is not None and "P80" in title.text
    assert description is not None
    assert description.text is not None
    for token in (
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "Scientific status:",
        "simplex",
        "coordinate-overlap radius",
        "P79",
    ):
        assert token.lower() in description.text.lower()


def test_p80_figure_declares_expected_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    viewbox = [float(value) for value in root.attrib["viewBox"].split()]
    assert viewbox == [0.0, 0.0, 1200.0, 760.0]
    assert _number(root.attrib["width"]) == 1200.0
    assert _number(root.attrib["height"]) == 760.0


def test_p80_rectangles_and_text_fit_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        if _local_name(node.tag) == "rect":
            x = _number(node.attrib.get("x", "0"))
            y = _number(node.attrib.get("y", "0"))
            width = _number(node.attrib["width"])
            height = _number(node.attrib["height"])
            assert 0 <= x <= 1200
            assert 0 <= y <= 760
            assert x + width <= 1200
            assert y + height <= 760
        elif _local_name(node.tag) == "text":
            assert 0 <= _number(node.attrib["x"]) <= 1200
            assert 0 <= _number(node.attrib["y"]) <= 760


def test_p80_stage_connectors_attach_to_neighboring_panel_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()
    stage1 = _find_rect(root, 70.0, 145.0)
    stage2 = _find_rect(root, 445.0, 145.0)
    stage3 = _find_rect(root, 820.0, 145.0)

    assert _number(stage1.attrib["x"]) + _number(stage1.attrib["width"]) == 380.0
    assert _number(stage2.attrib["x"]) == 445.0
    assert _number(stage2.attrib["x"]) + _number(stage2.attrib["width"]) == 755.0
    assert _number(stage3.attrib["x"]) == 820.0

    expected = {("380", "445"), ("755", "820")}
    found: set[tuple[str, str]] = set()
    for node in root.iter():
        if _local_name(node.tag) != "path":
            continue
        d = node.attrib.get("d", "")
        if d == "M380 349 L445 349":
            assert node.attrib.get("marker-end") == "url(#arrow)"
            found.add(("380", "445"))
        elif d == "M755 349 L820 349":
            assert node.attrib.get("marker-end") == "url(#arrow)"
            found.add(("755", "820"))

    assert found == expected


def test_p80_radius_feasibility_text_stays_inside_card() -> None:
    root = ET.parse(FIGURE).getroot()
    card = _find_rect(root, 469.0, 369.0)
    left = _number(card.attrib["x"])
    right = left + _number(card.attrib["width"])
    top = _number(card.attrib["y"])
    bottom = top + _number(card.attrib["height"])

    for token in (
        "Exact radius feasibility",
        "r >= r_box = L78(B)",
        "sum max(l_i, p_i-r) <= 1",
        "1 <= sum min(u_i, p_i+r)",
    ):
        node = _find_text(root, token)
        x = _number(node.attrib["x"])
        y = _number(node.attrib["y"])
        assert left + 15 <= x <= right - 15
        assert top + 20 <= y <= bottom - 5


def test_p80_visual_contains_complete_certification_logic() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P78 box enclosure",
        "Intersect with the simplex",
        "Stronger certified bound",
        "R_delta subset R_box",
        "r >= r_box = L78(B)",
        "sum max(l_i, p_i-r) <= 1",
        "1 <= sum min(u_i, p_i+r)",
        "L80 = max(r_box, r_A, r_C)",
        "L80(B) >= L78(B)",
        "L80 > epsilon_upper  =>  reject",
        "computational certificate, not a consciousness-identification theorem",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text

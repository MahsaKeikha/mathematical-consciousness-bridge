import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p79_certified_sampling_radius.svg")


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


def test_p79_figure_has_accessible_title_and_description() -> None:
    root = ET.parse(FIGURE).getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}
    title = root.find("svg:title", ns)
    description = root.find("svg:desc", ns)

    assert title is not None
    assert title.text is not None and "P79" in title.text
    assert description is not None
    assert description.text is not None
    for token in (
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "Scientific status:",
        "exact-rational",
        "P78",
    ):
        assert token in description.text


def test_p79_figure_declares_a_valid_viewbox() -> None:
    root = ET.parse(FIGURE).getroot()
    viewbox = [float(value) for value in root.attrib["viewBox"].split()]
    assert viewbox == [0.0, 0.0, 1200.0, 760.0]
    assert _number(root.attrib["width"]) == 1200.0
    assert _number(root.attrib["height"]) == 760.0


def test_p79_primary_panels_and_text_fit_inside_canvas() -> None:
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


def test_p79_stage_connectors_attach_to_neighboring_panel_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()
    stage1 = _find_rect(root, 70.0, 142.0)
    stage2 = _find_rect(root, 435.0, 142.0)
    stage3 = _find_rect(root, 830.0, 142.0)

    assert _number(stage1.attrib["x"]) + _number(stage1.attrib["width"]) == 370.0
    assert _number(stage2.attrib["x"]) == 435.0
    assert _number(stage2.attrib["x"]) + _number(stage2.attrib["width"]) == 765.0
    assert _number(stage3.attrib["x"]) == 830.0

    expected = {("370", "435"), ("765", "830")}
    found: set[tuple[str, str]] = set()
    for node in root.iter():
        if _local_name(node.tag) != "line":
            continue
        pair = (node.attrib.get("x1", ""), node.attrib.get("x2", ""))
        if pair in expected and node.attrib.get("y1") == "338" and node.attrib.get("y2") == "338":
            assert node.attrib.get("marker-end") == "url(#arrow)"
            found.add(pair)

    assert found == expected


def test_p79_visual_contains_the_three_certification_stages_and_direction() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "Exact statistical inputs",
        "Certify log and square root",
        "Safe rejection comparison",
        "Positive atanh series",
        "Integer-certified dyadic",
        "square-root enclosure",
        "L_model <= d_inf(P_hat,M)",
        "epsilon <= epsilon_upper",
        "Strict certified gate",
        "L_model > epsilon_upper",
        "Only a strict certified lower-bound > certified upper-bound comparison",
        "Non-rejection is not model acceptance",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text


def test_p79_bottom_interpretation_stays_inside_band() -> None:
    root = ET.parse(FIGURE).getroot()
    band = _find_rect(root, 70.0, 568.0)
    band_bottom = _number(band.attrib["y"]) + _number(band.attrib["height"])
    for token in (
        "Certified P77/P78/P79 chain",
        "P78 lower-bounds model distance.",
        "Only a strict certified lower-bound",
        "Failure of the strict gate is inconclusive",
    ):
        assert _number(_find_text(root, token).attrib["y"]) < band_bottom

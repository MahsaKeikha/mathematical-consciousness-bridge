import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/consciousness_map.svg")


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _by_id(root: ET.Element, element_id: str) -> ET.Element:
    for node in root.iter():
        if node.attrib.get("id") == element_id:
            return node
    raise AssertionError(f"missing SVG element id={element_id!r}")


def _box(node: ET.Element) -> tuple[float, float, float, float]:
    x = float(node.attrib["x"])
    y = float(node.attrib["y"])
    return x, y, x + float(node.attrib["width"]), y + float(node.attrib["height"])


def _overlap(a: tuple[float, float, float, float], b: tuple[float, float, float, float]) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def test_consciousness_map_has_accessible_reader_guidance() -> None:
    root = ET.parse(FIGURE).getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}

    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "720"
    assert root.attrib["viewBox"] == "0 0 1200 720"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    title = root.find("svg:title", ns)
    description = root.find("svg:desc", ns)
    assert title is not None and title.text is not None and "Consciousness map" in title.text
    assert description is not None and description.text is not None
    for token in (
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "Scientific status:",
        "physical-to-experiential bridge remains open",
    ):
        assert token in description.text


def test_primary_cards_are_aligned_and_do_not_overlap() -> None:
    root = ET.parse(FIGURE).getroot()
    ids = ("theory-card", "measurement-card", "dynamics-card", "bridge-card")
    boxes = {element_id: _box(_by_id(root, element_id)) for element_id in ids}

    assert boxes["theory-card"] == (70.0, 145.0, 500.0, 315.0)
    assert boxes["measurement-card"] == (700.0, 145.0, 1130.0, 315.0)
    assert boxes["dynamics-card"] == (70.0, 390.0, 500.0, 560.0)
    assert boxes["bridge-card"] == (700.0, 390.0, 1130.0, 560.0)

    values = list(boxes.values())
    for index, first in enumerate(values):
        for second in values[index + 1 :]:
            assert not _overlap(first, second)

    assert boxes["measurement-card"][0] - boxes["theory-card"][2] == 200.0
    assert boxes["dynamics-card"][1] - boxes["theory-card"][3] == 75.0


def test_all_four_connectors_attach_exactly_to_card_boundaries() -> None:
    root = ET.parse(FIGURE).getroot()

    top = _by_id(root, "theory-measurement-arrow")
    assert (top.attrib["x1"], top.attrib["y1"], top.attrib["x2"], top.attrib["y2"]) == (
        "500",
        "230",
        "700",
        "230",
    )

    theory_down = _by_id(root, "theory-dynamics-arrow")
    assert (
        theory_down.attrib["x1"],
        theory_down.attrib["y1"],
        theory_down.attrib["x2"],
        theory_down.attrib["y2"],
    ) == ("285", "315", "285", "390")

    measurement_down = _by_id(root, "measurement-bridge-arrow")
    assert (
        measurement_down.attrib["x1"],
        measurement_down.attrib["y1"],
        measurement_down.attrib["x2"],
        measurement_down.attrib["y2"],
    ) == ("915", "315", "915", "390")

    bottom = _by_id(root, "dynamics-bridge-arrow")
    assert (
        bottom.attrib["x1"],
        bottom.attrib["y1"],
        bottom.attrib["x2"],
        bottom.attrib["y2"],
    ) == ("500", "475", "700", "475")

    for connector in (top, theory_down, measurement_down, bottom):
        assert connector.attrib.get("marker-end") == "url(#arrow)"


def test_connector_labels_have_dedicated_whitespace() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    for token in (
        "Theoretical sufficiency",
        "model-implied evolution",
        "measurement validity",
        "Dynamical sufficiency",
    ):
        assert token in text

    # The horizontal cards leave a 200-pixel corridor and the vertical rows
    # leave a 75-pixel corridor. Connector labels are deliberately confined
    # to those corridors rather than drawn over scientific card content.
    for node in root.iter():
        if _local_name(node.tag) != "rect":
            continue
        x = float(node.attrib.get("x", "0"))
        y = float(node.attrib.get("y", "0"))
        width = float(node.attrib.get("width", "0"))
        height = float(node.attrib.get("height", "0"))
        if 500 < x < 700:
            assert x + width <= 700
        if 315 < y < 390:
            assert y + height <= 390


def test_visible_copy_preserves_scientific_boundary() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "Consciousness Map",
        "Theory",
        "Measurement",
        "Dynamics",
        "Sufficiency bridge",
        "Interpretation boundary",
        "does not identify a physical state with consciousness",
        "The physical-to-experiential bridge remains open.",
    )
    for token in required:
        assert token in text


def test_every_visible_positioned_element_stays_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    positioned_tags = {"rect", "text", "line", "circle", "ellipse", "polygon", "polyline", "path"}

    for node in root.iter():
        if _local_name(node.tag) not in positioned_tags:
            continue
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 720.0

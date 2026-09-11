import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p69_dual_optimal_multiplier.svg"
NS = {"svg": "http://www.w3.org/2000/svg"}


def _float(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _font_size(text: ET.Element) -> float:
    if "font-size" in text.attrib:
        return float(text.attrib["font-size"])
    return {
        "stageTitle": 18.0,
        "body": 14.0,
        "note": 14.0,
    }.get(text.attrib.get("class", ""), 16.0)


def _point_on_boundary(
    point_x: float,
    point_y: float,
    block: tuple[float, float, float, float],
) -> bool:
    x, y, width, height = block
    right = x + width
    bottom = y + height
    return (
        point_x in {x, right} and y <= point_y <= bottom
    ) or (
        point_y in {y, bottom} and x <= point_x <= right
    )


def test_p69_figure_has_accessible_publication_canvas():
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "840"
    assert root.attrib["viewBox"] == "0 0 1200 840"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    text = " ".join("".join(node.itertext()) for node in root.iter())
    for token in (
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "Scientific status:",
        "physical-to-experiential bridge remains open",
    ):
        assert token in text


def test_p69_figure_text_stays_inside_declared_blocks():
    root = ET.parse(FIGURE).getroot()
    for group in root.findall("svg:g", NS):
        if not group.attrib.get("id", "").startswith("block-"):
            continue
        x = _float(group, "data-x")
        y = _float(group, "data-y")
        width = _float(group, "data-w")
        height = _float(group, "data-h")
        for text in group.findall("svg:text", NS):
            tx = _float(text, "x")
            ty = _float(text, "y")
            font_size = _font_size(text)
            content = "".join(text.itertext())
            conservative_width = len(content) * font_size * 0.58
            assert tx >= x + 12
            assert tx + conservative_width <= x + width - 12, (
                group.attrib["id"],
                content,
            )
            assert y + font_size <= ty <= y + height - 8, (
                group.attrib["id"],
                content,
            )


def test_p69_figure_connectors_attach_to_declared_blocks():
    root = ET.parse(FIGURE).getroot()
    blocks = {
        group.attrib["id"]: (
            _float(group, "data-x"),
            _float(group, "data-y"),
            _float(group, "data-w"),
            _float(group, "data-h"),
        )
        for group in root.findall("svg:g", NS)
        if group.attrib.get("id", "").startswith("block-")
    }
    arrows = [
        line
        for line in root.findall("svg:line", NS)
        if line.attrib.get("id", "").startswith("arrow-")
    ]
    assert len(arrows) == 5
    for arrow in arrows:
        source = arrow.attrib["data-source"]
        target = arrow.attrib["data-target"]
        assert source in blocks
        assert target in blocks
        assert source != target
        x1 = _float(arrow, "x1")
        y1 = _float(arrow, "y1")
        x2 = _float(arrow, "x2")
        y2 = _float(arrow, "y2")
        assert _point_on_boundary(x1, y1, blocks[source]), arrow.attrib["id"]
        assert _point_on_boundary(x2, y2, blocks[target]), arrow.attrib["id"]
        assert arrow.attrib.get("marker-end") == "url(#arrow)"


def test_p69_figure_connectors_do_not_cross_unrelated_midpoints():
    root = ET.parse(FIGURE).getroot()
    blocks = {
        group.attrib["id"]: (
            _float(group, "data-x"),
            _float(group, "data-y"),
            _float(group, "data-w"),
            _float(group, "data-h"),
        )
        for group in root.findall("svg:g", NS)
        if group.attrib.get("id", "").startswith("block-")
    }
    arrows = [
        line
        for line in root.findall("svg:line", NS)
        if line.attrib.get("id", "").startswith("arrow-")
    ]
    for arrow in arrows:
        source = arrow.attrib["data-source"]
        target = arrow.attrib["data-target"]
        x1 = _float(arrow, "x1")
        y1 = _float(arrow, "y1")
        x2 = _float(arrow, "x2")
        y2 = _float(arrow, "y2")
        midpoint_x = 0.5 * (x1 + x2)
        midpoint_y = 0.5 * (y1 + y2)
        for block_id, (x, y, width, height) in blocks.items():
            if block_id in {source, target}:
                continue
            assert not (x < midpoint_x < x + width and y < midpoint_y < y + height), (
                arrow.attrib["id"],
                block_id,
            )


def test_p69_figure_keeps_dual_primal_and_scientific_boundaries_visible():
    text = FIGURE.read_text(encoding="utf-8")
    required = [
        "Optimize the P68 lower-bound family without assuming strong duality.",
        "Contains 0: exact dual optimum.",
        "Q_low &lt;= q* &lt;= Q_up",
        "does not assume q* = U*_int",
        "Dual optimality is not, by itself, primal exactness",
        "not evidence about consciousness or quantum ontology",
        "The physical-to-experiential bridge remains open.",
    ]
    for token in required:
        assert token in text


def test_p69_explicit_coordinates_remain_inside_canvas():
    root = ET.parse(FIGURE).getroot()
    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0 <= float(node.attrib[coordinate]) <= 1200
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0 <= float(node.attrib[coordinate]) <= 840

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p69_dual_optimal_multiplier.svg"
NS = {"svg": "http://www.w3.org/2000/svg"}


def _float(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


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
            font_size = float(text.attrib.get("font-size", "16"))
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


def test_p69_figure_connectors_reference_existing_blocks_and_do_not_cross_them():
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
        for block_id, (x, y, width, height) in blocks.items():
            if block_id in {source, target}:
                continue
            midpoint_x = 0.5 * (x1 + x2)
            midpoint_y = 0.5 * (y1 + y2)
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
    ]
    for token in required:
        assert token in text

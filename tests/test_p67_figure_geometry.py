import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p67_global_integer_optimality_certificate.svg"
NS = {"svg": "http://www.w3.org/2000/svg"}


def _float(element, name):
    return float(element.attrib[name])


def test_p67_figure_text_stays_inside_declared_blocks():
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
            assert y + 12 <= ty <= y + height - 5, (
                group.attrib["id"],
                content,
            )


def test_p67_connectors_touch_declared_source_and_target_blocks():
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
    assert len(arrows) == 4

    expected_routes = {
        "arrow-1": ("block-candidate", "block-intervals"),
        "arrow-2": ("block-intervals", "block-intersection"),
        "arrow-3": ("block-intersection", "block-certified"),
        "arrow-4": ("block-intersection", "block-inconclusive"),
    }

    for line in arrows:
        source = line.attrib["data-source"]
        target = line.attrib["data-target"]
        assert expected_routes[line.attrib["id"]] == (source, target)
        assert source in blocks
        assert target in blocks
        x1, y1, x2, y2 = map(
            float,
            (
                line.attrib["x1"],
                line.attrib["y1"],
                line.attrib["x2"],
                line.attrib["y2"],
            ),
        )
        sx, sy, sw, sh = blocks[source]
        tx, ty, tw, th = blocks[target]
        source_touch = (
            abs(x1 - sx) <= 1
            or abs(x1 - (sx + sw)) <= 1
            or abs(y1 - sy) <= 1
            or abs(y1 - (sy + sh)) <= 1
        )
        target_touch = (
            abs(x2 - tx) <= 1
            or abs(x2 - (tx + tw)) <= 1
            or abs(y2 - ty) <= 1
            or abs(y2 - (ty + th)) <= 1
        )
        assert source_touch, line.attrib["id"]
        assert target_touch, line.attrib["id"]


def test_p67_figure_is_self_explanatory_and_preserves_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "sum c_e k_e = B",
        "lambda_low &lt;= lambda_high",
        "gate passes",
        "gate fails or budget is not tight",
        "Certified unrestricted P63 global optimum.",
        "Status: not certified",
        "This does not prove suboptimality.",
        "It is not a consciousness theorem or physical-to-experiential bridge theorem.",
        "It is not an empirical consciousness result or quantum-completeness claim.",
    ]:
        assert token in text

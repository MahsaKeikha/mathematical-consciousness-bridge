import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p68_lagrangian_optimality_gap.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
NS = {"svg": "http://www.w3.org/2000/svg"}
CLASS_FONT_SIZES = {
    "title": 30.0,
    "subtitle": 16.0,
    "stageTitle": 18.0,
    "body": 14.0,
    "note": 13.0,
    "math": 14.0,
}


def _float(element, name):
    return float(element.attrib[name])


def _font_size(text):
    if "font-size" in text.attrib:
        return float(text.attrib["font-size"])
    for class_name in text.attrib.get("class", "").split():
        if class_name in CLASS_FONT_SIZES:
            return CLASS_FONT_SIZES[class_name]
    return 16.0


def test_p68_figure_has_self_explanatory_accessible_description():
    root = ET.parse(FIGURE).getroot()
    title = root.find("svg:title", NS)
    desc = root.find("svg:desc", NS)

    assert title is not None
    assert desc is not None
    title_text = "" if title.text is None else " ".join(title.text.split())
    desc_text = "" if desc.text is None else " ".join(desc.text.split())

    assert "P68" in title_text
    for phrase in (
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "Scientific status:",
        "every positive multiplier gives a valid lower bound",
        "physical-to-experiential bridge remains open",
    ):
        assert phrase in desc_text


def test_p68_figure_text_stays_inside_declared_blocks():
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
            assert y + 12 <= ty <= y + height - 10, (
                group.attrib["id"],
                content,
            )


def test_p68_connectors_reference_blocks_and_touch_boundaries():
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
    assert len(arrows) == 6

    expected_routes = {
        "arrow-1": ("block-candidate", "block-lambda"),
        "arrow-2": ("block-lambda", "block-edge"),
        "arrow-3": ("block-edge", "block-dual"),
        "arrow-4": ("block-dual", "block-additive"),
        "arrow-5": ("block-dual", "block-multiplicative"),
        "arrow-6": ("block-additive", "block-p67"),
    }

    for line in arrows:
        arrow_id = line.attrib["id"]
        source = line.attrib["data-source"]
        target = line.attrib["data-target"]
        assert expected_routes[arrow_id] == (source, target)
        assert source in blocks
        assert target in blocks
        assert line.attrib.get("marker-end") == "url(#arrow)"

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
        assert source_touch, arrow_id
        assert target_touch, arrow_id


def test_p68_figure_preserves_weak_duality_gap_and_positivity_gate():
    text = FIGURE.read_text(encoding="utf-8")
    for token in (
        "q(lambda) &lt;= U*_int(B) &lt;= U(k)",
        "0 &lt;= U(k)-U* &lt;= U(k)-q(lambda)",
        "If q(lambda) &gt; 0:",
        "U(k)/U* &lt;= U(k)/q(lambda)",
        "If q &lt;= 0, keep the additive certificate.",
        "P67 zero-gap special case",
        "=&gt; q(lambda) = U(k) = U*_int(B).",
        "Not a consciousness theorem",
        "physical-to-experiential bridge remains open",
    ):
        assert token in text


def test_p68_catalog_row_is_self_explanatory_and_linked():
    catalog = CATALOG.read_text(encoding="utf-8")
    matching_rows = [
        line
        for line in catalog.splitlines()
        if "(figures/p68_lagrangian_optimality_gap.svg)" in line
    ]
    assert len(matching_rows) == 1
    row = matching_rows[0]
    for token in (
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "every positive multiplier gives a valid lower bound",
        "physical-to-experiential bridge remains open",
        "[Proposition 68](proposition_68_lagrangian_optimality_gap.md)",
    ):
        assert token in row

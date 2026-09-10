from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p66_residual_exact_calibration_augmentation.svg"
NS = {"svg": "http://www.w3.org/2000/svg"}


def _float(element, name):
    return float(element.attrib[name])


def test_p66_figure_text_stays_inside_declared_blocks():
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
            assert y + 12 <= ty <= y + height - 10, (
                group.attrib["id"],
                content,
            )


def test_p66_connectors_reference_existing_blocks_and_touch_boundaries():
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

    for line in arrows:
        source = line.attrib["data-source"]
        target = line.attrib["data-target"]
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


def test_p66_figure_preserves_exactness_and_scientific_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "0 ≤ R &lt; Σ c_e = B₀",
        "Globally exact within k ≥ f.",
        "factor₆₆ ≤ factor₆₅ ≤ √2",
        "P63 remains globally exact",
        "not a consciousness or quantum-ontology theorem",
    ]:
        assert token in text

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p65_lower_bounded_heterogeneous_calibration.svg"
NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {
    "head": 18.0,
    "copy": 15.0,
    "small": 14.0,
    "eq": 16.0,
    "strong": 17.0,
}
WIDTH_FACTOR = 0.58


def _float(element, name):
    return float(element.attrib[name])


def _visible(element):
    return " ".join("".join(element.itertext()).split())


def test_p65_text_stays_inside_declared_blocks():
    root = ET.parse(FIGURE).getroot()
    blocks = [
        group
        for group in root.findall("svg:g", NS)
        if group.attrib.get("id", "").startswith("block-")
    ]
    assert len(blocks) == 7

    for block in blocks:
        x = _float(block, "data-x")
        y = _float(block, "data-y")
        width = _float(block, "data-w")
        height = _float(block, "data-h")
        rect = block.find("svg:rect", NS)
        assert rect is not None
        assert _float(rect, "x") == x
        assert _float(rect, "y") == y
        assert _float(rect, "width") == width
        assert _float(rect, "height") == height

        for label in block.findall("svg:text", NS):
            css_class = label.attrib.get("class")
            assert css_class in FONT_SIZE
            font_size = FONT_SIZE[css_class]
            label_x = _float(label, "x")
            label_y = _float(label, "y")
            estimated_width = len(_visible(label)) * font_size * WIDTH_FACTOR
            if label.attrib.get("text-anchor") == "middle":
                left = label_x - estimated_width / 2
                right = label_x + estimated_width / 2
            else:
                left = label_x
                right = label_x + estimated_width
            assert left >= x + 12, (block.attrib["id"], _visible(label))
            assert right <= x + width - 12, (block.attrib["id"], _visible(label))
            assert y + 12 <= label_y <= y + height - 5, (
                block.attrib["id"],
                _visible(label),
            )


def test_p65_connectors_keep_declared_block_topology():
    root = ET.parse(FIGURE).getroot()
    connectors = {
        path.attrib["id"]: (
            path.attrib["data-source"],
            path.attrib["data-target"],
            path.attrib["d"],
        )
        for path in root.findall("svg:path", NS)
        if path.attrib.get("id", "").startswith("arrow-")
    }
    assert connectors == {
        "arrow-1": ("block-p64-limit", "block-problem", "M385 240 H435"),
        "arrow-2": ("block-problem", "block-active", "M765 240 H815"),
        "arrow-3": ("block-problem", "block-water", "M600 350 V410"),
        "arrow-4": ("block-active", "block-water", "M980 350 V380 H900 V410"),
        "arrow-5": ("block-water", "block-floor", "M420 615 V675"),
        "arrow-6": ("block-water", "block-certificate", "M780 615 V675"),
    }


def test_p65_figure_is_self_explanatory_and_preserves_claim_boundaries():
    source = FIGURE.read_text(encoding="utf-8")
    for phrase in (
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "P62 may give n*ₑ &lt; 1",
        "B ≥ B₀ = Σₑ cₑ.",
        "Free edge: τ &gt; tₑ",
        "n*ₑ = max{1, τ (bₑ / cₑ)^(2/3)}",
        "kₑ = ⌊n*ₑ⌋ ≥ 1",
        "rmin ≥ 1/2",
        "U(k) ≤ √2 U*int(B)",
        "P63 remains the exact integer solver.",
        "It makes no claim that a calibration variable is consciousness",
        "P65 also does not establish a physical-to-experiential bridge.",
    ):
        assert phrase in source
    assert "\u2013" not in source
    assert "\u2014" not in source

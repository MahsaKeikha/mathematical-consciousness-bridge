import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p59_optimal_transition_calibration.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
NS = {"svg": "http://www.w3.org/2000/svg"}
WIDTH_FACTOR = 0.58
FONT_SIZE = {
    "head": 18.0,
    "copy": 15.0,
    "small": 14.0,
    "eq": 16.0,
    "strong": 17.0,
}
ROUTES = {
    "arrow-1": ("block-uncertainty", "block-optimum", "M220 330 V360 H380 V390"),
    "arrow-2": ("block-weight", "block-optimum", "M600 330 V390"),
    "arrow-3": ("block-budget", "block-optimum", "M980 330 V360 H820 V390"),
    "arrow-4": ("block-optimum", "block-law", "M300 615 V650 H220 V680"),
    "arrow-5": ("block-optimum", "block-target", "M600 615 V680"),
    "arrow-6": ("block-optimum", "block-handoff", "M900 615 V650 H980 V680"),
}


def _float(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_p59_text_stays_inside_declared_blocks():
    root = ET.parse(FIGURE).getroot()
    blocks = [
        group
        for group in root.findall("svg:g", NS)
        if group.attrib.get("id", "").startswith("block-")
    ]
    assert len(blocks) == 8

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
            estimated_width = len(_visible(label)) * FONT_SIZE[css_class] * WIDTH_FACTOR
            label_x = _float(label, "x")
            label_y = _float(label, "y")
            if label.attrib.get("text-anchor") == "middle":
                left = label_x - estimated_width / 2.0
                right = label_x + estimated_width / 2.0
            else:
                left = label_x
                right = label_x + estimated_width
            assert left >= x + 12, (block.attrib["id"], _visible(label))
            assert right <= x + width - 12, (block.attrib["id"], _visible(label))
            assert y + 12 <= label_y <= y + height - 5, (
                block.attrib["id"],
                _visible(label),
            )


def test_p59_connectors_keep_continuous_optimization_topology():
    root = ET.parse(FIGURE).getroot()
    arrows = [
        path
        for path in root.findall("svg:path", NS)
        if path.attrib.get("id", "").startswith("arrow-")
    ]
    actual = {
        path.attrib["id"]: (
            path.attrib["data-source"],
            path.attrib["data-target"],
            path.attrib["d"],
        )
        for path in arrows
    }
    assert actual == ROUTES


def test_p59_figure_preserves_optimum_threshold_and_scope_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "P59 exact continuous transition-calibration allocation",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "ρₑ(nₑ) = aₑ / √nₑ",
        "bₑ = wₑ aₑ",
        "Σₑ nₑ = N",
        "U(n) = Σₑ bₑ / √nₑ",
        "S = Σⱼ bⱼ^(2/3)",
        "nₑ* = N bₑ^(2/3) / S",
        "U*(N) = S^(3/2) / √N",
        "iff N ≥ S³ / ε²",
        "P60 gives hard-budget integer",
        "P61 gives the exact",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p59_catalog_explains_continuous_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P59 exact continuous transition-calibration allocation" in text
    assert "unique two-thirds-power allocation" in text
    assert "necessary-and-sufficient target-budget condition" in text
    assert "fractional allocations require a separate integer implementation" in text
    assert "physical-to-experiential bridge" in text

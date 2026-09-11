import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p61_exact_integer_transition_calibration.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 18.0, "copy": 15.0, "small": 14.0, "eq": 16.0, "strong": 17.0}
WIDTH_FACTOR = 0.58

EXPECTED_ROUTES = {
    "arrow-1": ("block-baseline", "block-gain", "M385 230 H435"),
    "arrow-2": ("block-gain", "block-greedy", "M765 230 H815"),
    "arrow-3": ("block-gain", "block-exactness", "M600 330 V390"),
    "arrow-4": ("block-greedy", "block-exactness", "M980 330 V360 H900 V390"),
    "arrow-5": ("block-exactness", "block-certificate", "M300 615 V650 H220 V680"),
    "arrow-6": ("block-exactness", "block-global", "M600 615 V680"),
    "arrow-7": ("block-exactness", "block-complexity", "M900 615 V650 H980 V680"),
}


def _float(element, name):
    return float(element.attrib[name])


def _visible(element):
    return " ".join("".join(element.itertext()).split())


def test_p61_text_stays_inside_declared_blocks():
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
            assert y + 12 <= label_y <= y + height - 4, (
                block.attrib["id"],
                _visible(label),
            )


def test_p61_connectors_keep_exact_greedy_topology():
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
    assert actual == EXPECTED_ROUTES


def test_p61_figure_preserves_exactness_certificate_complexity_and_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "P61 exact unit-cost integer transition calibration",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "B ≥ m = |E|",
        "R = B - m",
        "Δₑ(k) = bₑ [",
        "eₜ ∈ arg maxₑ Δₑ(kₑ)",
        "Δₑ(k+1) &lt; Δₑ(k) for every edge and k ≥ 1",
        "Repeatedly taking the largest available next gain is globally optimal.",
        "≥ largest next unused gain",
        "U(kᴾ⁶¹) ≤ U(k)",
        "Ties can produce nonunique optima.",
        "O(m + (B-m) log m)",
        "memory O(m)",
        "equal-unit-cost separable integer calibration surrogate",
        "not asserted for heterogeneous costs",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p61_catalog_explains_exact_unit_cost_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P61 exact unit-cost integer transition calibration" in text
    assert "strictly diminishing per-edge gains and prefix feasibility" in text
    assert "does not extend the same greedy proof to heterogeneous costs" in text
    assert "physical-to-experiential bridge" in text

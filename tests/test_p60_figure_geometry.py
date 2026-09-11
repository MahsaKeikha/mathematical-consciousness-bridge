import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p60_integer_transition_calibration.svg"
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
    "arrow-1": ("block-budget", "block-continuous", "M385 230 H435"),
    "arrow-2": ("block-continuous", "block-round", "M765 230 H815"),
    "arrow-3": ("block-continuous", "block-certificate", "M600 330 V390"),
    "arrow-4": ("block-round", "block-certificate", "M980 330 V360 H900 V390"),
    "arrow-5": ("block-certificate", "block-overhead", "M300 615 V650 H220 V680"),
    "arrow-6": ("block-certificate", "block-target", "M600 615 V680"),
    "arrow-7": ("block-certificate", "block-scope", "M900 615 V650 H980 V680"),
}


def _float(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_p60_text_stays_inside_declared_blocks():
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


def test_p60_connectors_keep_rounding_certificate_topology():
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


def test_p60_figure_preserves_budget_overhead_and_scope_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "P60 hard-budget integer rounding with certified overhead",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "B &gt; m = |E|",
        "N₀ = B - m &gt; 0",
        "kₑ = ceil(ñₑ)",
        "Σₑ kₑ ≤ B - 1 &lt; B",
        "U(k) ≤ U*(B - m) = S^(3/2) / √(B - m)",
        "√[B / (B - m)]",
        "S³ / ε² )",
        "P61 gives the exact integer",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p60_catalog_explains_constructive_not_exact_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P60 hard-budget integer rounding with certified overhead" in text
    assert "deliberately reduced budget N0 = B - m" in text
    assert "explicit worst-case overhead" in text
    assert "not claimed to be the exact integer optimum" in text
    assert "physical-to-experiential bridge" in text

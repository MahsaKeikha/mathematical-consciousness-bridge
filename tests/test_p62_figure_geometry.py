import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p62_heterogeneous_cost_transition_calibration.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 18.0, "copy": 15.0, "small": 14.0, "eq": 16.0, "strong": 17.0}
WIDTH_FACTOR = 0.58

EXPECTED_ROUTES = {
    "arrow-1": ("block-importance", "block-problem", "M385 230 H435"),
    "arrow-2": ("block-cost", "block-problem", "M815 230 H765"),
    "arrow-3": ("block-problem", "block-optimum", "M600 330 V390"),
    "arrow-4": ("block-optimum", "block-count", "M300 615 V650 H220 V680"),
    "arrow-5": ("block-optimum", "block-share", "M600 615 V680"),
    "arrow-6": ("block-optimum", "block-target", "M900 615 V650 H980 V680"),
}


def _float(element, name):
    return float(element.attrib[name])


def _visible(element):
    return " ".join("".join(element.itertext()).split())


def test_p62_text_stays_inside_declared_blocks():
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


def test_p62_connectors_keep_declared_continuous_optimization_topology():
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


def test_p62_figure_preserves_exact_continuous_results_and_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "P62 exact heterogeneous-cost continuous calibration",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "bₑ = wₑ aₑ &gt; 0",
        "Σₑ cₑnₑ = B",
        "T = Σⱼ bⱼ^(2/3)cⱼ^(1/3)",
        "nₑ* = (B/T) bₑ^(2/3)cₑ^(-2/3)",
        "U*(B) = T^(3/2) / √B",
        "nₑ* ∝ bₑ^(2/3)cₑ^(-2/3)",
        "cₑnₑ* ∝ bₑ^(2/3)cₑ^(1/3)",
        "iff B ≥ T^3 / ε^2",
        "P62 reduces exactly to P59",
        "heterogeneous integer counts are the separate P63 problem",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p62_catalog_explains_continuous_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P62 exact heterogeneous-cost continuous calibration" in text
    assert "sample count and budget share scale with different powers of cost" in text
    assert "heterogeneous integer counts are a separate P63 problem" in text
    assert "physical-to-experiential bridge" in text

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p64_fast_heterogeneous_integer_approximation.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 18.0, "copy": 15.0, "small": 14.0, "eq": 16.0, "strong": 17.0}
WIDTH_FACTOR = 0.58

EXPECTED_ROUTES = {
    "arrow-1": ("block-continuous", "block-gate", "M385 240 H435"),
    "arrow-2": ("block-gate", "block-floor", "M765 240 H815"),
    "arrow-3": ("block-floor", "block-certificate", "M980 350 V380 H780 V410"),
    "arrow-4": ("block-certificate", "block-uniform", "M420 635 V695"),
    "arrow-5": ("block-certificate", "block-scope", "M780 635 V695"),
}


def _float(element, name):
    return float(element.attrib[name])


def _visible(element):
    return " ".join("".join(element.itertext()).split())


def test_p64_text_stays_inside_declared_blocks():
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


def test_p64_connectors_keep_the_declared_dependency_topology():
    root = ET.parse(FIGURE).getroot()
    arrows = [
        path
        for path in root.findall("svg:path", NS)
        if path.attrib.get("id", "").startswith("arrow-")
    ]
    assert len(arrows) == 5

    actual = {
        path.attrib["id"]: (
            path.attrib["data-source"],
            path.attrib["data-target"],
            path.attrib["d"],
        )
        for path in arrows
    }
    assert actual == EXPECTED_ROUTES


def test_p64_figure_preserves_applicability_and_scientific_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "<title id=\"title\">P64 fast certified heterogeneous-cost integer approximation</title>",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "nₑ* ≥ 1 for every edge",
        "Gate failure means P64 is",
        "kₑ = floor(nₑ*) ≥ 1",
        "U(kfloor) ≤ (1 / √rmin) U*int(B)",
        "factor ≤ √[ν / (ν - 1)]",
        "Use P65 for a baseline-safe continuous route;",
        "P63 remains the unrestricted exact integer solver.",
        "does not identify consciousness, establish a physical-to-experiential bridge",
        "or imply quantum incompleteness",
    ]:
        assert token in text


def test_p64_catalog_explains_the_regime_gate_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P64 fast certified heterogeneous-cost integer approximation" in text
    assert "only in the regime where every continuous count is at least one" in text
    assert "P65 provides the baseline-safe continuous route" in text
    assert "P63 remains the unrestricted exact integer solver" in text

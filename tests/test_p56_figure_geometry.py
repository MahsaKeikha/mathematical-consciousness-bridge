import xml.etree.ElementTree as ET
from pathlib import Path

# Publication regression guard for the finalized P56 visual certificate.
ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p56_moving_start_metric_reoptimization_stability.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
NS = {"svg": "http://www.w3.org/2000/svg"}
WIDTH_FACTOR = 0.54
FONT_SIZE = {
    "head": 18.0,
    "copy": 15.0,
    "small": 13.5,
    "eq": 15.0,
    "strong": 16.0,
}
ROUTES = {
    "arrow-1": ("block-metric", "block-lipschitz", "M220 315 V350 H360 V385"),
    "arrow-2": ("block-old", "block-lipschitz", "M600 315 V385"),
    "arrow-3": ("block-new", "block-lipschitz", "M980 315 V350 H840 V385"),
    "arrow-4": ("block-lipschitz", "block-fixed", "M300 635 V660 H220 V685"),
    "arrow-5": ("block-lipschitz", "block-combined", "M600 635 V685"),
    "arrow-6": ("block-lipschitz", "block-strict", "M900 635 V660 H980 V685"),
}


def _float(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_p56_publication_canvas_and_accessibility():
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "1000"
    assert root.attrib["viewBox"] == "0 0 1200 1000"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"
    title = root.find("svg:title", NS)
    desc = root.find("svg:desc", NS)
    assert title is not None
    assert desc is not None
    assert title.attrib["id"] == "title"
    assert desc.attrib["id"] == "desc"
    description = _visible(desc)
    for phrase in [
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "Scientific status:",
    ]:
        assert phrase in description


def test_p56_text_stays_inside_declared_blocks():
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
        assert 0 <= x < 1200
        assert 0 <= y < 1000
        assert x + width <= 1200
        assert y + height <= 1000

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


def test_p56_connectors_preserve_start_perturbation_topology():
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


def test_p56_figure_preserves_theorem_and_scientific_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "P56 moving-start metric reoptimization stability",
        "one finite metric c",
        "Triangle inequality is essential.",
        "start s, active support S",
        "start s′, same support S",
        "|L*(S;s) - L*(S;s′)| ≤ c(s,s′)",
        "c(s′,v₁) ≤ c(s′,s) + c(s,v₁)",
        "Coefficient one is sharp",
        "|C*(r;s)-C*(r;s′)|",
        "Δfixed=C*(r;s)-C*(r′;s) ≥ 0",
        "≥ Δfixed-c(s,s′)",
        "Δfixed &gt; c(s,s′)",
        "Sufficient only; converse not claimed.",
        "changing metric requires the separate P57 perturbation theorem",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p56_catalog_explains_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P56 moving-start metric reoptimization stability" in text
    assert "one-Lipschitz" in text
    assert "coefficient one is sharp" in text
    assert "converse is not claimed" in text
    assert "physical-to-experiential bridge" in text

import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p57_switching_metric_perturbation.svg"
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
    "arrow-1": ("block-old", "block-combined", "M220 320 V365 H360 V390"),
    "arrow-2": ("block-new", "block-combined", "M600 320 V390"),
    "arrow-3": ("block-metric", "block-combined", "M980 320 V365 H840 V390"),
    "arrow-4": ("block-combined", "block-q", "M300 650 V675 H220 V700"),
    "arrow-5": ("block-combined", "block-strict", "M600 650 V700"),
    "arrow-6": ("block-combined", "block-reuse", "M900 650 V675 H980 V700"),
}


def _float(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_p57_text_stays_inside_declared_blocks():
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


def test_p57_connectors_keep_perturbation_certificate_topology():
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


def test_p57_figure_preserves_metric_perturbation_theorem_and_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "P57 deterministic switching-metric perturbation stability",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "c is a declared valid finite metric.",
        "c′ is another valid finite metric.",
        "δ = maxₓ,ᵧ |c(x,y)-c′(x,y)|",
        "≤ q(S;s) δ",
        "Δfixed = C*c(r;s) - C*c(r′;s) ≥ 0",
        "A = c(s,s′) + q(S′;s′)δ",
        "B = q(S′;s)δ + c′(s,s′)",
        "P57 = min{A, B}",
        "C*c(r;s) - C*c′(r′;s′) ≥ Δfixed - P57",
        "q=|S|-1: no start or s∈S",
        "q=|S|: s∉S",
        "The coefficient is sharp in general.",
        "Δfixed &gt; P57",
        "Sufficient only; converse not claimed.",
        "L*c′(S;s′) ≤ ℓc′(π*c;s′)",
        "metric estimation is a separate statistical problem",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p57_catalog_explains_deterministic_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P57 deterministic switching-metric perturbation stability" in text
    assert "two valid finite metrics" in text
    assert "route-reuse upper bound" in text
    assert "converse is not claimed" in text
    assert "physical-to-experiential bridge" in text

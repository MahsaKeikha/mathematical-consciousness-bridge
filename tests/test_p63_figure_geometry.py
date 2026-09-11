import pathlib
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
WIDTH_FACTOR = 0.58

P63_FIGURE = ROOT / "docs/figures/p63_exact_heterogeneous_integer_calibration.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
P63_FONT_SIZE = {
    "head": 18.0,
    "copy": 15.0,
    "small": 14.0,
    "eq": 16.0,
    "strong": 17.0,
}
P63_ROUTES = {
    "arrow-1": ("block-greedy", "block-problem", "M385 240 H435"),
    "arrow-2": ("block-problem", "block-state", "M765 240 H815"),
    "arrow-3": ("block-problem", "block-bellman", "M600 350 V410"),
    "arrow-4": ("block-state", "block-bellman", "M980 350 V380 H900 V410"),
    "arrow-5": ("block-bellman", "block-gcd", "M300 630 V660 H220 V690"),
    "arrow-6": ("block-bellman", "block-complexity", "M600 630 V690"),
    "arrow-7": ("block-bellman", "block-benchmark", "M900 630 V660 H980 V690"),
}


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_p63_text_stays_inside_declared_blocks():
    svg = ET.parse(P63_FIGURE).getroot()
    blocks = [
        group
        for group in svg.findall("svg:g", SVG_NS)
        if group.attrib.get("id", "").startswith("block-")
    ]
    assert len(blocks) == 8

    for block in blocks:
        x = _value(block, "data-x")
        y = _value(block, "data-y")
        width = _value(block, "data-w")
        height = _value(block, "data-h")
        rect = block.find("svg:rect", SVG_NS)
        assert rect is not None
        assert _value(rect, "x") == x
        assert _value(rect, "y") == y
        assert _value(rect, "width") == width
        assert _value(rect, "height") == height

        for label in block.findall("svg:text", SVG_NS):
            css_class = label.attrib.get("class")
            assert css_class in P63_FONT_SIZE
            estimated_width = len(_visible(label)) * P63_FONT_SIZE[css_class] * WIDTH_FACTOR
            label_x = _value(label, "x")
            label_y = _value(label, "y")
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


def test_p63_connectors_keep_exact_solver_topology():
    svg = ET.parse(P63_FIGURE).getroot()
    arrows = [
        path
        for path in svg.findall("svg:path", SVG_NS)
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
    assert actual == P63_ROUTES


def test_p63_figure_preserves_exactness_complexity_and_scientific_boundaries():
    text = P63_FIGURE.read_text(encoding="utf-8")
    for token in [
        "P63 exact heterogeneous-cost integer calibration",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "B ≥ Σₑ cₑ.",
        "F₀(0)=0",
        "U*int(B) = min over 0 ≤ s ≤ B of Fₘ(s)",
        "g = gcd{cₑ}",
        "O(m B'^2)",
        "Pseudo-polynomial in numeric B'.",
        "Not an NP-hardness claim by itself.",
        "U*cont(B) ≤ U*int(B)",
        "Unspent budget is allowed",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p63_catalog_explains_exact_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P63 exact heterogeneous-cost integer calibration" in text
    assert "exact-spend Bellman dynamic program" in text
    assert "pseudo-polynomial in the compressed numeric budget" in text
    assert "not an NP-hardness claim" in text

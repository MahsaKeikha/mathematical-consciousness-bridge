import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p54_metric_switching_cost_residual_scheduling.svg"
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
    "arrow-1": ("block-residual", "block-batching", "M220 315 V350 H360 V385"),
    "arrow-2": ("block-metric", "block-batching", "M600 315 V385"),
    "arrow-3": ("block-schedule", "block-batching", "M980 315 V350 H840 V385"),
    "arrow-4": ("block-batching", "block-routing", "M300 655 V680 H220 V705"),
    "arrow-5": ("block-batching", "block-dp", "M600 655 V705"),
    "arrow-6": ("block-batching", "block-interpretation", "M900 655 V680 H980 V705"),
}


def _float(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_p54_publication_canvas_and_accessibility():
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


def test_p54_text_stays_inside_declared_blocks():
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


def test_p54_connectors_preserve_batching_topology():
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


def test_p54_figure_preserves_theorem_and_scientific_boundaries():
    root = ET.parse(FIGURE).getroot()
    visible = _visible(root)
    for token in [
        "P54 metric switching-cost residual scheduling",
        "rᵢ ∈ Z≥0, V+={i:rᵢ>0}",
        "R=Σᵢrᵢ, fixed acquisition=aR",
        "finite metric c on setup points",
        "c(u,w) ≤ c(u,v)+c(v,w)",
        "Repeated visits allowed initially.",
        "Csw(σbar) ≤ Csw(σ)",
        "An optimal schedule exists with one contiguous block per preparation.",
        "C*total=aΣrᵢ+L*(V+;s)",
        "Shortest Hamiltonian path; no return.",
        "D(S,j)=min k∈S\\{j}",
        "L*=minⱼ D(V+,j)",
        "O(m²2ᵐ) time; O(m2ᵐ) states.",
        "P54 does not validate pruning.",
        "nonmetric costs",
        "physical-to-experiential bridge remains open",
        "quantum incompleteness is not implied",
    ]:
        assert token in visible
    raw = FIGURE.read_text(encoding="utf-8")
    assert "\u2013" not in raw
    assert "\u2014" not in raw


def test_p54_catalog_explains_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8").lower()
    assert "p54 metric switching-cost residual scheduling" in text
    assert "metric batching" in text
    assert "shortest hamiltonian path" in text
    assert "held-karp" in text
    assert "physical-to-experiential bridge" in text

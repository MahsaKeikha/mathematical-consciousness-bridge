import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs/figures/p58_finite_data_metric_uncertainty.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
NS = {"svg": "http://www.w3.org/2000/svg"}
WIDTH_FACTOR = 0.54
FONT_SIZE = {
    "head": 18.0,
    "copy": 15.0,
    "small": 14.0,
    "eq": 15.0,
    "strong": 17.0,
}
ROUTES = {
    "arrow-1": ("block-model", "block-event", "M385 237 H435"),
    "arrow-2": ("block-event", "block-envelope", "M765 237 H815"),
    "arrow-3": ("block-envelope", "block-bracket", "M980 345 V372 H900 V402"),
    "arrow-4": ("block-bracket", "block-regret", "M300 617 V650 H220 V680"),
    "arrow-5": ("block-bracket", "block-compare", "M600 617 V680"),
    "arrow-6": ("block-bracket", "block-sample", "M900 617 V650 H980 V680"),
}


def _float(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_p58_text_stays_inside_declared_blocks():
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


def test_p58_connectors_keep_confidence_to_routing_topology():
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


def test_p58_figure_preserves_confidence_regret_and_scope_boundaries():
    text = FIGURE.read_text(encoding="utf-8")
    for token in [
        "P58 finite-data switching-metric uncertainty and robust routing",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "true c is a finite metric",
        "ρₑ = Bₑ √[log(2/αₑ)/(2nₑ)]",
        "Σₑ αₑ ≤ α",
        "No independence between different",
        "transition pairs is needed.",
        "Envelope tables need not be metrics.",
        "L⁻(S;s) ≤ L*c(S;s) ≤ L⁺(S;s)",
        "P( L⁻ ≤ L*c ≤ L⁺ ) ≥ 1-α",
        "Groute = L⁺-L⁻",
        "C₀⁻ &gt; C₁⁺",
        "Joint coverage;",
        "no state independence needed.",
        "7. Sample-size certificate",
        "L⁺-L⁻ ≤ 2qrect η",
        "Sufficient common-sample condition.",
        "Not a minimax lower bound.",
        "adaptive pair selection",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p58_catalog_explains_nonmetric_empirical_center_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P58 finite-data switching-metric uncertainty and robust routing" in text
    assert "empirical pairwise center is allowed to violate triangle inequalities" in text
    assert "robust-route regret certificate" in text
    assert "common-sample inequality is sufficient, not a minimax lower bound" in text
    assert "physical-to-experiential bridge" in text

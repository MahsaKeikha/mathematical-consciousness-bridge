import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 21.0, "body": 16.0, "small": 14.0, "eq": 18.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 20.0

EXPECTED_CONNECTORS = {
    ("p64-limit", "lower-bounded-problem"): "M520 295 H663",
    ("lower-bounded-problem", "active-set"): "M1125 295 H1268",
    ("lower-bounded-problem", "water-filling"): "M900 410 V498",
    ("active-set", "water-filling"): "M1505 410 V455 H1180 V498",
    ("water-filling", "integer-floor"): "M650 730 V790 H445 V838",
    ("water-filling", "certificates"): "M1150 730 V790 H1355 V838",
}


def _number(value: str) -> float:
    return float(value)


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_p65_text_stays_inside_declared_blocks():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "p65_lower_bounded_heterogeneous_calibration.svg"
    svg = ET.parse(figure).getroot()
    blocks = svg.findall(".//svg:g[@data-qa-block='true']", SVG_NS)
    assert len(blocks) == 6

    for block in blocks:
        x = _number(block.attrib["data-x"])
        y = _number(block.attrib["data-y"])
        width = _number(block.attrib["data-width"])
        height = _number(block.attrib["data-height"])
        rect = block.find("svg:rect", SVG_NS)
        assert rect is not None
        assert _number(rect.attrib["x"]) == x
        assert _number(rect.attrib["y"]) == y
        assert _number(rect.attrib["width"]) == width
        assert _number(rect.attrib["height"]) == height

        labels = block.findall("svg:text", SVG_NS)
        assert labels
        for label in labels:
            css_class = label.attrib.get("class")
            assert css_class in FONT_SIZE
            assert label.attrib.get("text-anchor") == "middle"
            label_x = _number(label.attrib["x"])
            label_y = _number(label.attrib["y"])
            estimated_width = len(_visible(label)) * FONT_SIZE[css_class] * WIDTH_FACTOR
            half_width = estimated_width / 2.0
            assert label_x - half_width >= x + HORIZONTAL_PADDING, _visible(label)
            assert label_x + half_width <= x + width - HORIZONTAL_PADDING, _visible(label)
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_p65_connectors_keep_declared_block_topology():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "p65_lower_bounded_heterogeneous_calibration.svg"
    svg = ET.parse(figure).getroot()
    connectors = svg.findall(".//svg:path[@data-from][@data-to]", SVG_NS)
    actual = {
        (path.attrib["data-from"], path.attrib["data-to"]): path.attrib["d"]
        for path in connectors
    }
    assert actual == EXPECTED_CONNECTORS


def test_p65_figure_preserves_scientific_claim_boundaries():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (
        root / "docs" / "figures" / "p65_lower_bounded_heterogeneous_calibration.svg"
    ).read_text(encoding="utf-8")
    for phrase in (
        "n*ₑ = max{1, τ (bₑ / cₑ)^(2/3)}",
        "Feasible exactly when B ≥ B₀ = Σₑ cₑ.",
        "kₑ = ⌊n*ₑ⌋ ≥ 1",
        "rmin ≥ 1/2",
        "U(k) ≤ √2 U*int(B)",
        "P63 remains the exact integer solver.",
        "It makes no claim that a calibration variable is consciousness",
    ):
        assert phrase in source
    assert "\u2013" not in source
    assert "\u2014" not in source

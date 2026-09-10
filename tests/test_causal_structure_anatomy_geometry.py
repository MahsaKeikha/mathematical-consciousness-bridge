import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 20.0, "body": 15.0, "label": 12.0, "eq": 18.0, "eqsmall": 16.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 30.0
VERTICAL_PADDING = 20.0


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def test_causal_anatomy_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "causal_structure_anatomy.svg"
    svg = ET.parse(figure).getroot()

    blocks = svg.findall(".//svg:g[@data-qa-block='true']", SVG_NS)
    assert len(blocks) == 3

    for block in blocks:
        x = _value(block, "data-x")
        y = _value(block, "data-y")
        width = _value(block, "data-width")
        height = _value(block, "data-height")
        rect = block.find("svg:rect", SVG_NS)
        assert rect is not None
        assert _value(rect, "x") == x
        assert _value(rect, "y") == y
        assert _value(rect, "width") == width
        assert _value(rect, "height") == height

        for label in block.findall("svg:text", SVG_NS):
            css_class = label.attrib.get("class")
            if css_class not in FONT_SIZE:
                continue
            text = " ".join("".join(label.itertext()).split())
            estimated_width = len(text) * FONT_SIZE[css_class] * WIDTH_FACTOR
            label_x = _value(label, "x")
            label_y = _value(label, "y")
            assert x + HORIZONTAL_PADDING <= label_x
            assert label_x + estimated_width <= x + width - HORIZONTAL_PADDING, (
                f"{block.attrib['id']} may overflow right: {text!r}"
            )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_causal_anatomy_preserves_three_component_minimality_claims():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (root / "docs" / "figures" / "causal_structure_anatomy.svg").read_text(
        encoding="utf-8"
    )
    for phrase in (
        "P13: not recoverable from A and K",
        "P13: not recoverable from G and K",
        "P13: not recoverable from G and A",
    ):
        assert phrase in source
    assert source.count("P12: insufficient alone") == 3

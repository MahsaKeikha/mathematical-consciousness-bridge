import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {
    "bt": 25.0,
    "tx": 20.0,
    "math": 20.0,
    "small": 17.0,
}
HORIZONTAL_PADDING = 36.0
VERTICAL_PADDING = 28.0
WIDTH_FACTOR = 0.62


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def test_p63_text_is_contained_inside_every_declared_block():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "p63_exact_heterogeneous_integer_calibration.svg"
    svg = ET.parse(figure).getroot()

    blocks = svg.findall(".//svg:g[@data-qa-block='true']", SVG_NS)
    assert len(blocks) == 6

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
            css_class = label.attrib["class"]
            assert css_class in FONT_SIZE
            label_text = "".join(label.itertext()).strip()
            label_x = _value(label, "x")
            label_y = _value(label, "y")
            estimated_width = len(label_text) * FONT_SIZE[css_class] * WIDTH_FACTOR

            assert x + HORIZONTAL_PADDING <= label_x
            assert label_x + estimated_width <= x + width - HORIZONTAL_PADDING, (
                f"P63 label may overflow block {block.attrib['id']}: {label_text!r}"
            )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_p63_connectors_reference_existing_blocks_and_stay_outside_text():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "p63_exact_heterogeneous_integer_calibration.svg"
    svg = ET.parse(figure).getroot()

    block_ids = {
        block.attrib["id"]
        for block in svg.findall(".//svg:g[@data-qa-block='true']", SVG_NS)
    }
    connectors = svg.findall(".//svg:path[@data-from][@data-to]", SVG_NS)
    assert len(connectors) == 6

    for connector in connectors:
        assert connector.attrib["data-from"] in block_ids
        assert connector.attrib["data-to"] in block_ids
        assert connector.attrib.get("class") == "arrow"
        assert "marker-end:url(#arrow)" in svg.find("svg:defs/svg:style", SVG_NS).text


def test_p63_figure_has_no_forbidden_unicode_dashes():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "p63_exact_heterogeneous_integer_calibration.svg"
    text = figure.read_text(encoding="utf-8")
    assert "\u2013" not in text
    assert "\u2014" not in text

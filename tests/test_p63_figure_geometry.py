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
FIGURES = {
    "P59": ("p59_optimal_transition_calibration.svg", 5),
    "P60": ("p60_integer_transition_calibration.svg", 6),
    "P61": ("p61_exact_integer_transition_calibration.svg", 6),
    "P62": ("p62_heterogeneous_cost_transition_calibration.svg", 5),
    "P63": ("p63_exact_heterogeneous_integer_calibration.svg", 6),
}


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _load_figure(filename: str) -> tuple[pathlib.Path, ET.Element]:
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / filename
    return figure, ET.parse(figure).getroot()


def _assert_text_fits(
    proposition: str,
    block: ET.Element,
    label: ET.Element,
) -> None:
    x = _value(block, "data-x")
    y = _value(block, "data-y")
    width = _value(block, "data-width")
    height = _value(block, "data-height")
    css_class = label.attrib["class"]
    assert css_class in FONT_SIZE

    label_text = "".join(label.itertext()).strip()
    label_x = _value(label, "x")
    label_y = _value(label, "y")
    estimated_width = len(label_text) * FONT_SIZE[css_class] * WIDTH_FACTOR
    left_limit = x + HORIZONTAL_PADDING
    right_limit = x + width - HORIZONTAL_PADDING

    if label.attrib.get("text-anchor") == "middle":
        left_edge = label_x - estimated_width / 2.0
        right_edge = label_x + estimated_width / 2.0
    else:
        left_edge = label_x
        right_edge = label_x + estimated_width

    assert left_limit <= left_edge, (
        f"{proposition} label may overflow left side of block "
        f"{block.attrib['id']}: {label_text!r}"
    )
    assert right_edge <= right_limit, (
        f"{proposition} label may overflow right side of block "
        f"{block.attrib['id']}: {label_text!r}"
    )
    assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_p59_p63_text_is_contained_inside_every_declared_block():
    for proposition, (filename, _) in FIGURES.items():
        _, svg = _load_figure(filename)
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
                _assert_text_fits(proposition, block, label)


def test_p59_p63_connectors_reference_existing_blocks():
    for proposition, (filename, expected_connectors) in FIGURES.items():
        _, svg = _load_figure(filename)
        block_ids = {
            block.attrib["id"]
            for block in svg.findall(".//svg:g[@data-qa-block='true']", SVG_NS)
        }
        connectors = svg.findall(".//svg:path[@data-from][@data-to]", SVG_NS)
        assert len(connectors) == expected_connectors, proposition

        style = svg.find("svg:defs/svg:style", SVG_NS)
        assert style is not None
        assert "marker-end:url(#arrow)" in style.text
        for connector in connectors:
            assert connector.attrib["data-from"] in block_ids
            assert connector.attrib["data-to"] in block_ids
            assert connector.attrib.get("class") == "arrow"


def test_p59_p63_figures_have_no_forbidden_unicode_dashes():
    for proposition, (filename, _) in FIGURES.items():
        figure, _ = _load_figure(filename)
        text = figure.read_text(encoding="utf-8")
        assert "\u2013" not in text, proposition
        assert "\u2014" not in text, proposition

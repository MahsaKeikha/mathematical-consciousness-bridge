import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {
    "head": 20.0,
    "body": 17.0,
    "eq": 19.0,
    "dark-head": 19.0,
    "dark-body": 16.0,
}
HORIZONTAL_PADDING = 36.0
VERTICAL_PADDING = 28.0
WIDTH_FACTOR = 0.62


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _estimated_width(label: ET.Element) -> float:
    text = "".join(label.itertext()).strip()
    return len(text) * FONT_SIZE[label.attrib["class"]] * WIDTH_FACTOR


def test_universal_proof_ladder_text_stays_inside_safe_block_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "universal_proof_ladder.svg"
    svg = ET.parse(figure).getroot()

    blocks = svg.findall(".//svg:g[@data-qa-block='true']", SVG_NS)
    assert len(blocks) == 13

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

            label_x = _value(label, "x")
            label_y = _value(label, "y")
            width_estimate = _estimated_width(label)
            if label.attrib.get("text-anchor") == "middle":
                left_edge = label_x - width_estimate / 2.0
                right_edge = label_x + width_estimate / 2.0
            else:
                left_edge = label_x
                right_edge = label_x + width_estimate

            assert x + HORIZONTAL_PADDING <= left_edge, (
                f"{block.attrib['id']} text may overflow left: "
                f"{''.join(label.itertext()).strip()!r}"
            )
            assert right_edge <= x + width - HORIZONTAL_PADDING, (
                f"{block.attrib['id']} text may overflow right: "
                f"{''.join(label.itertext()).strip()!r}"
            )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_universal_proof_ladder_preserves_all_twelve_criteria():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "universal_proof_ladder.svg"
    svg = ET.parse(figure).getroot()
    text = " ".join("".join(node.itertext()) for node in svg.findall(".//svg:text", SVG_NS))

    for criterion in ("U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "U10", "U11", "U12"):
        assert criterion in text

    required_references = (
        "Proposition 1",
        "Propositions 2-3",
        "Proposition 4",
        "Proposition 5",
        "Proposition 6",
        "Proposition 7",
        "Proposition 8",
        "Proposition 9",
    )
    for reference in required_references:
        assert reference in text


def test_universal_proof_ladder_uses_no_forbidden_unicode_dashes():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "universal_proof_ladder.svg"
    text = figure.read_text(encoding="utf-8")
    assert "\u2013" not in text
    assert "\u2014" not in text

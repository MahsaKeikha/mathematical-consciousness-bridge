import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"label": 10.0, "head": 17.0, "body": 13.0, "eq": 15.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 20.0

OPENING_CARDS = (
    (95.0, 145.0, 420.0, 180.0),
    (590.0, 145.0, 420.0, 180.0),
    (1085.0, 145.0, 420.0, 180.0),
    (95.0, 410.0, 420.0, 180.0),
    (590.0, 410.0, 420.0, 180.0),
    (1085.0, 410.0, 420.0, 180.0),
)


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _text_width(element: ET.Element) -> float:
    visible = " ".join("".join(element.itertext()).split())
    return len(visible) * FONT_SIZE[element.attrib["class"]] * WIDTH_FACTOR


def test_theorem_roadmap_opening_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "theorem_roadmap.svg"
    svg = ET.parse(figure).getroot()

    rects = svg.findall(".//svg:rect", SVG_NS)
    texts = svg.findall(".//svg:text", SVG_NS)

    for x, y, width, height in OPENING_CARDS:
        matching = [
            rect
            for rect in rects
            if _value(rect, "x") == x
            and _value(rect, "y") == y
            and _value(rect, "width") == width
            and _value(rect, "height") == height
        ]
        assert len(matching) == 1

        labels = [
            text
            for text in texts
            if text.attrib.get("class") in FONT_SIZE
            and x <= _value(text, "x") <= x + width
            and y <= _value(text, "y") <= y + height
        ]
        assert labels

        for label in labels:
            label_x = _value(label, "x")
            label_y = _value(label, "y")
            visible = " ".join("".join(label.itertext()).split())
            assert x + HORIZONTAL_PADDING <= label_x
            assert label_x + _text_width(label) <= x + width - HORIZONTAL_PADDING, (
                f"Opening-card text may overflow right: {visible!r}"
            )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_theorem_roadmap_opening_preserves_p1_through_p18_labels():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "theorem_roadmap.svg"
    source = figure.read_text(encoding="utf-8")

    required_ranges = (
        "P1-P4",
        "P5-P10",
        "P11-P13",
        "P14-P15",
        "P16",
        "P17-P18",
    )
    for label in required_ranges:
        assert label in source

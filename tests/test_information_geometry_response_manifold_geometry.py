import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 18.0, "body": 13.8, "eq": 16.0, "cite": 12.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 16.0

CARDS = (
    (75.0, 165.0, 510.0, 270.0),
    (645.0, 165.0, 510.0, 270.0),
    (1215.0, 165.0, 510.0, 270.0),
    (120.0, 525.0, 455.0, 250.0),
    (675.0, 525.0, 455.0, 250.0),
    (1230.0, 525.0, 455.0, 250.0),
)


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_information_geometry_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "information_geometry_response_manifold.svg"
    svg = ET.parse(figure).getroot()

    rects = [
        rect
        for rect in svg.findall(".//svg:rect", SVG_NS)
        if {"x", "y", "width", "height"}.issubset(rect.attrib)
    ]
    texts = svg.findall(".//svg:text", SVG_NS)

    for x, y, width, height in CARDS:
        matches = [
            rect
            for rect in rects
            if _value(rect, "x") == x
            and _value(rect, "y") == y
            and _value(rect, "width") == width
            and _value(rect, "height") == height
        ]
        assert len(matches) == 1

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
            visible = _visible(label)
            estimated_width = len(visible) * FONT_SIZE[label.attrib["class"]] * WIDTH_FACTOR
            assert x + HORIZONTAL_PADDING <= label_x
            assert label_x + estimated_width <= x + width - HORIZONTAL_PADDING, (
                f"Card text may overflow right: {visible!r}"
            )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_information_geometry_preserves_scientific_boundaries():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (
        root / "docs" / "figures" / "information_geometry_response_manifold.svg"
    ).read_text(encoding="utf-8")

    for phrase in (
        "Fisher geometry quantifies local statistical",
        "Total variation gives an operational distance",
        "repository P2, P11",
        "P14-P15",
        "P16 tests factorization and coupling; P17",
        "B̄ : QP → QE",
        "An experiential geometry would require an independently justified bridge.",
        "A physical metric or manifold does not define",
    ):
        assert phrase in source

    assert "\u2013" not in source
    assert "\u2014" not in source

import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 19.0, "body": 15.0, "small": 13.0, "eq": 17.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 20.0

CARDS = (
    (80.0, 180.0, 500.0, 150.0),
    (80.0, 370.0, 500.0, 150.0),
    (80.0, 560.0, 500.0, 165.0),
    (80.0, 765.0, 500.0, 190.0),
    (650.0, 180.0, 500.0, 175.0),
    (650.0, 400.0, 500.0, 175.0),
    (650.0, 620.0, 500.0, 175.0),
    (650.0, 840.0, 500.0, 160.0),
    (1220.0, 180.0, 500.0, 180.0),
    (1220.0, 405.0, 500.0, 165.0),
    (1220.0, 615.0, 500.0, 175.0),
)


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_multiscale_hierarchy_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "multiscale_physical_hierarchy.svg"
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


def test_multiscale_hierarchy_preserves_core_scientific_boundaries():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (root / "docs" / "figures" / "multiscale_physical_hierarchy.svg").read_text(
        encoding="utf-8"
    )
    for phrase in (
        "P11-P13",
        "P14-P15",
        "P16",
        "P17",
        "B̄ : QP → QE",
        "Measurements constrain theory; they do not define experience.",
        "match a formally justified experiential equivalence.",
    ):
        assert phrase in source

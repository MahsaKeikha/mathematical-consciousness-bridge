import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {
    "head": 19.0,
    "body": 14.0,
    "eq": 17.0,
    "cite": 12.0,
}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 20.0

CARDS = (
    (80.0, 180.0, 365.0, 255.0),
    (505.0, 180.0, 365.0, 255.0),
    (930.0, 180.0, 365.0, 255.0),
    (1355.0, 180.0, 365.0, 255.0),
    (145.0, 520.0, 690.0, 285.0),
    (965.0, 520.0, 690.0, 285.0),
)


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible_text(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def _estimated_width(element: ET.Element) -> float:
    return len(_visible_text(element)) * FONT_SIZE[element.attrib["class"]] * WIDTH_FACTOR


def test_thermodynamics_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "thermodynamics_information_processing.svg"
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
            visible = _visible_text(label)
            assert x + HORIZONTAL_PADDING <= label_x
            assert label_x + _estimated_width(label) <= x + width - HORIZONTAL_PADDING, (
                f"Card text may overflow right: {visible!r}"
            )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_thermodynamics_figure_preserves_scientific_boundaries():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (root / "docs" / "figures" / "thermodynamics_information_processing.svg").read_text(
        encoding="utf-8"
    )

    for phrase in (
        "Werase ≥ kB T ln 2",
        "⟨Δstot⟩ ≥ 0",
        "Landauer 1961",
        "Seifert 2012",
        "Pearl 2009",
        "that energy or entropy is a consciousness variable.",
        "≠ experiential structure by definition",
    ):
        assert phrase in source

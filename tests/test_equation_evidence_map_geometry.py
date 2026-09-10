import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 17.0, "body": 13.5, "eq": 15.0, "tag": 11.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 20.0

CARDS = (
    (75.0, 172.0, 380.0, 135.0),
    (505.0, 172.0, 380.0, 135.0),
    (935.0, 172.0, 380.0, 135.0),
    (1365.0, 172.0, 360.0, 135.0),
    (75.0, 332.0, 380.0, 135.0),
    (505.0, 332.0, 380.0, 135.0),
    (935.0, 332.0, 380.0, 135.0),
    (1365.0, 332.0, 360.0, 135.0),
    (75.0, 492.0, 380.0, 135.0),
    (505.0, 492.0, 380.0, 135.0),
    (935.0, 492.0, 380.0, 135.0),
    (1365.0, 492.0, 360.0, 135.0),
    (75.0, 652.0, 380.0, 135.0),
    (505.0, 652.0, 380.0, 135.0),
    (935.0, 652.0, 380.0, 135.0),
    (1365.0, 652.0, 360.0, 135.0),
    (75.0, 812.0, 380.0, 135.0),
    (505.0, 812.0, 380.0, 135.0),
    (935.0, 812.0, 380.0, 135.0),
    (1365.0, 812.0, 360.0, 135.0),
)


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_equation_evidence_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "equation_evidence_map.svg"
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


def test_equation_evidence_map_preserves_scientific_status_boundaries():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (root / "docs" / "figures" / "equation_evidence_map.svg").read_text(
        encoding="utf-8"
    )
    for phrase in (
        "information ≠ experience",
        "Pearl; repository P11",
        "do(u): intervention ≠ correlation",
        "repository P14-P15",
        "path property ≠ endpoint score",
        "Werase ≥ kBT ln 2",
        "Landauer 1961",
        "Σentropy ≥ 0",
        "Seifert 2012",
        "Consciousness-specific necessity:",
        "not established",
        "B̄ : 𝒬P → 𝒬E",
        "Kleiner; repository P1-P17",
        "complete+identifiable+falsifiable",
        "Scientific solution: open problem",
        "Interpretation rule: an equation becomes consciousness evidence only through",
        "a declared measurement model and a separately justified bridge hypothesis.",
    ):
        assert phrase in source

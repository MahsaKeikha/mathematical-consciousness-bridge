import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 18.0, "body": 13.8, "eq": 16.0, "cite": 12.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 20.0

CARDS = (
    (75.0, 175.0, 350.0, 260.0),
    (500.0, 175.0, 350.0, 260.0),
    (925.0, 175.0, 350.0, 260.0),
    (1350.0, 175.0, 375.0, 260.0),
    (115.0, 520.0, 480.0, 250.0),
    (660.0, 520.0, 480.0, 250.0),
    (1205.0, 520.0, 480.0, 250.0),
)


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_measurement_map_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "conscious_state_measurement_map.svg"
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


def test_measurement_map_preserves_scientific_dissociation_boundaries():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (root / "docs" / "figures" / "conscious_state_measurement_map.svg").read_text(
        encoding="utf-8"
    )
    for phrase in (
        "Behavior, report, neural activation, and perturbational complexity are distinct observables.",
        "They should not be collapsed into a single experiential axis.",
        "responsiveness ↓",
        "experience may persist",
        "unresponsiveness ≠",
        "uniform experience",
        "motor output ≠",
        "neural command response",
        "Siclari et al. 2017",
        "Sarasso et al. 2015",
        "Claassen et al. 2019",
        "Casali et al. 2013",
        "repository P11-P17",
        "No single component defines consciousness.",
        "state label ≠ responsiveness ≠ report ≠ neural evidence ≠ bridge class",
    ):
        assert phrase in source

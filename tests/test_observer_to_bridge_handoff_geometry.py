import pathlib
import re
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
CLASS_FONT_SIZE = {
    "head": 18.0,
    "body": 15.0,
    "small": 13.0,
    "label": 11.0,
    "eq": 17.0,
    "eqdark": 18.0,
}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 20.0
VERTICAL_PADDING = 16.0

CARDS = (
    (120.0, 307.0, 680.0, 120.0),
    (120.0, 470.0, 680.0, 145.0),
    (120.0, 658.0, 680.0, 160.0),
    (880.0, 280.0, 160.0, 445.0),
    (1120.0, 307.0, 560.0, 145.0),
    (1120.0, 495.0, 560.0, 145.0),
    (1120.0, 683.0, 560.0, 135.0),
)


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def _font_size(element: ET.Element) -> float | None:
    css_class = element.attrib.get("class")
    if css_class in CLASS_FONT_SIZE:
        return CLASS_FONT_SIZE[css_class]
    match = re.search(r"font:\d+\s+([0-9.]+)px", element.attrib.get("style", ""))
    return float(match.group(1)) if match else None


def test_observer_bridge_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "observer_to_bridge_handoff.svg"
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
            if _font_size(text) is not None
            and x <= _value(text, "x") <= x + width
            and y <= _value(text, "y") <= y + height
        ]
        assert labels

        for label in labels:
            size = _font_size(label)
            assert size is not None
            label_x = _value(label, "x")
            label_y = _value(label, "y")
            visible = _visible(label)
            estimated_width = len(visible) * size * WIDTH_FACTOR
            if label.attrib.get("text-anchor") == "middle":
                assert label_x - estimated_width / 2 >= x + HORIZONTAL_PADDING, (
                    f"Centered text may overflow left: {visible!r}"
                )
                assert label_x + estimated_width / 2 <= x + width - HORIZONTAL_PADDING, (
                    f"Centered text may overflow right: {visible!r}"
                )
            else:
                assert x + HORIZONTAL_PADDING <= label_x
                assert label_x + estimated_width <= x + width - HORIZONTAL_PADDING, (
                    f"Card text may overflow right: {visible!r}"
                )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_observer_bridge_handoff_preserves_scientific_boundary():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (root / "docs" / "figures" / "observer_to_bridge_handoff.svg").read_text(
        encoding="utf-8"
    )
    for phrase in (
        "Spatiotemporal Observer Mathematics",
        "Time-dependent subsystem boundary",
        "Recovery and finite-sample certification",
        "Output: a statistically certified physical subsystem.",
        "pW ∈ QP",
        "no experiential",
        "property added",
        "at this step",
        "Mathematical Consciousness Bridge",
        "Intervention-resolved causal structure",
        "P14-P15 · temporal continuation + finite error",
        "P16 · independent composition + coupling",
        "P17 · coarse-graining + refinement limits",
        "Open physical-to-experiential bridge",
        "B̄ : QP → QE",
        "It does not redefine the observer theorem as a consciousness result.",
    ):
        assert phrase in source

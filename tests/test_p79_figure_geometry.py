import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p79_certified_sampling_radius.svg")


def _number(value: str) -> float:
    return float(value.replace("px", ""))


def test_p79_figure_has_accessible_title_and_description() -> None:
    root = ET.parse(FIGURE).getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}
    title = root.find("svg:title", ns)
    description = root.find("svg:desc", ns)

    assert title is not None
    assert title.text is not None and "P79" in title.text
    assert description is not None
    assert description.text is not None
    assert "exact-rational" in description.text
    assert "P78" in description.text


def test_p79_figure_declares_a_valid_viewbox() -> None:
    root = ET.parse(FIGURE).getroot()
    viewbox = [float(value) for value in root.attrib["viewBox"].split()]
    assert viewbox == [0.0, 0.0, 1200.0, 760.0]
    assert _number(root.attrib["width"]) == 1200.0
    assert _number(root.attrib["height"]) == 760.0


def test_p79_primary_panels_fit_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}

    for rect in root.findall("svg:rect", ns):
        x = _number(rect.attrib.get("x", "0"))
        y = _number(rect.attrib.get("y", "0"))
        width = _number(rect.attrib["width"])
        height = _number(rect.attrib["height"])
        assert 0 <= x <= 1200
        assert 0 <= y <= 760
        assert x + width <= 1200
        assert y + height <= 760


def test_p79_visual_contains_the_three_certification_stages() -> None:
    text = FIGURE.read_text(encoding="utf-8")
    required = (
        "Exact statistical inputs",
        "Certify log and square root",
        "Safe rejection comparison",
        "Positive atanh series",
        "Integer-certified dyadic",
        "square-root enclosure",
        "Strict certified gate",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text

import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p82_exact_nested_projection_contrast.svg")
SVG_NS = "{http://www.w3.org/2000/svg}"


def test_p82_figure_has_accessible_title_description_and_expected_canvas() -> None:
    root = ET.fromstring(FIGURE.read_text(encoding="utf-8"))

    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    title = root.find(f"{SVG_NS}title")
    description = root.find(f"{SVG_NS}desc")
    assert title is not None and "P82" in (title.text or "")
    assert description is not None
    description_text = description.text or ""
    assert "256" in description_text
    assert "one twelfth" in description_text
    assert "physical-to-experiential bridge remains open" in description_text


def test_p82_figure_key_panels_remain_inside_canvas() -> None:
    root = ET.fromstring(FIGURE.read_text(encoding="utf-8"))

    for element in root.iter(f"{SVG_NS}rect"):
        x = float(element.attrib.get("x", 0))
        y = float(element.attrib.get("y", 0))
        width = float(element.attrib.get("width", 0))
        height = float(element.attrib.get("height", 0))
        assert 0 <= x <= 1200
        assert 0 <= y <= 760
        assert x + width <= 1200
        assert y + height <= 760


def test_p82_figure_contains_exact_interval_and_strict_witness_labels() -> None:
    source = FIGURE.read_text(encoding="utf-8")

    required = (
        "P_s(A\\B) = P_s(A) [1 - P_s(D)]",
        "Standard P82 family: 256",
        "exact interval can be strictly tighter than subtraction",
        "L82(B) = max(L81(B), L_nest(B))",
        "L80 = 0,  L81 = 1/16,  L82 = 1/12",
        "P79 gate",
    )
    for token in required:
        assert token in source

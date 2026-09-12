import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p83_signed_cylinder_contrast_separation.svg")
SVG_NS = "{http://www.w3.org/2000/svg}"


def test_p83_figure_has_accessible_title_description_and_expected_canvas() -> None:
    root = ET.fromstring(FIGURE.read_text(encoding="utf-8"))

    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    title = root.find(f"{SVG_NS}title")
    description = root.find(f"{SVG_NS}desc")
    assert title is not None and "P83" in (title.text or "")
    assert description is not None
    description_text = description.text or ""
    assert "2,696" in description_text
    assert "five one-hundred-twenty-eighths" in description_text
    assert "physical-to-experiential bridge remains open" in description_text


def test_p83_figure_key_panels_remain_inside_canvas() -> None:
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


def test_p83_figure_contains_exact_interval_and_strict_witness_labels() -> None:
    source = FIGURE.read_text(encoding="utf-8")

    required = (
        "phi(x) = 1_A(x) - 1_B(x)",
        "Standard P83 family: 2,696",
        "multi-affine in at most four response coordinates",
        "L83(B) = max(L82(B), L_signed(B))",
        "A = {1100},  B = {1101}",
        "L82 = 0,  L83 = 5/128 = exact distance",
        "pi = 5/16 gives distance 5/128",
    )
    for token in required:
        assert token in source

import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p80_simplex_coupled_model_separation.svg")


def _number(value: str) -> float:
    return float(value.replace("px", ""))


def test_p80_figure_has_accessible_title_and_description() -> None:
    root = ET.parse(FIGURE).getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}
    title = root.find("svg:title", ns)
    description = root.find("svg:desc", ns)

    assert title is not None
    assert title.text is not None and "P80" in title.text
    assert description is not None
    assert description.text is not None
    assert "simplex" in description.text.lower()
    assert "coordinate-overlap radius" in description.text
    assert "P79" in description.text


def test_p80_figure_declares_expected_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    viewbox = [float(value) for value in root.attrib["viewBox"].split()]
    assert viewbox == [0.0, 0.0, 1200.0, 760.0]
    assert _number(root.attrib["width"]) == 1200.0
    assert _number(root.attrib["height"]) == 760.0


def test_p80_rectangles_fit_inside_canvas() -> None:
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


def test_p80_text_baselines_remain_inside_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}

    for text_element in root.findall("svg:text", ns):
        x = _number(text_element.attrib["x"])
        y = _number(text_element.attrib["y"])
        assert 0 <= x <= 1200
        assert 0 <= y <= 760


def test_p80_visual_contains_complete_certification_logic() -> None:
    text = FIGURE.read_text(encoding="utf-8")
    required = (
        "P78 box enclosure",
        "Intersect with the simplex",
        "Stronger certified bound",
        "R_delta subset R_box",
        "r &gt;= r_box = L78(B)",
        "sum max(l_i, p_i-r) &lt;= 1",
        "1 &lt;= sum min(u_i, p_i+r)",
        "L80 = max(r_box, r_A, r_C)",
        "L80(B) &gt;= L78(B)",
        "L80 &gt; epsilon_upper  =&gt;  reject",
        "physical-to-experiential bridge remains open",
    )
    for token in required:
        assert token in text

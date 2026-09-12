from pathlib import Path
import xml.etree.ElementTree as ET


FIGURE = Path("docs/figures/p84_exact_pairwise_walsh_contrast.svg")


def _figure_text() -> str:
    return FIGURE.read_text(encoding="utf-8")


def test_p84_figure_is_valid_accessible_svg() -> None:
    text = _figure_text()
    root = ET.fromstring(text)

    assert root.tag.endswith("svg")
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "780"
    assert root.attrib["viewBox"] == "0 0 1200 780"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"
    assert "<title id=\"title\">P84 exact pairwise Walsh-contrast certificate</title>" in text
    assert "<desc id=\"desc\">" in text
    assert "Scientific status:" in text
    assert "physical-to-experiential bridge remains open" in text


def test_p84_figure_exposes_theorem_equations_and_strict_witness() -> None:
    text = _figure_text()
    required = (
        "15 nonconstant characters",
        "210 signed contrasts",
        "||phi||_1 = 16",
        "multi-affine: exact extrema occur at vertices",
        "L84(B) = max(L83(B), L_Walsh(B))",
        "E[chi12 - chi13] = 0",
        "empirical E[chi12 - chi13] = 3/16",
        "L82 = L83 = 0,  L84 = 3/256",
        "P79 gate: L84 &gt; epsilon_upper =&gt; reject",
    )
    for token in required:
        assert token in text


def test_p84_figure_keeps_all_drawn_geometry_inside_canvas() -> None:
    root = ET.fromstring(_figure_text())
    namespace = {"svg": "http://www.w3.org/2000/svg"}

    for rect in root.findall("svg:rect", namespace):
        x = float(rect.attrib.get("x", 0))
        y = float(rect.attrib.get("y", 0))
        width = float(rect.attrib.get("width", 0))
        height = float(rect.attrib.get("height", 0))
        assert 0 <= x <= 1200
        assert 0 <= y <= 780
        assert x + width <= 1200
        assert y + height <= 780

    for circle in root.findall("svg:circle", namespace):
        cx = float(circle.attrib["cx"])
        cy = float(circle.attrib["cy"])
        radius = float(circle.attrib["r"])
        assert radius <= cx <= 1200 - radius
        assert radius <= cy <= 780 - radius


def test_p84_figure_has_no_foreign_object_or_external_asset_dependency() -> None:
    text = _figure_text()
    assert "foreignObject" not in text
    assert "http://www.w3.org/1999/xlink" not in text
    assert "<image" not in text

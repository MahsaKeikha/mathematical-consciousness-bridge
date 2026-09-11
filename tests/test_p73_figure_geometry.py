from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FIGURE = ROOT / "docs" / "figures" / "p73_three_view_target_channel_identifiability.svg"
SVG = {"svg": "http://www.w3.org/2000/svg"}


def test_p73_figure_is_valid_accessible_svg():
    assert FIGURE.exists()
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["viewBox"] == "0 0 1600 980"
    assert root.attrib["role"] == "img"
    title = root.find("svg:title", SVG)
    desc = root.find("svg:desc", SVG)
    assert title is not None and "P73" in "".join(title.itertext())
    assert desc is not None and "three-view" in "".join(desc.itertext())


def test_p73_figure_exposes_identifiability_boundary_and_handoff():
    text = FIGURE.read_text(encoding="utf-8")
    for token in (
        "Two views: one product, a continuum of channels",
        "Three views: three products identify stability magnitudes",
        "gamma1 = sqrt(m12 m13 / m23)",
        "Same observable moment, different individual stabilities",
        "simultaneous Hoeffding moment bands",
        "certified lower stability bound for P72 design",
        "physical-to-experiential bridge remains open",
    ):
        assert token in text


def test_p73_figure_contains_no_en_or_em_dash():
    text = FIGURE.read_text(encoding="utf-8")
    assert "\u2013" not in text
    assert "\u2014" not in text

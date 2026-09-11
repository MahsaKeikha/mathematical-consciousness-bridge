import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p73_target_channel_identifiability.svg")
SVG_NS = "http://www.w3.org/2000/svg"


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def _number(value: str) -> float:
    return float(value.replace("px", ""))


def _group(root: ET.Element, group_id: str) -> ET.Element:
    for node in root.findall(f".//{{{SVG_NS}}}g"):
        if node.attrib.get("id") == group_id:
            return node
    raise AssertionError(f"missing SVG group: {group_id}")


def test_p73_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()
    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    desc = root.find(f"{{{SVG_NS}}}desc")
    assert desc is not None and desc.text is not None
    for token in (
        "follow the attached latent-to-view connectors",
        "two views generally cannot identify individual reliabilities",
        "does not identify the latent class with consciousness",
    ):
        assert token in desc.text


def test_p73_svg_contains_recovery_and_nonidentifiability_results() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)
    required = (
        "P73 Three-View Target-Channel Identifiability",
        "Cij = bi bj v",
        "M123 = -2 m v b1 b2 b3",
        "m² = q / (q + 4)",
        "gamma_j = |b_j|",
        "gamma_123 ≥ max",
        "Two views are not enough in general",
        "same product 0.36, same observed law",
        "does not identify the latent class with consciousness",
    )
    for token in required:
        assert token in text


def test_p73_all_rectangles_and_explicit_coordinates_fit_canvas() -> None:
    root = ET.parse(FIGURE).getroot()
    for rect in root.findall(f".//{{{SVG_NS}}}rect"):
        x = _number(rect.attrib.get("x", "0"))
        y = _number(rect.attrib.get("y", "0"))
        width = _number(rect.attrib["width"])
        height = _number(rect.attrib["height"])
        assert x + width <= 1200
        assert y + height <= 760

    for node in root.iter():
        for coordinate in ("x", "x1", "x2"):
            if coordinate in node.attrib:
                assert 0.0 <= _number(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2"):
            if coordinate in node.attrib:
                assert 0.0 <= _number(node.attrib[coordinate]) <= 760.0


def test_p73_declared_model_connectors_run_from_latent_state_to_views() -> None:
    root = ET.parse(FIGURE).getroot()
    panel = _group(root, "declared-model-panel")
    connectors = [
        node
        for node in panel.findall(f"{{{SVG_NS}}}path")
        if node.attrib.get("marker-end") == "url(#arrow)"
    ]
    assert {node.attrib["d"] for node in connectors} == {
        "M284 252 L166 302",
        "M320 252 L320 296",
        "M356 252 L474 302",
    }
    assert len(connectors) == 3


def test_p73_long_explanations_are_wrapped_within_lower_panels() -> None:
    root = ET.parse(FIGURE).getroot()
    stability = _group(root, "stability-panel")
    two_view = _group(root, "two-view-boundary-panel")

    stability_lines = [
        "".join(node.itertext()) for node in stability.findall(f"{{{SVG_NS}}}text")
    ]
    assert "The global latent-label swap sends bj to -bj," in stability_lines
    assert "so gamma_j is unchanged." in stability_lines
    assert "The joint three-view channel is at least as" in stability_lines
    assert "TV-stable as each marginal view." in stability_lines

    two_view_lines = [
        "".join(node.itertext()) for node in two_view.findall(f"{{{SVG_NS}}}text")
    ]
    assert "A third independent view or another justified anchor" in two_view_lines
    assert "is required." in two_view_lines

    for panel in (stability, two_view):
        baselines = [
            _number(node.attrib["y"])
            for node in panel.findall(f"{{{SVG_NS}}}text")
        ]
        assert max(baselines) <= 688
        assert 700 - max(baselines) >= 12

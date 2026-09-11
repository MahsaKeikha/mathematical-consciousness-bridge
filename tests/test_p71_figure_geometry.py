import xml.etree.ElementTree as ET
from pathlib import Path

FIGURE = Path("docs/figures/p71_target_provenance_noncircularity.svg")


def _all_text(root: ET.Element) -> str:
    return " ".join("".join(node.itertext()) for node in root.iter())


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _find_rect(root: ET.Element, x: float, y: float) -> ET.Element:
    for node in root.iter():
        if _local_name(node.tag) != "rect":
            continue
        if float(node.attrib.get("x", -1)) == x and float(node.attrib.get("y", -1)) == y:
            return node
    raise AssertionError(f"missing rect at {(x, y)}")


def _find_text(root: ET.Element, token: str) -> ET.Element:
    for node in root.iter():
        if _local_name(node.tag) == "text" and token in "".join(node.itertext()):
            return node
    raise AssertionError(f"missing text containing {token!r}")


def test_p71_svg_has_publication_canvas_and_accessibility_metadata() -> None:
    root = ET.parse(FIGURE).getroot()

    assert root.attrib["width"] == "1200"
    assert root.attrib["height"] == "760"
    assert root.attrib["viewBox"] == "0 0 1200 760"
    assert root.attrib["role"] == "img"
    assert root.attrib["aria-labelledby"] == "title desc"

    ns = {"svg": "http://www.w3.org/2000/svg"}
    description = root.find("svg:desc", ns)
    assert description is not None and description.text is not None
    for token in (
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "Scientific status:",
    ):
        assert token in description.text


def test_p71_svg_contains_theorem_synthetic_witness_and_provenance_boundary() -> None:
    root = ET.parse(FIGURE).getroot()
    text = _all_text(root)

    required = (
        "P71 Target-Provenance Non-Circularity",
        "Descriptor-derived target",
        "Separately declared synthetic target",
        "E_h = h(T)",
        "I(E_h; Omega | T) = 0",
        "same T = 0, but different E_ext",
        "I(E_circ; Omega | T) = 0",
        "I(E_ext; Omega | T) = log 2 ≈ 0.6931 nats",
        "zero residual cannot, from observed values alone, prove independent target provenance",
        "synthetic E_ext is not a claim about measured experience",
        "Passing it is necessary, not sufficient",
    )
    for token in required:
        assert token in text


def test_p71_descriptor_derived_arrows_attach_to_boxes() -> None:
    root = ET.parse(FIGURE).getroot()
    omega = _find_rect(root, 96.0, 244.0)
    descriptor = _find_rect(root, 278.0, 244.0)
    target = _find_rect(root, 460.0, 244.0)

    assert float(omega.attrib["x"]) + float(omega.attrib["width"]) == 206.0
    assert float(descriptor.attrib["x"]) == 278.0
    assert float(descriptor.attrib["x"]) + float(descriptor.attrib["width"]) == 390.0
    assert float(target.attrib["x"]) == 460.0

    expected = {("206", "276"), ("390", "458")}
    found: set[tuple[str, str]] = set()
    for node in root.iter():
        if _local_name(node.tag) != "line":
            continue
        pair = (node.attrib.get("x1", ""), node.attrib.get("x2", ""))
        if pair in expected and node.attrib.get("y1") == "275" and node.attrib.get("y2") == "275":
            assert node.attrib.get("marker-end") == "url(#arrow)"
            found.add(pair)

    assert found == expected


def test_p71_synthetic_same_descriptor_arrows_terminate_at_t_card() -> None:
    root = ET.parse(FIGURE).getroot()
    same_t = _find_rect(root, 806.0, 273.0)
    left = float(same_t.attrib["x"])
    assert left == 806.0

    destinations: set[tuple[str, str]] = set()
    for node in root.iter():
        if _local_name(node.tag) != "line":
            continue
        if node.attrib.get("marker-end") != "url(#blueArrow)":
            continue
        destinations.add((node.attrib.get("x2", ""), node.attrib.get("y2", "")))

    assert destinations == {("804", "290"), ("804", "316")}


def test_p71_residual_cards_and_provenance_text_stay_inside_containers() -> None:
    root = ET.parse(FIGURE).getroot()

    left_card = _find_rect(root, 68.0, 534.0)
    left_bottom = float(left_card.attrib["y"]) + float(left_card.attrib["height"])
    for token in (
        "Descriptor-derived E_circ = T",
        "I(E_circ; Omega | T) = 0",
        "guaranteed by construction",
    ):
        assert float(_find_text(root, token).attrib["y"]) < left_bottom

    right_card = _find_rect(root, 600.0, 534.0)
    right_bottom = float(right_card.attrib["y"]) + float(right_card.attrib["height"])
    for token in (
        "Separately declared synthetic E_ext",
        "I(E_ext; Omega | T) = log 2 ≈ 0.6931 nats",
    ):
        assert float(_find_text(root, token).attrib["y"]) < right_bottom

    boundary = _find_rect(root, 68.0, 642.0)
    boundary_bottom = float(boundary.attrib["y"]) + float(boundary.attrib["height"])
    assert float(_find_text(root, "Provenance boundary").attrib["y"]) < boundary_bottom
    assert float(_find_text(root, "A zero residual cannot").attrib["y"]) < boundary_bottom


def test_p71_svg_keeps_content_inside_declared_canvas() -> None:
    root = ET.parse(FIGURE).getroot()

    for node in root.iter():
        for coordinate in ("x", "x1", "x2", "cx"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 1200.0
        for coordinate in ("y", "y1", "y2", "cy"):
            if coordinate in node.attrib:
                assert 0.0 <= float(node.attrib[coordinate]) <= 760.0

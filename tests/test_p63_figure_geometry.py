import pathlib
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
WIDTH_FACTOR = 0.58

LEGACY_FONT_SIZE = {
    "bt": 25.0,
    "tx": 20.0,
    "math": 20.0,
    "small": 17.0,
}
LEGACY_FIGURES = {
    "P59": ("p59_optimal_transition_calibration.svg", 5),
}

P63_FIGURE = ROOT / "docs/figures/p63_exact_heterogeneous_integer_calibration.svg"
CATALOG = ROOT / "docs/figure_catalog.md"
P63_FONT_SIZE = {
    "head": 18.0,
    "copy": 15.0,
    "small": 14.0,
    "eq": 16.0,
    "strong": 17.0,
}
P63_ROUTES = {
    "arrow-1": ("block-greedy", "block-problem", "M385 240 H435"),
    "arrow-2": ("block-problem", "block-state", "M765 240 H815"),
    "arrow-3": ("block-problem", "block-bellman", "M600 350 V410"),
    "arrow-4": ("block-state", "block-bellman", "M980 350 V380 H900 V410"),
    "arrow-5": ("block-bellman", "block-gcd", "M300 630 V660 H220 V690"),
    "arrow-6": ("block-bellman", "block-complexity", "M600 630 V690"),
    "arrow-7": ("block-bellman", "block-benchmark", "M900 630 V660 H980 V690"),
}


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def _load_legacy(filename: str) -> tuple[pathlib.Path, ET.Element]:
    figure = ROOT / "docs" / "figures" / filename
    return figure, ET.parse(figure).getroot()


def _assert_legacy_text_fits(
    proposition: str,
    block: ET.Element,
    label: ET.Element,
) -> None:
    x = _value(block, "data-x")
    y = _value(block, "data-y")
    width = _value(block, "data-width")
    height = _value(block, "data-height")
    css_class = label.attrib["class"]
    assert css_class in LEGACY_FONT_SIZE

    label_text = "".join(label.itertext()).strip()
    label_x = _value(label, "x")
    label_y = _value(label, "y")
    estimated_width = len(label_text) * LEGACY_FONT_SIZE[css_class] * 0.62
    left_limit = x + 36.0
    right_limit = x + width - 36.0

    if label.attrib.get("text-anchor") == "middle":
        left_edge = label_x - estimated_width / 2.0
        right_edge = label_x + estimated_width / 2.0
    else:
        left_edge = label_x
        right_edge = label_x + estimated_width

    assert left_limit <= left_edge, (
        f"{proposition} label may overflow left side of block "
        f"{block.attrib['id']}: {label_text!r}"
    )
    assert right_edge <= right_limit, (
        f"{proposition} label may overflow right side of block "
        f"{block.attrib['id']}: {label_text!r}"
    )
    assert y + 28.0 <= label_y <= y + height - 28.0


def test_p59_legacy_text_is_contained_inside_every_declared_block():
    for proposition, (filename, _) in LEGACY_FIGURES.items():
        _, svg = _load_legacy(filename)
        blocks = svg.findall(".//svg:g[@data-qa-block='true']", SVG_NS)
        assert len(blocks) == 6
        for block in blocks:
            rect = block.find("svg:rect", SVG_NS)
            assert rect is not None
            assert _value(rect, "x") == _value(block, "data-x")
            assert _value(rect, "y") == _value(block, "data-y")
            assert _value(rect, "width") == _value(block, "data-width")
            assert _value(rect, "height") == _value(block, "data-height")
            for label in block.findall("svg:text", SVG_NS):
                _assert_legacy_text_fits(proposition, block, label)


def test_p59_legacy_connectors_reference_existing_blocks():
    for proposition, (filename, expected_connectors) in LEGACY_FIGURES.items():
        _, svg = _load_legacy(filename)
        block_ids = {
            block.attrib["id"]
            for block in svg.findall(".//svg:g[@data-qa-block='true']", SVG_NS)
        }
        connectors = svg.findall(".//svg:path[@data-from][@data-to]", SVG_NS)
        assert len(connectors) == expected_connectors, proposition
        style = svg.find("svg:defs/svg:style", SVG_NS)
        assert style is not None
        assert "marker-end:url(#arrow)" in style.text
        for connector in connectors:
            assert connector.attrib["data-from"] in block_ids
            assert connector.attrib["data-to"] in block_ids
            assert connector.attrib.get("class") == "arrow"


def test_p59_legacy_figure_has_no_forbidden_unicode_dashes():
    for proposition, (filename, _) in LEGACY_FIGURES.items():
        figure, _ = _load_legacy(filename)
        text = figure.read_text(encoding="utf-8")
        assert "\u2013" not in text, proposition
        assert "\u2014" not in text, proposition


def test_p63_text_stays_inside_declared_blocks():
    svg = ET.parse(P63_FIGURE).getroot()
    blocks = [
        group
        for group in svg.findall("svg:g", SVG_NS)
        if group.attrib.get("id", "").startswith("block-")
    ]
    assert len(blocks) == 8

    for block in blocks:
        x = _value(block, "data-x")
        y = _value(block, "data-y")
        width = _value(block, "data-w")
        height = _value(block, "data-h")
        rect = block.find("svg:rect", SVG_NS)
        assert rect is not None
        assert _value(rect, "x") == x
        assert _value(rect, "y") == y
        assert _value(rect, "width") == width
        assert _value(rect, "height") == height

        for label in block.findall("svg:text", SVG_NS):
            css_class = label.attrib.get("class")
            assert css_class in P63_FONT_SIZE
            estimated_width = len(_visible(label)) * P63_FONT_SIZE[css_class] * WIDTH_FACTOR
            label_x = _value(label, "x")
            label_y = _value(label, "y")
            if label.attrib.get("text-anchor") == "middle":
                left = label_x - estimated_width / 2.0
                right = label_x + estimated_width / 2.0
            else:
                left = label_x
                right = label_x + estimated_width
            assert left >= x + 12, (block.attrib["id"], _visible(label))
            assert right <= x + width - 12, (block.attrib["id"], _visible(label))
            assert y + 12 <= label_y <= y + height - 5, (
                block.attrib["id"],
                _visible(label),
            )


def test_p63_connectors_keep_exact_solver_topology():
    svg = ET.parse(P63_FIGURE).getroot()
    arrows = [
        path
        for path in svg.findall("svg:path", SVG_NS)
        if path.attrib.get("id", "").startswith("arrow-")
    ]
    actual = {
        path.attrib["id"]: (
            path.attrib["data-source"],
            path.attrib["data-target"],
            path.attrib["d"],
        )
        for path in arrows
    }
    assert actual == P63_ROUTES


def test_p63_figure_preserves_exactness_complexity_and_scientific_boundaries():
    text = P63_FIGURE.read_text(encoding="utf-8")
    for token in [
        "P63 exact heterogeneous-cost integer calibration",
        "What this figure shows:",
        "How to read it:",
        "Main takeaway:",
        "B ≥ Σₑ cₑ.",
        "F₀(0)=0",
        "U*int(B) = min over 0 ≤ s ≤ B of Fₘ(s)",
        "g = gcd{cₑ}",
        "O(m B'^2)",
        "Pseudo-polynomial in numeric B'.",
        "Not an NP-hardness claim by itself.",
        "U*cont(B) ≤ U*int(B)",
        "Unspent budget is allowed",
        "physical-to-experiential bridge",
        "quantum incompleteness",
    ]:
        assert token in text
    assert "\u2013" not in text
    assert "\u2014" not in text


def test_p63_catalog_explains_exact_scope_without_guessing():
    text = CATALOG.read_text(encoding="utf-8")
    assert "P63 exact heterogeneous-cost integer calibration" in text
    assert "exact-spend Bellman dynamic program" in text
    assert "pseudo-polynomial in the compressed numeric budget" in text
    assert "not an NP-hardness claim" in text

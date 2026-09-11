import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"label": 10.0, "head": 17.0, "body": 13.0, "eq": 15.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 20.0

OPENING_CARDS = (
    (95.0, 145.0, 420.0, 180.0),
    (590.0, 145.0, 420.0, 180.0),
    (1085.0, 145.0, 420.0, 180.0),
    (95.0, 410.0, 420.0, 180.0),
    (590.0, 410.0, 420.0, 180.0),
    (1085.0, 410.0, 420.0, 180.0),
)

EXPECTED_BRANCH_ROUTES = {
    "branch-scale-p25": ("p17-p18", "p25"),
    "branch-scale-p26": ("p17-p18", "p26"),
    "arrow-p26-p27": ("p26", "p27"),
    "arrow-p27-p28": ("p27", "p28"),
    "branch-p25-p28": ("p25", "p28"),
    "branch-p27-p29": ("p27", "p29"),
    "branch-p27-p30": ("p27", "p30"),
    "arrow-p29-p30": ("p29", "p30"),
    "branch-p28-p30": ("p28", "p30"),
    "arrow-p30-p31": ("p30", "p31"),
}


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _text_width(element: ET.Element) -> float:
    visible = " ".join("".join(element.itertext()).split())
    return len(visible) * FONT_SIZE[element.attrib["class"]] * WIDTH_FACTOR


def test_theorem_roadmap_opening_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "theorem_roadmap.svg"
    svg = ET.parse(figure).getroot()

    rects = [
        rect
        for rect in svg.findall(".//svg:rect", SVG_NS)
        if {"x", "y", "width", "height"}.issubset(rect.attrib)
    ]
    texts = svg.findall(".//svg:text", SVG_NS)

    for x, y, width, height in OPENING_CARDS:
        matching = [
            rect
            for rect in rects
            if _value(rect, "x") == x
            and _value(rect, "y") == y
            and _value(rect, "width") == width
            and _value(rect, "height") == height
        ]
        assert len(matching) == 1

        labels = [
            text
            for text in texts
            if text.attrib.get("class") in FONT_SIZE
            and x <= _value(text, "x") <= x + width
            and y <= _value(text, "y") <= y + height
        ]
        assert labels

        for label in labels:
            label_x = _value(label, "x")
            label_y = _value(label, "y")
            visible = " ".join("".join(label.itertext()).split())
            assert x + HORIZONTAL_PADDING <= label_x
            assert label_x + _text_width(label) <= x + width - HORIZONTAL_PADDING, (
                f"Opening-card text may overflow right: {visible!r}"
            )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_theorem_roadmap_opening_preserves_p1_through_p18_labels():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "theorem_roadmap.svg"
    source = figure.read_text(encoding="utf-8")

    required_ranges = (
        "P1-P4",
        "P5-P10",
        "P11-P13",
        "P14-P15",
        "P16",
        "P17-P18",
    )
    for label in required_ranges:
        assert label in source


def test_theorem_roadmap_makes_p25_through_p31_dependencies_explicit():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "theorem_roadmap.svg"
    svg = ET.parse(figure).getroot()

    semantic_paths = {
        path.attrib["id"]: (
            path.attrib.get("data-source"),
            path.attrib.get("data-target"),
        )
        for path in svg.findall(".//svg:path", SVG_NS)
        if path.attrib.get("id") in EXPECTED_BRANCH_ROUTES
    }
    assert semantic_paths == EXPECTED_BRANCH_ROUTES

    for path in svg.findall(".//svg:path", SVG_NS):
        if path.attrib.get("id") in EXPECTED_BRANCH_ROUTES:
            assert path.attrib.get("marker-end") == "url(#arrow)" or path.attrib.get(
                "class"
            ) in {"arrow", "branch"}


def test_theorem_roadmap_does_not_invent_p24_to_p25_dependency():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "theorem_roadmap.svg"
    source = figure.read_text(encoding="utf-8")

    assert "P24 is not a mathematical prerequisite" in source
    assert 'data-source="p24" data-target="p25"' not in source
    assert 'data-source="p25" data-target="p26"' not in source


def test_theorem_roadmap_description_explains_branch_semantics_and_boundary():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "theorem_roadmap.svg"
    svg = ET.parse(figure).getroot()
    desc = svg.find("svg:desc", SVG_NS)
    assert desc is not None
    text = " ".join("".join(desc.itertext()).split())

    for phrase in (
        "mathematical dependency rather than simple numerical succession",
        "do not infer a P24-to-P25 dependency",
        "P30 then assembles",
        "visual adjacency is not theorem dependency",
        "physical-to-experiential bridge remains open",
    ):
        assert phrase in text

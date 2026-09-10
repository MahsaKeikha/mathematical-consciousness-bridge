import pathlib
import xml.etree.ElementTree as ET

SVG_NS = {"svg": "http://www.w3.org/2000/svg"}
FONT_SIZE = {"head": 22.0, "copy": 15.0, "math": 18.0, "small": 13.0}
WIDTH_FACTOR = 0.62
HORIZONTAL_PADDING = 24.0
VERTICAL_PADDING = 20.0

CARDS = (
    (530.0, 155.0, 740.0, 150.0),
    (90.0, 405.0, 340.0, 220.0),
    (520.0, 405.0, 340.0, 220.0),
    (940.0, 405.0, 340.0, 220.0),
    (1370.0, 405.0, 340.0, 220.0),
    (610.0, 690.0, 580.0, 165.0),
    (420.0, 930.0, 960.0, 205.0),
)


def _value(element: ET.Element, name: str) -> float:
    return float(element.attrib[name])


def _visible(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


def test_fundamental_theory_cards_keep_text_inside_safe_regions():
    root = pathlib.Path(__file__).resolve().parents[1]
    figure = root / "docs" / "figures" / "fundamental_theory_consciousness_map.svg"
    svg = ET.parse(figure).getroot()

    rects = [
        rect
        for rect in svg.findall(".//svg:rect", SVG_NS)
        if {"x", "y", "width", "height"}.issubset(rect.attrib)
    ]
    texts = svg.findall(".//svg:text", SVG_NS)

    for x, y, width, height in CARDS:
        matches = [
            rect
            for rect in rects
            if _value(rect, "x") == x
            and _value(rect, "y") == y
            and _value(rect, "width") == width
            and _value(rect, "height") == height
        ]
        assert len(matches) == 1

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
            visible = _visible(label)
            estimated_width = len(visible) * FONT_SIZE[label.attrib["class"]] * WIDTH_FACTOR
            if label.attrib.get("text-anchor") == "middle":
                assert label_x - estimated_width / 2 >= x + HORIZONTAL_PADDING, (
                    f"Centered text may overflow left: {visible!r}"
                )
                assert label_x + estimated_width / 2 <= x + width - HORIZONTAL_PADDING, (
                    f"Centered text may overflow right: {visible!r}"
                )
            else:
                assert x + HORIZONTAL_PADDING <= label_x
                assert label_x + estimated_width <= x + width - HORIZONTAL_PADDING, (
                    f"Card text may overflow right: {visible!r}"
                )
            assert y + VERTICAL_PADDING <= label_y <= y + height - VERTICAL_PADDING


def test_fundamental_theory_map_preserves_scientific_boundaries():
    root = pathlib.Path(__file__).resolve().parents[1]
    source = (
        root / "docs" / "figures" / "fundamental_theory_consciousness_map.svg"
    ).read_text(encoding="utf-8")
    for phrase in (
        "Theory-neutral primitive",
        "G: 𝓜 → 𝓠_G",
        "Q: 𝓜 → 𝓠_Q",
        "C: 𝓜 → 𝓠_C",
        "E: 𝓜 → 𝓠_E",
        "P11-P18",
        "Must not be defined using",
        "the candidate physical signature",
        "T(Ω) = (G(Ω), Q(Ω), C(Ω))",
        "H₀:  E = B_T ∘ T",
        "d_TOE^⊥ = rank D(Ψ_T, Ψ_E) − rank DΨ_T",
        "Exact witness: T(Ω)=T(Ω′) but E(Ω)≠E(Ω′)",
        "a positive residual would indicate non-factorization relative to the declared physical representation.",
        "It would not by itself prove a fifth spatial dimension, nonphysical substance, simulation ontology, or failure of quantum mechanics.",
    ):
        assert phrase in source

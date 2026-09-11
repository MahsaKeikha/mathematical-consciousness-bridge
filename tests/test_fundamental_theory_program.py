import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
PROGRAM = ROOT / "docs" / "fundamental_theory_consciousness_program.md"
STOCHASTIC = ROOT / "docs" / "stochastic_fundamental_bridge.md"
MAP = ROOT / "docs" / "figures" / "fundamental_theory_consciousness_map.svg"
NS = {"svg": "http://www.w3.org/2000/svg"}


def test_main_page_exposes_fundamental_theory_interface():
    text = README.read_text(encoding="utf-8")

    required = (
        "# 4.4 Fundamental theory / Theory-of-Everything interface",
        "fundamental_theory_consciousness_map.svg",
        "There is currently no experimentally established Theory of Everything",
        "T(\\Omega)=\\bigl(G(\\Omega),Q(\\Omega),C(\\Omega)\\bigr)",
    )
    for phrase in required:
        assert phrase in text


def test_my_big_toe_is_not_presented_as_scientific_fact():
    text = README.read_text(encoding="utf-8")
    program = PROGRAM.read_text(encoding="utf-8")

    assert "Thomas W. Campbell" in text
    assert "speculative falsifiable antecedents" in text
    assert "not as established premises" in text
    assert "not established scientific facts" in program
    assert "speculative falsifiable proposal" in program


def test_program_defines_exact_factorization_failure_and_controls():
    text = PROGRAM.read_text(encoding="utf-8")

    assert "E=B_T\\circ T" in text
    assert "\\Omega\\sim_T\\Omega'" in text
    assert "d_{\\mathrm{TOE}}^{\\perp}" in text
    assert "R_{E|T}" in text
    assert "No-free-metaphysics rule" in text
    assert "The last possibility matters" in text


def test_stochastic_bridge_defines_conditional_information_residual():
    text = STOCHASTIC.read_text(encoding="utf-8")

    assert "Markov kernel" in text
    assert "E\\perp\\!\\!\\!\\perp\\Omega\\mid T" in text
    assert "I(E;\\Omega\\mid T)=0" in text
    assert "\\mathcal I_{\\perp}^{\\mathrm{fund}}" in text
    assert "I(E;Z\\mid T)" in text
    assert "omitted physical variable" in text
    assert "would automatically prove" in text


def test_fundamental_theory_map_is_valid_svg_with_scientific_boundary():
    text = MAP.read_text(encoding="utf-8")

    assert "<svg" in text
    assert "Fundamental Theory to Consciousness" in text
    assert "Complete declared physical map" in text
    assert "Bridge factorization / residual test" in text
    assert "would not by itself prove" in text


def test_fundamental_theory_map_has_complete_attached_arrow_architecture():
    root = ET.parse(MAP).getroot()
    arrows = {
        path.attrib["id"]: path
        for path in root.findall("svg:path", NS)
        if path.attrib.get("id", "").startswith("arrow-")
    }

    expected_routes = {
        "arrow-fundamental-geometry": "M900 305 V360 H260 V405",
        "arrow-fundamental-quantum": "M900 305 V360 H690 V405",
        "arrow-fundamental-causal": "M900 305 V360 H1110 V405",
        "arrow-fundamental-experiential": "M900 305 V360 H1540 V405",
        "arrow-geometry-physical": "M260 625 V655 H760 V690",
        "arrow-quantum-physical": "M690 625 V690",
        "arrow-causal-physical": "M1110 625 V690",
        "arrow-physical-bridge": "M900 855 V930",
        "arrow-experiential-bridge": "M1540 625 V1032 H1380",
    }
    assert set(arrows) == set(expected_routes)

    for arrow_id, route in expected_routes.items():
        arrow = arrows[arrow_id]
        assert arrow.attrib["d"] == route
        assert arrow.attrib.get("marker-end") is None
        assert "marker-end:url(#arrow)" not in arrow.attrib.get("style", "")
        assert arrow.attrib["data-source"]
        assert arrow.attrib["data-target"]

    # Marker attachment comes from the shared .arrow/.dash classes; every route
    # ends exactly on the declared target box boundary rather than inside a box.
    style_text = "".join(root.find("svg:defs/svg:style", NS).itertext())
    assert ".arrow{stroke:#64748b;stroke-width:2.4;fill:none;marker-end:url(#arrow)}" in style_text
    assert ".dash{stroke:#94a3b8;stroke-width:2.2;stroke-dasharray:9 8;fill:none;marker-end:url(#arrow)}" in style_text

    assert arrows["arrow-geometry-physical"].attrib["data-target"] == "physical-map"
    assert arrows["arrow-quantum-physical"].attrib["data-target"] == "physical-map"
    assert arrows["arrow-causal-physical"].attrib["data-target"] == "physical-map"
    assert arrows["arrow-experiential-bridge"].attrib["data-target"] == "bridge-test"
    assert arrows["arrow-experiential-bridge"].attrib["data-source"] == "experiential"
    assert arrows["arrow-physical-bridge"].attrib["data-target"] == "bridge-test"

import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURES = (
    "research_architecture.svg",
    "theorem_roadmap.svg",
    "causal_structure_anatomy.svg",
    "p12_collision_map.svg",
    "p13_component_irredundancy.svg",
    "universal_proof_ladder.svg",
    "theory_comparison_map.svg",
)


def _numeric_svg_dimension(value: str) -> float:
    return float(value.removesuffix("px"))


def test_canonical_figures_follow_publication_layout_baseline():
    figure_root = ROOT / "docs" / "figures"

    for name in FIGURES:
        path = figure_root / name
        svg = ET.parse(path).getroot()
        width = _numeric_svg_dimension(svg.attrib["width"])
        height = _numeric_svg_dimension(svg.attrib["height"])

        assert width >= 1500, f"{name} canvas is too narrow for the canonical layout"
        assert height >= 850, f"{name} canvas is too short for the canonical layout"
        assert svg.attrib.get("role") == "img"
        assert "title" in svg.attrib.get("aria-labelledby", "")
        assert "desc" in svg.attrib.get("aria-labelledby", "")

        namespace = {"svg": "http://www.w3.org/2000/svg"}
        title = svg.find("svg:title", namespace)
        description = svg.find("svg:desc", namespace)
        assert title is not None and (title.text or "").strip()
        assert description is not None and (description.text or "").strip()

        source = path.read_text(encoding="utf-8")
        assert "feDropShadow" not in source
        assert "B-bar" not in source
        assert "gamma_" not in source
        assert " -> " not in source
        assert "Inter,Segoe UI,Arial" in source
        assert "Georgia" in source


def test_obsolete_candidate_shorthand_is_absent_from_current_text_sources():
    forbidden = "IR" + "CG"
    suffixes = {".md", ".py", ".svg", ".cff", ".toml"}

    offenders = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in suffixes:
            continue
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if forbidden in text or forbidden.lower() in text.lower():
            offenders.append(str(path.relative_to(ROOT)))

    assert not offenders, f"Obsolete candidate shorthand found in: {offenders}"


def test_obsolete_duplicate_paths_are_absent():
    obsolete_paths = (
        ROOT / "docs" / "figures" / ("ir" + "cg_anatomy.svg"),
        ROOT / "docs" / "proposition_11_intervention_resolved_causal_geometry.md",
        ROOT / "src" / "consciousness_bridge" / ("ir" + "cg_minimality.py"),
        ROOT / "src" / "consciousness_bridge" / ("ir" + "cg_pairwise_minimality.py"),
        ROOT / "src" / "consciousness_bridge" / "intervention_causal_geometry.py",
        ROOT / "tests" / ("test_ir" + "cg_minimality.py"),
        ROOT / "tests" / ("test_ir" + "cg_pairwise_minimality.py"),
        ROOT / "tests" / "test_intervention_causal_geometry.py",
    )

    present = [str(path.relative_to(ROOT)) for path in obsolete_paths if path.exists()]
    assert not present, f"Obsolete duplicate paths remain: {present}"

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOCS = ROOT / "docs"
WEBSITE = ROOT / "website"


def test_p75_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_75_target_model_adequacy_overidentification.md",
        DOCS / "p75_equation_provenance.md",
        DOCS / "figures" / "p75_target_model_adequacy_overidentification.svg",
        ROOT / "src" / "consciousness_bridge" / "target_model_adequacy.py",
        ROOT / "tests" / "test_target_model_adequacy.py",
    )
    for path in required:
        assert path.exists(), path


def test_p75_public_research_surfaces_expose_the_current_frontier() -> None:
    readme = README.read_text(encoding="utf-8")
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    navigation = (DOCS / "research_navigation.md").read_text(encoding="utf-8")
    detail = (DOCS / "detailed_proposition_record.md").read_text(encoding="utf-8")
    website = (WEBSITE / "index.html").read_text(encoding="utf-8")
    research_map = (WEBSITE / "research-map.html").read_text(encoding="utf-8")
    atlas = (WEBSITE / "visual-atlas.html").read_text(encoding="utf-8")

    for text in (readme, roadmap, navigation, detail, website, research_map, atlas):
        assert "P75" in text

    assert "0.75.0" in readme
    assert "75 proposition-level results" in readme
    assert "P1 through P75 with explicit dependency branches" in readme
    assert "proposition_75_target_model_adequacy_overidentification.md" in roadmap
    assert "| P75 |" in navigation
    assert "Complete P1 to P75 chronology" in detail
    assert "docs/figures/p75_target_model_adequacy_overidentification.svg" in website


def test_p75_scientific_boundary_is_preserved_on_public_surfaces() -> None:
    readme = README.read_text(encoding="utf-8")
    proof = (DOCS / "proposition_75_target_model_adequacy_overidentification.md").read_text(
        encoding="utf-8"
    )
    required = (
        "identifiability",
        "model adequacy",
        "generically just-identified",
        "six generic overidentifying degrees of freedom",
        "full-law",
        "does not establish",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in proof, token
    assert "physical-to-experiential bridge itself remains open" in readme

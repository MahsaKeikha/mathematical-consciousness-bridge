from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def test_p75_core_artifacts_exist() -> None:
    required = (
        DOCS / "proposition_75_target_model_adequacy_overidentification.md",
        DOCS / "p75_equation_provenance.md",
        DOCS / "figures" / "p75_target_model_adequacy_overidentification.svg",
        ROOT / "src" / "consciousness_bridge" / "target_model_adequacy.py",
        ROOT / "tests" / "test_target_model_adequacy.py",
    )
    for path in required:
        assert path.is_file(), path


def test_p75_uses_layered_publication_surfaces() -> None:
    proof_path = DOCS / "proposition_75_target_model_adequacy_overidentification.md"
    figure_path = DOCS / "figures" / "p75_target_model_adequacy_overidentification.svg"
    roadmap = (DOCS / "theorem_roadmap.md").read_text(encoding="utf-8")
    record = (DOCS / "detailed_proposition_record.md").read_text(encoding="utf-8")
    catalog = (DOCS / "figure_catalog.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert proof_path.name in roadmap
    assert proof_path.name in record
    assert figure_path.name in catalog
    assert "docs/theorem_roadmap.md" in readme
    assert "docs/detailed_proposition_record.md" in readme
    assert "docs/figure_catalog.md" in readme


def test_p75_scientific_boundary_remains_explicit() -> None:
    proof = (DOCS / "proposition_75_target_model_adequacy_overidentification.md").read_text(encoding="utf-8")
    provenance = (DOCS / "p75_equation_provenance.md").read_text(encoding="utf-8")
    source = (ROOT / "src" / "consciousness_bridge" / "target_model_adequacy.py").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    combined = "\n".join((proof, provenance, source)).lower()

    assert "physical-to-experiential bridge" in combined
    assert "consciousness" in combined
    assert any(token in combined for token in ("does not", "remains open", "inconclusive"))
    assert "The bridge remains an open scientific problem." in readme


def test_p75_release_history_is_preserved() -> None:
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    assert "# 0.75.0" in changelog

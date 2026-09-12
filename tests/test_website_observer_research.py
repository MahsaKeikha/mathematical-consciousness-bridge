from pathlib import Path

PAGE = Path("website/observer-research.html")


def test_observer_research_has_its_own_dedicated_public_page() -> None:
    page = PAGE.read_text(encoding="utf-8")

    required = (
        "Research I · Physical subsystem identification",
        "Spatiotemporal Observer Mathematics",
        "https://github.com/MahsaKeikha/spatiotemporal-observer-math",
        "58",
        "45",
        "33",
        "223",
        "moving world-tube",
        "The Research I question",
        "The inferred object",
        "Global recovery objective",
        "Visual evidence and reproducibility",
        "Research I → Research II",
    )
    for token in required:
        assert token in page


def test_observer_research_preserves_physical_to_experiential_boundary() -> None:
    page = PAGE.read_text(encoding="utf-8")

    required = (
        "Recovering a world-tube is a physical subsystem-identification result, not a conclusion about subjective experience",
        "It does <strong>not</strong> prove that the recovered subsystem is conscious",
        "A well-specified physical subsystem is the starting point of the bridge problem, not its answer",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in page


def test_observer_research_exposes_authoritative_original_audit_paths() -> None:
    page = PAGE.read_text(encoding="utf-8")

    required_paths = (
        "docs/visual_research_guide.md",
        "docs/physics_guide.md",
        "docs/physics_mathematics_citation_map.md",
        "docs/research_overview.md",
        "docs/research_index.md",
        "docs/assumption_ledger.md",
        "docs/bibliography.md",
        "docs/reproducible_results.md",
        "docs/proofs_and_conjectures.md",
        "docs/proposition_56_innovation_whitened_target.md",
        "docs/proposition_58_observer_bridge.md",
    )
    for path in required_paths:
        assert path in page

    # These guessed paths were previously exposed but are not part of the authoritative Research I record.
    assert "docs/scientific_foundations.md" not in page
    assert "docs/figures/physics_to_observer_pipeline.svg" not in page


def test_observer_research_links_forward_without_conflating_programs() -> None:
    page = PAGE.read_text(encoding="utf-8")

    assert 'href="research-lineage.html"' in page
    assert 'href="research-map.html"' in page
    assert "Research I identifies the physical subsystem" in page
    assert "Research II tests what more a scientifically defensible bridge would require" in page


def test_observer_research_is_visually_navigable_without_guessing() -> None:
    page = PAGE.read_text(encoding="utf-8")

    for section_id in ("question", "dynamics", "mathematics", "scores", "objective", "evidence", "handoff", "record"):
        assert f'id="{section_id}"' in page

    assert "research-jumpbar" in page
    assert "research-flowline" in page
    assert "research-card-grid" in page
    assert "research-figure-grid" in page
    assert "record-grid" in page

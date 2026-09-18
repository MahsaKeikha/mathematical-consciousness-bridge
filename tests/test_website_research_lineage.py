from pathlib import Path


def test_research_lineage_connects_both_public_repositories() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")

    required = (
        "Spatiotemporal Observer Mathematics",
        "Mathematical Consciousness Bridge",
        "https://github.com/MahsaKeikha/spatiotemporal-observer-math",
        "https://github.com/MahsaKeikha/mathematical-consciousness-bridge",
        "Research I repository",
        "Research II",
        "Research Map",
        "physical subsystem identification",
        "physical-to-experiential bridge",
    )
    for token in required:
        assert token in page




def test_lineage_exposes_auditable_research_one_entry_points() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")

    required_paths = (
        "docs/visual_research_guide.md",
        "docs/research_overview.md",
        "docs/research_index.md",
        "docs/physics_guide.md",
        "docs/assumption_ledger.md",
    )
    for path in required_paths:
        assert path in page



def test_lineage_exposes_current_research_three_v45_progression() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")

    for token in (
        "V1-V45</strong><span>formal validation stages",
        "20</strong><span>code-generated validation figures",
        "171</strong><span>tests in each CI job",
        "9</strong><span>reproducible validation runners",
        "Seven linked validation layers",
        "V1-V15 · identification and validation",
        "V16-V20 · electromagnetic observables",
        "V21-V25 · source identifiability",
        "V26-V30 · resolution and information limits",
        "V31-V35 · design and spatial specificity",
        "V36-V40 · finite-sample electromagnetic inference",
        "V41-V45 · multiplicity and selection-safe inference",
        "v36_v40_electromagnetic_finite_sample_validation.svg",
        "v41_v45_electromagnetic_selection_validation.svg",
        "electromagnetic-finite-sample-inference.md",
        "electromagnetic-selection-safe-inference.md",
        "statistically valid source inference is still not direct evidence that a source is consciousness or qualia",
    ):
        assert token in page


def test_lineage_keeps_research_three_empirical_boundary_visible() -> None:
    page = Path("website/research-lineage.html").read_text(encoding="utf-8")

    assert "Research III does not assume that consciousness is nonphysical" in page
    assert "statistical significance identifies an experiential target" in page
    assert "one scalar can serve as a universal consciousness meter" in page

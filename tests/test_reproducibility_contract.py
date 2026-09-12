from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_publication_figure_environment_is_pinned() -> None:
    lock = _read("requirements-figures.txt")
    assert "matplotlib==3.11.2" in lock
    assert "numpy==2.5.3" in lock


def test_plot_generators_use_deterministic_svg_metadata_and_ids() -> None:
    for path in (
        "scripts/generate_quantitative_atlas.py",
        "scripts/generate_quantum_foundations_atlas.py",
    ):
        source = _read(path)
        assert '"svg.hashsalt": "mathematical-consciousness-bridge-v0.81.0"' in source
        assert '"Date": None' in source
        assert '"Creator": "Mathematical Consciousness Bridge v0.81.0"' in source


def test_unified_figure_build_reapplies_documentation_metadata() -> None:
    source = _read("scripts/generate_all_figures.py")
    assert "enrich_figure_documentation.py" in source
    assert "_run_generator(ENRICHER)" in source


def test_figure_ci_requires_clean_regeneration() -> None:
    workflow = _read(".github/workflows/figures.yml")
    assert "requirements-figures.txt" in workflow
    assert "git status --porcelain" in workflow
    assert "exit 1" in workflow


def test_one_command_reproducibility_audit_is_exposed() -> None:
    makefile = _read("Makefile")
    scripts_readme = _read("scripts/README.md")
    guide = _read("docs/reproducibility.md")
    assert "reproduce:" in makefile
    assert "scripts/reproducibility_audit.py" in makefile
    assert "reproducibility_audit.py" in scripts_readme
    assert "make reproduce" in guide

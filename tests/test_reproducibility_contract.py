import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def _project_version() -> str:
    source = _read("pyproject.toml")
    match = re.search(
        r'^version = "([0-9]+\.[0-9]+\.[0-9]+)"$',
        source,
        re.MULTILINE,
    )
    assert match is not None
    return match.group(1)


def test_publication_figure_environment_is_pinned() -> None:
    lock = _read("requirements-figures.txt")
    assert "matplotlib==3.11.2" in lock
    assert "numpy==2.5.3" in lock


def test_plot_generators_use_deterministic_svg_metadata_and_ids() -> None:
    version = _project_version()
    for path in (
        "scripts/generate_quantitative_atlas.py",
        "scripts/generate_quantum_foundations_atlas.py",
    ):
        source = _read(path)
        assert (
            f'"svg.hashsalt": "mathematical-consciousness-bridge-v{version}"'
            in source
        )
        assert '"Date": None' in source
        assert f'"Creator": "Mathematical Consciousness Bridge v{version}"' in source


def test_unified_figure_build_reapplies_documentation_metadata() -> None:
    source = _read("scripts/generate_all_figures.py")
    assert "enrich_figure_documentation.py" in source
    assert "_run_script(ENRICHER)" in source
    assert "_run_script(PUBLICATION_SYNCER)" in source
    assert '_run_script(PUBLICATION_SYNCER, "--check")' in source


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

def test_figure_enrichment_preserves_curated_theorem_metadata() -> None:
    source = _read("scripts/enrich_figure_documentation.py")
    assert "def _has_curated_metadata" in source
    assert "if _has_curated_metadata(svg):" in source
    assert 'enriched = svg' in source

def test_generated_catalog_preserves_p55_scope_language() -> None:
    catalog = _read("docs/figure_catalog.md")
    for token in (
        "metric shortcutting",
        "support-preserving",
        "shortcut lower certificate",
        "physical-to-experiential bridge",
    ):
        assert token in catalog


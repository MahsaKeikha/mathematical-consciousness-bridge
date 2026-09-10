from pathlib import Path
import re
import tomllib

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website" / "index.html"


def _project_version() -> str:
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    return data["project"]["version"]


def _max_proposition_number() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers)


def test_website_assets_exist():
    assert WEBSITE.exists()
    assert (ROOT / "website" / "styles.css").exists()
    assert (ROOT / "website" / "app.js").exists()


def test_website_release_status_matches_repository():
    html = WEBSITE.read_text(encoding="utf-8")
    version = _project_version()
    proposition = _max_proposition_number()
    assert f"v{version}" in html
    assert f"<strong>{proposition}</strong><span>proposition-level results</span>" in html


def test_website_latest_figure_is_real():
    html = WEBSITE.read_text(encoding="utf-8")
    figure = "docs/figures/p64_fast_heterogeneous_integer_approximation.svg"
    assert figure in html
    assert (ROOT / figure).exists()


def test_website_has_scientific_boundary_and_provenance_paths():
    html = WEBSITE.read_text(encoding="utf-8")
    required = [
        "Scientific boundary",
        "does <strong>not</strong> claim that consciousness has already been derived from physics",
        "Equation and citation map",
        "Citation policy",
        "Reference audit",
        "Theorem roadmap",
        "Falsification and evidence",
        "Repository-original theorem or computation",
        "Open hypothesis or theorem target",
    ]
    for text in required:
        assert text in html


def test_publication_architecture_has_required_claim_layers():
    text = (ROOT / "docs" / "research_publication_architecture.md").read_text(encoding="utf-8")
    for label in [
        "Layer A. Standard mathematics",
        "Layer B. Established physical theory",
        "Layer C. External empirical evidence",
        "Layer D. Repository-original theorem or computational result",
        "Layer E. Open hypothesis, research target, or conjecture",
    ]:
        assert label in text


def test_website_links_to_existing_core_record_documents():
    for path in [
        "docs/research_navigation.md",
        "docs/research_publication_architecture.md",
        "docs/equation_and_citation_map.md",
        "docs/citation_and_reference_policy.md",
        "docs/reference_audit.md",
        "docs/theorem_roadmap.md",
        "docs/falsification_program.md",
        "CITATION.cff",
    ]:
        assert (ROOT / path).exists(), path

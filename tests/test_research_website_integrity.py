from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WEBSITE_DIR = ROOT / "website"
WEBSITE = WEBSITE_DIR / "index.html"
PUBLIC_PAGES = [
    "index.html",
    "research-map.html",
    "physics-mathematics.html",
    "visual-atlas.html",
    "sources.html",
]


def _project_version() -> str:
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
    assert match is not None
    return match.group(1)


def _max_proposition_number() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*_*.md"):
        match = re.match(r"proposition_(\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers)


def test_website_assets_and_public_pages_exist():
    assert (WEBSITE_DIR / "styles.css").exists()
    assert (WEBSITE_DIR / "app.js").exists()
    for page in PUBLIC_PAGES:
        assert (WEBSITE_DIR / page).exists(), page


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
        "docs/physics_equation_provenance.md",
        "docs/foundational_physics_mathematics_bibliography.md",
        "docs/quantum_foundations_and_bridge_test.md",
        "docs/quantitative_physics_mathematics_atlas.md",
        "references.bib",
        "foundational_physics_mathematics.bib",
        "empirical_consciousness_measurement.bib",
        "CITATION.cff",
    ]:
        assert (ROOT / path).exists(), path


def test_secondary_page_navigation_has_no_missing_local_pages():
    local_page_pattern = re.compile(r'href="([a-z0-9-]+\.html)"')
    for page in PUBLIC_PAGES:
        html = (WEBSITE_DIR / page).read_text(encoding="utf-8")
        for target in local_page_pattern.findall(html):
            assert (WEBSITE_DIR / target).exists(), f"{page} -> {target}"


def test_visual_atlas_referenced_repository_figures_exist():
    html = (WEBSITE_DIR / "visual-atlas.html").read_text(encoding="utf-8")
    figure_pattern = re.compile(
        r"raw\.githubusercontent\.com/MahsaKeikha/"
        r"mathematical-consciousness-bridge/main/(docs/figures/[^"]+\.svg)"
    )
    figures = figure_pattern.findall(html)
    assert len(figures) >= 10
    for figure in figures:
        assert (ROOT / figure).exists(), figure


def test_research_map_covers_full_proposition_frontier():
    html = (WEBSITE_DIR / "research-map.html").read_text(encoding="utf-8")
    assert "P1-P10" in html
    assert "P11-P18" in html
    assert "P19-P24" in html
    assert "P25-P37" in html
    assert "P38-P44" in html
    assert "P45-P53" in html
    assert "P54-P64" in html
    assert _max_proposition_number() == 64

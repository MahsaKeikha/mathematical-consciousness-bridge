from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_sources_page_records_tegmark_origin_without_overclaiming() -> None:
    sources = _read("website/sources.html")
    assert 'id="research-origins"' in sources
    assert "Max Tegmark" in sources
    assert "Consciousness as a State of Matter" in sources
    assert "10.1016/j.chaos.2015.03.014" in sources
    assert "arXiv:1401.1219" in sources
    assert "intellectual and physical-context background" in sources
    assert "not evidence for the repository's later original propositions" in sources


def test_machine_readable_bibliography_contains_exact_tegmark_metadata() -> None:
    bibliography = _read("references.bib")
    assert "@article{tegmark2015consciousness" in bibliography
    assert "Consciousness as a State of Matter" in bibliography
    assert "Chaos, Solitons \\& Fractals" in bibliography
    assert "volume  = {76}" in bibliography
    assert "pages   = {238--270}" in bibliography
    assert "year    = {2015}" in bibliography
    assert "doi     = {10.1016/j.chaos.2015.03.014}" in bibliography


def test_claim_evidence_standard_separates_evidential_roles() -> None:
    standard = _read("docs/claim_evidence_standard.md")
    required = (
        "External established results",
        "Repository-original theorems and constructions",
        "Modeling assumptions and definitions",
        "Empirical claims",
        "Generated and synthetic material",
        "Open bridge and interpretation claims",
        "Research origins versus evidential support",
        "arXiv:1401.1219",
    )
    for marker in required:
        assert marker in standard


def test_sources_page_points_to_current_p86_audit_record() -> None:
    sources = _read("website/sources.html")
    assert 'id="p86-source"' in sources
    assert "Current theorem source · P86" in sources
    assert "L85 = 0 &lt; L86 = 1/192" in sources
    assert "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md" in sources
    assert "p86_equation_provenance.md" in sources
    assert "weighted_quad_projection_parity_functional_separation.py" in sources
    assert "test_weighted_quad_projection_parity_functional_separation.py" in sources


def test_public_provenance_does_not_make_priority_or_ontology_claims() -> None:
    public = _read("website/sources.html") + _read("docs/claim_evidence_standard.md")
    forbidden = (
        "first theory of consciousness",
        "first proof of consciousness",
        "proves consciousness is nonphysical",
        "proves consciousness is a new dimension",
        "Tegmark validates this framework",
        "Tegmark proves this framework",
    )
    for phrase in forbidden:
        assert phrase not in public

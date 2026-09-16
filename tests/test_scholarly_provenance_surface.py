from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_sources_page_records_tegmark_origin_with_collegial_scope() -> None:
    sources = _read("website/sources.html")
    assert 'id="research-origins"' in sources
    assert "Max Tegmark" in sources
    assert "Consciousness as a State of Matter" in sources
    assert "10.1016/j.chaos.2015.03.014" in sources
    assert "arXiv:1401.1219" in sources
    assert "important conceptual starting point" in sources
    assert "distinct mathematical framework" in sources


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
        "Research origins and scholarly provenance",
        "arXiv:1401.1219",
    )
    for marker in required:
        assert marker in standard


def test_claim_source_matrix_preserves_p91_publication_snapshot() -> None:
    matrix = _read("docs/claim_source_matrix.md")
    required = (
        "Claim-to-Source Scientific Audit Matrix",
        "Research origin",
        "Formal consciousness modeling",
        "external methodological background plus repository formulation",
        "P75 model family",
        "P86 weighted four-event compatibility",
        "L85 = 0 < L86 = 1/192",
        "P87 bounded primitive four-event compatibility",
        "L86 = 1/192 < L87 = 1/96",
        "P88 radius-three bounded primitive four-event compatibility",
        "208,560-functional P88 family",
        "L87 = 1/96 < L88 = 1/64",
        "Historical P91 publication snapshot",
        "The current repository contains 91 proposition-level results",
        "P91 is the current Research II theorem frontier",
        "P91 mixed-prevalence rank-two flattening separation",
        "passing CI supports internal consistency and reproducibility; it is not external peer review",
    )
    for marker in required:
        assert marker in matrix


def test_reference_audit_records_tegmark_as_research_origin() -> None:
    audit = _read("docs/reference_audit.md")
    assert "Tegmark, 2015" in audit
    assert "10.1016/j.chaos.2015.03.014" in audit
    assert "arXiv:1401.1219" in audit
    assert "important conceptual starting point" in audit
    assert "distinct mathematical framework" in audit


def test_sources_page_points_to_current_p100_and_ordered_historical_records() -> None:
    sources = _read("website/sources.html")

    assert 'id="p100-source"' in sources
    assert "Current theorem source · P100" in sources
    assert "proposition_100_anytime_sequential_eprocess.md" in sources
    assert "p100_equation_provenance.md" in sources
    assert "anytime_sequential_eprocess.py" in sources
    assert "test_anytime_sequential_eprocess.py" in sources

    expected_historical = (
        (91, "1/42", "proposition_91_mixed_prevalence_rank_two_flattening_separation.md"),
        (90, "5/72", "proposition_90_exact_nonlinear_rank_one_separation.md"),
        (89, "5/168", "proposition_89_complete_linear_parity_duality.md"),
        (88, "L87 = 1/96 &lt; L88 = 1/64", "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md"),
        (87, "L86 = 1/192 &lt; L87 = 1/96", "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md"),
        (86, "L85 = 0 &lt; L86 = 1/192", "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md"),
    )
    for number, marker, proof in expected_historical:
        assert f'id="p{number}-source"' in sources
        assert f"Detailed theorem source record · P{number}" in sources
        assert marker in sources
        assert proof in sources

    assert "p91_equation_provenance.md" in sources
    assert "mixed_prevalence_rank_two_flattening_separation.py" in sources
    assert "test_mixed_prevalence_rank_two_flattening_separation.py" in sources
    assert "p90_equation_provenance.md" in sources
    assert "p89_equation_provenance.md" in sources
    assert "claim_source_matrix.md" in sources

    for number in range(86, 100):
        assert f"Current theorem source · P{number}" not in sources


def test_public_provenance_does_not_make_priority_or_ontology_claims() -> None:
    public = (
        _read("website/sources.html")
        + _read("docs/claim_evidence_standard.md")
        + _read("docs/claim_source_matrix.md")
    )
    forbidden = (
        "first theory of consciousness",
        "first proof of consciousness",
        "proves consciousness is nonphysical",
        "proves consciousness is a new dimension",
        "Tegmark validates this framework",
        "Tegmark proves this framework",
        "this origin citation does not make Tegmark's paper evidence",
        "not evidence for the repository's later original propositions",
        "not evidential support for later repository-original propositions",
    )
    for phrase in forbidden:
        assert phrase not in public

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_public_sources_page_uses_self_contained_research_i_provenance() -> None:
    sources = _read("website/sources.html")
    assert 'id="research-origins"' in sources
    assert "Research I provenance" in sources
    assert "self-contained mathematical and computational research program" in sources
    assert "repository-original results" in sources

def test_machine_readable_bibliography_remains_parseable_source_record() -> None:
    bibliography = _read("references.bib")
    assert "@article{" in bibliography
    assert "doi" in bibliography.lower()


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
    )
    for marker in required:
        assert marker in standard


def test_claim_source_matrix_preserves_p91_publication_snapshot() -> None:
    matrix = _read("docs/claim_source_matrix.md")
    required = (
        "Claim-to-Source Scientific Audit Matrix",
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


def test_reference_audit_retains_evidence_classification() -> None:
    audit = _read("docs/reference_audit.md")
    assert "Reference Audit" in audit
    assert "Evidence class" in audit
    assert "Interpretation rule" in audit


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
        "this origin citation does not make Tegmark's paper evidence",
        "not evidence for the repository's later original propositions",
        "not evidential support for later repository-original propositions",
    )
    for phrase in forbidden:
        assert phrase not in public

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


def test_claim_source_matrix_tracks_p88_frontier_and_boundaries() -> None:
    matrix = _read("docs/claim_source_matrix.md")
    for marker in (
        "Claim-to-Source Scientific Audit Matrix",
        "P75 model family",
        "P87 bounded primitive four-event compatibility",
        "P88 radius-three bounded primitive four-event compatibility",
        "L87 = 1/96 < L88 = 1/64",
        "88 proposition-level results",
        "P88 is the current theorem frontier",
        "passing CI supports internal consistency and reproducibility; it is not external peer review",
    ):
        assert marker in matrix


def test_sources_page_points_to_current_p88_and_previous_p87_records() -> None:
    sources = _read("website/sources.html")
    for marker in (
        'id="p88-source"',
        "Current theorem source · P88",
        "208,560",
        "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64",
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
        "p88_equation_provenance.md",
        "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        'id="p87-source"',
        "Previous theorem source · P87",
        "L86 = 1/192 &lt; L87 = 1/96",
        "claim_source_matrix.md",
    ):
        assert marker in sources


def test_machine_readable_bibliography_contains_exact_tegmark_metadata() -> None:
    bibliography = _read("references.bib")
    assert "@article{tegmark2015consciousness" in bibliography
    assert "doi     = {10.1016/j.chaos.2015.03.014}" in bibliography


def test_public_provenance_does_not_make_priority_or_ontology_claims() -> None:
    public = _read("website/sources.html") + _read("docs/claim_source_matrix.md")
    for phrase in (
        "first theory of consciousness",
        "first proof of consciousness",
        "proves consciousness is nonphysical",
        "proves consciousness is a new dimension",
        "Tegmark validates this framework",
        "Tegmark proves this framework",
    ):
        assert phrase not in public

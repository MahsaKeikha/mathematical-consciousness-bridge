from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "website" / "measurement-science.html"


def _page() -> str:
    return PAGE.read_text(encoding="utf-8")


def test_research_three_page_leads_with_the_formal_measurement_problem() -> None:
    text = _page()

    required = (
        "A formal measurement framework for claims about consciousness",
        "Formal measurement problem",
        "p(R,B,N,P,A\\mid E,Y,I,C,\\theta)",
        "\\mathcal I_E(D,\\mathcal A)",
        "Consciousness Evidence Profile",
        "dependence-robust partial identification with sharp Fr&eacute;chet-Hoeffding bounds",
        "Structural measurement pipeline",
        "M0-M7",
        "Scope of current evidence",
    )
    for marker in required:
        assert marker in text


def test_research_three_page_does_not_restore_the_old_audit_banner() -> None:
    text = _page()

    forbidden = (
        "Verified repository snapshot",
        "The public page is pinned to the completed foundational framework",
        "What would it take to measure consciousness without defining it by the signal we happen to record?",
        "Implemented now versus not yet established",
    )
    for marker in forbidden:
        assert marker not in text


def test_provenance_is_kept_but_moved_below_the_scientific_content() -> None:
    text = _page()

    science_anchor = text.index("Canonical scientific record")
    scope_anchor = text.index("Scope of current evidence")
    provenance_anchor = text.index("Reproducibility and provenance")

    assert science_anchor < scope_anchor < provenance_anchor
    assert "3cf9202977953644c980246c1f3e46a3514b3a4a" in text
    assert "35</strong><span>tests in each CI job" in text


def test_research_three_reader_surface_keeps_claim_boundaries_explicit() -> None:
    text = _page()

    assert "does not establish a universal consciousness biomarker" in text
    assert "direct third-person readout of qualia" in text
    assert "validated clinical diagnostic device" in text
    assert "ontological identity" in text
    assert "Inconclusive is an allowed result" in text


def test_research_three_page_respects_reader_facing_dash_policy() -> None:
    text = _page()
    assert "\u2013" not in text
    assert "\u2014" not in text

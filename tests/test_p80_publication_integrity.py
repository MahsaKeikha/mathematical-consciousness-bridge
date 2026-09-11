import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_p80_proof_records_the_complete_feasibility_gate() -> None:
    proof = _read("docs/proposition_80_simplex_coupled_model_separation.md")

    required = (
        r"r_{\square}",
        r"A(r)\le1\le C(r)",
        r"L_{80}(B)=\max(r_{\square},r_A,r_C)",
        r"L_{80}(B)\ge L_{78}(B)",
        "Failure of the strict inequality is inconclusive",
        "physical-to-experiential bridge therefore remains open",
    )
    for token in required:
        assert token in proof


def test_p80_provenance_has_direct_routes_for_every_equation_row() -> None:
    provenance = _read("docs/p80_equation_provenance.md")
    lines = provenance.splitlines()

    in_equation_table = False
    data_rows = []
    for line in lines:
        if line.startswith("| Object | Formula or statement"):
            in_equation_table = True
            continue
        if in_equation_table and not line.startswith("|"):
            break
        if in_equation_table and line.startswith("|") and "---" not in line:
            data_rows.append(line)

    assert data_rows
    for row in data_rows:
        assert re.search(r"\[[^\]]+\]\([^)]+\)", row), row


def test_p80_reproducibility_map_is_fully_clickable() -> None:
    proof = _read("docs/proposition_80_simplex_coupled_model_separation.md")
    section = proof.split("## 8. Reproducibility map", 1)[1]
    table = section.split("For equation-level provenance", 1)[0]

    rows = [
        line
        for line in table.splitlines()
        if line.startswith("|") and "---" not in line and "Research object" not in line
    ]
    assert len(rows) >= 8
    for row in rows:
        assert re.search(r"\[[^\]]+\]\([^)]+\)", row), row


def test_p80_artifact_links_resolve_to_repository_paths() -> None:
    expected = (
        "src/consciousness_bridge/simplex_coupled_model_separation.py",
        "tests/test_simplex_coupled_model_separation.py",
        "tests/test_p80_figure_geometry.py",
        "docs/p80_equation_provenance.md",
        "docs/proposition_80_simplex_coupled_model_separation.md",
        "docs/figures/p80_simplex_coupled_model_separation.svg",
        "docs/proposition_78_certified_continuous_model_separation.md",
        "docs/proposition_79_certified_sampling_radius.md",
        "docs/proposition_77_full_law_model_set_separation.md",
        "docs/proposition_75_target_model_adequacy_overidentification.md",
    )
    for relative in expected:
        assert (ROOT / relative).exists(), relative


def test_p80_scope_is_consistent_across_proof_provenance_and_source() -> None:
    texts = (
        _read("docs/proposition_80_simplex_coupled_model_separation.md"),
        _read("docs/p80_equation_provenance.md"),
        _read("src/consciousness_bridge/simplex_coupled_model_separation.py"),
    )

    for text in texts:
        assert "physical-to-experiential bridge" in text
        assert "consciousness" in text

    assert "does not close the physical-to-experiential bridge" in texts[0]
    assert "does not close the physical-to-experiential bridge" in texts[1]
    assert "does not solve the physical-to-experiential bridge" in texts[2]

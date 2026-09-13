import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEOREM = ROOT / "docs/proposition_86_exact_quadruple_projection_parity_functional.md"
PROVENANCE = ROOT / "docs/p86_equation_provenance.md"
IMPLEMENTATION = (
    ROOT / "src/consciousness_bridge/quadruple_projection_parity_functional_separation.py"
)
SEARCH = ROOT / "scripts/search_p86_strict_witness.py"


def test_p86_core_publication_files_exist() -> None:
    for path in (THEOREM, PROVENANCE, IMPLEMENTATION, SEARCH):
        assert path.exists(), path


def test_p86_theorem_records_exact_hierarchy_and_scope() -> None:
    text = THEOREM.read_text(encoding="utf-8")
    for token in (
        "2640",
        "L_{85}(B)=\\frac5{48}",
        "L_{86}(B)=\\frac9{64}",
        "\\frac7{192}",
        "Q(\\widehat p)=-\\frac98",
        "I_B(Q)=[0,0]",
        "D(Q)=2\\cdot2+12\\cdot0+2\\cdot2=\\boxed8",
        "does not identify the P75 latent state with consciousness",
        "physical-to-experiential bridge",
    ):
        assert token in text, token


def test_p86_provenance_classifies_new_and_imported_steps() -> None:
    text = PROVENANCE.read_text(encoding="utf-8")
    for token in (
        "imported project definition from P75",
        "new P86 joint observable",
        "standard multi-affine box-extremum principle",
        "new P86 combination theorem",
        "project-specific exact regression witness",
        "L_{85}=\\frac5{48}",
        "L_{86}=\\frac9{64}",
    ):
        assert token in text, token


def test_p86_search_requires_strict_improvement_over_complete_p85() -> None:
    text = SEARCH.read_text(encoding="utf-8")
    for token in (
        "Random(20260913)",
        "p75_box_p85_linf_lower_bound_exact",
        "p75_box_quadruple_parity_witness_exact",
        "witness.lower_bound <= p85",
        "FOUND_P86_STRICT_WITNESS",
        "strict_gain",
    ):
        assert token in text, token


def test_p86_seeded_search_reproduces_the_strict_record() -> None:
    completed = subprocess.run(
        [sys.executable, str(SEARCH)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
        timeout=60,
    )
    output = completed.stdout
    for token in (
        "FOUND_P86_STRICT_WITNESS",
        "iteration=1",
        "p85_bound=Fraction(5, 48)",
        "p86_quadruple_bound=Fraction(9, 64)",
        "strict_gain=Fraction(7, 192)",
    ):
        assert token in output, output

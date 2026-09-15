"""Narrow post-promotion fixes for the P93 publication migration.

This temporary feature-branch helper repairs exact reader, test, citation, and
reproducibility contracts that are outside the main P93 frontier block. It is
removed before merge and never becomes part of the permanent publication path.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _replace(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if old in text:
        target.write_text(text.replace(old, new), encoding="utf-8")


def _replace_once(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    if old in text:
        target.write_text(text.replace(old, new, 1), encoding="utf-8")


def _rewrite_p93_reproducibility_section() -> None:
    path = ROOT / "docs/reproducibility.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "| Run only the current P90 theorem checks | focused P90 commands below |",
        "| Run only the current P93 theorem checks | focused P93 commands below |",
    )
    start = text.index("## 5. Focused audit of the current P93 frontier")
    end = text.index("\n---\n\n## 6. Run the full tests", start)
    section = r'''## 5. Focused audit of the current P93 frontier

The current theorem frontier is **P93**.

Its direct technical record is:

```text
docs/proposition_93_localized_sign_coherence_rejection.md
docs/p93_equation_provenance.md
src/consciousness_bridge/localized_sign_coherence_rejection.py
tests/test_localized_sign_coherence_rejection.py
docs/figures/p93_localized_sign_coherence_rejection.svg
figures/manifest.json
```

Run the focused theorem and publication checks with:

```bash
python -m pytest -q \
  tests/test_localized_sign_coherence_rejection.py \
  tests/test_p93_reader_surface_coherence.py \
  tests/test_figure_publication_sync.py \
  tests/test_frontier_publication_consistency.py
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

P93 is the finite-data continuation of P92's nonlinear three-minor sign-coherence witness. The three determinants use only seven distinct observable cells, so the simultaneous IID confidence radius is

\[
\varepsilon_{n,7}(\alpha)
=
\sqrt{\frac{\log(14/\alpha)}{2n}}.
\]

For the established witness, the determinant values are

\[
-\frac1{48},\qquad \frac1{64},\qquad \frac5{192},
\]

with exact sign-stability radii

\[
\frac1{24},\qquad \frac3{56},\qquad \frac5{72}.
\]

The limiting radius is therefore `1/24`. At 95 percent confidence, exact P79 rational certification proves

```text
epsilon_1622,7 > 1/24
epsilon_1623,7 < 1/24
```

so **1623 is the exact mathematical crossing**. Because the established empirical proportions have denominator 24, the first exact replication of that profile that also clears the certificate is

```text
1632 = 68 x 24.
```

For comparison, the generic P77 full-law fixed-population-margin sufficient condition at margin `1/24` crosses at 7444. These are different guarantees: P77 is a generic full-law design bound, while P93 is localized to the observed P92 nonlinear sign witness.

P93 does not claim universal or minimax sample complexity. Non-rejection remains inconclusive. The theorem does not identify the latent state with consciousness, establish nonphysicality, validate an alternative ontology, or close the physical-to-experiential bridge.
'''
    path.write_text(text[:start] + section.rstrip() + text[end:], encoding="utf-8")


def _rewrite_citation_frontier() -> None:
    path = ROOT / "CITATION.md"
    text = path.read_text(encoding="utf-8")
    start = text.index("## Current theorem frontier: P93")
    end = text.index("\n## Historical mixed-prevalence frontier: P91", start)
    section = '''## Current theorem frontier: P93

The current documented theorem frontier is **P93**. The formal package release remains **Version 0.82.0**. P93 converts P92's exact nonlinear three-minor sign-coherence obstruction into a finite-sample rejection theorem using only the seven observable cells entering that witness. At 95 percent confidence, exact P79 rational sampling-radius certification places the mathematical crossing between `n = 1622` and `n = 1623`. Because the established empirical proportions have denominator 24, the first exact replication of the original profile that also clears the certificate is `n = 1632 = 68 x 24`.

For comparison, the generic P77 full-law fixed-population-margin sufficient condition at margin `1/24` crosses at `n = 7444`. P77 and P93 provide different guarantees, and P93 does not claim universal or minimax sample complexity.

- Proof: [`proposition_93_localized_sign_coherence_rejection.md`](docs/proposition_93_localized_sign_coherence_rejection.md)
- Equation provenance: [`p93_equation_provenance.md`](docs/p93_equation_provenance.md)
- Implementation: [`localized_sign_coherence_rejection.py`](src/consciousness_bridge/localized_sign_coherence_rejection.py)
- Exact tests: [`test_localized_sign_coherence_rejection.py`](tests/test_localized_sign_coherence_rejection.py)

P93 remains a conditional finite-sample model-rejection theorem. Non-rejection is inconclusive. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.
'''
    text = text[:start] + section.rstrip() + text[end:]
    text = text.replace(
        "[Detailed proposition record](docs/detailed_proposition_record.md): P1 through P92 chronological theorem record.",
        "[Detailed proposition record](docs/detailed_proposition_record.md): P1 through P93 chronological theorem record.",
    )
    duplicate = '''## Proposition 92 method citation

For work that uses the exact full-cube mixed-prevalence distance theorem, cite the program together with **Proposition 92: Exact Global Mixed-Prevalence Distance** and its [equation provenance record](docs/p92_equation_provenance.md). P92 proves `d_inf(P_emp, M75) = 1/24` for the established witness and complete P75 parameter cube.'''
    text = text.replace(duplicate + "\n\n" + duplicate, duplicate)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    _replace("website/index.html", "Explore all 92 results", "Explore all 93 results")
    _replace(
        "website/index.html",
        "P92 current theorem frontier · v0.82.0",
        "P93 current theorem frontier · v0.82.0",
    )

    _replace(
        "tests/test_figure_publication_sync.py",
        'assert manifest["current_frontier"] == "P92"',
        'assert manifest["current_frontier"] == "P93"',
    )
    _replace_once(
        "tests/test_figure_publication_sync.py",
        "    p93 = text.index('id=\"p93-frontier\"')\n    p93 = text.index('id=\"p93-frontier\"')\n",
        "    p93 = text.index('id=\"p93-frontier\"')\n    p92 = text.index('id=\"p92-frontier\"')\n",
    )
    _replace_once(
        "tests/test_figure_publication_sync.py",
        "    p93 = text.index('id=\"p93-frontier\"')\n    p93 = text.index('id=\"p93-frontier\"')\n    research_iii =",
        "    p93 = text.index('id=\"p93-frontier\"')\n    research_iii =",
    )

    _replace(
        "tests/test_reader_experience.py",
        "def test_no_reader_facing_html_page_advertises_pre_p92_as_current() -> None:",
        "def test_no_reader_facing_html_page_advertises_pre_p93_as_current() -> None:",
    )
    _replace(
        "tests/test_reader_experience.py",
        "overview.index('id=\"project-journey\"') < overview.index('id=\"p92-frontier\"')",
        "overview.index('id=\"project-journey\"') < overview.index('id=\"p93-frontier\"')",
    )
    _replace(
        "tests/test_publication_contract_v2.py",
        "for number in range(1, 93):",
        "for number in range(1, 94):",
    )

    _rewrite_p93_reproducibility_section()
    _rewrite_citation_frontier()
    _replace(
        "docs/detailed_proposition_record.md",
        "A first-time reader should not read this page as 91 disconnected proposition-level results.",
        "A first-time reader should not read this page as 93 disconnected proposition-level results.",
    )

    # Research III synchronization is independent of theorem mathematics, but
    # its homepage marker must follow the current Research II publication head.
    _replace(
        "scripts/synchronize_research_three_website.py",
        'CURRENT_HOME_MARKER = "<!-- current-frontier-home: P92 -->"',
        'CURRENT_HOME_MARKER = "<!-- current-frontier-home: P93 -->"',
    )

    print("[P93] publication contracts repaired")


if __name__ == "__main__":
    main()

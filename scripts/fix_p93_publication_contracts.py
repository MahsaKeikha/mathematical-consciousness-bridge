"""Narrow post-promotion fixes for the P93 publication migration.

This temporary feature-branch helper repairs exact reader, test, citation, and
reproducibility contracts that are outside the main P93 frontier block. It is
removed before merge and never becomes part of the permanent publication path.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

P93_READER_BLOCK = '''<section class="boundary" id="p93-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P93</p><h2>P92's exact population obstruction now has a localized finite-data rejection rule</h2><p>P93 controls only the seven observable cells entering the P92 sign witness. At 95 percent confidence, the mathematical radius crosses at 1623 samples; the first exact replication of the original profile that clears is 1632. Non-rejection remains inconclusive.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_93_localized_sign_coherence_rejection.md">Read P93</a></p></div></section>'''

P93_RESEARCH_MAP_BLOCK = '''<section id="p93-research-map" class="theorem-frontier">
  <div class="section-head"><p class="eyebrow">P93 · Localized finite-sample nonlinear rejection</p><h2>P93: Can finite IID data preserve the P92 sign obstruction strongly enough to reject P75?</h2></div>
  <p>Yes. The three P92 minors use only seven distinct observable cells. If their empirical determinant product is negative and the P79-certified seven-cell sampling radius is smaller than every empirical determinant sign-stability radius, the unknown population has the same impossible sign pattern and P75 is rejected at confidence at least 1-alpha.</p>
  <p><strong>Established profile at 95 percent confidence:</strong> mathematical radius crossing 1622/1623; first exact 24-count replication that clears, 1632.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_93_localized_sign_coherence_rejection.md">proposition_93_localized_sign_coherence_rejection.md</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p93_equation_provenance.md">p93_equation_provenance.md</a> · <a href="index.html#p93-frontier">Current frontier</a></p>
</section>'''


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


def _place_block_before(path: str, block: str, marker: str) -> None:
    target = ROOT / path
    text = target.read_text(encoding="utf-8")
    text = text.replace("\n\n" + block, "").replace(block, "")
    if marker not in text:
        raise RuntimeError(f"missing insertion marker in {path}: {marker}")
    text = text.replace(marker, block + "\n\n" + marker, 1)
    target.write_text(text, encoding="utf-8")


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


def _repair_reader_html() -> None:
    start = ROOT / "website/start-here.html"
    text = start.read_text(encoding="utf-8")
    replacements = (
        ("Open all 92 Research II results", "Open all 93 Research II results"),
        ("The 92 propositions are the formal theorem record of Research II.", "The 93 propositions are the formal theorem record of Research II."),
        ("P1-P92 build", "P1-P93 build"),
        ("P75-P92 test", "P75-P93 test"),
        ("<span>P75-P92</span>", "<span>P75-P93</span>"),
        ("You do not need to read 92 Research II proofs in order", "You do not need to read 93 Research II proofs in order"),
        ("Focus on P19 and P71-P91", "Focus on P19 and P71-P93"),
        ("complete 90-result Research II dependency structure", "complete 93-result Research II dependency structure"),
        ("<h2>P78-P91 develop certified nonlinear separation from the declared continuous model family</h2>", "<h2>P78-P93 develop certified nonlinear separation and its finite-sample handoff</h2>"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    p91_tail = '<p><strong>P91 extends the nonlinear result to arbitrary latent prevalence.</strong> For every two-component P75 law, the declared (X1,X4) versus (X2,X3) 4 by 4 flattening has rank at most two, so every 3 by 3 minor vanishes. On the established empirical witness, exact nonnegative interval certification excludes the closed full-law L-infinity ball of radius <strong>1/42</strong>, while an explicit rational point with prevalence <strong>4/5</strong> lies at distance <strong>1/24</strong>. Thus <strong>1/42 &lt; d_inf(P_emp, M75) &lt;= 1/24</strong>. The upper endpoint is not claimed to be the exact global optimum.</p>'
    if p91_tail in text and "P93 carries that exact obstruction into finite data" not in text:
        text = text.replace(
            p91_tail,
            p91_tail
            + '\n      <p><strong>P92 closes the mixed-prevalence population distance exactly.</strong> Three selected determinant signs imply the exact full-cube distance <strong>d_inf(P_emp, M75) = 1/24</strong>.</p>'
            + '\n      <p><strong>P93 carries that exact obstruction into finite data.</strong> A simultaneous seven-cell confidence event yields the exact 95 percent mathematical crossing between 1622 and 1623 samples, while the first exact 24-count replication that clears is 1632.</p>',
            1,
        )
    text = text.replace(
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md">Read P91 theorem</a>',
        'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_93_localized_sign_coherence_rejection.md">Read P93 theorem</a>',
    )
    start.write_text(text, encoding="utf-8")
    _place_block_before("website/start-here.html", P93_READER_BLOCK, '<section class="boundary" id="p92-start-frontier">')

    plain = ROOT / "website/plain-language.html"
    text = plain.read_text(encoding="utf-8")
    replacements = (
        ("This is the 92-result Research II theorem program currently reaching P92.", "This is the 93-result Research II theorem program currently reaching P93."),
        ("A 92-result sufficiency and falsification architecture", "A 93-result sufficiency and falsification architecture"),
        ("The 92-result proposition program asks", "The 93-result proposition program asks"),
        ("The current theorem frontier is P92.", "The current theorem frontier is P93."),
        ("P92 is the current checkpoint, not the destination", "P93 is the current checkpoint, not the destination"),
        ("P92 is the current mathematical checkpoint", "P93 is the current mathematical checkpoint"),
        ("shows how all 92 Research II results connect", "shows how all 93 Research II results connect"),
        ("The destination is not Proposition 91, 100, or 200.", "The destination is not Proposition 93, 100, or 200."),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    plain.write_text(text, encoding="utf-8")
    _place_block_before("website/plain-language.html", P93_READER_BLOCK, '<section class="boundary" id="p92-reader-frontier">')

    research = ROOT / "website/research-map.html"
    text = research.read_text(encoding="utf-8")
    replacements = (
        ("Ninety-two results, one dependency-aware scientific program", "Ninety-three results, one dependency-aware scientific program"),
        ("Current Research II model-audit range: P75-P92.", "Current Research II model-audit range: P75-P93."),
        ("The current theorem frontier is P92.", "The current theorem frontier is P93."),
        ("<strong>92</strong><span>proposition-level results</span>", "<strong>93</strong><span>proposition-level results</span>"),
        ("<strong>P92</strong><span>current theorem frontier</span>", "<strong>P93</strong><span>current theorem frontier</span>"),
        ("P74-P92 continue", "P74-P93 continue"),
        ("<span>6 · P73-P92</span>", "<span>6 · P73-P93</span>"),
        ("P77-P92 move from", "P77-P93 move from"),
        ("<h2>P77-P92: from full-law rejection to nonlinear mixed-prevalence certification</h2>", "<h2>P77-P93: from full-law rejection to localized finite-sample nonlinear certification</h2>"),
        ('href="index.html#p92-frontier">Continue to the current P92 frontier</a>', 'href="index.html#p93-frontier">Continue to the current P93 frontier</a>'),
        ('href="visual-atlas.html#p92-frontier">See the P92 figure</a>', 'href="visual-atlas.html#p93-frontier">See the P93 figure</a>'),
        ('href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p92_equation_provenance.md">Audit P92 provenance</a>', 'href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p93_equation_provenance.md">Audit P93 provenance</a>'),
        ("Current Research II theorem frontier · P92", "Historical exact population checkpoint · P92"),
        ('href="index.html#p92-frontier">Current frontier</a>', 'href="visual-atlas.html#p92-frontier">Historical P92 figure</a>'),
        ("Research Map · Current theorem frontier P92", "Research Map · Current theorem frontier P93"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    text = text.replace(
        "and P92 closes the remaining mixed-prevalence distance bracket at the exact value 1/24.",
        "P92 closes the remaining mixed-prevalence distance bracket at the exact value 1/24, and P93 converts that nonlinear sign obstruction into a localized seven-cell finite-sample rejection certificate.",
    )
    text = text.replace(
        "culminating in P92 exact global mixed-prevalence distance.",
        "culminating in P92 exact global mixed-prevalence distance and the P93 finite-sample rejection handoff.",
    )
    research.write_text(text, encoding="utf-8")
    _place_block_before("website/research-map.html", P93_RESEARCH_MAP_BLOCK, '<section id="p92-research-map" class="theorem-frontier">')


def main() -> None:
    _replace("website/index.html", "Explore all 92 results", "Explore all 93 results")
    _replace("website/index.html", "P92 current theorem frontier · v0.82.0", "P93 current theorem frontier · v0.82.0")

    _replace("tests/test_figure_publication_sync.py", 'assert manifest["current_frontier"] == "P92"', 'assert manifest["current_frontier"] == "P93"')
    _replace_once("tests/test_figure_publication_sync.py", "    p93 = text.index('id=\"p93-frontier\"')\n    p93 = text.index('id=\"p93-frontier\"')\n", "    p93 = text.index('id=\"p93-frontier\"')\n    p92 = text.index('id=\"p92-frontier\"')\n")
    _replace_once("tests/test_figure_publication_sync.py", "    p93 = text.index('id=\"p93-frontier\"')\n    p93 = text.index('id=\"p93-frontier\"')\n    research_iii =", "    p93 = text.index('id=\"p93-frontier\"')\n    research_iii =")
    _replace("tests/test_reader_experience.py", "def test_no_reader_facing_html_page_advertises_pre_p92_as_current() -> None:", "def test_no_reader_facing_html_page_advertises_pre_p93_as_current() -> None:")
    _replace("tests/test_reader_experience.py", "overview.index('id=\"project-journey\"') < overview.index('id=\"p92-frontier\"')", "overview.index('id=\"project-journey\"') < overview.index('id=\"p93-frontier\"')")
    _replace("tests/test_publication_contract_v2.py", "for number in range(1, 93):", "for number in range(1, 94):")

    _rewrite_p93_reproducibility_section()
    _rewrite_citation_frontier()
    _replace("docs/detailed_proposition_record.md", "A first-time reader should not read this page as 91 disconnected proposition-level results.", "A first-time reader should not read this page as 93 disconnected proposition-level results.")
    _replace("scripts/synchronize_research_three_website.py", 'CURRENT_HOME_MARKER = "<!-- current-frontier-home: P92 -->"', 'CURRENT_HOME_MARKER = "<!-- current-frontier-home: P93 -->"')
    _repair_reader_html()

    print("[P93] publication contracts repaired")


if __name__ == "__main__":
    main()

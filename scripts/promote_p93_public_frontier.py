"""Promote canonical publication surfaces from P92 to P93.

This is a one-time, idempotent feature-branch migration helper. P93 converts
P92's nonlinear three-minor sign-coherence obstruction into a localized
finite-sample rejection theorem using a simultaneous seven-cell confidence
event and P79-certified exact sampling-radius comparisons.

Permanent publication workflows must remain read-only. After the P93 feature
branch has been synchronized and validated, this script is replaced by a
read-only audit helper before merge.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROOF = "proposition_93_localized_sign_coherence_rejection.md"
PROVENANCE = "p93_equation_provenance.md"
FIGURE = "p93_localized_sign_coherence_rejection.svg"
SOURCE = "localized_sign_coherence_rejection.py"
TEST = "test_localized_sign_coherence_rejection.py"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace(text: str, old: str, new: str) -> str:
    if old in text:
        return text.replace(old, new)
    return text


def replace_many(text: str, pairs: tuple[tuple[str, str], ...]) -> str:
    for old, new in pairs:
        text = replace(text, old, new)
    return text


def append_once(text: str, marker: str, block: str) -> str:
    if marker not in text:
        text = text.rstrip() + "\n\n" + block.strip() + "\n"
    return text


def promote_readme() -> None:
    path = "README.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The current public theorem frontier is **P92**.", "The current public theorem frontier is **P93**."),
            ("**[Read the current frontier](docs/proposition_92_exact_global_mixed_prevalence_distance.md)**", f"**[Read the current frontier](docs/{PROOF})**"),
            ("**Public theorem frontier:** P92", "**Public theorem frontier:** P93"),
        ),
    )
    block = f'''### Current theorem frontier

![P93 Localized Finite-Sample Sign-Coherence Rejection](docs/figures/{FIGURE})

**Figure 2. P93 localized finite-sample sign-coherence rejection.** P92 proves the exact nonlinear population obstruction. P93 turns that obstruction into a finite-data rejection rule using only the seven observable cells that enter the three P92 minors. For the established sign geometry, the exact determinant stability radii are `1/24`, `3/56`, and `5/72`. At 95 percent confidence, P79 exact-rational envelopes prove that the seven-cell sampling radius is still above `1/24` at `n = 1622` and below it at `n = 1623`. The first exact replication of the original 24-count profile that clears the certificate is `n = 1632 = 68 x 24`.

The generic P77 fixed-population-margin sufficient bound crosses at `n = 7444`, but that is a different guarantee. P93 is a localized observed-data certificate for the P92 sign witness. It is not claimed to be minimax optimal or universally sufficient.

P93 is a conditional finite-sample model-rejection theorem. Non-rejection remains inconclusive. It does not identify consciousness, establish nonphysicality, validate an alternative theory, or close the physical-to-experiential bridge.
'''
    text = re.sub(
        r"### Current theorem frontier\n.*?(?=\n## Choose your path)",
        block.rstrip(),
        text,
        count=1,
        flags=re.DOTALL,
    )
    write(path, text)


def promote_start_here() -> None:
    path = "START_HERE.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("The public theorem frontier is **P90**.", "The public theorem frontier is **P93**."),
            ("You do not need to read 90 propositions", "You do not need to read 93 propositions"),
            ("| Read the current frontier result | **[P88](docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md)** |", f"| Read the current frontier result | **[P93](docs/{PROOF})** |"),
            ("### P91 mixed-prevalence frontier", "### P91 historical mixed-prevalence step"),
            ("The current Research II frontier is [P91]", "The P91 Research II step is [P91]"),
            ("### P92 exact full-cube frontier", "### P92 historical exact full-cube step"),
            ("The current Research II frontier is [P92]", "The P92 Research II step is [P92]"),
        ),
    )
    text = append_once(
        text,
        "### P93 localized finite-sample frontier",
        f'''### P93 localized finite-sample frontier

The current Research II frontier is [P93](docs/{PROOF}). P93 takes P92's exact nonlinear sign-coherence obstruction into finite IID data. It needs simultaneous control of only seven observable cells. At 95 percent confidence, the exact mathematical radius crosses between 1622 and 1623 samples; the first exact replication of the original 24-count profile that clears the certificate is 1632 samples. Non-rejection remains inconclusive.''',
    )
    write(path, text)


def promote_citations() -> None:
    for path in ("CITATION.md", "CITATION.bib", "CITATION.cff"):
        text = read(path)
        text = replace_many(
            text,
            (
                ("current documented frontier, P92", "current documented frontier, P93"),
                ("Current documented theorem frontier: P92", "Current documented theorem frontier: P93"),
                ("## Current theorem frontier: P92", "## Current theorem frontier: P93"),
                ("theorem frontier **P92**", "theorem frontier **P93**"),
            ),
        )
        if path == "CITATION.md":
            text = append_once(
                text,
                "## Proposition 93 method citation",
                f'''## Proposition 93 method citation

For work using the localized finite-sample P92 sign-coherence rejection gate, cite the program together with **Proposition 93: Localized Finite-Sample Sign-Coherence Rejection** and its [equation provenance record](docs/{PROVENANCE}). P93 gives a seven-cell familywise rejection rule and an exact 95 percent radius crossing between sample sizes 1622 and 1623 for the established sign geometry. The first exact replication of the original 24-count profile that clears the certificate is 1632. The theorem does not claim universal or minimax sample complexity.''',
            )
        write(path, text)


def promote_documents() -> None:
    path = "docs/theorem_roadmap.md"
    text = read(path)
    text = replace_many(
        text,
        (
            ("current documented theorem frontier is **P92**", "current documented theorem frontier is **P93**"),
            ("from **P1 through P92", "from **P1 through P93"),
            ("P71-P91 return", "P71-P93 return"),
        ),
    )
    if "P93: the P92 sign-coherence witness yields" not in text:
        text = text.replace(
            "&\\text{P92: three-minor sign coherence closes the full mixed-prevalence P75 distance at 1/24}\\\\\n",
            "&\\text{P92: three-minor sign coherence closes the full mixed-prevalence P75 distance at 1/24}\\\\\n&\\Downarrow\\\\\n&\\text{P93: the P92 sign-coherence witness yields a localized seven-cell finite-sample rejection certificate}\\\\\n",
            1,
        )
    text = append_once(
        text,
        "## P93: localized finite-sample sign-coherence rejection",
        f'''## P93: localized finite-sample sign-coherence rejection

P93 converts the P92 nonlinear three-minor invariant into a finite-sample rejection theorem. The three P92 minors involve only seven distinct cell probabilities, so one seven-cell Hoeffding event is sufficient. If the empirical determinant product is negative and a P79-certified upper sampling radius is smaller than every empirical determinant sign-stability radius, the population determinant product is also negative and the complete P75 family is rejected at confidence at least `1-alpha`.

For the established sign geometry at 95 percent confidence, exact P79 envelopes certify the mathematical radius crossing between `n = 1622` and `n = 1623`. The first exact replication of the original 24-count profile that clears the certificate is `n = 1632 = 68 x 24`. The generic P77 fixed-margin sufficient condition at the P92 population margin crosses at 7444, but that is a different guarantee.

- [P93 proof]({PROOF})
- [P93 provenance]({PROVENANCE})
- Source: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE})
- Tests: [`{TEST}`](../tests/{TEST})

P93 does not claim universal or minimax sample complexity. Non-rejection remains inconclusive, and the physical-to-experiential bridge remains open.''',
    )
    write(path, text)

    path = "docs/detailed_proposition_record.md"
    text = read(path).replace("## Complete P1 to P92 chronology", "## Complete P1 to P93 chronology")
    text = append_once(
        text,
        "## Proposition 93: Localized Finite-Sample Sign-Coherence Rejection",
        f'''## Proposition 93: Localized Finite-Sample Sign-Coherence Rejection

P93 is the finite-data continuation of P92's nonlinear three-minor sign-coherence invariant. It uses only the seven observable cells entering those minors. A simultaneous seven-cell Hoeffding event plus the exact P92 determinant sign-stability radii and the P79 one-sided rational sampling-radius envelope gives a confidence-valid P75 rejection rule.

For the established sign geometry at `alpha = 0.05`, the mathematical radius crossing is 1622/1623. The first exact replication of the original 24-count profile that clears is `1632 = 68 x 24`. This is a localized observed-data certificate, not a universal sample-complexity theorem.

- [Proof]({PROOF})
- [Equation provenance]({PROVENANCE})
- Implementation: `src/consciousness_bridge/{SOURCE}`
- Tests: `tests/{TEST}`
- Figure: `docs/figures/{FIGURE}`''',
    )
    write(path, text)

    additions = {
        "docs/equation_and_citation_map.md": f'''## P93 localized finite-sample sign-coherence rejection

- Theorem: [Proposition 93]({PROOF})
- Equation provenance: [P93 equation record]({PROVENANCE})
- Implementation: [`{SOURCE}`](../src/consciousness_bridge/{SOURCE})
- Exact tests: [`{TEST}`](../tests/{TEST})
- Figure: [`{FIGURE}`](figures/{FIGURE})

P93 combines standard Hoeffding concentration and a seven-cell union bound with the repository's P92 determinant sign-stability theorem and P79 exact-rational sampling-radius envelope. The repository-original contribution is the localized finite-sample handoff for the P92 nonlinear invariant.''',
        "docs/claim_source_matrix.md": f'''| P93 localized finite-sample sign-coherence rejection | A negative empirical P92 determinant-sign product plus a certified seven-cell sampling radius below every empirical sign-stability radius rejects the P75 family at confidence at least `1-alpha`. | Repository-original conditional theorem built from standard concentration, P92 sign stability, and P79 exact numerical certification. | [{PROOF}]({PROOF}); [{PROVENANCE}]({PROVENANCE}); `../src/consciousness_bridge/{SOURCE}`; `../tests/{TEST}` | Do not report 1623 as a universal sample-size requirement or treat non-rejection as model acceptance. |''',
    }
    for path, block in additions.items():
        text = append_once(read(path), block.splitlines()[0], block)
        write(path, text)

    path = "docs/research_navigation.md"
    text = replace_many(
        read(path),
        (
            ("current documented theorem frontier is **P92**", "current documented theorem frontier is **P93**"),
            ("the full 92 proposition index", "the full 93 proposition index"),
            ("P71 through P92", "P71 through P93"),
            ("P71-P92", "P71-P93"),
        ),
    )
    text = append_once(
        text,
        "## P93 current frontier",
        f'''## P93 current frontier

| What you want | Direct link |
| --- | --- |
| The theorem and proof | [P93 proposition]({PROOF}) |
| Equation and method provenance | [P93 provenance]({PROVENANCE}) |
| Implementation | [`{SOURCE}`](../src/consciousness_bridge/{SOURCE}) |
| Exact tests | [`{TEST}`](../tests/{TEST}) |
| Figure | [P93 localized finite-sample certificate](figures/{FIGURE}) |

P93 uses seven observable cells from the P92 sign witness. The 1623 crossing is the exact mathematical confidence-radius threshold for the established sign geometry at 95 percent confidence; the first exact replication of the original profile that clears is 1632.''',
    )
    write(path, text)

    path = "docs/reproducibility.md"
    text = replace_many(
        read(path),
        (
            ("current public theorem frontier is **P92**", "current public theorem frontier is **P93**"),
            ("current P92 frontier", "current P93 frontier"),
            ("Current P92 frontier", "Current P93 frontier"),
        ),
    )
    text = append_once(
        text,
        "P93 focused audit",
        f'''### P93 focused audit

```bash
python -m pytest -q tests/{TEST}
python scripts/sync_figure_publication.py --check
python scripts/verify_repository.py
```

The P93 threshold audit uses P79 exact rational lower and upper sampling-radius envelopes and distinguishes the mathematical 1623 crossing from the first realizable exact 24-count replication at 1632.''',
    )
    write(path, text)

    path = "docs/glossary.md"
    text = replace(read(path), "current documented frontier P92", "current documented frontier P93")
    text = replace(text, "current theorem frontier, P92", "current theorem frontier, P93")
    write(path, text)

    path = "docs/research_map.md"
    text = replace_many(read(path), (("P71-P92", "P71-P93"), ("through P92", "through P93")))
    text = append_once(
        text,
        "### P93 localized finite-sample sign-coherence rejection",
        f'''### P93 localized finite-sample sign-coherence rejection

P93 asks whether finite IID data preserve P92's impossible determinant sign pattern strongly enough to reject the complete P75 family. It uses only seven selected cells and exact P79 sampling-radius certification. [Read P93]({PROOF}).''',
    )
    write(path, text)


def p93_home_section() -> str:
    return f'''<!-- current-frontier-home: P93 -->
<section id="p93-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head">
    <p class="eyebrow">Research II · Current theorem frontier · P93</p>
    <h2>Localized finite-sample sign-coherence rejection</h2>
    <p>P93 converts P92's nonlinear three-minor population obstruction into a confidence-valid finite-data rejection rule using only the seven observable cells that enter the witness.</p>
  </div>
  <div class="theorem-figure-shell"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/{FIGURE}"><img loading="eager" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}" alt="P93 localized finite-sample sign-coherence rejection certificate" /></a></div>
  <div class="frontier-summary-grid">
    <article class="frontier-summary-card"><h3>Seven-cell confidence event</h3><p>The three P92 minors involve only <strong>7</strong> observable cells, giving <strong>eps = sqrt(log(14/alpha)/(2n))</strong>.</p></article>
    <article class="frontier-summary-card"><h3>Exact 95 percent crossing</h3><p>P79 proves <strong>n = 1622</strong> is still above the limiting radius and <strong>n = 1623</strong> is below it.</p></article>
    <article class="frontier-summary-card"><h3>First exact profile replication</h3><p>The original 24-count proportions first clear the certificate at <strong>n = 1632 = 68 x 24</strong>.</p></article>
  </div>
  <div class="boundary"><p><strong>Scientific boundary:</strong> P93 is a localized observed-data rejection certificate, not a universal or minimax sample-complexity theorem. Non-rejection remains inconclusive. It does not identify consciousness or close the physical-to-experiential bridge.</p></div>
  <p><a href="research-map.html">Research II map</a> · <a href="visual-atlas.html">Theorem figures</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{SOURCE}">{SOURCE}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{TEST}">{TEST}</a></p>
</section>'''


def promote_website() -> None:
    path = "website/index.html"
    text = read(path)
    text = replace_many(
        text,
        (
            ("92 proposition-level results through P92", "93 proposition-level results through P93"),
            ("The 92 results form several dependency branches.", "The 93 results form several dependency branches."),
            ("The 92-result program", "The 93-result program"),
            ("all 92 propositions", "all 93 propositions"),
            ("current P92 frontier", "current P93 frontier"),
            ("Current P92 frontier", "Current P93 frontier"),
            ("sources.html#p92-source", "sources.html#p93-source"),
            ("P92 sources", "P93 sources"),
        ),
    )
    text = re.sub(
        r"<!-- current-frontier-home: P92 -->\s*<section id=\"p92-frontier\".*?</section>",
        p93_home_section(),
        text,
        count=1,
        flags=re.DOTALL,
    )
    write(path, text)

    path = "website/visual-atlas.html"
    text = read(path)
    if 'id="p93-frontier"' not in text:
        p93 = f'''<section id="p93-frontier" class="theorem-frontier current-frontier-visual">
  <div class="section-head"><p class="eyebrow">Current theorem frontier · P93</p><h2>Localized finite-sample sign-coherence rejection</h2><p>P93 uses a seven-cell confidence event to carry the P92 nonlinear sign witness into finite IID data. At 95 percent confidence, the exact radius crosses between 1622 and 1623 samples, and the first exact replication of the original 24-count profile that clears is 1632.</p></div>
  <div class="theorem-figure-shell"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/{FIGURE}" alt="P93 localized finite-sample sign-coherence rejection certificate" /></div>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a></p>
</section>

'''
        anchor = text.find('<section id="p92-frontier"')
        if anchor < 0:
            raise RuntimeError("visual atlas has no P92 frontier anchor")
        text = text[:anchor] + p93 + text[anchor:]
    text = text.replace("Current theorem frontier · P92", "Previous theorem frontier · P92")
    write(path, text)

    for path in ("website/start-here.html", "website/plain-language.html"):
        text = replace_many(
            read(path),
            (
                ("92 results · current frontier P92", "93 results · current frontier P93"),
                ("92 proposition-level results", "93 proposition-level results"),
                ("The 92 Research II propositions", "The 93 Research II propositions"),
                ("through P92", "through P93"),
                ("current P92 frontier", "current P93 frontier"),
                ("Current frontier · P92", "Historical population frontier · P92"),
            ),
        )
        marker = 'id="p93-reader-frontier"'
        if marker not in text:
            block = f'''<section class="boundary" id="p93-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current frontier · P93</p><h2>P92's exact population obstruction now has a localized finite-data rejection rule</h2><p>P93 controls only the seven observable cells entering the P92 sign witness. At 95 percent confidence, the mathematical radius crosses at 1623 samples; the first exact replication of the original profile that clears is 1632. Non-rejection remains inconclusive.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">Read P93</a></p></div></section>\n\n'''
            text = text.rstrip() + "\n\n" + block
        write(path, text)

    path = "website/research-map.html"
    text = replace_many(
        read(path),
        (("P71-P92", "P71-P93"), ("through P92", "through P93"), ("92 proposition-level", "93 proposition-level")),
    )
    if 'id="p93-research-map"' not in text:
        text = text.rstrip() + f'''\n\n<section id="p93-research-map" class="theorem-frontier">
  <div class="section-head"><p class="eyebrow">P93 · Localized finite-sample nonlinear rejection</p><h2>P93: Can finite IID data preserve the P92 sign obstruction strongly enough to reject P75?</h2></div>
  <p>Yes. The three P92 minors use only seven distinct observable cells. If their empirical determinant product is negative and the P79-certified seven-cell sampling radius is smaller than every empirical determinant sign-stability radius, the unknown population has the same impossible sign pattern and P75 is rejected at confidence at least 1-alpha.</p>
  <p><strong>Established profile at 95 percent confidence:</strong> mathematical radius crossing 1622/1623; first exact 24-count replication that clears, 1632.</p>
  <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · <a href="index.html#p93-frontier">Current frontier</a></p>
</section>\n'''
    write(path, text)

    path = "website/research-lineage.html"
    text = replace_many(
        read(path),
        (
            ("<strong>92</strong><span>proposition-level results</span>", "<strong>93</strong><span>proposition-level results</span>"),
            ("<strong>P92</strong><span>current theorem frontier</span>", "<strong>P93</strong><span>current theorem frontier</span>"),
            ("through P92", "through P93"),
        ),
    )
    write(path, text)

    path = "website/sources.html"
    text = append_once(
        read(path),
        'id="p93-source"',
        f'''<section id="p93-source" class="boundary"><div class="section-head"><p class="eyebrow">Current theorem source record · P93</p><h2>Localized finite-sample sign-coherence rejection</h2></div><p>Proof: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROOF}">{PROOF}</a> · provenance: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{PROVENANCE}">{PROVENANCE}</a> · implementation: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/{SOURCE}">{SOURCE}</a> · tests: <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/{TEST}">{TEST}</a>.</p><p>P93 combines standard finite-alphabet concentration with P92 determinant sign stability and P79 exact-rational radius certification. It is a conditional model-rejection theorem, not a consciousness identification result.</p></section>''',
    )
    write(path, text)

    path = "website/implementation.html"
    text = read(path).replace("Stage 06 · P73-P92", "Stage 06 · P73-P93")
    write(path, text)


def promote_scripts() -> None:
    path = "scripts/prepare_website.py"
    text = replace_many(
        read(path),
        (
            ("p92_exact_global_mixed_prevalence_distance.svg", FIGURE),
            ("Current record:</strong> 92 proposition-level results through P92", "Current record:</strong> 93 proposition-level results through P93"),
            ("<strong>92</strong><span>proposition-level results</span>", "<strong>93</strong><span>proposition-level results</span>"),
            ("<strong>P92</strong><span>current theorem frontier</span>", "<strong>P93</strong><span>current theorem frontier</span>"),
            ('id="p92-frontier"', 'id="p93-frontier"'),
        ),
    )
    write(path, text)

    path = "scripts/verify_repository.py"
    text = read(path)
    text = replace_many(
        text,
        (
            ('CURRENT_FRONTIER = "P92"', 'CURRENT_FRONTIER = "P93"'),
            ('"docs/figures/p92_exact_global_mixed_prevalence_distance.svg",\n    "docs/figures/p92_exact_global_mixed_prevalence_distance.svg",', '"docs/figures/p92_exact_global_mixed_prevalence_distance.svg",'),
            ('"docs/proposition_92_exact_global_mixed_prevalence_distance.md",\n    "docs/p92_equation_provenance.md",\n    "docs/proposition_92_exact_global_mixed_prevalence_distance.md",\n    "docs/p92_equation_provenance.md",', '"docs/proposition_92_exact_global_mixed_prevalence_distance.md",\n    "docs/p92_equation_provenance.md",'),
            ('"src/consciousness_bridge/exact_global_mixed_prevalence_distance.py",\n    "src/consciousness_bridge/exact_global_mixed_prevalence_distance.py",', '"src/consciousness_bridge/exact_global_mixed_prevalence_distance.py",'),
            ('"tests/test_exact_global_mixed_prevalence_distance.py",\n    "tests/test_exact_global_mixed_prevalence_distance.py",', '"tests/test_exact_global_mixed_prevalence_distance.py",'),
            ("Current documented theorem frontier: P92", "Current documented theorem frontier: P93"),
            ("does not declare P92", "does not declare P93"),
            ("range(1, 93)", "range(1, 94)"),
            ("p92_exact_global_mixed_prevalence_distance.svg", FIGURE),
            ("canonical P91 SVG", "canonical P93 SVG"),
            ("len(figures) != 150", "len(figures) != 151"),
            ("canonical 150 figures", "canonical 151 figures"),
            ("p92 = visual_atlas.index('id=\"p92-frontier\"')", "p93 = visual_atlas.index('id=\"p93-frontier\"')\n    p92 = visual_atlas.index('id=\"p92-frontier\"')"),
            ("if not (p92 < p91 < p90):", "if not (p93 < p92 < p91):"),
            ("Visual Atlas does not lead with the current P92 figure", "Visual Atlas does not lead with the current P93 figure"),
        ),
    )
    p92_core = '    "docs/p92_equation_provenance.md",\n'
    if f'    "docs/{PROOF}",\n' not in text:
        text = text.replace(
            p92_core,
            p92_core
            + f'    "docs/{PROOF}",\n'
            + f'    "docs/{PROVENANCE}",\n'
            + f'    "docs/figures/{FIGURE}",\n'
            + f'    "src/consciousness_bridge/{SOURCE}",\n'
            + f'    "tests/{TEST}",\n',
            1,
        )
    stale_anchor = 'STALE_READER_FRONTIER_MARKERS = (\n'
    if '"Current theorem frontier · P92",' not in text:
        text = text.replace(
            stale_anchor,
            stale_anchor
            + '    "Current theorem frontier · P92",\n'
            + '    "current P92 frontier",\n'
            + '    "<strong>P92</strong><span>current theorem frontier</span>",\n',
            1,
        )
    write(path, text)

    path = "scripts/sync_figure_publication.py"
    text = read(path)
    if "if frontier == 93:" not in text:
        marker = "    return []\n\n\ndef _frontier_page"
        block = '''    if frontier == 93:\n        return [\n            "### Exact P93 localized finite-sample sign-coherence rejection",\n            "",\n            "P93 carries the P92 nonlinear sign-coherence obstruction into finite IID data using only seven selected observable cells.",\n            "",\n            "```text",\n            "empirical determinant signs = (-,+,+)",\n            "sign-stability radii = (1/24, 3/56, 5/72)",\n            "95% mathematical crossing = 1622 / 1623",\n            "first exact 24-count replication that clears = 1632",\n            "generic P77 fixed-margin comparison = 7444",\n            "```",\n            "",\n            "The P77 comparison is a different guarantee. P93 is localized to the observed P92 sign witness, does not claim universal or minimax sample complexity, and does not identify consciousness.",\n            "",\n        ]\n'''
        text = text.replace(marker, block + marker, 1)
    write(path, text)


def promote_tests_and_workflow() -> None:
    path = "tests/test_figure_publication_sync.py"
    text = read(path)
    text = replace_many(
        text,
        (
            ("P92_FIGURE", "P93_FIGURE"),
            ("p92_exact_global_mixed_prevalence_distance.svg", FIGURE),
            ("tracks_p92", "tracks_p93"),
            ("P71-P92", "P71-P93"),
            ("Current theorem frontier: P92", "Current theorem frontier: P93"),
            ("leads_with_p92", "leads_with_p93"),
            ("p92 = text.index('id=\"p92-frontier\"')", "p93 = text.index('id=\"p93-frontier\"')\n    p92 = text.index('id=\"p92-frontier\"')"),
            ("assert p92 < p91 < p90 < p89", "assert p93 < p92 < p91 < p90"),
            ("current = text[p92:p91]", "current = text[p93:p92]"),
            ("Current theorem frontier · P92", "Current theorem frontier · P93"),
            ("proposition_92_exact_global_mixed_prevalence_distance.md", PROOF),
            ("previous = text[p91:p90]", "previous = text[p92:p91]"),
            ("Previous theorem frontier · P91", "Previous theorem frontier · P92"),
            ("p92 = text.index('id=\"p92-frontier\"')", "p93 = text.index('id=\"p93-frontier\"')"),
            ("research_i < p92 < research_iii", "research_i < p93 < research_iii"),
            ("current = text[p92:research_iii]", "current = text[p93:research_iii]"),
            ("exact_global_mixed_prevalence_distance.py", SOURCE),
            ("test_exact_global_mixed_prevalence_distance.py", TEST),
            ("text[research_i:p92]", "text[research_i:p93]"),
            ('\'id="p91-frontier"\',\n        \'id="p90-frontier"\'', '\'id="p92-frontier"\',\n        \'id="p91-frontier"\',\n        \'id="p90-frontier"\''),
            ("The 92 results form several dependency branches.", "The 93 results form several dependency branches."),
            ("all 92 propositions", "all 93 propositions"),
            ('assert "92" in source', 'assert "93" in source'),
            ('assert "P92" in source', 'assert "P93" in source'),
            ("exact_commit_p92", "exact_commit_p93"),
            ("deployed_p92", "deployed_p93"),
            ("p92 = home.index('id=\"p92-frontier\"')", "p93 = home.index('id=\"p93-frontier\"')"),
            ("research_i < p92 < research_iii", "research_i < p93 < research_iii"),
        ),
    )
    write(path, text)

    path = "tests/test_publication_contract_v2.py"
    text = read(path)
    text = text.replace("P92", "P93").replace("p92", "p93").replace("92", "93")
    text = text.replace("exact_global_mixed_prevalence_distance", "localized_sign_coherence_rejection")
    write(path, text)

    path = "tests/test_reader_experience.py"
    text = read(path)
    text = replace_many(
        text,
        (
            ("tracks_p92_and_all_92", "tracks_p93_and_all_93"),
            ('CURRENT_FRONTIER = "P92"', 'CURRENT_FRONTIER = "P93"'),
            ("range(1, 93)", "range(1, 94)"),
        ),
    )
    write(path, text)

    path = ".github/workflows/figures.yml"
    text = replace_many(
        read(path),
        (
            ("p92_exact_global_mixed_prevalence_distance.svg", FIGURE),
            ("p92=t.index", "p93=t.index"),
            ("p91=t.index", "p92=t.index"),
            ("p90=t.index", "p91=t.index"),
            ("assert p92 < p91 < p90", "assert p93 < p92 < p91"),
        ),
    )
    write(path, text)


def main() -> None:
    promote_readme()
    promote_start_here()
    promote_citations()
    promote_documents()
    promote_website()
    promote_scripts()
    promote_tests_and_workflow()
    print("[P93] publication surfaces promoted")


if __name__ == "__main__":
    main()

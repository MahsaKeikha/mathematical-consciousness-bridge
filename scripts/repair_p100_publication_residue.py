from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def main() -> None:
    # Figure catalog: exact count plus P100 row.
    path = "docs/figure_catalog.md"
    text = read(path)
    text = text.replace(
        "**Current catalog:** 157 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 82 proposition/theorem visuals, and 40 quantitative figures.",
        "**Current catalog:** 158 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 83 proposition/theorem visuals, and 40 quantitative figures.",
    )
    if "figures/p100_anytime_sequential_eprocess.svg" not in text:
        row = (
            "| [P100 anytime-valid sequential e-process](figures/p100_anytime_sequential_eprocess.svg) | "
            "What this figure shows: P100 composes fresh, conditionally valid P99 certification-round e-values with predictable reserve stakes into one sequential evidence process. "
            "How to read it: follow fresh rounds from left to right, compute F_t = (1 - eta_t) + eta_t E_t, and compare M_t with 1/alpha. "
            "Main takeaway: two individually non-decisive half-staked rounds with E_t = 25/2 give M_2 = 729/16 > 20. | "
            "Exact sequential-inference theorem figure. Its guarantee requires current-round choices to be predictable and current certification data to remain conditionally valid given the past; it does not establish consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge. | "
            "[Proposition 100](proposition_100_anytime_sequential_eprocess.md) |"
        )
        lines = text.splitlines()
        for index, line in enumerate(lines):
            if "figures/p99_cross_fitted_evalue_aggregation.svg" in line:
                lines.insert(index + 1, row)
                text = "\n".join(lines) + "\n"
                break
        else:
            raise RuntimeError("P99 figure row not found in catalog")
    write(path, text)

    # Homepage: count, historical P98 visibility, correct P100 source label.
    path = "website/index.html"
    text = read(path)
    text = text.replace("The 99 results form several dependency branches.", "The 100 results form several dependency branches.")
    text = text.replace(">P94 sources</a>", ">P100 sources</a>")
    if "P98 cross-fitted certification" not in text:
        anchor = '<p>The 100-result program is summarized here; <a href="research-map.html">all 100 propositions</a> remain in the Research Map.</p>'
        addition = (
            '<p>Historical selection-valid lineage: P96 introduced independent holdout certification, P97 added finite candidate-family protection, '
            'P98 cross-fitted certification rotated genuinely independent holdouts, P99 aggregated valid fold evidence with e-values, and P100 adds the outer anytime-valid sequential layer.</p>'
        )
        if anchor not in text:
            raise RuntimeError("homepage Research II anchor not found")
        text = text.replace(anchor, anchor + "\n          " + addition, 1)
    write(path, text)

    # Research lineage: exact current count and current P100 summary.
    path = "website/research-lineage.html"
    text = read(path)
    text = text.replace(
        '<div><strong>99</strong><span>proposition-level results</span></div>',
        '<div><strong>100</strong><span>proposition-level results</span></div>',
    )
    text = text.replace("Current Research II frontier · P99", "Current Research II frontier · P100")
    text = text.replace("From selection-valid cross-fitting to distributed evidence", "From selection-valid evidence to anytime-valid sequential accumulation")
    text = text.replace(
        "P98 made rotated independent-block certification simultaneous. P99 adds an evidence layer: valid fold rejections become e-values, finite frozen calibrations are mixed exactly, and dependent cross-fitted fold evidence is averaged without assuming fold independence. The physical-to-experiential bridge remains open.",
        "P98 established rotated independent-block certification, P99 converted valid cross-fitted evidence into exact e-values, and P100 adds a fresh-round sequential layer with predictable reserve stakes. Under the declared conditional-validity contract, the cumulative process is a nonnegative supermartingale and the first crossing of 1 / alpha is anytime-valid. The physical-to-experiential bridge remains open.",
    )
    write(path, text)

    # Detailed proposition chronology.
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("Complete P1 to P99 chronology", "Complete P1 to P100 chronology")
    text = text.replace("99 disconnected proposition-level results", "100 disconnected proposition-level results")
    write(path, text)

    # Current P100 source anchor.
    path = "website/sources.html"
    text = read(path)
    if 'id="p100-source"' not in text:
        section = '''
<section id="p100-source" class="boundary"><div class="section-head"><p class="eyebrow">Current Research II theorem source · P100</p><h2>Anytime-valid sequential e-process</h2><p>P100 composes fresh, conditionally valid P99 certification rounds with predictable exact-rational reserve stakes into a nonnegative supermartingale. Ville's inequality protects repeated inspection and stopping at the first crossing of 1 / alpha.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_100_anytime_sequential_eprocess.md"><h3>Proposition 100</h3><p>Formal theorem, conditional-validity contract, exact checkpoint, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p100_equation_provenance.md"><h3>P100 provenance</h3><p>Separates standard supermartingale, e-process, and Ville machinery from the repository-specific P99-to-P100 integration.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/anytime_sequential_eprocess.py"><h3>P100 implementation</h3><p>Exact-rational sequential factors, cumulative evidence, crossing logic, freshness guards, and sample accounting.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_anytime_sequential_eprocess.py"><h3>P100 tests</h3><p>Regression coverage for 25/2, 27/4, 729/16, reserve behavior, predictability, freshness, and invalid stakes.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p100_anytime_sequential_eprocess.svg"><h3>P100 theorem figure</h3><p>Canonical visual of the anytime-valid two-round checkpoint and its scientific boundary.</p></a></div><div class="boundary"><p><strong>Scientific boundary:</strong> current-round plans, calibrations, and stakes must be frozen from past information, and current certification data must retain conditional P99 validity given that past. P100 does not make reused data fresh, establish model acceptance, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div></section>
'''
        if "</main>" not in text:
            raise RuntimeError("sources closing main not found")
        text = text.replace("</main>", section + "</main>", 1)
    write(path, text)

    # Citation and changelog markers.
    path = "CITATION.bib"
    write(path, read(path).replace("Current documented theorem frontier: P99.", "Current documented theorem frontier: P100."))

    path = "CHANGELOG.md"
    text = read(path)
    text = text.replace(
        "# Unreleased research frontier - P99\n\n## Unreleased research frontier - P100\n",
        "# Unreleased research frontier - P100\n\n## P100 anytime-valid sequential e-process frontier\n",
        1,
    )
    write(path, text)

    # Implementation page: current P100, historical P99, correct routes.
    path = "website/implementation.html"
    text = read(path)
    text = text.replace("<strong>P1-P95 proposition record</strong>", "<strong>P1-P100 proposition record</strong>")
    text = text.replace("<strong>6 · P73-P99</strong>", "<strong>6 · P73-P100</strong>")
    text = text.replace('index.html#p99-frontier">current P100 frontier', 'index.html#p100-frontier">current P100 frontier')
    text = text.replace(
        "P100 compounds fresh P99 round evidence through predictable reserve stakes into an anytime-valid sequential e-process and fixed convex averaging.",
        "P100 compounds fresh P99 round evidence through predictable reserve stakes into an anytime-valid sequential e-process.",
    )
    p99_current = '<section><div class="section-head"><p class="eyebrow">Current Research II implementation · P99</p><h2>P99 cross-fitted e-value aggregation</h2></div><p>The executable P99 layer uses exact rational fold levels, threshold-mixture weights, regime alpha weights, and fold weights. It delegates each threshold test to the selection-valid P96/P95/P94 chain and compares the final aggregate e-value with `1/alpha` exactly.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/cross_fitted_evalue_aggregation.py">Open P99 implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_cross_fitted_evalue_aggregation.py">Open P99 tests</a></p></section>'
    if "Current Research II implementation · P100" not in text and p99_current in text:
        p100 = '<section><div class="section-head"><p class="eyebrow">Current Research II implementation · P100</p><h2>P100 anytime-valid sequential e-process</h2></div><p>The executable P100 layer nests the P99 certificate inside fresh sequential rounds, applies predictable exact-rational reserve stakes, accumulates the product process exactly, and records the first anytime-valid threshold crossing. Current-round predictability and conditional freshness are explicit guards.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/anytime_sequential_eprocess.py">Open P100 implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_anytime_sequential_eprocess.py">Open P100 tests</a></p></section>\n<section><div class="section-head"><p class="eyebrow">Previous Research II implementation · P99</p><h2>P99 cross-fitted e-value aggregation</h2></div><p>The executable P99 layer uses exact rational fold levels, threshold-mixture weights, regime alpha weights, and fold weights. It delegates each threshold test to the selection-valid P96/P95/P94 chain and compares the final aggregate e-value with `1/alpha` exactly.</p><p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/cross_fitted_evalue_aggregation.py">Open P99 implementation</a> · <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_cross_fitted_evalue_aggregation.py">Open P99 tests</a></p></section>'
        text = text.replace(p99_current, p100, 1)
    write(path, text)

    # Research map current-state orientation.
    path = "website/research-map.html"
    text = read(path)
    text = text.replace("P71-P98 return to the P19 bridge-sufficiency lineage", "P71-P100 return to the P19 bridge-sufficiency lineage")
    text = text.replace(
        "Mathematical Consciousness Bridge · Research Map · Current theorem frontier P99</p>",
        "Mathematical Consciousness Bridge · Research Map · Current theorem frontier P100</p>",
    )
    if "through Proposition 100." not in text:
        anchor = '<p><strong>Current Research II model-audit range: P75-P100.</strong> The current theorem frontier is P100. The physical-to-experiential bridge remains open.</p>'
        if anchor not in text:
            raise RuntimeError("research-map current range anchor not found")
        text = text.replace(anchor, anchor + '\n  <p>This map tracks the formal program through Proposition 100.</p>', 1)
    write(path, text)

    # Preserve P98 historical auditability on protected reader surfaces.
    for path in (
        "README.md",
        "website/index.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = read(path)
        if "p98" in text.lower():
            continue
        sentence = "P98 established cross-fitted selection-valid certification across genuinely independent certification blocks with own-fold exclusion. P99 and P100 build on that inference boundary rather than replacing it."
        if path.endswith(".md"):
            text = text.rstrip() + "\n\n### Historical P98 checkpoint\n\n" + sentence + "\n"
        elif "</main>" in text:
            text = text.replace(
                "</main>",
                '<section class="boundary"><p><strong>Historical P98 checkpoint:</strong> ' + sentence + "</p></section>\n</main>",
                1,
            )
        else:
            raise RuntimeError(f"cannot add P98 note to {path}")
        write(path, text)

    print("P100 publication residue repaired")


if __name__ == "__main__":
    main()

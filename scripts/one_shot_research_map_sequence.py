from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website" / "research-map.html"
ORIENTATION_TEST = ROOT / "tests" / "test_website_research_orientation.py"
SEQUENCE_TEST = ROOT / "tests" / "test_research_map_p77_p100_sequence.py"

BEGIN = "<!-- BEGIN CONTINUOUS MODEL FRONTIER -->"
END = "<!-- END CONTINUOUS MODEL FRONTIER -->"

CARDS = [
    (
        77,
        "Full-law model-set rejection",
        "Reject only when the simultaneous empirical-law confidence region is certified disjoint from the complete declared model family.",
        "proposition_77_full_law_model_set_separation.md",
    ),
    (
        78,
        "Certified continuous distance",
        "Use exact-rational multi-affine parameter-box enclosures to produce global lower bounds on full-law L-infinity distance.",
        "proposition_78_certified_continuous_model_separation.md",
    ),
    (
        79,
        "Certified sampling radius",
        "Bound the finite-sample radius with one-sided exact arithmetic so the P77 rejection comparison has a safe numerical direction.",
        "proposition_79_certified_sampling_radius.md",
    ),
    (
        80,
        "Simplex-coupled separation",
        "Intersect exact cell intervals with probability normalization to obtain a never-weaker continuous-family relaxation.",
        "proposition_80_simplex_coupled_model_separation.md",
    ),
    (
        81,
        "Projected-event constraints",
        "Add exact ranges for projected cylinder events and transfer event mismatch back to full-law distance.",
        "proposition_81_projection_event_model_separation.md",
    ),
    (
        82,
        "Nested residual constraints",
        "Preserve common-parameter structure in residual events that separate projection intervals can lose.",
        "proposition_82_exact_nested_projection_contrast.md",
    ),
    (
        83,
        "Projection-parity constraints",
        "Add exact two-, three-, and four-view parity observables that expose dependence structure missed by the previous event family.",
        "proposition_83_exact_projection_parity.md",
    ),
    (
        84,
        "Joint parity compatibility",
        "Require parity observables to be compatible under one shared P75 parameter assignment rather than merely compatible separately.",
        "proposition_84_exact_projection_parity_contrast.md",
    ),
    (
        85,
        "Three-event parity functionals",
        "Move beyond the complete pairwise certificate by testing exact shared-parameter functionals across three distinct parity observables.",
        "proposition_85_exact_triple_projection_parity_functional.md",
    ),
    (
        86,
        "Minimally weighted four-event functionals",
        "Add the first non-uniform primitive four-event coefficient family and obtain the strict exact witness L86 = 1/192.",
        "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md",
    ),
    (
        87,
        "Complete bounded primitive radius two",
        "Exhaust every nonzero primitive four-event coefficient vector with coefficient magnitude at most two and reach L87 = 1/96.",
        "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",
    ),
    (
        88,
        "Complete bounded primitive radius three",
        "Extend the exact four-event primitive coefficient box to magnitude three and improve the established rational witness bound to L88 = 1/64.",
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
    ),
    (
        89,
        "Complete real linear parity duality",
        "Remove finite support and coefficient-radius restrictions and close every real linear direction on the eleven canonical parity coordinates at 5/168.",
        "proposition_89_complete_linear_parity_duality.md",
    ),
    (
        90,
        "Exact nonlinear single-component separation",
        "Move beyond the complete linear envelope. On the prevalence-zero P75 face, the rank-one identity ad = bc gives exact full-law L-infinity distance 5/72.",
        "proposition_90_exact_nonlinear_rank_one_separation.md",
    ),
    (
        91,
        "Mixed-prevalence rank-two separation",
        "Remove the extreme-prevalence restriction. The declared bipartite flattening gives the certified global bracket 1/42 < d_inf(P_emp, M75) <= 1/24.",
        "proposition_91_mixed_prevalence_rank_two_flattening_separation.md",
    ),
    (
        92,
        "Exact global mixed-prevalence distance",
        "Close the P91 bracket with determinant sign stability and matching exact certificates: d_inf(P_emp, M75) = 1/24.",
        "proposition_92_exact_global_mixed_prevalence_distance.md",
    ),
    (
        93,
        "Localized IID finite-sample rejection",
        "Use only the seven observable cells needed by the P92 sign obstruction and reject P75 when certified sampling uncertainty preserves the impossible sign pattern.",
        "proposition_93_localized_sign_coherence_rejection.md",
    ),
    (
        94,
        "Finite-range dependent rejection",
        "Extend the localized sign-coherence gate to declared m-dependence under one common marginal law with squared radius (m+1) log(14/alpha)/(2n).",
        "proposition_94_finite_range_dependent_sign_coherence.md",
    ),
    (
        95,
        "Drift-aware stratified rejection",
        "Test predeclared regimes separately, assign exact local error budgets, and combine the regime certificates with familywise error control instead of invalid pooling.",
        "proposition_95_drift_aware_stratified_sign_coherence.md",
    ),
    (
        96,
        "Selection-valid holdout stratification",
        "Allow pilot data to choose a finite regime plan, then freeze that plan before certification on genuinely independent holdout information.",
        "proposition_96_selection_valid_holdout_stratification.md",
    ),
    (
        97,
        "Simultaneous finite-family selection",
        "Protect same-data selection over a finite candidate family fixed before inspection by making every candidate certificate simultaneous under preallocated error budgets.",
        "proposition_97_simultaneous_candidate_family_selection.md",
    ),
    (
        98,
        "Cross-fitted selection-valid certification",
        "Rotate frozen plan selection across mutually independent blocks while excluding each fold from the rule used to certify that same fold.",
        "proposition_98_cross_fitted_selection_valid_certification.md",
    ),
    (
        99,
        "Cross-fitted e-value aggregation",
        "Turn valid fold rejections into e-values, freeze finite threshold mixtures before own-fold evaluation, and combine folds by a fixed convex average without requiring fold independence.",
        "proposition_99_cross_fitted_evalue_aggregation.md",
    ),
    (
        100,
        "Anytime-valid sequential e-process",
        "Accumulate fresh P99 round e-values with predictable reserve stakes. The resulting product is a nonnegative supermartingale, so Ville control permits repeated inspection and stopping.",
        "proposition_100_anytime_sequential_eprocess.md",
    ),
]

GROUPS = (
    (77, 85, "Certified model-set separation", "From full-law exclusion to shared-parameter parity diagnostics."),
    (86, 92, "Exact parity and nonlinear population separation", "From finite parity families to linear closure and exact nonlinear model-image distance."),
    (93, 100, "Finite-data, selection-valid, distributed, and anytime-valid inference", "From localized finite-sample rejection to fresh-round sequential evidence accumulation."),
)


def card(number: int, title: str, summary: str, proof: str) -> str:
    status = "P100 - Current theorem frontier" if number == 100 else f"P{number}"
    return f'''    <article class="result frontier-sequence-card" id="p{number}-research-map" data-proposition="P{number}">
      <span>{status}</span>
      <h3>{title}</h3>
      <p>{summary}</p>
      <p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/{proof}">Open P{number} theorem</a></p>
    </article>'''


def build_sequence() -> str:
    by_number = {number: (title, summary, proof) for number, title, summary, proof in CARDS}
    parts = [
        BEGIN,
        '<section id="continuous-model-frontier">',
        '  <div class="section-head">',
        '    <p class="eyebrow">Continuous model-audit lineage</p>',
        '    <h2>P77-P100: one ordered path from model-set rejection to anytime-valid sequential certification</h2>',
        '    <p>Read this branch from left to right and top to bottom. Every proposition appears once, in numeric order, with the same visual card structure and a direct link to its canonical theorem record. P77-P99 are auditable predecessor steps; P100 is the current theorem frontier.</p>',
        '  </div>',
        '  <nav class="proposition-nav-index" aria-label="Continuous model-audit sequence">',
        '    <a href="#frontier-p77-p85">P77-P85</a>',
        '    <a href="#frontier-p86-p92">P86-P92</a>',
        '    <a href="#frontier-p93-p100">P93-P100</a>',
        '    <a href="#p100-research-map">Current P100</a>',
        '  </nav>',
    ]
    for start, end, heading, description in GROUPS:
        parts.extend(
            [
                f'  <div class="frontier-sequence-band" id="frontier-p{start}-p{end}">',
                '    <div class="proposition-nav-group-head">',
                f'      <span>P{start}-P{end}</span>',
                f'      <h3>{heading}</h3>',
                f'      <p>{description}</p>',
                '    </div>',
                '    <div class="result-grid frontier-sequence-grid">',
            ]
        )
        for number in range(start, end + 1):
            title, summary, proof = by_number[number]
            parts.append(card(number, title, summary, proof))
        parts.extend(['    </div>', '  </div>'])
    parts.extend(
        [
            '  <div class="hero-actions">',
            '    <a class="button primary" href="#p100-research-map">Jump to P100</a>',
            '    <a class="button" href="visual-atlas.html#p100-frontier">See the P100 figure</a>',
            '    <a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p100_equation_provenance.md">Audit P100 provenance</a>',
            '  </div>',
            '</section>',
            END,
        ]
    )
    return "\n".join(parts)


def extract_section(text: str, pattern: str, label: str) -> str:
    match = re.search(pattern, text, flags=re.DOTALL)
    if not match:
        raise RuntimeError(f"could not locate {label}")
    return match.group(0)


def update_map() -> None:
    text = MAP.read_text(encoding="utf-8")
    start = text.find('<section id="continuous-model-frontier">')
    end = text.find("</main>", start)
    if start < 0 or end < 0:
        raise RuntimeError("could not locate continuous model frontier or main close")

    boundary = extract_section(
        text,
        r'<section class="boundary" id="scientific-boundary">.*?</section>',
        "scientific boundary",
    )
    audit = extract_section(
        text,
        r'<section id="audit-paths">.*?</section>',
        "audit paths",
    )

    replacement = build_sequence() + "\n\n" + boundary + "\n\n" + audit + "\n\n"
    text = text[:start] + replacement + text[end:]

    numbers = [
        int(value)
        for value in re.findall(r'id="p(\d+)-research-map"', build_sequence())
    ]
    if numbers != list(range(77, 101)):
        raise RuntimeError(f"generated frontier sequence is not P77-P100: {numbers}")
    if text.count('id="historical-frontiers"'):
        raise RuntimeError("legacy historical-frontiers block survived normalization")
    if 'id="p87-reader-frontier"' in text:
        raise RuntimeError("legacy isolated P87 frontier box survived normalization")
    for number in range(77, 101):
        if text.count(f'id="p{number}-research-map"') != 1:
            raise RuntimeError(f"P{number} research-map id is not unique")
    if "\u2013" in replacement or "\u2014" in replacement:
        raise RuntimeError("generated reader-facing sequence violates dash policy")

    MAP.write_text(text, encoding="utf-8")


def update_orientation_test() -> None:
    text = ORIENTATION_TEST.read_text(encoding="utf-8")
    pattern = re.compile(
        r"def test_current_and_previous_nonlinear_frontiers_are_structurally_inside_main\(\):.*?(?=\n\ndef test_continuous_frontier_keeps_lineage_and_current_provenance_auditable)",
        flags=re.DOTALL,
    )
    replacement = '''def test_continuous_model_frontier_is_strictly_ordered_inside_main():
    text = MAP.read_text(encoding="utf-8")
    main_open = text.index("<main>")
    main_close = text.index("</main>")
    positions = [text.index(f'id="p{number}-research-map"') for number in range(77, 101)]

    assert positions == sorted(positions)
    assert main_open < positions[0] < positions[-1] < main_close
    for number in range(77, 101):
        assert text.count(f'id="p{number}-research-map"') == 1

    assert 'id="historical-frontiers"' not in text
    assert 'id="p87-reader-frontier"' not in text
    assert "Historical P90 checkpoint" not in text
    assert "P100 - Current theorem frontier" in text[positions[-1]:main_close]
'''
    text, count = pattern.subn(replacement.rstrip(), text, count=1)
    if count != 1:
        raise RuntimeError("could not update obsolete frontier-order orientation test")

    pattern = re.compile(
        r"def test_continuous_frontier_keeps_lineage_and_current_provenance_auditable\(\):.*$",
        flags=re.DOTALL,
    )
    replacement = '''def test_continuous_frontier_keeps_lineage_and_current_provenance_auditable():
    text = MAP.read_text(encoding="utf-8")
    begin = text.index("<!-- BEGIN CONTINUOUS MODEL FRONTIER -->")
    end = text.index("<!-- END CONTINUOUS MODEL FRONTIER -->")
    frontier_text = text[begin:end]

    for number in range(77, 101):
        assert f'id="p{number}-research-map"' in frontier_text
        assert _proof_name(number) in frontier_text

    assert frontier_text.index('id="p90-research-map"') < frontier_text.index('id="p91-research-map"')
    assert frontier_text.index('id="p99-research-map"') < frontier_text.index('id="p100-research-map"')
    assert "P100 - Current theorem frontier" in frontier_text
    assert "p100_equation_provenance.md" in text
'''
    text, count = pattern.subn(replacement.rstrip() + "\n", text, count=1)
    if count != 1:
        raise RuntimeError("could not strengthen continuous-frontier orientation test")
    ORIENTATION_TEST.write_text(text, encoding="utf-8")


def write_sequence_test() -> None:
    SEQUENCE_TEST.write_text(
        '''import re\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nMAP = ROOT / "website" / "research-map.html"\n\n\ndef _sequence() -> str:\n    text = MAP.read_text(encoding="utf-8")\n    return text.split("<!-- BEGIN CONTINUOUS MODEL FRONTIER -->", 1)[1].split(\n        "<!-- END CONTINUOUS MODEL FRONTIER -->", 1\n    )[0]\n\n\ndef test_research_map_has_one_uniform_p77_p100_card_sequence():\n    block = _sequence()\n    numbers = [\n        int(value)\n        for value in re.findall(\n            r'<article class="result frontier-sequence-card" id="p(\\d+)-research-map"',\n            block,\n        )\n    ]\n    assert numbers == list(range(77, 101))\n\n\ndef test_every_frontier_card_links_to_its_canonical_theorem():\n    block = _sequence()\n    for number in range(77, 101):\n        proofs = list((ROOT / "docs").glob(f"proposition_{number}_*.md"))\n        assert len(proofs) == 1\n        assert proofs[0].name in block\n        assert f'data-proposition="P{number}"' in block\n\n\ndef test_scattered_legacy_frontier_blocks_are_gone():\n    text = MAP.read_text(encoding="utf-8")\n    assert 'id="historical-frontiers"' not in text\n    assert 'id="p87-reader-frontier"' not in text\n    for number in range(77, 101):\n        assert text.count(f'id="p{number}-research-map"') == 1\n\n\ndef test_sequence_precedes_boundary_and_audit_paths():\n    text = MAP.read_text(encoding="utf-8")\n    end = text.index("<!-- END CONTINUOUS MODEL FRONTIER -->")\n    boundary = text.index('id="scientific-boundary"')\n    audit = text.index('id="audit-paths"')\n    assert end < boundary < audit\n    assert "P100 - Current theorem frontier" in _sequence()\n\n\ndef test_sequence_reader_text_respects_dash_policy():\n    block = _sequence()\n    assert "\\u2013" not in block\n    assert "\\u2014" not in block\n''',
        encoding="utf-8",
    )


def main() -> None:
    update_map()
    update_orientation_test()
    write_sequence_test()


if __name__ == "__main__":
    main()

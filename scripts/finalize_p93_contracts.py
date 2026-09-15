"""Finalize residual P93 publication contracts on the feature branch.

This is a one-run branch helper. It repairs stale P92 reader/build/test contracts
without changing the P93 theorem mathematics. Delete it before merge.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace(path: str, old: str, new: str) -> None:
    text = read(path)
    if old in text:
        write(path, text.replace(old, new))
    elif new not in text:
        raise RuntimeError(f"{path}: expected contract not found: {old!r}")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    if old in text:
        write(path, text.replace(old, new, 1))
    elif new not in text:
        raise RuntimeError(f"{path}: expected one-run contract not found: {old!r}")


def append_once(path: str, marker: str, block: str) -> None:
    text = read(path)
    if marker not in text:
        write(path, text.rstrip() + "\n\n" + block.strip() + "\n")


def insert_before_once(path: str, marker: str, block: str, *, sentinel: str) -> None:
    text = read(path)
    if sentinel in text:
        return
    if marker not in text:
        raise RuntimeError(f"{path}: insertion marker not found: {marker!r}")
    write(path, text.replace(marker, block.rstrip() + "\n\n" + marker, 1))


def collapse_repeated_line(path: str, line: str) -> None:
    text = read(path)
    doubled = line + line
    while doubled in text:
        text = text.replace(doubled, line)
    write(path, text)


def rewrite_function(path: str, name: str, next_name: str, replacement: str) -> None:
    text = read(path)
    pattern = re.compile(
        rf"def {re.escape(name)}\(.*?(?=\ndef {re.escape(next_name)}\()",
        flags=re.DOTALL,
    )
    if pattern.search(text):
        text = pattern.sub(replacement.rstrip() + "\n\n", text, count=1)
        write(path, text)
    elif f"def {replacement.split('def ', 1)[1].split('(', 1)[0]}(" not in text:
        raise RuntimeError(f"{path}: could not rewrite {name}")


def main() -> None:
    # Canonical generated frontier summary: preserve P92 population geometry
    # while making the P93 finite-sample handoff explicit.
    replace_once(
        "scripts/sync_figure_publication.py",
        '            "empirical determinant signs = (-,+,+)",\n',
        '            "empirical determinants = (-1/48, 1/64, 5/192)",\n'
        '            "empirical determinant signs = (-,+,+)",\n'
        '            "d_inf(P_emp, M_75) = 1/24",\n',
    )

    # Current public figure and homepage blocks must state the limiting radius.
    replace(
        "website/visual-atlas.html",
        "<!-- current-frontier-visual: P92 -->",
        "<!-- current-frontier-visual: P93 -->",
    )
    replace_once(
        "website/visual-atlas.html",
        "P93 uses a seven-cell confidence event to carry the P92 nonlinear sign witness into finite IID data. At 95 percent confidence,",
        "P93 uses a seven-cell confidence event to carry the P92 nonlinear sign witness into finite IID data. The limiting exact sign-stability radius is <strong>1/24</strong>. At 95 percent confidence,",
    )
    replace_once(
        "website/index.html",
        "<span class=\"research-program-metric\"><strong>92</strong><span>proposition-level results</span></span>",
        "<span class=\"research-program-metric\"><strong>93</strong><span>proposition-level results</span></span>",
    )
    replace(
        "website/index.html",
        "<span class=\"research-program-metric\"><strong>34</strong><span>tests in each CI job</span></span>",
        "<span class=\"research-program-metric\"><strong>35</strong><span>tests in each CI job</span></span>",
    )
    replace_once(
        "website/index.html",
        "P93 converts P92's nonlinear three-minor population obstruction into a confidence-valid finite-data rejection rule using only the seven observable cells that enter the witness.</p>",
        "P93 converts P92's nonlinear three-minor population obstruction into a confidence-valid finite-data rejection rule using only the seven observable cells that enter the witness. The limiting exact determinant sign-stability radius is <strong>1/24</strong>.</p>",
    )

    # Exact theorem interpretation language used by the public contract.
    replace_once(
        "docs/proposition_93_localized_sign_coherence_rejection.md",
        "P93 also does not claim minimax optimality, model acceptance under non-rejection, semantic validity of the latent state, nonphysicality of consciousness, or a completed physical-to-experiential bridge.\n\nThe physical-to-experiential bridge remains open.",
        "P93 also does not claim minimax optimality, model acceptance under non-rejection, semantic validity of the latent state, nonphysicality of consciousness, or a completed physical-to-experiential bridge.\n\nNon-rejection remains inconclusive. The physical-to-experiential bridge remains open.",
    )

    # Reader-facing current-frontier metadata.
    append_once(
        "docs/glossary.md",
        "## Current theorem frontier: P93",
        """## Current theorem frontier: P93

The current documented Research II theorem frontier is **P93**. P92 remains the exact population-distance theorem at `d_inf(P_emp, M75) = 1/24`; P93 adds the localized seven-cell finite-sample rejection handoff. This frontier status does not identify consciousness or close the physical-to-experiential bridge.""",
    )

    p93_source = """<section id=\"p93-source\"><div class=\"section-head\"><p class=\"eyebrow\">Current theorem source · P93</p><h2>Localized finite-sample sign-coherence rejection</h2><p>P93 carries P92's exact nonlinear population obstruction into finite IID data using only the seven observable cells entering the three-minor witness. The limiting sign-stability radius is <strong>1/24</strong>; at 95 percent confidence the exact mathematical crossing is 1622/1623 and the first exact 24-count replication that clears is 1632.</p></div><div class=\"source-grid\"><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_93_localized_sign_coherence_rejection.md\"><h3>Proposition 93</h3><p>Formal finite-sample rejection theorem and scientific boundary.</p></a><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p93_equation_provenance.md\"><h3>P93 provenance</h3><p>Separates standard concentration and inherited P92/P79 machinery from the repository-original localized handoff.</p></a><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/localized_sign_coherence_rejection.py\"><h3>P93 implementation</h3><p>Exact rational determinant geometry and certified sampling-radius comparison.</p></a><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_localized_sign_coherence_rejection.py\"><h3>P93 exact tests</h3><p>Seven-cell radius, 1622/1623 crossing, 1608/1632 replication, and boundary regressions.</p></a><a href=\"https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p93_localized_sign_coherence_rejection.svg\"><h3>P93 theorem figure</h3><p>Source-controlled visual summary synchronized with the 151-figure canonical manifest.</p></a></div><div class=\"boundary\"><p><strong>Scientific boundary:</strong> P93 is a localized conditional rejection certificate. Non-rejection remains inconclusive. It does not claim universal or minimax sample complexity, identify consciousness, or close the physical-to-experiential bridge.</p></div></section>"""
    insert_before_once(
        "website/sources.html",
        '<section id="p90-source">',
        p93_source,
        sentinel='id="p93-source"',
    )

    # Implementation/navigation advances to P93 while retaining P92 as history.
    replace("website/implementation.html", "P73-P92", "P73-P93")
    replace("website/implementation.html", "index.html#p92-frontier", "index.html#p93-frontier")

    # Research map current/historical labels and direct current audit paths.
    replacements = (
        ("Ninety-two results, one dependency-aware scientific program", "Ninety-three results, one dependency-aware scientific program"),
        ("Current Research II model-audit range: P75-P92.", "Current Research II model-audit range: P75-P93."),
        ("The current theorem frontier is P92.", "The current theorem frontier is P93."),
        ("<strong>92</strong><span>proposition-level results</span>", "<strong>93</strong><span>proposition-level results</span>"),
        ("<strong>P92</strong><span>current theorem frontier</span>", "<strong>P93</strong><span>current theorem frontier</span>"),
        ("P73-P92", "P73-P93"),
        ("P77-P92", "P77-P93"),
        ("index.html#p92-frontier", "index.html#p93-frontier"),
        ("Continue to the current P92 frontier", "Continue to the current P93 frontier"),
        ("See the P92 figure", "See the P93 figure"),
        ("Audit P92 provenance", "Audit P93 provenance"),
    )
    for old, new in replacements:
        replace("website/research-map.html", old, new)

    # Start Here and plain-language metadata/current summary cleanup.
    replace(
        "website/start-here.html",
        "current Research II P92 frontier",
        "current Research II P93 frontier",
    )
    for old, new in (
        ("This is the 92-result Research II theorem program currently reaching P92.", "This is the 93-result Research II theorem program currently reaching P93."),
        ("A 92-result sufficiency and falsification architecture", "A 93-result sufficiency and falsification architecture"),
        ("The 92-result proposition program", "The 93-result proposition program"),
        ("P92 is the current checkpoint, not the destination", "P93 is the current checkpoint, not the destination"),
        ("P92 is the current mathematical checkpoint", "P93 is the current mathematical checkpoint"),
        ("all 92 Research II results connect", "all 93 Research II results connect"),
        ("P75-P92", "P75-P93"),
    ):
        replace("website/plain-language.html", old, new)

    # Website build validator is P93-current; make its diagnostics truthful.
    for old, new in (
        ("internally consistent with P92", "internally consistent with P93"),
        ("current P92 theorem figure", "current P93 theorem figure"),
        ("bundled P92 theorem figure", "bundled P93 theorem figure"),
        ("synchronized to 92/P92", "synchronized to 93/P93"),
        ("stale pre-P92 reader text", "stale pre-P93 reader text"),
        ("Research II P92 and Research III", "Research II P93 and Research III"),
    ):
        replace("scripts/prepare_website.py", old, new)

    # Repository verifier follows CURRENT_FRONTIER instead of retaining a P92 literal.
    replace_once(
        "scripts/verify_repository.py",
        '    if "P92" not in (ROOT / "CITATION.cff").read_text(encoding="utf-8"):\n        raise RuntimeError("CITATION.cff does not mention P92")',
        '    if CURRENT_FRONTIER not in (ROOT / "CITATION.cff").read_text(encoding="utf-8"):\n        raise RuntimeError(f"CITATION.cff does not mention {CURRENT_FRONTIER}")',
    )
    collapse_repeated_line(
        "scripts/verify_repository.py",
        '    p93 = visual_atlas.index(\'id="p93-frontier"\')\n',
    )

    # Roadmap: P93 is canonical, P92 transition is historical, P94+ is future work.
    replace(
        "docs/theorem_roadmap.md",
        "- [P93 proof](proposition_93_localized_sign_coherence_rejection.md)",
        "- [P93](proposition_93_localized_sign_coherence_rejection.md)",
    )
    replace(
        "docs/theorem_roadmap.md",
        "## After P92",
        "## Historical transition from P92 to P93",
    )
    append_once(
        "docs/theorem_roadmap.md",
        "## After P93",
        """## After P93

P93 closes the localized finite-sample handoff for the established P92 sign witness. Any P94 candidate must close a genuinely new mathematical or scientific gap rather than merely increase proposition number. Natural directions include alternative observable slicings, broader latent-class families, or sharper finite-sample procedures with equally explicit one-sided certification. The physical-to-experiential bridge remains open.""",
    )

    # Remove migration corruption from the P93 publication tests.
    collapse_repeated_line(
        "tests/test_figure_publication_sync.py",
        '    p93 = text.index(\'id="p93-frontier"\')\n',
    )

    # P92 is now a historical exact population theorem; P93 owns the homepage.
    rewrite_function(
        "tests/test_p92_reader_surface_coherence.py",
        "test_p92_homepage_is_current_and_links_complete_record",
        "test_visual_atlas_orders_p92_before_p91_and_p90",
        '''def test_p92_is_historical_while_p93_owns_the_homepage() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    assert 'id="p93-frontier"' in home
    assert 'id="p92-frontier"' not in home
    p93 = atlas.index('id="p93-frontier"')
    p92 = atlas.index('id="p92-frontier"')
    assert p93 < p92
    historical = atlas[p92:]
    assert "Previous theorem frontier · P92" in historical
    assert "p92_exact_global_mixed_prevalence_distance.svg" in historical
    assert "proposition_92_exact_global_mixed_prevalence_distance.md" in historical
    assert "p92_equation_provenance.md" in historical''',
    )

    # Research-map tests follow the current P93 audit route and preserve P92 history.
    rewrite_function(
        "tests/test_website_research_orientation.py",
        "test_research_map_gives_direct_audit_paths",
        "test_current_and_previous_nonlinear_frontiers_are_structurally_inside_main",
        '''def test_research_map_gives_direct_audit_paths():
    text = MAP.read_text(encoding="utf-8")
    required = [
        "theorem_roadmap.md",
        "research_navigation.md",
        "equation_and_citation_map.md",
        "visual-atlas.html",
        "proposition_71_target_provenance_noncircularity.md",
        "proposition_72_target_measurement_channel_robustness.md",
        "proposition_73_target_channel_identifiability.md",
        "proposition_77_full_law_model_set_separation.md",
        "proposition_78_certified_continuous_model_separation.md",
        "proposition_79_certified_sampling_radius.md",
        "proposition_80_simplex_coupled_model_separation.md",
        "proposition_81_projection_event_model_separation.md",
        "proposition_82_exact_nested_projection_contrast.md",
        "proposition_83_exact_projection_parity.md",
        "proposition_84_exact_projection_parity_contrast.md",
        "proposition_85_exact_triple_projection_parity_functional.md",
        "proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md",
        "proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md",
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
        "proposition_89_complete_linear_parity_duality.md",
        "proposition_90_exact_nonlinear_rank_one_separation.md",
        "proposition_91_mixed_prevalence_rank_two_flattening_separation.md",
        "proposition_92_exact_global_mixed_prevalence_distance.md",
        "p92_equation_provenance.md",
        "proposition_93_localized_sign_coherence_rejection.md",
        "p93_equation_provenance.md",
        'index.html#p93-frontier',
    ]
    for token in required:
        assert token in text, token

    assert "P73-P76" in text
    assert "P74 adds finite-data recovery" in text
    assert "P75 introduces fourth-view overidentification" in text
    assert "P76 turns its necessary restrictions into finite-sample rejection certificates" in text
    assert 'index.html#p91-frontier' not in text
    assert 'index.html#p88-frontier' not in text''',
    )
    rewrite_function(
        "tests/test_website_research_orientation.py",
        "test_current_and_previous_nonlinear_frontiers_are_structurally_inside_main",
        "test_continuous_frontier_keeps_lineage_and_current_provenance_auditable",
        '''def test_current_and_previous_nonlinear_frontiers_are_structurally_inside_main():
    text = MAP.read_text(encoding="utf-8")
    main_open = text.index("<main>")
    main_close = text.index("</main>")
    p90 = text.index('id="p90-research-map"')
    p91 = text.index('id="p91-research-map"')
    p93 = text.index('id="p93-research-map"')
    p92 = text.index('id="p92-research-map"')

    assert text.count('id="p90-research-map"') == 1
    assert text.count('id="p91-research-map"') == 1
    assert text.count('id="p92-research-map"') == 1
    assert text.count('id="p93-research-map"') == 1
    assert main_open < p90 < p91 < p93 < p92 < main_close
    assert "Historical P90 checkpoint" in text[p90:p91]
    assert "Current Research II theorem frontier" not in text[p90:p91]
    assert "Current Research II theorem frontier" not in text[p91:p93]
    assert "P93 · Localized finite-sample nonlinear rejection" in text[p93:p92]
    assert "Historical exact population checkpoint · P92" in text[p92:main_close]''',
    )

    print("[P93] final publication contracts repaired")


if __name__ == "__main__":
    main()

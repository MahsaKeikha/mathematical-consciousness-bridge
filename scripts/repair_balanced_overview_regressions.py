"""Repair CI contracts exposed by the balanced three-stage Overview migration.

This helper is temporary. It keeps historical Research II theorem cards on specialist
surfaces, restores compact cross-cutting provenance/audit navigation to Overview,
and repairs a stale P86 Overview anchor in the implementation guide.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


def replace_once(path: str, old: str, new: str, label: str) -> None:
    text = read(path)
    if new in text:
        return
    if old not in text:
        raise RuntimeError(f"missing repair marker: {label}")
    write(path, text.replace(old, new, 1))


def patch_p84_contract() -> None:
    path = "tests/test_p84_reader_presentation.py"
    old = '''def test_p84_homepage_uses_figure_first_publication_layout() -> None:
    section = _section(_read("website/index.html"), "p84-frontier")
    assert 'class="theorem-frontier"' in section
    assert 'class="theorem-figure-shell"' in section
    assert 'class="frontier-summary-grid"' in section
    assert section.count('class="frontier-summary-card"') == 3
    assert 'class="two-col"' not in section
    assert '<aside class="card">' not in section
    assert "two tests can pass separately and still fail together" in section
    assert "220 coupled contrasts" in section
    assert "L83 = 0" in section
    assert "L84 = 1/32" in section
    assert "does not close the physical-to-experiential bridge" in section
'''
    new = '''def test_p84_history_is_specialist_and_keeps_figure_first_layout() -> None:
    overview = _read("website/index.html")
    assert 'id="p84-frontier"' not in overview

    section = _section(_read("website/visual-atlas.html"), "p84-frontier")
    assert 'class="theorem-frontier"' in section
    assert 'class="theorem-figure-shell"' in section
    assert 'class="frontier-summary-grid"' in section
    assert section.count('class="frontier-summary-card"') == 3
    assert 'class="two-col"' not in section
    assert '<aside class="card">' not in section
    assert "P83 can accept two parity events separately" in section
    assert "common-parameter contrast range" in section
    assert "L83 = 0 but L84 = 1/32" in section
    assert "not an experiential identification claim" in section
'''
    replace_once(path, old, new, "P84 specialist-surface contract")


def patch_overview_audit_paths() -> None:
    path = "website/index.html"
    text = read(path)
    if 'id="audit-paths"' in text:
        return
    marker = '    <section id="plain-language">'
    if marker not in text:
        raise RuntimeError("Overview plain-language insertion marker missing")
    section = '''    <section id="audit-paths">
      <div class="section-head">
        <p class="eyebrow">Audit the research</p>
        <h2>Trace every consequential claim back to its equation, source, proof, test, and scientific boundary.</h2>
        <p>The three research stages share one publication rule: standard mathematics and physics stay sourced, empirical evidence stays distinguishable from theorem, repository-original results stay tied to their proof and implementation record, and unresolved targets remain visibly open.</p>
      </div>
      <div class="source-grid">
        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/equation_and_citation_map.md"><h3>Equation and citation map</h3><p>Trace important equations to external sources, declared assumptions, or earlier propositions.</p></a>
        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/citation_and_reference_policy.md"><h3>Citation policy</h3><p>See the source-quality, DOI, empirical-wording, and scientific-role rules used across the program.</p></a>
        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/reference_audit.md"><h3>Reference audit</h3><p>Check metadata, evidence classification, and the role assigned to consequential external sources.</p></a>
        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/theorem_roadmap.md"><h3>Theorem roadmap</h3><p>Follow dependencies and proposition lineage without mistaking development order for scientific depth.</p></a>
        <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/falsification_program.md"><h3>Falsification and evidence</h3><p>Inspect what observations can reject, bound, or leave unresolved under the declared model family.</p></a>
        <a href="sources.html"><h3>Sources &amp; reproducibility</h3><p>Audit bibliographies, claim classes, proof/code/test links, and the current theorem source record.</p></a>
      </div>
      <div class="boundary"><p><strong>Publication labels:</strong> a <strong>Repository-original theorem or computation</strong> is not presented as an external fact, and an <strong>Open hypothesis or theorem target</strong> is not formatted as an established result.</p></div>
    </section>

'''
    write(path, text.replace(marker, section + marker, 1))


def patch_implementation_frontier() -> None:
    path = "website/implementation.html"
    old = '''  <p class="scientific-boundary"><strong>Frontier continuation:</strong> P77-P86 strengthen this branch from individual adequacy constraints to certified separation from the complete continuous model family. P84 adds pairwise shared-parameter parity compatibility, P85 adds three-event functionals, and the current P88 frontier adds 10,560 minimally weighted four-event functionals with the strict exact hierarchy <strong>L85 = 0 &lt; L86 = 1/192</strong>. See the <a href="index.html#p86-frontier">current P88 frontier</a> and the <a href="research-map.html">Research Map</a> for the full lineage.</p>'''
    new = '''  <p class="scientific-boundary"><strong>Frontier continuation:</strong> P77-P88 strengthen this branch from individual adequacy constraints to certified separation from the complete continuous model family. P84 adds pairwise shared-parameter parity compatibility, P85 adds three-event functionals, P86 adds 10,560 minimally weighted four-event functionals, P87 completes the 39,600-function primitive radius-two family, and P88 enlarges that complete primitive family to radius three with 208,560 exact functionals. The strict witness hierarchy is <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>. See the <a href="index.html#p88-frontier">current P88 frontier</a> and the <a href="research-map.html">Research Map</a> for the full lineage.</p>'''
    replace_once(path, old, new, "implementation P88 frontier continuation")
    replace_once(
        path,
        '<strong>weighted_quad_projection_parity_functional_separation.py</strong><small>P86 current four-event exact parity-functional implementation</small>',
        '<strong>weighted_quad_projection_parity_functional_separation.py</strong><small>P86 minimally weighted four-event exact parity-functional implementation</small>',
        "implementation P86 label",
    )


def verify() -> None:
    overview = read("website/index.html")
    expected_order = [
        overview.index('id="project-journey"'),
        overview.index('id="research-i-overview"'),
        overview.index('id="p88-frontier"'),
        overview.index('id="research-iii-overview"'),
        overview.index('id="reader-paths"'),
        overview.index('id="audit-paths"'),
        overview.index('id="plain-language"'),
    ]
    if expected_order != sorted(expected_order):
        raise RuntimeError("Overview stage/audit ordering drifted")
    for historical_id in ('id="p87-frontier"', 'id="p86-frontier"', 'id="p85-frontier"', 'id="p84-frontier"'):
        if historical_id in overview:
            raise RuntimeError(f"historical frontier leaked into Overview: {historical_id}")
    for token in (
        "Equation and citation map",
        "Citation policy",
        "Reference audit",
        "Theorem roadmap",
        "Falsification and evidence",
        "Repository-original theorem or computation",
        "Open hypothesis or theorem target",
    ):
        if token not in overview:
            raise RuntimeError(f"missing Overview audit token: {token}")
    implementation = read("website/implementation.html")
    if "index.html#p86-frontier" in implementation:
        raise RuntimeError("stale P86 Overview anchor remains")
    if "index.html#p88-frontier" not in implementation:
        raise RuntimeError("current P88 Overview anchor missing")


def main() -> None:
    patch_p84_contract()
    patch_overview_audit_paths()
    patch_implementation_frontier()
    verify()


if __name__ == "__main__":
    main()

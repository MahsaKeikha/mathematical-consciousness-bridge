"""Synchronize P86 reader-facing scholarly and layout contracts.

This is a temporary migration helper. It is intentionally strict and idempotent:
it edits only known stale P85-era reader text and permanent publication guards.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _replace_once(text: str, old: str, new: str, label: str) -> str:
    if old == new:
        return text
    if old not in text:
        if new in text:
            return text
        raise RuntimeError(f"missing migration anchor for {label}: {old!r}")
    return text.replace(old, new, 1)


def sync_start_here() -> None:
    path = ROOT / "website" / "start-here.html"
    text = path.read_text(encoding="utf-8")
    replacements = (
        (
            "to the 85-result theorem program and current P86 frontier.",
            "to the 86-result theorem program and current P86 frontier.",
            "metadata result count",
        ),
        (
            "<h2>P78-P85 progressively tighten global separation from the declared continuous model family</h2>",
            "<h2>P78-P86 progressively tighten global separation from the declared continuous model family</h2>",
            "frontier heading",
        ),
        (
            "P83 now adds 22 exact projection-parity observables",
            "P83 added 22 exact projection-parity observables",
            "P83 historical wording",
        ),
        (
            "<strong>P84 now preserves shared-parameter compatibility between pairs of P83 parity events.</strong>",
            "<strong>P84 added pairwise shared-parameter compatibility between P83 parity events.</strong>",
            "P84 historical wording",
        ),
        (
            "<strong>P85 now tests exact three-event shared-parameter compatibility beyond the complete P84 pairwise certificate.</strong>",
            "<strong>P85 extended the hierarchy to exact three-event shared-parameter compatibility beyond the complete P84 pairwise certificate.</strong>",
            "P85 historical wording",
        ),
        (
            '<a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_85_exact_triple_projection_parity_functional.md">Read P85</a>',
            '<a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md">Read P86</a>',
            "frontier CTA",
        ),
    )
    for old, new, label in replacements:
        text = _replace_once(text, old, new, label)

    p85 = (
        "      <p><strong>P85 extended the hierarchy to exact three-event shared-parameter compatibility "
        "beyond the complete P84 pairwise certificate.</strong> Its 660 sign-normalized functionals include "
        "an exact-rational witness with L84 = 0, empirical value 5/8, exact P75 interval [1,2], centered "
        "coefficient norm 12, and L85 = 1/32.</p>\n"
    )
    p86 = (
        p85
        + "      <p><strong>P86 is the current exact frontier.</strong> It audits 10,560 sign-normalized "
        "four-event functionals with primitive coefficient magnitudes {1,1,1,2}. Its strict exact-rational "
        "witness satisfies <strong>L85 = 0 &lt; L86 = 1/192</strong>, so the minimally weighted four-event "
        "family can separate a P75 parameter box that remains compatible with the complete P85 certificate.</p>\n"
    )
    if "P86 is the current exact frontier." not in text:
        if p85 not in text:
            raise RuntimeError("missing P85 paragraph used to insert P86 frontier")
        text = text.replace(p85, p86, 1)

    origin_anchor = "    <section>\n      <div class=\"section-head\">\n        <p class=\"eyebrow\">First principle</p>"
    origin = (
        "    <section id=\"research-origin\" class=\"boundary\">\n"
        "      <div class=\"section-head\">\n"
        "        <p class=\"eyebrow\">Research origin</p>\n"
        "        <h2>One early question that helped start the program</h2>\n"
        "        <p>The earliest conceptual line that eventually led to this research program began while studying "
        "Max Tegmark's <em>Consciousness as a State of Matter</em> (2015). That paper motivated questions about "
        "physical subsystem structure, factorization, information, integration, independence, and dynamics. The "
        "present repository subsequently developed its own theorem program, assumptions, proofs, computational "
        "certificates, and falsification boundaries.</p>\n"
        "        <p><strong>Citation:</strong> Max Tegmark, <em>Consciousness as a State of Matter</em>, "
        "<em>Chaos, Solitons &amp; Fractals</em> 76 (2015), 238–270. "
        "<a href=\"https://doi.org/10.1016/j.chaos.2015.03.014\">DOI</a> · "
        "<a href=\"https://arxiv.org/abs/1401.1219\">arXiv:1401.1219</a>. "
        "See <a href=\"sources.html#research-origins\">Sources &amp; Reproducibility</a> for the exact evidential role.</p>\n"
        "        <p><strong>Boundary:</strong> this origin citation does not make Tegmark's paper evidence for the later "
        "P1–P86 results and does not imply that any physical-to-experiential ontology has been established.</p>\n"
        "      </div>\n"
        "    </section>\n\n"
    )
    if 'id="research-origin"' not in text:
        if origin_anchor not in text:
            raise RuntimeError("missing Start Here first-principle insertion anchor")
        text = text.replace(origin_anchor, origin + origin_anchor, 1)

    path.write_text(text, encoding="utf-8")


def sync_reader_css() -> None:
    path = ROOT / "website" / "reader-experience-v2.css"
    text = path.read_text(encoding="utf-8")
    marker = "/* Site-wide grid containment contract:"
    if marker in text:
        return
    anchor = "@media (max-width: 900px) {\n"
    if anchor not in text:
        raise RuntimeError("missing reader CSS media anchor")
    block = """/* Site-wide grid containment contract:
 * long scientific labels and repository paths must stay inside their own
 * cards at every desktop and tablet width. */
.status-grid > *,
.flow > *,
.result-grid > *,
.source-grid > *,
.falsify-grid > *,
.reader-primer-grid > *,
.reader-step-grid > *,
.research-card-grid > *,
.reader-trail-grid > *,
.lineage-callout-actions > *,
.frontier-summary-grid > *,
.implementation-index > *,
.implementation-links > * {
  min-width: 0;
  max-width: 100%;
}

.source-grid h3,
.result h3,
.flow-node h3,
.card h3,
.reader-primer-card strong,
.reader-step-card strong,
.frontier-summary-card h3,
.implementation-index strong,
.implementation-links strong,
.research-card-grid h3,
.research-card-grid strong,
.reader-trail-grid strong {
  max-width: 100%;
  overflow-wrap: anywhere;
  word-break: normal;
}

.button {
  max-width: 100%;
  overflow-wrap: anywhere;
}

"""
    path.write_text(text.replace(anchor, block + anchor, 1), encoding="utf-8")


def sync_reader_tests() -> None:
    path = ROOT / "tests" / "test_reader_experience.py"
    text = path.read_text(encoding="utf-8")
    style_anchor = '    assert \'"reader-experience-v2.css"\' in prepare\n'
    if 'assert "Site-wide grid containment contract:" in css' not in text:
        if style_anchor not in text:
            raise RuntimeError("missing reader style test anchor")
        text = text.replace(
            style_anchor,
            style_anchor
            + '    assert "Site-wide grid containment contract:" in css\n'
            + '    assert ".implementation-links > *" in css\n'
            + '    assert "overflow-wrap: anywhere" in css\n',
            1,
        )

    start_anchor = '    assert "The 86 propositions by scientific role" in start\n'
    if 'assert "P86 is the current exact frontier." in start' not in text:
        if start_anchor not in text:
            raise RuntimeError("missing Start Here test anchor")
        text = text.replace(
            start_anchor,
            '    assert "86-result theorem program and current P86 frontier" in start\n'
            '    assert "P78-P86 progressively tighten global separation" in start\n'
            '    assert "P86 is the current exact frontier." in start\n'
            '    assert "L85 = 0 &lt; L86 = 1/192" in start\n'
            '    assert ">Read P86</a>" in start\n'
            '    assert \'id="research-origin"\' in start\n'
            '    assert "10.1016/j.chaos.2015.03.014" in start\n'
            + start_anchor,
            1,
        )

    tuple_anchor = '        "<strong>85</strong><span>proposition-level results</span>",\n'
    if '"85-result theorem program and current P86 frontier"' not in text:
        if tuple_anchor not in text:
            raise RuntimeError("missing stale-token tuple anchor")
        text = text.replace(
            tuple_anchor,
            '        "85-result theorem program and current P86 frontier",\n'
            '        "<h2>P78-P85 progressively tighten global separation from the declared continuous model family</h2>",\n'
            + tuple_anchor,
            1,
        )
    path.write_text(text, encoding="utf-8")


def sync_verifier() -> None:
    path = ROOT / "scripts" / "verify_repository.py"
    text = path.read_text(encoding="utf-8")
    core_anchor = '    "docs/figure_caption_and_description_standard.md",\n'
    if '    "docs/claim_evidence_standard.md",\n' not in text:
        if core_anchor not in text:
            raise RuntimeError("missing verifier core-file anchor")
        text = text.replace(
            core_anchor,
            core_anchor + '    "docs/claim_evidence_standard.md",\n',
            1,
        )
    website_anchor = '    "website/visual-atlas.html",\n'
    if '    "website/sources.html",\n' not in text:
        if website_anchor not in text:
            raise RuntimeError("missing verifier website core anchor")
        text = text.replace(
            website_anchor,
            website_anchor + '    "website/sources.html",\n',
            1,
        )
    link_anchor = '    "docs/figure_caption_and_description_standard.md",\n'
    # The first occurrence belongs to CORE_FILES; add to LINK_SURFACES separately.
    link_section = text.index("LINK_SURFACES = (")
    link_pos = text.find(link_anchor, link_section)
    if '"docs/claim_evidence_standard.md"' not in text[link_section:text.index(")", link_section)]:
        if link_pos == -1:
            raise RuntimeError("missing verifier link-surface anchor")
        insertion = link_pos + len(link_anchor)
        text = text[:insertion] + '    "docs/claim_evidence_standard.md",\n' + text[insertion:]

    stale_anchor = "STALE_READER_FRONTIER_MARKERS = (\n"
    if '    "85-result theorem program and current P86 frontier",\n' not in text:
        if stale_anchor not in text:
            raise RuntimeError("missing verifier stale marker anchor")
        text = text.replace(
            stale_anchor,
            stale_anchor
            + '    "85-result theorem program and current P86 frontier",\n'
            + '    "<h2>P78-P85 progressively tighten global separation from the declared continuous model family</h2>",\n',
            1,
        )

    read_anchor = '    visual_atlas = _read("website/visual-atlas.html")\n'
    if '    sources_page = _read("website/sources.html")\n' not in text:
        if read_anchor not in text:
            raise RuntimeError("missing verifier sources read anchor")
        text = text.replace(
            read_anchor,
            read_anchor + '    sources_page = _read("website/sources.html")\n',
            1,
        )
    frontier_anchor = '        ("website/visual-atlas.html", visual_atlas),\n'
    if '("website/sources.html", sources_page)' not in text:
        if frontier_anchor not in text:
            raise RuntimeError("missing verifier frontier-surface anchor")
        text = text.replace(
            frontier_anchor,
            frontier_anchor + '        ("website/sources.html", sources_page),\n',
            1,
        )

    release_gate = '    _verify_reader_frontier_freshness()\n'
    origin_checks = (
        '    if "10.1016/j.chaos.2015.03.014" not in sources_page or "arXiv:1401.1219" not in sources_page:\n'
        '        raise RuntimeError("sources page does not expose the verified Tegmark research-origin citation")\n'
        '    if "intellectual and physical-context background" not in sources_page:\n'
        '        raise RuntimeError("sources page does not distinguish research origin from evidential support")\n\n'
    )
    if "verified Tegmark research-origin citation" not in text:
        if release_gate not in text:
            raise RuntimeError("missing verifier release gate anchor")
        text = text.replace(release_gate, origin_checks + release_gate, 1)
    path.write_text(text, encoding="utf-8")


def sync_literature_map() -> None:
    path = ROOT / "docs" / "literature_map.md"
    text = path.read_text(encoding="utf-8")
    citation = (
        'Max Tegmark, "Consciousness as a State of Matter," *Chaos, Solitons & Fractals* 76 (2015): '
        '238-270. DOI: [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014).'
    )
    citation_with_preprint = citation + ' Preprint: [arXiv:1401.1219](https://arxiv.org/abs/1401.1219).'
    if "arXiv:1401.1219" not in text.split("---", 2)[1]:
        if citation not in text:
            raise RuntimeError("missing Tegmark literature-map citation anchor")
        text = text.replace(citation, citation_with_preprint, 1)
    role_anchor = (
        "**Use here:** motivates part of the physical-subsystem problem and the companion observer program. "
        "It does not supply the physical-to-experiential bridge developed in this repository."
    )
    origin = (
        role_anchor
        + "\n\n**Research-origin note:** this was the earliest paper whose physical framing directly prompted the "
        "line of questions that grew into this program. That historical role is distinct from evidential support: "
        "the later repository propositions require their own proofs, code, tests, and provenance."
    )
    if "**Research-origin note:**" not in text:
        if role_anchor not in text:
            raise RuntimeError("missing Tegmark role anchor in literature map")
        text = text.replace(role_anchor, origin, 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    sync_start_here()
    sync_reader_css()
    sync_reader_tests()
    sync_verifier()
    sync_literature_map()
    sources = (ROOT / "website" / "sources.html").read_text(encoding="utf-8")
    required = (
        'id="research-origins"',
        "10.1016/j.chaos.2015.03.014",
        "arXiv:1401.1219",
        'id="p86-source"',
        "claim_evidence_standard.md",
    )
    missing = [marker for marker in required if marker not in sources]
    if missing:
        raise RuntimeError(f"sources page scholarly contract incomplete: {missing}")


if __name__ == "__main__":
    main()

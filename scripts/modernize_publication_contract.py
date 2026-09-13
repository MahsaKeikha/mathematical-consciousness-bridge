"""Modernize stale publication metadata and reader-contract tests for P88.

This is a one-shot maintenance script used to repair reader surfaces that still
encoded pre-P88 publication assumptions after the README was intentionally
refactored into a compact gateway. It preserves the current scientific scope:
P88 is a conditional exact model-separation result, not a consciousness proof.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, text: str) -> None:
    (ROOT / relative).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise RuntimeError(f"{label}: expected text not found: {old!r}")
    return text.replace(old, new)


def update_citation_metadata() -> None:
    text = read("CITATION.cff")
    text = text.replace(
        "Current documented theorem frontier: P87.",
        "Current documented theorem frontier: P88.",
    )
    write("CITATION.cff", text)

    text = read("CITATION.md")
    text = re.sub(
        r"current documented theorem frontier is \*\*P\d+\*\*",
        "current documented theorem frontier is **P88**",
        text,
        count=1,
    )
    text = text.replace("P1 through **P86**", "P1 through **P88**")
    text = text.replace("P1 through **P87**", "P1 through **P88**")
    if "P88" not in text:
        raise RuntimeError("CITATION.md did not acquire a P88 frontier reference")
    write("CITATION.md", text)


def update_detailed_record() -> None:
    path = "docs/detailed_proposition_record.md"
    text = read(path)
    text = text.replace("Complete P1 to P87 chronology", "Complete P1 to P88 chronology")
    text = text.replace("Complete P1-P87 chronology", "Complete P1-P88 chronology")
    text = text.replace("84 disconnected proofs", "88 disconnected proofs")
    if "**P88**" not in text:
        block = r"""

### P88 - Radius-three bounded primitive four-event parity certificate

**P88** extends the complete primitive four-event parity audit from the
coefficient box `|c_i| <= 2` to every nonzero integer coefficient vector with
`|c_i| <= 3`, after primitive reduction and sign normalization. For each
four-event subset, the exact family contains **632** primitive coefficient
patterns. Across the 330 four-event subsets of the 11 canonical P83 parity
coordinates, this gives **208,560 exact functionals**.

The strict exact witness uses

`((0,2),1), ((1,3),-1), ((1,2,3),-3), ((0,1,2,3),2)`.

For that witness, the empirical functional value is `-11/8`, the exact P75
model interval is `[-1,2]`, the interval gap is `3/8`, the centered coefficient
norm is `24`, and the certified separation lower bound is `1/64`. Consequently,

`L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64`.

**Scientific status.** P88 is an exact conditional model-separation theorem for
the declared P75 target-measurement family. It does not identify consciousness,
establish nonphysicality, or close the physical-to-experiential bridge.

Audit path: [P88 proof](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md), [P88 equation provenance](p88_equation_provenance.md), [implementation](../src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py), [exact tests](../tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py), and [theorem figure](figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg).
"""
        text = text.rstrip() + block + "\n"
    write(path, text)


def repair_reproducibility_equations() -> None:
    path = "docs/reproducibility.md"
    text = read(path).replace("\x0crac", r"\frac")
    write(path, text)


def update_p88_figure_status() -> None:
    path = "docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg"
    text = read(path)
    if "Scientific status:" not in text:
        text = text.replace(
            " under the declared P75 interval model, not a general consciousness proof.</desc>",
            " under the declared P75 interval model. Scientific status: exact conditional model-separation certificate for the declared P75 family; it does not identify consciousness, imply nonphysicality, or close the physical-to-experiential bridge.</desc>",
        )
    if "Scientific status:" not in text:
        raise RuntimeError("P88 SVG description was not updated with scientific status")
    write(path, text)


def update_figure_catalog() -> None:
    path = "docs/figure_catalog.md"
    text = read(path)
    figure_count = len(list((ROOT / "docs" / "figures").glob("*.svg")))
    text = re.sub(r"## All \d+ figures", f"## All {figure_count} figures", text, count=1)
    filename = "p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg"
    if filename not in text:
        text = text.rstrip() + f"""

### P88 exact radius-three bounded primitive four-event parity certificate

![P88 exact radius-three bounded primitive four-event parity certificate](figures/{filename})

**Interpretation.** P88 exhausts the primitive nonzero four-event coefficient
box with `|c_i| <= 3`, yielding 632 sign-normalized patterns per four-event
subset and 208,560 exact functionals across the canonical P83 parity
coordinates. The strict witness raises the certified lower bound from `1/96`
to `1/64`.

**Scientific status.** This figure visualizes an exact conditional
model-separation certificate for the declared P75 family. It is not a direct
measure of consciousness and does not establish nonphysicality.
"""
    write(path, text + ("" if text.endswith("\n") else "\n"))


def update_claim_source_matrix() -> None:
    path = "docs/claim_source_matrix.md"
    text = read(path)
    text = text.replace("audited by P75-P86", "audited by P75-P88")
    p87_row = "| P87 bounded primitive four-event compatibility | Completing every nonzero primitive four-event coefficient vector with `|c_i| <= 2` can strictly strengthen the complete P86 certificate | repository theorem | [P87 proof](proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md), [P87 provenance](p87_equation_provenance.md), [`bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py), [tests](../tests/test_bounded_primitive_quad_projection_parity_functional_separation.py), [figure](figures/p87_exact_bounded_primitive_quad_projection_parity.svg) | `L86 = 1/192 < L87 = 1/96` is an exact synthetic strict witness inside the declared P75 family |"
    if "| P88 radius-three bounded primitive four-event compatibility |" not in text:
        if p87_row not in text:
            raise RuntimeError("claim-source matrix P87 row not found")
        p88_row = "| P88 radius-three bounded primitive four-event compatibility | Completing every nonzero primitive four-event coefficient vector with `|c_i| <= 3` can strictly strengthen the complete P87 certificate | repository theorem | [P88 proof](proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md), [P88 provenance](p88_equation_provenance.md), [`radius_three_bounded_primitive_quad_projection_parity_functional_separation.py`](../src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py), [tests](../tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py), [figure](figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg) | `L87 = 1/96 < L88 = 1/64` is an exact synthetic strict witness inside the declared P75 family |"
        text = text.replace(p87_row, p87_row + "\n" + p88_row)
    text = text.replace(
        "The current repository contains 87 proposition-level results",
        "The current repository contains 88 proposition-level results",
    )
    text = text.replace(
        "P87 is the current theorem frontier",
        "P88 is the current theorem frontier",
    )
    text = text.replace(
        "P86 proof, implementation, tests, provenance, figure, and frontier publication tests",
        "P88 proof, implementation, tests, provenance, figure, and frontier publication tests",
    )
    text = text.replace(
        "P84 and P85 remain historical certified frontiers, not current ones",
        "P84 through P87 remain historical certified frontiers, not current ones",
    )
    write(path, text)


def update_sources_page() -> None:
    path = "website/sources.html"
    text = read(path)
    start = text.find('<section id="p87-source">')
    end = text.find("</main>", start)
    if start < 0 or end < 0:
        raise RuntimeError("website theorem-source block not found")
    block = """<section id="p88-source"><div class="section-head"><p class="eyebrow">Current theorem source · P88</p><h2>Exact radius-three bounded primitive four-event projection-parity certificate</h2><p>P88 completes every nonzero primitive four-event coefficient vector with magnitude at most three, yielding 632 sign-normalized primitive patterns per four-event subset and 208,560 exact functionals. On the strict rational witness, <strong>L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64</strong>.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md"><h3>Proposition 88</h3><p>Formal statement, exact family count, interval proof, centered transfer bound, strict witness, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p88_equation_provenance.md"><h3>P88 provenance</h3><p>Separates inherited parity algebra and exact finite arguments from the repository-original radius-three construction.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/radius_three_bounded_primitive_quad_projection_parity_functional_separation.py"><h3>P88 implementation</h3><p>Exact rational exhaustive enumeration of the complete 208,560-functional family.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py"><h3>P88 exact tests</h3><p>Family count, exact interval, centered norm, strict witness, hierarchy, and interpretation-boundary regression tests.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg"><h3>P88 theorem figure</h3><p>Source-controlled visual summary synchronized with the exact theorem and publication checks.</p></a></div><div class="boundary"><p><strong>Scientific status:</strong> P88 is a conditional exact model-separation result for the declared P75 family. It does not identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p></div></section>

<section id="p87-source"><div class="section-head"><p class="eyebrow">Previous theorem source · P87</p><h2>Exact bounded primitive four-event projection-parity certificate</h2><p>P87 completes every nonzero primitive four-event coefficient vector with magnitude at most two, yielding 39,600 exact functionals and the strict hierarchy <strong>L86 = 1/192 &lt; L87 = 1/96</strong>.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md"><h3>Proposition 87</h3><p>Formal statement, exact family count, interval proof, transfer bound, strict witness, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p87_equation_provenance.md"><h3>P87 provenance</h3><p>Separates inherited parity algebra, finite counting, endpoint arguments, and repository-original constructions.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/bounded_primitive_quad_projection_parity_functional_separation.py"><h3>P87 implementation</h3><p>Exact rational exhaustive enumeration of the complete 39,600-functional family.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_bounded_primitive_quad_projection_parity_functional_separation.py"><h3>P87 exact tests</h3><p>Family count, exact interval, centered norm, strict witness, dominance, and interpretation-boundary regression tests.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p87_exact_bounded_primitive_quad_projection_parity.svg"><h3>P87 theorem figure</h3><p>Source-controlled visual summary synchronized with the theorem and figure publication manifest.</p></a></div></section>

"""
    text = text[:start] + block + text[end:]
    write(path, text)


def update_lineage_source() -> None:
    path = "website/research-lineage.html"
    text = read(path)
    text = text.replace(
        'src="figures/research_architecture.svg"',
        'src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/research_architecture.svg"',
    )
    phrase = "Bridge remains an independently testable open problem."
    if phrase not in text:
        marker = "The mathematical sequence does not, by itself, supply an experiential target."
        if marker in text:
            text = text.replace(marker, marker + " " + phrase, 1)
        else:
            text = text.replace(
                "The three repositories form a research progression",
                phrase + " The three repositories form a research progression",
                1,
            )
    write(path, text)


def update_prepare_website_fixture_behavior() -> None:
    path = "scripts/prepare_website.py"
    text = read(path)
    old = "    _validate_current_frontier_pages(output)\n    _validate_research_three(output)\n"
    new = """    frontier_sentinels = (
        output / \"index.html\",
        output / \"visual-atlas.html\",
        output / \"reader-experience-v2.css\",
    )
    if all(path.is_file() for path in frontier_sentinels):
        _validate_current_frontier_pages(output)

    research_three_sentinels = (
        output / \"measurement-science.html\",
        output / \"research-lineage.html\",
    )
    if all(path.is_file() for path in research_three_sentinels):
        _validate_research_three(output)
"""
    text = replace_required(text, old, new, path)
    write(path, text)


README_ORIENTATION_TEST = '''import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = ROOT / "START_HERE.md"
DETAIL = ROOT / "docs/detailed_proposition_record.md"


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*.md"):
        match = re.match(r"proposition_(\\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers)


def test_readme_is_compact_gateway_to_current_frontier():
    text = README.read_text(encoding="utf-8")
    assert len(text) < 12_000
    assert "The current public theorem frontier is **P88**" in text
    assert "formal release remains **v0.82.0**" in text
    for target in (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/figure_catalog.md",
        "docs/detailed_proposition_record.md",
        "docs/theorem_roadmap.md",
        "docs/reproducibility.md",
    ):
        assert target in text


def test_reader_gateway_preserves_scientific_boundaries():
    text = README.read_text(encoding="utf-8").lower()
    for phrase in (
        "does **not** claim",
        "proves that consciousness is nonphysical",
        "final bridge from physical description to experience has been solved",
        "bridge remains an open scientific problem",
    ):
        assert phrase in text


def test_detailed_record_tracks_complete_dynamic_frontier():
    detail = DETAIL.read_text(encoding="utf-8")
    frontier = _frontier()
    assert frontier == 88
    assert f"Complete P1 to P{frontier} chronology" in detail
    assert "**P1**" in detail
    assert "**P88**" in detail
    assert "208,560 exact functionals" in detail
    assert "L85 = 0 < L86 = 1/192 < L87 = 1/96 < L88 = 1/64" in detail


def test_start_here_matches_public_identity():
    text = START.read_text(encoding="utf-8")
    assert "88" in text
    assert "P88" in text
    assert "v0.82.0" in text
'''


MAIN_PAGE_VISUAL_TEST = '''import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DETAIL = ROOT / "docs/detailed_proposition_record.md"
CATALOG = ROOT / "docs/figure_catalog.md"


def _frontier() -> int:
    numbers = []
    for path in (ROOT / "docs").glob("proposition_*.md"):
        match = re.match(r"proposition_(\\d+)_", path.name)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers)


def test_readme_routes_visual_depth_instead_of_embedding_full_atlas():
    text = README.read_text(encoding="utf-8")
    assert "docs/figure_catalog.md" in text
    assert "docs/detailed_proposition_record.md" in text
    assert "docs/theorem_roadmap.md" in text
    assert len(text) < 12_000


def test_figure_catalog_contains_current_frontier_figure_and_status():
    text = CATALOG.read_text(encoding="utf-8")
    assert "p88_exact_radius_three_bounded_primitive_quad_projection_parity.svg" in text
    assert "208,560" in text
    assert "Scientific status." in text or "Scientific status:" in text


def test_detailed_proposition_chronology_reaches_dynamic_frontier():
    readme = README.read_text(encoding="utf-8")
    detail = DETAIL.read_text(encoding="utf-8")
    frontier = _frontier()
    assert frontier == 88
    assert "docs/detailed_proposition_record.md" in readme
    assert f"Complete P1 to P{frontier} chronology" in detail
    assert "**P88**" in detail


def test_readme_declares_scientific_status_boundaries():
    text = README.read_text(encoding="utf-8")
    required = (
        "does **not** claim",
        "proves that consciousness is nonphysical",
        "final bridge from physical description to experience has been solved",
        "The bridge remains an open scientific problem.",
    )
    for phrase in required:
        assert phrase in text
'''


WEBSITE_ORIENTATION_TEST = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"


def test_research_map_starts_with_orientation_before_stage_details():
    text = MAP.read_text(encoding="utf-8")
    hero = text.index("Eighty-eight results, one dependency-aware scientific program")
    orientation = text.index("How to read this research")
    stage_one = text.index("I · Formal bridge foundations")
    assert hero < orientation < stage_one


def test_research_map_exposes_current_status_and_stage_ranges():
    text = MAP.read_text(encoding="utf-8")
    for token in (
        "Proved results",
        "Conditional results",
        "Open bridge target",
        "P1-P10",
        "P11-P18",
        "P19-P24",
        "P71",
        "P72",
        "P73-P88",
        "P25-P37",
        "P38-P44",
        "P45-P60",
        "P61-P70",
        "Ten-stage scientific path",
    ):
        assert token in text


def test_research_map_exposes_current_p88_audit_path():
    text = MAP.read_text(encoding="utf-8")
    for token in (
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
        "p88_equation_provenance.md",
        "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        "index.html#p88-frontier",
        "208,560",
        "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64",
    ):
        assert token in text


def test_research_map_keeps_previous_frontiers_as_history():
    text = MAP.read_text(encoding="utf-8")
    assert "through Proposition 88" in text
    assert "P85 tests exact three-event shared-parameter parity functionals" in text
    assert "P86 adds exact minimally weighted four-event functionals" in text
    assert "39,600" in text
    assert "P88" in text
    assert text.index("P87") < text.index("P88", text.index("P87"))
'''


SCHOLARLY_TEST = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_sources_page_records_tegmark_origin_with_collegial_scope() -> None:
    sources = _read("website/sources.html")
    assert 'id="research-origins"' in sources
    assert "Max Tegmark" in sources
    assert "Consciousness as a State of Matter" in sources
    assert "10.1016/j.chaos.2015.03.014" in sources
    assert "arXiv:1401.1219" in sources
    assert "important conceptual starting point" in sources
    assert "distinct mathematical framework" in sources


def test_claim_source_matrix_tracks_p88_frontier_and_boundaries() -> None:
    matrix = _read("docs/claim_source_matrix.md")
    for marker in (
        "Claim-to-Source Scientific Audit Matrix",
        "P75 model family",
        "P87 bounded primitive four-event compatibility",
        "P88 radius-three bounded primitive four-event compatibility",
        "L87 = 1/96 < L88 = 1/64",
        "88 proposition-level results",
        "P88 is the current theorem frontier",
        "passing CI supports internal consistency and reproducibility; it is not external peer review",
    ):
        assert marker in matrix


def test_sources_page_points_to_current_p88_and_previous_p87_records() -> None:
    sources = _read("website/sources.html")
    for marker in (
        'id="p88-source"',
        "Current theorem source · P88",
        "208,560",
        "L85 = 0 &lt; L86 = 1/192 &lt; L87 = 1/96 &lt; L88 = 1/64",
        "proposition_88_exact_radius_three_bounded_primitive_quad_projection_parity_functional.md",
        "p88_equation_provenance.md",
        "radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        "test_radius_three_bounded_primitive_quad_projection_parity_functional_separation.py",
        'id="p87-source"',
        "Previous theorem source · P87",
        "L86 = 1/192 &lt; L87 = 1/96",
        "claim_source_matrix.md",
    ):
        assert marker in sources


def test_machine_readable_bibliography_contains_exact_tegmark_metadata() -> None:
    bibliography = _read("references.bib")
    assert "@article{tegmark2015consciousness" in bibliography
    assert "doi     = {10.1016/j.chaos.2015.03.014}" in bibliography


def test_public_provenance_does_not_make_priority_or_ontology_claims() -> None:
    public = _read("website/sources.html") + _read("docs/claim_source_matrix.md")
    for phrase in (
        "first theory of consciousness",
        "first proof of consciousness",
        "proves consciousness is nonphysical",
        "proves consciousness is a new dimension",
        "Tegmark validates this framework",
        "Tegmark proves this framework",
    ):
        assert phrase not in public
'''


PUBLIC_LAYERING_TEST = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
START = ROOT / "START_HERE.md"
INDEX = ROOT / "website/index.html"
APP = ROOT / "website/app.js"


def test_public_reader_documents_keep_progressive_disclosure():
    assert len(README.read_text(encoding="utf-8")) < 12_000
    assert len(START.read_text(encoding="utf-8")) < 9_000


def test_readme_is_gateway_not_monolithic_paper():
    text = README.read_text(encoding="utf-8")
    for target in (
        "START_HERE.md",
        "docs/research_map.md",
        "docs/figure_catalog.md",
        "docs/detailed_proposition_record.md",
        "docs/reproducibility.md",
    ):
        assert target in text
    assert "The current public theorem frontier is **P88**" in text


def test_start_here_exposes_current_identity_without_forcing_theorem_sequence():
    text = START.read_text(encoding="utf-8")
    assert "88" in text
    assert "P88" in text
    assert "v0.82.0" in text
    assert "You do not need to read" in text


def test_homepage_is_visual_gateway_with_current_status():
    text = INDEX.read_text(encoding="utf-8")
    assert "Explore all 88 results" in text
    assert "Current theorem frontier · P88" in text
    assert 'href="start-here.html"' in text
    assert 'href="research-map.html"' in text
    assert 'href="measurement-science.html"' in text
    assert 'href="visual-atlas.html"' in text
    assert text.count('id="p88-frontier"') == 1


def test_navigation_script_exposes_reader_routes():
    text = APP.read_text(encoding="utf-8")
    for token in (
        "Start Here",
        "Research II",
        "Research III",
        "measurement-science.html",
        "visual-atlas.html",
    ):
        assert token in text
'''


PUBLIC_PUNCTUATION_TEST = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = (
    ROOT / "README.md",
    ROOT / "START_HERE.md",
    ROOT / "website/index.html",
    ROOT / "website/plain-language.html",
    ROOT / "website/start-here.html",
    ROOT / "website/research-map.html",
    ROOT / "website/measurement-science.html",
    ROOT / "website/research-lineage.html",
    ROOT / "website/sources.html",
)


def test_published_reader_surfaces_use_ascii_punctuation():
    for path in PUBLIC:
        text = path.read_text(encoding="utf-8")
        assert "—" not in text, path
        assert "–" not in text, path


def test_ascii_hyphenated_scientific_compounds_are_allowed():
    text = (ROOT / "website/measurement-science.html").read_text(encoding="utf-8")
    assert "machine-readable" in text
    assert "third-person" in text
    assert "measurement-science" in text
'''


def rewrite_reader_contract_tests() -> None:
    write("tests/test_readme_research_orientation.py", README_ORIENTATION_TEST)
    write("tests/test_main_page_visual_paper.py", MAIN_PAGE_VISUAL_TEST)
    write("tests/test_website_research_orientation.py", WEBSITE_ORIENTATION_TEST)
    write("tests/test_scholarly_provenance_surface.py", SCHOLARLY_TEST)
    write("tests/test_public_reader_layering.py", PUBLIC_LAYERING_TEST)
    write("tests/test_public_reader_punctuation.py", PUBLIC_PUNCTUATION_TEST)

    path = "tests/test_reader_experience.py"
    text = read(path)
    text = text.replace("test_first_reader_surfaces_match_p87_frontier", "test_first_reader_surfaces_match_p88_frontier")
    text = text.replace('assert "87 proposition-level results" in content', 'assert "88" in content')
    text = text.replace('assert "P87" in content', 'assert "P88" in content')
    text = text.replace('CURRENT_FRONTIER = "P87"', 'CURRENT_FRONTIER = "P88"')
    write(path, text)


def main() -> None:
    update_citation_metadata()
    update_detailed_record()
    repair_reproducibility_equations()
    update_p88_figure_status()
    update_figure_catalog()
    update_claim_source_matrix()
    update_sources_page()
    update_lineage_source()
    update_prepare_website_fixture_behavior()
    rewrite_reader_contract_tests()
    print("Modernized P88 publication metadata and reader contracts.")


if __name__ == "__main__":
    main()

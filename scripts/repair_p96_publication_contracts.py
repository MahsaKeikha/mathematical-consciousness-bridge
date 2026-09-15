"""Repair legacy publication contracts after promotion to Proposition 96.

This one-time migration updates reader surfaces whose contracts still encoded
P95 as current and narrows historical P92/P94 regression tests so they protect
history without forcing every first-reader surface to carry all old frontiers.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


# Complete chronological archive.
path = "docs/detailed_proposition_record.md"
text = read(path)
text = text.replace("Complete P1 to P95 chronology", "Complete P1 to P96 chronology")
text = text.replace("94 disconnected proposition-level results", "96 disconnected proposition-level results")
write(path, text)

# Glossary: P95 becomes the immediate predecessor and P96 owns current status.
path = "docs/glossary.md"
text = read(path)
text = text.replace(
    "The current public frontier is **P95**.",
    "The current public frontier is **P96**.",
)
text = text.replace(
    "## Current theorem frontier: P95",
    "## Immediate predecessor theorem frontier: P95",
)
if "## Current theorem frontier: P96" not in text:
    text += """

## Current theorem frontier: P96

**Pilot-selection information:** the information used to choose a finite regime plan before certification. P96 permits this selection rule to be arbitrarily complicated under its declared sample-separation assumptions.

**Frozen plan:** the selected number of regimes, regime definitions, declared dependence ranges, rational error budgets, and certification allocation are fixed before holdout statistics are inspected.

**Independent holdout certification:** certification information is independent of the pilot-selection information in the sense required by the conditional P96 theorem. An ordinary random split of one temporally dependent stream is not automatically such an independent holdout design.

**Selection-complexity alpha penalty:** under the P96 independent-holdout and frozen-plan assumptions, the pilot search itself requires no additional alpha spending. The cost is sample separation: pilot observations are not certification observations.

**P96 boundary:** same-data redesign, unrestricted within-regime drift, model acceptance under non-rejection, consciousness identification, nonphysicality, and completion of the physical-to-experiential bridge are not established.
"""
write(path, text)

# Implementation page: extend the target-model stage to P96 and route current links correctly.
path = "website/implementation.html"
text = read(path)
text = text.replace("Stage 06 · P73-P95", "Stage 06 · P73-P96")
text = text.replace("P73-P95 build a continuous chain", "P73-P96 build a continuous chain")
text = text.replace("index.html#p95-frontier", "index.html#p96-frontier")
text = text.replace("current P95 frontier", "current P96 frontier")
old = (
    "P89 removes the finite coefficient-radius and four-observable support restrictions "
    "entirely and closes the complete real linear parity-functional class on all eleven "
    "canonical parity coordinates with a matching exact optimum of 5/168 on the published witness."
)
new = old + (
    " P90-P92 move beyond that linear closure through nonlinear algebraic constraints, "
    "P93-P95 carry the witness into IID, finite-range dependent, and predeclared-regime "
    "finite-data rejection, and P96 permits pilot-selected regime plans when final "
    "certification uses a frozen plan and genuinely independent holdout information."
)
text = text.replace(old, new)
write(path, text)

# Research Map: all current ranges and direct audit routes advance together.
path = "website/research-map.html"
text = read(path)
text = text.replace("through Proposition 95.", "through Proposition 96.")
text = text.replace("Ninety-five results", "Ninety-six results")
for old_range, new_range in (
    ("P71-P95", "P71-P96"),
    ("P74-P95", "P74-P96"),
    ("P73-P95", "P73-P96"),
    ("P77-P95", "P77-P96"),
):
    text = text.replace(old_range, new_range)
text = text.replace("index.html#p95-frontier", "index.html#p96-frontier")
text = text.replace("current P95 frontier", "current P96 frontier")
text = text.replace(
    "and P95 adds predeclared drift-aware stratification with familywise error control.",
    "P95 adds predeclared drift-aware stratification with familywise error control, and P96 separates pilot-selected regime design from independent holdout certification.",
)
text = text.replace(
    "P94 extends that rejection gate to declared finite-range dependence under one common marginal law, and P95 adds predeclared regime-level drift handling without pooling.",
    "P94 extends that rejection gate to declared finite-range dependence under one common marginal law, P95 adds predeclared regime-level drift handling without pooling, and P96 permits pilot-selected regime plans under a frozen-plan independent-holdout design.",
)
if 'href="index.html#p96-frontier"' not in text:
    marker = "P96 equation provenance</a></p></section>"
    replacement = (
        'P96 equation provenance</a> · <a href="index.html#p96-frontier">'
        "Overview P96 frontier</a></p></section>"
    )
    if marker not in text:
        raise RuntimeError("P96 Research Map audit block not found")
    text = text.replace(marker, replacement, 1)
write(path, text)

# Sources page: make P96 the current theorem source and keep P95 as predecessor.
path = "website/sources.html"
text = read(path)
if 'id="p96-source"' not in text:
    marker = '<section id="p95-source">'
    if marker not in text:
        raise RuntimeError("P95 source insertion point not found")
    section = """<section id="p96-source"><div class="section-head"><p class="eyebrow">Current theorem source · P96</p><h2>Selection-valid holdout stratification</h2><p>P96 permits arbitrary pilot-data selection of a finite regime plan when that plan is frozen before a genuinely independent holdout sample is evaluated with the P95 familywise certificate. Conditional P95 validity and the tower property preserve the same unconditional failure bound without an extra alpha penalty for pilot-search complexity under the declared assumptions.</p></div><div class="source-grid"><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_96_selection_valid_holdout_stratification.md"><h3>Proposition 96</h3><p>Formal selection-valid theorem, assumptions, exact checkpoint, and scientific boundary.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/p96_equation_provenance.md"><h3>P96 provenance</h3><p>Separates standard sample-splitting, conditioning, union-bound, and tower-property logic from the repository-specific P92-P95 integration.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/src/consciousness_bridge/selection_valid_holdout_stratification.py"><h3>P96 implementation</h3><p>Executable frozen-plan guards, independent-holdout declaration, nested exact P95 certificate, and balanced sample accounting.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/tests/test_selection_valid_holdout_stratification.py"><h3>P96 exact tests</h3><p>Selection-valid rejection, unequal error budgets, holdout matching, frozen-plan guards, and 3645/3648 checkpoints.</p></a><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figures/p96_selection_valid_holdout_stratification.svg"><h3>P96 theorem figure</h3><p>Canonical selection-to-certification diagram in the 154-figure synchronized publication record.</p></a></div><div class="boundary"><p><strong>Scientific boundary:</strong> an ordinary random split of one dependent time series is not automatically an independent holdout design. Same-data redesign, within-regime drift, non-rejection as model acceptance, consciousness identification, nonphysicality, and the physical-to-experiential bridge remain outside the theorem.</p></div></section>

"""
    text = text.replace(marker, section + marker, 1)
text = text.replace(
    '<section id="p95-source"><div class="section-head"><p class="eyebrow">Current theorem source · P95</p>',
    '<section id="p95-source"><div class="section-head"><p class="eyebrow">Immediate predecessor theorem source · P95</p>',
    1,
)
text = text.replace(
    'docs/figures/p96_selection_valid_holdout_stratification.svg"><h3>P95 theorem figure</h3>',
    'docs/figures/p95_drift_aware_stratified_sign_coherence.svg"><h3>P95 theorem figure</h3>',
    1,
)
write(path, text)

# Historical P92 contract: preserve theorem/boundary without requiring all first-reader surfaces.
path = "tests/test_p92_reader_surface_coherence.py"
text = read(path)
old = '''def test_p92_reader_surfaces_preserve_scientific_boundary() -> None:
    for path in ("README.md", "website/index.html", "website/plain-language.html", "website/start-here.html", "website/research-map.html"):
        text = _read(path).lower()
        assert "p92" in text
        assert "physical-to-experiential bridge" in text
'''
new = '''def test_p92_historical_reader_surfaces_preserve_scientific_boundary() -> None:
    for path in (
        "docs/proposition_92_exact_global_mixed_prevalence_distance.md",
        "website/visual-atlas.html",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p92" in text
        assert "physical-to-experiential bridge" in text
'''
if old in text:
    text = text.replace(old, new)
elif "test_p92_historical_reader_surfaces_preserve_scientific_boundary" not in text:
    raise RuntimeError("P92 stale reader contract not found")
write(path, text)

# P94 is now historical below P95, while P96 is current.
path = "tests/test_p94_reader_surface_coherence.py"
text = read(path)
marker = "def test_p94_remains_visible_as_immediate_predecessor()"
if marker in text:
    start = text.index(marker)
    text = text[:start] + '''def test_p94_remains_visible_below_p95_and_p96() -> None:
    home = _read("website/index.html")
    atlas = _read("website/visual-atlas.html")
    plain = _read("website/plain-language.html")
    start = _read("website/start-here.html")
    research = _read("website/research-map.html")
    assert 'id="p94-frontier"' not in home
    assert atlas.index('id="p96-frontier"') < atlas.index('id="p95-frontier"') < atlas.index('id="p94-frontier"')
    assert "Previous theorem frontier · P94" in atlas
    assert 'id="p94-reader-frontier"' in plain
    assert 'id="p94-reader-frontier"' in start
    assert 'id="p94-research-map"' in research
    assert "96 results · current frontier P96" in plain
    assert "96 results · current frontier P96" in start


def test_p94_drift_boundary_is_preserved_on_historical_surfaces() -> None:
    for path in (
        "docs/proposition_94_finite_range_dependent_sign_coherence.md",
        "website/plain-language.html",
        "website/start-here.html",
        "website/research-map.html",
    ):
        text = _read(path).lower()
        assert "p94" in text
        assert "drift" in text
        assert "physical-to-experiential bridge" in text
'''
elif "test_p94_remains_visible_below_p95_and_p96" not in text:
    raise RuntimeError("P94 stale reader contract not found")
write(path, text)

print("[p96-repair] stale publication contracts repaired")

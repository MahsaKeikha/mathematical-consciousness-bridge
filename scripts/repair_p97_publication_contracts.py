"""Repair publication contracts uncovered by the P97 promotion audit.

This is one-time migration machinery. It updates surfaces whose contracts still
encoded P96, P95, or P94 as the active frontier after P97 became current.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


# Citation guide: publish one explicit machine-checkable current-frontier block.
path = "CITATION.md"
text = read(path)
text = text.replace("current documented frontier, P96", "current documented frontier, P97")
text = text.replace("Current documented theorem frontier: P96", "Current documented theorem frontier: P97")
text = text.replace("theorem frontier **P96**", "theorem frontier **P97**")
text = text.replace("P1 through P96 chronological theorem record", "P1 through P97 chronological theorem record")
if "## Current theorem frontier: P97" not in text:
    marker = "## DOI and archival status"
    block = """## Current theorem frontier: P97

The current documented theorem frontier is **P97**. P97 permits same-data post-inspection selection among a finite candidate family fixed before certification statistics are inspected. Each candidate receives an exact P95 familywise budget, and a second union bound across candidates makes the candidate certificates simultaneous. The formal package release remains **Version 0.82.0**.

P97 is a conditional model-rejection theorem. It does not validate newly generated post-inspection candidates, unrestricted search, model acceptance after non-rejection, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge.

"""
    if marker not in text:
        raise RuntimeError("citation insertion point not found")
    text = text.replace(marker, block + marker, 1)
write(path, text)

# Changelog: P97 is the unreleased theorem frontier while v0.82.0 stays formal.
path = "CHANGELOG.md"
text = read(path)
if not text.startswith("# Unreleased research frontier - P97\n"):
    entry = """# Unreleased research frontier - P97

## P97 simultaneous finite candidate-family selection frontier

- Added Proposition 97 as the same-data selection-valid complement to P96 independent-holdout certification.
- Fixed the complete finite candidate family before certification statistics are inspected and allowed arbitrary post-inspection selection only within that covered family.
- Nested exact P95 familywise certificates inside each candidate and applied a second union bound across candidate-level error budgets; no candidate-certificate independence assumption is required.
- Certified the balanced K=2, B=2, m=1, 95 percent crossing at 4045 observations per regime and first exact denominator-24 replication at 4056.
- Recorded balanced unique-observation totals 8090 and 8112 because candidate plans may reuse the same underlying certification observations.
- Preserved the boundary that newly generated post-inspection candidates, unrestricted search, within-regime drift, non-rejection as model acceptance, consciousness identification, nonphysicality, and bridge completion remain open.
- Kept formal release v0.82.0 separate from the advancing theorem frontier.

"""
    text = entry + text
write(path, text)

# Figure catalog: add the new source-controlled theorem visual and update counts.
path = "docs/figure_catalog.md"
text = read(path)
text = text.replace(
    "**Current catalog:** 154 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 79 proposition/theorem visuals, and 40 quantitative figures.",
    "**Current catalog:** 155 SVG figures: 17 architecture/conceptual visuals, 18 foundational quantum-physics visuals, 80 proposition/theorem visuals, and 40 quantitative figures.",
)
if "p97_simultaneous_candidate_family_selection.svg" not in text:
    text += """

## Current theorem frontier: P97

| Figure | What it shows and how to interpret it | Scientific status | Formal context |
| --- | --- | --- | --- |
| [P97 simultaneous finite candidate-family selection](figures/p97_simultaneous_candidate_family_selection.svg) | What this figure shows: a finite family of candidate regime plans is fixed before certification statistics are inspected; each candidate receives its own P95 familywise budget; a second union bound covers all candidate certificates simultaneously; the final candidate may then be chosen after inspection from the covered family. How to read it: move from predeclared candidates to candidate-wise certification and then to post-inspection selection. The balanced K=2, B=2, m=1 checkpoint is 4045 observations per regime, with first exact denominator-24 replication at 4056. | Conditional P97 theorem figure. It does not cover newly generated post-inspection candidates, unrestricted search, model acceptance, consciousness identification, nonphysicality, or completion of the physical-to-experiential bridge. | [Proposition 97](proposition_97_simultaneous_candidate_family_selection.md) |
"""
write(path, text)

# Research lineage: advance only the Research II frontier counters.
path = "website/research-lineage.html"
text = read(path)
text = text.replace(
    "<strong>96</strong><span>proposition-level results</span>",
    "<strong>97</strong><span>proposition-level results</span>",
)
text = text.replace(
    "<strong>P96</strong><span>current theorem frontier</span>",
    "<strong>P97</strong><span>current theorem frontier</span>",
)
write(path, text)

# Historical P96 links must not point to a removed home-page anchor.
path = "website/research-map.html"
text = read(path)
text = text.replace('href="index.html#p96-frontier"', 'href="visual-atlas.html#p96-frontier"')
write(path, text)

# The P96 roadmap had already named P97 as future work. Once P97 is closed, move
# that future placeholder forward rather than leaving P97 described as a candidate.
path = "docs/theorem_roadmap.md"
text = read(path)
text = text.replace("Any P97 candidate", "Any P98 candidate")
text = text.replace("Any P97 claim", "Any P98 claim")
text = text.replace("continuation beyond P96", "continuation beyond P97")
write(path, text)

print("[p97-repair] stale publication contracts repaired")

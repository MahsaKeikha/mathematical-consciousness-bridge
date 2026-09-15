"""Repair publication-history contracts after the P98 frontier promotion.

This script is temporary migration machinery. It runs after
``promote_p98_public_frontier.py`` and before canonical figure regeneration.
It preserves predecessor visibility while ensuring every surface that means
"current" names P98 rather than P97.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


# README: keep the immediate predecessor discoverable after the main frontier
# block is replaced by P98.
path = "README.md"
text = read(path)
if "### Immediate predecessor: P97" not in text:
    marker = "## Choose your path"
    predecessor = """### Immediate predecessor: P97

[P97: Simultaneous Finite Candidate-Family Selection](docs/proposition_97_simultaneous_candidate_family_selection.md) remains the immediate same-data selection predecessor to P98. P97 permits post-inspection choice only within a finite candidate family fixed before certification statistics are inspected and pays for that search through explicit multiplicity. P98 takes a different route by rotating genuinely independent certification blocks while enforcing own-fold exclusion.

"""
    text = text.replace(marker, predecessor + marker, 1)
write(path, text)

# Navigation: P97 must remain visible, but never retain a "Current frontier"
# label after P98 has been promoted.
path = "docs/research_navigation.md"
text = read(path)
text = text.replace(
    "**Current frontier:** [P97: Simultaneous Finite Candidate-Family Selection](proposition_97_simultaneous_candidate_family_selection.md)",
    "**Previous frontier:** [P97: Simultaneous Finite Candidate-Family Selection](proposition_97_simultaneous_candidate_family_selection.md)",
)
text = text.replace("P74 through P97", "P74 through P98")
text = text.replace("P71 through P97", "P71 through P98")
write(path, text)

# Research lineage: this page is validated independently from the overview.
path = "website/research-lineage.html"
text = read(path)
text = text.replace(
    "<strong>97</strong><span>proposition-level results</span>",
    "<strong>98</strong><span>proposition-level results</span>",
)
text = text.replace(
    "<strong>P97</strong><span>current theorem frontier</span>",
    "<strong>P98</strong><span>current theorem frontier</span>",
)
write(path, text)

# Research map: remove the final stale route into the old home frontier and
# state the P98 scientific boundary in the wording required by the generic
# publication contract.
path = "website/research-map.html"
text = read(path)
text = text.replace("index.html#p97-frontier", "index.html#p98-frontier")
text = text.replace(
    "P97 remains a conditional model-rejection theorem under its declared pilot-selection, frozen-plan, and independent-holdout assumptions.",
    "P98 remains a conditional model-rejection theorem under its declared independent-block, own-fold-exclusion, frozen-plan, and exact error-budget assumptions.",
)
write(path, text)

print("[p98-repair] predecessor history and current-frontier contracts repaired")

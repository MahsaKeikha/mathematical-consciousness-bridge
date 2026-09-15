"""One-time repair of P97 reader-navigation language after PR validation."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text.rstrip() + "\n", encoding="utf-8")


# Start Here must expose the generic current-frontier navigation contract.
path = "website/start-here.html"
text = read(path)
for old, new in (
    ("current Research II P96 frontier", "current Research II P97 frontier"),
    ("Open all 96 Research II results", "Open all 97 Research II results"),
    ("The 96 propositions are the formal theorem record of Research II.", "The 97 propositions are the formal theorem record of Research II."),
    ("P1-P96 build the mathematical conditions", "P1-P97 build the mathematical conditions"),
    ("P75-P96 test the declared target-measurement model itself", "P75-P97 test the declared target-measurement model itself"),
    ("<span>P75-P96</span>", "<span>P75-P97</span>"),
    ("P78-P96 develop certified nonlinear separation, dependence control, and drift-aware stratification", "P78-P97 develop certified nonlinear separation, dependence control, and selection-valid certification"),
    ("The 96 results form", "The 97 results form"),
    ("You do not need to read 93 Research II proofs in order", "You do not need to read 97 Research II proofs in order"),
    ("complete 93-result Research II dependency structure", "complete 97-result Research II dependency structure"),
    ("P19 and P71-P93", "P19 and P71-P97"),
    ("P74-P91", "P74-P97"),
    ("Research II · Immediate predecessor · P95", "Research II · Historical drift-aware frontier · P95"),
    ("Research II · Immediate predecessor · P94", "Research II · Historical finite-range frontier · P94"),
):
    text = text.replace(old, new)

p97_start = text.index('id="p97-reader-frontier"')
p97_end = text.index("</section>", p97_start)
p97_block = text[p97_start:p97_end]
if "Read P97 theorem" not in p97_block:
    link = '<p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_97_simultaneous_candidate_family_selection.md">Read P97 theorem</a></p>'
    text = text[:p97_end] + link + text[p97_end:]
write(path, text)

# Plain Language must state the generic current-frontier sentences used by deployment CI.
path = "website/plain-language.html"
text = read(path)
for old, new in (
    ("This is the 96-result Research II theorem program currently reaching P96.", "This is the 97-result Research II theorem program currently reaching P97."),
    ("The current theorem frontier is P96.", "The current theorem frontier is P97."),
    ("A 95-result sufficiency and falsification architecture", "A 97-result sufficiency and falsification architecture"),
    ("currently through P95", "currently through P97"),
    ("The 93-result proposition program", "The 97-result proposition program"),
    ("current theorem frontier is P96", "current theorem frontier is P97"),
    ("P75-P96", "P75-P97"),
):
    text = text.replace(old, new)
write(path, text)

print("[p97-reader-repair] current-frontier navigation synchronized")

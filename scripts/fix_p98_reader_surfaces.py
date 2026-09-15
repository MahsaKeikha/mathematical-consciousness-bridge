"""Synchronize reader-facing website surfaces with the P98 theorem frontier.

Temporary migration helper. The workflow that invokes this script removes both
this file and itself before committing the final reader-surface state.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


# Start Here: advance all reader counts/ranges and replace the stale P93-era
# certified-frontier narrative with the full P92-P98 chain.
path = "website/start-here.html"
text = read(path)
for old, new in {
    "The 97 propositions are the formal theorem record of Research II.": "The 98 propositions are the formal theorem record of Research II.",
    "P1-P97 build the mathematical conditions": "P1-P98 build the mathematical conditions",
    "P75-P97 test the declared target-measurement model itself": "P75-P98 test the declared target-measurement model itself",
    "<span>P75-P97</span>": "<span>P75-P98</span>",
    "<h2>P78-P97 develop certified nonlinear separation, dependence control, and selection-valid certification</h2>": "<h2>P78-P98 develop certified nonlinear separation, dependence control, and selection-valid certification</h2>",
    "You do not need to read 97 Research II proofs in order": "You do not need to read 98 Research II proofs in order",
    "Focus on P19 and P71-P97, then the falsification program.": "Focus on P19 and P71-P98, then the falsification program.",
    "P47-P60, and P74-P97.": "P47-P60, and P74-P98.",
}.items():
    text = text.replace(old, new)

section_lines = [
    '    <section class="dark-section">',
    '      <p class="eyebrow">Research II · Current certified frontier</p>',
    '      <h2>P92-P98 connect exact population separation to dependence-aware, selection-valid certification</h2>',
    '      <p><strong>P92 closes the mixed-prevalence population distance exactly.</strong> Three selected determinant signs imply the exact full-cube distance <strong>d_inf(P_emp, M75) = 1/24</strong>.</p>',
    '      <p><strong>P93 carries that obstruction into finite IID data.</strong> A simultaneous seven-cell confidence event yields the 95 percent mathematical crossing at 1623 samples, with the first exact 24-count replication clearing at 1632.</p>',
    '      <p><strong>P94 allows a declared finite dependence range.</strong> The same sign-coherence witness remains certifiable under an m-dependent stream with one common marginal law, while an exact counterexample shows why arbitrary temporal drift cannot simply be pooled away.</p>',
    '      <p><strong>P95 handles declared drift by stratification.</strong> Predeclared regimes receive local finite-range certificates and one familywise error budget, allowing their marginal laws to differ without pretending the pooled stream is stationary.</p>',
    '      <p><strong>P96 separates adaptive plan selection from final certification.</strong> Pilot information may choose the regime plan, but that plan must be frozen before a genuinely independent holdout sample is inspected.</p>',
    '      <p><strong>P97 permits same-data selection inside one predeclared finite candidate family.</strong> It pays explicitly for the search through simultaneous candidate-level error accounting.</p>',
    '      <p><strong>P98 is the current frontier.</strong> It rotates the P96 holdout principle across mutually independent data blocks. In fold k, the plan may use the other blocks, but block k is excluded from its own plan-selection rule and is inspected only after that plan is frozen. The final fold certificates may be dependent because their selection information overlaps; one outer union bound controls them simultaneously.</p>',
    '      <p><strong>Exact P98 checkpoint:</strong> for two folds, two one-step-dependent regimes per fold, and 95 percent global confidence, the crossing is <strong>4045 observations per regime</strong>, the first exact denominator-24 replication is <strong>4056</strong>, and the two-fold unique-data totals are <strong>16180 / 16224</strong>.</p>',
    '      <p>The logical direction remains one-sided. These results can reject the declared P75 model family under their assumptions. They do not validate the model after non-rejection, identify consciousness, establish nonphysicality, or close the physical-to-experiential bridge.</p>',
    '      <div class="hero-actions">',
    '        <a class="button primary" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">Read P98 theorem</a>',
    '        <a class="button" href="visual-atlas.html">See theorem visuals</a>',
    '        <a class="button" href="implementation.html#stage-06">See the implementation path</a>',
    '      </div>',
    '    </section>',
]
current_section = "\n".join(section_lines)
text, count = re.subn(
    r'    <section class="dark-section">.*?    </section>',
    current_section,
    text,
    count=1,
    flags=re.DOTALL,
)
if count != 1:
    raise RuntimeError(f"expected one Start Here dark-section replacement, got {count}")

if "Read P98 theorem" not in text:
    raise RuntimeError("Start Here failed to receive the P98 theorem link")
write(path, text)

# Plain Language: advance all global counts/ranges and preserve the explicit P98
# frontier section already introduced by the promotion.
path = "website/plain-language.html"
text = read(path)
for old, new in {
    "This is the 97-result Research II theorem program currently reaching P97.": "This is the 98-result Research II theorem program currently reaching P98.",
    "A 97-result sufficiency and falsification architecture": "A 98-result sufficiency and falsification architecture",
    "currently through P97.": "currently through P98.",
    "The current theorem frontier is P97.": "The current theorem frontier is P98.",
    "P1-P97": "P1-P98",
    "P75-P97": "P75-P98",
    "P71-P97": "P71-P98",
    "P74-P97": "P74-P98",
    "97 Research II": "98 Research II",
}.items():
    text = text.replace(old, new)

if 'id="p98-reader-frontier"' not in text:
    raise RuntimeError("Plain Language lost the P98 reader-frontier section")
if "Read P98 theorem" not in text:
    anchor = "</section>\n\n<section class=\"boundary\" id=\"p97-reader-frontier\">"
    link = '<p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_98_cross_fitted_selection_valid_certification.md">Read P98 theorem</a></p>\n</section>\n\n<section class="boundary" id="p97-reader-frontier">'
    if anchor not in text:
        raise RuntimeError("could not place Plain Language P98 theorem link")
    text = text.replace(anchor, link, 1)
write(path, text)

# Exact migration assertions used by normal repository CI.
start = read("website/start-here.html")
plain = read("website/plain-language.html")
for surface in (start, plain):
    assert "98 results · current frontier P98" in surface
    assert 'id="p98-reader-frontier"' in surface
assert "Read P98 theorem" in start
assert "You do not need to read 98 Research II proofs in order" in start
assert "P75-P98" in start
assert "This is the 98-result Research II theorem program currently reaching P98." in plain
assert "The current theorem frontier is P98." in plain

print("[p98-reader-fix] Start Here and Plain Language synchronized to P98")

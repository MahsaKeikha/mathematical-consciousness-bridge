from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_required(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f"missing expected text: {old}")
    return text.replace(old, new)


# Plain-language reader surface.
path = "website/plain-language.html"
text = read(path)
text = text.replace(
    "This is the 90-result Research II theorem program currently reaching P89.",
    "This is the 90-result Research II theorem program currently reaching P90.",
)
text = text.replace(
    "Research II develops exact and finite-data tests for representation, scale, target provenance, model adequacy, and physical-description sufficiency, currently through P89.",
    "Research II develops exact and finite-data tests for representation, scale, target provenance, model adequacy, and physical-description sufficiency, currently through P90.",
)
text = text.replace(
    "The current theorem frontier is P89.",
    "The current theorem frontier is P90.",
)
old_block = '''<section class="boundary" id="p89-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current exact frontier · P89</p><h2>Complete linear parity-functional duality</h2><p>P89 removes P88's finite coefficient-radius and four-observable support restrictions. Across all real linear combinations of all eleven canonical parity coordinates, the strict exact-rational witness has <strong>L88 = 1/64 &lt; L89 = 5/168</strong>, and a matching universal upper certificate proves that 5/168 is the exact complete-linear optimum on that box.</p><p>This closes the declared linear parity-functional class only. It does not replace Research I or Research III, exhaust nonlinear P75 constraints, or close the physical-to-experiential bridge.</p></div></section>'''
new_block = '''<section class="boundary" id="p90-reader-frontier"><div class="section-head"><p class="eyebrow">Research II · Current exact frontier · P90</p><h2>Exact nonlinear rank-one slice separation</h2><p>P90 moves beyond the complete P89 linear parity-functional envelope by exploiting a nonlinear identity of the declared strict P75 model image. With prevalence fixed at zero, the active law is one product Bernoulli component, so the canonical two-by-two slice must satisfy <strong>ad = bc</strong>. The empirical determinant residual is <strong>5/192</strong>, giving the exact distance <strong>L90 = 5/72 = (7/3)L89</strong>, while P89 remains the complete-linear subfrontier at <strong>5/168</strong>.</p><p>This is a conditional exact separation result for the stated strict box. It does not identify consciousness, establish nonphysicality, exhaust more general nonlinear mixture regimes, or close the physical-to-experiential bridge.</p></div></section>'''
text = replace_required(text, old_block, new_block)
write(path, text)

# Start Here reader surface.
path = "website/start-here.html"
text = read(path)
text = text.replace(
    "current Research II P89 frontier",
    "current Research II P90 frontier",
)
text = text.replace(
    "Open all 89 Research II results",
    "Open all 90 Research II results",
)
text = text.replace(
    "<h2>P78-P89 progressively tighten global separation from the declared continuous model family</h2>",
    "<h2>P78-P90 progressively tighten global separation from the declared continuous model family</h2>",
)
anchor = '''      <p><strong>P89 closes the complete real linear parity-functional class.</strong> <strong>P89 is the current complete-linear frontier.</strong> It removes both the finite coefficient-radius restriction and the exactly-four-observable support restriction. Across every real linear functional of all eleven canonical P83 parity coordinates, matching exact lower and upper certificates prove <strong>L89 = 5/168</strong>, strictly above <strong>L88 = 1/64</strong>.</p>'''
addition = anchor + '''\n      <p><strong>P90 moves beyond that complete linear envelope.</strong> On the strict P75 box, prevalence is fixed at zero, so the active observable law is a single product Bernoulli component and a canonical two-by-two slice must satisfy <strong>ad = bc</strong>. The empirical determinant residual gives a lower radius of <strong>5/72</strong>, and an explicit rational P75 point attains the same full-law distance. Thus <strong>L90 = 5/72 = (7/3)L89</strong>.</p>'''
if "P90 moves beyond that complete linear envelope." not in text:
    text = replace_required(text, anchor, addition)
text = text.replace(
    "docs/proposition_89_complete_linear_parity_duality.md\">Read P89 theorem",
    "docs/proposition_90_exact_nonlinear_rank_one_separation.md\">Read P90 theorem",
)
write(path, text)

# Permanent promoter must recreate the same state idempotently.
path = "scripts/promote_p90_public_frontier.py"
text = read(path)
needle = '''def promote_website() -> None:\n'''
if needle not in text:
    raise RuntimeError("promote_website anchor missing")
# Add exact reader-surface replacements once inside promote_website.
marker = '    path = "website/plain-language.html"\n'
if marker not in text:
    insert = '''    path = "website/plain-language.html"\n    text = read(path)\n    text = text.replace("This is the 90-result Research II theorem program currently reaching P89.", "This is the 90-result Research II theorem program currently reaching P90.")\n    text = text.replace("currently through P89.", "currently through P90.")\n    text = text.replace("The current theorem frontier is P89.", "The current theorem frontier is P90.")\n    text = text.replace('id="p89-reader-frontier"', 'id="p90-reader-frontier"')\n    text = text.replace("Research II · Current exact frontier · P89", "Research II · Current exact frontier · P90")\n    text = text.replace("Complete linear parity-functional duality", "Exact nonlinear rank-one slice separation", 1 if 'id="p90-reader-frontier"' in text else 0)\n    write(path, text)\n\n    path = "website/start-here.html"\n    text = read(path)\n    text = text.replace("current Research II P89 frontier", "current Research II P90 frontier")\n    text = text.replace("Open all 89 Research II results", "Open all 90 Research II results")\n    text = text.replace("P78-P89 progressively tighten global separation", "P78-P90 progressively tighten global separation")\n    text = text.replace('docs/proposition_89_complete_linear_parity_duality.md">Read P89 theorem', 'docs/proposition_90_exact_nonlinear_rank_one_separation.md">Read P90 theorem')\n    write(path, text)\n\n'''
    text = text.replace(needle, needle + insert, 1)
write(path, text)

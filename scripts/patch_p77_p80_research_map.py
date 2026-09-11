from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website" / "research-map.html"
WORKFLOW = ROOT / ".github" / "workflows" / "patch-p77-p80-research-map.yml"
SELF = Path(__file__)

text = MAP.read_text(encoding="utf-8")

text = text.replace(
    "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 76.",
    "Scientific dependency map of the Mathematical Consciousness Bridge through Proposition 80.",
    1,
)

old_lede = (
    "P71-P80 return to the P19 bridge-sufficiency lineage after the P61-P70 calibration branch: "
    "P71 protects target provenance, P72 protects the target-observation interface, P73 identifies "
    "target channels under one explicit latent model, P74 asks when finite data are strong enough to "
    "certify that recovery, P75 asks whether the measurement model itself survives independent adequacy "
    "checks, and P76 asks whether finite data can certify an adequacy violation beyond sampling noise."
)
new_lede = (
    "P71-P80 return to the P19 bridge-sufficiency lineage after the P61-P70 calibration branch: "
    "P71 protects target provenance, P72 protects the target-observation interface, P73 identifies "
    "target channels under one explicit latent model, P74 certifies finite-data recovery, P75 introduces "
    "independent model-adequacy restrictions, P76 turns those restrictions into finite-sample rejection "
    "tests, P77 lifts rejection to the complete declared model set, P78 certifies continuous-family "
    "distance lower bounds, P79 certifies the sampling-radius upper bound, and P80 tightens the continuous "
    "lower bound by enforcing probability normalization inside each parameter-box relaxation."
)
if old_lede in text:
    text = text.replace(old_lede, new_lede, 1)

p79_anchor = '<section><div class="section-head"><p class="eyebrow">IV-I · Certified sampling radius</p><h2>P79: Certified rational sampling-radius envelope</h2>'
if p79_anchor not in text:
    raise SystemExit("P79 research-map anchor not found")

p77_p78 = '''<section><div class="section-head"><p class="eyebrow">IV-G · Full-law model-set separation</p><h2>P77: When does the entire confidence region miss the declared model family?</h2></div><div class="result-grid"><article class="result"><span>P77</span><h3>Full-law rejection criterion</h3><p>P77 strengthens necessary-constraint rejection to the complete sixteen-cell observed law. A rejection is certified only when the simultaneous empirical-law confidence region is separated from the complete declared P75 model set, or when a sound lower bound on empirical model distance exceeds the same sampling radius.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p77_full_law_model_set_separation.svg" alt="P77 full-law model-set separation"/><div><h3>P77 full-law separation</h3><p>Best-fit candidates provide upper bounds on distance and cannot by themselves certify rejection. The certificate requires a lower bound with the correct inequality direction.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_77_full_law_model_set_separation.md">Read Proposition 77</a></div></div></section>

<section><div class="section-head"><p class="eyebrow">IV-H · Certified continuous-family separation</p><h2>P78: How is P77 made rigorous for the continuous P75 family?</h2></div><div class="result-grid"><article class="result"><span>P78</span><h3>Exact parameter-box lower bounds</h3><p>P78 exploits the nine-parameter multi-affine structure of the P75 family. Exact-rational cell intervals on each parameter box produce rigorous lower bounds on L-infinity distance to the complete continuous model image, while explicit admissible parameter points provide upper bounds and mesh refinement controls convergence.</p></article></div><div class="figure-card"><img src="https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures/p78_certified_continuous_model_separation.svg" alt="P78 certified continuous model separation"/><div><h3>P78 continuous-family certificate</h3><p>The key direction is one-sided: only the certified global lower bound can feed the P77 rejection gate.</p><a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_78_certified_continuous_model_separation.md">Read Proposition 78</a></div></div></section>

'''
if "IV-G · Full-law model-set separation" not in text:
    text = text.replace(p79_anchor, p77_p78 + p79_anchor, 1)

# Remove the older out-of-order standalone P78 section now that P77-P80 are presented sequentially.
old_p78_start = '<section class="boundary">\n      <h2>P78: Certified continuous P75 model separation</h2>'
if old_p78_start in text:
    start = text.index(old_p78_start)
    end = text.index("</section>", start) + len("</section>")
    text = text[:start] + text[end:]

MAP.write_text(text, encoding="utf-8")

# This is a one-shot publication repair. Remove the helper and workflow before the bot commits.
if SELF.exists():
    SELF.unlink()
if WORKFLOW.exists():
    WORKFLOW.unlink()

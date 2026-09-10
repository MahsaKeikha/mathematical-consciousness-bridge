from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / "website/research-map.html"

text = MAP.read_text(encoding="utf-8")
marker = '<section>\n<div class="section-head"><p class="eyebrow">I · Formal bridge foundations</p>'
if text.count(marker) != 1:
    raise RuntimeError("expected one stage-I insertion marker")

orientation = '''<section class="boundary" id="orientation">
  <div class="section-head">
    <p class="eyebrow">Reader orientation</p>
    <h2>How to read this research</h2>
    <p>This program is easier to follow by scientific function than by proposition number alone. Read the seven stages from top to bottom if you want the logic of the full program. Open an individual proposition only when you want its assumptions, proof, implementation, tests, and figure.</p>
  </div>
  <div class="status-grid" aria-label="Scientific status">
    <div><strong>70</strong><span>proposition-level results</span></div>
    <div><strong>Proved results</strong><span>mathematical conclusions under stated assumptions</span></div>
    <div><strong>Conditional results</strong><span>claims that depend on declared models or regularity classes</span></div>
    <div><strong>Open bridge target</strong><span>no physical-to-experiential law is assumed solved</span></div>
  </div>
  <h3>Seven-stage scientific path</h3>
  <div class="result-grid">
    <article class="result"><span>1 · P1-P10</span><h3>Foundations</h3><p>Define invariance, identifiability, equivalence, recovery, and finite-data testability.</p></article>
    <article class="result"><span>2 · P11-P18</span><h3>Structured physical candidates</h3><p>Build causal, temporal, compositional, and scale-aware physical structure.</p></article>
    <article class="result"><span>3 · P19-P24</span><h3>Bridge sufficiency tests</h3><p>Test factorization and nonfactorization with finite-data and repeated-look validity.</p></article>
    <article class="result"><span>4 · P25-P37</span><h3>Operational scale</h3><p>Track which physical structures survive coarse-graining and quotient operations.</p></article>
    <article class="result"><span>5 · P38-P44</span><h3>Quantum interface</h3><p>State what quantum operational descriptions can support and what still requires an explicit bridge class.</p></article>
    <article class="result"><span>6 · P45-P53</span><h3>Adaptive evidence acquisition</h3><p>Allocate samples, protect validity, and derive stopping and service guarantees.</p></article>
    <article class="result"><span>7 · P54-P70</span><h3>Execution and calibration</h3><p>Optimize switching, noisy transition measurement, heterogeneous calibration, and certificate diagnostics.</p></article>
  </div>
  <div class="source-grid">
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/theorem_roadmap.md"><h3>Dependency map</h3><p>Follow theorem prerequisites and proposition lineage.</p></a>
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/research_navigation.md"><h3>Question-based navigation</h3><p>Enter through the scientific problem rather than proposition order.</p></a>
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/equation_and_citation_map.md"><h3>Equation and citation map</h3><p>Audit mathematical provenance, evidence roles, and repository-original results.</p></a>
    <a href="visual-atlas.html"><h3>Visual atlas</h3><p>Inspect the major diagrams before reading long proofs.</p></a>
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/tree/main/src/consciousness_bridge/"><h3>Source implementation</h3><p>Inspect the executable theorem interfaces and numerical routines.</p></a>
    <a href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/tree/main/tests/"><h3>Regression tests</h3><p>Check theorem guards, geometry guards, publication integrity, and reproducibility.</p></a>
  </div>
  <p><strong>Reading rule:</strong> later propositions may refine, quantify, or operationalize earlier ones, but they do not silently strengthen an open scientific claim. Optimization results remain optimization results. Quantum operational results remain conditional on their declared physical and bridge assumptions. The physical-to-experiential bridge remains open.</p>
</section>
'''

text = text.replace(marker, orientation + marker, 1)
MAP.write_text(text, encoding="utf-8")

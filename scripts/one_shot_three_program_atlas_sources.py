from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEBSITE = ROOT / "website"
TESTS = ROOT / "tests"

R1 = "https://github.com/MahsaKeikha/spatiotemporal-observer-math"
R1_RAW = "https://raw.githubusercontent.com/MahsaKeikha/spatiotemporal-observer-math/main/docs"
R2 = "https://github.com/MahsaKeikha/mathematical-consciousness-bridge"
R2_RAW = "https://raw.githubusercontent.com/MahsaKeikha/mathematical-consciousness-bridge/main/docs/figures"
R3 = "https://github.com/MahsaKeikha/consciousness-measurement-science"
R3_RAW = "https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/main/docs/figures"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def update_visual_atlas() -> None:
    path = WEBSITE / "visual-atlas.html"
    text = path.read_text(encoding="utf-8")

    text = replace_once(
        text,
        '<meta name="description" content="Visual atlas for the Mathematical Consciousness Bridge research program."/>',
        '<meta name="description" content="Three-program visual atlas for Research I physical-system identification, Research II bridge sufficiency and falsification, and Research III consciousness measurement science."/>',
        "visual atlas meta description",
    )
    text = replace_once(
        text,
        '<h1>Figures as navigational aids to the mathematics</h1><p class="lede">The figures below are selected entry points into the formal record. They are diagrams, quantitative illustrations, or computational visualizations. They do not replace proofs, and each should be read together with its theorem, assumptions, and provenance.</p><div class="hero-actions"><a class="button primary" href="#p100-frontier">Current P100 frontier</a><a class="button" href="#p99-frontier">Follow frontier history</a><a class="button" href="research-map.html#continuous-model-frontier">Read P77-P100 chronologically</a><a class="button" href="https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/figure_catalog.md">Complete figure catalog</a></div>',
        '<h1>Three research programs, one visual evidence record</h1><p class="lede">This atlas now presents the visual record of all three connected programs. Research I shows physical-subsystem identification and world-tube recovery. Research II shows bridge sufficiency, falsification, and the P1-P100 theorem record. Research III shows the measurement-science architecture, phenomenal-structure program, and claim discipline. Each figure keeps its own scientific status and boundary.</p><div class="hero-actions"><a class="button primary" href="#research-i-visual-program">Research I visuals</a><a class="button" href="#research-ii-visual-program">Research II visuals</a><a class="button" href="#research-iii-visual-program">Research III visuals</a><a class="button" href="sources.html">Sources and reproducibility</a></div>',
        "visual atlas hero",
    )

    old_rule = '<p><strong>Reading order:</strong> this atlas is intentionally current-first. P100 appears first, followed by P99 and the earlier P98-P86 theorem frontiers in descending historical order. For the chronological scientific progression, use the <a href="research-map.html#continuous-model-frontier">P77-P100 Research Map sequence</a>.</p>'
    new_rule = '<p><strong>Global reading order:</strong> this page is organized by research program: Research I, Research II, then Research III. Within Research II, the detailed frontier archive is intentionally current-first. P100 appears first, followed by P99 and earlier retained theorem frontiers. For the chronological Research II progression, use the <a href="research-map.html#continuous-model-frontier">P77-P100 Research Map sequence</a>. Research I and Research III retain their own evidence status rather than being forced into the Research II proposition numbering scheme.</p>'
    text = replace_once(text, old_rule, new_rule, "atlas reading rule")

    marker = "\n<!-- current-frontier-visual: P100 -->"
    if "id=\"research-i-visual-program\"" in text:
        raise RuntimeError("three-program visual sections already present")

    block = f'''
<section id="three-program-visual-index" class="three-program-index">
  <div class="section-head">
    <p class="eyebrow">The complete visual program</p>
    <h2>Research I, Research II, and Research III answer different questions and carry different evidence status</h2>
    <p>The three programs are connected, but they are not interchangeable. Research I identifies the physical subsystem. Research II tests whether a declared physical description is sufficient for an independently specified target. Research III develops the measurement architecture needed to state what observable evidence can justify about experiential targets.</p>
  </div>
  <div class="three-program-index-grid">
    <a class="program-index-card" href="#research-i-visual-program"><span>Research I</span><strong>Physical-system identification</strong><small>58 results, 45 experiments, 33 scientific result figures</small></a>
    <a class="program-index-card" href="#research-ii-visual-program"><span>Research II</span><strong>Bridge sufficiency and falsification</strong><small>100 results, 158 canonical figures, current frontier P100</small></a>
    <a class="program-index-card" href="#research-iii-visual-program"><span>Research III</span><strong>Consciousness measurement science</strong><small>5 targets, 2 research arms, M0-M7 claim ladder</small></a>
  </div>
</section>

<section id="research-i-visual-program" class="program-overview-section" data-program="research-i">
  <div class="section-head">
    <p class="eyebrow">Research I · Spatiotemporal Observer Mathematics</p>
    <h2>Visual record of physical subsystem identification</h2>
    <p>Research I asks whether a moving physical subsystem can be inferred from stochastic dynamics rather than having its boundary fixed in advance. The visual record follows world-tube recovery, finite-data certification, temporal calibration, innovation inference, and the return from covariance uncertainty to the observer-scale moving-boundary problem.</p>
  </div>
  <div class="program-record-grid" aria-label="Research I record">
    <div class="program-record-metric"><strong>58</strong><span>proposition-level results</span></div>
    <div class="program-record-metric"><strong>45</strong><span>reproducible experiments</span></div>
    <div class="program-record-metric"><strong>33</strong><span>scientific result figures</span></div>
    <div class="program-record-metric"><strong>223</strong><span>claim-level tests</span></div>
  </div>
  <div class="program-visual-grid">
    <a class="program-visual-card" href="{R1}/blob/main/docs/physics_guide.md">
      <img loading="lazy" decoding="async" src="{R1_RAW}/physics_pipeline.svg" alt="Research I physics to inference pipeline" />
      <span>Research I architecture</span><h3>Physics to inference pipeline</h3><p>Measured physical observables flow into stochastic dynamics, candidate moving boundaries, world-tube optimization, finite-data certification, and interpretation.</p>
    </a>
    <a class="program-visual-card" href="{R1}/blob/main/docs/reproducible_results.md">
      <img loading="lazy" decoding="async" src="{R1_RAW}/worldtube_baseline.png" alt="Research I baseline moving world-tube recovery" />
      <span>Moving-boundary recovery</span><h3>Baseline world-tube recovery</h3><p>The recovered path shows how a coherent physical subsystem can be tracked even when the coordinates representing it change through time.</p>
    </a>
    <a class="program-visual-card" href="{R1}/blob/main/docs/proposition_58_observer_bridge.md">
      <img loading="lazy" decoding="async" src="{R1_RAW}/observer_bridge_dimension_audit.svg" alt="Research I Proposition 58 observer-scale covariance to world-tube audit" />
      <span>Current Research I frontier</span><h3>P58 observer-scale dimension audit</h3><p>The current bottleneck is observer-scale dimension and structural propagation of covariance uncertainty, not scalar physical-time calibration.</p>
    </a>
  </div>
  <div class="program-actions">
    <a href="{R1}/blob/main/docs/visual_research_guide.md">Open all Research I figures</a>
    <a href="{R1}/blob/main/docs/research_index.md">Research I result index</a>
    <a href="{R1}/blob/main/docs/reproducible_results.md">Reproducible results</a>
  </div>
  <div class="boundary"><p><strong>Research I boundary:</strong> recovering or certifying a physical world-tube identifies a candidate physical subsystem. It does not by itself identify that subsystem as a conscious subject.</p></div>
</section>

<section id="research-ii-visual-program" class="program-overview-section" data-program="research-ii">
  <div class="section-head">
    <p class="eyebrow">Research II · Mathematical Consciousness Bridge</p>
    <h2>Visual record of bridge sufficiency, falsification, and certified inference</h2>
    <p>Research II asks whether a declared physical or computational description is sufficient for an independently specified target. Its visual record spans the P1-P100 theorem program, target and measurement audits, model-family separation, finite-data certification, adaptive selection protection, and anytime-valid evidence accumulation.</p>
  </div>
  <div class="program-record-grid" aria-label="Research II record">
    <div class="program-record-metric"><strong>100</strong><span>proposition-level results</span></div>
    <div class="program-record-metric"><strong>158</strong><span>canonical figures</span></div>
    <div class="program-record-metric"><strong>P100</strong><span>current theorem frontier</span></div>
    <div class="program-record-metric"><strong>Open</strong><span>physical-to-experiential bridge</span></div>
  </div>
  <div class="program-visual-grid">
    <a class="program-visual-card" href="{R2}/blob/main/docs/theorem_roadmap.md">
      <img loading="lazy" decoding="async" src="{R2_RAW}/theorem_roadmap.svg" alt="Research II complete P1-P100 theorem roadmap" />
      <span>Complete Research II map</span><h3>P1-P100 theorem roadmap</h3><p>The roadmap separates the core bridge lineage from connected physical, quantum, scheduling, and calibration branches while showing every proposition through P100.</p>
    </a>
    <a class="program-visual-card" href="{R2}/blob/main/docs/proposition_100_anytime_sequential_eprocess.md">
      <img loading="lazy" decoding="async" src="{R2_RAW}/p100_anytime_sequential_eprocess.svg" alt="Research II P100 anytime-valid sequential e-process" />
      <span>Current Research II frontier</span><h3>P100 anytime-valid sequential evidence</h3><p>The current endpoint carries protected P99 evidence across fresh certification rounds while retaining validity under adaptive stopping.</p>
    </a>
    <a class="program-visual-card" href="{R2}/blob/main/docs/figure_catalog.md">
      <img loading="lazy" decoding="async" src="{R2_RAW}/equation_evidence_map.svg" alt="Research II equation evidence map" />
      <span>Complete visual catalog</span><h3>158 canonical Research II figures</h3><p>The figure catalog links conceptual, quantitative, quantum, and proposition-level visuals to their theorem and provenance context.</p>
    </a>
  </div>
  <div class="program-actions">
    <a href="#research-ii-frontier-archive">Open the detailed Research II frontier archive</a>
    <a href="research-map.html">Read Research II chronologically</a>
    <a href="sources.html#complete-source-sequence">Audit all P1-P100 theorem sources</a>
  </div>
  <div class="boundary"><p><strong>Research II boundary:</strong> rejection is relative to the declared descriptor, target, model family, and assumptions. A rejected descriptor does not prove nonphysical consciousness, and a model that survives the tests is not thereby established as the true theory of consciousness.</p></div>
</section>

<section id="research-iii-visual-program" class="program-overview-section" data-program="research-iii">
  <div class="section-head">
    <p class="eyebrow">Research III · Consciousness Measurement Science</p>
    <h2>Visual record of the measurement-science architecture</h2>
    <p>Research III asks what observable reports, behavior, neural activity, perturbational responses, physiology, interventions, and context can justify about declared experiential targets. Its current status is a foundational research program and computational scaffold, not an empirically or clinically validated consciousness instrument.</p>
  </div>
  <div class="program-record-grid" aria-label="Research III program">
    <div class="program-record-metric"><strong>5</strong><span>declared measurement targets</span></div>
    <div class="program-record-metric"><strong>2</strong><span>research arms</span></div>
    <div class="program-record-metric"><strong>M0-M7</strong><span>claim ladder</span></div>
    <div class="program-record-metric"><strong>4</strong><span>auditable software scaffold components</span></div>
  </div>
  <div class="program-visual-grid">
    <a class="program-visual-card" href="{R3}/blob/main/docs/measurement-framework.md">
      <img loading="lazy" decoding="async" src="{R3_RAW}/measurement_architecture.svg" alt="Research III consciousness measurement architecture" />
      <span>Measurement architecture</span><h3>Observable evidence to declared experiential targets</h3><p>The architecture makes target, evidence model, assumptions, uncertainty, and allowed claim level explicit instead of hiding the bridge inside one score.</p>
    </a>
    <a class="program-visual-card" href="{R3}/blob/main/docs/phenomenal-structure.md">
      <img loading="lazy" decoding="async" src="{R3_RAW}/structural_measurement_pipeline.svg" alt="Research III phenomenal structural measurement pipeline" />
      <span>Research arm B</span><h3>Phenomenal-structure measurement</h3><p>Experiential and physical relational spaces are compared through preregistered mappings and distortion statistics without assuming ontological identity.</p>
    </a>
    <a class="program-visual-card" href="{R3}/blob/main/docs/claim-registry.md">
      <img loading="lazy" decoding="async" src="{R3_RAW}/claim_ladder.svg" alt="Research III M0-M7 measurement claim ladder" />
      <span>Claim discipline</span><h3>M0-M7 evidence ladder</h3><p>The ladder separates signal differences, prediction, generalization, causal support, latent-target identification, structural prediction, and unique theory tests.</p>
    </a>
  </div>
  <div class="program-actions">
    <a href="{R3}/blob/main/docs/README.md">Research III documentation map</a>
    <a href="{R3}/blob/main/docs/experimental-program.md">Experimental program</a>
    <a href="{R3}/blob/main/docs/reproducibility.md">Reproducibility standard</a>
  </div>
  <div class="boundary"><p><strong>Research III boundary:</strong> specification and computational scaffolding are not empirical validation, external validation, clinical validation, or direct third-person measurement of qualia. Inconclusive and partially identified outcomes remain legitimate scientific results.</p></div>
</section>

<section id="research-ii-frontier-archive" class="research-program-divider">
  <div class="section-head"><p class="eyebrow">Research II · Detailed visual archive</p><h2>Current frontier first, followed by retained historical theorem frontiers</h2><p>The detailed archive below belongs specifically to Research II. It preserves the current-first P100, P99, P98 and earlier retained-frontier presentation, while the Research Map provides the chronological theorem reading path.</p></div>
</section>
'''
    if marker not in text:
        raise RuntimeError("visual atlas P100 marker not found")
    text = text.replace(marker, "\n" + block + marker, 1)
    path.write_text(text, encoding="utf-8")


def update_sources() -> None:
    path = WEBSITE / "sources.html"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        '<meta name="description" content="Sources, provenance, citations, and reproducibility for the Mathematical Consciousness Bridge."/>',
        '<meta name="description" content="Sources, provenance, citations, figures, and reproducibility across Research I, Research II, and Research III."/>',
        "sources meta description",
    )
    text = replace_once(
        text,
        '<h1>A complete source path from P1 through P100</h1>\n  <p class="lede">Start with the ordered theorem source sequence below. Every proposition is visible once, in numeric order, grouped by scientific stage, and linked directly to its canonical proof record. The rest of this page explains provenance, reproducibility, and the richer audit bundles behind the latest theorem family.</p>',
        '<h1>Sources, provenance, and reproducibility across all three research programs</h1>\n  <p class="lede">Research I, Research II, and Research III have different kinds of records, so this page keeps them distinct while making every audit path easy to reach. Research I exposes its physical-system results, experiments, figures, tests, and assumptions. Research II retains the complete P1-P100 theorem source sequence. Research III exposes its measurement specifications, epistemic boundaries, statistical framework, software scaffold, and reproducibility requirements.</p>',
        "sources hero",
    )
    old_status = '''  <div class="status-grid" aria-label="Theorem source sequence status">
    <div><strong>100</strong><span>ordered proposition records</span></div>
    <div><strong>P1-P100</strong><span>continuous numeric source path</span></div>
    <div><strong>P100</strong><span>current theorem frontier</span></div>
    <div><strong>Open</strong><span>physical-to-experiential bridge</span></div>
  </div>'''
    new_status = '''  <div class="hero-actions">
    <a class="button primary" href="#research-i-source-program">Research I sources</a>
    <a class="button" href="#research-ii-source-program">Research II sources</a>
    <a class="button" href="#research-iii-source-program">Research III sources</a>
    <a class="button" href="#complete-source-sequence">P1-P100 sequence</a>
  </div>
  <div class="status-grid" aria-label="Three-program source record">
    <div><strong>Research I</strong><span>58 results · 45 experiments · 33 result figures · 223 tests</span></div>
    <div><strong>Research II</strong><span>100 results · 158 figures · current frontier P100</span></div>
    <div><strong>Research III</strong><span>foundational measurement-science specification and scaffold</span></div>
    <div><strong>Open</strong><span>physical-to-experiential bridge</span></div>
  </div>'''
    text = replace_once(text, old_status, new_status, "sources status grid")

    marker = "\n<!-- BEGIN COMPLETE SOURCE SEQUENCE -->"
    if "id=\"research-i-source-program\"" in text:
        raise RuntimeError("three-program source sections already present")
    block = f'''
<section id="three-program-source-index" class="three-program-index">
  <div class="section-head"><p class="eyebrow">Three source records</p><h2>Audit each research program according to the kind of evidence it actually contains</h2><p>The programs share a scientific lineage but not one uniform result type. Research I has proposition-level physical-system results and experiments. Research II has the P1-P100 theorem program. Research III is presently a foundational measurement-science specification and computational scaffold whose empirical validation program is explicitly still ahead.</p></div>
  <div class="three-program-index-grid">
    <a class="program-index-card" href="#research-i-source-program"><span>Research I</span><strong>Physical-system sources</strong><small>Results, experiments, figures, assumptions, and reproducibility</small></a>
    <a class="program-index-card" href="#research-ii-source-program"><span>Research II</span><strong>Bridge theorem sources</strong><small>P1-P100 proofs, figures, code, tests, and equation provenance</small></a>
    <a class="program-index-card" href="#research-iii-source-program"><span>Research III</span><strong>Measurement-science sources</strong><small>Specifications, epistemic boundaries, statistics, schemas, and scaffold</small></a>
  </div>
</section>

<section id="research-i-source-program" class="program-overview-section program-source-section" data-program="research-i">
  <div class="section-head"><p class="eyebrow">Research I · Source and reproducibility record</p><h2>Spatiotemporal Observer Mathematics</h2><p>Research I records a physical-system identification program with 58 proposition-level results, 45 reproducible experiments, 33 scientific result figures, and 223 claim-level tests. Its source trail separates mathematical assumptions, physical interpretation, reproducible experiments, and the current observer-scale bottleneck.</p></div>
  <div class="program-record-grid" aria-label="Research I source record">
    <div class="program-record-metric"><strong>58</strong><span>proposition-level results</span></div><div class="program-record-metric"><strong>45</strong><span>reproducible experiments</span></div><div class="program-record-metric"><strong>33</strong><span>scientific result figures</span></div><div class="program-record-metric"><strong>223</strong><span>claim-level tests</span></div>
  </div>
  <div class="program-source-grid">
    <a class="program-source-card" href="{R1}/blob/main/docs/research_index.md"><span>Result index</span><h3>Research I theorem and experiment record</h3><p>Follow the formal result sequence and its associated experiments.</p></a>
    <a class="program-source-card" href="{R1}/blob/main/docs/visual_research_guide.md"><span>Visual record</span><h3>33-figure visual research guide</h3><p>Browse the scientific result figures and their interpretation boundaries.</p></a>
    <a class="program-source-card" href="{R1}/blob/main/docs/physics_mathematics_citation_map.md"><span>Equation provenance</span><h3>Physics and mathematics citation map</h3><p>Trace mathematical tools, physical meaning, and source lineage.</p></a>
    <a class="program-source-card" href="{R1}/blob/main/docs/assumption_ledger.md"><span>Assumptions</span><h3>Assumption ledger</h3><p>Audit which physical and statistical assumptions each certification requires.</p></a>
    <a class="program-source-card" href="{R1}/blob/main/docs/reproducible_results.md"><span>Reproducibility</span><h3>Reproducible experimental results</h3><p>Inspect recorded computational outputs and validation experiments.</p></a>
    <a class="program-source-card" href="{R1}/blob/main/docs/proposition_58_observer_bridge.md"><span>Current frontier</span><h3>P58 observer-scale bridge audit</h3><p>Inspect the current dimension and covariance-uncertainty bottleneck.</p></a>
  </div>
  <div class="boundary"><p><strong>Research I source boundary:</strong> this record supports physical subsystem identification claims under stated assumptions. It does not independently establish that the recovered subsystem is a conscious subject.</p></div>
</section>

<section id="research-ii-source-program" class="program-overview-section program-source-section" data-program="research-ii">
  <div class="section-head"><p class="eyebrow">Research II · Source and reproducibility record</p><h2>Mathematical Consciousness Bridge</h2><p>Research II contains the 100-result P1-P100 proposition record and 158 canonical figures. The full ordered theorem sequence remains below this section, while the links here provide the shortest routes to the dependency map, figure inventory, machine-readable manifest, code tests, and reproducibility contract.</p></div>
  <div class="program-record-grid" aria-label="Research II source record"><div class="program-record-metric"><strong>100</strong><span>proposition-level results</span></div><div class="program-record-metric"><strong>158</strong><span>canonical figures</span></div><div class="program-record-metric"><strong>P100</strong><span>current theorem frontier</span></div><div class="program-record-metric"><strong>Open</strong><span>physical-to-experiential bridge</span></div></div>
  <div class="program-source-grid">
    <a class="program-source-card" href="#complete-source-sequence"><span>Complete proof path</span><h3>P1-P100 theorem source sequence</h3><p>Follow every Research II proposition once, in numeric order.</p></a>
    <a class="program-source-card" href="{R2}/blob/main/docs/theorem_roadmap.md"><span>Dependency map</span><h3>Complete theorem roadmap</h3><p>Distinguish development order from scientific dependency across P1-P100.</p></a>
    <a class="program-source-card" href="{R2}/blob/main/docs/figure_catalog.md"><span>Visual provenance</span><h3>Complete figure catalog</h3><p>Link each conceptual, quantitative, quantum, and theorem visual to its context.</p></a>
    <a class="program-source-card" href="{R2}/blob/main/figures/manifest.json"><span>Machine-readable record</span><h3>Figure manifest</h3><p>Inspect the canonical figure count, hashes, titles, and current frontier.</p></a>
    <a class="program-source-card" href="{R2}/tree/main/tests"><span>Verification</span><h3>Research II test suite</h3><p>Audit theorem, publication, website, and reproducibility regression contracts.</p></a>
    <a class="program-source-card" href="{R2}/blob/main/docs/reproducibility.md"><span>Reproducibility</span><h3>Research II reproducibility guide</h3><p>Rebuild the current theorem and publication record from the declared environment.</p></a>
  </div>
  <div class="boundary"><p><strong>Research II source boundary:</strong> traceability makes the declared theorem program auditable. It does not turn model rejection into proof of nonphysical consciousness or model compatibility into theory confirmation.</p></div>
</section>

<section id="research-iii-source-program" class="program-overview-section program-source-section" data-program="research-iii">
  <div class="section-head"><p class="eyebrow">Research III · Source and reproducibility record</p><h2>Consciousness Measurement Science</h2><p>Research III is presently a foundational measurement-science program and computational scaffold. Its source record is therefore organized around specifications, epistemic boundaries, target definitions, statistical identification, theory falsification, machine-readable claims, and reproducibility rather than around a completed theorem-frontier sequence.</p></div>
  <div class="program-record-grid" aria-label="Research III source record"><div class="program-record-metric"><strong>5</strong><span>declared targets</span></div><div class="program-record-metric"><strong>2</strong><span>research arms</span></div><div class="program-record-metric"><strong>M0-M7</strong><span>claim ladder</span></div><div class="program-record-metric"><strong>4</strong><span>software scaffold components</span></div></div>
  <div class="program-source-grid">
    <a class="program-source-card" href="{R3}/blob/main/docs/README.md"><span>Documentation map</span><h3>Complete Research III reading path</h3><p>Navigate orientation, measurement specification, experiments, statistics, theory comparison, translation, and implementation.</p></a>
    <a class="program-source-card" href="{R3}/blob/main/docs/epistemic-boundaries.md"><span>Epistemic boundary</span><h3>What observable evidence can and cannot establish</h3><p>Separate first-person access, third-person evidence, report, causation, and theory neutrality.</p></a>
    <a class="program-source-card" href="{R3}/blob/main/docs/measurement-framework.md"><span>Measurement specification</span><h3>Formal measurement framework</h3><p>Define targets, evidence, identification regions, causal tests, and allowed outputs.</p></a>
    <a class="program-source-card" href="{R3}/blob/main/docs/assumption-registry.md"><span>Assumptions</span><h3>Assumption registry</h3><p>Make the conditions required for each measurement inference explicit and auditable.</p></a>
    <a class="program-source-card" href="{R3}/blob/main/docs/statistical-validation.md"><span>Statistics</span><h3>Statistical validation plan</h3><p>Track calibration, transport, uncertainty, multiplicity, abstention, and external validation.</p></a>
    <a class="program-source-card" href="{R3}/blob/main/docs/partial-identification.md"><span>Identification</span><h3>Dependence-robust partial identification</h3><p>Use bounds and sensitivity analysis when the latent target is not point identified.</p></a>
    <a class="program-source-card" href="{R3}/blob/main/docs/phenomenal-structure.md"><span>Structural arm</span><h3>Phenomenal-structure program</h3><p>Compare experiential and neural relational structures without assuming identity.</p></a>
    <a class="program-source-card" href="{R3}/blob/main/docs/falsification-matrix.md"><span>Theory comparison</span><h3>Falsification matrix</h3><p>Record what would count against tested versions of competing theory families.</p></a>
    <a class="program-source-card" href="{R3}/blob/main/docs/reproducibility.md"><span>Reproducibility</span><h3>Research III reproducibility contract</h3><p>Preserve data lineage, preprocessing freeze, confirmatory splits, claim provenance, and release artifacts.</p></a>
    <a class="program-source-card" href="{R3}/tree/main/schemas"><span>Machine-readable record</span><h3>CEP and claim schemas</h3><p>Inspect machine-readable structures for measurement profiles and scientific claims.</p></a>
  </div>
  <div class="boundary"><p><strong>Research III source boundary:</strong> specification and software scaffolding are not empirical evidence, external validation, clinical validation, or direct measurement of qualia. The program explicitly permits uncertainty, partial identification, abstention, and inconclusive results.</p></div>
</section>
'''
    if marker not in text:
        raise RuntimeError("complete source sequence marker not found")
    text = text.replace(marker, "\n" + block + marker, 1)
    text = replace_once(
        text,
        '<p class="eyebrow">Complete theorem source sequence</p>\n    <h2>Follow every theorem source from P1 through P100 in order</h2>\n    <p>This is the continuous source path for the full proposition record. Every proposition appears exactly once in numeric order, with its title, scientific object, status, and a direct link to the canonical proof document. Group headings keep the sequence readable without hiding any proposition inside a range summary.</p>',
        '<p class="eyebrow">Research II · Complete theorem source sequence</p>\n    <h2>Research II: follow every theorem source from P1 through P100 in order</h2>\n    <p>This is the continuous source path for the full Research II proposition record. Every proposition appears exactly once in numeric order, with its title, scientific object, status, and a direct link to the canonical proof document. Research I and Research III use their own source structures above because their scientific objects and evidence status are different.</p>',
        "Research II source sequence heading",
    )
    path.write_text(text, encoding="utf-8")


def update_orientation() -> None:
    path = WEBSITE / "research-orientation.js"
    text = path.read_text(encoding="utf-8")
    old_atlas = '''    'visual-atlas.html': {
      stage: 'Visual evidence record',
      question: 'What does the current theorem frontier look like, and how do the historical figures support the development of the research?',
      established:
        'The Atlas presents P100 as the current visual frontier, P99 as its immediate predecessor, and earlier retained frontier figures as historical theorem records. It is intentionally current-first rather than chronological.',
      open:
        'A figure is an audit surface for a declared result, not independent proof of an experiential interpretation. Scientific meaning still comes from the theorem assumptions, proof record, computation, and tests.',
      links: [
        ['#p100-frontier', 'Jump to the current P100 visual frontier'],
        ['research-map.html', 'Follow the chronological theorem sequence'],
        ['sources.html', 'Audit provenance and reproducibility'],
      ],
    },'''
    new_atlas = '''    'visual-atlas.html': {
      stage: 'Three-program visual evidence record',
      question: 'What visual evidence, architecture, or computational record belongs to Research I, Research II, and Research III, and what scientific status does each visual carry?',
      established:
        'The Atlas now separates Research I physical-system visuals, Research II theorem and frontier visuals, and Research III measurement-science architecture. Within Research II, P100 remains the current visual frontier and the detailed archive remains current-first.',
      open:
        'A figure does not upgrade the status of its underlying evidence. Research I world-tube recovery is not consciousness identification, Research II model rejection is not bridge completion, and Research III specification is not empirical or clinical validation.',
      links: [
        ['#research-i-visual-program', 'Open Research I visuals'],
        ['#research-ii-visual-program', 'Open Research II visuals'],
        ['#research-iii-visual-program', 'Open Research III visuals'],
      ],
    },'''
    text = replace_once(text, old_atlas, new_atlas, "visual orientation contract")
    old_sources = '''    'sources.html': {
      stage: 'Provenance and reproducibility',
      question: 'Where do the equations, references, implementations, tests, and figure records come from, and how can a reader audit them?',
      established:
        'The source layer connects public claims to proposition records, equation provenance, implementations, tests, figure manifests, and cited literature so the research trail can be independently inspected.',
      open:
        'Traceability is necessary for rigor but does not make a scientific claim true by itself. Assumptions, derivations, numerical checks, and empirical relevance still require substantive evaluation.',
      links: [
        [REPO, 'Open the complete repository'],
        [`${REPO}/tree/main/tests`, 'Inspect the test suite'],
        [`${REPO}/blob/main/figures/manifest.json`, 'Inspect the figure manifest'],
      ],
    },'''
    new_sources = '''    'sources.html': {
      stage: 'Three-program provenance and reproducibility',
      question: 'Where do the formal results, experiments, figures, specifications, assumptions, code, tests, and reproducibility records for all three research programs live?',
      established:
        'The source page now separates Research I physical-system provenance, Research II P1-P100 theorem provenance, and Research III measurement-science specification and scaffold provenance while preserving direct audit paths for each program.',
      open:
        'Traceability establishes an inspectable research record, not scientific truth. Each program still has to earn its own mathematical, computational, empirical, external-validation, or clinical claims at the level appropriate to that program.',
      links: [
        ['#research-i-source-program', 'Audit Research I'],
        ['#research-ii-source-program', 'Audit Research II'],
        ['#research-iii-source-program', 'Audit Research III'],
      ],
    },'''
    text = replace_once(text, old_sources, new_sources, "sources orientation contract")
    path.write_text(text, encoding="utf-8")


def update_styles() -> None:
    path = WEBSITE / "styles.css"
    text = path.read_text(encoding="utf-8")
    marker = "/* three-program-atlas-sources */"
    if marker in text:
        return
    addition = r'''

/* three-program-atlas-sources */
.three-program-index,
.program-overview-section,
.research-program-divider {
  max-width: var(--max);
  margin: 0 auto;
  padding: 64px 24px;
}

.three-program-index {
  padding-top: 42px;
  padding-bottom: 30px;
}

.three-program-index-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
}

.program-index-card,
.program-visual-card,
.program-source-card {
  position: relative;
  display: block;
  color: var(--ink);
  text-decoration: none !important;
  border: 1px solid var(--line);
  border-radius: 17px;
  background: var(--paper);
  box-shadow: 0 10px 28px rgba(20, 26, 36, 0.055);
  transition: transform 150ms ease, border-color 150ms ease, box-shadow 150ms ease;
}

.program-index-card {
  min-height: 150px;
  padding: 21px 22px 48px;
}

.program-index-card span,
.program-visual-card > span,
.program-source-card > span {
  display: block;
  margin-bottom: 7px;
  color: var(--accent2);
  font-size: 0.71rem;
  font-weight: 780;
  letter-spacing: 0.055em;
  text-transform: uppercase;
}

.program-index-card strong {
  display: block;
  margin-bottom: 7px;
  font-family: var(--font-display);
  font-size: 1.22rem;
  line-height: 1.2;
}

.program-index-card small {
  color: var(--muted);
  line-height: 1.5;
}

.program-index-card::after,
.program-visual-card::after,
.program-source-card::after {
  content: 'Open record →';
  position: absolute;
  right: 18px;
  bottom: 16px;
  color: var(--accent);
  font-size: 0.78rem;
  font-weight: 740;
}

.program-index-card:hover,
.program-index-card:focus-visible,
.program-visual-card:hover,
.program-visual-card:focus-visible,
.program-source-card:hover,
.program-source-card:focus-visible {
  transform: translateY(-2px);
  border-color: #8f9db7;
  box-shadow: 0 14px 36px rgba(20, 26, 36, 0.1);
  outline: none;
}

.program-overview-section + .program-overview-section {
  border-top: 1px solid var(--line);
}

.program-record-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 10px;
  margin: 22px 0 28px;
}

.program-record-metric {
  min-height: 102px;
  padding: 16px 17px;
  border: 1px solid var(--line);
  border-radius: 13px;
  background: var(--soft);
}

.program-record-metric strong,
.program-record-metric span {
  display: block;
}

.program-record-metric strong {
  margin-bottom: 5px;
  color: var(--accent);
  font-size: 1.25rem;
  line-height: 1.1;
}

.program-record-metric span {
  color: var(--muted);
  font-size: 0.84rem;
  line-height: 1.4;
}

.program-visual-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 15px;
}

.program-visual-card {
  overflow: hidden;
  padding: 0 18px 52px;
}

.program-visual-card img {
  display: block;
  width: calc(100% + 36px);
  height: 230px;
  margin: 0 -18px 18px;
  object-fit: contain;
  background: #f7f9fc;
  border-bottom: 1px solid var(--line);
}

.program-visual-card h3,
.program-source-card h3 {
  margin: 0 0 8px;
  font-size: 1.08rem;
  line-height: 1.28;
}

.program-visual-card p,
.program-source-card p {
  margin: 0;
  color: var(--muted);
  font-size: 0.91rem;
  line-height: 1.55;
}

.program-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  margin: 22px 0;
}

.program-actions a {
  padding: 9px 12px;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--paper);
  font-size: 0.85rem;
  font-weight: 680;
  text-decoration: none;
}

.program-source-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  margin: 22px 0;
}

.program-source-card {
  min-height: 188px;
  padding: 20px 20px 50px;
}

.research-program-divider {
  padding-top: 52px;
  padding-bottom: 22px;
  border-top: 1px solid var(--line);
}

@media (max-width: 900px) {
  .three-program-index-grid,
  .program-visual-grid,
  .program-source-grid {
    grid-template-columns: 1fr;
  }

  .program-record-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .program-visual-card img {
    height: auto;
    max-height: 440px;
  }
}

@media (max-width: 520px) {
  .program-record-grid {
    grid-template-columns: 1fr;
  }

  .three-program-index,
  .program-overview-section,
  .research-program-divider {
    padding-left: 18px;
    padding-right: 18px;
  }
}
'''
    path.write_text(text.rstrip() + addition + "\n", encoding="utf-8")


def update_existing_test() -> None:
    path = TESTS / "test_visual_atlas_frontier_hierarchy.py"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        'assert "this atlas is intentionally current-first" in atlas',
        'assert "Within Research II, the detailed frontier archive is intentionally current-first" in atlas',
        "visual atlas current-first test",
    )
    path.write_text(text, encoding="utf-8")


def write_new_test() -> None:
    path = TESTS / "test_three_program_atlas_sources.py"
    content = '''from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_visual_atlas_has_all_three_programs_with_distinct_status() -> None:
    atlas = _read("website/visual-atlas.html")

    for section_id in (
        "research-i-visual-program",
        "research-ii-visual-program",
        "research-iii-visual-program",
        "research-ii-frontier-archive",
    ):
        assert f'id="{section_id}"' in atlas

    assert "58" in atlas and "45" in atlas and "33" in atlas and "223" in atlas
    assert "100" in atlas and "158" in atlas and "P100" in atlas
    assert "5" in atlas and "M0-M7" in atlas and "4" in atlas
    assert "foundational research program and computational scaffold" in atlas
    assert "not an empirically or clinically validated consciousness instrument" in atlas
    assert "physical world-tube" in atlas
    assert "does not by itself identify that subsystem as a conscious subject" in atlas


def test_visual_atlas_uses_canonical_figures_from_all_three_programs() -> None:
    atlas = _read("website/visual-atlas.html")

    for figure in (
        "physics_pipeline.svg",
        "worldtube_baseline.png",
        "observer_bridge_dimension_audit.svg",
        "theorem_roadmap.svg",
        "p100_anytime_sequential_eprocess.svg",
        "equation_evidence_map.svg",
        "measurement_architecture.svg",
        "structural_measurement_pipeline.svg",
        "claim_ladder.svg",
    ):
        assert figure in atlas

    assert atlas.count('class="program-visual-card"') == 9
    assert atlas.index('id="research-i-visual-program"') < atlas.index('id="research-ii-visual-program"')
    assert atlas.index('id="research-ii-visual-program"') < atlas.index('id="research-iii-visual-program"')
    assert atlas.index('id="research-iii-visual-program"') < atlas.index('id="research-ii-frontier-archive"')
    assert atlas.index('id="p100-frontier"') < atlas.index('id="p99-frontier"')


def test_sources_has_three_program_audit_sections_before_research_two_sequence() -> None:
    sources = _read("website/sources.html")

    for section_id in (
        "research-i-source-program",
        "research-ii-source-program",
        "research-iii-source-program",
        "complete-source-sequence",
    ):
        assert f'id="{section_id}"' in sources

    assert sources.index('id="research-i-source-program"') < sources.index('id="research-ii-source-program"')
    assert sources.index('id="research-ii-source-program"') < sources.index('id="research-iii-source-program"')
    assert sources.index('id="research-iii-source-program"') < sources.index('id="complete-source-sequence"')
    assert "Research II · Complete theorem source sequence" in sources
    assert "full Research II proposition record" in sources
    assert 'data-proposition="P1"' in sources
    assert 'data-proposition="P100"' in sources


def test_sources_links_each_program_to_its_real_audit_record() -> None:
    sources = _read("website/sources.html")

    for token in (
        "spatiotemporal-observer-math/blob/main/docs/research_index.md",
        "spatiotemporal-observer-math/blob/main/docs/assumption_ledger.md",
        "spatiotemporal-observer-math/blob/main/docs/proposition_58_observer_bridge.md",
        "mathematical-consciousness-bridge/blob/main/docs/theorem_roadmap.md",
        "mathematical-consciousness-bridge/blob/main/figures/manifest.json",
        "mathematical-consciousness-bridge/tree/main/tests",
        "consciousness-measurement-science/blob/main/docs/epistemic-boundaries.md",
        "consciousness-measurement-science/blob/main/docs/measurement-framework.md",
        "consciousness-measurement-science/blob/main/docs/statistical-validation.md",
        "consciousness-measurement-science/blob/main/docs/reproducibility.md",
        "consciousness-measurement-science/tree/main/schemas",
    ):
        assert token in sources

    assert sources.count('class="program-source-card"') == 22
    assert "specification and software scaffolding are not empirical evidence" in sources
    assert "external validation" in sources
    assert "clinical validation" in sources


def test_sitewide_orientation_describes_atlas_and_sources_as_three_program_surfaces() -> None:
    orientation = _read("website/research-orientation.js")

    assert "Three-program visual evidence record" in orientation
    assert "Research I physical-system visuals" in orientation
    assert "Research II theorem and frontier visuals" in orientation
    assert "Research III measurement-science architecture" in orientation
    assert "Three-program provenance and reproducibility" in orientation
    assert "Research I physical-system provenance" in orientation
    assert "Research II P1-P100 theorem provenance" in orientation
    assert "Research III measurement-science specification and scaffold provenance" in orientation


def test_three_program_cards_are_native_links_and_static_metrics_do_not_mimic_links() -> None:
    atlas = _read("website/visual-atlas.html")
    sources = _read("website/sources.html")
    css = _read("website/styles.css")

    assert atlas.count('<a class="program-index-card"') == 3
    assert sources.count('<a class="program-index-card"') == 3
    assert atlas.count('<a class="program-visual-card"') == 9
    assert sources.count('<a class="program-source-card"') == 22
    assert ".program-record-metric" in css
    assert ".program-visual-card::after" in css
    assert ".program-source-card::after" in css
    assert "Open record" in css


def test_three_program_reader_surfaces_respect_dash_policy() -> None:
    for path in (
        "website/visual-atlas.html",
        "website/sources.html",
        "website/research-orientation.js",
        "website/styles.css",
    ):
        text = _read(path)
        assert "\\u2013" not in text
        assert "\\u2014" not in text
'''
    path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    update_visual_atlas()
    update_sources()
    update_orientation()
    update_styles()
    update_existing_test()
    write_new_test()

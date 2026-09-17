(() => {
  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';
  const OBSERVER_REPO = 'https://github.com/MahsaKeikha/spatiotemporal-observer-math';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const MEASUREMENT_PIN = 'a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee';

  const PAGE_CONTRACTS = {
    'index.html': {
      stage: 'Whole program',
      question: 'How do the three research programs fit together, and where is the current formal frontier?',
      established:
        'The site documents a three-stage program: physical-system identification in Research I, bridge sufficiency and falsification through P100 in Research II, and a V1-V10 formal measurement-validation program in Research III.',
      open:
        'The physical-to-experiential bridge remains open. The overview organizes the mathematical, computational, and measurement-science evidence but does not add a new bridge principle or experiential identification claim.',
      links: [
        ['research-lineage.html', 'See the three-stage scientific handoff'],
        ['research-map.html', 'Audit the Research II theorem map'],
        ['measurement-science.html', 'Open Research III V1-V10'],
      ],
    },
    'plain-language.html': {
      stage: 'Reader translation',
      question: 'What is the research actually claiming in language that does not require reading the proofs first?',
      established:
        'The page translates the formal distinctions among physical description, independent target, compatibility, rejection, measurement assumptions, uncertainty, and validation without changing the underlying claims.',
      open:
        'A simpler explanation is not a weaker scientific boundary. Compatibility is not validation, rejection of one descriptor is not proof of nonphysical consciousness, and the final bridge remains unresolved.',
      links: [
        ['start-here.html', 'Move from intuition to the formal reading path'],
        ['research-map.html', 'Check the formal Research II record'],
        ['measurement-science.html', 'See the Research III measurement tests'],
      ],
    },
    'start-here.html': {
      stage: 'First-reader guide',
      question: 'What should a new reader understand before entering the proposition chronology and measurement program?',
      established:
        'The reading path fixes the project vocabulary, the sufficiency question, the interpretation boundary, and the relationship among Research I, II, and III before proposition-level or validation-stage detail begins.',
      open:
        'The guide does not identify consciousness with a latent variable, physical descriptor, observer subsystem, or measurement channel. Those identifications require independent scientific justification.',
      links: [
        ['#chain', 'Follow the inference chain'],
        ['research-map.html', 'Open all 100 Research II results'],
        ['measurement-science.html', 'Open Research III formal validation'],
      ],
    },
    'observer-research.html': {
      stage: 'Research I',
      question: 'Which physical subsystem is being followed through changing stochastic dynamics and time?',
      established:
        'Research I develops and tests a moving-boundary observer mathematics for identifying a persistent physical world-tube under explicit identifiability and finite-data conditions.',
      open:
        'A recovered physical world-tube is not automatically a conscious subject. Research I identifies a physical subsystem candidate and deliberately stops before the experiential bridge claim.',
      links: [
        [OBSERVER_REPO, 'Open the Research I repository'],
        ['research-lineage.html', 'See how Research I hands off to Research II'],
        ['research-map.html', 'Continue to bridge sufficiency testing'],
      ],
    },
    'research-lineage.html': {
      stage: 'Scientific handoff',
      question: 'Which conclusions pass from Research I to II to III, and which assumptions must be re-tested at each handoff?',
      established:
        'The lineage separates physical-system identification, bridge sufficiency testing, and measurement science so outputs from one stage are not silently promoted into conclusions belonging to another. Research III now adds V1-V10 formal validation of its measurement machinery.',
      open:
        'No handoff by itself establishes the physical-to-experiential bridge. The bridge requires an independently justified principle and empirical support beyond stage-to-stage bookkeeping.',
      links: [
        ['observer-research.html', 'Inspect Research I'],
        ['research-map.html', 'Inspect Research II'],
        ['measurement-science.html', 'Inspect Research III V1-V10'],
      ],
    },
    'research-map.html': {
      stage: 'Research II',
      question: 'When is a declared physical or computational description sufficient for an independently specified target, and how can that claim be falsified?',
      established:
        'Research II records 100 proposition-level results through P100, including exact sufficiency conditions, target and measurement audits, model-family separation, finite-data certification, adaptive analysis protection, and anytime-valid sequential evidence.',
      open:
        'Rejecting a declared descriptor or model family does not show that no richer physical description can work. Surviving the tests also does not establish that the surviving model is the true theory of consciousness.',
      links: [
        [`${REPO}/blob/main/docs/theorem_roadmap.md`, 'Open the formal theorem roadmap'],
        ['visual-atlas.html', 'Inspect the visual evidence record'],
        ['measurement-science.html', 'Continue to Research III measurement science'],
      ],
    },
    'measurement-science.html': {
      stage: 'Research III',
      question: 'What can observable channels legitimately identify about a declared experiential target, and exactly where does that inference fail?',
      established:
        'Research III now contains a reproducible V1-V10 formal validation program covering calibrated inversion, partial identification, finite-sample coverage, transport bias, channel dependence, structural null and power testing, finite calibration uncertainty, arbitrary missingness, inverse conditioning, site heterogeneity, and principled abstention.',
      open:
        'These analytic and synthetic results validate measurement machinery under declared models. They do not establish empirical calibration for consciousness in humans or other systems, and principled non-identification remains an allowed result.',
      links: [
        [`${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/VALIDATION.md`, 'Open the V1-V10 validation program'],
        [`${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/docs/validation-atlas.md`, 'Open the validation atlas'],
        [`${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/results/README.md`, 'Audit machine-readable results'],
      ],
    },
    'physics-mathematics.html': {
      stage: 'Foundations',
      question: 'Which mathematical and physical structures are used by the bridge-testing and measurement programs, and exactly where do their assumptions enter?',
      established:
        'This page organizes the physical, probabilistic, information-theoretic, causal, statistical, and quantum tools used to state and test the Research II claims and interpret the Research III measurement program.',
      open:
        'Mathematical consistency inside a chosen framework does not by itself supply an experiential interpretation. The foundations constrain bridge claims but do not manufacture the missing bridge principle.',
      links: [
        ['research-map.html', 'See where foundations enter Research II'],
        ['measurement-science.html', 'See how measurement assumptions are stress-tested'],
        ['sources.html', 'Trace equations and references'],
      ],
    },
    'visual-atlas.html': {
      stage: 'Three-program visual evidence record',
      question: 'What visual evidence, architecture, or computational record belongs to Research I, Research II, and Research III, and what scientific status does each visual carry?',
      established:
        'The Atlas uses one explicit gallery language across all three programs. Research I exposes its scientific-result figures, Research II renders its canonical theorem and architecture record, and Research III now exposes 9 foundational architecture visuals plus 10 code-generated V1-V10 validation-result figures.',
      open:
        'A figure does not upgrade the status of its underlying evidence. Research I world-tube recovery is not consciousness identification, Research II model rejection is not bridge completion, and Research III synthetic validation is not human or clinical validation.',
      links: [
        ['#research-i-complete-figure-gallery', 'Open the Research I result figures'],
        ['#research-ii-complete-core-gallery', 'Open the Research II core visuals'],
        ['#research-iii-complete-figure-gallery', 'Open all 9 Research III architecture figures'],
        ['#research-iii-validation-figure-gallery', 'Open all 10 Research III validation figures'],
      ],
    },
    'sources.html': {
      stage: 'Three-program provenance and reproducibility',
      question: 'Where do the formal results, experiments, figures, specifications, assumptions, code, tests, and reproducibility records for all three research programs live?',
      established:
        'The Sources page separates Research I physical-system provenance, Research II P1-P100 theorem provenance, and Research III architecture from its V1-V10 executable validation record. Research III validation figures link back to exact derivations, code, tests, and machine-readable results at one pinned commit.',
      open:
        'Traceability is necessary for rigor, but an inspectable research record is not scientific truth by itself. Each program still has to earn its mathematical, computational, empirical, external-validation, or clinical claims at the level appropriate to that program.',
      links: [
        ['#research-i-source-visual-anchor', 'See the Research I visual source anchor'],
        ['#research-ii-source-visual-anchor', 'See the Research II visual source anchor'],
        ['#research-iii-source-visual-anchor', 'See the Research III architecture source anchor'],
        ['#research-iii-source-validation-gallery', 'See the Research III validation source record'],
      ],
    },
  };

  function currentFile() {
    const file = window.location.pathname.split('/').pop();
    return file || 'index.html';
  }

  function linksMarkup(links) {
    return links
      .map(([href, label]) => `<a href="${href}">${label}<span aria-hidden="true"> →</span></a>`)
      .join('');
  }

  function renderScientificOrientation() {
    const page = currentFile();
    const contract = PAGE_CONTRACTS[page];
    if (!contract) return;

    const main = document.querySelector('main');
    const hero = main?.querySelector('.hero, .compact-hero');
    if (!main || !hero || main.querySelector('.scientific-orientation')) return;

    const section = document.createElement('section');
    section.className = 'scientific-orientation';
    section.id = 'scientific-orientation';
    section.dataset.orientationPage = page;
    section.setAttribute('aria-labelledby', 'scientific-orientation-title');
    section.innerHTML = `
      <div class="scientific-orientation-head">
        <div>
          <p class="eyebrow">Scientific orientation · ${contract.stage}</p>
          <h2 id="scientific-orientation-title">Know what this page establishes before entering the details</h2>
        </div>
        <p class="scientific-orientation-intro">Four fixed questions keep the research claim, its boundary, and its audit trail visible at the same time.</p>
      </div>
      <div class="scientific-orientation-grid">
        <article class="orientation-card orientation-question">
          <span class="orientation-number">01</span>
          <div><strong>Question</strong><p>${contract.question}</p></div>
        </article>
        <article class="orientation-card orientation-established">
          <span class="orientation-number">02</span>
          <div><strong>Established here</strong><p>${contract.established}</p></div>
        </article>
        <article class="orientation-card orientation-open">
          <span class="orientation-number">03</span>
          <div><strong>Still open</strong><p>${contract.open}</p></div>
        </article>
        <article class="orientation-card orientation-audit">
          <span class="orientation-number">04</span>
          <div><strong>Evidence and audit</strong><p>Go directly to the surfaces that support or delimit the claims on this page.</p><nav aria-label="Evidence and audit links">${linksMarkup(contract.links)}</nav></div>
        </article>
      </div>`;

    hero.insertAdjacentElement('afterend', section);
  }

  function enhanceHomepageResearchIII() {
    if (currentFile() !== 'index.html') return;

    const programCard = [...document.querySelectorAll('.research-program-card')].find((card) =>
      card.textContent.includes('Research III · Consciousness measurement science')
    );
    if (programCard) {
      const metric = programCard.querySelector('.research-program-metric');
      const meta = programCard.querySelector('.research-program-meta');
      if (metric) metric.innerHTML = '<strong>81</strong><span>tests in each CI job</span>';
      if (meta) meta.textContent = 'V1-V10 formal validation · 19 scientific visuals · 2 deterministic runners';
    }

    const journey = document.querySelector('#project-journey .flow');
    if (journey) {
      const node = [...journey.querySelectorAll('.flow-node')].find((item) =>
        item.querySelector('span')?.textContent.trim() === 'Research III'
      );
      if (node) {
        node.innerHTML = `
          <span>Research III</span>
          <h3>Engineer and falsify the measurement layer</h3>
          <p>Model the observable channel explicitly, prove when latent inference is identifiable, propagate calibration and finite-sample uncertainty, stress dependence and transport, and refuse a precise estimate when the data cannot support it.</p>
          <p><strong>Current record:</strong> V1-V10 formal validation, deterministic simulations, 10 generated result figures, CSV/JSON outputs, theorem tests, and CI across Python 3.10, 3.11, and 3.12.</p>
          <p><a href="measurement-science.html">Research III engineering record →</a></p>`;
      }
    }

    const section = document.getElementById('research-iii-overview');
    if (section) {
      section.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">Research III · Measurement engineering and formal validation</p>
          <h2>When does an observable channel support a latent claim, how unstable is the inverse, and when must the system abstain?</h2>
          <p>Research III is now an executable measurement-science program rather than only an architecture. It starts from a declared latent target and an observable evidence channel, then tests identification, finite-sample uncertainty, calibration transport, multimodal dependence, structural falsification, missing data, numerical conditioning, heterogeneous sites, and resolution-based abstention.</p>
        </div>
        <div class="figure-card">
          <a href="${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/docs/figures/validation_program_map.svg" aria-label="Open the Research III validation program map">
            <img loading="lazy" decoding="async" src="https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${MEASUREMENT_PIN}/docs/figures/validation_program_map.svg" alt="Research III formal measurement validation program from declared target and calibrated evidence through falsification and claim control" />
          </a>
          <div>
            <p class="eyebrow">Formal validation V1-V10</p>
            <h3>Equation → identification → uncertainty → stress test → reproducible result</h3>
            <p>The core binary channel uses <code>q = (1 - beta) + (alpha + beta - 1) pi</code>. The research does not stop at algebraic inversion. Each stage asks whether the inverse remains scientifically defensible once ideal assumptions are weakened.</p>
            <p><a href="${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/VALIDATION.md">Open the complete V1-V10 validation program →</a></p>
          </div>
        </div>
        <div class="frontier-summary-grid">
          <article class="frontier-summary-card"><h3>V1-V3 · Identification and transport</h3><p>Exact calibrated inversion, finite-sample outer identification, and an analytic calibration-shift bias equation establish what can be recovered and when transport fails.</p></article>
          <article class="frontier-summary-card"><h3>V4-V5 · Dependence and falsification</h3><p>Correlated-channel counterexamples expose false multimodal confidence, while permutation testing measures structural-alignment type-I error and power.</p></article>
          <article class="frontier-summary-card"><h3>V6-V8 · Calibration, missingness, conditioning</h3><p>Finite reference-sample uncertainty, sharp arbitrary-missingness bounds, and exact inverse sensitivities quantify how uncertainty and instability propagate.</p></article>
          <article class="frontier-summary-card"><h3>V9-V10 · Heterogeneous sites and abstention</h3><p>A constructive pooled-site non-identifiability result is paired with an explicit engineering rule that withholds a claim when interval resolution is insufficient.</p></article>
          <article class="frontier-summary-card"><h3>81 tests · 3 Python versions</h3><p>Repository policy, compilation, pytest, and Ruff pass across Python 3.10, 3.11, and 3.12 for the merged V1-V10 record.</p></article>
          <article class="frontier-summary-card"><h3>10 result figures · machine-readable outputs</h3><p>Fixed-seed runners generate the validation figures from committed CSV/JSON records rather than hand-entered chart values.</p></article>
        </div>
        <div class="result-grid">
          <article class="result"><span>0.997 → 0.84</span><h3>Dependence stress</h3><p>Naive independence versus the exact posterior in the canonical shared-dependence construction.</p></article>
          <article class="result"><span>20×</span><h3>Weak-channel amplification</h3><p>Proxy-rate error amplification when the Youden information margin is 0.05.</p></article>
          <article class="result"><span>0.375 to 0.5625</span><h3>Site non-identifiability</h3><p>Average latent prevalence compatible with the same pooled proxy rate 0.45 in the canonical two-site construction.</p></article>
          <article class="result"><span>44.4%</span><h3>Resolution-qualified release</h3><p>Canonical V10 release rate at deployment n=1000 under maximum interval width 0.28.</p></article>
        </div>
        <div class="boundary"><p><strong>Scientific boundary:</strong> V1-V10 provides mathematical proofs, deterministic simulations, stress tests, code, and reproducible engineering validation for the measurement machinery. It does not yet provide human empirical calibration showing that a neural, behavioral, physiological, perturbational, or artificial-system channel measures consciousness itself.</p></div>
        <p><a href="measurement-science.html">Full Research III website guide</a> · <a href="${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/docs/validation-atlas.md">Validation atlas</a> · <a href="${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/results/README.md">CSV/JSON results</a> · <a href="${MEASUREMENT_REPO}/tree/${MEASUREMENT_PIN}/tests">Test suite</a></p>`;
    }

    const readerCard = [...document.querySelectorAll('#reader-paths .card')].find((card) =>
      card.querySelector('h3')?.textContent.trim() === 'Follow Research III'
    );
    if (readerCard) {
      const paragraph = readerCard.querySelector('h3 + p');
      if (paragraph) {
        paragraph.textContent = 'Inspect calibrated inverse models, identifiability proofs, finite-sample uncertainty, dependence and transport stress, missingness, conditioning, heterogeneous-site bounds, abstention, simulations, figures, and tests.';
      }
    }

    const sharedBoundary = document.getElementById('shared-boundary');
    if (sharedBoundary) {
      const paragraphs = sharedBoundary.querySelectorAll('p');
      if (paragraphs[1]) {
        paragraphs[1].innerHTML = 'The repository does <strong>not</strong> claim that consciousness has already been derived from physics. Research I does not turn a recovered physical subsystem into a conscious subject. Research II does not turn conditional model separation into proof of consciousness or nonphysicality. Research III does not turn successful analytic and synthetic validation of a measurement model into empirical proof that consciousness itself has been measured.';
      }
    }

    const record = [...document.querySelectorAll('.result')].find((item) =>
      item.querySelector('h3')?.textContent.trim() === 'Research III record'
    );
    if (record) {
      const paragraph = record.querySelector('p');
      if (paragraph) {
        paragraph.textContent = 'Measurement engineering with V1-V10 formal validation, identifiability and robustness mathematics, deterministic simulations, 19 scientific visuals, machine-readable results, reproducible runners, and 81 CI-tested checks per Python job.';
      }
    }
  }

  function loadThreeProgramEvidence() {
    const page = currentFile();
    if (page !== 'visual-atlas.html' && page !== 'sources.html') return;
    if (document.querySelector('script[data-three-program-evidence]')) return;

    const script = document.createElement('script');
    script.src = 'three-program-evidence.js';
    script.defer = true;
    script.dataset.threeProgramEvidence = 'script';
    document.head.appendChild(script);
  }

  function loadSourceSectionVisuals() {
    if (currentFile() !== 'sources.html') return;
    if (document.querySelector('script[data-source-section-visuals]')) return;

    const script = document.createElement('script');
    script.src = 'source-section-visuals.js';
    script.defer = true;
    script.dataset.sourceSectionVisuals = 'script';
    document.head.appendChild(script);
  }

  function loadAtlasArchitectureRefresh() {
    if (currentFile() !== 'visual-atlas.html') return;
    if (document.querySelector('script[data-atlas-architecture-refresh]')) return;

    const script = document.createElement('script');
    script.src = 'atlas-architecture-refresh.js';
    script.defer = true;
    script.dataset.atlasArchitectureRefresh = 'script';
    document.head.appendChild(script);
  }

  function loadResearchIIIAtlasRefresh() {
    const page = currentFile();
    if (page !== 'visual-atlas.html' && page !== 'sources.html') return;
    if (document.querySelector('script[data-research-iii-atlas-refresh]')) return;

    const script = document.createElement('script');
    script.src = 'research-iii-atlas-refresh.js';
    script.defer = true;
    script.dataset.researchIiiAtlasRefresh = 'script';
    document.head.appendChild(script);
  }

  function initialize() {
    renderScientificOrientation();
    enhanceHomepageResearchIII();
    loadThreeProgramEvidence();
    loadSourceSectionVisuals();
    loadAtlasArchitectureRefresh();
    loadResearchIIIAtlasRefresh();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();
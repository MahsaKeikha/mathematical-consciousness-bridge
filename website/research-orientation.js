(() => {
  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';
  const OBSERVER_REPO = 'https://github.com/MahsaKeikha/spatiotemporal-observer-math';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const MEASUREMENT_PIN = '7a2a1a3a60263e48b7a268642eecc6941e84d1b4';

  const PAGE_CONTRACTS = {
    'index.html': {
      stage: 'Whole program',
      question: 'How do the three research programs fit together, and where is the current formal frontier?',
      established:
        'The site documents a three-stage program: physical-system identification in Research I, bridge sufficiency and falsification through P100 in Research II, and a V1-V15 formal measurement-validation program in Research III.',
      open:
        'The physical-to-experiential bridge remains open. The overview organizes mathematical, computational, and measurement-science evidence but does not add a new bridge principle or experiential identification claim.',
      links: [
        ['research-lineage.html', 'See the three-stage scientific handoff'],
        ['research-map.html', 'Audit the Research II theorem map'],
        ['measurement-science.html', 'Open Research III V1-V15'],
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
        'The lineage separates physical-system identification, bridge sufficiency testing, and measurement science so outputs from one stage are not silently promoted into conclusions belonging to another. Research III now adds V1-V15 formal validation and measurement-design laws.',
      open:
        'No handoff by itself establishes the physical-to-experiential bridge. The bridge requires an independently justified principle and empirical support beyond stage-to-stage bookkeeping.',
      links: [
        ['observer-research.html', 'Inspect Research I'],
        ['research-map.html', 'Inspect Research II'],
        ['measurement-science.html', 'Inspect Research III V1-V15'],
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
      heading: 'Scientific scope and validation status',
      intro: 'The formal results below concern identifiability, uncertainty, robustness, and measurement design. This orientation separates what is proved or simulated from what still requires empirical calibration.',
      question: 'What can observable channels legitimately identify about a declared experiential target, and exactly where does that inference fail?',
      established:
        'Research III contains a reproducible V1-V15 formal validation program covering calibrated inversion, partial identification, finite-sample coverage, transport bias, channel dependence, structural null and power testing, calibration uncertainty, arbitrary missingness, inverse conditioning, multisite identification, exact missingness-information loss, resolution sample-size design, and an independent pilot release gate.',
      open:
        'These analytic and synthetic results validate measurement machinery under declared models. They do not establish empirical calibration for consciousness in humans or other systems, and principled non-identification remains an allowed result.',
      links: [
        [`${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/VALIDATION.md`, 'Open the V1-V15 validation program'],
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
        'The Atlas uses one explicit gallery language across all three programs. Research I exposes its scientific-result figures, Research II renders its canonical theorem and architecture record, and Research III exposes 9 foundational architecture visuals plus 14 code-generated V1-V15 validation-result figures.',
      open:
        'A figure does not upgrade the status of its underlying evidence. Research I world-tube recovery is not consciousness identification, Research II model rejection is not bridge completion, and Research III analytic or synthetic validation is not human or clinical validation.',
      links: [
        ['#research-i-complete-figure-gallery', 'Open the Research I result figures'],
        ['#research-ii-complete-core-gallery', 'Open the Research II core visuals'],
        ['#research-iii-complete-figure-gallery', 'Open all 9 Research III architecture figures'],
        ['#research-iii-validation-figure-gallery', 'Open all 14 Research III validation figures'],
      ],
    },
    'sources.html': {
      stage: 'Three-program provenance and reproducibility',
      question: 'Where do the formal results, experiments, figures, specifications, assumptions, code, tests, and reproducibility records for all three research programs live?',
      established:
        'The Sources page separates Research I physical-system provenance, Research II P1-P100 theorem provenance, and Research III architecture from its V1-V15 executable validation record. Each Research III validation visual links to the exact derivation, machine-readable result data, and figure source at one pinned commit.',
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
    return window.location.pathname.split('/').pop() || 'index.html';
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
          <h2 id="scientific-orientation-title">${contract.heading || 'Scientific scope, evidence level, and audit path'}</h2>
          <p class="scientific-orientation-intro">${contract.intro || 'The four statements below keep the research question, current result, remaining uncertainty, and audit path together before the detailed record begins.'}</p>
        </div>
      </div>
      <div class="scientific-orientation-grid">
        <article class="orientation-card orientation-question"><span class="orientation-number">01</span><div><strong>Question</strong><p>${contract.question}</p></div></article>
        <article class="orientation-card orientation-established"><span class="orientation-number">02</span><div><strong>Established here</strong><p>${contract.established}</p></div></article>
        <article class="orientation-card orientation-open"><span class="orientation-number">03</span><div><strong>Still open</strong><p>${contract.open}</p></div></article>
        <article class="orientation-card orientation-audit"><span class="orientation-number">04</span><div><strong>Evidence and audit</strong><p>Go directly to the surfaces that support or delimit the claims on this page.</p><nav aria-label="Evidence and audit links">${linksMarkup(contract.links)}</nav></div></article>
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
      if (metric) metric.innerHTML = '<strong>98</strong><span>tests in each CI job</span>';
      if (meta) meta.textContent = 'V1-V15 formal validation · 23 scientific visuals · 3 deterministic runners';
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
          <p>Model the observable channel explicitly, prove when latent inference is identifiable, propagate calibration and finite-sample uncertainty, stress dependence and transport, quantify multisite and missing-data information loss, and design release rules that separate pilot selection from confirmatory inference.</p>
          <p><strong>Current record:</strong> V1-V15 formal validation, deterministic simulations, 14 generated result figures, CSV/JSON outputs, theorem tests, and CI across Python 3.10, 3.11, and 3.12.</p>
          <p><a href="measurement-science.html">Research III engineering record →</a></p>`;
      }
    }

    const section = document.getElementById('research-iii-overview');
    if (section) {
      section.querySelector('.section-head p:last-child')?.replaceChildren(document.createTextNode(
        'Research III is an executable measurement-science program. It tests identification, finite-sample uncertainty, calibration transport, dependence, missingness, inverse conditioning, heterogeneous sites, exact information loss, sample-size design, and selection-safe release.'
      ));
    }
  }

  function loadScriptOnce(src, dataKey) {
    if (document.querySelector(`script[${dataKey}]`)) return;
    const script = document.createElement('script');
    script.src = src;
    script.defer = true;
    script.setAttribute(dataKey, 'script');
    document.head.appendChild(script);
  }

  function loadThreeProgramEvidence() {
    const page = currentFile();
    if (page !== 'visual-atlas.html' && page !== 'sources.html') return;
    loadScriptOnce('three-program-evidence.js', 'data-three-program-evidence');
  }

  function loadSourceSectionVisuals() {
    if (currentFile() !== 'sources.html') return;
    loadScriptOnce('source-section-visuals.js', 'data-source-section-visuals');
  }

  function loadAtlasArchitectureRefresh() {
    if (currentFile() !== 'visual-atlas.html') return;
    loadScriptOnce('atlas-architecture-refresh.js', 'data-atlas-architecture-refresh');
  }

  function loadResearchIIIAtlasRefresh() {
    const page = currentFile();
    if (!['index.html', 'measurement-science.html', 'visual-atlas.html', 'sources.html'].includes(page)) return;
    loadScriptOnce('research-iii-atlas-refresh.js', 'data-research-iii-atlas-refresh');
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

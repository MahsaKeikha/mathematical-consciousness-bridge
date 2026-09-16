(() => {
  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';
  const OBSERVER_REPO = 'https://github.com/MahsaKeikha/spatiotemporal-observer-math';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';

  const PAGE_CONTRACTS = {
    'index.html': {
      stage: 'Whole program',
      question: 'How do the three research programs fit together, and where is the current formal frontier?',
      established:
        'The site documents a three-stage program: physical-system identification in Research I, bridge sufficiency and falsification through P100 in Research II, and measurement science in Research III.',
      open:
        'The physical-to-experiential bridge remains open. The overview organizes the evidence but does not add a new bridge principle or experiential identification claim.',
      links: [
        ['research-lineage.html', 'See the three-stage scientific handoff'],
        ['research-map.html', 'Audit the Research II theorem map'],
        ['sources.html', 'Open sources and reproducibility'],
      ],
    },
    'plain-language.html': {
      stage: 'Reader translation',
      question: 'What is the research actually claiming in language that does not require reading the proofs first?',
      established:
        'The page translates the formal distinctions among physical description, independent target, compatibility, rejection, and measurement assumptions without changing the theorem statements.',
      open:
        'A simpler explanation is not a weaker scientific boundary. Compatibility is not validation, rejection of one descriptor is not proof of nonphysical consciousness, and the final bridge remains unresolved.',
      links: [
        ['start-here.html', 'Move from intuition to the formal reading path'],
        ['research-map.html', 'Check the formal Research II record'],
        ['sources.html', 'Verify sources and audit surfaces'],
      ],
    },
    'start-here.html': {
      stage: 'First-reader guide',
      question: 'What should a new reader understand before entering the proposition chronology?',
      established:
        'The reading path fixes the project vocabulary, the sufficiency question, the interpretation boundary, and the relationship among Research I, II, and III before proposition-level detail begins.',
      open:
        'The guide does not identify consciousness with a latent variable, physical descriptor, observer subsystem, or measurement channel. Those identifications require independent scientific justification.',
      links: [
        ['#chain', 'Follow the seven-layer inference chain'],
        ['research-map.html', 'Open all 100 Research II results'],
        ['visual-atlas.html', 'See the visual theorem record'],
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
        'The lineage page separates physical-system identification, bridge sufficiency testing, and measurement science so that outputs from one stage are not silently promoted into conclusions belonging to another.',
      open:
        'No handoff by itself establishes the physical-to-experiential bridge. The bridge requires an independently justified principle and empirical support beyond stage-to-stage bookkeeping.',
      links: [
        ['observer-research.html', 'Inspect Research I'],
        ['research-map.html', 'Inspect Research II'],
        ['measurement-science.html', 'Inspect Research III'],
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
        ['sources.html', 'Audit provenance and reproducibility'],
      ],
    },
    'measurement-science.html': {
      stage: 'Research III',
      question: 'What can observable reports, behavior, neural signals, physiology, interventions, and context legitimately identify about experiential targets?',
      established:
        'Research III develops target-specific measurement claims under explicit uncertainty, dependence, competing explanations, and non-identification conditions rather than treating any one observable as experience itself.',
      open:
        'A measurement model can constrain or identify a declared target only under its assumptions. It does not turn an observable proxy into consciousness by definition, and principled non-identification remains an allowed result.',
      links: [
        [MEASUREMENT_REPO, 'Open the Research III repository'],
        ['research-lineage.html', 'See the Research II to III handoff'],
        ['sources.html', 'Open shared provenance and sources'],
      ],
    },
    'physics-mathematics.html': {
      stage: 'Foundations',
      question: 'Which mathematical and physical structures are used by the bridge-testing program, and exactly where do their assumptions enter?',
      established:
        'This page organizes the physical, probabilistic, information-theoretic, causal, statistical, and quantum tools used to state and test the Research II claims.',
      open:
        'Mathematical consistency inside a chosen framework does not by itself supply an experiential interpretation. The foundations constrain bridge claims but do not manufacture the missing bridge principle.',
      links: [
        ['research-map.html', 'See where each foundation enters Research II'],
        ['visual-atlas.html', 'Inspect the mathematical figures'],
        ['sources.html', 'Trace equations and references'],
      ],
    },
    'visual-atlas.html': {
      stage: 'Three-program visual evidence record',
      question: 'What visual evidence, architecture, or computational record belongs to Research I, Research II, and Research III, and what scientific status does each visual carry?',
      established:
        'The Atlas now uses one explicit gallery language across all three programs. Research I exposes all 33 scientific-result figures. Research II renders exactly 100 unique canonical core visuals from the bundled release manifest while preserving the longer theorem archive separately. Research III exposes its complete pinned 3 / 3 canonical figure set.',
      open:
        'A figure does not upgrade the status of its underlying evidence. Research I world-tube recovery is not consciousness identification, Research II model rejection is not bridge completion, and Research III specification is not empirical or clinical validation.',
      links: [
        ['#research-i-complete-figure-gallery', 'Open all 33 Research I result figures'],
        ['#research-ii-complete-core-gallery', 'Open all 100 Research II core visuals'],
        ['#research-iii-complete-figure-gallery', 'Open all 3 Research III canonical figures'],
      ],
    },
    'sources.html': {
      stage: 'Three-program provenance and reproducibility',
      question: 'Where do the formal results, experiments, figures, specifications, assumptions, code, tests, and reproducibility records for all three research programs live?',
      established:
        'The source page separates Research I physical-system provenance, Research II P1-P100 theorem provenance, and Research III measurement-science specification and scaffold provenance. Each research section now opens with a representative scientific visual before its source catalog, while Research I and Research III retain their complete direct source manifests.',
      open:
        'Traceability is necessary for rigor, but an inspectable research record is not scientific truth by itself. Each program still has to earn its own mathematical, computational, empirical, external-validation, or clinical claims at the level appropriate to that program.',
      links: [
        ['#research-i-source-visual-anchor', 'See the Research I visual source anchor'],
        ['#research-ii-source-visual-anchor', 'See the Research II visual source anchor'],
        ['#research-iii-source-visual-anchor', 'See the Research III visual source anchor'],
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

  function initialize() {
    renderScientificOrientation();
    loadThreeProgramEvidence();
    loadSourceSectionVisuals();
    loadAtlasArchitectureRefresh();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();

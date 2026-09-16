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
    },
    'sources.html': {
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

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderScientificOrientation, { once: true });
  } else {
    renderScientificOrientation();
  }
})();

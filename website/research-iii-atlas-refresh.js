(() => {
  const RESEARCH_III_PIN = '383a6cdab720b3f87c17191b7c98bd6828213b72';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const RAW_PIN_PREFIX =
    `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${RESEARCH_III_PIN}/docs/figures/`;
  const BLOB_PIN_PREFIX =
    `https://github.com/MahsaKeikha/consciousness-measurement-science/blob/${RESEARCH_III_PIN}/docs/figures/`;

  const RESEARCH_III_FIGURES = [
    {
      title: 'Research III program map',
      file: 'research_program_map.svg',
      context: 'docs/measurement-framework.md',
      phase: 'Whole-program architecture',
      summary: 'Five declared experiential targets are separated from observable evidence, assumptions, identification, validation, and the final claim ceiling.',
    },
    {
      title: 'Target-specific evidence matrix',
      file: 'target_evidence_matrix.svg',
      context: 'docs/measurement-instrument-spec.md',
      phase: 'Target and evidence design',
      summary: 'The matrix shows why an evidence channel can be informative for one target and insufficient for another, preventing cross-target category errors.',
    },
    {
      title: 'Consciousness measurement architecture',
      file: 'measurement_architecture.svg',
      context: 'docs/measurement-framework.md',
      phase: 'Measurement architecture',
      summary: 'The latent experiential target remains distinct from report, behavior, neural activity, perturbation, physiology, context, and intervention.',
    },
    {
      title: 'Consciousness Evidence Profile anatomy',
      file: 'cep_anatomy.svg',
      context: 'docs/measurement-instrument-spec.md',
      phase: 'Auditable evidence record',
      summary: 'The CEP keeps target, evidence vector, quality, uncertainty, assumptions, validation domain, and allowed claim level visible before any optional scalar summary.',
    },
    {
      title: 'Identification and uncertainty pipeline',
      file: 'identification_uncertainty_pipeline.svg',
      context: 'docs/partial-identification.md',
      phase: 'Identification discipline',
      summary: 'Point identification, partial identification, and principled abstention are treated as distinct scientific outcomes rather than forced into one score.',
    },
    {
      title: 'Phenomenal structural measurement pipeline',
      file: 'structural_measurement_pipeline.svg',
      context: 'docs/phenomenal-structure.md',
      phase: 'Phenomenal structure',
      summary: 'Phenomenal and physical relational geometries are compared through a preregistered mapping family and held-out distortion without assuming ontological identity.',
    },
    {
      title: 'Validation program map',
      file: 'validation_program_map.svg',
      context: 'docs/experimental-program.md',
      phase: 'Validation program',
      summary: 'Validation expands from report-rich benchmarks to confound separation, transport, causal perturbation, clinical stress tests, structural prediction, and theory comparison.',
    },
    {
      title: 'Theory comparison and falsification map',
      file: 'theory_falsification_map.svg',
      context: 'docs/falsification-matrix.md',
      phase: 'Theory falsification',
      summary: 'Competing theories are compared through declared commitments and preregistered divergent predictions rather than by post hoc fit alone.',
    },
    {
      title: 'M0-M7 measurement claim ladder',
      file: 'claim_ladder.svg',
      context: 'docs/claim-registry.md',
      phase: 'Claim discipline',
      summary: 'The claim ladder separates signal differences, prediction, transport, causal support, latent-target identification, structural prediction, and unique theory tests.',
    },
  ];

  const CURATED_FILES = new Set([
    'research_program_map.svg',
    'target_evidence_matrix.svg',
    'cep_anatomy.svg',
    'identification_uncertainty_pipeline.svg',
    'validation_program_map.svg',
    'theory_falsification_map.svg',
  ]);

  function currentFile() {
    return window.location.pathname.split('/').pop() || 'index.html';
  }

  function escapeHTML(value) {
    return String(value)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#39;');
  }

  function sourceLinks(record) {
    const context = `${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/${record.context}`;
    const figure = `${BLOB_PIN_PREFIX}${record.file}`;
    return `<div class="figure-source-links"><a href="${context}">Scientific context</a><a href="${figure}">Figure source</a></div>`;
  }

  function curatedCard(record) {
    const image = `${RAW_PIN_PREFIX}${record.file}`;
    const figure = `${BLOB_PIN_PREFIX}${record.file}`;
    return `
      <article class="program-visual-card" data-research-iii-curated-figure="docs/figures/${escapeHTML(record.file)}">
        <a href="${figure}" aria-label="Open full-resolution ${escapeHTML(record.title)}"><img loading="lazy" decoding="async" src="${image}" alt="Research III ${escapeHTML(record.title)}" /></a>
        <span>${escapeHTML(record.phase)}</span>
        <h3>${escapeHTML(record.title)}</h3>
        <p>${escapeHTML(record.summary)}</p>
        ${sourceLinks(record)}
      </article>`;
  }

  function completeCard(record) {
    const image = `${RAW_PIN_PREFIX}${record.file}`;
    const figure = `${BLOB_PIN_PREFIX}${record.file}`;
    return `
      <article class="complete-figure-card" data-research-iii-figure="docs/figures/${escapeHTML(record.file)}">
        <a href="${figure}" aria-label="Open full-resolution ${escapeHTML(record.title)}"><img loading="lazy" decoding="async" src="${image}" alt="Research III ${escapeHTML(record.title)}" /></a>
        <div class="complete-figure-card-body">
          <span class="figure-phase">Research III · ${escapeHTML(record.phase)}</span>
          <h4>${escapeHTML(record.title)}</h4>
          <p>${escapeHTML(record.summary)}</p>
          ${sourceLinks(record)}
        </div>
      </article>`;
  }

  function addCanonicalFigureMetric(section) {
    const metrics = section.querySelector('.program-record-grid');
    if (!metrics || metrics.querySelector('[data-research-iii-figure-count]')) return;
    const metric = document.createElement('div');
    metric.className = 'program-record-metric';
    metric.dataset.researchIiiFigureCount = '9';
    metric.innerHTML = '<strong>9</strong><span>canonical scientific visuals</span>';
    metrics.appendChild(metric);
  }

  function renderResearchIIIAtlas() {
    if (currentFile() !== 'visual-atlas.html') return;
    const section = document.getElementById('research-iii-visual-program');
    if (!section) return;

    addCanonicalFigureMetric(section);

    const legacyShowcase = section.querySelector(':scope > .program-visual-grid');
    if (legacyShowcase) {
      legacyShowcase.hidden = true;
      legacyShowcase.setAttribute('aria-hidden', 'true');
    }

    document.getElementById('research-iii-complete-figure-gallery')?.remove();
    document.getElementById('research-iii-curated-visual-story')?.remove();
    document.getElementById('research-iii-complete-figure-note')?.remove();

    const boundary = section.querySelector('.boundary');
    const curated = RESEARCH_III_FIGURES.filter((record) => CURATED_FILES.has(record.file));

    const story = document.createElement('div');
    story.id = 'research-iii-curated-visual-story';
    story.className = 'complete-record-block';
    story.innerHTML = `
      <div class="complete-record-head">
        <div><span class="record-badge">Curated Research III visual path</span><h3>From declared target to an auditable scientific claim</h3><p>Read these six visuals first to follow the measurement-science logic: define the program, match evidence to the target, preserve an auditable evidence profile, state what is identified, validate transport and causal robustness, then test competing theories.</p></div>
        <span class="record-badge">6-stage visual path</span>
      </div>
      <div class="program-visual-grid">${curated.map(curatedCard).join('')}</div>`;

    const complete = document.createElement('div');
    complete.id = 'research-iii-complete-figure-gallery';
    complete.className = 'complete-record-block';
    complete.innerHTML = `
      <div class="complete-record-head">
        <div><span class="record-badge">Complete canonical set</span><h3>All 9 Research III scientific visuals in one gallery</h3><p>This is the complete current visual record from the validated Research III revision ${RESEARCH_III_PIN.slice(0, 8)}. It includes the whole-program map, target-evidence matrix, measurement architecture, CEP anatomy, identification and uncertainty, phenomenal structure, validation, theory falsification, and M0-M7 claim discipline.</p></div>
        <span class="record-badge">9 / 9 visible</span>
      </div>
      <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/visual-research-guide.md">Open the Research III visual guide</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/figure-catalog.md">Open the Research III figure catalog</a></div>
      <div class="complete-figure-grid">${RESEARCH_III_FIGURES.map(completeCard).join('')}</div>`;

    if (boundary) {
      boundary.insertAdjacentElement('beforebegin', story);
      boundary.insertAdjacentElement('beforebegin', complete);
    } else {
      section.append(story, complete);
    }
  }

  function waitForBaseAtlas(attempt = 0) {
    if (currentFile() !== 'visual-atlas.html') return;
    const section = document.getElementById('research-iii-visual-program');
    const baseGallery = document.getElementById('research-iii-complete-figure-gallery');
    if ((section && baseGallery) || attempt >= 100) {
      renderResearchIIIAtlas();
      return;
    }
    window.setTimeout(() => waitForBaseAtlas(attempt + 1), 25);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => waitForBaseAtlas(), { once: true });
  } else {
    waitForBaseAtlas();
  }
})();

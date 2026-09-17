(() => {
  const RESEARCH_III_PIN = '3cf9202977953644c980246c1f3e46a3514b3a4a';
  const REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const RAW_PREFIX = `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${RESEARCH_III_PIN}/docs/figures/`;
  const BLOB_PREFIX = `${REPO}/blob/${RESEARCH_III_PIN}/docs/figures/`;

  const FIGURES = [
    {
      file: 'research_program_map.svg',
      title: 'Research III program map',
      context: 'docs/measurement-framework.md',
      summary: 'The whole measurement program, from declared experiential target through evidence, assumptions, identification, validation, and the final claim ceiling.',
    },
    {
      file: 'target_evidence_matrix.svg',
      title: 'Target-specific evidence matrix',
      context: 'docs/measurement-instrument-spec.md',
      summary: 'Why an evidence channel can be informative for one target while remaining insufficient for another, preventing cross-target category errors.',
    },
    {
      file: 'measurement_architecture.svg',
      title: 'Consciousness measurement architecture',
      context: 'docs/measurement-framework.md',
      summary: 'The latent experiential target remains distinct from report, behavior, neural activity, perturbation, physiology, intervention, and context.',
    },
    {
      file: 'cep_anatomy.svg',
      title: 'Consciousness Evidence Profile anatomy',
      context: 'docs/measurement-instrument-spec.md',
      summary: 'The CEP keeps evidence, quality, uncertainty, assumptions, validation domain, and allowed claim level visible before any optional summary.',
    },
    {
      file: 'identification_uncertainty_pipeline.svg',
      title: 'Identification and uncertainty pipeline',
      context: 'docs/partial-identification.md',
      summary: 'Point identification, partial identification, and principled abstention are kept as distinct scientific outcomes rather than forced into one score.',
    },
    {
      file: 'structural_measurement_pipeline.svg',
      title: 'Phenomenal structural measurement pipeline',
      context: 'docs/phenomenal-structure.md',
      summary: 'Phenomenal and physical relational geometries are compared through a preregistered mapping family and held-out distortion without assuming ontological identity.',
    },
    {
      file: 'validation_program_map.svg',
      title: 'Validation program map',
      context: 'docs/experimental-program.md',
      summary: 'Validation progresses from report-rich benchmarks through confound separation, transport, causal perturbation, clinical stress tests, structural prediction, and theory comparison.',
    },
    {
      file: 'theory_falsification_map.svg',
      title: 'Theory comparison and falsification map',
      context: 'docs/falsification-matrix.md',
      summary: 'Competing theories are compared through declared commitments and preregistered divergent predictions rather than by post hoc compatibility alone.',
    },
    {
      file: 'claim_ladder.svg',
      title: 'M0-M7 measurement claim ladder',
      context: 'docs/claim-registry.md',
      summary: 'The claim ladder separates signal differences, prediction, transport, causal support, latent-target identification, structural prediction, and unique theory tests.',
    },
  ];

  function escapeHTML(value) {
    return String(value)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#39;');
  }

  function card(record, index) {
    const rawFigure = `${RAW_PREFIX}${record.file}`;
    const sourceFigure = `${BLOB_PREFIX}${record.file}`;
    const context = `${REPO}/blob/${RESEARCH_III_PIN}/${record.context}`;
    return `
      <article class="figure-card" data-research-iii-page-figure="${escapeHTML(record.file)}">
        <a href="${rawFigure}" aria-label="Open full-resolution ${escapeHTML(record.title)}">
          <img loading="lazy" decoding="async" src="${rawFigure}" alt="Research III figure ${index + 1}: ${escapeHTML(record.title)}" />
        </a>
        <p class="eyebrow">Canonical figure ${index + 1} of 9</p>
        <h3>${escapeHTML(record.title)}</h3>
        <p>${escapeHTML(record.summary)}</p>
        <div class="figure-source-links">
          <a href="${rawFigure}">Full-resolution SVG</a>
          <a href="${context}">Scientific context</a>
          <a href="${sourceFigure}">Repository source</a>
        </div>
      </article>`;
  }

  function render() {
    if ((window.location.pathname.split('/').pop() || 'index.html') !== 'measurement-science.html') return;

    const sections = [...document.querySelectorAll('main > section')];
    const section = sections.find((candidate) =>
      candidate.querySelector('.section-head .eyebrow')?.textContent?.trim() === 'Visual architecture'
    );
    if (!section) return;

    const head = section.querySelector('.section-head');
    const grid = section.querySelector('.measurement-figure-grid');
    if (!head || !grid) return;

    head.innerHTML = `
      <p class="eyebrow">Complete visual architecture</p>
      <h2>All 9 canonical Research III scientific figures</h2>
      <p>This page now exposes the complete canonical visual record from the validated Research III revision <code>${RESEARCH_III_PIN.slice(0, 8)}</code>. Each figure is shown directly here, links to its full-resolution SVG, and retains a path to the scientific context and repository source.</p>`;

    grid.dataset.researchIiiCompleteGallery = '9';
    grid.innerHTML = FIGURES.map(card).join('');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', render, { once: true });
  } else {
    render();
  }
})();
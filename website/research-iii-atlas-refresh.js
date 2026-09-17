(() => {
  const RESEARCH_III_PIN = 'a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const RAW_PIN_PREFIX =
    `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${RESEARCH_III_PIN}/docs/figures/`;
  const BLOB_PIN_PREFIX =
    `https://github.com/MahsaKeikha/consciousness-measurement-science/blob/${RESEARCH_III_PIN}/docs/figures/`;

  const LEGACY_PINS = [
    '3cf9202977953644c980246c1f3e46a3514b3a4a',
    '5d1d979231aed62fde34383281fa8f252a3d2fa7',
    'b874eda1f6940f5601b7f89200b6a276b5ecbbc3',
    '8bbb7b029d70c43cc6a9dbf8b44dfe5069d0993d',
    '7a106820158e0d33ea651f7cdeaa505206f1ccc7',
  ];

  const FOUNDATION_FIGURES = [
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
      summary: 'A channel can be informative for one target and insufficient for another; the matrix prevents cross-target category errors.',
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
      summary: 'The CEP keeps target, evidence, quality, uncertainty, assumptions, validation domain, and allowed claim level visible before any optional summary.',
    },
    {
      title: 'Identification and uncertainty pipeline',
      file: 'identification_uncertainty_pipeline.svg',
      context: 'docs/partial-identification.md',
      phase: 'Identification discipline',
      summary: 'Point identification, partial identification, and principled abstention are separate scientific outcomes rather than one forced score.',
    },
    {
      title: 'Phenomenal structural measurement pipeline',
      file: 'structural_measurement_pipeline.svg',
      context: 'docs/phenomenal-structure.md',
      phase: 'Phenomenal structure',
      summary: 'Phenomenal and physical relational geometries are compared through a frozen mapping family and held-out distortion without assuming identity.',
    },
    {
      title: 'Validation program map',
      file: 'validation_program_map.svg',
      context: 'docs/experimental-program.md',
      phase: 'Validation program',
      summary: 'Validation expands from report-rich benchmarks to confound separation, transport, perturbation, clinical stress tests, structural prediction, and theory comparison.',
    },
    {
      title: 'Theory comparison and falsification map',
      file: 'theory_falsification_map.svg',
      context: 'docs/falsification-matrix.md',
      phase: 'Theory falsification',
      summary: 'Competing theories are compared through declared commitments and preregistered divergent predictions rather than post hoc compatibility.',
    },
    {
      title: 'M0-M7 measurement claim ladder',
      file: 'claim_ladder.svg',
      context: 'docs/claim-registry.md',
      phase: 'Claim discipline',
      summary: 'The ladder separates signal differences, prediction, transport, causal support, latent-target identification, structural prediction, and unique theory tests.',
    },
  ];

  const VALIDATION_FIGURES = [
    {
      title: 'Finite-sample identification',
      file: 'finite_sample_identification.svg',
      context: 'docs/formal-validation-program.md',
      phase: 'V2 · finite-sample identification',
      summary: 'The outer identified interval contracts with deployment sample size while retaining declared calibration uncertainty.',
    },
    {
      title: 'Finite-sample coverage',
      file: 'finite_sample_coverage.svg',
      context: 'docs/formal-validation-program.md',
      phase: 'V2 · coverage',
      summary: 'Repeated fixed-seed sampling checks whether the declared finite-sample interval covers the known synthetic target.',
    },
    {
      title: 'Calibration transport bias',
      file: 'transport_bias_surface.svg',
      context: 'docs/formal-validation-program.md',
      phase: 'V3 · transport',
      summary: 'The stress surface shows exact latent-contrast bias when sensitivity or specificity shifts but baseline calibration is reused.',
    },
    {
      title: 'Conditional-dependence stress',
      file: 'dependence_stress.svg',
      context: 'docs/formal-validation-program.md',
      phase: 'V4 · dependence',
      summary: 'A correlated-channel construction preserves marginal calibration while exposing false confidence from naive likelihood-ratio multiplication.',
    },
    {
      title: 'Structural alignment null and power',
      file: 'structural_alignment_power.svg',
      context: 'docs/formal-validation-program.md',
      phase: 'V5 · structural falsification',
      summary: 'Permutation testing is checked under a null construction and under increasing planted relational correspondence.',
    },
    {
      title: 'Finite calibration-sample uncertainty',
      file: 'calibration_sample_uncertainty.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      phase: 'V6 · calibration samples',
      summary: 'Sensitivity and specificity are estimated from finite reference samples, making calibration sample size part of the uncertainty budget.',
    },
    {
      title: 'Missingness identification loss',
      file: 'missingness_identification_loss.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      phase: 'V7 · arbitrary missingness',
      summary: 'Sharp worst-case bounds widen as outcomes go missing without a missing-at-random assumption; missing data are not converted into negative evidence.',
    },
    {
      title: 'Inverse conditioning by Youden margin',
      file: 'inverse_conditioning_youden.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      phase: 'V8 · inverse conditioning',
      summary: 'The exact 1/J amplification law shows when an algebraically invertible channel becomes numerically unstable.',
    },
    {
      title: 'Two-site partial identification',
      file: 'two_site_partial_identification.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      phase: 'V9 · site heterogeneity',
      summary: 'Different site calibration makes one pooled observable compatible with a range of population-average latent prevalences.',
    },
    {
      title: 'Resolution abstention frontier',
      file: 'resolution_abstention_frontier.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      phase: 'V10 · abstention',
      summary: 'The pipeline releases a result only when a predeclared maximum interval width is achieved; otherwise the scientific output is inconclusive.',
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

  function repinValue(value) {
    let updated = value;
    for (const pin of LEGACY_PINS) updated = updated.replaceAll(pin, RESEARCH_III_PIN);
    updated = updated.replace(
      'github.com/MahsaKeikha/consciousness-measurement-science/blob/main/',
      `github.com/MahsaKeikha/consciousness-measurement-science/blob/${RESEARCH_III_PIN}/`,
    );
    updated = updated.replace(
      'raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/main/',
      `raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${RESEARCH_III_PIN}/`,
    );
    return updated;
  }

  function repinResearchIIIAssets() {
    document.querySelectorAll('a[href], img[src]').forEach((node) => {
      if (node.hasAttribute('href')) {
        const value = node.getAttribute('href');
        if (value && value.includes('consciousness-measurement-science')) {
          node.setAttribute('href', repinValue(value));
        }
      }
      if (node.hasAttribute('src')) {
        const value = node.getAttribute('src');
        if (value && value.includes('consciousness-measurement-science')) {
          node.setAttribute('src', repinValue(value));
        }
      }
    });
  }

  function ensureStyles() {
    if (document.getElementById('research-iii-validation-styles')) return;
    const style = document.createElement('style');
    style.id = 'research-iii-validation-styles';
    style.textContent = `
      .r3-validation-record{margin:1.4rem 0;padding:1.25rem;border:1px solid rgba(120,140,170,.28);border-radius:20px;background:rgba(255,255,255,.025)}
      .r3-validation-head{display:flex;gap:1rem;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;margin-bottom:1rem}
      .r3-validation-head h3{margin:.3rem 0 .45rem}.r3-validation-head p{margin:0;max-width:900px;line-height:1.6}
      .r3-validation-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:1rem}
      .r3-validation-card{display:flex;flex-direction:column;border:1px solid rgba(120,140,170,.24);border-radius:16px;overflow:hidden;background:rgba(255,255,255,.02)}
      .r3-validation-card>a{display:flex;align-items:center;justify-content:center;min-height:320px;padding:.35rem;background:#fff}
      .r3-validation-card img{display:block;width:100%;height:340px;object-fit:contain;background:#fff}
      .r3-validation-card-body{display:flex;flex-direction:column;flex:1;padding:1rem 1.05rem 1.1rem}
      .r3-validation-card-body span{font-size:.76rem;font-weight:800;letter-spacing:.04em;text-transform:uppercase;opacity:.76}
      .r3-validation-card-body h4{margin:.5rem 0 .55rem;font-size:1.08rem;line-height:1.28}
      .r3-validation-card-body p{margin:0;line-height:1.55;font-size:.92rem}
      .r3-validation-links{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:auto;padding-top:.85rem}
      .r3-validation-links a{display:inline-flex;align-items:center;padding:.5rem .7rem;border:1px solid rgba(120,140,170,.3);border-radius:999px;text-decoration:none;font-size:.78rem;font-weight:800}
      @media(max-width:820px){.r3-validation-grid{grid-template-columns:1fr}.r3-validation-card img{height:auto;max-height:460px}.r3-validation-card>a{min-height:260px}}
    `;
    document.head.appendChild(style);
  }

  function sourceLinks(record) {
    const context = `${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/${record.context}`;
    const figure = `${BLOB_PIN_PREFIX}${record.file}`;
    return `<div class="figure-source-links"><a href="${context}">Scientific context</a><a href="${figure}">Figure source</a></div>`;
  }

  function curatedCard(record) {
    return `
      <article class="program-visual-card" data-research-iii-curated-figure="docs/figures/${escapeHTML(record.file)}">
        <a href="${BLOB_PIN_PREFIX}${record.file}" aria-label="Open full-resolution ${escapeHTML(record.title)}"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}${record.file}" alt="Research III ${escapeHTML(record.title)}" /></a>
        <span>${escapeHTML(record.phase)}</span>
        <h3>${escapeHTML(record.title)}</h3>
        <p>${escapeHTML(record.summary)}</p>
        ${sourceLinks(record)}
      </article>`;
  }

  function completeCard(record) {
    return `
      <article class="complete-figure-card" data-research-iii-figure="docs/figures/${escapeHTML(record.file)}">
        <a href="${BLOB_PIN_PREFIX}${record.file}" aria-label="Open full-resolution ${escapeHTML(record.title)}"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}${record.file}" alt="Research III ${escapeHTML(record.title)}" /></a>
        <div class="complete-figure-card-body">
          <span class="figure-phase">Research III · ${escapeHTML(record.phase)}</span>
          <h4>${escapeHTML(record.title)}</h4>
          <p>${escapeHTML(record.summary)}</p>
          ${sourceLinks(record)}
        </div>
      </article>`;
  }

  function validationCard(record) {
    return `
      <article class="r3-validation-card" data-research-iii-validation-figure="docs/figures/${escapeHTML(record.file)}">
        <a href="${BLOB_PIN_PREFIX}${record.file}" aria-label="Open full-resolution ${escapeHTML(record.title)}"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}${record.file}" alt="Research III ${escapeHTML(record.title)}" /></a>
        <div class="r3-validation-card-body">
          <span>${escapeHTML(record.phase)}</span>
          <h4>${escapeHTML(record.title)}</h4>
          <p>${escapeHTML(record.summary)}</p>
          <div class="r3-validation-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/${record.context}">Derivation</a><a href="${BLOB_PIN_PREFIX}${record.file}">Figure source</a></div>
        </div>
      </article>`;
  }

  function addFigureMetrics(section) {
    const metrics = section.querySelector('.program-record-grid');
    if (!metrics) return;
    if (!metrics.querySelector('[data-research-iii-figure-count]')) {
      const metric = document.createElement('div');
      metric.className = 'program-record-metric';
      metric.dataset.researchIiiFigureCount = '9';
      metric.innerHTML = '<strong>9</strong><span>foundational scientific visuals</span>';
      metrics.appendChild(metric);
    }
    if (!metrics.querySelector('[data-research-iii-validation-count]')) {
      const metric = document.createElement('div');
      metric.className = 'program-record-metric';
      metric.dataset.researchIiiValidationCount = '10';
      metric.innerHTML = '<strong>10</strong><span>formal validation result figures</span>';
      metrics.appendChild(metric);
    }
  }

  function renderResearchIIIAtlas() {
    if (currentFile() !== 'visual-atlas.html') return false;
    const section = document.getElementById('research-iii-visual-program');
    if (!section) return false;

    addFigureMetrics(section);
    const legacyShowcase = section.querySelector(':scope > .program-visual-grid');
    if (legacyShowcase) {
      legacyShowcase.hidden = true;
      legacyShowcase.setAttribute('aria-hidden', 'true');
    }

    document.getElementById('research-iii-complete-figure-gallery')?.remove();
    document.getElementById('research-iii-curated-visual-story')?.remove();
    document.getElementById('research-iii-validation-figure-gallery')?.remove();

    const boundary = section.querySelector('.boundary');
    const curated = FOUNDATION_FIGURES.filter((record) => CURATED_FILES.has(record.file));

    const story = document.createElement('div');
    story.id = 'research-iii-curated-visual-story';
    story.className = 'complete-record-block';
    story.innerHTML = `
      <div class="complete-record-head">
        <div><span class="record-badge">Curated Research III visual path</span><h3>From declared target to an auditable scientific claim</h3><p>Read these six architecture visuals first. They define the target, evidence, uncertainty, validation, and falsification logic before any numerical result is interpreted.</p></div>
        <span class="record-badge">6-stage visual path</span>
      </div>
      <div class="program-visual-grid">${curated.map(curatedCard).join('')}</div>`;

    const complete = document.createElement('div');
    complete.id = 'research-iii-complete-figure-gallery';
    complete.className = 'complete-record-block';
    complete.innerHTML = `
      <div class="complete-record-head">
        <div><span class="record-badge">Foundational architecture</span><h3>All 9 foundational Research III visuals</h3><p>The complete architecture record from validated Research III revision ${RESEARCH_III_PIN.slice(0, 8)}.</p></div>
        <span class="record-badge">9 / 9 visible</span>
      </div>
      <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/visual-research-guide.md">Architecture visual guide</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/figure-catalog.md">Figure catalog</a></div>
      <div class="complete-figure-grid">${FOUNDATION_FIGURES.map(completeCard).join('')}</div>`;

    const validation = document.createElement('div');
    validation.id = 'research-iii-validation-figure-gallery';
    validation.className = 'r3-validation-record';
    validation.innerHTML = `
      <div class="r3-validation-head">
        <div><span class="record-badge">Executable formal validation</span><h3>V1-V10 result record</h3><p>Ten code-generated result figures connect the mathematical program to deterministic simulations, failure tests, machine-readable outputs, and reproducible source code.</p></div>
        <span class="record-badge">10 / 10 visible</span>
      </div>
      <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/VALIDATION.md">V1-V10 program</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/validation-atlas.md">Validation atlas</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/results/README.md">Machine-readable results</a></div>
      <div class="r3-validation-grid">${VALIDATION_FIGURES.map(validationCard).join('')}</div>`;

    if (boundary) {
      boundary.insertAdjacentElement('beforebegin', story);
      boundary.insertAdjacentElement('beforebegin', complete);
      boundary.insertAdjacentElement('beforebegin', validation);
    } else {
      section.append(story, complete, validation);
    }
    return true;
  }

  function renderResearchIIISources() {
    if (currentFile() !== 'sources.html') return false;
    const section = document.getElementById('research-iii-source-program');
    if (!section) return false;
    if (document.getElementById('research-iii-source-validation-gallery')) return true;

    const block = document.createElement('div');
    block.id = 'research-iii-source-validation-gallery';
    block.className = 'r3-validation-record';
    block.innerHTML = `
      <div class="r3-validation-head">
        <div><span class="source-visual-badge">Research III executable evidence</span><h3>Formal validation V1-V10: figures, equations, code, tests, and result files</h3><p>The architecture sources remain separate from the result record. This block exposes the ten validation figures and links each one back to its formal derivation at the exact validated Research III commit.</p></div>
        <span class="source-visual-badge">10 result figures</span>
      </div>
      <div class="source-section-visual-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/VALIDATION.md">Validation program</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/validation-atlas.md">Validation atlas</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/results/README.md">Result index</a><a href="${MEASUREMENT_REPO}/tree/${RESEARCH_III_PIN}/tests">Tests</a></div>
      <div class="r3-validation-grid">${VALIDATION_FIGURES.map(validationCard).join('')}</div>`;

    const existing = document.getElementById('research-iii-source-complete-figure-gallery');
    if (existing) existing.insertAdjacentElement('afterend', block);
    else section.appendChild(block);
    return true;
  }

  function refresh() {
    ensureStyles();
    repinResearchIIIAssets();
    const atlasReady = renderResearchIIIAtlas();
    const sourcesReady = renderResearchIIISources();
    repinResearchIIIAssets();
    return atlasReady || sourcesReady;
  }

  function scheduleRefresh() {
    refresh();
    [50, 150, 400, 900, 1600].forEach((delay) => window.setTimeout(refresh, delay));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', scheduleRefresh, { once: true });
  } else {
    scheduleRefresh();
  }
})();

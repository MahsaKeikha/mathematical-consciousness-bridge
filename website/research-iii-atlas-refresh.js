(() => {
  const RESEARCH_III_PIN = '7a2a1a3a60263e48b7a268642eecc6941e84d1b4';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const RAW_PIN_PREFIX =
    `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${RESEARCH_III_PIN}/docs/figures/`;
  const BLOB_PIN_PREFIX =
    `https://github.com/MahsaKeikha/consciousness-measurement-science/blob/${RESEARCH_III_PIN}/docs/figures/`;
  const RESULT_PIN_PREFIX =
    `${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/results/`;

  const LEGACY_PINS = [
    '3cf9202977953644c980246c1f3e46a3514b3a4a',
    '5d1d979231aed62fde34383281fa8f252a3d2fa7',
    'b874eda1f6940f5601b7f89200b6a276b5ecbbc3',
    '8bbb7b029d70c43cc6a9dbf8b44dfe5069d0993d',
    '7a106820158e0d33ea651f7cdeaa505206f1ccc7',
    'a9ef67ed15595c26b0c9f4e449f53f8078d6a1ee',
    '64b2bc47461fe110b135080f8dc70883552d6fd9',
  ];

  const FOUNDATION_FIGURES = [
    {
      title: 'Research III program map',
      file: 'research_program_map.svg',
      context: 'docs/measurement-framework.md',
      phase: 'Whole-program architecture',
      summary: 'Declared experiential targets are separated from observable evidence, assumptions, identification, validation, and the final claim ceiling.',
    },
    {
      title: 'Target-specific evidence matrix',
      file: 'target_evidence_matrix.svg',
      context: 'docs/measurement-instrument-spec.md',
      phase: 'Target and evidence design',
      summary: 'A channel can be informative for one target and insufficient for another, preventing cross-target category errors.',
    },
    {
      title: 'Consciousness measurement architecture',
      file: 'measurement_architecture.svg',
      context: 'docs/measurement-framework.md',
      phase: 'Measurement architecture',
      summary: 'The declared latent target remains distinct from report, behavior, neural activity, perturbation, physiology, context, and intervention.',
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
      result: 'finite_sample_coverage.csv',
      phase: 'V2 · finite-sample identification',
      summary: 'The outer identified interval contracts with deployment sample size while retaining declared calibration uncertainty.',
    },
    {
      title: 'Finite-sample coverage',
      file: 'finite_sample_coverage.svg',
      context: 'docs/formal-validation-program.md',
      result: 'finite_sample_coverage.csv',
      phase: 'V2 · coverage',
      summary: 'Repeated fixed-seed sampling checks whether the declared finite-sample interval covers the known synthetic target.',
    },
    {
      title: 'Calibration transport bias',
      file: 'transport_bias_surface.svg',
      context: 'docs/formal-validation-program.md',
      result: 'transport_stress.csv',
      phase: 'V3 · transport',
      summary: 'The stress surface shows exact latent-contrast bias when sensitivity or specificity shifts but baseline calibration is reused.',
    },
    {
      title: 'Conditional-dependence stress',
      file: 'dependence_stress.svg',
      context: 'docs/formal-validation-program.md',
      result: 'dependence_stress.csv',
      phase: 'V4 · dependence',
      summary: 'A correlated-channel construction preserves marginal calibration while exposing false confidence from naive likelihood-ratio multiplication.',
    },
    {
      title: 'Structural alignment null and power',
      file: 'structural_alignment_power.svg',
      context: 'docs/formal-validation-program.md',
      result: 'structural_alignment_power.csv',
      phase: 'V5 · structural falsification',
      summary: 'Permutation testing is checked under a null construction and under increasing planted relational correspondence.',
    },
    {
      title: 'Finite calibration-sample uncertainty',
      file: 'calibration_sample_uncertainty.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      result: 'calibration_sample_uncertainty.csv',
      phase: 'V6 · calibration samples',
      summary: 'Sensitivity and specificity are estimated from finite reference samples, making calibration sample size part of the uncertainty budget.',
    },
    {
      title: 'Missingness identification loss',
      file: 'missingness_identification_loss.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      result: 'missingness_stress.csv',
      phase: 'V7 · arbitrary missingness',
      summary: 'Sharp worst-case bounds widen as outcomes go missing without a missing-at-random assumption; missing data are not converted into negative evidence.',
    },
    {
      title: 'Inverse conditioning by Youden margin',
      file: 'inverse_conditioning_youden.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      result: 'conditioning_stress.csv',
      phase: 'V8 · inverse conditioning',
      summary: 'The exact 1/J amplification law shows when an algebraically invertible channel becomes numerically unstable.',
    },
    {
      title: 'Two-site partial identification',
      file: 'two_site_partial_identification.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      result: 'two_site_nonidentifiability.csv',
      phase: 'V9 · site heterogeneity',
      summary: 'Different site calibration makes one pooled observable compatible with a range of population-average latent prevalences.',
    },
    {
      title: 'Resolution abstention frontier',
      file: 'resolution_abstention_frontier.svg',
      context: 'docs/formal-validation-program-v6-v10.md',
      result: 'resolution_abstention_frontier.csv',
      phase: 'V10 · resolution-aware abstention',
      summary: 'A predeclared width threshold controls when an interval is precise enough to release; marginal coverage controls erroneous releases, while conditional coverage is assessed separately.',
    },
    {
      title: 'Missingness information law',
      file: 'v11_missingness_information_law.svg',
      context: 'docs/formal-validation-program-v11-v15.md',
      result: 'v11_missingness_information_law.csv',
      phase: 'V11 · exact information loss',
      summary: 'Away from boundary clipping and with known positive calibration, the exact latent identified-set width equals the missing fraction divided by the Youden information margin.',
    },
    {
      title: 'Multisite identification under heterogeneous information',
      file: 'v12_v13_multisite_heterogeneity.svg',
      context: 'docs/formal-validation-program-v11-v15.md',
      result: 'v12_v13_multisite_identification.csv',
      phase: 'V12-V13 · multisite identification',
      summary: 'The population-average latent prevalence is point-identified from the pooled rate when site information margins are equal and becomes sharply set-identified as slope heterogeneity grows.',
    },
    {
      title: 'Resolution sample-size law',
      file: 'v14_resolution_sample_size.svg',
      context: 'docs/formal-validation-program-v11-v15.md',
      result: 'v14_resolution_sample_size.csv',
      phase: 'V14 · engineering design law',
      summary: 'The sufficient deployment sample size rises quadratically as the requested latent resolution tightens and as the measurement channel weakens.',
    },
    {
      title: 'Independent pilot gate',
      file: 'v15_independent_pilot_gate.svg',
      context: 'docs/formal-validation-program-v11-v15.md',
      result: 'v15_independent_pilot_gate.csv',
      phase: 'V15 · selection-safe release design',
      summary: 'Pilot data decide whether to proceed, while an independent confirmatory interval preserves its validity among released designs. The fixed-seed record is byte-stable across supported Python and NumPy environments.',
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
      'github.com/MahsaKeikha/consciousness-measurement-science/tree/main/',
      `github.com/MahsaKeikha/consciousness-measurement-science/tree/${RESEARCH_III_PIN}/`,
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
      #research-iii-validation-figure-gallery .r3-validation-grid{grid-template-columns:repeat(4,minmax(0,1fr))}
      #research-iii-validation-figure-gallery .r3-validation-card>a{min-height:190px}
      #research-iii-validation-figure-gallery .r3-validation-card img{height:210px}
      #research-iii-validation-figure-gallery .r3-validation-card-body{padding:.9rem}
      #research-iii-validation-figure-gallery .r3-validation-card-body h4{font-size:1rem}
      #research-iii-validation-figure-gallery .r3-validation-card-body p{font-size:.86rem}
      .r3-validation-card{display:flex;flex-direction:column;border:1px solid rgba(120,140,170,.24);border-radius:16px;overflow:hidden;background:rgba(255,255,255,.02)}
      .r3-validation-card>a{display:flex;align-items:center;justify-content:center;min-height:320px;padding:.35rem;background:#fff}
      .r3-validation-card img{display:block;width:100%;height:340px;object-fit:contain;background:#fff}
      .r3-validation-card-body{display:flex;flex-direction:column;flex:1;padding:1rem 1.05rem 1.1rem}
      .r3-validation-card-body span{font-size:.76rem;font-weight:800;letter-spacing:.04em;text-transform:uppercase;opacity:.76}
      .r3-validation-card-body h4{margin:.5rem 0 .55rem;font-size:1.08rem;line-height:1.28}
      .r3-validation-card-body p{margin:0;line-height:1.55;font-size:.92rem}
      .r3-validation-links{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:auto;padding-top:.85rem}
      .r3-validation-links a{display:inline-flex;align-items:center;padding:.5rem .7rem;border:1px solid rgba(120,140,170,.3);border-radius:999px;text-decoration:none;font-size:.78rem;font-weight:800}
      .r3-stage-extension{margin-top:2.4rem}
      .r3-stage-extension .section-head{max-width:980px;margin-bottom:1.35rem}
      .r3-design-panel{overflow:hidden;border:1px solid rgba(120,140,170,.30);border-radius:20px;background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(247,249,253,.96));box-shadow:0 14px 34px rgba(31,45,78,.06)}
      .r3-design-panel-head{display:grid;grid-template-columns:84px minmax(220px,.95fr) minmax(260px,1.15fr);gap:18px;padding:14px 20px;border-bottom:1px solid rgba(120,140,170,.22);background:rgba(239,243,250,.72);font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#526071}
      .r3-design-row{display:grid;grid-template-columns:84px minmax(220px,.95fr) minmax(260px,1.15fr);gap:18px;align-items:start;padding:20px;border-bottom:1px solid rgba(120,140,170,.18)}
      .r3-design-row:last-child{border-bottom:0}
      .r3-design-stage{display:flex;align-items:center;justify-content:center;width:54px;height:54px;border:1px solid rgba(54,91,160,.30);border-radius:50%;background:#fff;font-weight:800;color:#2e5799;letter-spacing:.03em}
      .r3-design-result h3{margin:0 0 8px;font-size:1rem;line-height:1.35;color:#182235}
      .r3-design-equation{display:inline-block;padding:5px 9px;border-radius:7px;background:#edf2fa;color:#233f72;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.82rem;line-height:1.45}
      .r3-design-meaning p{margin:0;color:#536174;font-size:.91rem;line-height:1.58}
      .r3-design-note{margin-top:12px;padding:11px 14px;border-left:3px solid rgba(54,91,160,.55);background:rgba(241,245,252,.7);color:#4a586a;font-size:.85rem;line-height:1.5}
      .r3-design-checkpoints{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin-top:16px;border:1px solid rgba(120,140,170,.24);border-radius:16px;background:#fff;overflow:hidden}
      .r3-design-checkpoint{padding:17px 18px;border-right:1px solid rgba(120,140,170,.18)}
      .r3-design-checkpoint:last-child{border-right:0}
      .r3-design-checkpoint span{display:block;margin-bottom:5px;font-size:.68rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#5f6d80}
      .r3-design-checkpoint strong{display:block;margin-bottom:6px;font-size:1.25rem;line-height:1.1;color:#172133}
      .r3-design-checkpoint p{margin:0;color:#596778;font-size:.79rem;line-height:1.45}
      @media(max-width:1180px){#research-iii-validation-figure-gallery .r3-validation-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.r3-design-checkpoints{grid-template-columns:repeat(2,minmax(0,1fr))}.r3-design-checkpoint:nth-child(2){border-right:0}.r3-design-checkpoint:nth-child(-n+2){border-bottom:1px solid rgba(120,140,170,.18)}}
      @media(max-width:900px){.r3-design-panel-head{display:none}.r3-design-row{grid-template-columns:68px 1fr;gap:14px}.r3-design-meaning{grid-column:2}.r3-design-stage{width:48px;height:48px}}
      @media(max-width:820px){.r3-validation-grid{grid-template-columns:1fr}.r3-validation-card img{height:auto;max-height:460px}.r3-validation-card>a{min-height:260px}}
      @media(max-width:680px){#research-iii-validation-figure-gallery .r3-validation-grid{grid-template-columns:1fr}#research-iii-validation-figure-gallery .r3-validation-card img{height:auto;max-height:460px}#research-iii-validation-figure-gallery .r3-validation-card>a{min-height:260px}.r3-design-checkpoints{grid-template-columns:1fr}.r3-design-checkpoint{border-right:0;border-bottom:1px solid rgba(120,140,170,.18)}.r3-design-checkpoint:last-child{border-bottom:0}.r3-design-row{grid-template-columns:1fr;padding:17px}.r3-design-stage{width:auto;height:auto;justify-content:flex-start;border:0;background:transparent}.r3-design-meaning{grid-column:auto}}
    `;
    document.head.appendChild(style);
  }

  function sourceLinks(record) {
    const context = `${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/${record.context}`;
    const figure = `${BLOB_PIN_PREFIX}${record.file}`;
    const result = record.result ? `${RESULT_PIN_PREFIX}${record.result}` : null;
    return `<div class="figure-source-links"><a href="${context}">Scientific context</a>${result ? `<a href="${result}">Result data</a>` : ''}<a href="${figure}">Figure source</a></div>`;
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
          <span>${escapeHTML(record.phase)} · analytic/synthetic validation</span>
          <h4>${escapeHTML(record.title)}</h4>
          <p>${escapeHTML(record.summary)}</p>
          <div class="r3-validation-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/${record.context}">Derivation</a><a href="${RESULT_PIN_PREFIX}${record.result}">Result data</a><a href="${BLOB_PIN_PREFIX}${record.file}">Figure source</a></div>
        </div>
      </article>`;
  }

  function setMetric(metrics, selector, value, label) {
    let metric = metrics.querySelector(selector);
    if (!metric) {
      metric = document.createElement('div');
      metric.className = 'program-record-metric';
      metrics.appendChild(metric);
    }
    metric.setAttribute(selector.match(/\[([^=\]]+)/)?.[1] || 'data-research-iii-metric', String(value));
    metric.innerHTML = `<strong>${value}</strong><span>${label}</span>`;
  }

  function addFigureMetrics(section) {
    const metrics = section.querySelector('.program-record-grid');
    if (!metrics) return;
    const architecture = metrics.querySelector('[data-research-iii-figure-count]');
    if (architecture) architecture.innerHTML = '<strong>9</strong><span>foundational scientific visuals</span>';
    else {
      const metric = document.createElement('div');
      metric.className = 'program-record-metric';
      metric.dataset.researchIiiFigureCount = '9';
      metric.innerHTML = '<strong>9</strong><span>foundational scientific visuals</span>';
      metrics.appendChild(metric);
    }
    const validation = metrics.querySelector('[data-research-iii-validation-count]');
    if (validation) validation.innerHTML = '<strong>14</strong><span>formal validation result figures</span>';
    else {
      const metric = document.createElement('div');
      metric.className = 'program-record-metric';
      metric.dataset.researchIiiValidationCount = '14';
      metric.innerHTML = '<strong>14</strong><span>formal validation result figures</span>';
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
        <div><span class="record-badge">Executable formal validation</span><h3>V1-V15 result record</h3><p>Fourteen code-generated result figures connect the mathematical program to deterministic simulations, exact design laws, failure tests, machine-readable outputs, and reproducible source code.</p></div>
        <span class="record-badge">14 / 14 visible</span>
      </div>
      <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/VALIDATION.md">V1-V15 program</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/validation-atlas.md">Validation atlas</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/results/README.md">Machine-readable results</a></div>
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
    document.getElementById('research-iii-source-validation-gallery')?.remove();

    const block = document.createElement('div');
    block.id = 'research-iii-source-validation-gallery';
    block.className = 'r3-validation-record';
    block.innerHTML = `
      <div class="r3-validation-head">
        <div><span class="source-visual-badge">Research III executable evidence</span><h3>Formal validation V1-V15: derivations, result data, figures, code, and tests</h3><p>The architecture sources remain separate from the result record. Every validation figure below is pinned to the same verified Research III commit and links to its formal derivation, exact machine-readable result file, and figure source.</p></div>
        <span class="source-visual-badge">14 result figures</span>
      </div>
      <div class="source-section-visual-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/VALIDATION.md">Validation program</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/validation-atlas.md">Validation atlas</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/results/README.md">Result index</a><a href="${MEASUREMENT_REPO}/tree/${RESEARCH_III_PIN}/tests">98-test suite</a></div>
      <div class="r3-validation-grid">${VALIDATION_FIGURES.map(validationCard).join('')}</div>`;

    const existing = document.getElementById('research-iii-source-complete-figure-gallery');
    if (existing) existing.insertAdjacentElement('afterend', block);
    else section.appendChild(block);
    return true;
  }

  function findSectionByText(pattern) {
    return [...document.querySelectorAll('main > section')].find((section) => pattern.test(section.textContent));
  }

  function renderResearchIIIMeasurementPage() {
    if (currentFile() !== 'measurement-science.html') return false;
    repinResearchIIIAssets();

    const status = document.querySelector('.status-grid');
    if (status) {
      const cells = status.querySelectorAll(':scope > div');
      if (cells[0]) cells[0].innerHTML = '<strong>V1-V15</strong><span>formal validation stages</span>';
      if (cells[1]) cells[1].innerHTML = '<strong>23</strong><span>scientific visuals: 9 architecture + 14 validation</span>';
      if (cells[2]) cells[2].innerHTML = '<strong>98</strong><span>tests in each CI job</span>';
      if (cells[3]) cells[3].innerHTML = '<strong>3</strong><span>Python versions in the CI matrix</span>';
    }

    const primary = document.querySelector('.hero-actions .button.primary');
    if (primary) {
      primary.textContent = 'Open V1-V15 validation program';
      primary.href = `${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/VALIDATION.md`;
    }

    const follow = document.querySelector('.source-grid a:first-child p');
    if (follow) follow.textContent = 'The compact V1-V15 map: scientific question, mathematical object, executable evidence, result record, and failure condition.';

    document.getElementById('formal-validation-v11-v15')?.remove();
    const baseStages = document.getElementById('formal-validation-v1-v10');
    if (baseStages) {
      const extension = document.createElement('section');
      extension.id = 'formal-validation-v11-v15';
      extension.className = 'r3-stage-extension';
      extension.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">Formal validation V11-V15</p>
          <h2>From identification limits to measurement design</h2>
          <p>Five formal results turn the robustness analysis into quantities an experimenter can design around: information loss from missingness, the exact condition for pooled multisite identification, sharp set identification when that condition fails, finite-sample resolution planning, and a release design that separates selection from confirmation.</p>
        </div>
        <div class="r3-design-panel" aria-label="Research III V11 to V15 theorem and design map">
          <div class="r3-design-panel-head" aria-hidden="true"><span>Stage</span><span>Formal result</span><span>Scientific consequence</span></div>
          <article class="r3-design-row" data-v11-v15-design-stage="V11">
            <div class="r3-design-stage">V11</div>
            <div class="r3-design-result"><h3>Exact missingness resolution law</h3><span class="r3-design-equation">W<sub>miss</sub> = (m/N)/J</span></div>
            <div class="r3-design-meaning"><p>With known positive calibration and away from boundary clipping, arbitrary missing outcomes widen the sharp latent identified set by exactly the missing fraction divided by the channel information margin.</p></div>
          </article>
          <article class="r3-design-row" data-v11-v15-design-stage="V12">
            <div class="r3-design-stage">V12</div>
            <div class="r3-design-result"><h3>Pooled multisite point identification</h3><span class="r3-design-equation">J<sub>1</sub> = ... = J<sub>K</sub></span></div>
            <div class="r3-design-meaning"><p>One pooled proxy rate identifies the population-average latent prevalence for every feasible site mixture if and only if the site information slopes are equal.</p></div>
          </article>
          <article class="r3-design-row" data-v11-v15-design-stage="V13">
            <div class="r3-design-stage">V13</div>
            <div class="r3-design-result"><h3>Sharp K-site partial identification</h3><span class="r3-design-equation">pi-bar in [L<sub>sharp</sub>, U<sub>sharp</sub>]</span></div>
            <div class="r3-design-meaning"><p>When site slopes differ, the exact population-average interval is obtained by allocating constraint mass in the order implied by the site information margins, with at most one fractional site.</p></div>
          </article>
          <article class="r3-design-row" data-v11-v15-design-stage="V14">
            <div class="r3-design-stage">V14</div>
            <div class="r3-design-result"><h3>Resolution-driven sample design</h3><span class="r3-design-equation">n &gt;= 2 log(2/delta)/(J<sup>2</sup> omega<sup>2</sup>)</span></div>
            <div class="r3-design-meaning"><p>The sufficient deployment size grows quadratically as the requested latent interval narrows and as the measurement channel weakens.</p></div>
          </article>
          <article class="r3-design-row" data-v11-v15-design-stage="V15">
            <div class="r3-design-stage">V15</div>
            <div class="r3-design-result"><h3>Selection-safe release design</h3><span class="r3-design-equation">P(C | G) = P(C) &gt;= 1 - delta</span></div>
            <div class="r3-design-meaning"><p>An independent pilot may decide whether to proceed while fresh confirmatory data retain the stated coverage guarantee among released designs.</p></div>
          </article>
        </div>
        <div class="r3-design-note"><strong>Interpretation boundary.</strong> These results are properties of the declared imperfect-proxy measurement model. They do not supply empirical calibration for a consciousness biomarker.</div>
        <div class="r3-design-checkpoints" aria-label="Canonical V11 to V15 numerical checkpoints">
          <article class="r3-design-checkpoint"><span>V11 checkpoint</span><strong>0.1333</strong><p>Exact interior width at 10% missingness with J = 0.75.</p></article>
          <article class="r3-design-checkpoint"><span>V12-V13 checkpoint</span><strong>0 to 0.3333</strong><p>Point identification at equal information slopes; sharp-set width at spread 0.30.</p></article>
          <article class="r3-design-checkpoint"><span>V14 checkpoint</span><strong>n = 1312</strong><p>Sufficient size for J = 0.75, 95% coverage, and latent width at most 0.10.</p></article>
          <article class="r3-design-checkpoint"><span>V15 checkpoint</span><strong>47.25%</strong><p>Fixed-seed pilot release rate at planned confirmatory n = 900.</p></article>
        </div>`;
      baseStages.insertAdjacentElement('afterend', extension);
    }

    document.getElementById('v11-v15-result-figures')?.remove();
    const v6Section = findSectionByText(/V6-V10 robustness figures/);
    if (v6Section) {
      const figures = document.createElement('section');
      figures.id = 'v11-v15-result-figures';
      figures.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V11-V15 design-law figures</p>
          <h2>Exact information loss, multisite identification, sample-size design, and selection-safe release</h2>
          <p>These figures are generated by the third deterministic validation runner from the committed CSV/JSON result record at Research III revision ${RESEARCH_III_PIN.slice(0, 8)}.</p>
        </div>
        <div class="measurement-figure-grid">${VALIDATION_FIGURES.slice(10).map((record) => `
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}${record.file}"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}${record.file}" alt="Research III ${escapeHTML(record.title)}" /></a>
            <p class="eyebrow">${escapeHTML(record.phase)}</p>
            <h3>${escapeHTML(record.title)}</h3>
            <p>${escapeHTML(record.summary)}</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/${record.context}">Derivation</a><a href="${RESULT_PIN_PREFIX}${record.result}">Result data</a><a href="${BLOB_PIN_PREFIX}${record.file}">Figure source</a></div>
          </article>`).join('')}</div>
        <div class="r3-design-law-grid">
          <article><strong>V11: 0.1333 width</strong><p>At 10% missingness and J = 0.75, the exact interior identified-set width is 0.1333.</p></article>
          <article><strong>V12-V13: 0 to 0.3333</strong><p>Equal site information margins give point identification in the canonical design; a 0.30 slope spread widens the sharp set to 0.3333.</p></article>
          <article><strong>V14: n = 1312</strong><p>For J = 0.75, a 95% Hoeffding guarantee with latent width at most 0.10 requires a sufficient deployment size of 1312.</p></article>
          <article><strong>V15: 47.25% release at n = 900</strong><p>The stable fixed-seed pilot gate releases 756 of 1600 designs at planned confirmatory n = 900; confirmatory coverage is evaluated only on independent confirmatory data.</p></article>
        </div>`;
      v6Section.insertAdjacentElement('afterend', figures);
    }

    const reproduction = findSectionByText(/Two deterministic runners regenerate|Reproducibility/);
    if (reproduction) {
      const heading = reproduction.querySelector('h2');
      if (heading && heading.textContent.includes('Two deterministic runners')) {
        heading.textContent = 'Three deterministic runners regenerate the validation results and figures';
      }
      const firstColumn = reproduction.querySelector('.two-col > div');
      if (firstColumn && !firstColumn.querySelector('[data-v11-v15-runner]')) {
        const p = document.createElement('p');
        p.dataset.v11V15Runner = 'true';
        p.innerHTML = '<strong>V11-V15 runner:</strong> <code>python scripts/run_identification_design_validation.py</code>';
        const wholeRepo = [...firstColumn.querySelectorAll('p')].find((node) => node.textContent.includes('Whole repository'));
        if (wholeRepo) wholeRepo.insertAdjacentElement('beforebegin', p);
        else firstColumn.appendChild(p);
      }
    }

    repinResearchIIIAssets();
    return true;
  }

  function renderHomepageMetrics() {
    if (currentFile() !== 'index.html') return false;
    const programCard = [...document.querySelectorAll('.research-program-card')].find((card) =>
      card.textContent.includes('Research III · Consciousness measurement science')
    );
    if (!programCard) return false;
    const metric = programCard.querySelector('.research-program-metric');
    const meta = programCard.querySelector('.research-program-meta');
    if (metric) metric.innerHTML = '<strong>98</strong><span>tests in each CI job</span>';
    if (meta) meta.textContent = 'V1-V15 formal validation · 23 scientific visuals · 3 deterministic runners';
    return true;
  }

  function refresh() {
    ensureStyles();
    repinResearchIIIAssets();
    const ready = [
      renderResearchIIIAtlas(),
      renderResearchIIISources(),
      renderResearchIIIMeasurementPage(),
      renderHomepageMetrics(),
    ].some(Boolean);
    repinResearchIIIAssets();
    return ready;
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

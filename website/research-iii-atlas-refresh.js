(() => {
  const RESEARCH_III_PIN = '89581ff150d768998967500d079d7ba61deafe86';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const RAW_PIN_PREFIX =
    `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${RESEARCH_III_PIN}/docs/figures/`;
  const BLOB_PIN_PREFIX =
    `https://github.com/MahsaKeikha/consciousness-measurement-science/blob/${RESEARCH_III_PIN}/docs/figures/`;
  const RESULT_PIN_PREFIX =
    `${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/results/`;

  const LEGACY_PINS = ['edc1db943d6efe8bdc679dbc5d77ecb7633476ab'];


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
    {
      title: 'Electromagnetic observables and confound validation',
      file: 'v16_v20_electromagnetic_validation.svg',
      context: 'docs/electromagnetic-field-program.md',
      result: 'electromagnetic_validation_summary.json',
      phase: 'V16-V20 · electromagnetic measurement arm',
      summary: 'Physical EM sanity checks, gain-invariant organization features, matched-power non-identifiability, common-mode confound stress, and frequency-specific structure are validated without treating any field statistic as consciousness itself.',
    },
    {
      title: 'Electromagnetic forward and inverse source limits',
      file: 'v21_v25_electromagnetic_inverse_validation.svg',
      context: 'docs/electromagnetic-source-identifiability.md',
      result: 'electromagnetic_inverse_validation_summary.json',
      phase: 'V21-V25 · electromagnetic source identifiability',
      summary: 'Reference invariance, exact lead-field source non-identifiability, inverse regularization sensitivity, multimodal null-space reduction, and forward-model perturbation are validated without treating one reconstructed source as uniquely true.',
    },
    {
      title: 'Electromagnetic resolution and information limits',
      file: 'v26_v30_electromagnetic_resolution_validation.svg',
      context: 'docs/electromagnetic-resolution-program.md',
      result: 'electromagnetic_resolution_validation_summary.json',
      phase: 'V26-V30 · electromagnetic resolution and information',
      summary: 'Covariance-aware residual geometry, a rank-limited resolution floor, Fisher-information loss, exact temporal aliasing, and weakest-singular-direction noise amplification are validated without treating any resolution statistic as consciousness.',
    },
    {
      title: 'Electromagnetic design and spatial specificity',
      file: 'v31_v35_electromagnetic_design_validation.svg',
      context: 'docs/electromagnetic-design-spatial-specificity.md',
      result: 'electromagnetic_design_validation_summary.json',
      phase: 'V31-V35 · electromagnetic design and spatial specificity',
      summary: 'Point-spread and cross-talk, covariance-aware source distinguishability, Fisher-information sensor design, nuisance-subspace information loss, and robust model uncertainty are validated without treating any design statistic as consciousness.',
    },
    {
      title: 'Finite-sample electromagnetic inference',
      file: 'v36_v40_electromagnetic_finite_sample_validation.svg',
      context: 'docs/electromagnetic-finite-sample-inference.md',
      result: 'electromagnetic_finite_sample_validation_summary.json',
      phase: 'V36-V40 · finite-sample electromagnetic inference',
      summary: 'GLS efficiency, inverse-covariance bias, Gaussian source discrimination, independent-search family-wise error control, and covariance-mismatch calibration are validated without treating statistical significance as consciousness.',
    },
    {
      title: 'Multiplicity and selection-safe electromagnetic inference',
      file: 'v41_v45_electromagnetic_selection_validation.svg',
      context: 'docs/electromagnetic-selection-safe-inference.md',
      result: 'electromagnetic_selection_validation_summary.json',
      phase: 'V41-V45 · multiplicity and selection-safe inference',
      summary: 'Bonferroni and Holm family-wise error control, exact sign-flip inference, post-selection coverage collapse, and independent holdout confirmation are validated without treating statistical significance as consciousness evidence.',
    },
    {
      title: 'Cross-site replication inference and stability',
      file: 'v46_v50_electromagnetic_replication_validation.svg',
      context: 'docs/electromagnetic-replication-inference.md',
      result: 'electromagnetic_replication_validation_summary.json',
      phase: 'V46-V50 · cross-site replication inference',
      summary: 'Common-effect pooling, heterogeneity calibration, leave-one-site-out influence, partial-conjunction replicability, and site-weight concentration are audited without treating synthetic sites as external empirical replication.',
    },
    {
      title: 'Transportability across sensors, hardware, and states',
      file: 'v51_v55_transportability_validation.svg',
      context: 'docs/transportability-program.md',
      result: 'transportability_validation_summary.json',
      phase: 'V51-V55 · transportability and distribution shift',
      summary: 'Coordinate invariance, projection information loss, cross-hardware topography mismatch, importance-weight overlap, and sharp total-variation transport budgets are audited without treating analytic transport laws as empirical generalization.',
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
      'github.com/MahsaKeikha/consciousness-measurement-science/blob/89581ff150d768998967500d079d7ba61deafe86/',
      `github.com/MahsaKeikha/consciousness-measurement-science/blob/${RESEARCH_III_PIN}/`,
    );
    updated = updated.replace(
      'github.com/MahsaKeikha/consciousness-measurement-science/tree/89581ff150d768998967500d079d7ba61deafe86/',
      `github.com/MahsaKeikha/consciousness-measurement-science/tree/${RESEARCH_III_PIN}/`,
    );
    updated = updated.replace(
      'raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/89581ff150d768998967500d079d7ba61deafe86/',
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
      .r3-stage-extension{margin-top:2rem}.r3-stage-extension .section-head{margin-bottom:1rem}
      .r3-design-law-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin-top:1rem}
      .r3-design-law-grid article{padding:18px;border:1px solid rgba(120,140,170,.25);border-radius:14px;background:rgba(255,255,255,.03)}
      .r3-design-law-grid strong{display:block;margin-bottom:7px;font-size:1.06rem}.r3-design-law-grid p{margin:0;line-height:1.55;font-size:.91rem}
      @media(max-width:1180px){#research-iii-validation-figure-gallery .r3-validation-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
      @media(max-width:820px){.r3-validation-grid{grid-template-columns:1fr}.r3-validation-card img{height:auto;max-height:460px}.r3-validation-card>a{min-height:260px}}
      @media(max-width:680px){#research-iii-validation-figure-gallery .r3-validation-grid{grid-template-columns:1fr}#research-iii-validation-figure-gallery .r3-validation-card img{height:auto;max-height:460px}#research-iii-validation-figure-gallery .r3-validation-card>a{min-height:260px}}
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
        <div><span class="record-badge">Executable formal validation</span><h3>V1-V55 result record</h3><p>Twenty-two code-generated result figures connect the mathematical program to deterministic simulations, exact design laws, failure tests, machine-readable outputs, and reproducible source code.</p></div>
        <span class="record-badge">22 / 22 visible</span>
      </div>
      <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/VALIDATION.md">V1-V55 program</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/validation-atlas.md">Validation atlas</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/results/README.md">Machine-readable results</a></div>
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
        <div><span class="source-visual-badge">Research III executable evidence</span><h3>Formal validation V1-V55: derivations, result data, figures, code, and tests</h3><p>The architecture sources remain separate from the result record. Every validation figure below is pinned to the same verified Research III commit and links to its formal derivation, exact machine-readable result file, and figure source.</p></div>
        <span class="source-visual-badge">22 result figures</span>
      </div>
      <div class="source-section-visual-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/VALIDATION.md">Validation program</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/validation-atlas.md">Validation atlas</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/results/README.md">Result index</a><a href="${MEASUREMENT_REPO}/tree/${RESEARCH_III_PIN}/tests">192-test suite</a></div>
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
      if (cells[0]) cells[0].innerHTML = '<strong>V1-V55</strong><span>formal validation stages</span>';
      if (cells[1]) cells[1].innerHTML = '<strong>31</strong><span>scientific visuals: 9 architecture + 22 validation</span>';
      if (cells[2]) cells[2].innerHTML = '<strong>192</strong><span>tests in each CI job</span>';
      if (cells[3]) cells[3].innerHTML = '<strong>3</strong><span>Python versions in the CI matrix</span>';
    }

    const primary = document.querySelector('.hero-actions .button.primary');
    if (primary) {
      primary.textContent = 'Open V1-V55 validation program';
      primary.href = `${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/VALIDATION.md`;
    }

    const follow = document.querySelector('.source-grid a:first-child p');
    if (follow) follow.textContent = 'The compact V1-V55 map: scientific question, mathematical object, executable evidence, result record, and failure condition.';

    document.getElementById('formal-validation-v11-v15')?.remove();
    const baseStages = document.getElementById('formal-validation-v1-v10');
    if (baseStages) {
      const extension = document.createElement('section');
      extension.id = 'formal-validation-v11-v15';
      extension.className = 'r3-stage-extension';
      extension.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">Formal validation V11-V15</p>
          <h2>From robustness diagnosis to explicit measurement-design laws</h2>
          <p>The second theorem layer asks how much information missingness destroys, when pooled multisite inference is point-identified, how to compute the sharp identified set when it is not, how resolution determines sample size, and how to separate design selection from confirmatory inference.</p>
        </div>
        <div class="result-grid">
          <article class="result"><span>V11</span><h3>Exact missingness law</h3><p>Derives the interior identified-set width as missing fraction divided by the Youden information margin under known positive calibration.</p></article>
          <article class="result"><span>V12</span><h3>Multisite point-identification criterion</h3><p>Gives the condition under which one pooled observable identifies the population-average latent prevalence: the site information margins must be equal.</p></article>
          <article class="result"><span>V13</span><h3>Sharp K-site identified set</h3><p>Computes the exact population-average interval when heterogeneous site slopes prevent point identification.</p></article>
          <article class="result"><span>V14</span><h3>Resolution sample-size law</h3><p>Converts requested latent resolution and channel strength into a sufficient finite-sample deployment size.</p></article>
          <article class="result"><span>V15</span><h3>Independent pilot release gate</h3><p>Uses pilot data only for the go/no-go decision and fresh confirmatory data for inference, preserving confirmatory validity among released designs.</p></article>
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
        <div class="measurement-figure-grid">${VALIDATION_FIGURES.slice(10, 14).map((record) => `
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

    document.getElementById('v16-v20-em-field-program')?.remove();
    const designSection = document.getElementById('v11-v15-result-figures');
    if (designSection) {
      const em = document.createElement('section');
      em.id = 'v16-v20-em-field-program';
      em.className = 'r3-stage-extension';
      em.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V16-V20 · Electromagnetic field measurement</p>
          <h2>Measure electromagnetic organization as a falsifiable evidence channel, not as a shortcut to consciousness</h2>
          <p>The new EM arm starts from measurable electric and magnetic observables, then tests organization descriptors, invariance, information loss, nuisance sensitivity, and frequency dependence before any consciousness-related interpretation is allowed.</p>
        </div>
        <div class="boundary">
          <p><strong>Scientific claim boundary:</strong> EEG, MEG, and other electromagnetic recordings can quantify physical and neural field dynamics. The present V16-V20 results establish measurement and synthetic validation properties only. They do not show that field strength, power, phase concentration, entropy, effective rank, or any other EM statistic is consciousness itself.</p>
        </div>
        <div class="measurement-figure-grid">
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}v16_v20_electromagnetic_validation.svg"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}v16_v20_electromagnetic_validation.svg" alt="Research III electromagnetic validation V16 to V20" /></a>
            <p class="eyebrow">V16-V20 · electromagnetic observables</p>
            <h3>Matched-power structure, common-mode confounding, and frequency specificity</h3>
            <p>V18 constructs equal-power fields with different spatial phase organization. V19 shows that a shared contaminant can create strong apparent global organization. V20 shows that the same multichannel signal can be aligned at one frequency and phase-balanced at another.</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/electromagnetic-field-program.md">Electromagnetic Field Measurement Program</a><a href="${RESULT_PIN_PREFIX}electromagnetic_validation_summary.json">Result record</a><a href="${BLOB_PIN_PREFIX}v16_v20_electromagnetic_validation.svg">Figure source</a></div>
          </article>
        </div>
        <div class="r3-design-law-grid">
          <article><strong>V17: gain invariance</strong><p>Normalized organization descriptors remain unchanged under global signal scaling in the declared deterministic construction.</p></article>
          <article><strong>V18: power is insufficient</strong><p>Channel power matches to numerical precision while spatial phase concentration changes from 1 to approximately 0.</p></article>
          <article><strong>V19: nuisance can mimic structure</strong><p>A shared contaminant raises raw phase concentration to about 0.935 in the canonical stress test.</p></article>
          <article><strong>V20: structure is frequency-specific</strong><p>The same signal is fully aligned at 10 Hz and phase-balanced at 17 Hz, ruling out an unqualified one-number field description.</p></article>
        </div>
        <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_observables.py">Observable code</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_simulations.py">Validation simulations</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/scripts/run_electromagnetic_validation.py">Reproduce V16-V20</a></div>`;
      designSection.insertAdjacentElement('afterend', em);
    }

    document.getElementById('v21-v25-em-source-identifiability')?.remove();
    document.getElementById('v26-v30-em-resolution-information')?.remove();
    document.getElementById('v31-v35-em-design-spatial-specificity')?.remove();
    document.getElementById('v36-v40-em-finite-sample-inference')?.remove();
    document.getElementById('v41-v45-em-selection-safe-inference')?.remove();
    document.getElementById('v46-v50-em-replication-inference')?.remove();
    document.getElementById('v51-v55-transportability')?.remove();
    const emSection = document.getElementById('v16-v20-em-field-program');
    if (emSection) {
      const inverse = document.createElement('section');
      inverse.id = 'v21-v25-em-source-identifiability';
      inverse.className = 'r3-stage-extension';
      inverse.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V21-V25 · Electromagnetic source identifiability</p>
          <h2>Separate sensor measurements from reconstructed sources before making any experiential inference</h2>
          <p>This layer treats EEG/MEG source analysis as a forward and inverse measurement problem. It tests reference invariance, lead-field null spaces, regularization dependence, multimodal complementarity, and forward-model perturbation before any source-space result can be interpreted as consciousness-related evidence.</p>
        </div>
        <div class="boundary">
          <p><strong>Scientific claim boundary:</strong> a source reconstruction is an inference under a declared forward model and inverse prior. V21-V25 do not show that EEG or MEG directly measures consciousness, that one reconstructed source is uniquely true, or that electromagnetic fields are identical to experience.</p>
        </div>
        <div class="measurement-figure-grid">
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}v21_v25_electromagnetic_inverse_validation.svg"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}v21_v25_electromagnetic_inverse_validation.svg" alt="Research III electromagnetic source identifiability validation V21 to V25" /></a>
            <p class="eyebrow">V21-V25 · forward and inverse measurement limits</p>
            <h3>Null spaces, inverse priors, complementary modalities, and model error</h3>
            <p>V22 constructs two source vectors separated by norm 1 with exactly zero sensor residual. V23 shows that regularization changes the selected source. V24 reduces nullity from 3 for each single synthetic modality to 1 when complementary operators are stacked, without reaching uniqueness.</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/electromagnetic-source-identifiability.md">Electromagnetic Source Identifiability Program</a><a href="${RESULT_PIN_PREFIX}electromagnetic_inverse_validation_summary.json">Result record</a><a href="${BLOB_PIN_PREFIX}v21_v25_electromagnetic_inverse_validation.svg">Figure source</a></div>
          </article>
        </div>
        <div class="r3-design-law-grid">
          <article><strong>V21: reference relation survives</strong><p>Pairwise sensor differences remain invariant to numerical precision across a 100-fold common-reference amplitude sweep.</p></article>
          <article><strong>V22: exact source ambiguity</strong><p>The canonical lead field has rank 3 and nullity 3; two distinct sources have source separation 1 and exactly zero sensor residual.</p></article>
          <article><strong>V23: inverse prior matters</strong><p>Across the declared regularization path, estimate norm falls from about 1.547 to 0.577 while sensor residual rises from about 1.43e-5 to 0.521.</p></article>
          <article><strong>V24-V25: complementarity and model sensitivity</strong><p>Stacking complementary operators reduces nullity from 3 to 1, and every forward-model perturbation obeys the declared operator-norm error bound.</p></article>
        </div>
        <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_inverse.py">Forward/inverse code</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_inverse_simulations.py">Validation simulations</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/scripts/run_electromagnetic_inverse_validation.py">Reproduce V21-V25</a></div>`;
      emSection.insertAdjacentElement('afterend', inverse);

      const resolution = document.createElement('section');
      resolution.id = 'v26-v30-em-resolution-information';
      resolution.className = 'r3-stage-extension';
      resolution.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V26-V30 · Electromagnetic resolution and information limits</p>
          <h2>Quantify what the acquisition and inverse system can resolve before interpreting source-space structure</h2>
          <p>This layer makes correlated sensor noise, finite inverse resolution, information bounds, sampling ambiguity, and ill-conditioned noise amplification explicit. It asks what can be recovered from the declared measurement system before any consciousness-specific interpretation is attempted.</p>
        </div>
        <div class="boundary">
          <p><strong>Scientific claim boundary:</strong> V26-V30 are analytic and deterministic synthetic measurement results. They do not show that EEG, MEG, OPM-MEG, a reconstructed source, a resolution matrix, Fisher information, or any electromagnetic descriptor directly measures consciousness or qualia.</p>
        </div>
        <div class="measurement-figure-grid">
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}v26_v30_electromagnetic_resolution_validation.svg"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}v26_v30_electromagnetic_resolution_validation.svg" alt="Research III electromagnetic resolution and information validation V26 to V30" /></a>
            <p class="eyebrow">V26-V30 · resolution and information</p>
            <h3>Noise geometry, rank limits, information loss, aliasing, and inverse amplification</h3>
            <p>V27 proves a rank-only normalized identity-error floor of 1/sqrt(2) for the canonical three-sensor, six-source system. V28 shows Fisher information falling as shared sensor noise rises. V29 gives an exact 17 Hz versus 83 Hz alias at 100 Hz sampling. V30 reaches the pseudoinverse noise-amplification bound in the weakest singular direction.</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/electromagnetic-resolution-program.md">Electromagnetic Resolution and Information Program</a><a href="${RESULT_PIN_PREFIX}electromagnetic_resolution_validation_summary.json">Result record</a><a href="${BLOB_PIN_PREFIX}v26_v30_electromagnetic_resolution_validation.svg">Figure source</a></div>
          </article>
        </div>
        <div class="r3-design-law-grid">
          <article><strong>V26: noise geometry is part of the model</strong><p>Covariance whitening preserves Mahalanobis residual energy to floating-point precision.</p></article>
          <article><strong>V27: rank imposes a resolution floor</strong><p>For source dimension 6 and operator rank at most 3, normalized identity error cannot fall below 1/sqrt(2), about 0.707106781.</p></article>
          <article><strong>V28-V29: information can be lost before inversion</strong><p>Common sensor noise lowers Fisher information, while insufficient sampling can make distinct continuous frequencies observationally identical.</p></article>
          <article><strong>V30: weak singular directions amplify noise</strong><p>At smallest singular value 0.01, the canonical construction attains 100-fold source-space amplification.</p></article>
        </div>
        <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_resolution.py">Resolution code</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_resolution_simulations.py">Validation simulations</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/scripts/run_electromagnetic_resolution_validation.py">Reproduce V26-V30</a></div>`;
      inverse.insertAdjacentElement('afterend', resolution);

      const design = document.createElement('section');
      design.id = 'v31-v35-em-design-spatial-specificity';
      design.className = 'r3-stage-extension';
      design.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V31-V35 · Electromagnetic design and spatial specificity</p>
          <h2>Turn source-resolution limits into explicit design and distinguishability laws</h2>
          <p>This layer quantifies point-spread and cross-talk, covariance-aware source distinguishability, Fisher-information sensor design, nuisance-subspace information loss, and robust information under bounded forward-model uncertainty.</p>
        </div>
        <div class="boundary">
          <p><strong>Scientific claim boundary:</strong> V31-V35 are analytic and deterministic synthetic measurement-design results. They do not show that PSFs, CTFs, Mahalanobis source distances, Fisher information, nuisance geometry, or robust information bounds directly measure consciousness or qualia.</p>
        </div>
        <div class="measurement-figure-grid">
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}v31_v35_electromagnetic_design_validation.svg"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}v31_v35_electromagnetic_design_validation.svg" alt="Research III electromagnetic design and spatial specificity validation V31 to V35" /></a>
            <p class="eyebrow">V31-V35 · design and spatial specificity</p>
            <h3>Spatial specificity, information geometry, nuisance loss, and robust design</h3>
            <p>V31 separates point-spread from cross-talk. V33 shows three redundant sensors can have weakest-direction information 1250 times smaller than a complementary three-sensor design. V34 proves the exact retained-information law sin squared theta. V35 proves the exact worst-case information bound under bounded whitened model uncertainty.</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/electromagnetic-design-spatial-specificity.md">Electromagnetic Design and Spatial Specificity Program</a><a href="${RESULT_PIN_PREFIX}electromagnetic_design_validation_summary.json">Result record</a><a href="${BLOB_PIN_PREFIX}v31_v35_electromagnetic_design_validation.svg">Figure source</a></div>
          </article>
        </div>
        <div class="r3-design-law-grid">
          <article><strong>V31: PSF is not CTF</strong><p>Resolution-matrix columns describe point-source spread, while rows describe sources that contaminate a reconstructed coefficient.</p></article>
          <article><strong>V32-V33: distinguishability is geometry-dependent</strong><p>Noise covariance and directional complementarity determine how much source and parameter information the sensors actually carry.</p></article>
          <article><strong>V34: nuisance removal has a price</strong><p>For one target and one nuisance direction, exact retained information is sin squared of their angle.</p></article>
          <article><strong>V35: nominal information is not robust information</strong><p>Bounded topography uncertainty reduces the guaranteed information to the square of max(norm minus radius, zero).</p></article>
        </div>
        <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_design.py">Design code</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_design_simulations.py">Validation simulations</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/scripts/run_electromagnetic_design_validation.py">Reproduce V31-V35</a></div>`;
      resolution.insertAdjacentElement('afterend', design);

      const inference = document.createElement('section');
      inference.id = 'v36-v40-em-finite-sample-inference';
      inference.className = 'r3-stage-extension';
      inference.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V36-V40 · Finite-sample electromagnetic inference</p>
          <h2>Separate a source estimate from the statistical calibration needed to trust it</h2>
          <p>This layer adds efficient scalar-amplitude inference, finite inverse-covariance bias, exact Gaussian source-discrimination error, search-wide false-positive control, and covariance-mismatch uncertainty calibration.</p>
        </div>
        <div class="boundary">
          <p><strong>Scientific claim boundary:</strong> V36-V40 are analytic or fixed-seed synthetic inference results. They do not show that a statistically significant source estimate, a low classification error, a corrected p-value, or a calibrated electromagnetic statistic directly measures consciousness or qualia.</p>
        </div>
        <div class="measurement-figure-grid">
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}v36_v40_electromagnetic_finite_sample_validation.svg"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}v36_v40_electromagnetic_finite_sample_validation.svg" alt="Research III finite-sample electromagnetic inference validation V36 to V40" /></a>
            <p class="eyebrow">V36-V40 · finite-sample inference</p>
            <h3>Estimator efficiency, covariance uncertainty, discrimination, multiplicity, and calibration</h3>
            <p>V36 proves GLS unbiasedness and CRLB attainment under known covariance and checks 40,000 fixed-seed Gaussian trials. V37 exposes finite inverse-covariance bias. V38 gives exact equal-prior Gaussian Bayes error from Mahalanobis separation. V39 gives an exact independent-search FWER baseline. V40 shows how covariance mismatch can understate uncertainty by about 33 percent in the canonical construction.</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/electromagnetic-finite-sample-inference.md">Finite-Sample Electromagnetic Inference Program</a><a href="${RESULT_PIN_PREFIX}electromagnetic_finite_sample_validation_summary.json">Result record</a><a href="${BLOB_PIN_PREFIX}v36_v40_electromagnetic_finite_sample_validation.svg">Figure source</a></div>
          </article>
        </div>
        <div class="r3-design-law-grid">
          <article><strong>V36: point estimate is not enough</strong><p>Under the declared Gaussian model, GLS has an exact variance equal to the CRLB, and finite-sample coverage can be checked against that law.</p></article>
          <article><strong>V37: estimated precision can be biased</strong><p>Even an unbiased sample covariance does not imply an unbiased inverse covariance when the noise sample is finite.</p></article>
          <article><strong>V38-V39: distinguishability and significance are different burdens</strong><p>Mahalanobis separation determines ideal Gaussian discrimination error, while search multiplicity determines the threshold needed to control false positives.</p></article>
          <article><strong>V40: nominal precision can be overconfident</strong><p>The sandwich variance exposes uncertainty inflation when the weighting covariance is not the true covariance.</p></article>
        </div>
        <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_finite_sample.py">Inference code</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_finite_sample_simulations.py">Validation simulations</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/scripts/run_electromagnetic_finite_sample_validation.py">Reproduce V36-V40</a></div>`;
      design.insertAdjacentElement('afterend', inference);

      const selection = document.createElement('section');
      selection.id = 'v41-v45-em-selection-safe-inference';
      selection.className = 'r3-stage-extension';
      selection.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V41-V45 · Multiplicity and selection-safe electromagnetic inference</p>
          <h2>Search-wide significance and same-data selection require explicit error control before any source claim is released</h2>
          <p>This layer makes multiplicity, exact randomization, post-selection coverage, and independent confirmation explicit when many sources, times, frequencies, or preprocessing choices are searched.</p>
        </div>
        <div class="boundary">
          <p><strong>Scientific claim boundary:</strong> V41-V45 are analytic or fixed-seed synthetic inference results. They establish statistical error-control and selection-safety properties only. They do not show that a significant electromagnetic source is a consciousness source or that statistical validity solves experiential target identification.</p>
        </div>
        <div class="measurement-figure-grid">
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}v41_v45_electromagnetic_selection_validation.svg"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}v41_v45_electromagnetic_selection_validation.svg" alt="Research III multiplicity and selection-safe electromagnetic inference validation V41 to V45" /></a>
            <p class="eyebrow">V41-V45 · search-wide inference</p>
            <h3>Multiplicity control, exact randomization, post-selection failure, and independent confirmation</h3>
            <p>V41 gives Bonferroni FWER control under arbitrary dependence. V42 shows Holm can gain rejections while retaining strong FWER control. V43 computes an exact sign-flip maximum-statistic p-value. V44 proves selected same-data coverage collapses as c^K. V45 shows independent confirmation restores selected-coordinate Type I error under the declared null.</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/electromagnetic-selection-safe-inference.md">Multiplicity and Selection-Safe Electromagnetic Inference Program</a><a href="${RESULT_PIN_PREFIX}electromagnetic_selection_validation_summary.json">Result record</a><a href="${BLOB_PIN_PREFIX}v41_v45_electromagnetic_selection_validation.svg">Figure source</a></div>
          </article>
        </div>
        <div class="r3-design-law-grid">
          <article><strong>V41: arbitrary dependence still permits Bonferroni control</strong><p>The union bound gives FWER at most alpha without requiring independent source statistics.</p></article>
          <article><strong>V42-V43: step-down and exact randomization sharpen inference</strong><p>Holm improves rejection efficiency, while a finite sign-flip orbit gives an exact randomization p-value under the declared symmetry.</p></article>
          <article><strong>V44: same-data selection can destroy nominal coverage</strong><p>For K searched null coordinates with marginal coverage c, selected-coordinate coverage falls exactly to c^K in the declared independent construction.</p></article>
          <article><strong>V45: confirmation must be independent</strong><p>The fixed-seed K = 100 experiment separates near-certain same-data false positives from approximately nominal independent-holdout Type I error.</p></article>
        </div>
        <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_selection.py">Selection-safe inference code</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_selection_simulations.py">Validation simulations</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/scripts/run_electromagnetic_selection_validation.py">Reproduce V41-V45</a></div>`;
      inference.insertAdjacentElement('afterend', selection);

      const replication = document.createElement('section');
      replication.id = 'v46-v50-em-replication-inference';
      replication.className = 'r3-stage-extension';
      replication.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V46-V50 · Cross-site replication inference and stability</p>
          <h2>Distinguish a pooled result from a result that is genuinely supported across sites</h2>
          <p>This layer audits common-effect pooling, heterogeneity, leave-one-site-out influence, partial-conjunction replicability, and concentration of inverse-variance weight across sites.</p>
        </div>
        <div class="boundary">
          <p><strong>Scientific claim boundary:</strong> V46-V50 use analytic and synthetic site records. They validate replication-inference machinery but do not constitute external replication in real cohorts or laboratories, and they do not show that an electromagnetic association is specific to consciousness or qualia.</p>
        </div>
        <div class="measurement-figure-grid">
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}v46_v50_electromagnetic_replication_validation.svg"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}v46_v50_electromagnetic_replication_validation.svg" alt="Research III cross-site replication inference and stability validation V46 to V50" /></a>
            <p class="eyebrow">V46-V50 · replication inference</p>
            <h3>Pooling, heterogeneity, influence, replicability, and effective site count</h3>
            <p>V46 gives the exact inverse-variance pooled estimate. V47 checks the known-variance Cochran Q moment law in 50,000 fixed-seed simulations. V48 verifies the exact delete-one shift identity. V49 asks how many sites support a non-null effect. V50 exposes when one high-weight site makes the nominal site count misleading.</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/electromagnetic-replication-inference.md">Cross-Site Replication Inference and Stability Program</a><a href="${RESULT_PIN_PREFIX}electromagnetic_replication_validation_summary.json">Result record</a><a href="${BLOB_PIN_PREFIX}v46_v50_electromagnetic_replication_validation.svg">Figure source</a></div>
          </article>
        </div>
        <div class="r3-design-law-grid">
          <article><strong>V46: pooling is a model, not a vote count</strong><p>The inverse-variance common-effect estimate is 0.42686 with known-variance standard error 0.06392 in the declared four-site construction.</p></article>
          <article><strong>V47-V48: heterogeneity and influence remain visible</strong><p>The Q statistic is calibrated against its declared reference law, and every site is deleted once to expose how much it moves the pooled estimate.</p></article>
          <article><strong>V49: evidence somewhere is not replication</strong><p>Partial-conjunction inference distinguishes one non-null site from evidence that at least two, three, or more sites carry an effect.</p></article>
          <article><strong>V50: nominal sites can overstate evidential diversity</strong><p>In the dominant-site construction, four nominal sites reduce to an effective site count of about 1.394 and deleting the dominant site inflates variance by about 6.33.</p></article>
        </div>
        <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_replication.py">Replication inference code</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/electromagnetic_replication_simulations.py">Validation simulations</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/scripts/run_electromagnetic_replication_validation.py">Reproduce V46-V50</a></div>`;
      selection.insertAdjacentElement('afterend', replication);

      const transport = document.createElement('section');
      transport.id = 'v51-v55-transportability';
      transport.className = 'r3-stage-extension';
      transport.innerHTML = `
        <div class="section-head">
          <p class="eyebrow">V51-V55 · Transportability across sensor systems, hardware, and states</p>
          <h2>Ask whether the measurement survives a change of representation, acquisition system, or population before calling it general</h2>
          <p>This layer moves beyond replication at fixed assumptions. It separates harmless invertible coordinate changes from lossy projections, quantifies forward-topography mismatch, makes support overlap visible under covariate shift, and bounds how far bounded outputs can move under distribution shift.</p>
        </div>
        <div class="boundary">
          <p><strong>Scientific claim boundary:</strong> V51-V55 are analytic and deterministic transportability results. They do not constitute empirical cross-device, cross-state, or cross-population validation, and they do not establish that an electromagnetic marker measures consciousness or qualia.</p>
        </div>
        <div class="measurement-figure-grid">
          <article class="figure-card">
            <a href="${BLOB_PIN_PREFIX}v51_v55_transportability_validation.svg"><img loading="lazy" decoding="async" src="${RAW_PIN_PREFIX}v51_v55_transportability_validation.svg" alt="Research III transportability validation V51 to V55" /></a>
            <p class="eyebrow">V51-V55 · transportability</p>
            <h3>Coordinate invariance, information loss, model mismatch, overlap, and bounded shift</h3>
            <p>V51 verifies exact invariance under a consistently modeled invertible sensor transform. V52 shows that rank-reducing projection cannot increase Fisher information. V53 quantifies topography-mismatch bias. V54 recovers the target expectation exactly under declared covariate-shift assumptions while exposing effective-sample loss. V55 gives a sharp total-variation expectation-shift budget for bounded outputs.</p>
            <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/docs/transportability-program.md">Transportability Across Sensor Systems, Hardware, and States Program</a><a href="${RESULT_PIN_PREFIX}transportability_validation_summary.json">Result record</a><a href="${BLOB_PIN_PREFIX}v51_v55_transportability_validation.svg">Figure source</a></div>
          </article>
        </div>
        <div class="r3-design-law-grid">
          <article><strong>V51: coordinate changes are not information changes</strong><p>When observation, topography, and covariance are transformed together by an invertible map, the GLS amplitude estimate and scalar Fisher information are preserved to floating-point precision.</p></article>
          <article><strong>V52: lossy projection cannot create target information</strong><p>The canonical two-sensor projection retains about 82.44% of full information; a single mixed channel retains about 67.73%.</p></article>
          <article><strong>V53: hardware mismatch becomes estimator bias</strong><p>Forward-topography mismatch changes the expected amplitude gain, with the relative bias bounded by the declared covariance-weighted Cauchy-Schwarz limit.</p></article>
          <article><strong>V54-V55: transport requires overlap and a shift budget</strong><p>Importance weighting exactly recovers the target expectation under the declared support and conditional-stability assumptions, while effective sample fraction falls to about 0.472 in the strongest canonical shift. For bounded outputs, total variation gives a sharp worst-case expectation-shift budget.</p></article>
        </div>
        <div class="figure-source-links"><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/transportability.py">Transportability code</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/src/consciousness_measurement/transportability_simulations.py">Validation constructions</a><a href="${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/scripts/run_transportability_validation.py">Reproduce V51-V55</a></div>`;
      replication.insertAdjacentElement('afterend', transport);
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
    if (metric) metric.innerHTML = '<strong>192</strong><span>tests in each CI job</span>';
    if (meta) meta.textContent = 'V1-V55 formal validation · 31 scientific visuals · 11 reproducible validation runners';
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

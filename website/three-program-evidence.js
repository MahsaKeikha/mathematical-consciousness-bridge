(() => {
  const OBSERVER_REPO = 'https://github.com/MahsaKeikha/spatiotemporal-observer-math';
  const OBSERVER_RAW = 'https://raw.githubusercontent.com/MahsaKeikha/spatiotemporal-observer-math/main';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const MEASUREMENT_RAW = 'https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/main';

  const researchIFigures = [
    ['I', 'Baseline moving world-tube', 'worldtube_baseline.png', 'reproducible_results.md'],
    ['I', 'Recovery phase diagram', 'worldtube_phase_diagram.png', 'reproducible_results.md'],
    ['II', 'Finite-sample benchmark', 'finite_sample_benchmark.png', 'reproducible_results.md'],
    ['II', 'Symbolic recovery region', 'symbolic_recovery_region.png', 'reproducible_results.md'],
    ['II', 'Perturbed recovery region', 'perturbed_recovery_region.png', 'reproducible_results.md'],
    ['III', 'Gaussian screen calibration', 'gaussian_screen_calibration.png', 'reproducible_results.md'],
    ['III', 'Structural-null screen', 'structural_null_screen.png', 'reproducible_results.md'],
    ['III', 'Trajectory-coupled screening', 'trajectory_coupled_screen_calibration.png', 'reproducible_results.md'],
    ['III', 'Relative covariance calibration', 'relative_covariance_calibration.png', 'reproducible_results.md'],
    ['IV', 'Cross-fitted relative calibration', 'cross_fitted_relative_calibration.png', 'reproducible_results.md'],
    ['IV', 'Drift-robust relative calibration', 'drift_robust_relative_calibration.png', 'reproducible_results.md'],
    ['IV', 'Calibrated drift comparison', 'calibrated_drift_comparison.png', 'reproducible_results.md'],
    ['IV', 'Multi-regime coupled calibration', 'multi_regime_coupled_calibration.png', 'reproducible_results.md'],
    ['V', 'Dependent Gaussian calibration', 'dependent_gaussian_calibration.png', 'reproducible_results.md'],
    ['V', 'Unknown-mean dependent calibration', 'dependent_centered_gaussian_calibration.png', 'reproducible_results.md'],
    ['V', 'Estimated AR(1) calibration', 'estimated_ar1_calibration.png', 'reproducible_results.md'],
    ['VI', 'P44 nuisance projection', 'nuisance_projection_calibration.svg', 'proposition_44_nuisance_projection.md'],
    ['VI', 'P45 estimated AR(1) nuisance projection', 'estimated_ar1_nuisance_projection.svg', 'proposition_45_estimated_ar1_nuisance_projection.md'],
    ['VI', 'P46 design-specific AR(1) envelope', 'design_specific_ar1_envelope.svg', 'proposition_46_design_specific_ar1_envelope.md'],
    ['VII', 'P47 weighted Wishart matrix Chernoff', 'weighted_wishart_matrix_chernoff.svg', 'proposition_47_weighted_wishart_matrix_chernoff.md'],
    ['VII', 'P48 uniform matrix Chernoff AR(1)', 'uniform_matrix_chernoff_ar1.svg', 'proposition_48_uniform_matrix_chernoff_ar1.md'],
    ['VII', 'P49 compact temporal family', 'compact_temporal_family.svg', 'proposition_49_compact_temporal_family.md'],
    ['VIII', 'P50 calibrated temporal family', 'calibrated_temporal_family.svg', 'proposition_50_calibrated_temporal_family.md'],
    ['VIII', 'P51 e-value temporal confidence set', 'evalue_temporal_confidence_set.svg', 'proposition_51_evalue_temporal_confidence_set.md'],
    ['VIII', 'P52 certified e-value outer cover', 'certified_evalue_outer_cover.svg', 'proposition_52_certified_evalue_outer_cover.md'],
    ['IX', 'Physical relaxation sampling', 'physical_relaxation_sampling.svg', 'proposition_53_physical_relaxation_time.md'],
    ['IX', 'Irregular-grid Markov factorization', 'physical_relaxation_markov.svg', 'proposition_53_physical_relaxation_time.md'],
    ['IX', 'P53B irregular-time relaxation calibration', 'irregular_relaxation_evalue_calibration.svg', 'proposition_53b_irregular_tau_evalue.md'],
    ['IX', 'P54 two-scale relaxation cover', 'two_scale_irregular_tau_cover.svg', 'proposition_54_two_scale_irregular_tau_cover.md'],
    ['IX', 'P55 quadratic relaxation calibration', 'quadratic_relaxation_calibration.svg', 'proposition_55_quadratic_relaxation_calibration.md'],
    ['X', 'P56 innovation-whitened target covariance', 'innovation_whitened_target.svg', 'proposition_56_innovation_whitened_target.md'],
    ['XI', 'P57 robust innovation-whitened target covariance', 'robust_innovation_whitened_target.svg', 'proposition_57_robust_innovation_whitening.md'],
    ['XII', 'P58 observer-scale covariance-to-world-tube audit', 'observer_bridge_dimension_audit.svg', 'proposition_58_observer_bridge.md'],
  ];

  const researchICoreSources = [
    ['Documentation map', 'README.md'],
    ['Visual research guide', 'docs/visual_research_guide.md'],
    ['Research index', 'docs/research_index.md'],
    ['Research overview', 'docs/research_overview.md'],
    ['Research program', 'docs/research_program.md'],
    ['Physics guide', 'docs/physics_guide.md'],
    ['Physics, mathematics, and citation map', 'docs/physics_mathematics_citation_map.md'],
    ['Reproducible results', 'docs/reproducible_results.md'],
    ['Experimental protocol', 'docs/experimental_protocol.md'],
    ['Proofs and conjectures', 'docs/proofs_and_conjectures.md'],
    ['Assumption ledger', 'docs/assumption_ledger.md'],
    ['Bibliography', 'docs/bibliography.md'],
    ['Interpretation protocol', 'docs/interpretation_protocol.md'],
    ['Figure reading guide', 'docs/figure_reading_guide.md'],
  ];

  const researchIFrontierSources = [
    ['P44 nuisance projection', 'docs/proposition_44_nuisance_projection.md'],
    ['P45 estimated AR(1) nuisance projection', 'docs/proposition_45_estimated_ar1_nuisance_projection.md'],
    ['P46 design-specific AR(1) envelope', 'docs/proposition_46_design_specific_ar1_envelope.md'],
    ['P47 weighted Wishart matrix Chernoff', 'docs/proposition_47_weighted_wishart_matrix_chernoff.md'],
    ['P48 uniform matrix Chernoff AR(1)', 'docs/proposition_48_uniform_matrix_chernoff_ar1.md'],
    ['P49 compact temporal family', 'docs/proposition_49_compact_temporal_family.md'],
    ['P50 calibrated temporal family', 'docs/proposition_50_calibrated_temporal_family.md'],
    ['P51 e-value temporal confidence set', 'docs/proposition_51_evalue_temporal_confidence_set.md'],
    ['P52 certified e-value outer cover', 'docs/proposition_52_certified_evalue_outer_cover.md'],
    ['P53A physical relaxation time', 'docs/proposition_53_physical_relaxation_time.md'],
    ['P53B irregular relaxation e-value', 'docs/proposition_53b_irregular_tau_evalue.md'],
    ['P54 two-scale irregular relaxation cover', 'docs/proposition_54_two_scale_irregular_tau_cover.md'],
    ['P55 quadratic relaxation calibration', 'docs/proposition_55_quadratic_relaxation_calibration.md'],
    ['P56 innovation-whitened target', 'docs/proposition_56_innovation_whitened_target.md'],
    ['P57 robust innovation whitening', 'docs/proposition_57_robust_innovation_whitening.md'],
    ['P58 observer bridge audit', 'docs/proposition_58_observer_bridge.md'],
  ];

  const researchIDataSources = [
    'finite_sample_results.json',
    'gaussian_screen_calibration.json',
    'trajectory_coupled_screen_calibration.json',
    'relative_covariance_calibration.json',
    'cross_fitted_relative_calibration.json',
    'drift_robust_relative_calibration.json',
    'calibrated_drift_comparison.json',
    'multi_regime_coupled_calibration.json',
    'dependent_gaussian_calibration.json',
    'dependent_centered_gaussian_calibration.json',
    'estimated_ar1_calibration.json',
    'nuisance_projection_calibration.json',
    'estimated_ar1_nuisance_projection.json',
    'design_specific_ar1_envelope.json',
    'weighted_wishart_matrix_chernoff.json',
    'uniform_matrix_chernoff_ar1.json',
    'compact_temporal_family.json',
    'calibrated_temporal_family.json',
    'evalue_temporal_confidence_set.json',
    'certified_evalue_outer_cover.json',
    'physical_relaxation_sampling.json',
    'irregular_relaxation_evalue_calibration.json',
    'two_scale_irregular_tau_cover.json',
    'quadratic_relaxation_calibration.json',
    'innovation_whitened_target.json',
    'robust_innovation_whitened_target.json',
    'observer_bridge_dimension_audit.json',
  ];

  const researchIIIDocSources = [
    ['Documentation map', 'docs/README.md'],
    ['Start Here', 'docs/start-here.md'],
    ['Glossary', 'docs/glossary.md'],
    ['Epistemic boundaries', 'docs/epistemic-boundaries.md'],
    ['Formal measurement framework', 'docs/measurement-framework.md'],
    ['Consciousness Evidence Profile specification', 'docs/measurement-instrument-spec.md'],
    ['Assumption registry', 'docs/assumption-registry.md'],
    ['Failure modes', 'docs/failure-modes.md'],
    ['Claim registry', 'docs/claim-registry.md'],
    ['Phase 1 protocol', 'docs/protocol-phase1.md'],
    ['Preregistration template', 'docs/preregistration-template.md'],
    ['Experimental program', 'docs/experimental-program.md'],
    ['Statistical validation', 'docs/statistical-validation.md'],
    ['Dependence-robust partial identification', 'docs/partial-identification.md'],
    ['Phenomenal structure', 'docs/phenomenal-structure.md'],
    ['Theory landscape', 'docs/theory-landscape.md'],
    ['Falsification matrix', 'docs/falsification-matrix.md'],
    ['Literature map', 'docs/literature.md'],
    ['Clinical translation', 'docs/clinical-translation.md'],
    ['Ethics', 'docs/ethics.md'],
    ['Edge cases', 'docs/edge-cases.md'],
    ['Software guide', 'docs/software-guide.md'],
    ['Reproducibility', 'docs/reproducibility.md'],
    ['Repository policy', 'docs/repository-policy.md'],
  ];

  const researchIIIMachineSources = [
    ['CEP schema', 'schemas/cep.schema.json'],
    ['CEP worked example', 'examples/cep_example.json'],
    ['Claim schema', 'schemas/claim.schema.json'],
    ['Claim worked example', 'examples/claim_example.json'],
    ['Repository policy verifier', 'scripts/verify_repository_policy.py'],
  ];

  const researchIIIFigures = [
    ['Measurement architecture', 'docs/figures/measurement_architecture.svg', 'docs/measurement-framework.md'],
    ['Structural measurement pipeline', 'docs/figures/structural_measurement_pipeline.svg', 'docs/phenomenal-structure.md'],
    ['M0-M7 claim ladder', 'docs/figures/claim_ladder.svg', 'docs/claim-registry.md'],
  ];

  function currentFile() {
    return window.location.pathname.split('/').pop() || 'index.html';
  }

  function ensureStyles() {
    if (document.getElementById('three-program-evidence-styles')) return;
    const style = document.createElement('style');
    style.id = 'three-program-evidence-styles';
    style.textContent = `
      .complete-record-block{margin:2rem 0;padding:1.4rem;border:1px solid rgba(120,140,170,.28);border-radius:20px;background:rgba(255,255,255,.025)}
      .complete-record-head{display:flex;gap:1rem;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;margin-bottom:1rem}
      .complete-record-head h3{margin:.15rem 0 .35rem;font-size:clamp(1.25rem,2vw,1.7rem)}
      .complete-record-head p{margin:0;max-width:78ch}
      .record-badge{display:inline-flex;align-items:center;gap:.35rem;padding:.35rem .65rem;border-radius:999px;border:1px solid rgba(120,140,170,.36);font-size:.78rem;font-weight:700;letter-spacing:.02em;white-space:nowrap}
      .complete-figure-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1rem}
      .complete-figure-card{border:1px solid rgba(120,140,170,.24);border-radius:16px;overflow:hidden;background:rgba(255,255,255,.02);display:flex;flex-direction:column;min-width:0}
      .complete-figure-card>a:first-child{display:block;background:#fff;min-height:190px}
      .complete-figure-card img{display:block;width:100%;height:220px;object-fit:contain;background:#fff}
      .complete-figure-card-body{padding:.9rem 1rem 1rem;display:flex;flex-direction:column;gap:.45rem;flex:1}
      .complete-figure-card-body h4{margin:0;font-size:1rem;line-height:1.35}
      .figure-phase{font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;opacity:.72}
      .figure-source-links{display:flex;gap:.7rem;flex-wrap:wrap;margin-top:auto;padding-top:.35rem}
      .figure-source-links a,.manifest-link{font-size:.82rem;font-weight:700;text-decoration:none}
      .manifest-group{margin-top:1.1rem}
      .manifest-group h4{margin:0 0 .65rem;font-size:1rem}
      .source-manifest-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:.55rem}
      .manifest-link{display:block;padding:.7rem .8rem;border:1px solid rgba(120,140,170,.22);border-radius:11px;background:rgba(255,255,255,.02);overflow-wrap:anywhere}
      .manifest-link small{display:block;margin-top:.2rem;font-weight:500;opacity:.68}
      .figure-file-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:.45rem}
      .figure-file-grid .manifest-link{padding:.55rem .7rem;font-size:.78rem}
      .research-iii-complete-note{margin-top:1rem;padding:1rem 1.1rem;border-left:4px solid currentColor;background:rgba(255,255,255,.025);border-radius:0 12px 12px 0}
      @media (max-width:640px){.complete-record-block{padding:1rem}.complete-figure-card img{height:190px}}
    `;
    document.head.appendChild(style);
  }

  function figureCard([phase, title, file, doc]) {
    const image = `${OBSERVER_RAW}/docs/${file}`;
    const figurePage = `${OBSERVER_REPO}/blob/main/docs/${file}`;
    const docPage = `${OBSERVER_REPO}/blob/main/docs/${doc}`;
    return `
      <article class="complete-figure-card" data-research-i-figure="${file}">
        <a href="${figurePage}" aria-label="Open full-resolution ${title}"><img loading="lazy" decoding="async" src="${image}" alt="Research I ${title}" /></a>
        <div class="complete-figure-card-body">
          <span class="figure-phase">Research I · Phase ${phase}</span>
          <h4>${title}</h4>
          <div class="figure-source-links"><a href="${docPage}">Scientific context</a><a href="${figurePage}">Figure source</a></div>
        </div>
      </article>`;
  }

  function researchIIIFigureCard([title, path, context]) {
    const image = `${MEASUREMENT_RAW}/${path}`;
    const figurePage = `${MEASUREMENT_REPO}/blob/main/${path}`;
    const contextPage = `${MEASUREMENT_REPO}/blob/main/${context}`;
    return `
      <article class="complete-figure-card" data-research-iii-figure="${path}">
        <a href="${figurePage}" aria-label="Open full-resolution ${title}"><img loading="lazy" decoding="async" src="${image}" alt="Research III ${title}" /></a>
        <div class="complete-figure-card-body">
          <span class="figure-phase">Research III · canonical figure</span>
          <h4>${title}</h4>
          <div class="figure-source-links"><a href="${contextPage}">Scientific context</a><a href="${figurePage}">Figure source</a></div>
        </div>
      </article>`;
  }

  function renderResearchIAtlas() {
    const section = document.getElementById('research-i-visual-program');
    if (!section || document.getElementById('research-i-complete-figure-gallery')) return;
    const block = document.createElement('div');
    block.className = 'complete-record-block';
    block.id = 'research-i-complete-figure-gallery';
    block.innerHTML = `
      <div class="complete-record-head">
        <div><span class="record-badge">Complete canonical set</span><h3>All 33 Research I scientific result figures</h3><p>This is the full scientific-result inventory recorded by the Research I visual guide, shown directly in the Atlas rather than hidden behind an external link. The explanatory physics pipeline remains above and is intentionally not counted among the 33 result figures.</p></div>
        <span class="record-badge">33 / 33 visible</span>
      </div>
      <div class="complete-figure-grid">${researchIFigures.map(figureCard).join('')}</div>`;
    const boundary = section.querySelector('.boundary');
    if (boundary) boundary.insertAdjacentElement('beforebegin', block);
    else section.appendChild(block);
  }

  function renderResearchIIIAtlasCompleteness() {
    const section = document.getElementById('research-iii-visual-program');
    if (!section || document.getElementById('research-iii-complete-figure-note')) return;
    const note = document.createElement('div');
    note.id = 'research-iii-complete-figure-note';
    note.className = 'research-iii-complete-note';
    note.innerHTML = `<strong>Complete Research III figure set: 3 / 3 visible above.</strong> The measurement architecture, structural measurement pipeline, and M0-M7 claim ladder are currently the complete canonical figure directory for Research III. <a href="${MEASUREMENT_REPO}/tree/main/docs/figures">Audit the figure directory</a>.`;
    const grid = section.querySelector('.program-visual-grid');
    if (grid) grid.insertAdjacentElement('afterend', note);
    else section.appendChild(note);
  }

  function linkGrid(items, repo, prefix = '') {
    return `<div class="source-manifest-grid">${items.map(([label, path]) => `<a class="manifest-link" href="${repo}/blob/main/${path}">${label}<small>${prefix}${path}</small></a>`).join('')}</div>`;
  }

  function renderResearchISources() {
    const section = document.getElementById('research-i-source-program');
    if (!section || document.getElementById('research-i-source-manifest')) return;
    const block = document.createElement('div');
    block.className = 'complete-record-block';
    block.id = 'research-i-source-manifest';
    const dataLinks = researchIDataSources.map(file => `<a class="manifest-link" href="${OBSERVER_REPO}/blob/main/docs/${file}">${file.replace(/\.json$/, '').replaceAll('_', ' ')}<small>docs/${file}</small></a>`).join('');
    block.innerHTML = `
      <div class="complete-record-head"><div><span class="record-badge">Research I source manifest</span><h3>The provenance record is visible here, not only one click away</h3><p>Core documentation, the P44-P58 formal frontier, all 33 scientific result figures, and machine-readable result records are shown directly on this page.</p></div><span class="record-badge">58 results · 33 result figures</span></div>
      <div class="manifest-group"><h4>Core scientific and reproducibility documents</h4>${linkGrid(researchICoreSources, OBSERVER_REPO)}</div>
      <div class="manifest-group"><h4>P44-P58 formal frontier sources</h4>${linkGrid(researchIFrontierSources, OBSERVER_REPO)}</div>
      <div class="manifest-group"><h4>All 33 scientific result figures with provenance</h4><div class="complete-figure-grid">${researchIFigures.map(figureCard).join('')}</div></div>
      <div class="manifest-group"><h4>Machine-readable result records</h4><div class="figure-file-grid">${dataLinks}</div></div>`;
    section.appendChild(block);
  }

  function renderResearchIIISources() {
    const section = document.getElementById('research-iii-source-program');
    if (!section || document.getElementById('research-iii-source-manifest')) return;
    const block = document.createElement('div');
    block.className = 'complete-record-block';
    block.id = 'research-iii-source-manifest';
    block.innerHTML = `
      <div class="complete-record-head"><div><span class="record-badge">Research III source manifest</span><h3>Measurement-science specification, figures, schemas, and audit files</h3><p>The complete reader-facing documentation map and all current canonical Research III figures are shown directly here. Their status remains specification and computational scaffold unless a document explicitly records empirical validation.</p></div><span class="record-badge">3 / 3 canonical figures</span></div>
      <div class="manifest-group"><h4>Reader-facing scientific specification</h4>${linkGrid(researchIIIDocSources, MEASUREMENT_REPO)}</div>
      <div class="manifest-group"><h4>Machine-readable schemas and verification</h4>${linkGrid(researchIIIMachineSources, MEASUREMENT_REPO)}</div>
      <div class="manifest-group"><h4>Complete canonical Research III figure set with provenance</h4><div class="complete-figure-grid">${researchIIIFigures.map(researchIIIFigureCard).join('')}</div></div>`;
    section.appendChild(block);
  }

  function render() {
    const page = currentFile();
    if (page !== 'visual-atlas.html' && page !== 'sources.html') return;
    ensureStyles();
    if (page === 'visual-atlas.html') {
      renderResearchIAtlas();
      renderResearchIIIAtlasCompleteness();
    } else {
      renderResearchISources();
      renderResearchIIISources();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', render, { once: true });
  } else {
    render();
  }
})();

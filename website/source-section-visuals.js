(() => {
  const OBSERVER_REPO = 'https://github.com/MahsaKeikha/spatiotemporal-observer-math';
  const OBSERVER_RAW = 'https://raw.githubusercontent.com/MahsaKeikha/spatiotemporal-observer-math/main';
  const BRIDGE_REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const MEASUREMENT_PIN = '383a6cdab720b3f87c17191b7c98bd6828213b72';
  const MEASUREMENT_RAW =
    `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${MEASUREMENT_PIN}`;

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

  const RESEARCH_III_CURATED = new Set([
    'research_program_map.svg',
    'target_evidence_matrix.svg',
    'cep_anatomy.svg',
    'identification_uncertainty_pipeline.svg',
    'validation_program_map.svg',
    'theory_falsification_map.svg',
  ]);

  const VISUALS = [
    {
      sectionId: 'research-i-source-program',
      id: 'research-i-source-visual-anchor',
      program: 'Research I',
      label: 'Representative physical-system visual',
      title: 'Moving world-tube recovery phase diagram',
      image: `${OBSERVER_RAW}/docs/worldtube_phase_diagram.png`,
      alt: 'Research I moving world-tube recovery phase diagram',
      caption:
        'A visual summary of the physical-system identification regime: where moving world-tube recovery succeeds, where it becomes uncertain, and where the declared assumptions stop supporting recovery.',
      contextHref: `${OBSERVER_REPO}/blob/main/docs/reproducible_results.md`,
      figureHref: `${OBSERVER_REPO}/blob/main/docs/worldtube_phase_diagram.png`,
    },
    {
      sectionId: 'research-ii-source-program',
      id: 'research-ii-source-visual-anchor',
      program: 'Research II',
      label: 'Representative theorem-program visual',
      title: 'Research architecture and falsification structure',
      image: 'figures/research_architecture.svg?v=20260916-color-safe',
      alt: 'Research II research architecture and falsification structure',
      caption:
        'The architecture view keeps the P1-P100 theorem record in context: declared physical descriptions, independent targets, bridge tests, falsification logic, finite-data certification, and the still-open physical-to-experiential bridge.',
      contextHref: `${BRIDGE_REPO}/blob/main/docs/theorem_roadmap.md`,
      figureHref: `${BRIDGE_REPO}/blob/main/docs/figures/research_architecture.svg`,
    },
    {
      sectionId: 'research-iii-source-program',
      id: 'research-iii-source-visual-anchor',
      program: 'Research III',
      label: 'Representative measurement-science visual',
      title: 'Consciousness measurement architecture',
      image: `${MEASUREMENT_RAW}/docs/figures/measurement_architecture.svg`,
      rawHref: `${MEASUREMENT_RAW}/docs/figures/measurement_architecture.svg`,
      alt: 'Research III consciousness measurement architecture',
      caption:
        'The measurement architecture shows how declared experiential targets, observables, assumptions, identification limits, uncertainty, and allowed scientific claims are kept separate instead of collapsing a proxy into experience itself.',
      contextHref: `${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/docs/measurement-framework.md`,
      figureHref: `${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/docs/figures/measurement_architecture.svg`,
    },
  ];

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

  function ensureStyles() {
    if (document.getElementById('source-section-visual-styles')) return;
    const style = document.createElement('style');
    style.id = 'source-section-visual-styles';
    style.textContent = `
      .source-section-visual{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(280px,.65fr);gap:1.1rem;align-items:stretch;margin:1.35rem 0 1.6rem;border:1px solid rgba(120,140,170,.28);border-radius:20px;overflow:hidden;background:linear-gradient(145deg,rgba(255,255,255,.035),rgba(255,255,255,.012));box-shadow:0 18px 42px rgba(0,0,0,.12)}
      .source-section-visual-stage{display:flex;align-items:center;justify-content:center;min-height:500px;padding:.45rem;background:#fff}
      .source-section-visual-stage a{display:flex;width:100%;height:100%;align-items:center;justify-content:center}
      .source-section-visual-stage img{display:block;width:100%;height:auto;max-height:640px;object-fit:contain;background:#fff}
      .source-section-visual-copy{display:flex;flex-direction:column;justify-content:center;padding:1.3rem 1.35rem 1.35rem .25rem}
      .source-section-visual-copy .eyebrow{margin:0 0 .45rem}
      .source-section-visual-copy h3{margin:0 0 .7rem;font-size:clamp(1.22rem,2vw,1.65rem);line-height:1.2}
      .source-section-visual-copy p{margin:0;line-height:1.65}
      .source-section-visual-links{display:flex;gap:.55rem;flex-wrap:wrap;margin-top:1rem}
      .source-section-visual-links a{display:inline-flex;align-items:center;min-height:38px;padding:.55rem .78rem;border:1px solid rgba(120,140,170,.3);border-radius:999px;text-decoration:none;font-size:.82rem;font-weight:800}
      .source-section-visual-links a:first-child{background:rgba(255,255,255,.055)}
      .source-visual-record{margin:1.5rem 0;padding:1.35rem;border:1px solid rgba(120,140,170,.28);border-radius:20px;background:rgba(255,255,255,.025)}
      .source-visual-record-head{display:flex;gap:1rem;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;margin-bottom:1rem}
      .source-visual-record-head h3{margin:.3rem 0 .45rem}
      .source-visual-record-head p{margin:0;max-width:920px;line-height:1.65}
      .source-visual-badge{display:inline-flex;align-items:center;padding:.35rem .65rem;border:1px solid rgba(120,140,170,.34);border-radius:999px;font-size:.78rem;font-weight:800;letter-spacing:.02em;white-space:nowrap}
      .source-visual-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(470px,1fr));gap:1.2rem}
      .source-visual-card{display:flex;flex-direction:column;min-width:0;border:1px solid rgba(120,140,170,.24);border-radius:16px;overflow:hidden;background:rgba(255,255,255,.02)}
      .source-visual-card>.source-visual-image-link{display:flex;align-items:center;justify-content:center;min-height:360px;padding:.35rem;background:#fff}
      .source-visual-card img{display:block;width:100%;height:360px;object-fit:contain;background:#fff}
      .source-visual-card-body{display:flex;flex-direction:column;flex:1;padding:1rem 1.05rem 1.1rem}
      .source-visual-card-body span{font-size:.76rem;font-weight:800;letter-spacing:.04em;text-transform:uppercase;opacity:.76}
      .source-visual-card-body h4{margin:.5rem 0 .55rem;font-size:1.08rem;line-height:1.28}
      .source-visual-card-body p{margin:0;line-height:1.55;font-size:.92rem}
      .source-visual-card-body .source-section-visual-links{margin-top:auto;padding-top:.85rem}
      .source-visual-reading-note{margin:.85rem 0 0;font-size:.83rem;line-height:1.5;opacity:.8}
      @media (max-width:1050px){.source-visual-grid{grid-template-columns:1fr}.source-visual-card img{height:auto;max-height:520px}.source-visual-card>.source-visual-image-link{min-height:320px}}
      @media (max-width:820px){.source-section-visual{grid-template-columns:1fr}.source-section-visual-stage{min-height:300px;padding:.25rem}.source-section-visual-copy{padding:0 1rem 1.15rem}.source-section-visual-stage img{max-height:480px}.source-visual-grid{grid-template-columns:1fr}.source-visual-card img{height:auto;max-height:460px}.source-visual-card>.source-visual-image-link{min-height:280px;padding:.25rem}}
    `;
    document.head.appendChild(style);
  }

  function visualMarkup(visual) {
    const imageHref = visual.rawHref || visual.figureHref;
    const fullResolutionLink = visual.rawHref
      ? `<a href="${visual.rawHref}" target="_blank" rel="noopener noreferrer">Open full-resolution SVG</a>`
      : '';
    return `
      <div class="source-section-visual-stage">
        <a href="${imageHref}" target="_blank" rel="noopener noreferrer" aria-label="Open full-resolution ${visual.title}">
          <img loading="lazy" decoding="async" src="${visual.image}" alt="${visual.alt}" />
        </a>
      </div>
      <figcaption class="source-section-visual-copy">
        <p class="eyebrow">${visual.program} · ${visual.label}</p>
        <h3>${visual.title}</h3>
        <p>${visual.caption}</p>
        <div class="source-section-visual-links">
          <a href="${visual.contextHref}">Scientific context</a>
          <a href="${visual.figureHref}">Figure source</a>
          ${fullResolutionLink}
        </div>
        ${visual.rawHref ? '<p class="source-visual-reading-note">The full-resolution SVG opens directly in the browser so you can zoom without GitHub shrinking the preview.</p>' : ''}
      </figcaption>`;
  }

  function insertVisual(visual) {
    const section = document.getElementById(visual.sectionId);
    if (!section || document.getElementById(visual.id)) return;

    const figure = document.createElement('figure');
    figure.id = visual.id;
    figure.className = 'source-section-visual';
    figure.dataset.program = visual.program;
    figure.innerHTML = visualMarkup(visual);

    const metrics = section.querySelector('.program-record-grid');
    const sources = section.querySelector('.program-source-grid');
    if (metrics) metrics.insertAdjacentElement('afterend', figure);
    else if (sources) sources.insertAdjacentElement('beforebegin', figure);
    else section.appendChild(figure);
  }

  function researchIIIRawHref(record) {
    return `${MEASUREMENT_RAW}/docs/figures/${record.file}`;
  }

  function researchIIISourceHref(record) {
    return `${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/docs/figures/${record.file}`;
  }

  function researchIIISourceLinks(record) {
    return `<div class="source-section-visual-links"><a href="${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/${record.context}">Scientific context</a><a href="${researchIIISourceHref(record)}">Figure source</a><a href="${researchIIIRawHref(record)}" target="_blank" rel="noopener noreferrer">Open full-resolution SVG</a></div>`;
  }

  function researchIIISourceCard(record) {
    const title = escapeHTML(record.title);
    return `
      <article class="source-visual-card" data-research-iii-source-figure="docs/figures/${escapeHTML(record.file)}">
        <a class="source-visual-image-link" href="${researchIIIRawHref(record)}" target="_blank" rel="noopener noreferrer" aria-label="Open full-resolution ${title}">
          <img loading="lazy" decoding="async" src="${researchIIIRawHref(record)}" alt="Research III ${title}" />
        </a>
        <div class="source-visual-card-body">
          <span>${escapeHTML(record.phase)}</span>
          <h4>${title}</h4>
          <p>${escapeHTML(record.summary)}</p>
          ${researchIIISourceLinks(record)}
          <p class="source-visual-reading-note">Use the full-resolution SVG for a zoomable browser view; the GitHub source link remains available for provenance and history.</p>
        </div>
      </article>`;
  }

  function renderResearchIIISourceRecord() {
    const section = document.getElementById('research-iii-source-program');
    if (!section || document.getElementById('research-iii-source-complete-figure-gallery')) return;

    const anchor = document.getElementById('research-iii-source-visual-anchor');
    const sourceCatalog = section.querySelector('.program-source-grid');
    const curated = RESEARCH_III_FIGURES.filter((record) => RESEARCH_III_CURATED.has(record.file));

    const story = document.createElement('div');
    story.id = 'research-iii-source-curated-visual-story';
    story.className = 'source-visual-record';
    story.innerHTML = `
      <div class="source-visual-record-head">
        <div><span class="source-visual-badge">Curated Research III source path</span><h3>Follow the measurement-science record from target to falsification</h3><p>These six source-linked visuals provide the shortest rigorous path through the Research III record: define the program, match evidence to the target, preserve the evidence profile, state identification limits, validate transport and causal robustness, then compare competing theories. The previews are deliberately large so labels remain readable without relying on GitHub's compact SVG preview.</p></div>
        <span class="source-visual-badge">6-stage source path</span>
      </div>
      <div class="source-visual-grid">${curated.map(researchIIISourceCard).join('')}</div>`;

    const complete = document.createElement('div');
    complete.id = 'research-iii-source-complete-figure-gallery';
    complete.className = 'source-visual-record';
    complete.innerHTML = `
      <div class="source-visual-record-head">
        <div><span class="source-visual-badge">Complete pinned Research III visual record</span><h3>All 9 canonical Research III figures with readable source views</h3><p>This gallery exposes the complete current Research III figure set from validated revision ${MEASUREMENT_PIN.slice(0, 8)}. Each figure is rendered at a substantially larger reading size and links to its scientific context, GitHub source history, and direct full-resolution SVG.</p></div>
        <span class="source-visual-badge">9 / 9 visible</span>
      </div>
      <div class="source-section-visual-links"><a href="${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/docs/visual-research-guide.md">Open the Research III visual guide</a><a href="${MEASUREMENT_REPO}/blob/${MEASUREMENT_PIN}/docs/figure-catalog.md">Open the Research III figure catalog</a></div>
      <div class="source-visual-grid">${RESEARCH_III_FIGURES.map(researchIIISourceCard).join('')}</div>`;

    if (anchor) {
      anchor.insertAdjacentElement('afterend', story);
      story.insertAdjacentElement('afterend', complete);
    } else if (sourceCatalog) {
      sourceCatalog.insertAdjacentElement('beforebegin', story);
      story.insertAdjacentElement('afterend', complete);
    } else {
      section.append(story, complete);
    }
  }

  function render() {
    if (currentFile() !== 'sources.html') return;
    ensureStyles();
    VISUALS.forEach(insertVisual);
    renderResearchIIISourceRecord();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', render, { once: true });
  } else {
    render();
  }
})();

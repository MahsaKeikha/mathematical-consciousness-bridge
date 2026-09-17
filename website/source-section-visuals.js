(() => {
  const OBSERVER_REPO = 'https://github.com/MahsaKeikha/spatiotemporal-observer-math';
  const OBSERVER_RAW = 'https://raw.githubusercontent.com/MahsaKeikha/spatiotemporal-observer-math/main';
  const BRIDGE_REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const MEASUREMENT_PIN = '383a6cdab720b3f87c17191b7c98bd6828213b72';
  const MEASUREMENT_RAW =
    `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${MEASUREMENT_PIN}`;

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

  function ensureStyles() {
    if (document.getElementById('source-section-visual-styles')) return;
    const style = document.createElement('style');
    style.id = 'source-section-visual-styles';
    style.textContent = `
      .source-section-visual{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(250px,.75fr);gap:1.25rem;align-items:stretch;margin:1.35rem 0 1.6rem;border:1px solid rgba(120,140,170,.28);border-radius:20px;overflow:hidden;background:linear-gradient(145deg,rgba(255,255,255,.035),rgba(255,255,255,.012));box-shadow:0 18px 42px rgba(0,0,0,.12)}
      .source-section-visual-stage{display:flex;align-items:center;justify-content:center;min-height:310px;padding:1rem;background:#fff}
      .source-section-visual-stage img{display:block;width:100%;height:100%;max-height:390px;object-fit:contain;background:#fff}
      .source-section-visual-copy{display:flex;flex-direction:column;justify-content:center;padding:1.3rem 1.35rem 1.35rem 0}
      .source-section-visual-copy .eyebrow{margin:0 0 .45rem}
      .source-section-visual-copy h3{margin:0 0 .7rem;font-size:clamp(1.22rem,2vw,1.65rem);line-height:1.2}
      .source-section-visual-copy p{margin:0;line-height:1.65}
      .source-section-visual-links{display:flex;gap:.65rem;flex-wrap:wrap;margin-top:1rem}
      .source-section-visual-links a{display:inline-flex;align-items:center;min-height:38px;padding:.55rem .78rem;border:1px solid rgba(120,140,170,.3);border-radius:999px;text-decoration:none;font-size:.82rem;font-weight:800}
      .source-section-visual-links a:first-child{background:rgba(255,255,255,.055)}
      @media (max-width:820px){.source-section-visual{grid-template-columns:1fr}.source-section-visual-stage{min-height:230px}.source-section-visual-copy{padding:0 1rem 1.15rem}.source-section-visual-stage img{max-height:320px}}
    `;
    document.head.appendChild(style);
  }

  function visualMarkup(visual) {
    return `
      <div class="source-section-visual-stage">
        <a href="${visual.figureHref}" aria-label="Open full-resolution ${visual.title}">
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
        </div>
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

  function render() {
    if (currentFile() !== 'sources.html') return;
    ensureStyles();
    VISUALS.forEach(insertVisual);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', render, { once: true });
  } else {
    render();
  }
})();
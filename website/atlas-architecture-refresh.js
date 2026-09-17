(() => {
  const BRIDGE_REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';
  const RESEARCH_II_MANIFEST = 'figures/manifest.json';
  const RESEARCH_II_CORE_CATEGORY = 'theorem-or-architecture';
  const RESEARCH_II_CORE_EXPECTED = 100;
  const RESEARCH_III_PIN = '4082a357929beecc2158fe5bc159e42562de19bf';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';
  const RAW_MAIN_PREFIX =
    'https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/main/docs/figures/';
  const RAW_PIN_PREFIX =
    `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${RESEARCH_III_PIN}/docs/figures/`;
  const BLOB_MAIN_PREFIX =
    'https://github.com/MahsaKeikha/consciousness-measurement-science/blob/main/docs/figures/';
  const BLOB_PIN_PREFIX =
    `https://github.com/MahsaKeikha/consciousness-measurement-science/blob/${RESEARCH_III_PIN}/docs/figures/`;

  const RESEARCH_III_FIGURES = [
    ['Measurement architecture', 'measurement_architecture.svg', 'docs/measurement-framework.md'],
    ['Structural measurement pipeline', 'structural_measurement_pipeline.svg', 'docs/phenomenal-structure.md'],
    ['M0-M7 claim ladder', 'claim_ladder.svg', 'docs/claim-registry.md'],
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

  function pinResearchIIIVisualSources() {
    if (currentFile() !== 'visual-atlas.html') return;

    document.querySelectorAll('img').forEach((image) => {
      const source = image.getAttribute('src') || '';
      if (!source.startsWith(RAW_MAIN_PREFIX)) return;

      image.setAttribute('src', source.replace(RAW_MAIN_PREFIX, RAW_PIN_PREFIX));

      const anchor = image.closest('a');
      const href = anchor?.getAttribute('href') || '';
      if (href.startsWith(BLOB_MAIN_PREFIX)) {
        anchor.setAttribute('href', href.replace(BLOB_MAIN_PREFIX, BLOB_PIN_PREFIX));
      }
    });
  }

  function propositionNumber(path) {
    const file = path.split('/').pop() || '';
    const match = /^p([0-9]+)_/.exec(file);
    return match ? Number(match[1]) : null;
  }

  function sortResearchIICoreFigures(a, b) {
    const aNumber = propositionNumber(a.path);
    const bNumber = propositionNumber(b.path);
    if (aNumber === null && bNumber !== null) return -1;
    if (aNumber !== null && bNumber === null) return 1;
    if (aNumber !== null && bNumber !== null) return aNumber - bNumber;
    return String(a.title).localeCompare(String(b.title));
  }

  function researchIICard(record) {
    const path = String(record.path);
    const file = path.split('/').pop();
    const title = escapeHTML(record.title || file.replace(/\.svg$/, '').replaceAll('_', ' '));
    const number = propositionNumber(path);
    const badge = number === null ? 'Research II · architecture' : `Research II · P${number}`;
    const figurePage = `${BRIDGE_REPO}/blob/main/${path}`;
    const catalogPage = `${BRIDGE_REPO}/blob/main/docs/figure_catalog.md`;
    return `
      <article class="complete-figure-card" data-research-ii-core-figure="${escapeHTML(path)}">
        <a href="${figurePage}" aria-label="Open full-resolution ${title}"><img loading="lazy" decoding="async" src="figures/${escapeHTML(file)}" alt="Research II ${title}" /></a>
        <div class="complete-figure-card-body">
          <span class="figure-phase">${badge}</span>
          <h4>${title}</h4>
          <div class="figure-source-links"><a href="${catalogPage}">Catalog context</a><a href="${figurePage}">Figure source</a></div>
        </div>
      </article>`;
  }

  async function renderResearchIICoreGallery() {
    const section = document.getElementById('research-ii-visual-program');
    if (!section || document.getElementById('research-ii-complete-core-gallery')) return;

    const block = document.createElement('div');
    block.className = 'complete-record-block';
    block.id = 'research-ii-complete-core-gallery';
    block.setAttribute('aria-live', 'polite');
    block.innerHTML = `
      <div class="complete-record-head">
        <div><span class="record-badge">Canonical core visual set</span><h3>Loading the unified Research II visual record</h3><p>The Atlas is reading the exact figure manifest bundled into this Pages release.</p></div>
        <span class="record-badge">manifest audit</span>
      </div>`;

    const boundary = section.querySelector('.boundary');
    if (boundary) boundary.insertAdjacentElement('beforebegin', block);
    else section.appendChild(block);

    try {
      const response = await fetch(RESEARCH_II_MANIFEST, { cache: 'no-store' });
      if (!response.ok) throw new Error(`manifest request returned ${response.status}`);
      const manifest = await response.json();
      const allFigures = Array.isArray(manifest.figures) ? manifest.figures : [];
      const core = allFigures
        .filter((record) => record.category === RESEARCH_II_CORE_CATEGORY)
        .sort(sortResearchIICoreFigures);
      const uniquePaths = new Set(core.map((record) => record.path));
      if (core.length !== RESEARCH_II_CORE_EXPECTED || uniquePaths.size !== RESEARCH_II_CORE_EXPECTED) {
        throw new Error(`expected ${RESEARCH_II_CORE_EXPECTED} unique core figures, found ${core.length}/${uniquePaths.size}`);
      }

      const theoremCount = core.filter((record) => propositionNumber(record.path) !== null).length;
      const architectureCount = core.length - theoremCount;
      const totalCount = Number(manifest.figure_count || allFigures.length);

      block.innerHTML = `
        <div class="complete-record-head">
          <div><span class="record-badge">Canonical core visual set</span><h3>All ${core.length} Research II core visuals in one gallery</h3><p>This gallery shows every figure classified by the canonical manifest as theorem-or-architecture: ${architectureCount} architecture/conceptual visuals plus ${theoremCount} proposition/theorem visuals. It is a visual inventory, not a one-figure-per-proposition mapping. Research II separately contains 100 proposition-level results. The complete repository contains ${totalCount} canonical figures; the additional foundational quantum and quantitative support figures remain available in the full catalog.</p></div>
          <span class="record-badge">${core.length} / ${RESEARCH_II_CORE_EXPECTED} visible</span>
        </div>
        <div class="figure-source-links"><a href="${BRIDGE_REPO}/blob/main/docs/figure_catalog.md">Open all ${totalCount} canonical figures</a><a href="${BRIDGE_REPO}/blob/main/docs/theorem_roadmap.md">Open the P1-P100 theorem roadmap</a></div>
        <div class="complete-figure-grid">${core.map(researchIICard).join('')}</div>`;

      const showcase = section.querySelector('.program-visual-grid');
      if (showcase) {
        showcase.hidden = true;
        showcase.setAttribute('aria-hidden', 'true');
      }
    } catch (error) {
      block.innerHTML = `
        <div class="complete-record-head">
          <div><span class="record-badge">Gallery audit warning</span><h3>The 100-card Research II gallery did not pass its manifest check</h3><p>The original Research II showcase remains visible. Open the canonical catalog while this release is audited: ${escapeHTML(error.message || error)}.</p></div>
        </div>
        <div class="figure-source-links"><a href="${BRIDGE_REPO}/blob/main/docs/figure_catalog.md">Open the complete figure catalog</a></div>`;
    }
  }

  function researchIIICard([title, file, context]) {
    const image = `${RAW_PIN_PREFIX}${file}`;
    const figurePage = `${BLOB_PIN_PREFIX}${file}`;
    const contextPage = `${MEASUREMENT_REPO}/blob/${RESEARCH_III_PIN}/${context}`;
    return `
      <article class="complete-figure-card" data-research-iii-figure="docs/figures/${file}">
        <a href="${figurePage}" aria-label="Open full-resolution ${title}"><img loading="lazy" decoding="async" src="${image}" alt="Research III ${title}" /></a>
        <div class="complete-figure-card-body">
          <span class="figure-phase">Research III · canonical figure</span>
          <h4>${title}</h4>
          <div class="figure-source-links"><a href="${contextPage}">Scientific context</a><a href="${figurePage}">Figure source</a></div>
        </div>
      </article>`;
  }

  function renderResearchIIICompleteGallery() {
    const section = document.getElementById('research-iii-visual-program');
    if (!section || document.getElementById('research-iii-complete-figure-gallery')) return;

    document.getElementById('research-iii-complete-figure-note')?.remove();

    const block = document.createElement('div');
    block.className = 'complete-record-block';
    block.id = 'research-iii-complete-figure-gallery';
    block.innerHTML = `
      <div class="complete-record-head">
        <div><span class="record-badge">Complete canonical set</span><h3>All 3 Research III figures in one gallery</h3><p>The measurement architecture, structural measurement pipeline, and M0-M7 claim ladder are the complete current canonical visual record. All three are pinned to the validated Research III revision ${RESEARCH_III_PIN.slice(0, 8)}.</p></div>
        <span class="record-badge">3 / 3 visible</span>
      </div>
      <div class="complete-figure-grid">${RESEARCH_III_FIGURES.map(researchIIICard).join('')}</div>`;

    const boundary = section.querySelector('.boundary');
    if (boundary) boundary.insertAdjacentElement('beforebegin', block);
    else section.appendChild(block);

    const showcase = section.querySelector('.program-visual-grid');
    if (showcase) {
      showcase.hidden = true;
      showcase.setAttribute('aria-hidden', 'true');
    }
  }

  function collapseDetailedResearchIIArchive() {
    const divider = document.getElementById('research-ii-frontier-archive');
    if (!divider || document.getElementById('research-ii-detailed-archive')) return;
    const parent = divider.parentElement;
    if (!parent) return;

    const details = document.createElement('details');
    details.id = 'research-ii-detailed-archive';
    details.className = 'complete-record-block';
    details.dataset.researchIiArchive = 'collapsed-by-default';

    const summary = document.createElement('summary');
    summary.className = 'complete-record-head';
    summary.innerHTML = '<span class="record-badge">Detailed Research II archive</span><strong>Open the current-first theorem frontiers and supporting visual sections</strong>';
    details.appendChild(summary);
    parent.insertBefore(details, divider);

    let node = divider;
    while (node) {
      const next = node.nextElementSibling;
      details.appendChild(node);
      node = next;
    }

    const openHashTarget = () => {
      const id = window.location.hash.replace(/^#/, '');
      if (!id) return;
      const target = document.getElementById(id);
      if (!target || !details.contains(target)) return;
      details.open = true;
      window.requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }));
    };

    window.addEventListener('hashchange', openHashTarget);
    openHashTarget();
  }

  function renderUnifiedAtlas() {
    if (currentFile() !== 'visual-atlas.html') return;
    pinResearchIIIVisualSources();
    renderResearchIIICompleteGallery();
    collapseDetailedResearchIIArchive();
    void renderResearchIICoreGallery();
  }

  function waitForResearchIEvidence(attempt = 0) {
    if (currentFile() !== 'visual-atlas.html') return;
    if (document.getElementById('research-i-complete-figure-gallery') || attempt >= 80) {
      renderUnifiedAtlas();
      return;
    }
    window.setTimeout(() => waitForResearchIEvidence(attempt + 1), 25);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => waitForResearchIEvidence(), { once: true });
  } else {
    waitForResearchIEvidence();
  }
})();

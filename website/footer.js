(() => {
  const AUTHOR_NAME = 'Mahsa Keikha';
  const AUTHOR_URL = 'https://github.com/MahsaKeikha';
  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';

  const RESOURCE_LINKS = {
    'Proof documents': [`${REPO}/tree/main/docs`, 'Open proof documents'],
    Implementations: [`${REPO}/tree/main/src/consciousness_bridge`, 'Open implementations'],
    'Regression tests': [`${REPO}/tree/main/tests`, 'Open regression tests'],
    Figures: [`${REPO}/tree/main/docs/figures`, 'Open canonical figures'],
    'Release metadata': [REPO, 'Open repository metadata'],
    'Version history': [`${REPO}/blob/main/CHANGELOG.md`, 'Open version history'],
    'Read assumptions': ['research-map.html#proposition-atlas', 'Choose a proposition and read its assumptions'],
    'Check dependencies': [`${REPO}/blob/main/docs/equation_and_citation_map.md`, 'Open equation and citation map'],
    'Inspect proof': ['research-map.html#proposition-atlas', 'Open proposition proof index'],
    'Run implementation': [`${REPO}/tree/main/src/consciousness_bridge`, 'Open executable implementation'],
    'Run tests': [`${REPO}/tree/main/tests`, 'Open test suite'],
    'Check scientific boundary': [`${REPO}/blob/main/docs/claim_evidence_standard.md`, 'Open claim and evidence standard'],
  };

  function currentFile() {
    return window.location.pathname.split('/').pop() || 'index.html';
  }

  function addAuthorAttribution() {
    document.querySelectorAll('footer').forEach((footer) => {
      let attribution = footer.querySelector('.footer-attribution');
      if (!attribution) {
        attribution = footer.querySelector('p') || document.createElement('p');
        attribution.classList.add('footer-attribution');
        if (!attribution.isConnected) footer.prepend(attribution);
      }

      attribution.replaceChildren(document.createTextNode('Research by '));
      const author = document.createElement('a');
      author.href = AUTHOR_URL;
      author.textContent = AUTHOR_NAME;
      author.rel = 'author';
      attribution.append(
        author,
        document.createTextNode(' · Mathematical Consciousness Bridge'),
      );
    });
  }

  function syncSourcesFrontier() {
    if (currentFile() !== 'sources.html') return;

    const p99 = document.querySelector('#p99-source');
    if (!p99) return;

    const p99Eyebrow = p99.querySelector('.section-head .eyebrow');
    if (p99Eyebrow) {
      p99Eyebrow.textContent = 'Immediate predecessor theorem source · P99';
    }

    if (document.querySelector('#p100-source')) return;

    const p100 = document.createElement('section');
    p100.id = 'p100-source';
    p100.innerHTML = `
      <div class="section-head">
        <p class="eyebrow">Current theorem source · P100</p>
        <h2>Anytime-valid sequential e-process</h2>
        <p>P100 extends the P99 evidence layer across a sequence of fresh certification rounds. Under conditional round validity and predictable stakes, the reserve-stake product is a nonnegative supermartingale and can be monitored after every round with an anytime-valid crossing rule.</p>
      </div>
      <div class="source-grid">
        <a href="${REPO}/blob/main/docs/proposition_100_anytime_sequential_eprocess.md"><h3>Proposition 100</h3><p>Formal sequential e-process theorem, predictable-stake construction, exact crossing checkpoint, and scientific boundary.</p></a>
        <a href="${REPO}/blob/main/docs/p100_equation_provenance.md"><h3>P100 provenance</h3><p>Separates standard supermartingale, e-process, predictable-betting, and Ville ingredients from repository-specific integration.</p></a>
        <a href="${REPO}/blob/main/src/consciousness_bridge/anytime_sequential_eprocess.py"><h3>P100 implementation</h3><p>Exact-rational stakes, reserve factors, cumulative process values, threshold checks, and sequential validity guards.</p></a>
        <a href="${REPO}/blob/main/tests/test_anytime_sequential_eprocess.py"><h3>P100 exact tests</h3><p>Conditional freshness, predictable-plan guards, reserve protection, exact crossings, and sample-accounting checks.</p></a>
        <a href="${REPO}/blob/main/docs/figures/p100_anytime_sequential_eprocess.svg"><h3>P100 theorem figure</h3><p>Canonical visual record for fresh rounds, predictable stakes, cumulative evidence, and the anytime-valid crossing.</p></a>
        <a href="${REPO}/blob/main/docs/reproducibility.md"><h3>P100 reproducibility path</h3><p>Direct proof, provenance, implementation, test, figure, environment, and reproduction entry points.</p></a>
      </div>
      <div class="boundary"><p><strong>Scientific boundary:</strong> P100 is a sequential inference theorem under its declared conditional-validity, freshness, and predictability assumptions. It does not identify the latent state with consciousness, establish nonphysicality, prove model truth from non-rejection, or complete the physical-to-experiential bridge.</p></div>
    `;
    p99.insertAdjacentElement('beforebegin', p100);
  }

  function wireSourceCards() {
    if (currentFile() !== 'sources.html') return;

    document.querySelectorAll('.result, .flow-node').forEach((card) => {
      const heading = card.querySelector('h3')?.textContent?.trim();
      const target = RESOURCE_LINKS[heading];
      if (!target || card.querySelector('.resource-card-overlay')) return;

      const [href, label] = target;
      const link = document.createElement('a');
      link.className = 'resource-card-overlay';
      link.href = href;
      link.setAttribute('aria-label', label);
      link.title = label;
      link.style.position = 'absolute';
      link.style.inset = '0';
      link.style.zIndex = '1';

      card.style.position = 'relative';
      card.classList.add('interactive-card', 'resource-link-card');
      card.append(link);
    });
  }

  function loadResearchMapGuide() {
    if (currentFile() !== 'research-map.html') return;
    if (document.querySelector('script[data-research-map-guide]')) return;

    const script = document.createElement('script');
    script.src = 'research-map-guide.js';
    script.dataset.researchMapGuide = 'true';
    document.head.append(script);
  }

  function run() {
    addAuthorAttribution();
    syncSourcesFrontier();
    wireSourceCards();
    loadResearchMapGuide();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
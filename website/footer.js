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
    wireSourceCards();
    loadResearchMapGuide();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
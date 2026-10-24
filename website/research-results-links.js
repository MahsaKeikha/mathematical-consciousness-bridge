(() => {
  const RESULTS_LINKS = {
    'observer-research.html': {
      label: 'Research I',
      summary: 'Open the complete current Research I record: 58 proposition-level results, 45 reproducible experiments, 33 scientific result figures, and the supporting source trail.',
      primary: ['sources.html#research-i-source-program', 'View all Research I results'],
      secondary: ['visual-atlas.html#research-i-complete-figure-gallery', 'View all Research I figures'],
    },
    'research-map.html': {
      label: 'Research II',
      summary: 'Jump directly to the complete P1-P100 proposition navigator, where every current Research II result has its own visible link to the canonical theorem record.',
      primary: ['research-map.html#complete-proposition-navigator', 'View all Research II results'],
      secondary: ['sources.html#complete-source-sequence', 'Audit all P1-P100 sources'],
    },
    'measurement-science.html': {
      label: 'Research III',
      summary: 'Open the complete current Research III measurement-science record, including specifications, identification results, validation architecture, canonical figures, code, tests, and reproducibility sources.',
      primary: ['sources.html#research-iii-source-program', 'View all Research III results'],
      secondary: ['visual-atlas.html#research-iii-complete-figure-gallery', 'View all Research III figures'],
    },
  };

  function currentFile() {
    return window.location.pathname.split('/').pop() || 'index.html';
  }

  function render() {
    const contract = RESULTS_LINKS[currentFile()];
    if (!contract || document.querySelector('[data-research-results-entry]')) return;

    const orientation = document.querySelector('.scientific-orientation');
    const hero = document.querySelector('main .hero, main .compact-hero');
    const anchor = orientation || hero;
    if (!anchor) return;

    const section = document.createElement('section');
    section.className = 'boundary research-results-entry';
    section.dataset.researchResultsEntry = currentFile();
    section.innerHTML = `
      <p class="eyebrow">Complete ${contract.label} record</p>
      <h2>See every result collected so far</h2>
      <p>${contract.summary}</p>
      <div class="hero-actions">
        <a class="button primary" href="${contract.primary[0]}">${contract.primary[1]}</a>
        <a class="button" href="${contract.secondary[0]}">${contract.secondary[1]}</a>
      </div>`;

    anchor.insertAdjacentElement('afterend', section);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', render, { once: true });
  } else {
    render();
  }
})();
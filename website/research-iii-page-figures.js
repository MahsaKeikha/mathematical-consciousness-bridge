(() => {
  function renderResultsLinks() {
    if ((window.location.pathname.split('/').pop() || 'index.html') !== 'measurement-science.html') return;

    const sections = [...document.querySelectorAll('main > section')];
    const section = sections.find((candidate) =>
      candidate.querySelector('.section-head .eyebrow')?.textContent?.trim() === 'Visual architecture'
    );
    if (!section || section.querySelector('[data-research-iii-results-links]')) return;

    const head = section.querySelector('.section-head');
    if (!head) return;

    const actions = document.createElement('div');
    actions.className = 'hero-actions';
    actions.dataset.researchIiiResultsLinks = 'true';
    actions.innerHTML = `
      <a class="button primary" href="visual-atlas.html#research-iii-complete-figure-gallery">Open all Research III results and figures</a>
      <a class="button" href="sources.html#research-iii-source-visual-anchor">Open complete Research III source record</a>`;
    head.appendChild(actions);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderResultsLinks, { once: true });
  } else {
    renderResultsLinks();
  }
})();
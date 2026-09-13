(() => {
  const AUTHOR_NAME = 'Mahsa Keikha';
  const AUTHOR_URL = 'https://github.com/MahsaKeikha';
  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';

  function normalizeFooter() {
    document.querySelectorAll('footer').forEach((footer) => {
      footer.innerHTML = `
        <p class="footer-attribution">Research by <a rel="author" href="${AUTHOR_URL}">${AUTHOR_NAME}</a> · Mathematical Consciousness Bridge</p>
        <p>87 proposition-level results · Current theorem frontier: P87 · Formal release: v0.82.0 · Final physical-to-experiential bridge: open</p>
        <p><a href="index.html">Overview</a> · <a href="plain-language.html">Plain Language</a> · <a href="start-here.html">Start Here</a> · <a href="research-map.html">Research Map</a> · <a href="research-navigation.html">Research Navigation</a> · <a href="visual-atlas.html">Visual Atlas</a> · <a href="implementation.html">Reproducibility</a> · <a href="${REPO}">GitHub</a></p>`;
    });
  }

  document.addEventListener('DOMContentLoaded', normalizeFooter);
})();

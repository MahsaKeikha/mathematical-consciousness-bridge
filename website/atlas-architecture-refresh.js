(() => {
  const RESEARCH_III_PIN = '1ceea4c428d835ec9a8a417cbf238d9bcfe1d7c3';
  const RAW_MAIN_PREFIX =
    'https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/main/docs/figures/';
  const RAW_PIN_PREFIX =
    `https://raw.githubusercontent.com/MahsaKeikha/consciousness-measurement-science/${RESEARCH_III_PIN}/docs/figures/`;
  const BLOB_MAIN_PREFIX =
    'https://github.com/MahsaKeikha/consciousness-measurement-science/blob/main/docs/figures/';
  const BLOB_PIN_PREFIX =
    `https://github.com/MahsaKeikha/consciousness-measurement-science/blob/${RESEARCH_III_PIN}/docs/figures/`;

  function currentFile() {
    return window.location.pathname.split('/').pop() || 'index.html';
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

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', pinResearchIIIVisualSources, {
      once: true,
    });
  } else {
    pinResearchIIIVisualSources();
  }
})();

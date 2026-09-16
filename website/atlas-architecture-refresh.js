(() => {
  const VERSIONED_SRC = 'figures/research_architecture.svg?v=20260916-color-safe';

  function currentFile() {
    return window.location.pathname.split('/').pop() || 'index.html';
  }

  function ensureStyles() {
    if (document.getElementById('atlas-architecture-refresh-styles')) return;
    const style = document.createElement('style');
    style.id = 'atlas-architecture-refresh-styles';
    style.textContent = `
      .figure-card img.atlas-architecture-current {
        display: block;
        width: min(100%, var(--figure-card-media-max, 980px));
        max-width: 100%;
        max-height: 530px;
        height: auto;
        margin-inline: auto;
        object-fit: contain;
        object-position: center;
        background: #ffffff;
      }
    `;
    document.head.appendChild(style);
  }

  function refreshArchitectureFigure() {
    if (currentFile() !== 'visual-atlas.html') return;
    const images = document.querySelectorAll('img[src*="research_architecture.svg"]');
    if (!images.length) return;

    ensureStyles();
    images.forEach((image) => {
      image.src = VERSIONED_SRC;
      image.classList.add('atlas-architecture-current');
      image.setAttribute('data-architecture-version', 'color-safe');
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', refreshArchitectureFigure, { once: true });
  } else {
    refreshArchitectureFigure();
  }
})();

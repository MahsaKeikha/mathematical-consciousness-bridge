(() => {
  function slugify(text) {
    return text
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '')
      .slice(0, 72);
  }

  function uniqueId(base, used) {
    let id = base || 'section';
    let suffix = 2;
    while (used.has(id) || document.getElementById(id)) {
      id = `${base || 'section'}-${suffix}`;
      suffix += 1;
    }
    used.add(id);
    return id;
  }

  function addHeadingAnchors() {
    const used = new Set();
    document.querySelectorAll('main h2, main h3').forEach((heading) => {
      if (heading.closest('.reader-trail')) return;
      if (heading.querySelector('.heading-anchor')) return;

      const label = heading.textContent.trim();
      const id = heading.id || uniqueId(slugify(label), used);
      heading.id = id;
      used.add(id);

      const anchor = document.createElement('a');
      anchor.className = 'heading-anchor';
      anchor.href = `#${id}`;
      anchor.textContent = '#';
      anchor.setAttribute('aria-label', `Link to ${label}`);
      anchor.title = 'Link to this section';
      heading.append(anchor);
    });
  }

  function makeStandaloneFiguresOpenable() {
    document.querySelectorAll('main img').forEach((image) => {
      if (image.closest('a')) return;
      const src = image.getAttribute('src');
      if (!src) return;
      const card = image.closest('.interactive-card');
      if (card) return;

      image.classList.add('openable-figure');
      image.tabIndex = 0;
      image.setAttribute('role', 'link');
      image.setAttribute('aria-label', image.alt ? `Open figure: ${image.alt}` : 'Open figure');
      const open = () => {
        window.location.href = src;
      };
      image.addEventListener('click', open);
      image.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          open();
        }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    addHeadingAnchors();
    makeStandaloneFiguresOpenable();
  });
})();
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

  function addResearchStatusCardStyles() {
    if (document.getElementById('research-status-card-styles')) return;
    const style = document.createElement('style');
    style.id = 'research-status-card-styles';
    style.textContent = `
      .status-grid > a.research-status-link {
        position: relative;
        display: block;
        min-width: 0;
        padding: 18px 19px 50px;
        border: 1px solid var(--line);
        border-radius: 13px;
        background: var(--paper);
        color: var(--ink);
        text-decoration: none !important;
        cursor: pointer;
        transition: transform 150ms ease, border-color 150ms ease, box-shadow 150ms ease, background-color 150ms ease;
      }
      .status-grid > a.research-status-link:hover,
      .status-grid > a.research-status-link:focus-visible {
        transform: translateY(-2px);
        border-color: #8f9db7;
        background: #fbfcff;
        box-shadow: 0 9px 24px rgba(31, 45, 84, 0.09);
        text-decoration: none !important;
      }
      .status-grid > a.research-status-link::after {
        content: 'Open research page →';
      }
    `;
    document.head.append(style);
  }

  function wireResearchStatusCards() {
    const destinations = new Map([
      ['research i', 'observer-research.html'],
      ['research ii', 'research-map.html'],
      ['research iii', 'measurement-science.html'],
    ]);

    let linkedAny = false;
    document.querySelectorAll('.status-grid').forEach((grid) => {
      Array.from(grid.children).forEach((card) => {
        if (card.matches('a')) return;
        const label = card.querySelector('strong')?.textContent?.trim().toLowerCase();
        const href = label ? destinations.get(label) : null;
        if (!href) return;

        const link = document.createElement('a');
        link.className = `${card.className || ''} research-status-link`.trim();
        link.href = href;
        link.innerHTML = card.innerHTML;
        link.setAttribute('aria-label', `Open ${card.querySelector('strong')?.textContent?.trim()} website page`);
        link.title = 'Open research page';
        card.replaceWith(link);
        linkedAny = true;
      });
    });

    if (linkedAny) addResearchStatusCardStyles();
  }

  function addResearchPathCardStyles() {
    if (document.getElementById('research-path-card-styles')) return;
    const style = document.createElement('style');
    style.id = 'research-path-card-styles';
    style.textContent = `
      .research-path-card {
        cursor: pointer;
        position: relative;
        transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
      }
      .research-path-card:hover,
      .research-path-card:focus-visible {
        transform: translateY(-3px);
        box-shadow: 0 14px 36px rgba(15, 23, 42, 0.12);
        outline: none;
      }
      .research-path-card:focus-visible {
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.28), 0 14px 36px rgba(15, 23, 42, 0.12);
      }
      .research-path-card .research-path-cue {
        display: inline-block;
        margin-top: 0.8rem;
        font-weight: 700;
        line-height: 1.35;
        color: var(--link, #1d4ed8);
      }
    `;
    document.head.append(style);
  }

  function wireResearchPathCards() {
    if (!document.body || !document.querySelector('#orientation')) return;

    const destinations = [
      'implementation.html#stage-01',
      'implementation.html#stage-02',
      'implementation.html#stage-03',
      'implementation.html#stage-04',
      'implementation.html#stage-05',
      'implementation.html#stage-06',
      'implementation.html#stage-07',
      'implementation.html#stage-08',
      'implementation.html#stage-09',
      'implementation.html#stage-10',
    ];

    const firstGrid = document.querySelector('#orientation .result-grid');
    if (!firstGrid) return;

    const cards = Array.from(firstGrid.children).filter((element) => element.matches('.result'));
    if (cards.length < destinations.length) return;

    addResearchPathCardStyles();

    cards.slice(0, destinations.length).forEach((card, index) => {
      if (card.dataset.implementationLinked === 'true') return;
      const href = destinations[index];
      const title = card.querySelector('h3')?.textContent?.trim() || `research stage ${index + 1}`;
      const cue = document.createElement('span');
      cue.className = 'research-path-cue';
      cue.textContent = 'How it works & implementation →';
      cue.setAttribute('aria-hidden', 'true');
      card.append(cue);

      card.classList.add('research-path-card');
      card.dataset.implementationLinked = 'true';
      card.tabIndex = 0;
      card.setAttribute('role', 'link');
      card.setAttribute('aria-label', `${title}: open how it works and implementation details`);
      card.title = 'Open implementation details';

      const open = () => {
        window.location.href = href;
      };
      card.addEventListener('click', (event) => {
        if (event.target.closest('a, button')) return;
        open();
      });
      card.addEventListener('keydown', (event) => {
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
    wireResearchStatusCards();
    wireResearchPathCards();
  });
})();
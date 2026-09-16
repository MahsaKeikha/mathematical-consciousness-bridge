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
      a.research-path-card {
        cursor: pointer;
        position: relative;
        display: block;
        color: var(--ink);
        text-decoration: none !important;
        transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
      }
      a.research-path-card:hover,
      a.research-path-card:focus-visible {
        transform: translateY(-3px);
        border-color: #8f9db7;
        background: #fbfcff;
        box-shadow: 0 14px 36px rgba(15, 23, 42, 0.12);
        outline: none;
        text-decoration: none !important;
      }
      a.research-path-card .research-path-cue {
        display: inline-block;
        margin-top: 0.8rem;
        font-weight: 700;
        line-height: 1.35;
        color: var(--accent, #1f3a7a);
      }
    `;
    document.head.append(style);
  }

  function wireResearchPathCards() {
    const stageGrid = document.querySelector('#program-stages .result-grid');
    if (!stageGrid) return;

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

    const cards = Array.from(stageGrid.children).filter((element) => element.matches('.result'));
    if (cards.length < destinations.length) return;

    addResearchPathCardStyles();

    cards.slice(0, destinations.length).forEach((card, index) => {
      const href = destinations[index];
      const title = card.querySelector('h3')?.textContent?.trim() || `research stage ${index + 1}`;
      const link = document.createElement('a');
      link.className = `${card.className || 'result'} research-path-card`.trim();
      link.href = href;
      link.innerHTML = card.innerHTML;
      link.setAttribute('aria-label', `${title}: open how it works and implementation details`);
      link.title = 'Open implementation details';

      const cue = document.createElement('span');
      cue.className = 'research-path-cue';
      cue.textContent = 'How it works & implementation →';
      cue.setAttribute('aria-hidden', 'true');
      link.append(cue);

      card.replaceWith(link);
    });
  }

  function propositionNumber(text) {
    const match = String(text || '').match(/\bP(\d{1,3})\b/i);
    return match ? Number(match[1]) : null;
  }

  function normalizeResearchMapResultBoxes() {
    const bridge = document.querySelector('#bridge-lineage');
    if (bridge && !bridge.querySelector('.research-map-detail-grid')) {
      const headings = Array.from(bridge.children).filter(
        (element) => element.tagName === 'H3' && /^P(?:71|72|73):/.test(element.textContent.trim()),
      );

      if (headings.length) {
        const grid = document.createElement('div');
        grid.className = 'result-grid research-map-detail-grid';
        bridge.insertBefore(grid, headings[0]);

        headings.forEach((heading) => {
          const detail = heading.nextElementSibling;
          const number = propositionNumber(heading.textContent);
          const card = document.createElement('article');
          card.className = 'result research-map-result-card';
          if (number) card.id = `p${number}`;

          const badge = document.createElement('span');
          badge.textContent = number ? `P${number}` : 'Result';
          card.append(badge);
          grid.append(card);
          card.append(heading);
          if (detail?.tagName === 'P') card.append(detail);
        });

        const missing = [
          {
            number: 74,
            title: 'Finite-sample target-channel recovery certification',
            description:
              'Propagate simultaneous eight-cell sampling uncertainty through the P73 inversion and refuse recovery when finite-data margins remain too close to the degeneracy boundary.',
            href: 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_74_finite_sample_target_channel_recovery.md',
          },
          {
            number: 75,
            title: 'Target-model adequacy and four-view overidentification',
            description:
              'Separate identifiability from adequacy: a fourth binary view introduces observable restrictions that can falsify the declared conditional-independence target model.',
            href: 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_75_target_model_adequacy_overidentification.md',
          },
          {
            number: 76,
            title: 'Finite-sample target-model adequacy rejection',
            description:
              'Reject only when finite IID uncertainty leaves a necessary P75 restriction separated from zero. Nonrejection remains nonacceptance.',
            href: 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge/blob/main/docs/proposition_76_finite_sample_target_model_adequacy.md',
          },
        ];

        missing.forEach(({ number, title, description, href }) => {
          if (document.getElementById(`p${number}`)) return;
          const card = document.createElement('article');
          card.className = 'result research-map-result-card';
          card.id = `p${number}`;
          card.innerHTML = `<span>P${number}</span><h3>P${number}: ${title}</h3><p>${description}</p><p><a href="${href}">Read P${number}</a></p>`;
          grid.append(card);
        });
      }
    }

    ['#p92-research-map', '#p93-research-map', '#p94-research-map'].forEach((selector) => {
      const section = document.querySelector(selector);
      if (!section) return;
      section.classList.add('result', 'research-map-result-card');
    });
  }

  function primaryCardHref(card) {
    const links = Array.from(card.querySelectorAll('a[href]')).filter(
      (link) => !link.classList.contains('heading-anchor'),
    );
    const preferred = links.find((link) => {
      const label = (link.textContent || '').toLowerCase();
      return label.includes('theorem') || label.includes('proposition') || label.includes('open p') || label.includes('read p');
    });
    if (preferred) return preferred.href;
    if (links.length) return links[0].href;

    const number = propositionNumber(card.textContent);
    if (number) return `research-map.html#p${number}`;
    return null;
  }

  function clickableCardLabel(card) {
    const heading = card.querySelector('h2, h3, h4, strong');
    const title = heading?.textContent?.trim();
    if (title) return `Open result: ${title}`;
    const number = propositionNumber(card.textContent);
    return number ? `Open result P${number}` : 'Open result';
  }

  function wireWholeResultCard(card) {
    if (!(card instanceof HTMLElement)) return;
    if (card.matches('a')) return;
    if (card.dataset.clickableReady === 'true') return;

    const href = primaryCardHref(card);
    if (!href) return;

    card.dataset.clickableReady = 'true';
    card.classList.add('interactive-card');
    card.tabIndex = 0;
    card.setAttribute('role', 'link');
    card.setAttribute('aria-label', clickableCardLabel(card));
    card.title = 'Open this result';

    const open = () => {
      window.location.href = href;
    };

    card.addEventListener('click', (event) => {
      if (event.target.closest('a, button, input, select, textarea, summary')) return;
      open();
    });

    card.addEventListener('keydown', (event) => {
      if (event.key !== 'Enter' && event.key !== ' ') return;
      if (event.target.closest('a, button, input, select, textarea, summary')) return;
      event.preventDefault();
      open();
    });
  }

  function wireAllResultCards() {
    const cards = new Set();
    const containers = document.querySelectorAll(
      '.result-grid, .results-grid, .theorem-grid, .theorem-cards, .key-results, .key-results-grid, .frontier-summary-grid, .roadmap-grid',
    );
    containers.forEach((container) => {
      Array.from(container.children).forEach((card) => cards.add(card));
    });

    document
      .querySelectorAll('.result, .result-card, .result-tile, .theorem-card, .theorem-tile, .key-result, .key-result-card, .frontier-summary-card')
      .forEach((card) => cards.add(card));

    cards.forEach(wireWholeResultCard);
  }

  function addResearchOverviewDiagramStyles() {
    if (document.getElementById('research-overview-diagram-styles')) return;
    const style = document.createElement('style');
    style.id = 'research-overview-diagram-styles';
    style.textContent = `
      #research-ii-overview .research-ii-figure-card {
        grid-template-columns: minmax(280px, 0.82fr) minmax(320px, 1.18fr);
        align-items: center;
      }
      #research-ii-overview .research-ii-figure-card > a {
        display: flex;
        min-width: 0;
        align-items: center;
        justify-content: center;
      }
      #research-ii-overview .research-ii-figure-card img {
        width: min(100%, 560px);
        max-width: 100%;
        height: auto;
        max-height: 360px;
        object-fit: contain;
      }
      @media (max-width: 900px) {
        #research-ii-overview .research-ii-figure-card {
          grid-template-columns: 1fr;
        }
        #research-ii-overview .research-ii-figure-card img {
          width: min(100%, 620px);
          max-height: none;
        }
      }
    `;
    document.head.append(style);
  }

  document.addEventListener('DOMContentLoaded', () => {
    addHeadingAnchors();
    makeStandaloneFiguresOpenable();
    wireResearchStatusCards();
    wireResearchPathCards();
    normalizeResearchMapResultBoxes();
    wireAllResultCards();
    addResearchOverviewDiagramStyles();
  });
})();
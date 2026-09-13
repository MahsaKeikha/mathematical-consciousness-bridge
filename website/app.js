(() => {
  const PROGRAM = Object.freeze({
    resultCount: 87,
    frontier: 'P87',
    release: 'v0.82.0',
    boundary:
      'P87 is a conditional model-separation result for the declared P75 target-measurement family. It does not identify a latent state with consciousness, prove that consciousness is nonphysical, or complete the physical-to-experiential bridge. The final bridge remains open.',
  });

  const PAGES = [
    { file: 'index.html', label: 'Overview' },
    { file: 'plain-language.html', label: 'Plain Language' },
    { file: 'start-here.html', label: 'Start Here' },
    { file: 'research-map.html', label: 'Research Map' },
    { file: 'research-navigation.html', label: 'Research Navigation' },
    { file: 'visual-atlas.html', label: 'Visual Atlas' },
    { file: 'physics-mathematics.html', label: 'Physics & Mathematics' },
    { file: 'implementation.html', label: 'Reproducibility' },
    { file: 'sources.html', label: 'Sources' },
  ];

  const EXPLORE_ITEMS = [
    {
      file: 'research-navigation.html',
      kicker: 'Index',
      label: 'Research navigation',
      description: 'Choose the shortest route to a branch, theorem range, proof, figure, or audit record.',
    },
    {
      file: 'visual-atlas.html',
      kicker: 'Figures',
      label: 'Visual atlas',
      description: 'Browse a curated visual path through the same research program.',
    },
    {
      file: 'physics-mathematics.html',
      kicker: 'Formal layer',
      label: 'Physics & mathematics',
      description: 'Open the definitions, equations, assumptions, and theorem structure.',
    },
    {
      file: 'implementation.html',
      kicker: 'Audit',
      label: 'Reproducibility',
      description: 'Follow claims into code, tests, figures, provenance, and reproducible checks.',
    },
    {
      file: 'sources.html',
      kicker: 'Provenance',
      label: 'Sources',
      description: 'Trace references, equation provenance, source roles, and citation boundaries.',
    },
  ];

  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';

  const propositionLinks = {
    19: `${REPO}/blob/main/docs/proposition_19_fundamental_physical_sufficiency.md`,
    71: `${REPO}/blob/main/docs/proposition_71_target_provenance_noncircularity.md`,
    72: `${REPO}/blob/main/docs/proposition_72_target_measurement_channel_robustness.md`,
    73: `${REPO}/blob/main/docs/proposition_73_target_channel_identifiability.md`,
    74: `${REPO}/blob/main/docs/proposition_74_finite_sample_target_channel_recovery.md`,
    75: `${REPO}/blob/main/docs/proposition_75_target_model_adequacy_overidentification.md`,
    76: `${REPO}/blob/main/docs/proposition_76_finite_sample_target_model_adequacy.md`,
    77: `${REPO}/blob/main/docs/proposition_77_full_law_model_set_separation.md`,
    78: `${REPO}/blob/main/docs/proposition_78_certified_continuous_model_separation.md`,
    79: `${REPO}/blob/main/docs/proposition_79_certified_sampling_radius.md`,
    80: `${REPO}/blob/main/docs/proposition_80_simplex_coupled_model_separation.md`,
    81: `${REPO}/blob/main/docs/proposition_81_projection_event_model_separation.md`,
    82: `${REPO}/blob/main/docs/proposition_82_exact_nested_projection_contrast.md`,
    83: `${REPO}/blob/main/docs/proposition_83_exact_projection_parity.md`,
    84: `${REPO}/blob/main/docs/proposition_84_exact_projection_parity_contrast.md`,
    85: `${REPO}/blob/main/docs/proposition_85_exact_triple_projection_parity_functional.md`,
    86: `${REPO}/blob/main/docs/proposition_86_exact_minimally_weighted_quad_projection_parity_functional.md`,
    87: `${REPO}/blob/main/docs/proposition_87_exact_bounded_primitive_quad_projection_parity_functional.md`,
  };

  function currentFile() {
    const file = window.location.pathname.split('/').pop();
    return file || 'index.html';
  }

  function createSimpleNavLink(file, label, current) {
    const link = document.createElement('a');
    link.href = file;
    link.textContent = label;
    link.className = 'top-level-link';
    if (file === current) link.setAttribute('aria-current', 'page');
    return link;
  }

  function createExploreDropdown(current) {
    const details = document.createElement('details');
    details.className = 'nav-dropdown explore-menu';
    if (EXPLORE_ITEMS.some((item) => item.file === current)) {
      details.classList.add('contains-current');
    }

    const summary = document.createElement('summary');
    summary.className = 'nav-dropbtn';
    summary.textContent = 'Explore';
    summary.setAttribute('aria-label', 'Explore navigation');
    details.append(summary);

    const menu = document.createElement('div');
    menu.className = 'nav-dropdown-menu';
    EXPLORE_ITEMS.forEach((item) => {
      const link = document.createElement('a');
      link.href = item.file;
      link.className = 'nav-dropdown-item';
      if (item.file === current) link.setAttribute('aria-current', 'page');
      link.innerHTML = `<span>${item.kicker}</span><strong>${item.label}</strong><small>${item.description}</small>`;
      menu.append(link);
    });
    details.append(menu);
    return details;
  }

  function ensureNavigation() {
    const topbar = document.querySelector('.topbar');
    if (!topbar) return;

    let nav = topbar.querySelector('nav');
    if (!nav) {
      nav = document.createElement('nav');
      topbar.append(nav);
    }

    nav.replaceChildren();
    const file = currentFile();
    nav.append(createSimpleNavLink('index.html', 'Overview', file));
    nav.append(createSimpleNavLink('plain-language.html', 'Plain Language', file));
    nav.append(createSimpleNavLink('start-here.html', 'Start Here', file));
    nav.append(createSimpleNavLink('research-map.html', 'Research Map', file));
    nav.append(createExploreDropdown(file));

    const repo = document.createElement('a');
    repo.href = REPO;
    repo.textContent = 'GitHub';
    repo.className = 'external-nav top-level-link';
    nav.append(repo);

    let button = topbar.querySelector('.nav-toggle');
    if (!button) {
      button = document.createElement('button');
      button.className = 'nav-toggle';
      button.type = 'button';
      button.textContent = 'Menu';
      button.setAttribute('aria-label', 'Toggle navigation');
      topbar.insertBefore(button, nav);
    }
    button.setAttribute('aria-expanded', 'false');

    button.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      button.setAttribute('aria-expanded', String(open));
    });

    nav.querySelectorAll('a').forEach((link) =>
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        button.setAttribute('aria-expanded', 'false');
      }),
    );

    document.addEventListener('click', (event) => {
      nav.querySelectorAll('.nav-dropdown[open]').forEach((dropdown) => {
        if (!dropdown.contains(event.target)) dropdown.removeAttribute('open');
      });
    });

    document.addEventListener('keydown', (event) => {
      if (event.key !== 'Escape') return;
      nav.querySelectorAll('.nav-dropdown[open]').forEach((dropdown) => dropdown.removeAttribute('open'));
    });
  }

  function ensureProgramStatus() {
    const hero = document.querySelector('main .hero');
    if (!hero) return;

    let grid = hero.querySelector('[data-program-status]');
    if (!grid) {
      grid = document.createElement('div');
      grid.className = 'status-grid program-status';
      grid.setAttribute('data-program-status', 'true');
      grid.setAttribute('aria-label', 'Current research status');
      hero.append(grid);
    }

    grid.innerHTML = `
      <div><strong>${PROGRAM.resultCount}</strong><span>proposition-level results</span></div>
      <div><strong>${PROGRAM.frontier}</strong><span>current theorem frontier</span></div>
      <div><strong>${PROGRAM.release}</strong><span>formal release</span></div>
      <div><strong>Open</strong><span>final physical-to-experiential bridge</span></div>`;

    let note = hero.querySelector('.program-boundary-note');
    if (!note) {
      note = document.createElement('p');
      note.className = 'program-boundary-note';
      grid.insertAdjacentElement('afterend', note);
    }
    note.innerHTML = `<strong>Scientific boundary:</strong> ${PROGRAM.boundary}`;
  }

  function normalizeBoundaryBlocks() {
    document.querySelectorAll('[data-public-boundary]').forEach((block) => {
      block.innerHTML = `
        <p class="eyebrow">Scientific boundary</p>
        <h2>What the current frontier does and does not establish</h2>
        <p>${PROGRAM.boundary}</p>`;
    });
  }

  function addBreadcrumbs() {
    const main = document.querySelector('main');
    if (!main || main.querySelector('.breadcrumbs')) return;
    const file = currentFile();
    const current = PAGES.find((page) => page.file === file);
    if (!current || current.file === 'index.html') return;

    const trail = document.createElement('nav');
    trail.className = 'breadcrumbs';
    trail.setAttribute('aria-label', 'Breadcrumb');
    trail.innerHTML = `<a href="index.html">Overview</a><span aria-hidden="true">/</span><span>${current.label}</span>`;
    main.insertBefore(trail, main.firstChild);
  }

  function addReaderTrail() {
    const main = document.querySelector('main');
    if (!main || main.querySelector('.reader-trail')) return;
    const file = currentFile();
    const index = PAGES.findIndex((page) => page.file === file);
    if (index <= 0) return;

    const previous = PAGES[index - 1];
    const next = PAGES[index + 1];
    const trail = document.createElement('section');
    trail.className = 'reader-trail';

    const nextHtml = next
      ? `<a class="trail-card next" href="${next.file}"><span>Next</span><strong>${next.label}</strong><small>Continue through the guided research path</small></a>`
      : `<a class="trail-card next" href="research-map.html"><span>Continue</span><strong>Research Map</strong><small>Return to the complete research structure</small></a>`;

    trail.innerHTML = `
      <div class="reader-trail-head">
        <p class="eyebrow">Continue reading</p>
        <h2>Follow one coherent public research path</h2>
      </div>
      <div class="reader-trail-grid">
        <a class="trail-card previous" href="${previous.file}"><span>Previous</span><strong>${previous.label}</strong><small>Move back one layer</small></a>
        <a class="trail-card map" href="research-map.html"><span>Map</span><strong>Research Map</strong><small>See all ten branches in proposition order</small></a>
        ${nextHtml}
      </div>`;
    main.append(trail);
  }

  function propositionNumber(text) {
    const match = text.match(/\bP(\d{1,2})\b/i);
    return match ? Number(match[1]) : null;
  }

  function inferredCardHref(card) {
    const direct = card.querySelector('a[href]');
    if (direct) return direct.href;

    const number = propositionNumber(card.textContent || '');
    if (number && propositionLinks[number]) return propositionLinks[number];
    if (number) return `research-map.html#p${number}`;

    const image = card.querySelector('img[src]');
    if (image) return image.src;
    return null;
  }

  function activateCard(card) {
    if (card.dataset.clickableReady === 'true') return;
    const href = inferredCardHref(card);
    if (!href) return;

    card.dataset.clickableReady = 'true';
    card.classList.add('interactive-card');
    card.tabIndex = 0;
    card.setAttribute('role', 'link');

    const go = () => {
      window.location.href = href;
    };
    card.addEventListener('click', (event) => {
      if (event.target.closest('a, button, input, select, textarea')) return;
      go();
    });
    card.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        go();
      }
    });
  }

  function activateCards() {
    document
      .querySelectorAll('.result, .flow-node, .figure-card, .card')
      .forEach(activateCard);
  }

  function addResearchAnchors() {
    if (currentFile() !== 'research-map.html') return;
    document.querySelectorAll('[data-range]').forEach((element) => {
      if (element.id) return;
      const first = (element.getAttribute('data-range') || '').match(/P(\d+)/i);
      if (first) element.id = `p${first[1]}`;
    });

    if (window.location.hash) {
      const target = document.querySelector(window.location.hash);
      if (target) requestAnimationFrame(() => target.scrollIntoView({ block: 'start' }));
    }
  }

  function addBackToTop() {
    if (document.querySelector('.back-to-top')) return;
    const link = document.createElement('a');
    link.className = 'back-to-top';
    link.href = '#top';
    link.textContent = 'Top';
    link.setAttribute('aria-label', 'Back to top');
    document.body.append(link);

    const update = () => link.classList.toggle('visible', window.scrollY > 600);
    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  function markExternalLinks() {
    document.querySelectorAll('a[href^="http"]').forEach((link) => {
      if (!link.href.startsWith(window.location.origin)) {
        link.rel = 'noopener noreferrer';
      }
    });
  }

  function normalizePublicPunctuation(root = document.body) {
    if (!root) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    const textNodes = [];
    while (walker.nextNode()) textNodes.push(walker.currentNode);
    textNodes.forEach((node) => {
      const parent = node.parentElement;
      if (parent && parent.closest('script, style, pre, code')) return;
      let text = node.nodeValue || '';
      text = text.replace(/[\u2013\u2014]/g, ', ');
      node.nodeValue = text;
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    ensureNavigation();
    ensureProgramStatus();
    normalizeBoundaryBlocks();
    addBreadcrumbs();
    addResearchAnchors();
    activateCards();
    addReaderTrail();
    addBackToTop();
    markExternalLinks();
    normalizePublicPunctuation();
  });
})();

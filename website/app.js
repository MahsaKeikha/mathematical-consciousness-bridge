(() => {
  const PAGES = [
    { file: 'index.html', label: 'Overview' },
    { file: 'plain-language.html', label: 'Plain Language' },
    { file: 'start-here.html', label: 'Start Here' },
    { file: 'observer-research.html', label: 'Research I · Observer Mathematics' },
    { file: 'research-lineage.html', label: 'Research Lineage' },
    { file: 'research-map.html', label: 'Research II · Bridge Map' },
    { file: 'measurement-science.html', label: 'Research III · Measurement Science' },
    { file: 'physics-mathematics.html', label: 'Physics & Math' },
    { file: 'visual-atlas.html', label: 'Visual Atlas' },
    { file: 'sources.html', label: 'Sources' },
  ];

  const NAV_GROUPS = [
    {
      label: 'Research',
      className: 'research-menu',
      items: [
        {
          file: 'observer-research.html',
          kicker: 'Research I',
          label: 'Observer mathematics',
          description: 'Spacetime, causal access, observer readouts, metrics, interventions, and robustness.',
        },
        {
          file: 'research-lineage.html',
          kicker: 'Scientific handoff',
          label: 'Research lineage',
          description: 'The handoff from physical observer mathematics to bridge testing and then to measurement science.',
        },
        {
          file: 'research-map.html',
          kicker: 'Research II',
          label: 'Bridge theorem map',
          description: 'The current physical-to-experiential test architecture through P100.',
        },
        {
          file: 'measurement-science.html',
          kicker: 'Research III',
          label: 'Consciousness measurement science',
          description: 'Multimodal inference, causal tests, phenomenal structure, calibration, and explicit uncertainty.',
        },
        {
          file: 'physics-mathematics.html',
          kicker: 'Foundations',
          label: 'Physics & mathematics',
          description: 'The physical, information-theoretic, statistical, and quantum foundations used by Research II.',
        },
      ],
    },
    {
      label: 'Explore',
      className: 'explore-menu',
      items: [
        {
          file: 'visual-atlas.html',
          kicker: 'Figures',
          label: 'Visual atlas',
          description: 'Browse the theorem figures and computational visual record.',
        },
        {
          file: 'sources.html',
          kicker: 'Provenance',
          label: 'Sources',
          description: 'Follow equations, references, provenance records, and citation boundaries.',
        },
      ],
    },
  ];

  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';
  const OBSERVER_REPO = 'https://github.com/MahsaKeikha/spatiotemporal-observer-math';
  const MEASUREMENT_REPO = 'https://github.com/MahsaKeikha/consciousness-measurement-science';

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

  function createDropdown(group, current) {
    const details = document.createElement('details');
    details.className = `nav-dropdown ${group.className}`;
    if (group.items.some((item) => item.file === current)) {
      details.classList.add('contains-current');
    }

    const summary = document.createElement('summary');
    summary.className = 'nav-dropbtn';
    summary.textContent = group.label;
    summary.setAttribute('aria-label', `${group.label} navigation`);
    details.append(summary);

    const menu = document.createElement('div');
    menu.className = 'nav-dropdown-menu';
    group.items.forEach((item) => {
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
    NAV_GROUPS.forEach((group) => nav.append(createDropdown(group, file)));

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

  function addBreadcrumbs() {
    const main = document.querySelector('main');
    if (!main || main.querySelector('.breadcrumbs')) return;
    const file = currentFile();
    const current = PAGES.find((page) => page.file === file) || PAGES[0];
    if (current.file === 'index.html') return;

    const trail = document.createElement('nav');
    trail.className = 'breadcrumbs';
    trail.setAttribute('aria-label', 'Breadcrumb');
    trail.innerHTML = `<a href="index.html">Overview</a><span aria-hidden="true">/</span><span>${current.label}</span>`;
    main.insertBefore(trail, main.firstChild);
  }

  function addLineageCallout() {
    const file = currentFile();
    if (!['index.html', 'start-here.html', 'research-map.html'].includes(file)) return;
    const main = document.querySelector('main');
    const hero = main?.querySelector('.hero');
    if (!main || !hero || main.querySelector('.lineage-callout')) return;

    const section = document.createElement('section');
    section.className = 'lineage-callout';
    section.innerHTML = `
      <div class="lineage-callout-copy">
        <p class="eyebrow">Three connected research stages</p>
        <h2>From physical observer identification to bridge tests to consciousness measurement</h2>
        <p><strong>Research I: Spatiotemporal Observer Mathematics</strong> identifies and tests the physical observer subsystem. <strong>Research II: Mathematical Consciousness Bridge</strong> asks what a physical-to-experiential claim must survive before it is scientifically defensible. <strong>Research III: Consciousness Measurement Science</strong> then asks what can actually be identified, bounded, predicted, or falsified about experiential targets from multimodal evidence under explicit assumptions.</p>
      </div>
      <div class="lineage-callout-actions">
        <a class="lineage-mini-card" href="observer-research.html"><span>Research I</span><strong>Spatiotemporal Observer Mathematics</strong><small>Physical observer architecture →</small></a>
        <a class="lineage-mini-card" href="research-map.html"><span>Research II</span><strong>Mathematical Consciousness Bridge</strong><small>Bridge-test program through P100 →</small></a>
        <a class="lineage-mini-card current" href="measurement-science.html"><span>Research III</span><strong>Consciousness Measurement Science</strong><small>Multimodal measurement program →</small></a>
        <a class="lineage-mini-card" href="research-lineage.html"><span>Research lineage</span><strong>See the full scientific handoff</strong><small>What carries forward and what remains open →</small></a>
      </div>`;
    hero.insertAdjacentElement('afterend', section);
  }

  function addReaderTrail() {
    const main = document.querySelector('main');
    if (!main || main.querySelector('.reader-trail')) return;
    const file = currentFile();
    const index = PAGES.findIndex((page) => page.file === file);
    if (index < 0) return;

    const trail = document.createElement('section');
    trail.className = 'reader-trail';
    const previous = PAGES[index - 1];
    const next = PAGES[index + 1];

    const previousHtml = previous
      ? `<a class="trail-card previous" href="${previous.file}"><span>Previous</span><strong>${previous.label}</strong><small>Move back in the guided reading path</small></a>`
      : `<a class="trail-card previous" href="${OBSERVER_REPO}"><span>Research I</span><strong>Observer Mathematics</strong><small>See the physical-subsystem foundation</small></a>`;
    const nextHtml = next
      ? `<a class="trail-card next" href="${next.file}"><span>Next</span><strong>${next.label}</strong><small>Continue through the guided research path</small></a>`
      : `<a class="trail-card next" href="${MEASUREMENT_REPO}"><span>Research III</span><strong>Measurement Science Repository</strong><small>Continue into the experimental measurement program</small></a>`;

    trail.innerHTML = `
      <div class="reader-trail-head">
        <p class="eyebrow">Continue reading</p>
        <h2>Follow the research without losing your place</h2>
      </div>
      <div class="reader-trail-grid">
        ${previousHtml}
        <a class="trail-card map" href="research-lineage.html"><span>Lineage</span><strong>Research I → II → III</strong><small>See the full handoff from observer physics to bridge tests to measurement science</small></a>
        ${nextHtml}
      </div>`;
    main.append(trail);
  }

  function addResearchTwoVisuals() {
    if (currentFile() !== 'index.html') return;

    const overview = document.querySelector('#research-ii-overview');
    const overviewHead = overview?.querySelector('.section-head');
    if (overview && overviewHead && !overview.querySelector('.research-ii-figure-card')) {
      const figure = document.createElement('div');
      figure.className = 'figure-card research-ii-figure-card';
      figure.innerHTML = `
        <a href="research-ii-sufficiency-falsification-overview.svg" aria-label="Open the full Research II sufficiency and falsification architecture figure">
          <img loading="lazy" decoding="async" src="research-ii-sufficiency-falsification-overview.svg" alt="Research II testing architecture showing a declared physical or computational descriptor, an independently defined target, descriptor-equivalent cases, and falsification when the target distinguishes cases the declared description treats as equivalent" />
        </a>
        <div>
          <p class="eyebrow">Research II testing architecture</p>
          <h3>Declare the description → define the target independently → compare equivalent cases → try to falsify sufficiency</h3>
          <p>Research II reformulates a broad bridge claim as a falsification problem. A theory must first declare the physical or computational description it claims is sufficient. The target is then defined through an independent measurement route, so the answer is not built into the test itself.</p>
          <p>The framework then compares cases that are equivalent under the declared description. If the independently defined target still distinguishes those cases in a way the model forbids, the sufficiency claim is rejected for that descriptor. If no such separation is found, the descriptor remains compatible with the current evidence, but it is not thereby confirmed as the true theory.</p>
          <p><a href="research-map.html">Open the complete Research II testing map →</a></p>
        </div>`;
      overviewHead.insertAdjacentElement('afterend', figure);
    }

    const frontier = document.querySelector('#p100-frontier');
    const frontierHead = frontier?.querySelector('.section-head');
    if (frontier && frontierHead && !frontier.querySelector('.p100-figure-card')) {
      const figure = document.createElement('div');
      figure.className = 'figure-card p100-figure-card';
      figure.innerHTML = `
        <a href="p100-anytime-valid-sequence-overview.svg" aria-label="Open the plain-language P100 anytime-valid sequence overview">
          <img loading="lazy" decoding="async" src="p100-anytime-valid-sequence-overview.svg" alt="P100 diagram showing past information, a frozen next-round plan, fresh certification data, a valid e-value, a predictable stake, multiplicative evidence accumulation, and anytime-valid threshold crossing" />
        </a>
        <div>
          <p class="eyebrow">P100 sequential evidence architecture</p>
          <h3>Past information → freeze the next-round plan → collect fresh certification data → accumulate valid evidence → stop at the first justified crossing</h3>
          <p>P100 extends the Research II testing program from a single protected certification round to a sequence of fresh rounds. The next plan may adapt to past results, but current certification data cannot be used to choose their own calibration, selection rule, or stake.</p>
          <p>Under those conditions, evidence can be accumulated across rounds and inspected after every update. A threshold crossing then remains anytime-valid rather than being invalidated by repeated looks.</p>
          <p><a href="visual-atlas.html">Open the full technical P100 figure in the Visual Atlas →</a></p>
        </div>`;
      frontierHead.insertAdjacentElement('afterend', figure);
    }
  }

  function propositionMentions(text) {
    return Array.from(String(text || '').matchAll(/\bP(\d{1,3})\b/gi), (match) => Number(match[1]));
  }

  function propositionNumber(text) {
    const mentions = propositionMentions(text);
    return mentions.length ? mentions[0] : null;
  }

  function hasAmbiguousPropositionText(text) {
    const value = String(text || '');
    if (/\bP\d{1,3}\s*-\s*P?\d{1,3}\b/i.test(value)) return true;
    return new Set(propositionMentions(value)).size > 1;
  }

  function inferredCardHref(card) {
    const direct = card.querySelector('a[href]');
    if (direct) return direct.href;

    const text = card.textContent || '';
    if (hasAmbiguousPropositionText(text)) return null;

    const number = propositionNumber(text);
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
    document.querySelectorAll('section').forEach((section) => {
      if (section.id) return;
      const text = section.textContent || '';
      if (hasAmbiguousPropositionText(text)) return;
      const number = propositionNumber(text);
      if (number) section.id = `p${number}`;
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

  function loadScientificOrientation() {
    if (!document.querySelector('link[data-scientific-orientation]')) {
      const stylesheet = document.createElement('link');
      stylesheet.rel = 'stylesheet';
      stylesheet.href = 'research-orientation.css';
      stylesheet.dataset.scientificOrientation = 'style';
      document.head.append(stylesheet);
    }

    if (!document.querySelector('script[data-scientific-orientation]')) {
      const script = document.createElement('script');
      script.src = 'research-orientation.js';
      script.dataset.scientificOrientation = 'script';
      document.head.append(script);
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    ensureNavigation();
    loadScientificOrientation();
    addBreadcrumbs();
    addLineageCallout();
    addResearchAnchors();
    addResearchTwoVisuals();
    activateCards();
    addReaderTrail();
    addBackToTop();
    markExternalLinks();
  });
})();

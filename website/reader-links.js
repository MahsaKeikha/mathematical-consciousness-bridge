(() => {
  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';

  const PROPOSITION_DOC_SLUGS = [
    'representation_invariance',
    'bridge_identifiability',
    'bridge_equivalence_classes',
    'discriminating_experiment_design',
    'feature_sufficiency',
    'canonical_bridge_signature',
    'experimental_signature_recovery',
    'robust_signature_recovery',
    'categorical_sample_complexity',
    'robust_experiment_design',
    'intervention_resolved_causal_structure',
    'component_insufficiency',
    'pairwise_component_irredundancy',
    'temporal_continuation',
    'finite_sample_temporal_certification',
    'independent_composition_and_coupling',
    'coarse_graining_and_refinement',
    'scale_sufficiency_certification',
    'fundamental_physical_sufficiency',
    'finite_sample_residual_certification',
    'descriptor_refinement_residual_persistence',
    'simultaneous_refinement_chain_certification',
    'adaptive_descriptor_selection_certification',
    'anytime_adaptive_refinement_certification',
    'directed_influence_scale_certification',
    'partition_irreducibility_scale_certification',
    'partition_lattice_node_aggregation',
    'intervention_node_aggregation_compatibility',
    'response_geometry_node_aggregation',
    'full_p11_scale_compatibility',
    'intervention_quotient_compatibility',
    'delay_quotient_compatibility',
    'joint_operational_quotient',
    'joint_p11_operational_scale',
    'approximate_directed_influence_operational_quotient',
    'partition_irreducibility_operational_quotient',
    'complete_approximate_p11_operational_scale',
    'quantum_operational_sufficiency',
    'finite_data_quantum_nonfactorization',
    'continuous_quantum_region_regularity',
    'trace_ball_quantum_envelope',
    'quantum_regular_bridge_sample_complexity',
    'optimal_quantum_target_allocation',
    'pair_adaptive_sample_allocation',
    'shared_preparation_graph_allocation',
    'budget_constrained_witness_graph',
    'anytime_sequential_witness_graph',
    'gap_dependent_stopping_complexity',
    'dyadic_stopping_overhead',
    'bounded_starvation_asynchronous_sampling',
    'heterogeneous_service_rate_stopping',
    'capacity_optimal_service_allocation',
    'residual_demand_reoptimization',
    'metric_switching_cost_residual_scheduling',
    'pruning_aware_switching_monotonicity',
    'moving_start_metric_reoptimization_stability',
    'switching_metric_perturbation',
    'finite_data_metric_uncertainty',
    'optimal_transition_calibration',
    'integer_transition_calibration',
    'exact_integer_transition_calibration',
    'heterogeneous_cost_transition_calibration',
    'exact_heterogeneous_integer_calibration',
    'fast_heterogeneous_integer_approximation',
    'lower_bounded_heterogeneous_calibration',
    'residual_exact_calibration_augmentation',
    'global_integer_optimality_certificate',
    'lagrangian_optimality_gap',
    'dual_optimal_multiplier',
    'primal_dual_gap_decomposition',
    'target_provenance_noncircularity',
    'target_measurement_channel_robustness',
    'target_channel_identifiability',
    'finite_sample_target_channel_recovery',
    'target_model_adequacy_overidentification',
    'finite_sample_target_model_adequacy',
    'full_law_model_set_separation',
    'certified_continuous_model_separation',
    'certified_sampling_radius',
    'simplex_coupled_model_separation',
    'projection_event_model_separation',
    'exact_nested_projection_contrast',
    'exact_projection_parity',
    'exact_projection_parity_contrast',
    'exact_triple_projection_parity_functional',
    'exact_minimally_weighted_quad_projection_parity_functional',
    'exact_bounded_primitive_quad_projection_parity_functional',
    'exact_radius_three_bounded_primitive_quad_projection_parity_functional',
    'complete_linear_parity_duality',
    'exact_nonlinear_rank_one_separation',
    'mixed_prevalence_rank_two_flattening_separation',
    'exact_global_mixed_prevalence_distance',
    'localized_sign_coherence_rejection',
    'finite_range_dependent_sign_coherence',
    'drift_aware_stratified_sign_coherence',
    'selection_valid_holdout_stratification',
    'simultaneous_candidate_family_selection',
    'cross_fitted_selection_valid_certification',
    'cross_fitted_evalue_aggregation',
    'anytime_sequential_eprocess',
  ];

  const ATLAS_DOMAINS = [
    {
      id: 'foundations',
      label: 'Foundations',
      range: 'P1-P10',
      min: 1,
      max: 10,
      description:
        'Define invariance, identifiability, equivalence, recovery, finite-data uncertainty, and falsifiable experiment design.',
    },
    {
      id: 'physical-structure',
      label: 'Structured physical descriptions',
      range: 'P11-P18',
      min: 11,
      max: 18,
      description:
        'Track causal, temporal, compositional, and multiscale physical structure before any experiential interpretation is introduced.',
    },
    {
      id: 'bridge-sufficiency',
      label: 'Bridge sufficiency',
      range: 'P19-P24',
      min: 19,
      max: 24,
      description:
        'Test whether the declared physical descriptor screens off an independently specified target, with finite-data and repeated-look validity.',
    },
    {
      id: 'operational-scale',
      label: 'Operational scale',
      range: 'P25-P37',
      min: 25,
      max: 37,
      description:
        'Ask which physical distinctions survive quotienting, coarse-graining, aggregation, and approximate changes of operational scale.',
    },
    {
      id: 'quantum-interface',
      label: 'Quantum operational interface',
      range: 'P38-P44',
      min: 38,
      max: 44,
      description:
        'Separate consequences of quantum operational descriptions from claims that require an additional bridge hypothesis.',
    },
    {
      id: 'adaptive-evidence',
      label: 'Adaptive evidence acquisition',
      range: 'P45-P53',
      min: 45,
      max: 53,
      description:
        'Allocate measurements while protecting inference under adaptive selection, repeated looks, stopping rules, and service constraints.',
    },
    {
      id: 'calibration',
      label: 'Execution, scheduling, and calibration',
      range: 'P54-P70',
      min: 54,
      max: 70,
      description:
        'Control switching costs, transition uncertainty, heterogeneous calibration, integer allocation, and primal-dual optimality.',
    },
    {
      id: 'target-audit',
      label: 'Target measurement and model audit',
      range: 'P71-P100',
      min: 71,
      max: 100,
      description:
        'Return to the P19 bridge lineage: protect target provenance, recover the observation channel, test adequacy, and build increasingly strong certified rejection results.',
    },
  ];

  const RESEARCH_SPINE = [
    { file: 'start-here.html', short: 'Start', label: 'Start Here', note: 'Question and boundaries' },
    { file: 'observer-research.html', short: 'I', label: 'Research I', note: 'Observer mathematics' },
    { file: 'research-lineage.html', short: 'Handoff', label: 'Lineage', note: 'Scientific dependency' },
    { file: 'research-map.html', short: 'II', label: 'Research II', note: 'Bridge theorem map' },
    { file: 'measurement-science.html', short: 'III', label: 'Research III', note: 'Measurement science' },
    { file: 'visual-atlas.html', short: 'Figures', label: 'Visual Atlas', note: 'Visual evidence' },
    { file: 'sources.html', short: 'Audit', label: 'Sources', note: 'Provenance and tests' },
  ];

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

  function currentFile() {
    const file = window.location.pathname.split('/').pop();
    return file || 'index.html';
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
            href: `${REPO}/blob/main/docs/proposition_74_finite_sample_target_channel_recovery.md`,
          },
          {
            number: 75,
            title: 'Target-model adequacy and four-view overidentification',
            description:
              'Separate identifiability from adequacy: a fourth binary view introduces observable restrictions that can falsify the declared conditional-independence target model.',
            href: `${REPO}/blob/main/docs/proposition_75_target_model_adequacy_overidentification.md`,
          },
          {
            number: 76,
            title: 'Finite-sample target-model adequacy rejection',
            description:
              'Reject only when finite IID uncertainty leaves a necessary P75 restriction separated from zero. Nonrejection remains nonacceptance.',
            href: `${REPO}/blob/main/docs/proposition_76_finite_sample_target_model_adequacy.md`,
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

  function titleFromPropositionSlug(slug) {
    const replacements = new Map([
      ['p11', 'P11'],
      ['iid', 'IID'],
      ['evalue', 'e-value'],
      ['eprocess', 'e-process'],
    ]);
    return slug
      .split('_')
      .map((word) => replacements.get(word) || word)
      .join(' ')
      .replace(/^./, (character) => character.toUpperCase());
  }

  function atlasDomainFor(number) {
    return ATLAS_DOMAINS.find((domain) => number >= domain.min && number <= domain.max);
  }

  function propositionHref(number, slug) {
    return `${REPO}/blob/main/docs/proposition_${number}_${slug}.md`;
  }

  function addResearchGuideStyles() {
    if (document.getElementById('research-guide-styles')) return;
    const style = document.createElement('style');
    style.id = 'research-guide-styles';
    style.textContent = `
      .research-spine {
        max-width: var(--max, 1180px);
        margin: 18px auto 6px;
        padding: 0 24px;
      }
      .research-spine-shell {
        overflow-x: auto;
        padding: 8px;
        border: 1px solid var(--line, #d8dee9);
        border-radius: 18px;
        background: linear-gradient(180deg, #ffffff 0%, #f8faff 100%);
        box-shadow: 0 12px 34px rgba(15, 23, 42, 0.06);
        scrollbar-width: thin;
      }
      .research-spine-list {
        display: grid;
        grid-template-columns: repeat(7, minmax(132px, 1fr));
        gap: 7px;
        min-width: 980px;
      }
      .research-spine-step {
        display: grid;
        grid-template-columns: 30px 1fr;
        gap: 9px;
        align-items: center;
        min-width: 0;
        padding: 10px 11px;
        border-radius: 12px;
        color: var(--ink, #111827);
        text-decoration: none !important;
        transition: background-color 150ms ease, box-shadow 150ms ease, transform 150ms ease;
      }
      .research-spine-step:hover,
      .research-spine-step:focus-visible {
        background: #eef3ff;
        box-shadow: inset 0 0 0 1px #c7d2fe;
        transform: translateY(-1px);
        outline: none;
      }
      .research-spine-step[aria-current='page'] {
        background: #e8eefc;
        box-shadow: inset 0 0 0 1px #9fb0da;
      }
      .research-spine-index {
        display: grid;
        place-items: center;
        width: 30px;
        height: 30px;
        border-radius: 10px;
        background: #172554;
        color: white;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.02em;
      }
      .research-spine-step strong,
      .research-spine-step small {
        display: block;
        min-width: 0;
      }
      .research-spine-step strong {
        font-size: 0.84rem;
        line-height: 1.2;
      }
      .research-spine-step small {
        margin-top: 3px;
        color: var(--muted, #5d6675);
        font-size: 0.68rem;
        line-height: 1.25;
      }
      .proposition-atlas {
        margin-top: 34px;
        padding: clamp(24px, 4vw, 46px);
        border: 1px solid var(--line, #d8dee9);
        border-radius: 22px;
        background: linear-gradient(180deg, #fbfcff 0%, #ffffff 38%);
        box-shadow: 0 18px 46px rgba(15, 23, 42, 0.07);
      }
      .proposition-atlas-intro {
        display: grid;
        grid-template-columns: minmax(0, 1.35fr) minmax(260px, 0.65fr);
        gap: 28px;
        align-items: end;
      }
      .proposition-atlas-intro h2 {
        margin-bottom: 10px;
      }
      .proposition-atlas-intro p {
        max-width: 76ch;
      }
      .atlas-summary {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 10px;
      }
      .atlas-summary div {
        padding: 14px;
        border: 1px solid #dbe3f1;
        border-radius: 13px;
        background: white;
      }
      .atlas-summary strong,
      .atlas-summary span {
        display: block;
      }
      .atlas-summary strong {
        font-size: 1.35rem;
        color: #172554;
      }
      .atlas-summary span {
        margin-top: 3px;
        color: var(--muted, #5d6675);
        font-size: 0.74rem;
      }
      .atlas-controls {
        display: grid;
        grid-template-columns: minmax(240px, 1fr) minmax(210px, 0.42fr) auto;
        gap: 10px;
        align-items: center;
        margin: 24px 0 15px;
        padding: 14px;
        border: 1px solid #dde4ef;
        border-radius: 15px;
        background: #f7f9fd;
      }
      .atlas-controls label {
        position: absolute;
        width: 1px;
        height: 1px;
        overflow: hidden;
        clip: rect(0 0 0 0);
        white-space: nowrap;
      }
      .atlas-controls input,
      .atlas-controls select {
        width: 100%;
        min-height: 44px;
        padding: 9px 12px;
        border: 1px solid #c9d3e4;
        border-radius: 10px;
        background: white;
        color: var(--ink, #111827);
        font: inherit;
      }
      .atlas-controls input:focus,
      .atlas-controls select:focus {
        outline: 2px solid #9fb0da;
        outline-offset: 2px;
      }
      .atlas-count {
        min-width: 120px;
        color: #334155;
        font-size: 0.82rem;
        font-weight: 700;
        text-align: right;
      }
      .atlas-jumps {
        display: flex;
        gap: 7px;
        overflow-x: auto;
        margin: 0 0 26px;
        padding: 3px 1px 9px;
        scrollbar-width: thin;
      }
      .atlas-jumps a {
        flex: 0 0 auto;
        padding: 7px 10px;
        border: 1px solid #d8e0ec;
        border-radius: 999px;
        background: white;
        color: #334155;
        font-size: 0.74rem;
        font-weight: 700;
        text-decoration: none !important;
      }
      .atlas-jumps a:hover,
      .atlas-jumps a:focus-visible {
        border-color: #9fb0da;
        background: #eef3ff;
        outline: none;
      }
      .atlas-group {
        scroll-margin-top: 110px;
        margin-top: 32px;
      }
      .atlas-group[hidden] {
        display: none;
      }
      .atlas-group-head {
        display: grid;
        grid-template-columns: minmax(0, 1fr) auto;
        gap: 18px;
        align-items: start;
        margin-bottom: 14px;
        padding-bottom: 13px;
        border-bottom: 1px solid #dfe5ef;
      }
      .atlas-group-head h3 {
        margin: 0;
        font-size: clamp(1.1rem, 1.8vw, 1.38rem);
      }
      .atlas-group-head p {
        max-width: 78ch;
        margin: 6px 0 0;
      }
      .atlas-range {
        padding: 6px 9px;
        border-radius: 999px;
        background: #172554;
        color: white;
        font-size: 0.72rem;
        font-weight: 800;
        white-space: nowrap;
      }
      .proposition-atlas-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 11px;
      }
      .proposition-atlas-card {
        position: relative;
        display: flex;
        min-height: 178px;
        flex-direction: column;
        padding: 15px 15px 14px;
        border: 1px solid #dce3ed;
        border-radius: 14px;
        background: white;
        color: var(--ink, #111827);
        text-decoration: none !important;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.035);
        transition: transform 150ms ease, border-color 150ms ease, box-shadow 150ms ease;
      }
      .proposition-atlas-card:hover,
      .proposition-atlas-card:focus-visible {
        transform: translateY(-3px);
        border-color: #8fa3cf;
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.1);
        outline: none;
      }
      .proposition-atlas-card[hidden] {
        display: none;
      }
      .atlas-card-top {
        display: flex;
        gap: 8px;
        align-items: center;
        justify-content: space-between;
      }
      .atlas-proposition-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 42px;
        height: 28px;
        padding: 0 8px;
        border-radius: 9px;
        background: #e8eefc;
        color: #172554;
        font-size: 0.75rem;
        font-weight: 850;
      }
      .atlas-domain-label {
        color: #64748b;
        font-size: 0.64rem;
        font-weight: 700;
        line-height: 1.2;
        text-align: right;
      }
      .proposition-atlas-card h4 {
        margin: 14px 0 8px;
        font-size: 0.93rem;
        line-height: 1.34;
      }
      .proposition-atlas-card p {
        margin: 0;
        color: #64748b;
        font-size: 0.72rem;
        line-height: 1.42;
      }
      .atlas-open {
        margin-top: auto;
        padding-top: 13px;
        color: #1e3a8a;
        font-size: 0.72rem;
        font-weight: 800;
      }
      .atlas-branch-note {
        margin-top: 26px;
        padding: 15px 17px;
        border-left: 3px solid #7890c4;
        border-radius: 0 12px 12px 0;
        background: #f3f6fc;
        color: #334155;
        font-size: 0.84rem;
        line-height: 1.55;
      }
      @media (max-width: 1000px) {
        .proposition-atlas-grid {
          grid-template-columns: repeat(3, minmax(0, 1fr));
        }
        .proposition-atlas-intro {
          grid-template-columns: 1fr;
        }
      }
      @media (max-width: 760px) {
        .research-spine {
          margin-top: 10px;
          padding: 0 14px;
        }
        .proposition-atlas {
          padding: 21px 15px;
          border-radius: 17px;
        }
        .atlas-controls {
          grid-template-columns: 1fr;
        }
        .atlas-count {
          text-align: left;
        }
        .proposition-atlas-grid {
          grid-template-columns: repeat(2, minmax(0, 1fr));
        }
        .atlas-group-head {
          grid-template-columns: 1fr;
        }
        .atlas-range {
          width: fit-content;
        }
      }
      @media (max-width: 480px) {
        .proposition-atlas-grid {
          grid-template-columns: 1fr;
        }
        .proposition-atlas-card {
          min-height: 150px;
        }
      }
    `;
    document.head.append(style);
  }

  function addResearchSpine() {
    const file = currentFile();
    const eligible = new Set([
      'index.html',
      'plain-language.html',
      'start-here.html',
      'observer-research.html',
      'research-lineage.html',
      'research-map.html',
      'measurement-science.html',
      'physics-mathematics.html',
      'visual-atlas.html',
      'sources.html',
    ]);
    if (!eligible.has(file)) return;
    const main = document.querySelector('main');
    if (!main || main.querySelector('.research-spine')) return;

    const spine = document.createElement('nav');
    spine.className = 'research-spine';
    spine.setAttribute('aria-label', 'Guided research path');
    const list = document.createElement('div');
    list.className = 'research-spine-list';

    RESEARCH_SPINE.forEach((step) => {
      const link = document.createElement('a');
      link.className = 'research-spine-step';
      link.href = step.file;
      if (step.file === file) link.setAttribute('aria-current', 'page');
      link.innerHTML = `<span class="research-spine-index">${step.short}</span><span><strong>${step.label}</strong><small>${step.note}</small></span>`;
      list.append(link);
    });

    const shell = document.createElement('div');
    shell.className = 'research-spine-shell';
    shell.append(list);
    spine.append(shell);

    const hero = main.querySelector('.hero');
    if (hero) main.insertBefore(spine, hero);
    else main.insertBefore(spine, main.firstChild);
  }

  function addPropositionAtlas() {
    if (currentFile() !== 'research-map.html') return;
    const orientation = document.querySelector('#orientation');
    if (!orientation || document.getElementById('proposition-atlas')) return;

    const atlas = document.createElement('section');
    atlas.className = 'proposition-atlas';
    atlas.id = 'proposition-atlas';
    atlas.innerHTML = `
      <div class="proposition-atlas-intro">
        <div>
          <p class="eyebrow">Canonical proposition atlas</p>
          <h2>P1-P100 in one visual, searchable index</h2>
          <p>This is the fastest way to follow Research II without hunting through the repository. Every card opens the canonical proposition record. Results are grouped by scientific role, while proposition numbers preserve development order.</p>
          <p class="atlas-branch-note"><strong>Dependency note:</strong> P71-P100 returns to the bridge-sufficiency lineage after the separate P54-P70 scheduling and calibration branch. A larger proposition number does not automatically mean that every earlier proposition is a prerequisite.</p>
        </div>
        <div class="atlas-summary" aria-label="Proposition atlas summary">
          <div><strong>100</strong><span>individual proposition records</span></div>
          <div><strong>8</strong><span>scientific domains</span></div>
          <div><strong>P100</strong><span>current theorem frontier</span></div>
          <div><strong>Open</strong><span>physical-to-experiential bridge</span></div>
        </div>
      </div>
      <div class="atlas-controls">
        <label for="atlas-search">Search propositions</label>
        <input id="atlas-search" type="search" placeholder="Search P-number or topic, e.g. P19, quantum, calibration" autocomplete="off" />
        <label for="atlas-domain-filter">Filter scientific domain</label>
        <select id="atlas-domain-filter"><option value="all">All scientific domains</option></select>
        <span class="atlas-count" aria-live="polite">100 of 100 results</span>
      </div>
      <nav class="atlas-jumps" aria-label="Jump to proposition domain"></nav>
      <div class="atlas-groups"></div>`;

    const filter = atlas.querySelector('#atlas-domain-filter');
    const jumps = atlas.querySelector('.atlas-jumps');
    const groups = atlas.querySelector('.atlas-groups');

    ATLAS_DOMAINS.forEach((domain) => {
      const option = document.createElement('option');
      option.value = domain.id;
      option.textContent = `${domain.range}: ${domain.label}`;
      filter.append(option);

      const jump = document.createElement('a');
      jump.href = `#atlas-${domain.id}`;
      jump.textContent = domain.range;
      jump.title = domain.label;
      jumps.append(jump);

      const group = document.createElement('section');
      group.className = 'atlas-group';
      group.id = `atlas-${domain.id}`;
      group.dataset.domain = domain.id;
      group.innerHTML = `
        <div class="atlas-group-head">
          <div><h3>${domain.label}</h3><p>${domain.description}</p></div>
          <span class="atlas-range">${domain.range}</span>
        </div>
        <div class="proposition-atlas-grid"></div>`;
      groups.append(group);
    });

    PROPOSITION_DOC_SLUGS.forEach((slug, index) => {
      const number = index + 1;
      const domain = atlasDomainFor(number);
      const grid = atlas.querySelector(`#atlas-${domain.id} .proposition-atlas-grid`);
      const title = titleFromPropositionSlug(slug);
      const link = document.createElement('a');
      link.className = 'proposition-atlas-card';
      link.href = propositionHref(number, slug);
      link.dataset.number = String(number);
      link.dataset.domain = domain.id;
      link.dataset.search = `p${number} ${title} ${domain.label}`.toLowerCase();
      link.setAttribute('aria-label', `P${number}: ${title}. Open canonical proposition record.`);
      link.innerHTML = `
        <span class="atlas-card-top"><span class="atlas-proposition-number">P${number}</span><span class="atlas-domain-label">${domain.label}</span></span>
        <h4>${title}</h4>
        <p>Canonical proposition record</p>
        <span class="atlas-open">Open proof record →</span>`;
      grid.append(link);
    });

    const update = () => {
      const query = atlas.querySelector('#atlas-search').value.trim().toLowerCase();
      const selectedDomain = filter.value;
      let visible = 0;

      atlas.querySelectorAll('.proposition-atlas-card').forEach((card) => {
        const matchesDomain = selectedDomain === 'all' || card.dataset.domain === selectedDomain;
        const matchesQuery = !query || card.dataset.search.includes(query);
        const show = matchesDomain && matchesQuery;
        card.hidden = !show;
        if (show) visible += 1;
      });

      atlas.querySelectorAll('.atlas-group').forEach((group) => {
        const hasVisibleCard = Array.from(group.querySelectorAll('.proposition-atlas-card')).some(
          (card) => !card.hidden,
        );
        group.hidden = !hasVisibleCard;
      });

      atlas.querySelector('.atlas-count').textContent = `${visible} of ${PROPOSITION_DOC_SLUGS.length} results`;
    };

    atlas.querySelector('#atlas-search').addEventListener('input', update);
    filter.addEventListener('change', update);
    orientation.insertAdjacentElement('afterend', atlas);
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
    addResearchGuideStyles();
    addResearchSpine();
    addPropositionAtlas();
    wireAllResultCards();
    addResearchOverviewDiagramStyles();
  });
})();
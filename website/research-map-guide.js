(() => {
  const REPO = 'https://github.com/MahsaKeikha/mathematical-consciousness-bridge';

  const MILESTONES = [
    {
      number: 1,
      title: 'Representation invariance',
      role: 'Define what must not change under physically irrelevant redescription.',
      slug: 'representation_invariance',
    },
    {
      number: 11,
      title: 'Intervention-resolved causal structure',
      role: 'Move from passive state description to controlled physical response structure.',
      slug: 'intervention_resolved_causal_structure',
    },
    {
      number: 19,
      title: 'Fundamental physical sufficiency',
      role: 'State the core factorization test for whether a declared physical descriptor is sufficient for an independently specified target.',
      slug: 'fundamental_physical_sufficiency',
    },
    {
      number: 38,
      title: 'Quantum operational sufficiency',
      role: 'Apply the same bridge discipline to a declared finite-dimensional quantum operational description without identifying the target with consciousness.',
      slug: 'quantum_operational_sufficiency',
    },
    {
      number: 71,
      title: 'Target-provenance non-circularity',
      role: 'Require the target construction to remain independent enough that a successful bridge test is not guaranteed by definition.',
      slug: 'target_provenance_noncircularity',
    },
    {
      number: 75,
      title: 'Target-model adequacy and overidentification',
      role: 'Introduce observable restrictions that let the declared latent target model itself be challenged by data.',
      slug: 'target_model_adequacy_overidentification',
    },
    {
      number: 92,
      title: 'Exact global mixed-prevalence distance',
      role: 'Close the published mixed-prevalence separation bracket with an exact model-distance result for the declared witness.',
      slug: 'exact_global_mixed_prevalence_distance',
    },
    {
      number: 100,
      title: 'Anytime-valid sequential e-process',
      role: 'Accumulate evidence across fresh certification rounds while protecting repeated inspection and data-dependent stopping under the declared conditions.',
      slug: 'anytime_sequential_eprocess',
    },
  ];

  function canonicalHref(item) {
    return `${REPO}/blob/main/docs/proposition_${item.number}_${item.slug}.md`;
  }

  function addGuideStyles() {
    if (document.querySelector('#research-map-guide-styles')) return;
    const style = document.createElement('style');
    style.id = 'research-map-guide-styles';
    style.textContent = `
      .milestone-reading-path {
        margin: 34px 0 42px;
        padding: clamp(22px, 3vw, 34px);
        border: 1px solid rgba(73, 103, 153, 0.2);
        border-radius: 24px;
        background: linear-gradient(145deg, rgba(255,255,255,0.98), rgba(244,248,255,0.96));
        box-shadow: 0 18px 48px rgba(35, 55, 90, 0.08);
      }
      .milestone-reading-path .section-head {
        margin-bottom: 20px;
      }
      .milestone-guide-note {
        max-width: 78ch;
        margin: 0;
      }
      .milestone-guide-grid {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 14px;
        margin-top: 22px;
      }
      .milestone-guide-card {
        display: flex;
        min-height: 210px;
        flex-direction: column;
        gap: 10px;
        padding: 20px;
        border: 1px solid rgba(74, 105, 156, 0.2);
        border-radius: 18px;
        background: #fff;
        color: inherit;
        text-decoration: none;
        transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
      }
      .milestone-guide-card:hover,
      .milestone-guide-card:focus-visible {
        transform: translateY(-3px);
        border-color: rgba(45, 85, 150, 0.5);
        box-shadow: 0 14px 30px rgba(35, 55, 90, 0.11);
        outline: none;
      }
      .milestone-guide-number {
        align-self: flex-start;
        padding: 5px 9px;
        border-radius: 999px;
        background: rgba(54, 95, 162, 0.09);
        color: #2f5a9d;
        font-weight: 800;
        letter-spacing: 0.04em;
      }
      .milestone-guide-card strong {
        font-size: 1.02rem;
        line-height: 1.3;
      }
      .milestone-guide-card p {
        margin: 0;
        color: var(--muted, #596474);
        line-height: 1.55;
      }
      .milestone-guide-open {
        margin-top: auto;
        color: #315f9f;
        font-weight: 750;
      }
      .atlas-legend {
        display: grid;
        grid-template-columns: repeat(5, minmax(0, 1fr));
        gap: 10px;
        margin-top: 18px;
      }
      .atlas-legend div {
        padding: 12px 14px;
        border-radius: 13px;
        background: rgba(63, 94, 147, 0.055);
      }
      .atlas-legend strong,
      .atlas-legend span {
        display: block;
      }
      .atlas-legend strong {
        margin-bottom: 4px;
        font-size: 0.82rem;
        letter-spacing: 0.035em;
        text-transform: uppercase;
        color: #315f9f;
      }
      .atlas-legend span {
        color: var(--muted, #596474);
        font-size: 0.9rem;
        line-height: 1.45;
      }
      @media (max-width: 980px) {
        .milestone-guide-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        .atlas-legend { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      }
      @media (max-width: 620px) {
        .milestone-guide-grid,
        .atlas-legend { grid-template-columns: 1fr; }
        .milestone-guide-card { min-height: 0; }
      }
    `;
    document.head.append(style);
  }

  function addMilestoneReadingPath() {
    if ((window.location.pathname.split('/').pop() || '') !== 'research-map.html') return;
    if (document.querySelector('.milestone-reading-path')) return;

    const atlas = document.querySelector('#proposition-atlas');
    if (!atlas) return;

    addGuideStyles();

    const section = document.createElement('section');
    section.className = 'milestone-reading-path';
    section.setAttribute('aria-labelledby', 'milestone-reading-path-title');

    const cards = MILESTONES.map((item) => `
      <a class="milestone-guide-card" href="${canonicalHref(item)}">
        <span class="milestone-guide-number">P${item.number}</span>
        <strong>${item.title}</strong>
        <p>${item.role}</p>
        <span class="milestone-guide-open">Open canonical proof →</span>
      </a>
    `).join('');

    section.innerHTML = `
      <div class="section-head">
        <p class="eyebrow">Milestone reading path</p>
        <h2 id="milestone-reading-path-title">Eight orientation checkpoints through the P1-P100 program</h2>
        <p class="milestone-guide-note">These checkpoints are a reading aid, not a claim that the full theorem graph is a single linear dependency chain. Use them to understand the scientific progression, then use the complete searchable atlas for every proposition.</p>
      </div>
      <div class="atlas-legend" aria-label="How to read the proposition atlas">
        <div><strong>P number</strong><span>Development index, not a ranking of scientific importance.</span></div>
        <div><strong>Proof record</strong><span>The canonical proposition document contains the formal statement and derivation.</span></div>
        <div><strong>Figure</strong><span>A visual explanation or diagnostic aid, not a substitute for proof.</span></div>
        <div><strong>Boundary</strong><span>The strongest interpretation the theorem permits, including explicit non-claims.</span></div>
        <div><strong>Frontier</strong><span>P100 is the current Research II theorem frontier; the physical-to-experiential bridge remains open.</span></div>
      </div>
      <div class="milestone-guide-grid">${cards}</div>
    `;

    atlas.insertAdjacentElement('beforebegin', section);
  }

  function run() {
    addMilestoneReadingPath();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
# Reader Experience and Visual Presentation Standard

## Purpose

The Mathematical Consciousness Bridge is intended to be auditable by specialists and understandable to a technically curious first-time reader. The public website and documentation therefore use progressive disclosure: intuition first, formal statement second, proof and implementation third, and provenance plus scientific boundaries throughout.

This standard governs the website, README-level narrative, proposition documentation, figures, and reader navigation.

## First-reader path

A new reader should be able to move through the project in this order without already knowing the proposition chronology:

1. **Question:** What is the physical-to-experiential bridge problem?
2. **Vocabulary:** What do descriptor, target, latent state, observation channel, compatibility, rejection, and bridge claim mean here?
3. **Architecture:** Which scientific assumptions are tested at each layer?
4. **Current frontier:** What does P84 add beyond P83, in plain language?
5. **Formal theorem:** What is actually proved and under which assumptions?
6. **Implementation:** Which source module computes the declared certificate?
7. **Verification:** Which tests, provenance records, and reproducibility checks protect the result?
8. **Boundary:** What stronger interpretation is explicitly not justified?

No page should require a first-time reader to infer this ordering from proposition numbers alone.

## Progressive disclosure rule

Every mature result should expose four layers of explanation.

| Layer | Reader question | Required content |
| --- | --- | --- |
| Orientation | Why does this result exist? | Plain-language scientific question and failure mode |
| Formal result | What is proved? | Assumptions, definitions, theorem statement, proof route |
| Audit | Can I inspect it? | Implementation, tests, equation provenance, figure provenance |
| Interpretation | What may I conclude? | Exact scientific boundary and unresolved questions |

A page may be mathematically dense, but it should not be conceptually opaque.

## Visual size standard

Figures must remain readable at ordinary laptop and tablet widths without occupying an excessive fraction of the page.

- **Theorem and architecture figures:** preferred reading width 760 to 980 CSS pixels, with a normal maximum display height near 640 pixels or 72 percent of the viewport height. Full-resolution source remains one click away.
- **Figure-and-text cards:** figure area should normally resolve to roughly 520 to 720 CSS pixels on desktop, with a normal maximum display height near 500 pixels.
- **Atlas thumbnails:** use a reading height around 205 to 250 CSS pixels for simple plots and diagrams. Complex theorem figures should not be forced into thumbnail treatment.
- **Mobile:** use the full available content width, preserve aspect ratio, and cap vertical dominance rather than shrinking labels below readable size.
- **Never solve overflow by making text tiny.** If labels are not readable at the intended display size, rewrap, simplify, or split the figure.
- **Never crop mathematical content.** `object-fit: contain` or equivalent behavior is required for reader-facing theorem figures.

The goal is balanced visual hierarchy: a figure should be easy to inspect without becoming a poster that pushes the surrounding explanation off screen.

## Figure reading contract

Every important figure must answer:

1. What am I looking at?
2. How should I read the panels, arrows, axes, or regions?
3. What is the precise takeaway?
4. What is the scientific status of the visual?
5. What conclusion must not be inferred?
6. Where can I open the proof, implementation, tests, or source record?

The [Figure Caption and Description Standard](figure_caption_and_description_standard.md) gives the full figure-level requirements.

## Scientific language standard

Reader-friendly language must not weaken scientific precision.

- Say **compatible with the declared model**, not "proved true."
- Say **certified rejection**, not "disproved consciousness" or any broader ontological conclusion.
- Say **latent state**, not "conscious state," unless an independent semantic bridge has been established.
- Say **physical descriptor is insufficient for the declared target**, not "physics is insufficient."
- Say **non-rejection is inconclusive**, not "the model passed."

The physical-to-experiential bridge remains open unless independently formulated and empirically established.

## Cross-linking standard

A first reader should never reach a theorem or figure dead end. Mature surfaces should link to the nearest relevant items among:

- Start Here
- Research Map
- Visual Atlas
- theorem/proposition proof
- implementation module
- regression tests
- equation and citation provenance
- figure catalog
- reproducibility guide

## Maintenance and regression testing

Reader experience is part of repository quality. Regression tests should catch at least:

- stale proposition counts or stale frontier labels;
- broken public figure paths;
- missing shared visual styles in the Pages build;
- theorem figures without responsive containment;
- figure-display rules that can reintroduce clipping or extreme page dominance;
- missing first-reader explanations on the main orientation surfaces.

This standard does not replace scientific review. It makes the scientific record easier to inspect and harder to misunderstand.

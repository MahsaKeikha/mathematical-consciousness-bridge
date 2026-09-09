# Figure Style Guide

This repository treats figures as part of the scientific record. They are not decorative summaries. Every diagram must be readable at normal GitHub width, preserve the mathematical meaning of the underlying result, and remain visually consistent with the rest of the research program.

## 1. Publication standard

All canonical research figures follow these rules:

- white canvas with restrained academic accent colors;
- minimum canvas width of 1500 px for multi-panel diagrams;
- preferred canvas width of 1800 px for dense block diagrams;
- consistent sans-serif text family for prose and a serif family for equations;
- at least 36 px internal horizontal padding inside major cards;
- at least 28 px clearance between the final text glyph and any card border;
- no text placed against card borders;
- no drop shadows, gradients, decorative icons, or ornamental imagery;
- no unexplained acronyms;
- no raw programming notation when standard mathematical symbols are available;
- no claim compressed into a badge when the scientific qualification matters;
- every figure has an SVG `<title>` and `<desc>` for accessibility;
- every visual statement maps to a definition, theorem, experiment, evidence class, or open problem elsewhere in the repository.

The non-negotiable layout rule is

\[
\boxed{
\text{no clipped text}
\quad\text{and}\quad
\text{no text may bleed beyond its intended block}.
}
\]

If content does not fit comfortably, the figure must be enlarged, the text shortened, or the concept split across multiple figures. Font size must not be reduced merely to force content into a box.

## 2. Mathematical typography

Figures use standard mathematical symbols whenever they improve readability:

\[
\bar B,
\qquad
\gamma_S,
\qquad
\varepsilon,
\qquad
\pi,
\qquad
\kappa,
\qquad
\to,
\qquad
\ne.
\]

Long derivations remain in Markdown/LaTeX. Figures should show only the equation required to understand the scientific relation being illustrated.

For a long displayed relation, manual line breaking is preferred to horizontal compression. An equation block should normally contain no more than two visual lines inside one card.

## 3. Text density

A major card should normally contain:

1. one descriptive heading;
2. one defining equation or quantity;
3. two or three short explanatory lines;
4. one scientific-status line only when necessary.

If a concept requires a paragraph, the paragraph belongs in the accompanying documentation, not inside the figure.

For high-visibility figures, the repository's visual-quality tests enforce compact single-line copy. As a design target:

- card heading: approximately 58 characters or fewer;
- body line: approximately 82 characters or fewer;
- equation line: approximately 74 characters or fewer;
- label: approximately 42 characters or fewer.

These are not scientific limits; they are readability constraints for SVG text rendered on GitHub.

## 4. Block-diagram geometry

Every block diagram should use a predictable geometry:

- equal-width peer cards whenever the concepts have the same logical level;
- aligned headings and equation baselines;
- minimum 30 px vertical separation between unrelated text groups;
- minimum 35 px gap between neighboring cards;
- arrows terminate in whitespace, never in text;
- captions and status notes belong below the central content area when possible;
- long bridge statements should be split over two lines rather than extending across a card.

A figure should not rely on the browser to wrap SVG `<text>` automatically. SVG text does not provide reliable paragraph wrapping across renderers. Line breaks must therefore be explicit in the source.

## 5. Wording standard

Figure text should read as scientific prose, not interface copy. Preferred wording is concrete and descriptive:

- `Representation invariance`
- `Directed interventional influence`
- `Partition irreducibility`
- `Experimental recoverability`
- `Open bridge question`

Avoid vague labels such as `smart layer`, `AI result`, `final answer`, or unexplained internal shorthand.

## 6. Figure QA procedure

Before a figure is considered canonical:

1. verify its SVG source contains no unbounded long text line;
2. inspect the rendered GitHub figure at normal README width;
3. confirm every equation remains readable without zooming;
4. confirm no arrow crosses text;
5. confirm no text touches or leaves a card;
6. confirm the figure is cited or explained in the relevant Markdown page;
7. run `pytest` and `ruff check .` on Python 3.10, 3.11, and 3.12.

A canonical visual checkpoint is not complete until the full three-version CI matrix is green on the same repository head.

The automated tests are a minimum safety net. Visual inspection remains required because rendered font metrics can differ across environments.

## 7. Canonical visual set

The current visual research set includes:

- complete research architecture;
- theorem roadmap through P17;
- physics and mathematics atlas;
- equation-to-evidence map;
- thermodynamics of information processing;
- information geometry of response laws;
- conscious-state measurement map;
- state-space dynamics map;
- spaceflight and extreme-environment map;
- multiscale physical hierarchy;
- observer-math to consciousness-bridge handoff;
- intervention-resolved causal-structure anatomy;
- P12 component-collision map;
- P13 pairwise-component irredundancy;
- P14 temporal continuation;
- P15 finite-sample temporal certification;
- P16 composition and coupling;
- P17 coarse-graining and refinement;
- universal-proof ladder;
- theory-comparison map.

The [Visual Research Guide](visual_research_guide.md) provides the recommended reading order.

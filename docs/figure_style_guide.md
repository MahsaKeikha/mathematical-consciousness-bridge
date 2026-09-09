# Figure Style Guide

This repository treats figures as part of the scientific record. They are not decorative summaries. Every diagram must be readable at normal GitHub width, preserve the mathematical meaning of the underlying result, and remain visually consistent with the rest of the research program.

## 1. Publication standard

All canonical research figures follow these rules:

- white canvas with restrained academic accent colors;
- minimum canvas width of 1500 px for multi-panel diagrams;
- consistent sans-serif text family for prose and a serif family for equations;
- at least 24 px internal horizontal padding inside major cards;
- no text placed against card borders;
- no drop shadows, gradients, decorative icons, or ornamental imagery;
- no unexplained acronyms;
- no raw programming notation when standard mathematical symbols are available;
- no claim compressed into a badge when the scientific qualification matters;
- every figure has an SVG `<title>` and `<desc>` for accessibility;
- every visual statement maps to a definition, theorem, experiment, evidence class, or open problem elsewhere in the repository.

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

## 3. Text density

A major card should normally contain:

1. one descriptive heading;
2. one defining equation or quantity;
3. two or three short explanatory lines;
4. one scientific-status line only when necessary.

If a concept requires a paragraph, the paragraph belongs in the accompanying documentation, not inside the figure.

## 4. Wording standard

Figure text should read as scientific prose, not interface copy. Preferred wording is concrete and descriptive:

- `Representation invariance`
- `Directed interventional influence`
- `Partition irreducibility`
- `Experimental recoverability`
- `Open bridge question`

Avoid vague labels such as `smart layer`, `AI result`, `final answer`, or unexplained internal shorthand.

## 5. Canonical visual set

The current visual research set is:

| Figure | Scientific role |
| --- | --- |
| `research_architecture.svg` | complete physics-to-bridge research architecture |
| `theorem_roadmap.svg` | P1-P13 theorem dependency structure |
| `causal_structure_anatomy.svg` | physical definition of the intervention-resolved causal-structure candidate |
| `p12_collision_map.svg` | single-component and scalar collision logic |
| `p13_component_irredundancy.svg` | pairwise component irredundancy |
| `universal_proof_ladder.svg` | twelve conditions for the strongest theorem-and-evidence target |
| `theory_comparison_map.svg` | common comparison interface for major theory families |

The [Visual Research Guide](visual_research_guide.md) provides the recommended reading order.

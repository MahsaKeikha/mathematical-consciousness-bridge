# Figure Caption and Description Standard

## Purpose

Every reader-facing figure in the **Mathematical Consciousness Bridge** repository must be understandable without forcing the reader to guess what a panel, arrow, curve, matrix, color, or boundary is supposed to mean.

A figure is not decoration. It is part of the scientific argument. The visual, its caption, its accessibility description, and its links to the formal record must agree.

This standard applies to conceptual diagrams, theorem figures, quantitative plots, matrices, simulation figures, roadmap graphics, and website atlas images.

---

## Required information for every figure

Every figure must expose the following information either directly in the visible caption or through the immediately associated figure record.

| Required element | What the reader must be able to answer |
| --- | --- |
| **Title** | What object, theorem, experiment, or mathematical relation am I looking at? |
| **What the figure shows** | What are the panels, curves, boxes, arrows, axes, matrices, or regions representing? |
| **How to read it** | In what direction should the diagram be followed, or what comparison should be made across axes, colors, panels, or regions? |
| **Main takeaway** | What mathematical or scientific conclusion is the visual intended to communicate? |
| **Scientific status** | Is this a theorem illustration, exact calculation, synthetic example, simulation, empirical input, or open hypothesis? |
| **Boundary of interpretation** | What conclusion must *not* be inferred from the visual? In particular, a physical or statistical result must not silently become a consciousness-identification claim. |
| **Direct route to evidence** | Where can the reader open the proof, equation provenance, implementation, data/source, or tests? |

The goal is that a technically trained reader can understand the role of the figure on first contact and then follow a direct link if they want to audit the mathematics.

---

## SVG accessibility requirement

Every SVG under [`docs/figures/`](figures/) must contain:

- a meaningful `<title>` identifying the visual;
- a substantive `<desc>` explaining what the visual represents, how it should be interpreted, and its scientific status;
- a canvas/viewBox that contains all visible objects without clipping or bleed;
- labels that are readable at ordinary GitHub and website display sizes.

The embedded description matters because figures are often opened directly, reused outside the README, viewed with assistive technology, or encountered through the visual atlas rather than through the paragraph that originally introduced them.

---

## Visual layout and connector standard

The geometry of a research figure must communicate the same structure as its mathematics. A technically correct figure is not publication-ready if labels escape their containers, arrows float between unrelated objects, or dense text forces the reader to reconstruct the intended hierarchy.

For box-and-arrow theorem figures, the following rules are mandatory:

- **Text containment:** every visible label, equation, qualifier, and boundary statement must remain inside its intended panel or card. Long prose must be deliberately wrapped into separate lines rather than allowed to bleed across a border.
- **Internal padding:** text must have visible breathing room from every card edge. The last text baseline must leave a safe lower margin, and headings must not collide with the first body line.
- **Connector attachment:** a dependency arrow must start at the boundary of its source object and terminate at, or immediately against, the boundary of its destination object. Floating arrows with unexplained gaps are not acceptable.
- **Connector meaning:** arrows must be used only for an explicit logical, computational, temporal, set-inclusion, or data-flow relation. Decorative arrows that could be mistaken for a theorem implication are prohibited.
- **No collisions:** arrowheads, text, equations, card borders, and neighboring panels must not overlap. Connectors should occupy dedicated whitespace whenever possible.
- **Consistent hierarchy:** peer panels should use aligned edges, comparable padding, and consistent typography. A stronger conclusion may be emphasized visually, but not by making the rest of the diagram difficult to read.
- **Equation legibility:** equations must be short enough for the available width or split across logically meaningful lines. Font reduction is a last resort and must not make the mathematics harder to inspect than the surrounding prose.
- **Canvas safety:** all rectangles, text baselines, paths, markers, and other explicit coordinates must remain inside the declared viewBox. Nothing should depend on browser clipping to appear correct.

Where geometry is important to interpretation, regression tests should encode the intended layout, for example by checking panel bounds, safe text baselines, connector endpoints, canvas containment, or required visual stages. The goal is not pixel-perfect styling. The goal is to prevent a future edit or automated regeneration from reintroducing ambiguity, overflow, disconnected arrows, or accidental visual claims.

---

## Caption style for theorem and conceptual figures

A theorem or conceptual caption should answer four questions in plain technical language:

**What am I seeing?** Name the mathematical objects and the relation among them.

**How should I read it?** Explain whether arrows mean logical dependency, set inclusion, data flow, temporal progression, optimization refinement, or some other declared relation.

**What is the takeaway?** State the precise result the figure is meant to make intuitive.

**What is the boundary?** State the most likely overinterpretation when one exists. For this project, that often means distinguishing a physical/statistical certificate from a claim that a latent state or scalar has been identified with consciousness.

---

## Caption style for quantitative figures

Every quantitative entry in the [Quantitative Physics & Mathematics Atlas](quantitative_physics_mathematics_atlas.md) must provide:

1. the equation, definition, theorem, condition, or numerical construction generating the figure;
2. **What the figure shows**, written as an interpretation of the visible pattern rather than only a restatement of the equation;
3. the scientific status of the visual, such as closed-form fact, deterministic calculation, fixed-seed simulation, synthetic benchmark, or numerical verification;
4. a direct reproducibility route through the quantitative figure manifest, generator, and validation report.

Synthetic examples must be labeled synthetic. They must never be presented as empirical consciousness data.

---

## Figure catalog

The generated [Complete Figure Catalog](figure_catalog.md) is the single visual index for the repository. It lists every SVG figure with a direct link and a plain-language description so a reader does not need to search the repository to discover what a file means.

The catalog complements, rather than replaces:

- the [main research narrative](../README.md), which gives the scientific argument;
- the [Visual Atlas](../website/visual-atlas.html), which provides a web-oriented browsing surface;
- the [Quantitative Physics & Mathematics Atlas](quantitative_physics_mathematics_atlas.md), which documents equation-driven plots;
- the [Theorem Roadmap](theorem_roadmap.md), which gives proposition dependencies;
- the [Equation and Citation Map](equation_and_citation_map.md), which gives source and provenance routes.

---

## Automated quality guards

Repository tests enforce the minimum mechanical requirements: SVG title/description metadata, catalog coverage, reader-facing README captions, quantitative-atlas explanation fields, and geometry checks for figures whose layout carries theorem meaning. These checks do not replace scientific judgment, but they prevent undocumented, visually orphaned, overflowing, or structurally ambiguous figures from silently entering the public research record.

A figure should be revised whenever a reader could reasonably ask, “What exactly am I supposed to infer from this?” and the answer is not immediately available beside or inside the visual.

# Reader-First Publication Page Standard

This standard defines how public research pages in the Mathematical Consciousness Bridge should be written and organized.

The goal is simple: **rigor should increase as the reader goes deeper, not arrive all at once on the first screen.**

## 1. Every page has one job

A public page should answer one dominant question. If the page tries to be an introduction, proof archive, literature review, implementation guide, and figure gallery at the same time, split those roles or move the deeper material behind direct links.

## 2. Use progressive disclosure

Public-facing research content should normally appear in this order:

1. **Why this page exists** - one short paragraph.
2. **The scientific question** - one sentence or one compact callout.
3. **What was established** - the result in plain but exact language.
4. **The evidence or key visual** - at most one primary figure before deeper detail.
5. **Scientific boundary** - what the result does not imply.
6. **Go deeper** - direct links to proof, provenance, code, tests, and reproduction.
7. **Technical detail** - only after the reader has orientation.

## 3. Do not make the reader decode internal history before understanding the idea

Proposition numbers are important scholarly identifiers, but they are not a substitute for a scientific question.

Prefer:

> **Can a discovery-selected incompatibility survive independent validation?**  
> P88 answers this under a frozen discovery/validation design.

Avoid opening with a long sequence of internal result numbers and unexplained abbreviations.

## 4. Keep first screens sparse

The first visible section of a landing or orientation page should contain no more than:

- one central question,
- one concise explanation,
- one primary visual or status panel,
- three to six high-value links.

Large tables, exhaustive theorem lists, provenance matrices, and derivations belong on reference pages.

## 5. Make every deep claim directly auditable

A mature computational theorem should expose the following chain whenever those artifacts exist:

**theorem → provenance → implementation → tests → figure → reproduction**

Readers should not have to search the repository to move from a public claim to its evidence.

## 6. Separate scientific status categories

Do not blur these categories:

- definition,
- assumption,
- theorem,
- implementation,
- regression test,
- numerical illustration,
- empirical input,
- model rejection,
- non-rejection,
- scientific interpretation,
- open bridge claim.

A mathematically correct theorem can still be conditional on assumptions that require empirical justification.

## 7. End important pages with a boundary

Every proposition or frontier summary should state the strongest conclusion that is **not** licensed.

For target-model adequacy results, examples include:

- rejection of a declared model is not proof that consciousness is nonphysical;
- a latent variable is not automatically consciousness;
- non-rejection is not model validation;
- a box-specific rejection is not a global model-family rejection without a valid covering argument;
- the physical-to-experiential bridge remains open.

## 8. Prefer one visual with a purpose over many visuals with equal weight

A figure should answer a clear question. If several figures are needed, route readers to the [Figure Catalog](figure_catalog.md) or the [Visual Atlas](../website/visual-atlas.html) instead of stacking many full-size figures on a landing page.

## 9. Tables are for comparison, not prose storage

Use tables when the reader is comparing parallel items such as result status, research layers, or artifact types. Do not place paragraph-length explanations in every cell.

Every important public table should have a stable section heading or anchor so it can be linked directly.

## 10. Deep pages may be long, but they still need orientation

Proof and reference pages can be detailed. Their first section should still tell the reader:

- what question is being answered,
- what assumptions matter most,
- what the result changes relative to the previous result,
- what the result does not claim,
- where to go next.

Length is acceptable when it serves auditability. Unstructured accumulation is not.

## 11. Reader routes are explicit

Use these four public routes consistently:

- **New reader:** [Start Here](../START_HERE.md)
- **Research map:** [Research Architecture](research_architecture.md)
- **Find an artifact:** [Research Traceability Index](research_traceability_index.md)
- **Full technical record:** [Theorem Roadmap](theorem_roadmap.md) and [Detailed Proposition Record](detailed_proposition_record.md)

## 12. The homepage is not the archive

The README and website home page are invitations into the research. They should communicate:

- the central scientific question,
- why it is difficult,
- what the project contributes,
- the current frontier,
- the scientific limits,
- the shortest paths to deeper material.

They should not reproduce the complete research history.

---

This standard complements the [Reader Experience and Visual Presentation Standard](reader_experience_and_visual_standard.md) and the [Figure Caption and Description Standard](figure_caption_and_description_standard.md).

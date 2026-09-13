# Claim, Evidence, and Citation Standard

This document defines the publication rule for scientific claims in the Mathematical Consciousness Bridge project. The purpose is not to maximize citation count. It is to make every consequential statement auditable by showing what kind of statement it is, what supports it, and what it does **not** establish.

## 1. External established results

A nontrivial mathematical, physical, statistical, neuroscientific, or consciousness-science result imported from the literature should be tied to a primary source whenever practical. Prefer the original paper, theorem source, standards document, or authoritative monograph over a secondary summary. Include DOI metadata when available and use stable arXiv identifiers for preprints.

Imported results must not be presented as repository-original contributions.

## 2. Repository-original theorems and constructions

A result developed in this repository is supported by its local scientific record rather than by an unrelated external citation. A mature theorem should expose, as applicable:

- a proposition statement with assumptions and interpretation boundary;
- a proof or exact derivation;
- executable implementation for computational objects;
- regression, counterexample, and edge-case tests;
- equation or construction provenance;
- reproducible figures or a documented source-controlled explanatory figure;
- explicit dependencies on earlier propositions or external results.

A local theorem citation is therefore a path to the proof record, not a claim that external literature has already established the same result.

## 3. Modeling assumptions and definitions

A declared model, bridge class, regularity condition, observation channel, target-construction rule, or metric choice must be labeled as an assumption, definition, or modeling choice unless it is itself derived from a cited result. Mathematical consequences may be proved conditionally from such assumptions, but the assumptions do not become empirical facts because the downstream theorem is exact.

## 4. Empirical claims

Statements about brains, behavior, physiology, anesthesia, reports, clinical states, or measured consciousness-related phenomena require an empirical source. The wording must match the evidence level of that source. Mathematical examples, synthetic distributions, and generated simulations are not empirical evidence.

## 5. Generated and synthetic material

Generated figures, synthetic witnesses, simulations, and exact rational counterexamples must be identified as generated or synthetic where a reader could otherwise mistake them for measured data. Their role is to illustrate, test, or certify a mathematical statement, not to imply a biological observation.

## 6. Open bridge and interpretation claims

The physical-to-experiential bridge remains an open research target in this project. A model-separation theorem can reject a declared model family without proving that consciousness is nonphysical. A compatible model is not thereby validated. A latent variable is not thereby identified with experience. These interpretation boundaries are part of the scientific result and should remain visible on reader-facing surfaces.

## 7. Research origins and scholarly provenance

Intellectual origin and mathematical support are complementary scholarly roles. A paper may open a line of questions, while later results carry their own proof and reproducibility records.

The earliest conceptual line that eventually led to this research program began while studying Max Tegmark's *Consciousness as a State of Matter* (2015):

> Max Tegmark, “Consciousness as a State of Matter,” *Chaos, Solitons & Fractals* **76** (2015), 238-270. DOI: [10.1016/j.chaos.2015.03.014](https://doi.org/10.1016/j.chaos.2015.03.014). Preprint: [arXiv:1401.1219](https://arxiv.org/abs/1401.1219).

That paper is cited here as an important conceptual starting point for questions about physical subsystem structure, factorization, information, integration, independence, and dynamics. The subsequent proposition sequence develops a distinct mathematical framework, with its own assumptions, derivations, implementations, tests, and provenance.

## 8. Reader-facing publication rule

For each consequential claim, a reader should be able to determine which of the following applies:

1. **Externally established:** follow the primary citation.
2. **Repository theorem:** follow the proposition, proof, code, tests, provenance, and figure record.
3. **Modeling assumption or definition:** inspect the declared assumptions and scope.
4. **Generated or synthetic result:** reproduce it from code or exact construction.
5. **Open scientific question:** treat it as unresolved until a theorem or experiment changes its status.

When classification is ambiguous, the publication should be revised until the evidential role is explicit.

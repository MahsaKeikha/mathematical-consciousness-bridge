# Start Here: Mathematical Consciousness Bridge

**A reader-first guide to the research question, the 83-result theorem program, the code, the visual record, and the scientific boundaries.**

If this is your first time in the repository, begin here before opening the full README or an individual theorem file.

> **Central question**
>
> What mathematical and physical conditions would have to be satisfied before a physical description of a system could support a scientifically testable claim about an independently specified experiential target?

The project does **not** begin by choosing a preferred formula for consciousness. It asks what any serious bridge claim would have to survive: representation changes, hidden variables, coarse-graining, target circularity, noisy measurement, non-identifiability, finite data, model inadequacy, and uncertified optimization.

The P83 publication candidate contains **83 proposition-level results** and **71 paper-facing equation-driven quantitative figures**. The current theorem frontier is **P83: Exact Signed Cylinder-Contrast Certificate for Continuous P75 Separation**. The physical-to-experiential bridge itself remains open.

---

## The project in one picture

```mermaid
flowchart LR
    A[Physical system\nstate, dynamics, interventions] --> B[Operational physical description\ninvariance, causality, time, scale]
    B --> C[Physical sufficiency test\nP19-P24]
    C --> D[Target integrity\nprovenance + measurement\nP71-P74]
    D --> E[Target-model adequacy\nP75-P83]
    E --> F[Finite-data decision\ncertified rejection / inconclusive]
    F --> G[Physical-to-experiential bridge\nSTILL OPEN]

    H[Quantum branch\nP38-P44] --> C
    I[Experiment design + scheduling\nP45-P60] --> F
    J[Calibration + optimization\nP61-P70] --> I

    classDef open fill:#fff7ed,stroke:#ea580c,stroke-width:2px,color:#7c2d12;
    classDef core fill:#eff6ff,stroke:#2563eb,stroke-width:1.5px,color:#172554;
    classDef target fill:#f0fdf4,stroke:#16a34a,stroke-width:1.5px,color:#14532d;
    class A,B,C,H,I,J core;
    class D,E,F target;
    class G open;
```

The arrows show **logical dependency**, not proof that experience has already been reduced to physics. Read the repository as a staged test architecture: each layer removes one class of hidden assumption before a stronger claim is allowed.

---

## What has been proved, and what has not

| Status | Meaning in this repository |
| --- | --- |
| **Proved mathematical result** | A proposition follows from explicit assumptions and has an auditable proof record. |
| **Implemented certificate** | Executable code computes the theorem quantity and regression tests guard its invariants. |
| **Finite-data guarantee** | The conclusion includes explicit uncertainty or confidence control under the declared sampling model. |
| **Model rejection** | The declared model is incompatible with the data under the stated certificate. This is not a proof that consciousness is nonphysical. |
| **Non-rejection** | The current test did not certify incompatibility. This is not model validation. |
| **Open bridge claim** | The step from physical description to experiential structure has not been established. |

The repository deliberately separates **mathematical correctness**, **empirical adequacy**, and **experiential interpretation**. They are not interchangeable.

---

## Choose the reading path that fits you

| If you are... | Start with | Then read |
| --- | --- | --- |
| **A first-time reader** | this page | [README](README.md) → [Research Navigation](docs/research_navigation.md) |
| **A mathematician** | [Theorem Roadmap](docs/theorem_roadmap.md) | [Detailed Proposition Record](docs/detailed_proposition_record.md) → proposition proofs → [Equation and Citation Map](docs/equation_and_citation_map.md) |
| **A physicist** | [Bridge Problem](docs/bridge_problem.md) | P11-P19 → [Quantum Foundations and Bridge Test](docs/quantum_foundations_and_bridge_test.md) → P38-P44 → P71-P83 |
| **A consciousness researcher** | [Bridge Problem](docs/bridge_problem.md) | P19 → P71-P83 → [Falsification Program](docs/falsification_program.md) |
| **An experimentalist or statistician** | P20-P24 | P39-P44 → P47-P60 → P74-P83 |
| **A software reviewer** | [pyproject.toml](pyproject.toml) | [`src/consciousness_bridge/`](src/consciousness_bridge/) → [`tests/`](tests/) → theorem/provenance files |
| **A visual reader** | [Figure Catalog](docs/figure_catalog.md) | [Visual Atlas](website/visual-atlas.html) → theorem figures linked from the roadmap |

---

## The 83 results, organized by scientific role

Proposition numbers record development order. They do **not** imply that every later proposition depends on every earlier one.

| Results | Scientific function | Why this layer exists |
| --- | --- | --- |
| **P1-P10** | Invariance, identifiability, recovery, robust protocol design | Prevent representation choices or weak experiments from being mistaken for physical facts. |
| **P11-P18** | Intervention-resolved causal, temporal, compositional, and scale-aware physical structure | Make the physical description operational rather than purely descriptive. |
| **P19-P24** | Physical sufficiency, residual tests, refinement, adaptive validity | Test whether a declared physical descriptor screens off an independently specified target. |
| **P25-P37** | Operational-scale compatibility | Track which physical distinctions survive aggregation, quotienting, and scale changes. |
| **P38-P44** | Quantum operational sufficiency | Test declared quantum descriptions without assuming that quantum completeness is experiential completeness. |
| **P45-P60** | Adaptive experiment design, scheduling, switching, and transition calibration | Collect evidence efficiently while preserving validity. |
| **P61-P70** | Calibration and optimization | Solve downstream finite-resource allocation problems once the scientific witness is already defined. |
| **P71-P74** | Target provenance and target measurement | Prevent circular targets and quantify whether noisy target measurements are identifiable and reliable. |
| **P75-P83** | Target-model adequacy and certified continuous-family separation | Test the declared target-measurement model itself, including finite-data rejection and progressively tighter exact-rational model-distance certificates. |

For the complete one-row-per-proposition index, use the [Theorem Roadmap](docs/theorem_roadmap.md) and [Research Navigation](docs/research_navigation.md).

---

## The current frontier: P71-P83 in plain language

The newest branch returns to a basic scientific obligation: before a physical descriptor can be judged sufficient for an experiential target, the **target**, the **measurement of that target**, and the **measurement model itself** must survive independent tests.

**P71: target provenance.** A target constructed from the same descriptor being tested can satisfy the desired bridge relation by construction. P71 formalizes that circularity failure mode.

**P72: noisy target measurement.** Under the declared nondifferential channel, noisy observation can attenuate or erase a real target-side distinction. A null observation is therefore not automatically evidence of no latent distinction.

**P73: target-channel identifiability.** Under a restricted nondegenerate three-view binary latent model, target-measurement channels can be recovered up to the unavoidable global latent-label swap. Two views are insufficient in general.

**P74: finite-sample recovery.** Population identifiability is not enough. P74 adds simultaneous uncertainty bounds and refuses to certify recovery near the inversion singularity.

**P75: model adequacy.** Successfully recovering parameters does not prove the model is right. A fourth binary view creates overidentifying restrictions and a full-law reconstruction audit.

**P76: finite-sample adequacy rejection.** A P75 constraint violation must remain separated from zero after uncertainty is propagated before the model is rejected.

**P77: full-law model-set separation.** P77 asks whether the entire empirical confidence region is separated from the entire declared model family rather than checking only selected necessary constraints.

**P78: certified continuous separation.** The P75 family is continuous, so an ordinary numerical best fit cannot certify separation from every allowed model. P78 uses exact-rational branch-and-bound to produce a global lower bound.

**P79: certified sampling radius.** P79 gives an exact-rational upper certificate for the statistical radius used in the P77 rejection inequality.

**P80: simplex-coupled tightening.** P80 retains probability normalization inside the P78 interval relaxation, so its box lower bound cannot be weaker than P78.

**P81: projection-event tightening.** P81 adds all 80 nonempty projected binary cylinder events and transfers event mismatch back to a certified full-law $L_\infty$ lower bound.

**P82: exact nested residual tightening.** P82 adds 256 genuinely new residual events formed from nested cylinders and computes their parameter-box ranges directly from the P75 factorization. The strict witness improves P81 from $1/16$ to $1/12$.

**P83: exact signed cylinder-contrast tightening.** P83 asks whether two non-nested cylinder probabilities are jointly compatible with one common P75 parameter vector. It audits 2,696 new signed cylinder pairs. On the exact strict witness,

\[
L_{80}=L_{81}=L_{82}=0,
\qquad
L_{83}=\frac{5}{128},
\]

and an explicit admissible P75 law at prevalence $\pi=5/16$ is exactly $5/128$ away. Thus P83 closes the true model distance on that witness while the P82 relaxation reports zero.

The direct P83 proof is [here](docs/proposition_83_signed_cylinder_contrast_separation.md), with its [implementation](src/consciousness_bridge/signed_cylinder_contrast_separation.py), [tests](tests/test_signed_cylinder_contrast_separation.py), and [theorem figure](docs/figures/p83_signed_cylinder_contrast_separation.svg).

---

## The continuous model-separation chain

For the same P75 parameter box $B$ and empirical law $\widehat p$, the current exact-rational lower-bound chain is

\[
\boxed{
L_{83}(B)
\ge L_{82}(B)
\ge L_{81}(B)
\ge L_{80}(B)
\ge L_{78}(B).
}
\]

The roles are distinct:

- **P78**: exact cellwise parameter-box intervals plus certified branch-and-bound;
- **P80**: probability-simplex coupling;
- **P81**: all nonempty cylinder-event constraints;
- **P82**: exact nested residual events;
- **P83**: exact signed differences of non-nested cylinder events.

**P79** supplies the independent exact-rational upper bound on the P77 sampling radius. The rejection handoff remains one-sided:

\[
L_{83}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
\text{reject the declared P75 model family at the stated confidence level.}
\]

Failure of that strict inequality remains inconclusive.

---

## How to audit any theorem in this repository

Each mature proposition is intended to expose the same chain:

1. **Scientific question** — what hidden assumption or failure mode is being addressed?
2. **Declared assumptions** — exactly what mathematical, physical, statistical, or measurement conditions are required?
3. **Formal statement** — what is actually proved?
4. **Proof** — which constructions or inequalities establish it?
5. **Implementation** — does executable code compute the certificate?
6. **Tests** — are exact witnesses, edge cases, dominance relations, and regression behavior checked?
7. **Provenance** — which ingredients are standard, inherited, or repository-original?
8. **Scientific boundary** — what stronger conclusion is explicitly *not* justified?

This structure is designed so a skeptical reader can audit the mathematics without first accepting the research motivation.

---

## Key notation

| Symbol | Meaning |
| --- | --- |
| $\Omega$ | physically admissible state or history space |
| $T$ | declared physical descriptor |
| $E$ | independently specified target whose distinctions a bridge claims to explain |
| $B$ | candidate bridge map, when one is declared |
| $E^\star$ | latent target before target-measurement noise |
| $Y$ | observed target measurement |
| P75 model | declared four-view binary latent target-measurement family used in P75-P83 |
| $L_{78},L_{80},L_{81},L_{82},L_{83}$ | progressively tighter certified lower bounds for continuous P75 separation |

Every proof file defines its local notation explicitly.

---

## Where the strongest claims stop

A reader should leave the repository with five boundaries clear:

1. **A failed descriptor is not proof of nonphysical consciousness.** The descriptor may omit relevant physical information.
2. **A successful fit is not a bridge proof.** It may be circular, underidentified, noisy, or empirically underconstrained.
3. **A latent variable is not automatically consciousness.** Semantic identification requires independent justification.
4. **Quantum completeness is not automatically experiential completeness.** A bridge principle still has to be stated and tested.
5. **The physical-to-experiential bridge remains open.** The repository builds mathematical obligations and falsification machinery for studying it rigorously.

---

## Best next links

- **Full scientific narrative:** [README](README.md)
- **Logical theorem dependency structure:** [Theorem Roadmap](docs/theorem_roadmap.md)
- **All research entry points:** [Research Navigation](docs/research_navigation.md)
- **Every proposition in compact form:** [Detailed Proposition Record](docs/detailed_proposition_record.md)
- **P83 proof:** [Proposition 83](docs/proposition_83_signed_cylinder_contrast_separation.md)
- **P83 implementation:** [`signed_cylinder_contrast_separation.py`](src/consciousness_bridge/signed_cylinder_contrast_separation.py)
- **P83 regression tests:** [`test_signed_cylinder_contrast_separation.py`](tests/test_signed_cylinder_contrast_separation.py)
- **Equation-level provenance:** [Equation and Citation Map](docs/equation_and_citation_map.md)
- **All curated visuals:** [Figure Catalog](docs/figure_catalog.md)
- **What would count as failure:** [Falsification Program](docs/falsification_program.md)
- **How to cite the work:** [Citation Guide](CITATION.md)
- **Reproduce everything:** [Reproducibility Guide](docs/reproducibility.md)
- **Contribute or review changes:** [CONTRIBUTING.md](CONTRIBUTING.md)
- **Public visual site:** [website](website/index.html)

---

## Current research status

**Publication candidate:** v0.83.0  
**Proposition frontier:** P83  
**Proposition-level results:** 83  
**Paper-facing equation-driven figures:** 71  
**Scientific status of the bridge:** open  
**Repository standard:** theorem + proof + implementation + tests + provenance + explicit scientific boundary where applicable

The project is intended to remain difficult to overclaim. A result is strongest when a reader can see not only what it establishes, but exactly what it leaves unresolved.

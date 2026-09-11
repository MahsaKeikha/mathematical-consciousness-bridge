# P79 Equation and Provenance Record

## Purpose

This record classifies the mathematical ingredients used by P79 and separates standard statistical/global-optimization facts from the repository-specific P77-P78 assembly.

---

## Standard ingredients

### Confidence-set and hypothesis-test duality

The P77 rejection rule is an instance of confidence-set inversion: a declared model family is rejected when the finite-sample confidence region for the population law is disjoint from that model family.

This principle is standard statistical methodology and is not claimed as new.

Representative background:

- P. B. Stark, course notes on duality between hypothesis tests and confidence sets, University of California, Berkeley.

### Lower and upper bounds in deterministic global optimization

Branch-and-bound and interval global optimization use rigorous lower and upper bounds on a global optimum and refine those bounds until a termination criterion is satisfied.

This is standard global-optimization methodology and is not claimed as new.

Representative background:

- A. Schöbel and D. Scholz, "The theoretical and empirical rate of convergence for geometric branch-and-bound methods," *Journal of Global Optimization* 48, 473-495, 2010.
- D. Scholz, "Theoretical rate of convergence for interval inclusion functions," *Journal of Global Optimization* 53, 749-767, 2012.
- P. Kirst and C. Füllner, "On the use of restriction of the right-hand side in spatial branch-and-bound algorithms to ensure termination," *Computational Optimization and Applications* 90, 691-720, 2025.

P79 does not claim the existence of global lower/upper bound sequences or optimality-gap stopping as repository-original mathematics.

---

## Repository-specific assembly

### P79A: signed decision-margin enclosure

P77 defines the full-law decision boundary through the empirical model distance and the finite-sample radius. P78 provides a certified distance bracket

\[
L\le d\le U.
\]

P79 adds a certified radius bracket

\[
\underline\varepsilon\le\varepsilon\le\overline\varepsilon
\]

and assembles the two into

\[
\boxed{
L-\overline\varepsilon
\le
d-\varepsilon
\le
U-\underline\varepsilon.
}
\]

The interval arithmetic itself is elementary. The repository-specific content is its explicit role as the signed P77-P78 decision certificate.

### P79B: certified rejection

\[
L>\overline\varepsilon
\quad\Longrightarrow\quad
\mathcal C_n(\widehat P)\cap\mathcal M=\varnothing.
\]

This preserves the lower-bound direction already required by P77 and P78.

### P79C: certified non-separation

For the compact P75 observed-law family,

\[
U\le\underline\varepsilon
\quad\Longrightarrow\quad
\mathcal C_n(\widehat P)\cap\mathcal M_{4,2}\neq\varnothing.
\]

The compactness argument is standard. The repository-specific contribution is recognizing the upper side of the P78 bracket as a rigorous stopping certificate for the complementary non-separation outcome of the P77 test.

This conclusion is not model acceptance.

### P79D: unresolved state

If neither directional inequality is certified, the current bracket does not decide whether the P77 confidence region intersects the model family.

This is an algorithmic status, not a scientific conclusion about the truth of the model.

### P79E: total decision uncertainty and margin stopping

The signed decision interval has width

\[
\boxed{
(U-L)+(\overline\varepsilon-\underline\varepsilon).
}
\]

If the exact signed margin is nonzero and the total certified width is strictly smaller than its magnitude, the three-way decision cannot remain unresolved.

Again, interval-width reasoning is elementary. Its P79 contribution is the explicit combined optimization-plus-radius stopping condition for the P77 full-law test.

---

## Claims not made

P79 does not claim that:

- confidence-set inversion is new;
- branch-and-bound gap stopping is new;
- interval enclosures are new;
- the P75 latent variable is consciousness;
- certified non-separation validates the P75 model;
- conditional independence is established empirically;
- the physical-to-experiential bridge is solved.

The physical-to-experiential bridge remains open.

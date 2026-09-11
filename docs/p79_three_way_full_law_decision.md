# P79: Three-Way Full-Law Decision and Certified Computational Stopping

## Status

**Core theorem proved and implemented on the P79 development branch. Public frontier integration is intentionally deferred until the core result passes CI.**

P79 is a decision theorem at the interface between P77 and P78. It does not introduce a new consciousness ontology. It uses the certified distance bracket already produced by P78 and asks what that bracket can prove about the P77 full-law confidence-region test.

---

## 1. Setup

Let \(\widehat P\) be the empirical sixteen-cell four-view law and let \(\mathcal M_{4,2}\) denote the complete P75 observed-law family. Define the exact empirical model distance

\[
d := d_\infty(\widehat P,\mathcal M_{4,2})
=\inf_{Q\in\mathcal M_{4,2}}\|\widehat P-Q\|_\infty.
\]

P78 returns a certified optimization bracket

\[
L\le d\le U.
\]

P77 uses the simultaneous sampling radius

\[
\varepsilon_{n,16}(\alpha)
=\sqrt{\frac{\log(32/\alpha)}{2n}}.
\]

For a fully rigorous numerical interface, P79 does not require this transcendental quantity to be represented exactly. Instead assume certified rational bounds

\[
\underline\varepsilon
\le
\varepsilon_{n,16}(\alpha)
\le
\overline\varepsilon.
\]

The lower and upper directions matter differently.

---

## 2. P79A: certified signed-margin enclosure

Define the exact signed P77 decision margin

\[
\Delta=d-\varepsilon_{n,16}(\alpha).
\]

From

\[
L\le d\le U
\]

and

\[
\underline\varepsilon\le\varepsilon_{n,16}(\alpha)\le\overline\varepsilon,
\]

we immediately obtain

\[
\boxed{
L-\overline\varepsilon
\le
\Delta
\le
U-\underline\varepsilon.
}
\]

This interval is the P79 decision certificate. It encloses the exact quantity whose sign determines whether the P77 confidence ball is separated from the declared model family.

---

## 3. P79B: rejection side

If

\[
\boxed{L>\overline\varepsilon,}
\]

then

\[
d\ge L>\overline\varepsilon\ge\varepsilon_{n,16}(\alpha).
\]

Therefore

\[
\mathcal C_n(\widehat P)\cap\mathcal M_{4,2}=\varnothing,
\]

and P77 rejects the declared model family with its stated finite-sample confidence guarantee.

This is the same lower-bound direction already required by P77 and P78. P79 retains it unchanged.

---

## 4. P79C: certified non-separation side

Suppose

\[
\boxed{U\le\underline\varepsilon.}
\]

Then

\[
d\le U\le\underline\varepsilon\le\varepsilon_{n,16}(\alpha).
\]

The P75 model family is the continuous image of the compact parameter cube \([0,1]^9\). Hence \(\mathcal M_{4,2}\) is compact and the L-infinity distance is attained. There exists some

\[
Q^\star\in\mathcal M_{4,2}
\]

such that

\[
\|\widehat P-Q^\star\|_\infty=d
\le\varepsilon_{n,16}(\alpha).
\]

Therefore

\[
\boxed{
\mathcal C_n(\widehat P)\cap\mathcal M_{4,2}\neq\varnothing.
}
\]

This is a certified **non-separation** result for the P77 full-law test at the current empirical law, sample size, and confidence level.

It has an important computational consequence: once \(U\le\underline\varepsilon\), no amount of further global-optimization refinement on the same empirical law can make the P77 separation criterion reject. The exact model distance is already known to lie inside the confidence radius.

This conclusion is **not model acceptance**. It does not show that the P75 family is true, uniquely identified, scientifically adequate in every respect, or semantically connected to consciousness. It says only that this particular confidence-region separation test cannot reject the model with the current data and confidence level.

---

## 5. P79D: unresolved computational region

The remaining case is

\[
L\le\overline\varepsilon
\quad\text{and}\quad
U>\underline\varepsilon.
\]

Equivalently, the certified signed-margin interval contains zero or overlaps it:

\[
L-\overline\varepsilon\le0<U-\underline\varepsilon.
\]

Then the current information does not determine the P77 decision.

More P78 refinement may tighten \([L,U]\). A tighter certified enclosure of the P77 radius may also help. If neither is enough, new data may be required.

P79 therefore produces exactly three logically distinct states:

1. **reject**: certified model separation;
2. **nonseparation**: certified intersection with the P77 confidence region, without model acceptance;
3. **unresolved**: current certified brackets overlap the decision boundary.

---

## 6. P79E: deterministic margin-dependent stopping theorem

Let

\[
g_d=U-L
\]

be the optimization bracket width and

\[
g_\varepsilon=\overline\varepsilon-\underline\varepsilon
\]

be the numerical sampling-radius enclosure width.

The P79 signed-margin interval has width

\[
\boxed{
g_\Delta=g_d+g_\varepsilon.
}
\]

Suppose the exact signed margin is nonzero:

\[
|\Delta|>0.
\]

If

\[
\boxed{
g_d+g_\varepsilon<|\Delta|,}
\]

then an interval that contains \(\Delta\) cannot still straddle zero. Hence the P79 three-way decision must have resolved to either rejection or certified non-separation.

This is a deterministic computational stopping theorem. It does not provide an estimator of the unknown exact margin. Instead, it identifies the mathematical condition under which continued bracket refinement is guaranteed to resolve the decision.

The boundary case

\[
\Delta=0
\]

is intentionally excluded. At exact contact between the model set and the P77 confidence-ball boundary, finite termination from strict rejection logic need not follow from a generic convergence argument.

---

## 7. Why the two sampling-radius directions differ

The statistical radius is transcendental because it contains logarithm and square root operations. A naive floating-point value should not be silently promoted to a formal certificate.

P79 exposes the correct directional requirements:

- **rejection** needs a valid upper bound \(\overline\varepsilon\) on the radius;
- **non-separation** needs a valid lower bound \(\underline\varepsilon\) on the radius.

Using the wrong direction can invalidate the conclusion.

This is the radius-side analogue of the optimizer-direction rule established by P77 and P78:

- rejection needs a global lower bound on model distance;
- non-separation can use a valid upper bound on model distance.

Together these produce a fully directional four-bound interface.

---

## 8. Relation to standard statistics and global optimization

The ingredients are standard.

Confidence-set inversion and the duality between confidence sets and hypothesis tests are classical statistical ideas. Likewise, deterministic global optimization routinely uses convergent lower and upper bounds and stops when a certified optimality gap is sufficiently small.

P79 does not claim either principle as new.

The repository-specific contribution is their assembly at the P77-P78 interface:

- a certified interval for the signed full-law decision margin;
- a rigorous non-separation certificate complementary to P77 rejection;
- the observation that certified non-separation makes further optimization on the same dataset irrelevant to the P77 decision;
- a two-sided sampling-radius enclosure with correct inequality directions;
- a margin-dependent stopping condition that includes both optimization and radius-enclosure uncertainty.

---

## 9. Scientific boundaries

P79 establishes a decision and stopping theorem for a declared statistical model family. It does **not** establish that:

- the P75 latent state is consciousness;
- the P75 target-measurement model is true;
- non-separation is evidence that the model has been validated;
- a failure to reject supports one unique latent explanation;
- conditional independence is empirically correct;
- a new sample will preserve the same empirical model distance;
- consciousness is reducible to current physics;
- consciousness is irreducible to physics;
- the physical-to-experiential bridge has been solved.

The physical-to-experiential bridge remains open.

---

## 10. Implementation

Core implementation:

[`three_way_full_law_decision.py`](../src/consciousness_bridge/three_way_full_law_decision.py)

Core regression tests:

[`test_three_way_full_law_decision.py`](../tests/test_three_way_full_law_decision.py)

Public README, website, release metadata, figure, and proposition-frontier integration are intentionally deferred until the P79 core theorem passes CI.

# Candidate P84: Exact Joint Projection-Parity Contrast Certificate

## Status

**Candidate frontier theorem, implemented and regression-tested, not yet promoted to the documented proposition frontier.**

The current documented theorem frontier remains P83. This note records the stronger exact-rational construction already implemented in `src/consciousness_bridge/joint_projection_parity_contrast_separation.py` so that the mathematics can be reviewed before the README, citation metadata, theorem chronology, figures, and public website are advanced together.

This separation is intentional. A theorem number should not become part of the public frontier merely because code exists. Promotion should occur only after the proof record, provenance record, reader surfaces, figure, citation metadata, and reproducibility checks are synchronized.

---

## 1. Question left open by P83

P83 tests 22 projection-parity events separately. For each parity event it computes the exact probability range over a P75 parameter box.

Separate interval compatibility does not imply that two observed parity probabilities are jointly attainable by one common P75 parameter assignment. Two events can each lie inside their own exact scalar ranges while their difference lies outside the exact range allowed by the shared response parameters.

The candidate P84 construction tests that missing shared-parameter compatibility directly.

---

## 2. Coupled parity contrast

For two parity events

\[
H_1 = H(J_1,b_1),
\qquad
H_2 = H(J_2,b_2),
\]

with different view sets, define

\[
C = P(H_1)-P(H_2).
\]

Inside one P75 latent branch,

\[
P_s(H(J,b))
=
\frac{1+(-1)^b\prod_{j\in J}(1-2q_{j,s})}{2}.
\]

Therefore

\[
C_s
=
\frac12
\left[
(-1)^{b_1}\prod_{j\in J_1}(1-2q_{j,s})
-
(-1)^{b_2}\prod_{j\in J_2}(1-2q_{j,s})
\right].
\]

This is multi-affine in the response coordinates appearing in the union of the two view sets. Its exact extrema on an axis-aligned rational parameter box therefore occur at common endpoint vertices of that union box.

The phrase **common endpoint vertices** is essential. The two parity probabilities are not optimized independently.

---

## 3. Why the interval is exact

Let

\[
U=J_1\cup J_2.
\]

The branchwise contrast is multi-affine in the coordinates indexed by \(U\). Since there are only four observed views,

\[
|U|\le 4,
\]

so at most

\[
2^4=16
\]

endpoint assignments need to be checked per latent branch.

The minus-branch and plus-branch response coordinates are disjoint. Once their exact contrast intervals are known, the full latent mixture is affine in prevalence \(\pi\), so the mixture extrema occur at the prevalence endpoints.

The resulting contrast interval is exact over the declared parameter box. It is not a generic interval enclosure produced by subtracting two independently optimized P83 ranges.

---

## 4. Standard candidate family size

P83 has 22 parity events: both parity values for each of the 11 nontrivial view sets of sizes two, three, and four.

Candidate P84 takes every unordered pair whose view sets differ. Pairs with the same view set are omitted because the two complementary parity probabilities are algebraically redundant with one P83 probability.

This leaves

\[
\boxed{220}
\]

genuinely coupled standard contrasts.

The executable implementation verifies this count exactly.

---

## 5. Transfer to full-law L-infinity distance

For parity events \(H_1\) and \(H_2\), define

\[
c_x = 1_{H_1}(x)-1_{H_2}(x).
\]

Then

\[
|C(p)-C(q)|
\le
\left(\sum_x |c_x|\right)\|p-q\|_\infty.
\]

For the standard genuinely coupled parity contrasts used here, the signed coefficient support has eight cells. Therefore an empirical contrast gap \(g\) outside the exact P75 contrast interval gives the certified lower bound

\[
\|\widehat p-q\|_\infty
\ge
\frac{g}{8}.
\]

The candidate box certificate is

\[
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{joint-parity}}(B)\}.
\]

It is therefore never weaker than P83 on the same box.

---

## 6. Exact strict-strengthening witness

The regression suite contains an exact rational parameter box and empirical law for which

\[
L_{83}(B)=0,
\]

but one coupled parity contrast lies exactly

\[
\frac14
\]

outside its exact P75 box range.

The signed contrast has eight nonzero cell coefficients, so

\[
L_{84}(B)
=
\frac{1/4}{8}
=
\boxed{\frac1{32}}.
\]

Thus the executable witness establishes

\[
\boxed{L_{84}(B)=\frac1{32}>0=L_{83}(B)}.
\]

This is a strict strengthening of the declared model-distance certificate. It is not evidence that consciousness is nonphysical and does not identify the P75 latent state with experience.

---

## 7. Global branch-and-bound handoff

The candidate P84 lower bound can replace the P83 box lower bound inside the existing exact-rational branch-and-bound architecture.

The global lower certificate remains the minimum lower bound over active boxes that partition the complete P75 parameter cube. Explicit P75 parameter vectors remain valid global upper-bound witnesses. The previously proved P78 mesh-width upper certificate remains valid because the underlying model-distance problem is unchanged.

No new convergence-rate theorem is claimed here.

---

## 8. Finite-data handoff

The P79 one-sided sampling-radius upper certificate remains the statistical comparison quantity. A strict inequality

\[
L_{84}(\mathcal B) > \overline\varepsilon_{79}
\]

would certify rejection of the declared P75 family under the same P77 finite-data logic.

Failure of that strict inequality remains inconclusive. It is not model validation.

---

## 9. Executable record

Implementation:

- `src/consciousness_bridge/joint_projection_parity_contrast_separation.py`

Regression tests:

- `tests/test_joint_projection_parity_contrast_separation.py`

The tests verify:

- exactly 220 standard genuinely coupled contrasts;
- exact agreement between the analytic box interval and exhaustive parameter-box vertex evaluation on a nontrivial rational box;
- strict improvement from `L83 = 0` to `L84 = 1/32` on the exact witness;
- eight-cell signed coefficient support for the named strict witness;
- boxwise dominance `L84 >= L83`;
- exact-rational global branch-and-bound behavior;
- the scientific boundary that the certificate rejects only the declared P75 model family.

---

## 10. Promotion checklist

Before this candidate is promoted to the documented P84 frontier, the following surfaces should advance together:

1. proposition proof document;
2. equation and provenance record;
3. detailed proposition chronology;
4. theorem roadmap and research navigation;
5. README and START_HERE reader counts;
6. citation metadata and citation guide;
7. a dedicated P84 explanatory SVG with accessible metadata;
8. figure catalog and public visual surfaces;
9. website index, start page, research map, and implementation guide;
10. complete multi-version test and reproducibility audit.

Until that synchronization is complete, the public documented theorem frontier remains P83.

---

## Scientific boundary

The candidate P84 mathematics establishes a stronger conditional separation certificate for one declared latent-variable model family. It does not establish that the model's latent state is consciousness, that parity is a consciousness measure, that failure of the model implies experience lies outside physics, or that the physical-to-experiential bridge has been solved.

The bridge remains open.

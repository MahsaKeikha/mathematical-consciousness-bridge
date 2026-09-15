# P91 Equation Provenance

## Scope

This note records the origin and status of the equations used in Proposition 91, the mixed-prevalence rank-two flattening separation theorem.

P91 is repository-original as a **specific exact separation certificate for the declared P75 model family and established empirical witness**. The underlying facts that a two-component product mixture becomes a sum of two rank-one matrices after bipartite flattening, that such a matrix has rank at most two, and that its three-by-three minors vanish are standard linear algebra and latent-class tensor structure. P91 does not claim those general identities as new mathematics.

---

## Equation record

| Equation or construction | Status | Provenance |
| --- | --- | --- |
| Two-component P75 law | inherited repository model | P75 four-view latent conditional-independence family |
| Bipartite flattening \(F_{14\mid23}\) | P91 choice of representation | direct reshaping of the sixteen observable probabilities |
| \(F_{14\mid23}=(1-\pi_+)u_-v_-^{\mathsf T}+\pi_+u_+v_+^{\mathsf T}\) | direct derivation | elementary factorization of the P75 conditional-product model |
| \(\operatorname{rank}F_{14\mid23}\le2\) | standard linear algebra consequence | rank of a sum is at most the sum of ranks; each outer product has rank at most one |
| Vanishing of every three-by-three flattening minor | standard rank criterion | a matrix has rank at most two only if every three-by-three minor vanishes |
| Selected empirical minor | P91 witness choice | exact extraction from the established 24-count empirical law |
| Selected determinant \(1/512\) | exact arithmetic | direct determinant calculation |
| Nonnegative radius box \([\max(0,a_{ij}-\varepsilon),\min(1,a_{ij}+\varepsilon)]\) | P91 robustification | direct consequence of full-law L-infinity distance and probability constraints |
| Vertex-extremum rule for determinant | standard multi-affine fact | the determinant is affine in each entry separately, so rectangular-box extrema occur at vertices |
| 512-vertex enumeration | P91 exact certificate | nine uncertain minor entries give \(2^9=512\) box vertices |
| Minimum determinant \(23/677376\) at radius \(1/42\) | P91 exact certificate | exhaustive rational vertex evaluation |
| Failure of the same minor relaxation at radius \(1/41\) | P91 regression guard | exact vertex range crosses zero: minimum \(-7/860672\), maximum \(3793/860672\) |
| Global lower exclusion \(d_\infty>1/42\) | Proposition 91 | rank-two necessity plus exact positive determinant interval |
| Rational mixed parameter point \((4/5,9/10,5/8,1/6,1/2,1/6,2/3,0,1)\) | P91 constructive certificate | repository search followed by exact rational verification |
| Full-law upper radius \(1/24\) | exact evaluation | maximum absolute difference over all sixteen observable cells |
| Mixed-prevalence bracket \(1/42<d_\infty\le1/24\) | Proposition 91 | combination of the exact lower exclusion and constructive upper certificate |

---

## Why P91 is not a restatement of P90

P90 uses the strict parameter-box condition

\[
\pi_+=0,
\]

which removes one latent component entirely. The active observable law is then one product distribution, and selected two-by-two slices have rank one.

P91 permits arbitrary prevalence. When both latent weights are positive, a two-by-two slice can generically have rank two, so the P90 determinant-zero identity no longer applies. P91 instead reshapes the full four-way tensor into a four-by-four matrix. Two latent product components imply rank at most two for that flattening, producing cubic three-by-three-minor constraints that remain valid throughout the full prevalence interval.

Thus P91 changes both the parameter domain and the algebraic constraint.

---

## Exact arithmetic and implementation

The executable implementation uses `fractions.Fraction` for all published quantities.

The lower certificate:

1. constructs the exact empirical \((X_1,X_4)\mid(X_2,X_3)\) flattening;
2. extracts the declared three-by-three minor;
3. confirms determinant \(1/512\);
4. builds the nonnegative entrywise uncertainty box at radius \(1/42\);
5. enumerates all 512 vertices exactly; and
6. verifies that the minimum determinant is \(23/677376>0\).

The upper certificate evaluates one explicit rational P75 parameter point with prevalence \(4/5\), checks all sixteen three-by-three flattening minors, and computes full-law L-infinity distance exactly.

Files:

- `src/consciousness_bridge/mixed_prevalence_rank_two_flattening_separation.py`
- `tests/test_mixed_prevalence_rank_two_flattening_separation.py`
- `docs/proposition_91_mixed_prevalence_rank_two_flattening_separation.md`

---

## Scientific boundary

P91 is a conditional model-separation result for the declared P75 two-component four-view latent family and one established empirical witness.

It does not prove that the P75 latent variable is consciousness, that a failed P75 model implies nonphysical consciousness, that consciousness is an additional physical or mathematical dimension, or that any alternative consciousness theory is correct.

It also does not close the exact global-distance gap between the strict lower exclusion radius \(1/42\) and the explicit upper radius \(1/24\).

The physical-to-experiential bridge remains open.

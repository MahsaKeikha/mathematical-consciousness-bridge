# P90 Equation Provenance

## Scope

This note records the origin and status of the equations used in Proposition 90, the exact nonlinear rank-one slice separation theorem.

P90 is repository-original as a **specific exact certificate for the declared strict P75 box and established empirical witness**. The underlying determinant-zero property of a two-by-two slice of a product distribution is standard probability and algebraic-statistics structure and is not claimed as a new general mathematical identity.

---

## Equation record

| Equation or construction | Status | Provenance |
| --- | --- | --- |
| Single-component P75 factorization \(P(x_1,x_2,x_3,x_4)=\prod_j P(X_j=x_j\mid S=-1)\) when \(\pi_+=0\) | direct specialization of the P75 model | derived from the repository P75 four-view latent conditional-independence model |
| Canonical slice \((P(1000),P(1001),P(1010),P(1011))\) | P90 definition | repository-original choice of witness slice |
| Rank-one identity \(ad=bc\) | standard product-table identity | elementary consequence of factorization |
| Empirical slice \((1/8,1/24,0,5/24)\) | exact repository witness | direct extraction from the established 24-count empirical law |
| Determinant residual \(ad-bc=5/192\) | exact arithmetic | direct calculation from the empirical slice |
| Slice mass \(a+b+c+d=3/8\) | exact arithmetic | direct calculation from the empirical slice |
| Robustness inequality \((a-\varepsilon)(d-\varepsilon)\le(b+\varepsilon)(c+\varepsilon)\) | repository derivation | interval consequence of L-infinity perturbation plus rank one |
| Radius formula \(\varepsilon\ge(ad-bc)/(a+b+c+d)\) | repository derivation | expansion of the robustness inequality; quadratic terms cancel |
| Exact lower bound \(5/72\) | P90 exact certificate | substitution of \(5/192\) and \(3/8\) into the radius formula |
| Rational parameter point \((0,3/5,1/2,3/8,3/4,5/9,1/2,2/3,3/4)\) | P90 constructive certificate | repository search followed by exact rational verification |
| Model slice \((1/18,1/9,5/72,5/36)\) | exact evaluation | direct P75 model evaluation at the rational certificate point |
| Full-law upper radius \(5/72\) | exact evaluation | maximum absolute difference over all sixteen observable cells |
| Exact optimum \(L_{90}=5/72\) | Proposition 90 | equality of the exact lower and upper certificates |
| Improvement ratio \(L_{90}/L_{89}=7/3\) | exact comparison | \((5/72)/(5/168)=7/3\) |

---

## Why P90 is not implied by P89

P89 computes the complete support-function separation over every real linear functional of the eleven canonical parity coordinates. Equivalently, it closes the convex linear envelope seen by those observables.

The P90 determinant condition is quadratic:

\[
ad-bc=0.
\]

A point can satisfy every linear inequality of a convex hull while still fail a nonlinear algebraic identity obeyed by the underlying nonconvex model image. P90 uses exactly this distinction. Its strict witness distance \(5/72\) is larger than the P89 complete-linear value \(5/168\), proving that the nonlinear image contains additional certifiable structure not captured by the complete linear parity envelope.

---

## Exact arithmetic and implementation

The executable implementation uses `fractions.Fraction` throughout. No floating-point optimization is required for the published certificate.

The lower certificate is checked from the empirical four-cell slice and the exact determinant residual. The upper certificate evaluates one explicit rational P75 parameter point, verifies that it lies in the declared box, checks that the model slice determinant is exactly zero, and computes the exact L-infinity distance over all sixteen cells.

Files:

- `src/consciousness_bridge/exact_nonlinear_rank_one_separation.py`
- `tests/test_exact_nonlinear_rank_one_separation.py`
- `docs/proposition_90_exact_nonlinear_rank_one_separation.md`

---

## Scientific boundary

P90 is an exact model-separation theorem for one declared P75 parameter box whose prevalence is fixed at an extreme value, so the observable family reduces to one product component.

It does not establish a universal distance formula for every P75 parameter box. It does not identify the latent variable with consciousness, prove nonphysicality, establish an additional physical dimension, validate a replacement theory, or close the physical-to-experiential bridge.

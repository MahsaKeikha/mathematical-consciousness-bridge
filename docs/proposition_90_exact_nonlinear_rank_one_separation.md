# Proposition 90: Exact Nonlinear Rank-One Slice Separation

## Purpose

P89 closes the complete real linear parity-functional class on the eleven canonical P83 parity coordinates for the declared strict P75 parameter box. That result is exact for linear functionals, but it does not characterize the nonlinear P75 image itself.

P90 crosses that boundary for the first time in this branch of the program.

For the strict witness used from P83 through P89, the P75 prevalence coordinate is fixed at zero. The declared four-view latent model therefore reduces, on this box, to a single product Bernoulli law. Every two-by-two outcome slice obtained by fixing two views and varying the other two must consequently have matrix rank one. P90 exploits one such determinant constraint and proves the exact full-law L-infinity distance from the empirical witness to the declared P75 box.

The result is

\[
\boxed{
L_{90}=\frac{5}{72}.
}
\]

This is strictly stronger than the complete P89 linear parity optimum:

\[
\boxed{
L_{90}=\frac{7}{3}L_{89}
=\frac{5}{72}
>\frac{5}{168}=L_{89}.
}
\]

The gain is not obtained by searching a larger linear coefficient family. It comes from a genuinely nonlinear algebraic constraint of the model image.

---

## P90A. Single-component P75 boxes impose rank-one slices

Let the P75 four-view model have latent prevalence \(\pi_+\). On the strict box used by the current witness,

\[
\pi_+=0.
\]

The plus branch therefore has zero weight and the observable law factors as

\[
P(x_1,x_2,x_3,x_4)
=\prod_{j=1}^4 P(X_j=x_j\mid S=-1).
\]

Fix \((X_1,X_2)=(1,0)\) and vary \((X_3,X_4)\). Write the resulting two-by-two slice in lexicographic order as

\[
(a,b,c,d)
=
\bigl(
P(1000),
P(1001),
P(1010),
P(1011)
\bigr).
\]

Every product law satisfies

\[
\boxed{ad=bc.}
\]

This determinant-zero condition is nonlinear in the observable law and is not reducible to the complete linear support-function calculation closed by P89.

---

## P90B. Exact empirical determinant residual

For the established strict empirical count law

```text
(0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3) / 24
```

the canonical slice is

\[
(a,b,c,d)
=
\left(
\frac18,
\frac1{24},
0,
\frac5{24}
\right).
\]

Hence

\[
ad-bc
=
\frac18\frac5{24}-\frac1{24}0
=
\boxed{\frac5{192}}.
\]

The slice mass is

\[
a+b+c+d
=
\frac18+\frac1{24}+0+\frac5{24}
=
\boxed{\frac38}.
\]

---

## P90C. Exact L-infinity lower certificate

Suppose a rank-one nonnegative slice \((a',b',c',d')\) lies within L-infinity radius \(\varepsilon\) of the empirical slice. Because the empirical determinant has the orientation \(ad>bc\), any such slice must satisfy

\[
a'd'
\ge
(a-\varepsilon)(d-\varepsilon),
\]

and

\[
b'c'
\le
(b+\varepsilon)(c+\varepsilon).
\]

For rank one, these products must be equal. Therefore a necessary condition is

\[
(a-\varepsilon)(d-\varepsilon)
\le
(b+\varepsilon)(c+\varepsilon).
\]

Expanding both sides cancels the quadratic terms:

\[
ad-bc
\le
(a+b+c+d)\varepsilon.
\]

Thus every compatible model law obeys

\[
\varepsilon
\ge
\frac{ad-bc}{a+b+c+d}
=
\frac{5/192}{3/8}
=
\boxed{\frac5{72}}.
\]

The value \(5/72\) is below both positive factors \(a=1/8\) and \(d=5/24\), so the unclipped interval argument is valid exactly as written.

Because L-infinity distance on the complete sixteen-cell law dominates L-infinity distance on any selected four-cell slice, this is a valid full-law lower bound for every P75 model law in the strict box.

---

## P90D. Matching exact rational upper certificate

Consider the exact P75 parameter vector

\[
\left(
0,
\frac35,\frac12,
\frac38,\frac34,
\frac59,\frac12,
\frac23,\frac34
\right).
\]

It lies inside the declared strict P75 box. Since \(\pi_+=0\), only the minus-branch response probabilities affect the observable law.

At this parameter point the canonical slice is

\[
\left(
\frac1{18},
\frac19,
\frac5{72},
\frac5{36}
\right),
\]

and indeed

\[
\frac1{18}\frac5{36}
=
\frac19\frac5{72},
\]

so the slice determinant is exactly zero.

Direct exact evaluation of all sixteen observable cells gives

\[
\left\|P_{\mathrm{emp}}-P_{\mathrm{model}}\right\|_\infty
=
\boxed{\frac5{72}}.
\]

Therefore the lower and upper certificates match.

---

## P90E. Exact nonlinear distance theorem

Combining P90C and P90D gives

\[
\boxed{
\inf_{P\in\mathcal M_{75}(B_{\mathrm{strict}})}
\left\|P_{\mathrm{emp}}-P\right\|_\infty
=
\frac5{72}.
}
\]

P89 proved that no real linear functional of the eleven canonical parity coordinates can certify more than

\[
\frac5{168}.
\]

P90 proves that the actual nonlinear model image is farther away:

\[
\frac{5/72}{5/168}
=
\boxed{\frac73}.
\]

This is the first result in this chain where a nonlinear algebraic constraint strictly exceeds the complete linear parity-functional envelope already closed by P89.

---

## What P90 establishes

P90 establishes, for the declared strict P75 parameter box and the established exact empirical witness:

1. the model image is subject to a determinant-zero rank-one slice constraint because the prevalence is fixed to one latent component;
2. the empirical canonical slice violates that constraint by exactly \(5/192\);
3. every compatible P75 model law is at full-law L-infinity distance at least \(5/72\);
4. one explicit rational parameter point in the box attains exactly \(5/72\);
5. the exact nonlinear distance is therefore \(5/72\); and
6. this exact nonlinear certificate is \(7/3\) times the complete P89 linear certificate.

---

## What P90 does not establish

P90 does **not** show that every P75 box has a single-component rank-one structure. The theorem explicitly uses the current strict box, whose prevalence coordinate is fixed at zero.

It also does not show that the latent variable is consciousness, that consciousness is nonphysical, that consciousness is an additional dimension, or that rejection of the declared target-measurement family validates any alternative theory.

The physical-to-experiential bridge remains open.

---

## Reproducibility record

- Implementation: `src/consciousness_bridge/exact_nonlinear_rank_one_separation.py`
- Exact tests: `tests/test_exact_nonlinear_rank_one_separation.py`
- Equation provenance: `docs/p90_equation_provenance.md`
- Previous frontier: [P89 complete linear parity-functional duality](proposition_89_complete_linear_parity_duality.md)

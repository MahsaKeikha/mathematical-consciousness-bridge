# Proposition 93: Selective Finite-Sample Sign-Coherence Rejection

## Purpose

P92 proves an exact population obstruction for the complete P75 family. On the observable `X1 = 1` subtensor, three selected two-by-two determinants of every P75 law have a nonnegative product, while the established empirical witness has signs

\[
(-,+,+).
\]

P92 therefore closes the population model-distance problem exactly:

\[
d_\infty(P_{\mathrm{emp}},\mathcal M_{75})=\frac1{24}.
\]

P93 asks a different question:

> When can finite data certify the P92 sign-coherence contradiction directly, without spending confidence on all sixteen observable cells?

The answer uses exactly the seven distinct cells that enter the P92 minors. Each selected cell receives a confidence budget fixed independently of the table being tested. P79 supplies a certified rational Hoeffding radius for each budget, and exact interval arithmetic propagates the simultaneous cell box through the three determinants.

The result is a finite-sample rejection theorem specialized to the nonlinear P92 invariant.

---

## P93A. The seven-cell witness set

Inside the `X1 = 1` subtensor write

\[
A=X_2,\qquad B=X_3,\qquad C=X_4,
\]

and denote the subtensor cells by

\[
t_{abc}=P(X_1=1,A=a,B=b,C=c).
\]

The three P92 minors are

\[
D_1=D_{AB\mid C=1}
=
\det
\begin{pmatrix}
t_{001}&t_{011}\\t_{101}&t_{111}\end{pmatrix},
\]

\[
D_2=D_{AC\mid B=0}
=
\det
\begin{pmatrix}
t_{000}&t_{001}\\t_{100}&t_{101}\end{pmatrix},
\]

and

\[
D_3=D_{BC\mid A=0}
=
\det
\begin{pmatrix}
t_{000}&t_{001}\\t_{010}&t_{011}\end{pmatrix}.
\]

Only seven distinct cells occur:

\[
\boxed{
\mathcal S
=
\{t_{000},t_{001},t_{010},t_{011},t_{100},t_{101},t_{111}\}.
}
\]

The unused eighth `X1 = 1` cell and all eight `X1 = 0` cells are irrelevant to this particular nonlinear certificate.

---

## P93B. Fixed selective confidence allocation

Let \(\widehat p_x\) be the empirical frequency of selected cell \(x\in\mathcal S\) from \(n\) IID observations.

Choose positive rational error budgets

\[
\alpha_x>0,
\qquad
\sum_{x\in\mathcal S}\alpha_x\le\alpha,
\]

with the allocation fixed independently of the random table to which the test is applied.

For one selected cell, its indicator is Bernoulli. Hoeffding's inequality gives

\[
P\!\left(
|\widehat p_x-p_x|>r_x
\right)
\le
\alpha_x
\]

for

\[
r_x
=
\sqrt{
\frac{\log(2/\alpha_x)}{2n}
}.
\]

P79 replaces the transcendental value by a mathematically certified rational upper envelope

\[
\boxed{
r_x\le \overline r_x,}
\]

so every comparison used by P93 can be performed with exact rational arithmetic.

By a union bound, with probability at least

\[
1-\sum_{x\in\mathcal S}\alpha_x
\ge
1-\alpha,
\]

all seven population cells lie simultaneously in

\[
I_x
=
[\ell_x,u_x]
=
\left[
\max\{0,\widehat p_x-\overline r_x\},
\min\{1,\widehat p_x+\overline r_x\}
\right].
\]

No independence among the seven cell indicators is required for this union-bound step.

---

## P93C. Exact determinant image of a nonnegative interval box

Consider one determinant

\[
D=ad-bc
\]

with

\[
a\in[a_L,a_U],\quad
b\in[b_L,b_U],\quad
c\in[c_L,c_U],\quad
d\in[d_L,d_U],
\]

and all interval endpoints nonnegative.

On the nonnegative orthant, \(ad-bc\) is increasing in \(a,d\) and decreasing in \(b,c\). Therefore its exact interval image over the rectangular cell box is

\[
\boxed{
D\in
\left[
a_Ld_L-b_Uc_U,
      a_Ud_U-b_Lc_L
\right].
}
\]

Thus:

\[
a_Ud_U-b_Lc_L<0
\quad\Longrightarrow\quad
D<0,
\]

and

\[
a_Ld_L-b_Uc_U>0
\quad\Longrightarrow\quad
D>0.
\]

P93 applies these exact bounds separately to the three P92 minors.

---

## P93D. Finite-sample P75 rejection theorem

Let

\[
[L_j,U_j]
\]

be the exact determinant interval obtained from the seven simultaneous cell intervals for \(D_j\), \(j=1,2,3\).

If

\[
\boxed{
U_1<0,
\qquad
L_2>0,
\qquad
L_3>0,
}
\]

then on the simultaneous confidence event the population determinants have forced signs

\[
(-,+,+),
\]

so

\[
D_1D_2D_3<0.
\]

P92 proves that every law in the complete P75 family satisfies

\[
D_1D_2D_3\ge0.
\]

Therefore the P75 family is excluded whenever the P93 interval gate fires.

Because the gate can be wrong only if at least one of the seven selected cell confidence statements fails,

\[
\boxed{
P(\text{false P75 rejection})
\le
\sum_{x\in\mathcal S}\alpha_x
\le
\alpha.
}
\]

This is a direct finite-sample version of the P92 nonlinear obstruction.

---

## P93E. The current n = 24 witness is not certified

For the established empirical count law

```text
(0, 1, 0, 2, 0, 2, 1, 3, 3, 1, 0, 5, 0, 3, 0, 3) / 24
```

the seven selected empirical cells are

\[
\left(
\frac18,
\frac1{24},
0,
\frac5{24},
0,
\frac18,
\frac18
\right)
\]

in the order

\[
(t_{000},t_{001},t_{010},t_{011},t_{100},t_{101},t_{111}).
\]

The empirical determinants remain exactly

\[
\left(-\frac1{48},\frac1{64},\frac5{192}\right).
\]

At \(n=24\), however, the certified cell intervals are too wide to force any of the three determinant signs. P93 therefore returns

```text
forced signs = (0, 0, 0)
P75 rejection = false
```

where `0` means that the determinant interval contains zero.

This refusal is scientifically important. The exact P92 population geometry does not by itself turn a 24-observation empirical table into a finite-sample rejection claim.

---

## P93F. A transparent seven-cell 95 percent replication design

Take

\[
\alpha=\frac1{20}
\]

and split the familywise budget uniformly across the seven selected cells:

\[
\boxed{
\alpha_x=\frac1{140}
\quad\text{for every }x\in\mathcal S.
}
\]

Consider a prospective replicated table with the same exact proportions as the established 24-observation witness. Because the denominator is 24, compatible replication sizes are multiples of 24.

The exact P79 and P93 computation certifies

\[
\boxed{
n=1632
\quad\Longrightarrow\quad
(U_1<0,\ L_2>0,\ L_3>0),
}
\]

so the forced determinant signs are

\[
(-,+,+)
\]

and P75 is rejected at familywise confidence at least 95 percent.

This design uses only the cells needed by the nonlinear P92 witness. It is not the same as applying one common radius to all sixteen observable cells.

---

## P93G. A prospectively declared unequal allocation

The seven cells do not contribute equally to the determinant margins. P93 therefore also permits unequal error budgets, provided they are fixed before the new table is observed.

For the replication design recorded with this proposition, use

```text
t000 : 1/50000
t001 : 173/10000
t010 : 1/100000000
t011 : 81/10000
t100 : 1/50000
t101 : 169/10000
t111 : 765999/100000000
```

These seven positive rational budgets sum exactly to

\[
\frac1{20}.
\]

For a future replicated table having the same exact proportions as the fixed P92 witness, exact certification gives

\[
\boxed{
n=1464
\quad\Longrightarrow\quad
\text{forced signs }(-,+,+),
}
\]

while the same declared allocation at

\[
n=1440
\]

does not certify the negative first determinant.

P93 does not claim that this allocation is globally sample-optimal. It is an explicit prospective allocation with an exact machine-checked guarantee.

---

## P93H. Comparison with the direct full-law P77 route

A direct use of P77 with all sixteen observable cells and the exact P92 margin

\[
\tau=\frac1{24}
\]

requires

\[
\sqrt{
\frac{\log(32/\alpha)}{2n}
}
<
\frac1{24}.
\]

At \(\alpha=1/20\), this is

\[
\boxed{
n>288\log(640).}
\]

For replicated tables constrained to multiples of 24, the first compatible size clearing this direct full-law condition is

\[
1872.
\]

The P93 uniform seven-cell certificate fires at 1632, and the declared unequal prospective allocation fires at 1464.

This comparison is specifically against the direct sixteen-cell P77 use of the P92 margin. It is not a claim that P93 dominates every other finite-sample or projected-event certificate in the repository.

---

## What P93 establishes

P93 establishes that:

1. the nonlinear P92 obstruction depends on exactly seven distinct observable cells;
2. fixed per-cell error budgets can be combined with P79 certified rational Hoeffding radii;
3. the exact determinant image of the resulting nonnegative interval box is available in closed form;
4. forced determinant signs `(-,+,+)` give a finite-sample P75 rejection with familywise error at most the declared alpha budget;
5. the current `n=24` witness is not certified by this gate;
6. uniform seven-cell 95 percent allocation certifies the exact replicated witness at `n=1632`; and
7. one explicitly declared prospective unequal allocation certifies it at `n=1464` while refusing at `n=1440`.

---

## What P93 does not establish

P93 is a finite-sample rejection theorem for one declared latent-variable model family and one declared nonlinear diagnostic.

It does not identify the latent state with consciousness, prove that consciousness is nonphysical, establish consciousness as an additional dimension, validate a replacement ontology, or turn failure to reject into evidence that P75 is true.

The physical-to-experiential bridge remains open.

---

## Reproducibility record

- Implementation: `src/consciousness_bridge/selective_sign_coherence_rejection.py`
- Exact tests: `tests/test_selective_sign_coherence_rejection.py`
- Equation provenance: `docs/p93_equation_provenance.md`
- Population predecessor: [P92 exact global mixed-prevalence distance](proposition_92_exact_global_mixed_prevalence_distance.md)
- Sampling-radius predecessor: [P79 certified sampling radius](proposition_79_certified_sampling_radius.md)
- Generic full-law predecessor: [P77 full-law model-set separation](proposition_77_full_law_model_set_separation.md)

# P93 Equation Provenance

This record traces the equations used by Proposition 93 to earlier proved repository results and to the new interval step introduced at P93.

## 1. Population sign-coherence constraint

Source: P92.

For the three selected minors on the `X1 = 1` subtensor,

\[
D_1D_2D_3\ge0
\]

for every law in the complete P75 family.

The established empirical witness has

\[
(D_1,D_2,D_3)
=
\left(-\frac1{48},\frac1{64},\frac5{192}\right).
\]

Implementation source:

`src/consciousness_bridge/exact_global_mixed_prevalence_distance.py`

Formal record:

`docs/proposition_92_exact_global_mixed_prevalence_distance.md`

## 2. Selected-cell Hoeffding radius

For one selected cell `x`, let its empirical indicator mean be \(\widehat p_x\). The two-sided Hoeffding event uses

\[
r_x
=
\sqrt{
\frac{\log(2/\alpha_x)}{2n}
}.
\]

P79 supplies exact rational lower and upper certificates for the logarithm and square root. P93 uses only the certified upper endpoint

\[
\overline r_x\ge r_x.
\]

Implementation source:

`src/consciousness_bridge/certified_sampling_radius.py`

Formal record:

`docs/proposition_79_certified_sampling_radius.md`

## 3. Simultaneous seven-cell event

P93 assigns fixed positive budgets \(\alpha_x\) to the seven cells

\[
\mathcal S
=
\{t_{000},t_{001},t_{010},t_{011},t_{100},t_{101},t_{111}\}
\]

with

\[
\sum_{x\in\mathcal S}\alpha_x\le\alpha.
\]

A union bound gives

\[
P\left(
\forall x\in\mathcal S:
|\widehat p_x-p_x|\le\overline r_x
\right)
\ge
1-\sum_{x\in\mathcal S}\alpha_x
\ge
1-\alpha.
\]

This step does not require the selected cell indicators to be mutually independent.

## 4. Clipped population intervals

For each selected cell,

\[
I_x=[\ell_x,u_x]
\]

with

\[
\ell_x
=
\max\{0,\widehat p_x-\overline r_x\},
\qquad
u_x
=
\min\{1,\widehat p_x+\overline r_x\}.
\]

The clipping uses only the probability constraints \(0\le p_x\le1\).

## 5. Exact determinant interval

P93 introduces the following direct interval image.

For

\[
D=ad-bc
\]

on a nonnegative rectangular box

\[
a\in[a_L,a_U],
\quad
b\in[b_L,b_U],
\quad
c\in[c_L,c_U],
\quad
d\in[d_L,d_U],
\]

monotonicity on the nonnegative orthant gives

\[
\boxed{
D_{\min}=a_Ld_L-b_Uc_U,
\qquad
D_{\max}=a_Ud_U-b_Lc_L.
}
\]

This is exact for the rectangular interval relaxation because the lower and upper extrema occur at corners that can be chosen simultaneously.

Implementation source:

`src/consciousness_bridge/selective_sign_coherence_rejection.py`

Regression source:

`tests/test_selective_sign_coherence_rejection.py`

## 6. P93 rejection implication

If the three determinant intervals satisfy

\[
U_1<0,
\qquad
L_2>0,
\qquad
L_3>0,
\]

then on the simultaneous confidence event

\[
D_1D_2D_3<0.
\]

This contradicts the universal P92 P75 condition

\[
D_1D_2D_3\ge0.
\]

Therefore the probability of a false P75 rejection is at most

\[
\sum_{x\in\mathcal S}\alpha_x
\le
\alpha.
\]

## 7. Uniform 95 percent allocation

P93's transparent default uses

\[
\alpha=\frac1{20},
\qquad
\alpha_x=\frac1{140}
\]

for all seven selected cells.

For the exact replicated P92 proportions, the exact-rational implementation verifies forced signs

\[
(-,+,+)
\]

at

\[
n=1632.
\]

## 8. Prospective unequal 95 percent allocation

The recorded unequal design is

\[
\begin{aligned}
\alpha_{000}&=1/50000,\\
\alpha_{001}&=173/10000,\\
\alpha_{010}&=1/100000000,\\
\alpha_{011}&=81/10000,\\
\alpha_{100}&=1/50000,\\
\alpha_{101}&=169/10000,\\
\alpha_{111}&=765999/100000000.
\end{aligned}
\]

Exact rational addition gives

\[
\sum_x\alpha_x=\frac1{20}.
\]

For a future replication table with the fixed P92 proportions, the implementation verifies

\[
n=1464
\quad\Longrightarrow\quad
(-,+,+)
\]

while

\[
n=1440
\]

does not force the negative first determinant.

This allocation is a prospective design declaration. P93 does not claim global sample-size optimality for it.

## 9. Direct P77 comparison

P77 uses one common full-law cell radius over all \(K=16\) observable cells:

\[
\varepsilon_{n,16}(\alpha)
=
\sqrt{
\frac{\log(32/\alpha)}{2n}
}.
\]

Substituting the exact P92 population distance

\[
\tau=\frac1{24}
\]

and \(\alpha=1/20\) gives the direct sufficient condition

\[
\sqrt{
\frac{\log(640)}{2n}
}
<
\frac1{24},
\]

or equivalently

\[
\boxed{
n>288\log(640).}
\]

The P79 certified implementation verifies that the full sixteen-cell radius is still above \(1/24\) at `n=1464` and is below \(1/24\) at `n=1872`.

This comparison concerns the direct P77 use of the P92 distance only. It does not establish dominance over every other finite-sample certificate in the project.

## 10. Scientific boundary

P93 converts one declared nonlinear model obstruction into a finite-sample rejection gate. It does not identify consciousness, establish nonphysicality, validate another ontology, or close the physical-to-experiential bridge.

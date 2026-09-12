# Proposition 84: Exact Coupled Projection-Parity Certificate for Continuous P75 Separation

## Status

**Proved conditional computational theorem.** P84 strengthens the P83 exact projection-parity certificate for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P83 computes the exact parameter-box interval of each parity probability separately. P84 asks a stricter question: can two parity observables be realized by one common assignment of the response parameters? It answers this by certifying exact intervals for signed differences of two even-parity probabilities.

P84 is a model-distance certification result. It does not establish that the P75 latent state is consciousness, does not validate the P75 model when rejection fails, and does not close the physical-to-experiential bridge.

---

## 1. The compatibility gap left by P83

For a nontrivial view set $J$, define the even-parity event

\[
E_J
=
\left\{
x\in\{0,1\}^4:
\bigoplus_{j\in J}x_j=0
\right\}.
\]

P83 computes the exact scalar interval

\[
P(E_J)\in I_J(B)
\]

for every P78 parameter box $B$ and tests whether the empirical value belongs to that interval.

That test is exact for one observable, but separate scalar compatibility does not imply joint parameter compatibility. An endpoint assignment that realizes an extreme of $P(E_J)$ need not be the endpoint assignment that realizes an extreme of $P(E_K)$.

P84 retains that shared-parameter information for every pair of nontrivial parity view sets.

---

## 2. Coupled parity contrast

For two distinct nontrivial view sets $J$ and $K$, define

\[
\boxed{
D_{J,K}
=
P(E_J)-P(E_K).
}
\]

Inside latent branch $s\in\{-,+\}$, write

\[
a_{j,s}=1-2q_{j,s}.
\]

The P83 parity identity gives

\[
P_s(E_J)
=
\frac{1+\prod_{j\in J}a_{j,s}}{2}
\]

and

\[
P_s(E_K)
=
\frac{1+\prod_{j\in K}a_{j,s}}{2}.
\]

Subtracting cancels the constant terms:

\[
\boxed{
D_{J,K,s}
=
\frac12
\left(
\prod_{j\in J}a_{j,s}
-
\prod_{j\in K}a_{j,s}
\right).
}
\]

The two products are not extremized independently. They are evaluated on the same response-coordinate assignment.

---

## 3. Exact common-endpoint branch interval

Let

\[
U=J\cup K.
\]

For each $j\in U$ in branch $s$, the transformed response coordinate satisfies

\[
a_{j,s}
\in
[1-2u_{j,s},1-2\ell_{j,s}].
\]

Define

\[
F_{J,K,s}(a_U)
=
\frac12
\left(
\prod_{j\in J}a_{j,s}
-
\prod_{j\in K}a_{j,s}
\right).
\]

Every coordinate $a_{j,s}$ appears with degree at most one in $F_{J,K,s}$. Therefore $F_{J,K,s}$ is multi-affine on the rectangular union box.

A multi-affine function on a rectangular box attains its extrema at vertices. Hence

\[
\boxed{
[d_{s}^{L},d_{s}^{U}]
=
\left[
\min_{v\in V_U}F_{J,K,s}(v),
\max_{v\in V_U}F_{J,K,s}(v)
\right]
}
\]

is the exact branchwise interval.

Because $|U|\le4$, at most

\[
2^4=16
\]

common endpoint assignments are required per branch.

This is the central P84 step: the left and right parity products are evaluated at the same endpoint vertex, preserving the parameter coupling discarded by subtracting two independently computed P83 intervals.

---

## 4. Exact latent-mixture contrast interval

The full P75 parity contrast is

\[
D_{J,K}(\theta)
=
(1-\pi)D_{J,K,-}+\pi D_{J,K,+}.
\]

The minus-branch response coordinates, plus-branch response coordinates, and prevalence are disjoint coordinates of the P75 parameter box. Therefore the exact branch minima can be attained simultaneously, as can the exact branch maxima.

For

\[
\pi\in[\pi_L,\pi_U],
\]

the exact lower envelope is

\[
L(\pi)
=
(1-\pi)d_-^L+\pi d_+^L,
\]

and the exact upper envelope is

\[
U(\pi)
=
(1-\pi)d_-^U+\pi d_+^U.
\]

Both are affine in prevalence. Consequently,

\[
\boxed{
\ell_{J,K}(B)
=
\min_{\pi\in\{\pi_L,\pi_U\}}L(\pi),
}
\]

\[
\boxed{
u_{J,K}(B)
=
\max_{\pi\in\{\pi_L,\pi_U\}}U(\pi).
}
\]

Thus P84 computes the exact scalar image interval of the coupled parity contrast over the complete declared P75 parameter box.

---

## 5. Transfer to full-law $L_\infty$ distance

Let

\[
c_x
=
\mathbf 1_{E_J}(x)-\mathbf 1_{E_K}(x).
\]

Then

\[
D_{J,K}(p)-D_{J,K}(q)
=
\sum_x c_x(p_x-q_x).
\]

Therefore

\[
|D_{J,K}(p)-D_{J,K}(q)|
\le
\left(\sum_x|c_x|\right)
\|p-q\|_\infty.
\]

For distinct nonzero parity forms on four binary variables, $E_J$ and $E_K$ each contain eight cells and their intersection contains four cells. Their symmetric difference therefore contains eight cells. Hence

\[
\boxed{
\sum_x|c_x|=8.
}
\]

It follows that every P75 law generated inside $B$ satisfies

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\widehat D_{J,K},
[\ell_{J,K}(B),u_{J,K}(B)]
\right)
}{8}.
}
\]

---

## 6. The finite P84 family

P83 has 11 nontrivial view sets when parity complements are identified:

\[
{4\choose2}+{4\choose3}+{4\choose4}
=6+4+1
=11.
\]

P84 uses every unordered pair of distinct sets:

\[
\boxed{
|\mathcal C_{84}|
={11\choose2}
=55.
}
\]

Define

\[
\boxed{
L_{\mathrm{cpar}}(B)
=
\max_{\{J,K\}\in\mathcal C_{84}}
\frac{
d\!\left(
\widehat D_{J,K},
[\ell_{J,K}(B),u_{J,K}(B)]
\right)
}{8}.
}
\]

The family is finite, exact, and small enough to audit exhaustively.

---

## 7. P84 theorem

For every admissible P78 parameter box $B$, define

\[
\boxed{
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{cpar}}(B)\}.
}
\]

Then:

1. $L_{84}(B)$ is a rigorous lower bound on the $L_\infty$ distance from $\widehat p$ to every P75 law generated inside $B$;
2. $L_{84}(B)\ge L_{83}(B)\ge L_{82}(B)\ge L_{81}(B)\ge L_{80}(B)\ge L_{78}(B)$;
3. every P84 branchwise parity-contrast interval is exact over the declared response-coordinate box;
4. every P84 latent-mixture contrast interval is exact over the complete declared P75 box;
5. the exactness uses one common endpoint assignment for both parity products in each latent branch;
6. every interval endpoint and every P84 lower bound is rational when the empirical law and parameter-box endpoints are rational;
7. for any finite partition $\mathcal B$ of the complete P75 parameter cube,

\[
\boxed{
L_{84}(\mathcal B)
:=
\min_{B\in\mathcal B}L_{84}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2});
}
\]

8. on the same partition,

\[
\boxed{
L_{84}(\mathcal B)\ge L_{83}(\mathcal B);
}
\]

9. explicit P75 parameter vectors remain valid global upper-bound witnesses;
10. the previously proved P78 mesh-width upper certificate remains valid and is retained unchanged. P84 does not assume a new convergence-rate theorem.

---

## 8. Proof

### 8.1 Exact branch interval

The branch contrast

\[
F_{J,K,s}(a_U)
=
\frac12
\left(
\prod_{j\in J}a_{j,s}
-
\prod_{j\in K}a_{j,s}
\right)
\]

is multi-affine in the union coordinates $a_U$. Repeatedly fixing all but one coordinate shows that an extremum in that coordinate occurs at an endpoint. Applying this coordinate by coordinate moves an extremizer to a box vertex without worsening its value. Vertex enumeration therefore gives the exact branch minimum and maximum.

### 8.2 Exact mixture interval

Minus-branch and plus-branch response coordinates are disjoint. Their exact minima can be attained simultaneously, and likewise for their maxima. With those branch extrema fixed, the mixture contrast is affine in prevalence. Its exact extrema therefore occur at $\pi_L$ or $\pi_U$.

### 8.3 Signed-support inequality

For coefficient vector $c_x\in\{-1,0,1\}$,

\[
\left|\sum_xc_x(\widehat p_x-q_x)\right|
\le
\sum_x|c_x|\,\|\widehat p-q\|_\infty.
\]

For two distinct parity forms, the coefficient support has size eight, so empirical contrast separation divided by eight is a valid full-law lower bound.

### 8.4 Dominance

P83 is already sound. Taking the maximum of the P83 lower bound and the new sound contrast lower bound immediately yields

\[
L_{84}(B)\ge L_{83}(B).
\]

### 8.5 Exact arithmetic

The implementation uses only `fractions.Fraction`, finite endpoint enumeration, multiplication, subtraction, affine mixing, maxima, minima, and division by the integer eight. Rational inputs remain exact throughout.

---

## 9. Exact strict-improvement witness over P83

The repository includes an exact rational witness designed to expose the shared-parameter compatibility gap.

Fix prevalence to

\[
\pi=0,
\]

so only the minus branch contributes. Use the response intervals

\[
q_{1,-}\in\left[\frac14,\frac34\right],
\qquad
q_{2,-}\in\left[\frac14,\frac34\right],
\]

\[
q_{3,-}\in\left[0,\frac12\right],
\qquad
q_{4,-}\in\left[\frac14,\frac34\right].
\]

The plus-branch response coordinates may remain unrestricted because their prevalence weight is zero.

The exact empirical law, in lexicographic binary outcome order $0000,0001,\ldots,1111$, is

\[
\widehat p
=
\frac1{640}
(
9,
47,
10,
10,
97,
83,
84,
16,
11,
49,
10,
50,
19,
5,
44,
96
).
\]

These masses are nonnegative and sum exactly to one.

The exhaustive exact-rational audit gives

\[
\boxed{
L_{81}(B)=L_{82}(B)=L_{83}(B)=0.
}
\]

Thus every P81 cylinder, every P82 nested residual, and every P83 parity marginal is individually compatible with its exact P75 box interval.

Now select

\[
J=\{1,4\},
\qquad
K=\{1,3,4\}.
\]

The empirical contrast is

\[
\boxed{
\widehat D_{J,K}=\frac14.
}
\]

Exact common-endpoint enumeration of the P75 box gives

\[
\boxed{
D_{J,K}(B)
\in
\left[-\frac18,\frac18\right].
}
\]

Therefore the empirical distance to the complete feasible contrast interval is

\[
\frac14-\frac18
=
\frac18.
\]

The signed contrast has eight nonzero cell coefficients, so

\[
L_{\mathrm{cpar}}(B)
\ge
\frac{1/8}{8}
=
\boxed{\frac1{64}}.
\]

The complete standard P84 family confirms this is the strongest contrast witness on the box. Hence

\[
\boxed{
L_{84}(B)=\frac1{64}>0=L_{83}(B).
}
\]

This strict witness is important because it isolates the exact information added by P84: all earlier observables can be separately feasible while two parity summaries cannot be produced together by one shared P75 response-parameter assignment.

---

## 10. Global branch-and-bound handoff

P84 replaces the P83 box lower bound inside the same exact-rational branch-and-bound architecture. Active boxes continue to partition the complete nine-dimensional P75 parameter cube, and the global lower certificate is the minimum active P84 box bound.

For the upper direction, the established certificates remain unchanged:

- every explicit P75 parameter vector gives a valid global model-distance upper bound;
- the P78 mesh-width upper certificate remains valid because the underlying model-distance problem is unchanged.

P84 does not claim an independent convergence-rate theorem for the new contrast lower bound.

---

## 11. P79 finite-data rejection handoff

Let $\overline\varepsilon_{79}$ be the certified rational upper envelope for the P77 cellwise sampling radius supplied by P79. Then

\[
\boxed{
L_{84}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
\mathcal C_n(\widehat p)\cap\mathcal M_{4,2}=\varnothing.
}
\]

This remains a one-sided rejection statement. If the strict inequality does not hold, the result is inconclusive. It is not evidence that the P75 family is true.

---

## 12. What P84 does and does not establish

P84 establishes a sharper exact lower certificate for one declared continuous latent-variable model family. It demonstrates a concrete distinction between separate observable compatibility and common-parameter compatibility.

It does **not** establish:

- that the P75 latent variable is a conscious state;
- that parity or parity contrast is a measure of consciousness;
- that P75 is the unique or correct target model;
- that rejection of P75 implies nonphysical consciousness;
- that non-rejection validates P75;
- that quantum mechanics is required for the bridge;
- that the physical-to-experiential bridge has been solved.

The physical-to-experiential bridge remains open.

---

## 13. Executable objects

Implementation:

- `src/consciousness_bridge/coupled_projection_parity_separation.py`

Primary public objects:

- `P84ParityContrastWitness`
- `P84DistanceBracket`
- `p84_standard_parity_contrast_count`
- `p84_projection_parity_contrast_support_size`
- `p75_projection_parity_contrast_interval_exact`
- `empirical_projection_parity_contrast_exact`
- `p75_box_projection_parity_contrast_witness_exact`
- `p75_box_projection_parity_contrast_linf_lower_bound_exact`
- `p75_box_p84_linf_lower_bound_exact`
- `p84_dominates_p83_on_box`
- `certified_p75_linf_branch_and_bound_coupled_parity`
- `p84_rejection_with_p79_radius`

Tests:

- `tests/test_coupled_projection_parity_separation.py`

Equation provenance:

- `docs/p84_equation_provenance.md`

The exact P83-zero/P84-positive witness is executable directly from the test suite.

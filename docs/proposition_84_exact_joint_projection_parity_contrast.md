# Proposition 84: Exact Joint Projection-Parity Contrast Certificate for Continuous P75 Separation

## Status

**Proved conditional computational theorem.** P84 strengthens the P83 exact projection-parity certificate for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P83 computes the exact parameter-box interval of each declared parity probability separately. P84 asks a stricter question: can two observed parity probabilities be realized simultaneously by one common assignment of the P75 response parameters? It answers this by computing exact signed contrasts between parity events built from different view sets.

P84 is a model-distance certification result. It does not identify the P75 latent state with consciousness, does not validate the P75 model when rejection fails, and does not close the physical-to-experiential bridge.

---

## 1. The shared-parameter compatibility gap left by P83

For a nontrivial view set $J\subseteq\{1,2,3,4\}$ and parity bit $b\in\{0,1\}$, define

\[
H(J,b)
=
\left\{
x\in\{0,1\}^4:
\bigoplus_{j\in J}x_j=b
\right\}.
\]

P83 computes an exact scalar interval

\[
P(H(J,b))\in I_{J,b}(B)
\]

for every P78 parameter box $B$.

Separate scalar compatibility does not imply common-parameter compatibility. One endpoint assignment can realize an extremum of one parity probability while a different endpoint assignment realizes an extremum of another. The pair can therefore pass both separate P83 interval tests even when no single P75 parameter assignment realizes their observed relationship.

P84 retains the shared response-coordinate structure through direct pairwise parity contrasts.

---

## 2. Coupled parity contrast

For two parity events

\[
H_1=H(J_1,b_1),
\qquad
H_2=H(J_2,b_2),
\]

with $J_1\ne J_2$, define

\[
\boxed{
C_{12}=P(H_1)-P(H_2).
}
\]

Inside latent branch $s\in\{-,+\}$, set

\[
a_{j,s}=1-2q_{j,s}.
\]

The P83 parity identity gives

\[
P_s(H(J,b))
=
\frac{1+(-1)^b\prod_{j\in J}a_{j,s}}{2}.
\]

Hence

\[
\boxed{
C_{12,s}
=
\frac12
\left[
(-1)^{b_1}\prod_{j\in J_1}a_{j,s}
-
(-1)^{b_2}\prod_{j\in J_2}a_{j,s}
\right].
}
\]

The two products are evaluated at the same response-coordinate assignment.

---

## 3. Exact common-endpoint branch interval

Let

\[
U=J_1\cup J_2.
\]

For branch $s$, define

\[
F_s(a_U)
=
\frac12
\left[
(-1)^{b_1}\prod_{j\in J_1}a_{j,s}
-
(-1)^{b_2}\prod_{j\in J_2}a_{j,s}
\right].
\]

Each coordinate in $U$ appears with degree at most one, so $F_s$ is multi-affine on the transformed response-coordinate box. A multi-affine function on a rectangular box attains its extrema at vertices. Therefore

\[
\boxed{
[c_s^L,c_s^U]
=
\left[
\min_{v\in V_U}F_s(v),
\max_{v\in V_U}F_s(v)
\right]
}
\]

is the exact branchwise contrast interval.

Because there are only four observed views,

\[
|U|\le4,
\]

so at most

\[
2^4=16
\]

common endpoint assignments are required per branch.

This is the central P84 improvement: the two parity terms are extremized jointly over one common assignment instead of through independent scalar interval subtraction.

---

## 4. Exact latent-mixture contrast interval

The full P75 contrast is

\[
C_{12}(\theta)
=
(1-\pi)C_{12,-}+\pi C_{12,+}.
\]

The minus-branch response coordinates, plus-branch response coordinates, and prevalence are disjoint coordinates of the P75 parameter box. Consequently the exact branch minima can be attained simultaneously, as can the exact branch maxima.

For prevalence

\[
\pi\in[\pi_L,\pi_U],
\]

define

\[
L(\pi)
=(1-\pi)c_-^L+\pi c_+^L,
\]

\[
U(\pi)
=(1-\pi)c_-^U+\pi c_+^U.
\]

Both are affine in $\pi$, so

\[
\boxed{
\ell_{12}(B)
=
\min_{\pi\in\{\pi_L,\pi_U\}}L(\pi),
}
\]

\[
\boxed{
u_{12}(B)
=
\max_{\pi\in\{\pi_L,\pi_U\}}U(\pi).
}
\]

Thus P84 computes the exact scalar image interval of each declared coupled parity contrast over the complete P75 parameter box.

---

## 5. Transfer to full-law $L_\infty$ distance

Define the signed coefficient vector

\[
c_x
=
\mathbf 1_{H_1}(x)-\mathbf 1_{H_2}(x).
\]

Then

\[
C_{12}(p)-C_{12}(q)
=
\sum_x c_x(p_x-q_x).
\]

Therefore

\[
|C_{12}(p)-C_{12}(q)|
\le
\left(\sum_x|c_x|\right)
\|p-q\|_\infty.
\]

For two parity events built from different nonzero parity forms on four binary variables, the signed coefficient support has eight cells. Hence

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
\widehat C_{12},
[\ell_{12}(B),u_{12}(B)]
\right)
}{8}.
}
\]

---

## 6. The finite P84 family

P83 has 22 declared parity events: both parity values for each of the 11 nontrivial view sets of sizes two, three, and four.

P84 considers every unordered pair of those events whose view sets differ. Same-view complementary pairs are omitted because they are algebraic rewritings of one P83 probability rather than genuinely new shared-parameter constraints.

The standard P84 family therefore contains

\[
\boxed{220}
\]

genuinely coupled parity contrasts.

Define

\[
\boxed{
L_{\mathrm{joint-parity}}(B)
=
\max_{(H_1,H_2)\in\mathcal C_{84}}
\frac{
d\!\left(
\widehat C_{12},
[\ell_{12}(B),u_{12}(B)]
\right)
}{8}.
}
\]

The family is finite, exact, and exhaustively audited by the implementation.

---

## 7. P84 theorem

For every admissible P78 parameter box $B$, define

\[
\boxed{
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{joint-parity}}(B)\}.
}
\]

Then:

1. $L_{84}(B)$ is a rigorous lower bound on the $L_\infty$ distance from $\widehat p$ to every P75 law generated inside $B$;
2. $L_{84}(B)\ge L_{83}(B)\ge L_{82}(B)\ge L_{81}(B)\ge L_{80}(B)\ge L_{78}(B)$;
3. each branchwise P84 contrast interval is exact over the declared response-coordinate box;
4. each full P84 contrast interval is exact over the complete declared P75 box;
5. exactness uses one common endpoint assignment for both parity terms in each latent branch;
6. every interval endpoint and every P84 lower bound is rational whenever the empirical law and parameter-box endpoints are rational;
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
10. the previously proved P78 mesh-width upper certificate remains valid unchanged. P84 claims no new convergence-rate theorem.

---

## 8. Proof

### 8.1 Exact branch interval

The branch contrast $F_s$ is multi-affine in the union coordinates $a_U$. Fix all coordinates but one. The resulting function is affine in that coordinate, so an extremum occurs at an endpoint. Repeating this coordinate by coordinate moves an extremizer to a box vertex without weakening the extremal value. Therefore common endpoint enumeration gives the exact branch minimum and maximum.

### 8.2 Exact mixture interval

The two latent branches use disjoint response-coordinate sets. Their exact minima can be attained simultaneously, and likewise for their maxima. With those branch extrema fixed, the mixture contrast is affine in prevalence, so its extrema occur at the prevalence endpoints.

### 8.3 Signed-support inequality

For any laws $p$ and $q$,

\[
\left|\sum_x c_x(p_x-q_x)\right|
\le
\sum_x|c_x|\,\|p-q\|_\infty.
\]

The standard genuinely coupled parity pairs have eight nonzero signed coefficients. Dividing empirical contrast separation by eight therefore gives a sound full-law $L_\infty$ lower bound.

### 8.4 Dominance

P83 is already sound. Taking the maximum of the P83 lower bound and the new sound contrast lower bound immediately yields

\[
L_{84}(B)\ge L_{83}(B).
\]

### 8.5 Exact arithmetic

The implementation uses `fractions.Fraction`, finite endpoint enumeration, multiplication, subtraction, affine mixing, maxima, minima, and integer division. Rational inputs remain exact throughout.

---

## 9. Exact strict-improvement witness over P83

The regression suite contains an exact rational parameter box and empirical law for which the complete P83 certificate is zero:

\[
\boxed{L_{83}(B)=0.}
\]

For the named coupled parity pair

\[
H_1 = H(\{2,4\},0),
\qquad
H_2 = H(\{2,3,4\},1),
\]

the exact P75 box range is

\[
\boxed{
C_{12}(B)\in\left[0,\frac12\right].
}
\]

The empirical contrast is

\[
\boxed{
\widehat C_{12}=-\frac14.
}
\]

The empirical contrast therefore lies exactly

\[
\frac14
\]

outside the complete feasible contrast interval. Since the signed contrast has eight nonzero cell coefficients,

\[
L_{\mathrm{joint-parity}}(B)
\ge
\frac{1/4}{8}
=
\boxed{\frac1{32}}.
\]

The complete standard P84 family confirms that the strongest contrast witness on this box has lower bound $1/32$. Hence

\[
\boxed{
L_{84}(B)=\frac1{32}>0=L_{83}(B).
}
\]

This strict witness isolates the exact information added by P84: all P83 parity probabilities can be separately feasible while two of them cannot be realized together by one shared P75 response-parameter assignment.

---

## 10. Global branch-and-bound handoff

P84 replaces the P83 box lower bound inside the same exact-rational branch-and-bound architecture. Active boxes continue to partition the complete nine-dimensional P75 parameter cube, and the global lower certificate is the minimum active P84 box bound.

The upper direction is unchanged:

- every explicit P75 parameter vector gives a valid global model-distance upper bound;
- the P78 mesh-width upper certificate remains valid because the underlying model-distance problem is unchanged.

P84 does not claim an independent convergence-rate theorem for the new lower bound.

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

This remains a one-sided rejection statement. Failure of the strict inequality is inconclusive and is not evidence that P75 is true.

---

## 12. What P84 does and does not establish

P84 establishes a sharper exact lower certificate for one declared continuous latent-variable model family. It demonstrates a concrete distinction between separate observable compatibility and shared-parameter compatibility.

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

- `src/consciousness_bridge/joint_projection_parity_contrast_separation.py`

Primary public objects:

- `P84ParityContrastWitness`
- `P84DistanceBracket`
- `p84_standard_contrast_count`
- `p75_projection_parity_contrast_interval_exact`
- `empirical_projection_parity_contrast_exact`
- `parity_contrast_coefficient_support_size`
- `p75_box_projection_parity_contrast_witness_exact`
- `p75_box_projection_parity_contrast_linf_lower_bound_exact`
- `p75_box_p84_linf_lower_bound_exact`
- `p84_dominates_p83_on_box`
- `certified_p75_linf_branch_and_bound_parity_contrast`
- `p84_rejection_with_p79_radius`

Tests:

- `tests/test_joint_projection_parity_contrast_separation.py`

Equation provenance:

- `docs/p84_equation_provenance.md`

The exact P83-zero/P84-positive witness is executable directly from the regression suite.

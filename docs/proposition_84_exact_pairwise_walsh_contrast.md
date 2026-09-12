# Proposition 84: Exact Pairwise Walsh-Contrast Certificate for Continuous P75 Separation

## Status

**Proved conditional computational theorem.** P84 strengthens the P83 exact projection-parity certificate for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P83 tests each selected parity event separately. P84 retains shared parameter dependence between two Walsh parity characters by testing a finite family of signed pairwise contrasts. The resulting expectation is multi-affine inside each latent branch, so its complete rational parameter-box range is exactly computable by endpoint evaluation.

P84 is a model-distance certification result. It does not establish that the P75 latent state is consciousness, does not validate P75 when rejection fails, and does not close the physical-to-experiential bridge.

---

## 1. Why a contrast can reveal information missed by separate parity intervals

For a nonempty subset of observed views $J\subseteq\{1,2,3,4\}$, define the Walsh character

\[
\chi_J(x)=(-1)^{\sum_{j\in J}x_j}.
\]

The expectation $\mathbb E[\chi_J]$ is the even-minus-odd parity imbalance on $J$. P83 certifies exact box intervals for each such parity observable separately. That is sound, but separate intervals can discard a relation shared by two characters because their extrema may require incompatible values of the same P75 response parameters.

P84 therefore introduces, for distinct nonempty subsets $A$ and $B$ and $s\in\{-1,+1\}$,

\[
\boxed{
\phi_{A,B,s}(x)=\chi_A(x)+s\chi_B(x).
}
\]

The observable remains finite, exact, and predeclared, but it preserves one piece of cross-character parameter coupling that two independent interval checks can lose.

---

## 2. Exact branchwise Walsh identity

Within latent branch $t\in\{-,+\}$ the P75 model makes the selected binary views conditionally independent. For one Bernoulli variable,

\[
\mathbb E_t[(-1)^{X_j}]=1-2q_{j,t}.
\]

Therefore

\[
\boxed{
\mathbb E_t[\chi_J(X)]
=
\prod_{j\in J}(1-2q_{j,t}).
}
\]

and for one P84 contrast,

\[
\boxed{
\mathbb E_t[\phi_{A,B,s}(X)]
=
\prod_{j\in A}(1-2q_{j,t})
+s\prod_{j\in B}(1-2q_{j,t}).
}
\]

This is a multi-affine polynomial in the branch response coordinates that appear in $A\cup B$.

---

## 3. Exact rational parameter-box interval

Let $B_0$ be an axis-aligned P78 parameter box. For every active branch response coordinate,

\[
q_{j,t}\in[\ell_{j,t},u_{j,t}],
\qquad
1-2q_{j,t}\in[1-2u_{j,t},1-2\ell_{j,t}].
\]

Because the branch contrast expectation is multi-affine, its minimum and maximum on the response-coordinate rectangle occur at vertices. Hence finite endpoint enumeration gives the exact branch interval

\[
\mathbb E_-[\phi]\in[a_-^L,a_-^U],
\qquad
\mathbb E_+[\phi]\in[a_+^L,a_+^U].
\]

The two latent branches use disjoint response coordinates, so their branch extrema are jointly attainable. With prevalence

\[
\pi\in[\pi_L,\pi_U],
\]

the full P75 expectation is

\[
\mathbb E_q[\phi]
=(1-\pi)\mathbb E_-[\phi]+\pi\mathbb E_+[\phi].
\]

For fixed branch extrema this is affine in $\pi$. Therefore

\[
\boxed{
\ell_\phi(B_0)
=
\min_{\pi\in\{\pi_L,\pi_U\}}
\bigl[(1-\pi)a_-^L+\pi a_+^L\bigr],
}
\]

\[
\boxed{
u_\phi(B_0)
=
\max_{\pi\in\{\pi_L,\pi_U\}}
\bigl[(1-\pi)a_-^U+\pi a_+^U\bigr].
}
\]

Thus $[\ell_\phi(B_0),u_\phi(B_0)]$ is the exact image interval of the contrast expectation over the complete rational P75 parameter box, not merely a conservative enclosure.

---

## 4. Transfer from contrast mismatch to full-law $L_\infty$ distance

For any real-valued observable $\phi$ on the sixteen observed cells,

\[
\begin{aligned}
|\mathbb E_p\phi-\mathbb E_q\phi|
&=
\left|\sum_x\phi(x)(p_x-q_x)\right|\\
&\le
\sum_x|\phi(x)|\,|p_x-q_x|\\
&\le
\|p-q\|_\infty\sum_x|\phi(x)|.
\end{aligned}
\]

Define the discrete $L_1$ norm

\[
\|\phi\|_1=\sum_{x\in\{0,1\}^4}|\phi(x)|.
\]

Every P75 law generated in $B_0$ has its contrast expectation in the exact interval $[\ell_\phi(B_0),u_\phi(B_0)]$. Hence

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\mathbb E_{\widehat p}[\phi],
[\ell_\phi(B_0),u_\phi(B_0)]
\right)
}{\|\phi\|_1}.
}
\]

This is the P84 dual-observable lower certificate.

---

## 5. The finite P84 family

There are

\[
2^4-1=15
\]

nonconstant Walsh characters on four binary views. P84 takes every unordered pair of distinct characters and both relative signs. The predeclared family therefore contains

\[
\boxed{
2{15\choose2}=210
}
\]

signed pairwise contrasts.

For distinct Walsh characters $\chi_A$ and $\chi_B$, the ratio $\chi_A\chi_B=\chi_{A\triangle B}$ is nonconstant and balanced on the sixteen-cell cube. Therefore exactly eight cells have equal signs and eight have opposite signs. For either relative sign, $\phi$ is zero on eight cells and has magnitude two on eight cells, so

\[
\boxed{\|\phi_{A,B,s}\|_1=16.}
\]

The implementation computes this norm directly rather than relying on the closed form.

---

## 6. P84 theorem

Let $\mathcal W$ be the 210 predeclared pairwise signed Walsh contrasts and define

\[
\boxed{
L_{\mathrm{Walsh}}(B_0)
=
\max_{\phi\in\mathcal W}
\frac{
d\!\left(
\mathbb E_{\widehat p}[\phi],
[\ell_\phi(B_0),u_\phi(B_0)]
\right)
}{\|\phi\|_1}.
}
\]

Then define

\[
\boxed{
L_{84}(B_0)
=
\max\{L_{83}(B_0),L_{\mathrm{Walsh}}(B_0)\}.
}
\]

For every admissible rational P78 parameter box:

1. $L_{84}(B_0)$ is a rigorous lower bound on the full-law $L_\infty$ distance from $\widehat p$ to every P75 law generated inside $B_0$;
2. $L_{84}(B_0)\ge L_{83}(B_0)\ge L_{82}(B_0)\ge L_{81}(B_0)\ge L_{80}(B_0)\ge L_{78}(B_0)$;
3. every P84 branchwise contrast interval is exact over the declared response-coordinate box;
4. every full latent-mixture contrast interval is exact over the complete P75 box;
5. all interval endpoints and lower bounds are exactly rational for rational empirical laws and rational box endpoints;
6. for any finite partition $\mathcal B$ of the complete P75 parameter cube,

\[
\boxed{
L_{84}(\mathcal B)
:=
\min_{B_0\in\mathcal B}L_{84}(B_0)
\le
d_\infty(\widehat p,\mathcal M_{4,2});
}
\]

7. on the same partition $L_{84}(\mathcal B)\ge L_{83}(\mathcal B)$;
8. explicit P75 parameter vectors remain valid global upper-bound witnesses;
9. the already-proved P78 mesh-width upper certificate remains valid and is retained unchanged. P84 does not assert a new convergence-rate theorem.

---

## 7. Proof

### 7.1 Exact branch interval

The branch expectation is a sum of two products of affine coordinate functions. Each response coordinate occurs with degree at most one, so the expression is multi-affine. A multi-affine function on a rectangular box attains its extrema at vertices. Enumerating the response-coordinate endpoint choices therefore gives the exact branch interval.

### 7.2 Exact mixture interval

The minus-branch and plus-branch response coordinates are disjoint, so a minimizing minus-branch vertex and minimizing plus-branch vertex can be realized simultaneously; the same holds for the maxima. Prevalence is a separate coordinate and appears affinely. Checking $\pi_L$ and $\pi_U$ therefore gives the exact full-box interval.

### 7.3 Soundness

For any P75 law $q$ in the box,

\[
\mathbb E_q[\phi]\in[\ell_\phi,u_\phi].
\]

The Holder-type finite-alphabet bound

\[
|\mathbb E_{\widehat p}\phi-\mathbb E_q\phi|
\le
\|\widehat p-q\|_\infty\|\phi\|_1
\]

implies that empirical distance to the exact expectation interval, divided by $\|\phi\|_1$, lower-bounds full-law distance. Maximizing over a finite family preserves soundness.

### 7.4 Dominance

P83 is already a valid lower certificate. Therefore

\[
L_{84}(B_0)=\max\{L_{83}(B_0),L_{\mathrm{Walsh}}(B_0)\}
\]

is sound and can never be weaker than P83.

### 7.5 Exact arithmetic

The executable certificate uses `fractions.Fraction`, finite vertex enumeration, rational addition and multiplication, interval distance, finite maxima and minima, and division by an integer norm. No floating-point optimization is part of the proof path.

---

## 8. Strict exact-rational improvement witness over P83

Use the P75 parameter ordering

\[
(\pi,q_{1,-},q_{1,+},q_{2,-},q_{2,+},q_{3,-},q_{3,+},q_{4,-},q_{4,+}).
\]

Take the rational box

\[
\pi\in[0,1],
\qquad
q_{1,-},q_{1,+}\in\left[\frac38,\frac58\right],
\]

\[
q_{2,-}=q_{2,+}=\frac14,
\qquad
q_{3,-}=q_{3,+}=\frac14,
\qquad
q_{4,-}=q_{4,+}=\frac12.
\]

Define the empirical law by its Walsh expansion

\[
\boxed{
\widehat p(x)
=\frac1{16}\left[
1+\frac12\chi_{\{2\}}(x)
+\frac12\chi_{\{3\}}(x)
+\frac14\chi_{\{2,3\}}(x)
+\frac{3}{32}\chi_{\{1,2\}}(x)
-\frac{3}{32}\chi_{\{1,3\}}(x)
\right].
}
\]

The exact executable audit gives

\[
\min_x\widehat p_x=\frac1{64},
\qquad
\max_x\widehat p_x=\frac9{64},
\qquad
\sum_x\widehat p_x=1.
\]

Thus this is a genuine sixteen-cell probability law.

The complete exact P82 and P83 finite families remain compatible on this box:

\[
\boxed{L_{82}(B_0)=L_{83}(B_0)=0.}
\]

Now take

\[
\boxed{
\phi(x)=\chi_{\{1,2\}}(x)-\chi_{\{1,3\}}(x).
}
\]

Inside either P75 branch,

\[
\begin{aligned}
\mathbb E_t[\phi]
&=(1-2q_{1,t})(1-2q_{2,t})
 -(1-2q_{1,t})(1-2q_{3,t})\\
&=(1-2q_{1,t})\left[(1-2q_{2,t})-(1-2q_{3,t})\right]\\
&=0,
\end{aligned}
\]

because $q_{2,t}=q_{3,t}=1/4$. Therefore

\[
\boxed{
[\ell_\phi(B_0),u_\phi(B_0)]=[0,0].
}
\]

The empirical Walsh moments are

\[
\mathbb E_{\widehat p}[\chi_{\{1,2\}}]=\frac{3}{32},
\qquad
\mathbb E_{\widehat p}[\chi_{\{1,3\}}]=-\frac{3}{32},
\]

so

\[
\boxed{
\mathbb E_{\widehat p}[\phi]=\frac3{16}.
}
\]

Since $\|\phi\|_1=16$,

\[
\boxed{
L_{\mathrm{Walsh}}(B_0)
\ge
\frac{3/16}{16}
=\frac3{256}.
}
\]

The exact enumeration of all 210 predeclared contrasts identifies this same contrast as the unique strongest member of the P84 family on the witness. Consequently,

\[
\boxed{
L_{84}(B_0)=\frac3{256}>0=L_{83}(B_0).
}
\]

This proves a genuine strict strengthening rather than a restatement of a P83 parity violation.

---

## 9. Global branch-and-bound handoff

P84 can replace the P83 box lower bound inside the existing exact-rational branch-and-bound framework. Active boxes still partition the complete nine-dimensional P75 parameter cube, and the global lower bound is the minimum active P84 box bound.

For the upper direction, P84 deliberately retains the previously proved machinery:

- explicit P75 parameter vectors give valid model-distance upper witnesses;
- the P78 mesh-width certificate remains a valid global upper certificate.

No independent P84 convergence-rate theorem is claimed.

---

## 10. P79 finite-data rejection handoff

Let $\overline\varepsilon_{79}$ be the exact-rational upper envelope for the P77 cellwise sampling radius. Then

\[
\boxed{
L_{84}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
\mathcal C_n(\widehat p)\cap\mathcal M_{4,2}=\varnothing.
}
\]

The implication is one-sided. Failure of the strict inequality is inconclusive and does not validate P75.

---

## 11. Interpretation boundary

P84 proves an exact dependency-aware model-separation certificate for a declared latent-variable family. It shows that a signed combination of two parity characters can preserve shared parameter structure that separate event intervals discard.

It does **not** prove:

- that the P75 latent variable is a conscious state;
- that Walsh characters or their contrasts are measures of consciousness;
- that rejection of P75 implies nonphysical consciousness;
- that non-rejection validates P75;
- that quantum mechanics is required for the bridge;
- that the physical-to-experiential bridge is solved.

The physical-to-experiential bridge remains open.

---

## 12. Executable objects

Implementation:

- `src/consciousness_bridge/walsh_contrast_model_separation.py`

Primary public objects:

- `P84WalshContrastWitness`
- `P84DistanceBracket`
- `p84_standard_walsh_character_count`
- `p84_standard_contrast_count`
- `walsh_contrast_l1_norm`
- `empirical_walsh_character_expectation_exact`
- `empirical_walsh_contrast_expectation_exact`
- `p75_walsh_contrast_interval_exact`
- `p75_box_walsh_contrast_witness_exact`
- `p75_box_walsh_contrast_linf_lower_bound_exact`
- `p75_box_p84_linf_lower_bound_exact`
- `p84_dominates_p83_on_box`
- `certified_p75_linf_branch_and_bound_walsh`
- `p84_rejection_with_p79_radius`

Tests:

- `tests/test_walsh_contrast_model_separation.py`

Figure:

- `docs/figures/p84_exact_pairwise_walsh_contrast.svg`

Equation provenance:

- `docs/p84_equation_provenance.md`

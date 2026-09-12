# Proposition 84: Exact Coupled Projection-Parity Contrast Certificate

## Status

**Proved conditional computational theorem.** P84 strengthens the complete P83 certificate for the same declared P75 four-view binary latent family and the same full-law $L_\infty$ distance.

P83 tests each nontrivial parity observable separately. P84 asks a strictly stronger compatibility question: can two individually admissible parity observables be realized by the **same** P75 parameter choice inside the same parameter box?

The answer is encoded by an exact pairwise parity-expectation contrast. The contrast remains multi-affine in the P75 response coordinates, so its complete rational parameter-box range is exactly computable by endpoint evaluation.

P84 is a model-distance certification result. It does not establish that the P75 latent state is consciousness, does not validate the P75 model when rejection fails, and does not close the physical-to-experiential bridge.

---

## 1. The gap left by separate P83 intervals

For a selected view set $J$, define the signed parity observable

\[
\chi_J(x)=(-1)^{\sum_{j\in J}x_j}.
\]

P83 derives an exact interval for each parity probability, equivalently for each signed parity expectation

\[
Z(J)=\mathbb E[\chi_J].
\]

Suppose two empirical values $\widehat Z(J)$ and $\widehat Z(K)$ each fall inside their own exact P75 box intervals. That establishes only **marginal interval compatibility**. It does not prove that one common parameter vector $\theta$ inside the box can realize both values simultaneously.

This is the same logical distinction that appears throughout the repository: separate feasible projections need not imply joint feasibility in the underlying model.

P84 therefore tests the coupled contrast

\[
\boxed{
D(J,K)=Z(J)-Z(K).
}
\]

If the declared P75 box forces a restricted relationship between the two parity expectations, the contrast can expose an incompatibility that no separate P83 interval can see.

---

## 2. Exact branchwise formula

Inside latent branch $s\in\{-,+\}$, conditional independence gives the P83 identity

\[
Z_s(J)
=
\prod_{j\in J}(1-2q_{j,s}).
\]

For two distinct P83 view sets $J$ and $K$,

\[
\boxed{
D_s(J,K)
=
\prod_{j\in J}(1-2q_{j,s})
-
\prod_{j\in K}(1-2q_{j,s}).
}
\]

Every response coordinate appears with degree at most one. Therefore $D_s(J,K)$ is multi-affine in the coordinates indexed by $J\cup K$.

A multi-affine function on a rectangular parameter box attains its minimum and maximum at vertices. Consequently, if the relevant branchwise response coordinates have rational endpoints, the exact interval

\[
D_s(J,K)\in[d_s^L,d_s^U]
\]

is obtained by evaluating only the endpoint combinations of the response coordinates in $J\cup K$.

Since there are only four observed views, at most $2^4=16$ branch vertices are required for one contrast.

---

## 3. Exact latent-mixture contrast interval

Let latent prevalence satisfy

\[
\pi\in[\pi_L,\pi_U].
\]

The mixture parity expectation is

\[
Z(J)
=(1-\pi)Z_-(J)+\pi Z_+(J),
\]

so the pairwise contrast is

\[
D(J,K)
=(1-\pi)D_-(J,K)+\pi D_+(J,K).
\]

The minus-branch response coordinates and plus-branch response coordinates are disjoint. Their branch extrema can therefore be attained simultaneously. For a fixed prevalence, the global lower envelope uses both branch lower endpoints and the global upper envelope uses both branch upper endpoints. The remaining dependence on $\pi$ is affine.

Hence

\[
\boxed{
\ell_{J,K}(B)
=
\min_{\pi\in\{\pi_L,\pi_U\}}
\left[(1-\pi)d_-^L+\pi d_+^L\right],
}
\]

and

\[
\boxed{
u_{J,K}(B)
=
\max_{\pi\in\{\pi_L,\pi_U\}}
\left[(1-\pi)d_-^U+\pi d_+^U\right].
}
\]

Thus

\[
\boxed{
D(J,K)\in[\ell_{J,K}(B),u_{J,K}(B)]
}
\]

is the **exact** P75 parameter-box image interval of the coupled parity contrast.

---

## 4. Transfer to full-law $L_\infty$ distance

For distinct view sets $J$ and $K$, the linear functional associated with the contrast is

\[
D_p(J,K)
=
\sum_{x\in\{0,1\}^4}
\bigl[\chi_J(x)-\chi_K(x)\bigr]p(x).
\]

Because $J\ne K$, the symmetric difference $J\triangle K$ is nonempty. The two signs $\chi_J$ and $\chi_K$ therefore agree on exactly eight of the sixteen binary outcomes and disagree on exactly eight.

Hence

\[
\chi_J(x)-\chi_K(x)
\in\{-2,0,2\},
\]

with magnitude two on exactly eight cells. The coefficient $L_1$ norm is therefore

\[
\boxed{
\sum_x |\chi_J(x)-\chi_K(x)|=16.
}
\]

If

\[
\|p-q\|_\infty\le r,
\]

then

\[
|D_p(J,K)-D_q(J,K)|
\le
16r.
\]

Therefore

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\widehat D(J,K),
[\ell_{J,K}(B),u_{J,K}(B)]
\right)
}{16}.
}
\]

Define the strongest coupled parity-contrast bound on box $B$ as

\[
\boxed{
L_{\mathrm{pc}}(B)
=
\max_{(J,K)\in\mathcal C}
\frac{
d\!\left(
\widehat D(J,K),
[\ell_{J,K}(B),u_{J,K}(B)]
\right)
}{16}.
}
\]

---

## 5. The finite P84 contrast family

P83 uses all view subsets of size two, three, or four. The number of such view sets is

\[
{4\choose2}+{4\choose3}+{4\choose4}
=6+4+1
=11.
\]

P84 tests every unordered pair of distinct P83 view sets. Therefore

\[
\boxed{
|\mathcal C|={11\choose2}=55.
}
\]

The family is finite, exact, and small enough for direct rational evaluation inside every branch-and-bound box.

---

## 6. P84 theorem

For every admissible P78 parameter box $B$, define

\[
\boxed{
L_{84}(B)
=
\max\{L_{83}(B),L_{\mathrm{pc}}(B)\}.
}
\]

Then:

1. $L_{84}(B)$ is a rigorous lower bound on the $L_\infty$ distance from $\widehat p$ to every P75 law generated inside $B$;
2. $L_{84}(B)\ge L_{83}(B)\ge L_{82}(B)\ge L_{81}(B)\ge L_{80}(B)\ge L_{78}(B)$;
3. every P84 branchwise parity-contrast interval is exact over the declared response-coordinate box;
4. every P84 latent-mixture contrast interval is exact over the full P75 parameter box;
5. all interval endpoints and lower bounds are exactly rational whenever the empirical law and parameter-box endpoints are rational;
6. for any finite partition $\mathcal B$ of the complete P75 parameter cube,

\[
\boxed{
L_{84}(\mathcal B)
:=
\min_{B\in\mathcal B}L_{84}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2});
}
\]

7. on the same partition,

\[
\boxed{
L_{84}(\mathcal B)\ge L_{83}(\mathcal B);
}
\]

8. explicit P75 parameter vectors remain valid global upper-bound witnesses;
9. the previously proved P78 mesh-width upper certificate remains valid and is retained unchanged. P84 does not claim a new convergence-rate theorem.

---

## 7. Proof

### 7.1 Exact branch interval

Each branch contrast is a difference of two products of affine response-coordinate factors. Every coordinate appears with degree at most one, so the contrast is multi-affine. A multi-affine function on a rectangular box attains every global extremum at a vertex. Enumerating the endpoint choices of the coordinates in $J\cup K$ therefore gives the exact branch interval.

### 7.2 Exact mixture interval

Minus-branch and plus-branch response coordinates are disjoint. Their extrema can be selected independently and attained simultaneously. Prevalence is also a separate coordinate and enters linearly. The exact global minimum and maximum therefore occur at branch extrema and prevalence endpoints.

### 7.3 Soundness of the $L_\infty$ lower bound

The parity-contrast functional has coefficient $L_1$ norm sixteen. Therefore

\[
|D_{\widehat p}(J,K)-D_q(J,K)|
\le
16\|\widehat p-q\|_\infty.
\]

Every P75 law generated inside $B$ has its contrast inside the exact interval $[\ell_{J,K}(B),u_{J,K}(B)]$. Distance of the empirical contrast to that interval divided by sixteen is therefore a valid full-law lower bound. Maximizing over all 55 contrasts preserves soundness.

### 7.4 Dominance

By construction,

\[
L_{84}(B)=\max\{L_{83}(B),L_{\mathrm{pc}}(B)\},
\]

so $L_{84}(B)\ge L_{83}(B)$ for every box. Taking minima over a common partition preserves partition-level dominance.

---

## 8. Strict exact-rational witness: P84 can detect what the complete P83 audit misses

The strictness result is important because P84 is intended to add a genuinely new joint-compatibility test rather than merely re-express P83.

Take the P75 parameter box

\[
\pi\in[0,1],
\]

\[
q_{1,-},q_{1,+},q_{4,-},q_{4,+}\in[0,1],
\]

with fixed response coordinates

\[
q_{2,-}=q_{3,-}=\frac14,
\qquad
q_{2,+}=q_{3,+}=\frac34.
\]

Because views 2 and 3 have identical response probabilities inside each latent branch,

\[
Z_s(\{1,2\})=Z_s(\{1,3\})
\]

for both $s=-$ and $s=+$. Hence the entire P75 box forces

\[
\boxed{
D(\{1,2\},\{1,3\})=0.
}
\]

Using zero-based implementation indices, this is the contrast between view sets $(0,1)$ and $(0,2)$.

Now define the exact empirical sixteen-cell law, in lexicographic outcome order, by the nonzero masses

\[
\widehat p(0,0,1,1)=\frac{3}{16},
\]

\[
\widehat p(0,1,1,1)=\frac{3}{16},
\]

\[
\widehat p(1,0,0,1)=\frac{1}{16},
\]

\[
\widehat p(1,1,0,0)=\frac{3}{16},
\]

\[
\widehat p(1,1,1,0)=\frac{5}{16},
\]

\[
\widehat p(1,1,1,1)=\frac{1}{16},
\]

with all remaining cells zero.

Direct exact evaluation gives

\[
\widehat Z(\{1,2\})=\frac12,
\qquad
\widehat Z(\{1,3\})=-\frac14,
\]

so

\[
\boxed{
\widehat D(\{1,2\},\{1,3\})=\frac34.
}
\]

At the same time, this empirical law lies inside every exact P81 cylinder interval, every exact P82 nested-residual interval, and every exact P83 parity interval for the declared box. Therefore

\[
\boxed{
L_{83}(B)=0.
}
\]

P84 sees the joint incompatibility:

\[
L_{\mathrm{pc}}(B)
=
\frac{d(3/4,\{0\})}{16}
=
\boxed{\frac{3}{64}}.
\]

Thus

\[
\boxed{
L_{84}(B)=\frac{3}{64}>0=L_{83}(B).
}
\]

This is an exact rational strict-strengthening witness.

---

## 9. Global branch-and-bound use

The implementation uses $L_{84}(B)$ as the active-box lower bound inside the same global P75 branch-and-bound architecture used by P78-P83.

For a partition $\mathcal B$ of the complete parameter cube,

\[
L_{84}(\mathcal B)
=
\min_{B\in\mathcal B}L_{84}(B)
\]

is a valid global lower bound. Explicit box-center parameter vectors supply valid global upper witnesses.

The P78 mesh-width result remains the certified global upper-gap mechanism. P84 does not silently infer a sharper convergence theorem from the stronger box lower bound.

---

## 10. Finite-data rejection handoff

Let $R_{79}$ be the P79 certified rational upper bound on the P77 cellwise sampling radius. The same strict rejection gate applies:

\[
\boxed{
L_{84}(\mathcal B)>R_{79}
\Longrightarrow
\text{reject the declared P75 family at the stated finite-data guarantee.}
}
\]

If the inequality fails, the result is inconclusive. Failure to reject is not model validation.

---

## 11. Implementation and verification

### Source implementation

- [`src/consciousness_bridge/projection_parity_contrast_separation.py`](../src/consciousness_bridge/projection_parity_contrast_separation.py)

### Regression tests

- [`tests/test_projection_parity_contrast_separation.py`](../tests/test_projection_parity_contrast_separation.py)

The tests verify:

1. the standard P84 family contains exactly 55 pairwise contrasts;
2. exact P84 box intervals agree with exhaustive full parameter-box vertex evaluation on an independent rational test box;
3. the strict witness has complete P83 lower bound zero and P84 lower bound $3/64$;
4. the selected branch-symmetry contrast is exactly zero throughout the witness parameter box;
5. the empirical witness parity expectations are exactly $1/2$ and $-1/4$;
6. P84 always dominates P83 on the same box;
7. invalid contrast specifications are rejected;
8. the P84 global branch-and-bound wrapper returns a valid exact-rational lower/upper bracket;
9. the source retains explicit scientific-boundary language.

---

## 12. Scientific interpretation boundary

P84 establishes a stronger exact certificate for rejecting a declared continuous target-measurement model family when **joint parity structure** is incompatible with that family.

It does **not** establish any of the following:

- that the P75 model is true when the certificate is small;
- that a latent P75 state is an experience;
- that parity is a measure of consciousness;
- that consciousness is nonphysical;
- that failure of one target-measurement family falsifies every physical theory;
- that the physical-to-experiential bridge has been solved.

The result is deliberately narrower and stronger: separate compatibility of many exact observables does not imply their joint compatibility with one underlying parameter vector. P84 adds one exact family of joint constraints and shows, by an explicit rational witness, that those constraints can matter.

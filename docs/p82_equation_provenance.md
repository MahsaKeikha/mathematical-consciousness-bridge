# P82 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 82](proposition_82_exact_nested_projection_contrast.md), **Exact Nested Projection-Contrast Certificate for Continuous P75 Separation**.

P82 is a downstream computational-certification theorem for the same four-view binary latent model introduced in P75 and the same full-law $L_\infty$ rejection architecture developed through P77-P81.

The new mathematical step is an exact parameter-box extremization for residual events of the form $A\setminus B$ when $B$ is a nested child cylinder of $A$.

P82 introduces no consciousness variable and no new physical postulate.

---

## 1. Imported P75 model

The complete observed law is

\[
q_x(\theta)
=
(1-\pi)\prod_{j=1}^4 f(q_{j,-},x_j)
+
\pi\prod_{j=1}^4 f(q_{j,+},x_j),
\]

with

\[
f(q,1)=q,
\qquad
f(q,0)=1-q.
\]

**Classification:** imported project definition from P75.

**Dependencies:** [P75](proposition_75_target_model_adequacy_overidentification.md), [P78](proposition_78_certified_continuous_model_separation.md).

---

## 2. Imported P81 cylinder definition

For nonempty $J\subseteq\{1,2,3,4\}$ and assignment $a$,

\[
C(J,a)=\{x:x_j=a_j\text{ for every }j\in J\}.
\]

Its support size is

\[
|C(J,a)|=2^{4-|J|}.
\]

**Classification:** imported finite-product-space definition already used by P81.

**Dependency:** [P81](proposition_81_projection_event_model_separation.md).

---

## 3. Nested residual identity

Let

\[
A=C(J,a),
\qquad
B=C(K,b),
\qquad
J\subset K,
\qquad
b|_J=a.
\]

Then $B\subset A$ and

\[
\mathbf 1_A-\mathbf 1_B
=\mathbf 1_{A\setminus B}.
\]

The support size is

\[
|A\setminus B|
=2^{4-|J|}-2^{4-|K|}.
\]

**Classification:** elementary finite-set identity specialized to nested P81 cylinder events.

---

## 4. Branchwise factorization of the residual event

Let $R=K\setminus J$ and let $D$ be the added-view event that fixes the coordinates in $R$ according to the child assignment. Under one P75 latent branch $s$,

\[
B=A\cap D.
\]

P75 conditional independence across the observed views gives

\[
P_s(B)=P_s(A)P_s(D).
\]

Therefore

\[
\boxed{
P_s(A\setminus B)
=P_s(A)\bigl(1-P_s(D)\bigr).
}
\]

**Classification:** new P82 algebraic consequence of the P75 conditional-independence model.

---

## 5. Exact branchwise box interval

Suppose

\[
P_s(A)\in[a_s^L,a_s^U],
\qquad
P_s(D)\in[d_s^L,d_s^U].
\]

The parent coordinates $J$ and added coordinates $R$ are disjoint. Therefore the response parameters entering the two products are disjoint coordinates of the axis-aligned P78 parameter box and their endpoint extrema are jointly attainable.

On $[0,1]^2$, the map

\[
(a,d)\mapsto a(1-d)
\]

is nondecreasing in $a$ and nonincreasing in $d$. Hence

\[
\boxed{
P_s(A\setminus B)
\in
\left[
a_s^L(1-d_s^U),

a_s^U(1-d_s^L)
\right].
}
\]

This interval is exact, not merely conservative.

**Classification:** new P82 exact interval theorem.

**Dependency:** same endpoint-product principle used in P78 and P81, plus the disjoint-coordinate structure of the nested residual factorization.

**Numerical status:** exact rational arithmetic for rational box endpoints.

---

## 6. Exact latent-mixture box interval

Define

\[
r_s^L=a_s^L(1-d_s^U),
\qquad
r_s^U=a_s^U(1-d_s^L).
\]

For prevalence $\pi$,

\[
q(A\setminus B)
=(1-\pi)r_-+\pi r_+.
\]

For fixed prevalence the expression is monotone in both branch residuals. The lower and upper envelopes are therefore

\[
L(\pi)=(1-\pi)r_-^L+\pi r_+^L,
\]

\[
U(\pi)=(1-\pi)r_-^U+\pi r_+^U.
\]

Because both are affine in $\pi$, exact extrema on $[\pi_L,\pi_U]$ occur at a prevalence endpoint:

\[
\ell_{A\setminus B}
=
\min_{\pi\in\{\pi_L,\pi_U\}}L(\pi),
\]

\[
u_{A\setminus B}
=
\max_{\pi\in\{\pi_L,\pi_U\}}U(\pi).
\]

**Classification:** new P82 exact mixture-extremum theorem.

---

## 7. Conservative subtraction enclosure

Separate P81 intervals imply

\[
q(A)\in[\ell_A,u_A],
\qquad
q(B)\in[\ell_B,u_B].
\]

Therefore

\[
q(A\setminus B)=q(A)-q(B)
\]

lies in

\[
\left[
\max\{0,\ell_A-u_B\},
\min\{1,u_A-\ell_B\}
\right].
\]

**Classification:** standard interval subtraction with probability clipping.

P82 does not use this as its primary residual interval because it discards common-parameter dependence. It is retained in the implementation as an audit enclosure. The exact P82 interval must lie inside it.

---

## 8. Event-mass $L_\infty$ transfer

For every finite event $S$,

\[
\begin{aligned}
|\widehat p(S)-q(S)|
&=\left|\sum_{x\in S}(\widehat p_x-q_x)\right|\\
&\le\sum_{x\in S}|\widehat p_x-q_x|\\
&\le |S|\,\|\widehat p-q\|_\infty.
\end{aligned}
\]

**Classification:** standard triangle inequality and definition of the $L_\infty$ norm, already used by P81.

**Dependency:** [P81](proposition_81_projection_event_model_separation.md).

---

## 9. Single nested-residual lower bound

Since every model law generated inside the box has residual probability in the exact interval,

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\widehat p(A\setminus B),
[\ell_{A\setminus B},u_{A\setminus B}]
\right)
}{|A\setminus B|}.
}
\]

**Classification:** new P82 certificate obtained by combining the exact residual interval with the P81 event-mass transfer principle.

---

## 10. Standard family size

P82 includes nested pairs where the child adds at least two views. The count is

\[
\begin{aligned}
|\mathcal N|
&={4\choose1}2
\left[{3\choose2}2^2+{3\choose3}2^3\right]
+{4\choose2}2^2{2\choose2}2^2\\
&=256.
\end{aligned}
\]

**Classification:** new P82 finite-family definition plus direct combinatorial count.

One-view refinements are omitted because their residual is exactly a sibling cylinder already present in P81.

---

## 11. Combined P82 certificate

P82 defines

\[
L_{\mathrm{nest}}(B)
=
\max_{(A,B)\in\mathcal N}
\frac{
d\!\left(
\widehat p(A\setminus B),
[\ell_{A\setminus B},u_{A\setminus B}]
\right)
}{|A\setminus B|}
\]

and

\[
\boxed{
L_{82}(B)=\max\{L_{81}(B),L_{\mathrm{nest}}(B)\}.
}
\]

Hence

\[
L_{82}(B)\ge L_{81}(B)\ge L_{80}(B)\ge L_{78}(B).
\]

**Classification:** new P82 combination theorem.

---

## 12. Global partition certificate

For an active partition $\mathcal B$ of the full parameter cube,

\[
L_{82}(\mathcal B)
=
\min_{B\in\mathcal B}L_{82}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}).
\]

**Classification:** branch-and-bound lower-envelope logic inherited from P78-P81 with a stronger box lower bound.

P82 deliberately retains the P78 mesh-width upper certificate. No new P82 convergence-rate theorem is assumed.

---

## 13. P79 rejection gate

With P79 certified sampling-radius upper envelope $\overline\varepsilon_{79}$,

\[
L_{82}(\mathcal B)>\overline\varepsilon_{79}
\]

is sufficient for the P77 full-law rejection conclusion.

**Classification:** imported P77/P79 rejection logic with the stronger P82 model-distance lower bound.

**Dependencies:** [P77](proposition_77_full_law_model_set_separation.md), [P79](proposition_79_certified_sampling_radius.md).

---

## 14. Strict improvement witness

The exact witness in the proposition gives

\[
L_{80}=0,
\qquad
L_{81}=\frac1{16},
\qquad
L_{82}=\frac1{12}.
\]

**Classification:** project-derived exact-rational constructive witness verified by the implementation and regression tests.

---

## 15. Scientific boundary

Every P82 equation is conditional on the declared P75 target-view model and the declared $L_\infty$ observed-law metric.

P82 can strengthen evidence that an observed law is incompatible with that declared model. It cannot establish an experiential interpretation for the latent variable, cannot turn non-rejection into model truth, and does not close the physical-to-experiential bridge.

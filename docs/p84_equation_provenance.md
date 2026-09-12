# P84 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 84](proposition_84_exact_pairwise_walsh_contrast.md), **Exact Pairwise Walsh-Contrast Certificate for Continuous P75 Separation**.

P84 is a downstream computational-certification theorem for the same four-view binary latent family introduced in P75 and the same full-law $L_\infty$ rejection architecture developed through P77-P83.

The new mathematical step is to keep shared P75 parameter dependence across two Walsh parity characters instead of certifying those characters only one at a time. P84 does this with a finite family of signed pairwise Walsh contrasts, exact rational parameter-box extremization, and an observable-duality transfer to full-law $L_\infty$ distance.

P84 introduces no consciousness variable and no new physical postulate.

---

## 1. Imported P75 observed-law model

The sixteen-cell P75 observed law is

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

## 2. Walsh character

For every nonempty selected view set $J\subseteq\{1,2,3,4\}$,

\[
\boxed{
\chi_J(x)=(-1)^{\sum_{j\in J}x_j}.
}
\]

**Classification:** standard Walsh/Fourier character on the binary cube, specialized as a P84 observable basis.

There are

\[
2^4-1=15
\]

nonconstant characters.

---

## 3. Branchwise Walsh expectation

Conditional independence inside one P75 latent branch $t\in\{-,+\}$ gives

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

**Classification:** standard product identity for independent Bernoulli Walsh characters, applied to the declared P75 branch factorization.

**Relation to P83:** P83 uses the same character identity to certify one parity event at a time. P84 uses linear combinations of two characters to retain cross-character parameter dependence.

---

## 4. Signed pairwise Walsh contrast

For distinct nonempty view sets $A$ and $B$ and relative sign $s\in\{-1,+1\}$, define

\[
\boxed{
\phi_{A,B,s}(x)=\chi_A(x)+s\chi_B(x).
}
\]

Then

\[
\boxed{
\mathbb E_t[\phi_{A,B,s}(X)]
=
\prod_{j\in A}(1-2q_{j,t})
+s\prod_{j\in B}(1-2q_{j,t}).
}
\]

**Classification:** new P84 finite observable-family definition combined with the imported Walsh product identity.

---

## 5. Multi-affine branch extremization

Each branch expectation is a polynomial in the response coordinates with degree at most one in every coordinate. It is therefore multi-affine. On an axis-aligned response-parameter box, its extrema occur at endpoint vertices:

\[
\boxed{
[a_t^L,a_t^U]
=
\left[
\min_{v\in V_{A\cup B}}\mathbb E_t[\phi](v),
\max_{v\in V_{A\cup B}}\mathbb E_t[\phi](v)
\right].
}
\]

**Classification:** standard multi-affine box-extremum principle, used here as the new exact P84 branch certificate.

**Numerical status:** endpoint evaluation uses `fractions.Fraction`; there is no floating-point optimization in the proof path.

---

## 6. Exact latent-mixture interval

The minus and plus branches use disjoint response coordinates, so their branch minima and maxima can be attained simultaneously. For prevalence $\pi$,

\[
\mathbb E_q[\phi]
=(1-\pi)\mathbb E_-[\phi]+
\pi\mathbb E_+[\phi].
\]

With

\[
\mathbb E_-[\phi]\in[a_-^L,a_-^U],
\qquad
\mathbb E_+[\phi]\in[a_+^L,a_+^U],
\]

and $\pi\in[\pi_L,\pi_U]$,

\[
\boxed{
\ell_\phi(B)
=
\min_{\pi\in\{\pi_L,\pi_U\}}
\bigl[(1-\pi)a_-^L+\pi a_+^L\bigr],
}
\]

\[
\boxed{
u_\phi(B)
=
\max_{\pi\in\{\pi_L,\pi_U\}}
\bigl[(1-\pi)a_-^U+\pi a_+^U\bigr].
}
\]

**Classification:** new P84 exact full-box expectation interval.

---

## 7. Observable-to-$L_\infty$ transfer

For any finite real-valued observable $\phi$,

\[
\begin{aligned}
|\mathbb E_p\phi-\mathbb E_q\phi|
&=
\left|\sum_x \phi(x)(p_x-q_x)\right|\\
&\le
\sum_x |\phi(x)|\,|p_x-q_x|\\
&\le
\|p-q\|_\infty\sum_x|\phi(x)|.
\end{aligned}
\]

Define

\[
\boxed{
\|\phi\|_1=\sum_x|\phi(x)|.
}
\]

**Classification:** standard finite-dimensional Holder/triangle-inequality bound specialized to the sixteen-cell $L_\infty$ metric.

**New P84 use:** this transfers exact expectation mismatch of a signed contrast into a sound lower bound on full-law model distance.

---

## 8. Single-contrast lower certificate

Every P75 law generated in box $B$ satisfies

\[
\mathbb E_q[\phi]
\in
[\ell_\phi(B),u_\phi(B)].
\]

Hence

\[
\boxed{
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\mathbb E_{\widehat p}[\phi],
[\ell_\phi(B),u_\phi(B)]
\right)
}{\|\phi\|_1}.
}
\]

**Classification:** new P84 exact contrast certificate.

---

## 9. Pairwise contrast $L_1$ norm

For distinct characters $\chi_A$ and $\chi_B$,

\[
\chi_A\chi_B=\chi_{A\triangle B}.
\]

Because $A\triangle B\ne\varnothing$, this character is balanced on the four-bit cube. Therefore eight cells have $\chi_A=\chi_B$ and eight have $\chi_A=-\chi_B$. For either relative sign,

\[
|\chi_A+s\chi_B|
=
\begin{cases}
2,&\text{on eight cells},\\
0,&\text{on eight cells}.
\end{cases}
\]

Thus

\[
\boxed{
\|\phi_{A,B,s}\|_1=16.
}
\]

**Classification:** project-derived finite-cube consequence of the standard character multiplication identity.

The implementation nevertheless computes the norm directly as an executable guard.

---

## 10. Standard family size

There are fifteen nonconstant characters. P84 uses both relative signs for each unordered pair:

\[
\boxed{
|\mathcal W|
=2{15\choose2}
=210.
}
\]

**Classification:** new P84 finite-family definition plus direct combinatorial count.

---

## 11. Combined P84 certificate

Define

\[
L_{\mathrm{Walsh}}(B)
=
\max_{\phi\in\mathcal W}
\frac{
d\!\left(
\mathbb E_{\widehat p}[\phi],
[\ell_\phi(B),u_\phi(B)]
\right)
}{\|\phi\|_1},
\]

and then

\[
\boxed{
L_{84}(B)=\max\{L_{83}(B),L_{\mathrm{Walsh}}(B)\}.
}
\]

Therefore

\[
L_{84}(B)
\ge L_{83}(B)
\ge L_{82}(B)
\ge L_{81}(B)
\ge L_{80}(B)
\ge L_{78}(B).
\]

**Classification:** new P84 combination theorem.

---

## 12. Strict exact-rational witness

The P84 witness uses

\[
\pi\in[0,1],
\quad
q_{1,-},q_{1,+}\in[3/8,5/8],
\]

\[
q_{2,-}=q_{2,+}=1/4,
\quad
q_{3,-}=q_{3,+}=1/4,
\quad
q_{4,-}=q_{4,+}=1/2.
\]

The empirical law is

\[
\widehat p(x)
=\frac1{16}\left[
1+\frac12\chi_{\{2\}}
+\frac12\chi_{\{3\}}
+\frac14\chi_{\{2,3\}}
+\frac{3}{32}\chi_{\{1,2\}}
-\frac{3}{32}\chi_{\{1,3\}}
\right].
\]

The executable exact-rational audit gives

\[
\min_x\widehat p_x=1/64,
\qquad
\max_x\widehat p_x=9/64,
\qquad
\sum_x\widehat p_x=1.
\]

The complete P82 and P83 declared finite families give

\[
\boxed{L_{82}(B)=L_{83}(B)=0.}
\]

For

\[
\phi=\chi_{\{1,2\}}-\chi_{\{1,3\}},
\]

the P75 box forces

\[
\mathbb E_q[\phi]=0
\]

because views 2 and 3 have identical branchwise response probabilities. Empirically,

\[
\mathbb E_{\widehat p}[\phi]=3/16,
\]

and $\|\phi\|_1=16$, so

\[
\boxed{
L_{84}(B)=\frac{3}{256}>0=L_{83}(B).
}
\]

**Classification:** project-derived exact-rational constructive witness. The regression test evaluates the full P82, P83, and 210-member P84 families with `fractions.Fraction` arithmetic.

---

## 13. Global partition certificate

For an active partition $\mathcal B$ of the complete P75 parameter cube,

\[
L_{84}(\mathcal B)
=
\min_{B\in\mathcal B}L_{84}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}).
\]

**Classification:** branch-and-bound lower-envelope logic inherited from P78-P83 with a stronger box lower bound.

P84 deliberately retains the P78 mesh-width upper certificate. No new P84 convergence-rate theorem is assumed.

---

## 14. P79 rejection gate

With P79 certified sampling-radius upper envelope $\overline\varepsilon_{79}$,

\[
L_{84}(\mathcal B)>\overline\varepsilon_{79}
\]

is sufficient for the P77 full-law rejection conclusion.

**Classification:** imported P77/P79 one-sided rejection logic with the stronger P84 model-distance lower bound.

---

## 15. Scientific boundary

Every P84 equation is conditional on the declared P75 target-view model and the declared $L_\infty$ observed-law metric.

P84 can strengthen evidence that an observed law is incompatible with that declared model. It cannot assign experiential meaning to a latent variable, cannot turn non-rejection into model truth, cannot establish a new physical dimension, and does not close the physical-to-experiential bridge.

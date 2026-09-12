# P81 Equation and Provenance Record

## Scope

This record classifies the equations used in [Proposition 81](proposition_81_projection_event_model_separation.md), **Projection-Event Certificate for Continuous P75 Separation**. P81 is a downstream computational-certification result for the same four-view binary latent model introduced in P75 and the same $L_\infty$ full-law rejection architecture used in P77-P80.

The new mathematical step is to exploit exact parameter-box ranges of projected binary events and transfer discrepancies in those event probabilities back to a certified lower bound on sixteen-cell $L_\infty$ distance.

P81 does not introduce a consciousness variable or a new physical postulate.

---

## 1. Imported model definition

P81 inherits the P75 four-view binary latent model. With latent prevalence $\pi$ and view-channel probabilities $q_{j,-},q_{j,+}$, the complete observed law is

\[
q_x(\theta)
=
(1-\pi)
\prod_{j=1}^{4}f(q_{j,-},x_j)
+
\pi
\prod_{j=1}^{4}f(q_{j,+},x_j),
\]

where

\[
f(q,1)=q,
\qquad
f(q,0)=1-q.
\]

**Classification:** imported project definition from P75, reused by P78-P80.

**Dependency:** [P75](proposition_75_target_model_adequacy_overidentification.md), [P78](proposition_78_certified_continuous_model_separation.md).

---

## 2. Cylinder-event definition

For nonempty $J\subseteq\{1,2,3,4\}$ and assignment $a\in\{0,1\}^{|J|}$,

\[
C(J,a)
=
\{x\in\{0,1\}^4:x_j=a_j\ \forall j\in J\}.
\]

The event contains

\[
|C(J,a)|=2^{4-|J|}
\]

full observed cells.

**Classification:** standard finite-product-space definition specialized to the P75 four-view outcome space.

---

## 3. Projected P75 event probability

Marginalizing coordinates outside $J$ gives

\[
m_{J,a}(\theta)
=
(1-\pi)
\prod_{j\in J}f(q_{j,-},a_j)
+
\pi
\prod_{j\in J}f(q_{j,+},a_j).
\]

**Derivation:** sum the P75 sixteen-cell law over all assignments of the omitted coordinates and use

\[
q+(1-q)=1
\]

for every omitted Bernoulli factor.

**Classification:** direct algebraic consequence of the P75 model; new P81 use of that consequence for certification.

---

## 4. Exact parameter-box interval

For a rational P78 parameter box $B$, each selected Bernoulli factor is monotone in its channel parameter. Therefore the two latent-state products achieve exact extrema at parameter endpoints. Conditional on those product extrema, dependence on $\pi$ is affine, so prevalence endpoints suffice as well.

P81 writes the exact range as

\[
\ell_{J,a}(B)
\le
m_{J,a}(\theta)
\le
\nu_{J,a}(B).
\]

**Classification:** project-derived exact interval theorem using the same multi-affine endpoint principle already used by P78, specialized to projected events.

**Dependency:** [P78](proposition_78_certified_continuous_model_separation.md).

**Numerical status:** exact rational arithmetic in the implementation; no floating-point optimizer is required for this interval.

---

## 5. Empirical projected mass

For empirical sixteen-cell law $\widehat p$,

\[
\widehat m_{J,a}
=
\sum_{x\in C(J,a)}\widehat p_x.
\]

**Classification:** standard empirical marginalization.

---

## 6. Event-mass Lipschitz transfer

If

\[
\|\widehat p-q\|_\infty\le r,
\]

then

\[
\begin{aligned}
|\widehat m_{J,a}-q(C(J,a))|
&=
\left|\sum_{x\in C(J,a)}(\widehat p_x-q_x)\right|\\
&\le
\sum_{x\in C(J,a)}|\widehat p_x-q_x|\\
&\le
|C(J,a)|\,r.
\end{aligned}
\]

**Classification:** standard triangle inequality plus the definition of the $L_\infty$ norm, specialized to a finite event sum.

This is the key deterministic inequality that converts projected-event mismatch into a lower bound on full-law distance.

---

## 7. Single-event lower bound

Since every P75 law generated inside $B$ has event probability in the exact interval,

\[
\|\widehat p-q(\theta)\|_\infty
\ge
\frac{
d\!\left(
\widehat m_{J,a},
[\ell_{J,a}(B),\nu_{J,a}(B)]
\right)
}{|C(J,a)|}.
\]

Using $|C(J,a)|=2^{4-|J|}$ gives the form reported in P81.

**Classification:** new project theorem obtained by combining Sections 4-6.

---

## 8. Projection-family lower bound

P81 maximizes the valid single-event bound over all nonempty cylinder events:

\[
L_{\mathrm{proj}}(B)
=
\max_{\emptyset\ne J\subseteq\{1,2,3,4\}}
\max_a
\frac{
d\!\left(
\widehat m_{J,a},
[\ell_{J,a}(B),\nu_{J,a}(B)]
\right)
}{2^{4-|J|}}.
\]

The event count is

\[
\sum_{k=1}^{4}{4\choose k}2^k
=(1+2)^4-1
=80.
\]

**Classification:** new P81 certificate definition; the event-count identity is a direct binomial-theorem calculation.

---

## 9. Embedded P78 cell bound

For $|J|=4$, each cylinder event contains one cell. Its exact event interval is the corresponding exact P78 cell interval and the denominator equals one. Therefore

\[
L_{\mathrm{proj}}(B)\ge L_{78}(B).
\]

**Classification:** new P81 dominance observation derived directly from the inclusion of full assignments in the cylinder-event family.

---

## 10. Combined P81 box certificate

P81 defines

\[
L_{81}(B)
=
\max\{L_{80}(B),L_{\mathrm{proj}}(B)\}.
\]

Because both terms are sound lower bounds on distance to the true model image inside $B$,

\[
L_{81}(B)
\le
\inf_{\theta\in B}
\|\widehat p-q(\theta)\|_\infty.
\]

Also,

\[
L_{81}(B)\ge L_{80}(B)\ge L_{78}(B).
\]

**Classification:** new P81 combination theorem.

**Dependency:** [P80](proposition_80_simplex_coupled_model_separation.md).

---

## 11. Global partition certificate

For any finite active parameter-box partition $\mathcal B$,

\[
L_{81}(\mathcal B)
=
\min_{B\in\mathcal B}L_{81}(B)
\le
d_\infty(\widehat p,\mathcal M_{4,2}).
\]

**Classification:** standard branch-and-bound lower-envelope logic already used in P78 and P80, now with the stronger P81 box lower bound.

The implementation deliberately retains the original P78 active lower bounds and the P78 mesh-width upper certificate. P81 does not assume an unproved new convergence rate for its tighter relaxation.

---

## 12. Strict-improvement witness

For the box

\[
\pi=\frac12,
\qquad
q_{1,-}=q_{1,+}=\frac35,
\]

with all other channel coordinates free in $[0,1]$, and the uniform empirical sixteen-cell law,

\[
L_{80}(B)=0.
\]

But the event $X_1=0$ has exact model probability $2/5$, empirical probability $1/2$, and contains eight cells. Hence

\[
L_{81}(B)
\ge
\frac{|1/2-2/5|}{8}
=
\frac1{80}.
\]

The implementation evaluates all 80 cylinder events and returns exactly

\[
L_{81}(B)=\frac1{80}.
\]

**Classification:** project-derived exact algebraic witness, included as a regression test. It is not empirical evidence about consciousness.

---

## 13. P77/P79 statistical handoff

Let $\overline\varepsilon_{79}$ be the exact-rational P79 upper certificate for the P77 sampling radius. P81 preserves the established one-sided rejection gate:

\[
L_{81}(\mathcal B)>\overline\varepsilon_{79}
\Longrightarrow
 d_\infty(\widehat p,\mathcal M_{4,2})
>
\varepsilon_{n,K}(\alpha).
\]

**Classification:** downstream composition of P81's model-distance lower bound with the P79 sampling-radius upper bound and P77 rejection criterion.

**Dependencies:** [P77](proposition_77_full_law_model_set_separation.md), [P79](proposition_79_certified_sampling_radius.md).

---

## 14. Scientific boundary

The exact-rational nature of P81 concerns certification arithmetic, not ontology. P81 shows that a declared P75 parameter box can sometimes be separated from an empirical observed law more strongly by retaining projected-event constraints. It does not prove that the P75 latent variable is experiential, does not establish a physical law of consciousness, and does not imply that consciousness is outside physics when the P75 family fails.

The physical-to-experiential bridge remains open.

# Proposition 79: Robust Full-Law Rejection Under Bounded Target-View Dependence

## Status

**Proved conditional robustness theorem with executable finite-law checks.**

P75 through P78 use a four-view binary latent model whose target views are conditionally independent given a binary latent target state. P79 asks what remains valid when that assumption is not exact but the residual target-view dependence is independently bounded.

The result is deliberately one-sided. P79 does not claim that small residual dependence makes the P75 model true. It proves that a declared dependence allowance can only enlarge the admissible observed-law family by a controlled amount. Therefore a sufficiently large P77/P78 separation still rejects the model even after that allowance is granted.

The physical-to-experiential bridge remains open.

---

## 1. Conditional target-view laws and their independent projections

Let the latent target state be

\[
S\in\{-1,+1\},
\qquad
P(S=+1)=\pi.
\]

For each latent state \(s\), let

\[
R_s(x),
\qquad x\in\{0,1\}^4,
\]

be the true conditional joint law of the four observed target views. P79 does not initially assume that the coordinates of \(X=(X_1,X_2,X_3,X_4)\) are conditionally independent under \(R_s\).

Let

\[
R_{s,j}(x_j)
\]

be the one-view marginals of \(R_s\), and define the product projection

\[
\boxed{
\Pi_s(x)
=
\prod_{j=1}^4R_{s,j}(x_j).
}
\]

This product law preserves every one-view conditional marginal while removing residual dependence among the views.

The observed population law is

\[
P=(1-\pi)R_-+\pi R_+.
\]

The corresponding conditionally independent counterpart is

\[
Q=(1-\pi)\Pi_-+\pi\Pi_+.
\]

By construction, \(Q\) belongs to the P75 four-view conditionally independent model family \(\mathcal M_{4,2}\).

---

## 2. P79A: local-dependence defect

For either the \(L^\infty\) or \(L^1\) norm, define the conditional local-dependence defect

\[
\delta_s^{(p)}
=
\|R_s-\Pi_s\|_p,
\qquad p\in\{\infty,1\}.
\]

Define its prevalence-weighted version

\[
\boxed{
\rho_p
=
(1-\pi)\delta_-^{(p)}
+
\pi\delta_+^{(p)}.
}
\]

A scientific protocol may replace the exact value by an independently justified upper bound

\[
\rho_p\le\bar\rho_p.
\]

That allowance may come from external calibration, repeated-measurement validation, a preregistered design bound, or another independently justified source. It must not be tuned from the same observed discrepancy merely to avoid rejection.

---

## 3. P79B: bounded local dependence gives a model-neighborhood bound

Since

\[
P-Q
=
(1-\pi)(R_--\Pi_-)
+
\pi(R_+-\Pi_+),
\]

the triangle inequality gives

\[
\begin{aligned}
\|P-Q\|_p
&\le
(1-\pi)\|R_--\Pi_-\|_p
+
\pi\|R_+-\Pi_+\|_p\\
&=\rho_p.
\end{aligned}
\]

Because \(Q\in\mathcal M_{4,2}\),

\[
\boxed{
d_p(P,\mathcal M_{4,2})
\le
\rho_p
\le
\bar\rho_p.
}
\]

This is the central P79 population theorem.

It says that any four-view latent law whose conditional dependence defect is bounded by \(\bar\rho_p\) must lie inside the corresponding metric neighborhood of the P75 conditionally independent model family.

The converse is not asserted. A law near \(\mathcal M_{4,2}\) need not possess the particular latent conditional representation used above. P79 is therefore a valid rejection envelope, not a characterization theorem for every locally dependent latent-class model.

---

## 4. P79C: robust P77/P78 finite-sample rejection

Let \(\widehat P\) be the empirical observed law.

Suppose P78, or another mathematically valid procedure, supplies a certified lower bound

\[
L_p
\le
d_p(\widehat P,\mathcal M_{4,2}).
\]

Suppose the sampling analysis supplies a valid upper bound

\[
\varepsilon_p
\ge
\|\widehat P-P\|_p.
\]

Distance to a nonempty model set is 1-Lipschitz, so

\[
d_p(P,\mathcal M_{4,2})
\ge
d_p(\widehat P,\mathcal M_{4,2})-\|\widehat P-P\|_p.
\]

Hence

\[
\boxed{
d_p(P,\mathcal M_{4,2})
\ge
L_p-\varepsilon_p.}
\]

If the declared bounded-dependence model requires

\[
d_p(P,\mathcal M_{4,2})\le\bar\rho_p,
\]

then the finite-data robust rejection rule is

\[
\boxed{
L_p
>
\varepsilon_p+ar\rho_p
\quad\Longrightarrow\quad
\text{reject the bounded-dependence extension.}
}
\]

This rule has a simple interpretation:

- P78 contributes the certified model-distance lower bound;
- P77 contributes the sampling uncertainty budget;
- P79 contributes the independently declared target-view dependence budget.

Only separation beyond the sum of the two allowances certifies incompatibility.

---

## 5. P79D: why the dependence budget must be independent of the rejection discrepancy

If \(\bar\rho_p\) is chosen after seeing the observed P78 separation specifically so that

\[
L_p\le\varepsilon_p+\bar\rho_p,
\]

then the procedure can always be made non-rejecting by construction. Such a post hoc allowance would undermine the evidential force of the test in the same conceptual way that P71 rejects descriptor-derived target circularity.

Therefore P79 treats the dependence allowance as part of the declared target-measurement protocol. It may be estimated from an external calibration sample, bounded from instrument validation, specified from prior reproducibility work, or otherwise justified independently. The theorem itself does not prescribe one universal source for the allowance.

---

## 6. Executable implementation

The implementation

[`bounded_target_view_dependence.py`](../src/consciousness_bridge/bounded_target_view_dependence.py)

provides:

- exact construction of the product projection from a sixteen-cell conditional law;
- \(L^\infty\) and \(L^1\) conditional dependence defects;
- prevalence-weighted dependence budgets;
- construction of the observed law and its P75 independent counterpart;
- a robust finite-sample rejection certificate using
  \[
  L_p>\varepsilon_p+\bar\rho_p.
  \]

The executable tests verify that the constructed independent counterpart is a valid probability law, conditionally independent laws have zero defect, dependent laws have positive defect, the observed mixture distance never exceeds the weighted conditional defect, and equality at the robust threshold is treated as non-rejection.

---

## 7. Synthetic dependence example

A deliberately simple synthetic example sets \(X_1=X_2\) exactly inside one latent state while leaving \(X_3\) and \(X_4\) independent. The product projection preserves the one-view marginals but removes that residual pair dependence, producing a strictly positive local-dependence defect.

This example is only a theorem check. It is not an experiential target, a biological model, or evidence about consciousness.

---

## 8. Relation to latent-class local dependence literature

Conditional independence is a standard latent-class assumption, and local dependence is a well-known threat to latent-class validity. Existing work develops diagnostics, score tests, residual approaches, and extended latent-class models for such violations.

P79 does not claim that local-dependence modeling is new. Its repository-specific role is narrower:

- express target-view dependence as an explicit norm budget relative to the product projection;
- transport that budget through the latent mixture into an observed-law neighborhood around P75;
- combine that neighborhood with the P77 sampling radius and the P78 certified global model-distance lower bound;
- preserve a one-sided rejection interpretation without converting non-rejection into model truth.

Relevant methodological context includes:

- M. E. Berzofsky, P. P. Biemer, and W. D. Kalsbeek, "Local Dependence in Latent Class Analysis of Rare and Sensitive Events," *Sociological Methods & Research* 43(1), 2014, DOI: 10.1177/0049124113506407.
- A. Subtil, M. R. de Oliveira, and L. Goncalves, "Conditional dependence diagnostic in the latent class model: A simulation study," *Statistics & Probability Letters* 82(7), 1407-1412, 2012, DOI: 10.1016/j.spl.2012.03.030.
- E. S. Allman, C. Matias, and J. A. Rhodes, "Identifiability of parameters in latent structure models with many observed variables," *The Annals of Statistics* 37(6A), 3099-3132, 2009, DOI: 10.1214/09-AOS689.

The triangle inequality, convexity under mixture, and distance-to-set Lipschitz property used by P79 are standard mathematics.

---

## 9. Scientific boundaries

P79 does **not** establish that:

- the P75 latent variable is consciousness;
- target-view conditional dependence is actually bounded by any particular numerical value;
- a dependence allowance estimated from the same rejection discrepancy is evidentially independent;
- local dependence has a unique causal source;
- passing the robust test validates the target-measurement model;
- four binary target views form a complete measurement theory of experience;
- consciousness is reducible to current physics;
- consciousness is irreducible to physics;
- the physical-to-experiential bridge has been solved.

A failure to reject under the enlarged dependence allowance is inconclusive. It may reflect genuine compatibility, an allowance that is too broad, insufficient sample size, or a model failure not exposed by the current bound.

The physical-to-experiential bridge remains open.

---

Equation-level classification is recorded in [the P79 equation and provenance record](p79_equation_provenance.md).

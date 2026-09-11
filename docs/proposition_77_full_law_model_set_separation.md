# Proposition 77: Finite-Sample Full-Law Model-Set Separation

## Status

**Proved conditional theorem with an executable certification interface and exact finite-model-family regression tests.**

P77 is the full-law continuation of [P75](proposition_75_target_model_adequacy_overidentification.md) and [P76](proposition_76_finite_sample_target_model_adequacy.md).

P75 introduced an exact population reconstruction audit for the complete sixteen-cell law of four binary target views under one binary latent state with conditional independence. P76 then gave finite-sample rejection certificates for selected necessary polynomial consequences of that model. P76 explicitly left one gap open: an alternative can satisfy the tracked polynomial equations while still failing the stronger P75 full-law model-membership condition.

P77 closes that **logical** gap at the level of confidence-region inversion. It does not claim that continuous latent-model distance is computationally trivial. Instead, it separates the statistical theorem from the optimization requirement needed to evaluate it.

The central rule is:

\[
\boxed{
\mathcal C_n(\widehat P)\cap\mathcal M=\varnothing
\quad\Longrightarrow\quad
\text{reject the declared model set }\mathcal M
}
\]

with the same coverage level used to construct the finite-sample confidence region \(\mathcal C_n\).

Non-rejection remains inconclusive. P77 is not a model-acceptance procedure and does not identify any latent state with consciousness.

---

## 1. Setup

Let the observable alphabet be a finite set \(\mathcal X\) with

\[
|\mathcal X|=K.
\]

For the P75 four-binary-view model,

\[
K=2^4=16.
\]

Let \(P\in\Delta_{K-1}\) be the unknown population law and let \(\widehat P\) be the empirical law from \(n\) IID observations.

Let

\[
\mathcal M\subseteq\Delta_{K-1}
\]

be any declared nonempty statistical model set. For the immediate P75 application,

\[
\mathcal M_{4,2}
=
\left\{
Q:\
Q(x_1,x_2,x_3,x_4)
=
\sum_{s\in\{-1,+1\}}
\pi_s\prod_{j=1}^4Q_j(x_j\mid s)
\right\}.
\]

P77 is stated first for a generic finite-alphabet model set because the confidence-set logic does not depend on the special latent-class parameterization.

---

## 2. P77A: simultaneous empirical-law confidence region

For each cell \(x\in\mathcal X\), Hoeffding's inequality gives

\[
\Pr\left(
|\widehat P(x)-P(x)|>\varepsilon
\right)
\le 2e^{-2n\varepsilon^2}.
\]

A union bound over the \(K\) cells yields

\[
\boxed{
\varepsilon_{n,K}(\alpha)
=
\sqrt{\frac{\log(2K/\alpha)}{2n}}
}
\]

and

\[
\boxed{
\Pr\left(
\|\widehat P-P\|_\infty
\le
\varepsilon_{n,K}(\alpha)
\right)
\ge1-\alpha.
}
\]

The same event implies

\[
\boxed{
\|\widehat P-P\|_1
\le
\delta_{n,K}(\alpha)
:=
\min\{2,K\varepsilon_{n,K}(\alpha)\}.
}
\]

For \(K=16\), these are exactly the P76 empirical-law radii.

Define the simultaneous confidence regions

\[
\mathcal C_\infty
=
\left\{
Q\in\Delta_{K-1}:\|Q-\widehat P\|_\infty\le\varepsilon_{n,K}
\right\}
\]

and

\[
\mathcal C_1
=
\left\{
Q\in\Delta_{K-1}:\|Q-\widehat P\|_1\le\delta_{n,K}
\right\}.
\]

With probability at least \(1-\alpha\), the true population law belongs to both regions.

---

## 3. P77B: confidence-set inversion gives a full-law rejection theorem

Suppose the declared model is true, so

\[
P\in\mathcal M.
\]

On the P77A confidence event,

\[
P\in\mathcal C_\infty\cap\mathcal M
\]

and

\[
P\in\mathcal C_1\cap\mathcal M.
\]

Therefore either empty intersection is incompatible with the null model on that event:

\[
\boxed{
\mathcal C_\infty\cap\mathcal M=\varnothing
\quad\Longrightarrow\quad
P\notin\mathcal M
}
\]

and

\[
\boxed{
\mathcal C_1\cap\mathcal M=\varnothing
\quad\Longrightarrow\quad
P\notin\mathcal M.
}
\]

Thus the familywise confidence statement is inherited directly from the one empirical-law event. No additional multiplicity correction is introduced by testing model-set intersection.

This theorem is stronger in scope than checking a selected list of necessary polynomial constraints. It asks whether **any law in the complete declared model set** remains compatible with the finite-sample confidence region.

---

## 4. P77C: distance-to-model-set formulation

Define

\[
d_\infty(R,\mathcal M)
=
\inf_{Q\in\mathcal M}\|R-Q\|_\infty
\]

and

\[
d_1(R,\mathcal M)
=
\inf_{Q\in\mathcal M}\|R-Q\|_1.
\]

The confidence-region intersection tests are equivalent to

\[
\boxed{
d_\infty(\widehat P,\mathcal M)>\varepsilon_{n,K}}
\]

or

\[
\boxed{d_1(\widehat P,\mathcal M)>\delta_{n,K}}.
\]

Either inequality certifies rejection at confidence at least \(1-\alpha\).

The strict inequality matters. Equality means the closed confidence ball can still touch the model set.

---

## 5. P77D: distance to a set is 1-Lipschitz

For any two laws \(R,S\) and any nonempty model set \(\mathcal M\),

\[
d(R,\mathcal M)
\le
\|R-S\|+d(S,\mathcal M).
\]

Swapping \(R\) and \(S\) gives

\[
\boxed{
|d(R,\mathcal M)-d(S,\mathcal M)|
\le
\|R-S\|.
}
\]

Therefore, on the P77A event,

\[
\boxed{
|d_\infty(\widehat P,\mathcal M)-d_\infty(P,\mathcal M)|
\le
\varepsilon_{n,K}
}
\]

and

\[
\boxed{
|d_1(\widehat P,\mathcal M)-d_1(P,\mathcal M)|
\le
\delta_{n,K}.
}
\]

If the exact empirical model distance is available, P77 therefore gives an immediate finite-sample interval for the unknown population distance to the declared model set.

---

## 6. P77E: certified lower bounds are sufficient, optimizer values are not

For a continuous latent model, computing

\[
\inf_{Q\in\mathcal M}\|\widehat P-Q\|
\]

is a global optimization problem.

Suppose an algorithm returns a number \(L_\infty\) with a mathematically justified guarantee

\[
L_\infty
\le
d_\infty(\widehat P,\mathcal M).
\]

Then

\[
\boxed{
L_\infty>\varepsilon_{n,K}
\quad\Longrightarrow\quad
P\notin\mathcal M
}
\]

with confidence at least \(1-\alpha\). Likewise, a certified lower bound

\[
L_1\le d_1(\widehat P,\mathcal M)
\]

rejects whenever

\[
\boxed{L_1>\delta_{n,K}.}
\]

This is the computational interface implemented in the P77 source.

### Critical optimization direction

A numerical optimizer that returns a candidate \(Q^\star\in\mathcal M\) provides

\[
\|\widehat P-Q^\star\|
\ge
d(\widehat P,\mathcal M).
\]

That is an **upper bound** on the minimum distance. It cannot be used as though it were a lower bound. A poor optimizer can therefore never be allowed to create a false rejection certificate.

For a genuinely finite declared model family, exhaustive comparison does compute the exact minimum, and the executable P77 finite-family routine is fully decisive for that declared family.

For the continuous P75 latent-class family, a future global lower-bounding solver can plug into the P77 interface. Until such a lower bound is available, P77 refuses to convert an ordinary best-fit value into a certificate.

---

## 7. P77F: fixed-margin detection bounds

Suppose the population law is separated from the model set in \(L_\infty\):

\[
d_\infty(P,\mathcal M)\ge\tau>0.
\]

On the confidence event,

\[
d_\infty(\widehat P,\mathcal M)
\ge
\tau-\varepsilon_{n,K}.
\]

A sufficient condition for rejection is therefore

\[
\varepsilon_{n,K}<\frac{\tau}{2}.
\]

Equivalently, it is sufficient that

\[
\boxed{
n>
\frac{2\log(2K/\alpha)}{\tau^2}.}
\]

For \(L_1\), using the uncapped radius \(K\varepsilon_{n,K}\), a sufficient condition is

\[
K\varepsilon_{n,K}<\frac{\tau}{2},
\]

hence

\[
\boxed{
n>
\frac{2K^2\log(2K/\alpha)}{\tau^2}.}
\]

These are conservative fixed-margin design bounds. They are not claimed to be minimax optimal.

---

## 8. Relation to P75 and P76

P75 and P76 now have two different finite-data routes:

### P76 route: interpretable necessary constraints

P76 propagates uncertainty to covariance tetrads, cross-triple polynomials, and fourth-moment polynomials. These tests are transparent and can reject without solving a global latent-model optimization problem.

Their limitation is incompleteness: a misspecified law can in principle satisfy every tracked necessary polynomial while still fail the P75 full-law reconstruction condition.

### P77 route: complete declared model-set separation

P77 asks whether the finite-sample confidence region intersects the entire declared model set. If no intersection exists, the rejection is a full-law incompatibility result.

Its limitation is computational rather than statistical: for a continuous nonlinear latent model, one needs a sound global model-distance lower bound or an equivalent certified feasibility procedure.

The two routes are complementary. P76 can be computationally easier and diagnostically interpretable. P77 defines the stronger full-law target that a certified global solver should eventually evaluate.

---

## 9. Synthetic finite-family example

Consider a two-cell empirical law

\[
\widehat P=(0.9,0.1)
\]

and a declared finite model family containing only

\[
Q=(0.5,0.5).
\]

Then

\[
d_\infty(\widehat P,\mathcal M)=0.4,
\qquad
d_1(\widehat P,\mathcal M)=0.8.
\]

At \(n=100\) and \(\alpha=0.05\), the P77 radii are smaller than these distances, so the confidence region is disjoint from the finite model family and rejection is certified.

At a much smaller sample size, the same empirical discrepancy need not clear the sampling radius. The correct conclusion is then only non-rejection by the P77 certificate.

This example tests the theorem mechanics. It is not an empirical consciousness model.

---

## 10. Statistical and scientific boundaries

P77 does not establish that:

- the P75 binary latent model is correct in any empirical dataset;
- a best-fit local optimizer has found the global minimum distance;
- an optimizer upper bound can be used as a rejection lower bound;
- non-rejection means model acceptance;
- the latent state has experiential semantics;
- the target channel is biologically or clinically valid;
- failure of the target-measurement model implies that consciousness lies outside physics;
- the physical-to-experiential bridge has been solved.

A P77 rejection has the narrower meaning that, under the declared IID sampling model and a sound model-distance or feasibility certificate, the true observed law is incompatible with the declared statistical target-measurement model at the stated confidence level.

---

## 11. Literature and provenance boundary

The following ingredients are standard and are not claimed as new discoveries:

- Hoeffding concentration and union bounds for finite empirical distributions;
- inversion of confidence regions into hypothesis tests;
- distance to a nonempty set being 1-Lipschitz under a norm-induced metric;
- minimum-distance and goodness-of-fit ideas for multinomial models;
- the established difficulty of latent-class goodness-of-fit in sparse or nonregular settings;
- bootstrap and resampling approaches used in latent-class model assessment.

Relevant methodological context includes:

1. L. M. Collins, P. L. Fidler, S. E. Wugalter, and J. D. Long, "Goodness-of-Fit Testing for Latent Class Models," *Multivariate Behavioral Research* 28(3), 375-389, 1993. DOI: 10.1207/s15327906mbr2803_4.
2. R. Langeheine, J. Pannekoek, and F. van de Pol, "Bootstrapping Goodness-of-Fit Measures in Categorical Data Analysis," *Sociological Methods & Research* 24(4), 492-516, 1996. DOI: 10.1177/0049124196024004004.
3. G. H. van Kollenburg, J. Mulder, and J. K. Vermunt, "Assessing Model Fit in Latent Class Analysis When Asymptotics Do Not Hold," *Methodology* 11(2), 65-79, 2015. DOI: 10.1027/1614-2241/a000093.
4. E. S. Allman, C. Matias, and J. A. Rhodes, "Identifiability of Parameters in Latent Structure Models with Many Observed Variables," *The Annals of Statistics* 37(6A), 3099-3132, 2009. DOI: 10.1214/09-AOS689.

The repository-specific contribution is the explicit placement of a **full-law confidence-region/model-set separation gate** after the P71-P76 target-validity sequence, together with a certification interface that prevents ordinary optimizer upper bounds from being misreported as evidence of model incompatibility.

---

## 12. Reproducibility

Implementation:

- [`full_law_model_set_separation.py`](../src/consciousness_bridge/full_law_model_set_separation.py)

Regression tests:

- [`test_full_law_model_set_separation.py`](../tests/test_full_law_model_set_separation.py)

Immediate predecessors:

- [P75 target-model adequacy and four-view overidentification](proposition_75_target_model_adequacy_overidentification.md)
- [P76 finite-sample target-model adequacy rejection](proposition_76_finite_sample_target_model_adequacy.md)

The next computational problem is to construct a sound global lower-bounding or feasibility solver for the continuous P75 four-view latent model so that the P77 full-law criterion can be evaluated without relying on uncertified local optimization.

The physical-to-experiential bridge remains open.

# P78 Equation and Provenance Record

This record classifies the mathematical ingredients used in [Proposition 78](proposition_78_certified_continuous_model_separation.md). It distinguishes standard results from repository-specific assembly and consequences.

## 1. Four-view binary latent-class parameterization

\[
F_x(\theta)
=
(1-\pi)
\prod_{j=1}^4q_{j,-}^{x_j}(1-q_{j,-})^{1-x_j}
+
\pi
\prod_{j=1}^4q_{j,+}^{x_j}(1-q_{j,+})^{1-x_j}.
\]

**Classification:** standard two-component mixture of Bernoulli product distributions / binary latent-class model.

The broader identifiability literature includes Allman, Matias, and Rhodes (2009), DOI 10.1214/09-AOS689. P78 does not claim this latent-class parameterization as new.

## 2. Multi-affine structure

Each observed cell probability is affine in every one of the nine parameters when the remaining eight coordinates are fixed.

**Classification:** direct algebraic observation for the P75 parameterization.

The general fact that a multi-affine map on a hyperrectangle is controlled by its vertex values is standard. A representative reference is Belta, Habets, and Kumar (2002), DOI 10.1109/CDC.2002.1184551.

## 3. Exact boxwise cell interval

For an axis-aligned parameter box \(B\), P78 computes

\[
I_x(B)=[m_x(B),M_x(B)]
\]

as the exact scalar range hull of \(F_x\) over the box.

**Classification:** standard multi-affine endpoint/vertex extremum specialized to the product structure of the P75 model.

The implementation avoids explicit enumeration of all \(2^9\) vertices by first taking exact nonnegative product extrema in the two latent components and then extremizing the remaining affine prevalence coordinate at its endpoints.

## 4. Boxwise L-infinity lower bound

\[
L_\infty(B;\widehat P)
=
\max_x\operatorname{dist}(\widehat P(x),I_x(B)).
\]

Then

\[
L_\infty(B;\widehat P)
\le
\inf_{\theta\in B}\|\widehat P-F(\theta)\|_\infty.
\]

**Classification:** elementary interval-enclosure lower bound.

P78's role is to use it as a certified model-distance lower bound for the particular P75 model family required by the P77 rejection theorem.

## 5. Global partition lower bound

For a finite partition \(\mathcal B\) of \([0,1]^9\),

\[
L_{\mathcal B}(\widehat P)
=
\min_{B\in\mathcal B}L_\infty(B;\widehat P)
\le
d_\infty(\widehat P,\mathcal M_{4,2}).
\]

**Classification:** standard branch-and-bound lower-bound aggregation.

Complete continuous global search and interval branch-and-bound are established subjects. P78 does not claim the general branch-and-bound principle as new. A representative survey is Neumaier (2004), *Acta Numerica*.

## 6. Candidate upper bound

For every explicit admissible parameter vector \(\theta_c\),

\[
d_\infty(\widehat P,\mathcal M_{4,2})
\le
\|\widehat P-F(\theta_c)\|_\infty.
\]

**Classification:** standard definition-of-infimum consequence.

This direction is scientifically important because it prevents a local best-fit objective value from being misused as a rejection certificate.

## 7. Parameter-to-law Lipschitz bound

For every observed cell \(x\),

\[
\left|\frac{\partial F_x}{\partial\theta_r}\right|\le1,
\]

hence

\[
|F_x(\theta)-F_x(\theta')|
\le\|\theta-\theta'\|_1.
\]

**Classification:** elementary derivative bound specialized to the P75 parameterization.

## 8. Mesh-gap bound

With

\[
\eta(\mathcal B)
=
\max_{B\in\mathcal B}\sum_r(u_r-\ell_r),
\]

P78 derives

\[
0
\le
d_\infty(\widehat P,\mathcal M_{4,2})
-L_{\mathcal B}(\widehat P)
\le
\eta(\mathcal B).
\]

**Classification:** repository-specific specialization and consequence of the preceding standard interval and Lipschitz ingredients.

The inequality is not presented as a new theorem of global optimization in general. Its value here is that it gives an explicit convergence statement for the P75 model-distance certificate used by P77.

## 9. P77 rejection handoff

If

\[
L_{\mathcal B}>\overline\varepsilon
\ge\varepsilon_{n,16}(\alpha),
\]

then

\[
d_\infty(\widehat P,\mathcal M_{4,2})
>
\varepsilon_{n,16}(\alpha),
\]

and P77 rejects the declared model set at its stated confidence level.

**Classification:** repository-specific composition of the P78 optimization certificate with the already-proved P77 statistical rejection theorem.

The requirement that \(\overline\varepsilon\) itself be a valid upper bound is deliberate. An ordinary floating approximation is not promoted to a formal statistical certificate merely by converting it to a rational representation.

## 10. Polynomial epigraph formulation

\[
\begin{aligned}
\min_{\theta,t}\quad&t\\
\text{s.t.}\quad
&-t\le\widehat P(x)-F_x(\theta)\le t,\\
&0\le\theta_r\le1.
\end{aligned}
\]

**Classification:** standard polynomial-optimization reformulation of an L-infinity distance problem.

The feasible region is compact and semialgebraic. Moment and sum-of-squares hierarchies for such global polynomial optimization problems are standard; see Lasserre (2001), DOI 10.1137/S1052623400366802.

P78's dependency-light implementation uses exact-rational box bounds instead of introducing an SDP dependency. Moment-SOS remains a principled alternative for future stronger lower bounds.

## 11. Naive global convexification boundary

Because the full P75 cube includes degenerate parameter vertices that generate deterministic observed laws, the convex hull of the complete model image contains the simplex vertices and therefore equals the full observed simplex.

**Classification:** elementary consequence of the declared parameter domain and convexity.

This explains why one global convex-hull relaxation cannot provide a nontrivial full-simplex separation certificate. P78 preserves nonconvex structure through local boxes.

## 12. Repository-specific contribution

The P78 contribution is the following assembly within the Mathematical Consciousness Bridge architecture:

1. expose the exact multi-affine structure of the P75 four-view latent map;
2. derive exact rational cell enclosures without exhaustive vertex enumeration;
3. convert those enclosures into valid continuous-family L-infinity lower bounds;
4. aggregate them over a complete parameter-box partition;
5. derive an explicit mesh-gap guarantee;
6. implement the resulting branch-and-bound certificate using exact `Fraction` arithmetic for empirical counts and dyadic boxes;
7. hand the certified lower bound to P77 while preserving the strict distinction between optimization lower bounds, candidate upper bounds, and statistical sampling-radius bounds.

These steps do not constitute a consciousness ontology. The physical-to-experiential bridge remains open.

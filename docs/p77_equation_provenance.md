# P77 Equation and Provenance Record

This record classifies the mathematical ingredients used in **Proposition 77: Finite-Sample Full-Law Model-Set Separation**.

The purpose is to distinguish standard probability/statistics facts from the repository-specific way they are assembled into the physical-to-experiential bridge test architecture.

## 1. Finite-alphabet simultaneous confidence radius

For an alphabet of size \(K\), P77 uses

\[
\varepsilon_{n,K}(\alpha)
=
\sqrt{\frac{\log(2K/\alpha)}{2n}}.
\]

This follows from Hoeffding's inequality for each empirical cell frequency followed by a union bound over \(K\) cells.

**Classification:** standard probability result.

The induced \(L_1\) radius

\[
\delta_{n,K}(\alpha)
=
\min\{2,K\varepsilon_{n,K}(\alpha)\}
\]

is the deterministic consequence of

\[
\|v\|_1\le K\|v\|_\infty
\]

for a \(K\)-vector, together with the maximum possible \(L_1\) distance between probability distributions.

**Classification:** standard norm inequality.

For \(K=16\), these radii reduce exactly to the empirical-law event already used in P76.

## 2. Confidence-region inversion

Let \(\mathcal C_n(\widehat P)\) be a confidence region with

\[
\Pr(P\in\mathcal C_n)\ge1-\alpha
\]

and let \(\mathcal M\) be a declared model set. Then

\[
\mathcal C_n\cap\mathcal M=\varnothing
\]

implies rejection of \(P\in\mathcal M\) at the same coverage level.

**Classification:** standard confidence-set inversion / hypothesis-testing logic.

P77 does not claim this principle as a new statistical theorem.

## 3. Distance-to-model-set formulation

P77 defines

\[
d_p(R,\mathcal M)=\inf_{Q\in\mathcal M}\|R-Q\|_p.
\]

For the closed norm ball around \(\widehat P\), model-set disjointness is equivalent to the corresponding empirical model distance exceeding the sampling radius.

**Classification:** standard metric geometry.

## 4. One-Lipschitz distance transport

For any nonempty set \(\mathcal M\),

\[
|d(R,\mathcal M)-d(S,\mathcal M)|\le\|R-S\|.
\]

This follows immediately from the triangle inequality and then swapping \(R\) and \(S\).

**Classification:** standard metric-space fact.

Its P77 use is to transport a finite-sample empirical-law confidence event directly into a confidence interval for population distance to the declared model set.

## 5. Certified lower-bound rejection rule

If an algorithm supplies a sound lower bound

\[
L\le d(\widehat P,\mathcal M)
\]

and

\[
L>r_n,
\]

where \(r_n\) is the sampling radius in the same norm, then

\[
d(\widehat P,\mathcal M)>r_n
\]

and the confidence region is disjoint from \(\mathcal M\).

**Classification:** direct consequence of confidence-region inversion and order logic.

The important computational boundary is the direction of optimization bounds. For a candidate model \(Q^\star\in\mathcal M\),

\[
d(\widehat P,\mathcal M)
\le
\|\widehat P-Q^\star\|.
\]

Therefore an ordinary best-fit candidate provides an **upper** bound, not a rejection lower bound.

**Classification:** standard optimization bound direction, emphasized as a scientific safeguard.

## 6. Fixed-margin sample-size bounds

If

\[
d_\infty(P,\mathcal M)\ge\tau
\]

and

\[
\varepsilon_{n,K}<\tau/2,
\]

then on the simultaneous confidence event

\[
d_\infty(\widehat P,\mathcal M)
\ge
\tau-\varepsilon_{n,K}
>
\varepsilon_{n,K}.
\]

Solving for \(n\) gives the sufficient condition

\[
 n>
\frac{2\log(2K/\alpha)}{\tau^2}.
\]

Similarly, under the uncapped \(L_1\) radius,

\[
 n>
\frac{2K^2\log(2K/\alpha)}{\tau^2}
\]

is sufficient for fixed \(L_1\) separation margin \(\tau\).

**Classification:** elementary consequence of the preceding concentration and Lipschitz bounds. These are conservative sufficient design bounds, not minimax-optimality claims.

## 7. Relationship to established latent-class goodness-of-fit methods

Latent-class model assessment has a substantial existing literature using likelihood-ratio statistics, Pearson statistics, residual methods, limited-information procedures, parametric bootstrap, and posterior predictive checks. Sparse tables and nonregular latent-variable parameter points can make simple asymptotic chi-square calibration unreliable.

Relevant methodological sources include:

1. Collins, L. M., Fidler, P. L., Wugalter, S. E., & Long, J. D. (1993). Goodness-of-Fit Testing for Latent Class Models. *Multivariate Behavioral Research*, 28(3), 375-389. DOI: 10.1207/s15327906mbr2803_4.
2. Langeheine, R., Pannekoek, J., & van de Pol, F. (1996). Bootstrapping Goodness-of-Fit Measures in Categorical Data Analysis. *Sociological Methods & Research*, 24(4), 492-516. DOI: 10.1177/0049124196024004004.
3. van Kollenburg, G. H., Mulder, J., & Vermunt, J. K. (2015). Assessing Model Fit in Latent Class Analysis When Asymptotics Do Not Hold. *Methodology*, 11(2), 65-79. DOI: 10.1027/1614-2241/a000093.
4. Allman, E. S., Matias, C., & Rhodes, J. A. (2009). Identifiability of Parameters in Latent Structure Models with Many Observed Variables. *The Annals of Statistics*, 37(6A), 3099-3132. DOI: 10.1214/09-AOS689.

P77 does not claim to replace these established methods. Its role is different: it gives a finite-sample confidence-region separation statement that does not require an asymptotic reference distribution and that interfaces directly with the P75 full observed-law model set.

## 8. Repository-specific contribution

The repository-specific contribution of P77 is the assembly of the standard ingredients above into the P71-P77 target-validity branch as an explicit **full-law model-set separation gate**.

The new architectural point is:

- P75 defines the complete population model-membership target;
- P76 supplies interpretable finite-sample necessary-constraint rejection tests;
- P77 states the stronger finite-sample full-law criterion;
- P77 explicitly requires a sound lower bound or equivalent certified feasibility result before continuous-model rejection is allowed;
- an uncertified local optimizer is prohibited from being interpreted as a rejection certificate.

This is a methodological extension of the repository's bridge-test architecture, not a claim that confidence-set inversion, norm concentration, minimum distance, or latent-class goodness-of-fit were invented here.

The physical-to-experiential bridge remains open.

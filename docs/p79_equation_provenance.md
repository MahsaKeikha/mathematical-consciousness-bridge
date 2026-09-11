# P79 equation and provenance record

## Purpose

P79 extends the P75-P78 target-measurement branch from exact conditional independence to a declared bounded local-dependence regime. It is a robustness result, not a new latent-class ontology.

## Equation classification

### Product projection

\[
\Pi_s(x)=\prod_{j=1}^4R_{s,j}(x_j).
\]

**Status:** standard product construction from fixed marginals.

**Role in P79:** defines the conditionally independent counterpart of each latent-state target-view law while preserving its one-view marginals.

---

### Conditional local-dependence defect

\[
\delta_s^{(p)}=\|R_s-\Pi_s\|_p,
\qquad p\in\{\infty,1\}.
\]

**Status:** standard norm discrepancy.

**Role in P79:** gives an explicit quantitative allowance for residual target-view dependence instead of treating conditional independence as exact by default.

---

### Weighted dependence budget

\[
\rho_p=(1-\pi)\delta_-^{(p)}+\pi\delta_+^{(p)}.
\]

**Status:** direct mixture-weighted definition.

**Role in P79:** transports latent-state dependence allowances into the observed mixture scale.

---

### Observed-law neighborhood bound

With

\[
P=(1-\pi)R_-+\pi R_+,
\qquad
Q=(1-\pi)\Pi_-+\pi\Pi_+\in\mathcal M_{4,2},
\]

the triangle inequality gives

\[
\boxed{
\|P-Q\|_p
\le
(1-\pi)\|R_--\Pi_-\|_p
+
\pi\|R_+-\Pi_+\|_p
=
\rho_p.
}
\]

Therefore

\[
\boxed{
d_p(P,\mathcal M_{4,2})\le\rho_p.}
\]

**Status:** standard norm convexity and distance-to-set reasoning.

**Repository-specific role:** converts a declared target-view local-dependence budget into a robustness envelope around the specific P75 observed-law model family.

---

### Robust finite-sample rejection gate

If

\[
L_p\le d_p(\widehat P,\mathcal M_{4,2}),
\qquad
\|\widehat P-P\|_p\le\varepsilon_p,
\qquad
\rho_p\le\bar\rho_p,
\]

then the 1-Lipschitz property of distance to a nonempty set gives

\[
\boxed{
d_p(P,\mathcal M_{4,2})\ge L_p-\varepsilon_p.}
\]

Hence

\[
\boxed{
L_p>\varepsilon_p+\bar\rho_p
\Longrightarrow
\text{the bounded-dependence extension is incompatible.}
}
\]

**Status:** standard metric transport combined with the P79 dependence envelope.

**Repository-specific role:** provides the direct P78 to P77 to P79 handoff. The model-distance lower bound, sampling-radius upper bound, and dependence allowance must each be valid in the required direction.

---

## Evidential status of the dependence budget

The value \(\bar\rho_p\) is not identified by P79 from the same discrepancy used for rejection. It is a declared or independently justified scientific input. Examples of admissible sources include external calibration, preregistered instrument validation, repeated-measurement studies, or another independent protocol.

Choosing the allowance after seeing the P78 separation simply to avoid rejection would weaken the evidential interpretation and is explicitly outside the intended use of the theorem.

---

## Literature context

Conditional independence and local dependence in latent-class models are established topics. P79 therefore does not claim the general idea of local-dependence modeling as new.

Useful methodological context:

1. Berzofsky, M. E., Biemer, P. P., and Kalsbeek, W. D. (2014). Local Dependence in Latent Class Analysis of Rare and Sensitive Events. *Sociological Methods & Research*, 43(1). DOI: 10.1177/0049124113506407.
2. Subtil, A., de Oliveira, M. R., and Goncalves, L. (2012). Conditional dependence diagnostic in the latent class model: A simulation study. *Statistics & Probability Letters*, 82(7), 1407-1412. DOI: 10.1016/j.spl.2012.03.030.
3. Allman, E. S., Matias, C., and Rhodes, J. A. (2009). Identifiability of parameters in latent structure models with many observed variables. *The Annals of Statistics*, 37(6A), 3099-3132. DOI: 10.1214/09-AOS689.

These sources establish broader latent-class and local-dependence context. They are not claimed to contain the repository's P79 robustness envelope or its P77/P78 integration.

---

## Repository-specific contribution

P79 contributes the following assembly inside the Mathematical Consciousness Bridge architecture:

- a target-view dependence defect defined relative to the product projection of each latent-state conditional law;
- a prevalence-weighted observed-law neighborhood theorem around the P75 model family;
- a robust rejection rule that adds the independently declared dependence budget to the P77 finite-sample uncertainty radius;
- a strict one-sided interpretation in which non-rejection remains inconclusive;
- an explicit anti-circularity rule preventing the dependence allowance from being tuned from the same discrepancy it is supposed to excuse.

The physical-to-experiential bridge remains open.

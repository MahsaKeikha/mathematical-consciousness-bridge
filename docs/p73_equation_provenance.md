# P73 equation and provenance record

This page separates standard latent-variable mathematics from the repository-specific role of Proposition 73 in the physical-to-experiential bridge test architecture.

## Claim classification

| P73 object | Role | Status and provenance |
| --- | --- | --- |
| \(Y_i=ZN_i\) with mutually independent binary noises independent of \(Z\) | three-view target-measurement model | declared structural assumption, not inferred by P73 |
| \(r_i=\mathbb E[N_i]\), \(\gamma_i=|r_i|\) | signed reliability and P72 stability magnitude | definitions specialized to the binary symmetric channel |
| \(m_{ij}=\mathbb E[Y_iY_j]=r_ir_j\) | observable pairwise-moment factorization | elementary consequence of the declared conditional-independence model |
| two-view continuum \(\gamma_1\gamma_2=|m_{12}|\) | non-identifiability boundary | P73 explicit impossibility construction |
| three-view formulas for \(\gamma_1,\gamma_2,\gamma_3\) | exact stability identification | elementary algebraic identification under the P73 model |
| signed vector identified up to one global sign | label-orientation ambiguity | algebraic consequence of equal pairwise products |
| \(\eta_i=(1-\gamma_i)/2\) after declaring \(r_i>0\) | oriented symmetric error rate | direct binary-channel identity plus external orientation assumption |
| \(\varepsilon_n(\alpha)=\sqrt{2\log(6/\alpha)/n}\) | simultaneous pair-moment radius | standard Hoeffding inequality plus union bound |
| propagated intervals for \(\gamma_i\) | finite target-channel stability certificate | P73 interval construction from simultaneous moment bounds |
| confidence handoff \(1-(\alpha_c+\alpha_b)\) | calibration-to-bridge accounting | standard union bound assembled into the P72-P73 experimental workflow |

## Standard mathematical ingredients

### Repeated conditionally independent measurements

The idea that multiple imperfect observers can identify latent-response structure under suitable conditional-independence assumptions belongs to established latent-class statistics. P73 uses a particularly transparent binary symmetric specialization so every identifiability step can be written in closed form.

Classical observer-error context:

A. P. Dawid and A. M. Skene, "Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm," *Journal of the Royal Statistical Society: Series C (Applied Statistics)* 28(1), 1979, 20-28. DOI: `10.2307/2346806`.

Broader latent-structure identifiability context:

E. S. Allman, C. Matias, and J. A. Rhodes, "Identifiability of Parameters in Latent Structure Models with Many Observed Variables," *The Annals of Statistics* 37(6A), 2009, 3099-3132. DOI: `10.1214/09-AOS689`.

These sources provide methodological context. The exact P73 formulas are derived directly from the declared three-view binary model and do not depend on importing an external black-box identifiability theorem.

### Hoeffding concentration

For each pair, the product \(Y_iY_j\) is bounded in \([-1,1]\). P73 applies the standard Hoeffding inequality and a union bound over the three pairwise moments.

Standard reference:

W. Hoeffding, "Probability Inequalities for Sums of Bounded Random Variables," *Journal of the American Statistical Association* 58(301), 1963, 13-30.

## Repository-original role

P73 does not claim novelty for conditional-independence latent models, pairwise moment algebra, latent-label permutation ambiguity, Hoeffding concentration, or union bounds.

The repository-specific contribution is the role these tools play in closing a precise assumption left open by P72:

\[
\boxed{
\text{P71 target provenance}
\to
\text{P72 target-channel robustness}
\to
\text{P73 channel-stability identifiability}
\to
\text{finite stability certificate}
\to
\text{measurement-aware bridge design}.
}
\]

The important methodological result is that the stability magnitude needed by P72 can be identifiable even when latent semantic label orientation is not. That prevents the bridge experiment from requiring more latent-label information than its attenuation bound actually uses.

## Identifiability boundary

P73 deliberately records both a positive and a negative result.

With two heterogeneous views,

\[
|m_{12}|=\gamma_1\gamma_2
\]

contains one observable equation for two unknown stabilities. Without another assumption, individual reliabilities are not identified.

With three nonzero conditionally independent binary symmetric views,

\[
|m_{12}|=\gamma_1\gamma_2,
\quad
|m_{13}|=\gamma_1\gamma_3,
\quad
|m_{23}|=\gamma_2\gamma_3,
\]

and the three magnitudes are algebraically identified.

This threshold is model-specific. It is not a claim that three measurements identify arbitrary multi-class, dependent, instance-dependent, or nonstationary target-noise channels.

## Scientific boundary

P73 is conditional on its measurement model. Shared rater biases, correlated errors, physical-state-dependent reporting, intervention-dependent noise, temporal drift, or class-asymmetric confusion can invalidate the pairwise factorization used by the theorem.

The latent target remains a declared scientific target, not an ontological identification with consciousness. P73 improves the auditability of target measurement. It does not establish the physical-to-experiential bridge.

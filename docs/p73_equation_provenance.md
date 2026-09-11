# P73 Equation and Provenance Record

This document classifies the mathematics used in Proposition 73 so that standard latent-variable results are not presented as repository-original discoveries.

## Scientific scope

P73 studies one fixed physical stratum \(T=t\) with a binary latent target \(S\in\{-1,+1\}\) and three binary observed target views. The views are assumed conditionally independent given \(S\) inside the declared model.

The latent state is a statistical target variable. It is not identified with consciousness or experiential ground truth by the theorem.

## Equation classification

| P73 object | Classification | Role |
| --- | --- | --- |
| \(\mathbb E[X_j\mid S]=a_j+b_jS\) | standard binary-channel parameterization | represents each binary measurement channel |
| \(C_{ij}=b_ib_j(1-m^2)\) | direct moment consequence of the declared conditional-independence model | converts observable pair covariances into loading products |
| \(M_{123}=-2m(1-m^2)b_1b_2b_3\) | direct moment consequence of the declared model | supplies the third-order information needed for explicit inversion |
| \(q=M_{123}^2/(C_{12}C_{13}C_{23})\) | repository derivation specialized to the binary three-view parameterization | isolates latent imbalance |
| \(m^2=q/(q+4)\), \(v=4/(q+4)\) | repository algebraic inversion | recovers latent prevalence magnitude and variance |
| explicit formulas for \(b_1,b_2,b_3,a_1,a_2,a_3\) | repository specialization of standard latent-class identifiability | reconstructs the declared channels up to common label swap |
| global latent-label permutation | standard latent-class symmetry | states the unavoidable semantic ambiguity |
| \(\gamma_j=|b_j|\) | repository connection to P72 | identifies each binary P72 channel-stability coefficient |
| \(\gamma_{123}\ge\max_j\gamma_j\) | standard TV data processing applied to the recovered joint channel | shows the joint view is at least as stable as any marginal view |
| two-view law \(P(x_1,x_2)=\tfrac14(1+b_1b_2x_1x_2)\) | explicit repository counterexample family | proves that two views do not identify individual channel stabilities without extra assumptions |

## External methodological context

### Dawid and Skene 1979

A. P. Dawid and A. M. Skene, "Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm," *Applied Statistics* 28(1), 20-28 (1979). DOI: 10.2307/2346806.

Role here: methodological precedent for estimating observer error rates in a latent-response model when the true response is not directly observed. P73 does not use the Dawid-Skene EM proof as its own proof.

### Allman, Matias, and Rhodes 2009

E. S. Allman, C. Matias, and J. A. Rhodes, "Identifiability of Parameters in Latent Structure Models with Many Observed Variables," *The Annals of Statistics* 37(6A), 3099-3132 (2009). DOI: 10.1214/09-AOS689.

Role here: general identifiability context for latent-structure models whose observed variables have conditional-independence structure, including identifiability up to hidden-class label permutations. P73 gives a direct binary three-view moment inversion rather than claiming the general identifiability principle as new.

## Repository-original bridge contribution

The new contribution is the integration of a specialized three-view latent-class inversion into the P71-P72 bridge-test architecture:

1. P71 requires target provenance not to make the physical factorization true by definition.
2. P72 shows that a noisy target channel can attenuate or erase bridge evidence and introduces target-channel stability.
3. P73 gives a concrete model in which that stability can be identified from target-side observations rather than merely assumed.
4. P73 proves an explicit two-view counterexample showing why repeated agreement from only two channels cannot generally identify their individual reliability.

This sequence does not validate the latent target itself. It separates target provenance, target observation, channel identifiability, and eventual bridge testing into distinct mathematical obligations.

## Reproducibility paths

- Proof: [`proposition_73_target_channel_identifiability.md`](proposition_73_target_channel_identifiability.md)
- Implementation: [`../src/consciousness_bridge/target_channel_identifiability.py`](../src/consciousness_bridge/target_channel_identifiability.py)
- Tests: [`../tests/test_target_channel_identifiability.py`](../tests/test_target_channel_identifiability.py)
- Figure: [`figures/p73_target_channel_identifiability.svg`](figures/p73_target_channel_identifiability.svg)

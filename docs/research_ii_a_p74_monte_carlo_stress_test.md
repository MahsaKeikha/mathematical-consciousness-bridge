# P74 repeated-sampling stress test (independent gate audit)

**Date:** 2026-10-20. **Status:** independently implemented synthetic stress test, not a run of the official repository source tests or proof of psychological construct validity.

A seeded Monte Carlo implementation generated independent binary latent-class samples with three conditionally independent binary measurements. The P74 conservative covariance nondegeneracy gate was evaluated with 95% nominal confidence. The test used 300 replicates at n=1,000 and 10,000; 100 replicates at n=100,000 for each of three signal regimes (2,100 trials total).

| Regime | n=1,000 gate pass | n=10,000 | n=100,000 |
|---|---:|---:|---:|
| Strong loadings (0.9,0.85,0.8), prevalence 0.5 | 0/300 | 300/300 | 100/100 |
| Moderate loadings (0.7,0.65,0.6), prevalence 0.35 | 0/300 | 0/300 | 100/100 |
| Weak loading (0.05,0.8,0.75), prevalence 0.5 | 0/300 | 0/300 | 0/100 |

All three true pairwise covariances fell within the conservative calculated covariance bands in all simulated trials. This finite empirical observation **does not prove exact or nominal interval coverage**. The exercise did not examine the full P74 prevalence/channel confidence orbit, misspecified conditional independence, or real participant data.

**Interpretation:** A failure to pass the conservative nondegeneracy gate means *not certified by these observations*. It does not demonstrate absence of a target, falsity of the underlying latent model, or failure of the mathematics. For the journal manuscript this should be described as a sensitivity and feasibility limitation rather than evidence of discovery about consciousness.

Reproducibility materials: a seed-fixed `p74_monte_carlo_audit.py` and tabulated CSV were generated as part of the paper-preparation audit. The script has not been merged into the repository, and repository CI has not been run against it.

## Publication-facing interpretation and quality control

These nine simulation conditions test the **gate's empirical triggering frequency**, not the confidence-set coverage of the full latent parameter orbit. The three modeled regimes have minimum true absolute pairwise covariance 0.68, 0.3549, and 0.0375, respectively. At n=100,000, the computed covariance error allowance remains approximately 0.128891, which is greater than the weakest signal. That observation explains why gate failure in the weak setting is expected; it should not be described as a failure of identifiability at the population level.

The assumption that all three view errors are conditionally independent is central. Real psychological reports may share rater biases, shared stimuli, common contexts, or correlated noise. A covariance gate that passes does **not** independently verify that assumption. It is therefore scientifically inappropriate to claim validated psychological measurement from the current synthetic test.

For external review, preserve the exact simulation seed, source script, dependency versions, raw counts, and source revision. Until those are archived and checked, these numbers should be labeled **supporting sensitivity illustrations**, not reproduced independent empirical findings.

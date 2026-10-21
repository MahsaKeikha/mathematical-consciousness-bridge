# P20 and P74 independent numerical checkpoint audit

**Scope:** independent arithmetic check of published numerical formulas, conducted for Research II-A manuscript preparation on 2026-10-19. This is not a full execution of the repository test suite and does not verify empirical claims.

## P20 published synthetic checkpoint

Source: [P20 theorem record](proposition_20_finite_sample_residual_certification.md), [P20 implementation](../src/consciousness_bridge/finite_sample_residual_certification.py).

Use `n=10000`, `alpha=0.05`, `d_Omega=2`, `d_T=1`, `d_E=2`, `M=4`, and `Ihat=ln(2)`.

Independent evaluation of the published formulas yields:

| Quantity | Value |
|---|---:|
| `tau_n = (M/2)*sqrt(ln(2M/alpha)/(2n))` | `0.03185961021492205` |
| `Delta_CMI(tau_n)` | `0.45844563704418860` nats |
| `L_n = ln(2)-Delta_CMI(tau_n)` | `0.23470154351575667` nats |

The positive lower bound is a synthetic mathematical rejection certificate for the declared `T` **only under the explicitly stated finite-alphabet IID assumptions**. It does not establish that an observed experiential target is valid or that consciousness is nonphysical.

## P74 sufficient sample-size arithmetic

Source: [P74 theorem record](proposition_74_finite_sample_target_channel_recovery.md), [P74 implementation](../src/consciousness_bridge/finite_sample_target_channel_recovery.py).

The published conservative sufficient gate uses `n > 1152*ln(16/alpha)/c_min²`. For `alpha=0.05`, independently calculated minimum integer `n` values are:

| True minimum absolute pair covariance `c_min` | Sufficient integer sample size |
|---|---:|
| 1.00 | 6,646 |
| 0.50 | 26,581 |
| 0.25 | 106,322 |

These thresholds are **sufficient**, not necessary, and can be very conservative. The model is conditional on three-view independence, interior latent prevalence, nonzero loadings, and IID eight-cell observations. This arithmetic check does not establish those empirical assumptions.

## Journal-facing interpretation

Include this evidence as a *scope-and-limits* discussion rather than an unqualified practical performance claim. A successful synthetic checkpoint is not empirical construct validation, full theorem novelty verification, or software-wide reproduction.

## Remaining gates

- Run the actual P20 and P74 source tests from a pinned repository commit in the declared environment.
- Stress-test the P74 covariance sign/nondegeneracy gate under near-singular channel configurations.
- Check the complete proof and dimensional assumptions independently, with special attention to model-adequacy versus identifiability.
- Confirm manuscript tables/figures/citations match the final source revision.

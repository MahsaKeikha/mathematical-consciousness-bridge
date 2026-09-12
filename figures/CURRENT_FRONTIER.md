# Current visual frontier: P71-P81

This page is a compact visual entry point for the current target-side research branch.

The branch begins by asking whether the target itself is scientifically valid and measurable, then moves through channel identifiability, finite-sample recovery, model adequacy, full-law separation, and exact continuous-family certification.

## P71-P74: target integrity

### P71: target provenance and non-circularity

A physical-sufficiency test is scientifically informative only if the target is not constructed from the physical descriptor in a way that forces the desired factorization result.

[Open the P71 theorem figure](../docs/figures/p71_target_provenance_noncircularity.svg)

[Read the P71 proposition](../docs/proposition_71_target_provenance_noncircularity.md)

### P72: noisy target measurement

The declared target-observation channel can attenuate or erase a genuine latent distinction. A null observed witness therefore does not automatically imply a null latent witness.

[Open the P72 theorem figure](../docs/figures/p72_noisy_target_measurement.svg)

[Read the P72 proposition](../docs/proposition_72_noisy_target_measurement.md)

### P73: target-channel identifiability

Under the declared conditionally independent binary-view model, three nondegenerate views can identify the latent channel up to a global label swap, while two views are insufficient in general.

[Open the P73 theorem figure](../docs/figures/p73_target_channel_identifiability.svg)

[Read the P73 proposition](../docs/proposition_73_target_channel_identifiability.md)

### P74: finite-sample target-channel recovery

Finite-sample confidence bounds are propagated through the P73 inversion, including an explicit refusal to certify recovery near the covariance singularity.

[Open the P74 theorem figure](../docs/figures/p74_finite_sample_target_channel_recovery.svg)

[Read the P74 proposition](../docs/proposition_74_finite_sample_target_channel_recovery.md)

## P75-P81: target-model adequacy and certified separation

### P75: overidentification and model adequacy

A fourth observed view creates overidentifying restrictions. The model must survive an adequacy audit instead of being accepted simply because parameters can be recovered.

![P75 target model adequacy](../docs/figures/p75_target_model_adequacy_overidentification.svg)

[Read the P75 proposition](../docs/proposition_75_target_model_adequacy_overidentification.md)

### P76: finite-sample adequacy rejection

An apparent population violation becomes a finite-data rejection certificate only when uncertainty is small enough that the violation remains separated from zero.

![P76 finite sample adequacy](../docs/figures/p76_finite_sample_target_model_adequacy.svg)

[Read the P76 proposition](../docs/proposition_76_finite_sample_target_model_adequacy.md)

### P77: full-law model-set separation

The complete empirical confidence region is compared against the complete declared model family. A local optimizer value is not used as a global rejection certificate.

![P77 full-law separation](../docs/figures/p77_full_law_model_set_separation.svg)

[Read the P77 proposition](../docs/proposition_77_full_law_model_set_separation.md)

### P78: certified continuous-family lower bound

Exact-rational branch-and-bound replaces an uncertified local best fit with a global lower bound on distance to the continuous P75 family.

![P78 certified continuous separation](../docs/figures/p78_certified_continuous_model_separation.svg)

[Read the P78 proposition](../docs/proposition_78_certified_continuous_model_separation.md)

### P79: certified sampling-radius envelope

The statistical uncertainty side of the rejection gate is given the correct one-sided numerical direction through exact-rational logarithm and square-root enclosures.

![P79 certified sampling radius](../docs/figures/p79_certified_sampling_radius.svg)

[Read the P79 proposition](../docs/proposition_79_certified_sampling_radius.md)

### P80: simplex-coupled model separation

The box relaxation is tightened by retaining probability normalization, so the certified lower bound is never weaker than the P78 independent-cell relaxation.

![P80 simplex coupled separation](../docs/figures/p80_simplex_coupled_model_separation.svg)

[Read the P80 proposition](../docs/proposition_80_simplex_coupled_model_separation.md)

### P81: projection-event model separation

P81 retains exact box ranges for all nonempty projected binary events and transfers event mismatch into a certified full-law distance lower bound. The construction is never weaker than P80 and includes a strict-improvement witness.

![P81 projection event separation](../docs/figures/p81_projection_event_model_separation.svg)

[Read the P81 proposition](../docs/proposition_81_projection_event_model_separation.md)

[Open the P81 equation provenance](../docs/p81_equation_provenance.md)

[Open the P81 implementation](../src/consciousness_bridge/projection_event_model_separation.py)

[Open the P81 numerical tests](../tests/test_projection_event_model_separation.py)

[Open the P81 figure geometry tests](../tests/test_p81_figure_geometry.py)

## Run the current research stack

From the repository root:

```bash
python -m pytest
python -m ruff check .
python scripts/generate_all_figures.py --validate-only
python scripts/verify_repository.py
```

To regenerate the computational atlases:

```bash
python scripts/generate_all_figures.py
```

The project does not claim that P71-P81 derives consciousness from physics. These results strengthen the methodology required before a physical-to-experiential bridge claim could be treated as scientifically credible. The bridge itself remains open.

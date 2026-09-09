# Quantitative Atlas Validation Report

This report records deterministic numerical checkpoints used by the quantitative physics and mathematics atlas. The plots are not accepted merely because they render: associated values and structural properties are checked in [`tests/test_quantitative_atlas.py`](../tests/test_quantitative_atlas.py).

| Check | Expected result | Scientific role |
| --- | ---: | --- |
| OU stationary variance with `theta=1.4`, `sigma=0.65` | `0.1508928571` | verifies Q02 closed form |
| Landauer bound at `300 K` | `2.870978885e-21 J` | verifies Q09 physical scale |
| Q05 linear-system eigenvalues | `-0.4 ± 1.047616 i` | verifies asymptotic stability |
| Q12 subdominant Markov eigenvalue | `0.74` | verifies spectral mixing curve |
| P17 explicit fine TV | `0.6` | verifies nonzero fine-scale distinction |
| P17 explicit coarse TV after a collision map | `0.0` | verifies exact coarse-graining information loss |
| P18 exact-family reconstruction defect | `0.0` | verifies exact family sufficiency |
| P18 exact-family fine/coarse minimum separation | equal | verifies exact response-geometry preservation |
| P9 sample-requirement scaling | `n(2 gamma)=n(gamma)/4` | verifies inverse-square gap law |
| Quantitative figure inventory | `>=33`; generated inventory `40` | guards visual completeness |

## Test categories

The quantitative test suite checks four distinct layers rather than only checking file existence:

1. **Artifact integrity** - at least 33 equation-driven SVGs must exist, every manifest entry must resolve to a nonempty SVG, and equations/status labels must be present.
2. **Closed-form benchmarks** - OU stationary variance and the Landauer bound are checked numerically.
3. **Linear and stochastic systems** - the state-space eigenvalues and Markov-chain spectral quantity used by the figures are checked.
4. **Repository propositions** - explicit P17 contraction/collision and P18 exact-family-sufficiency examples are checked against the code implementation; P9 inverse-square sample-complexity scaling is also tested.

## Interpretation discipline

The validation report confirms equations, simulations, and proposition-level consequences. It does **not** convert a mathematical or physical quantity into a consciousness claim. Synthetic response, perturbation, and complexity examples are labeled synthetic throughout the atlas.

## Reproduction

```bash
python scripts/generate_quantitative_atlas.py
pytest tests/test_quantitative_atlas.py
```

The generator uses fixed random seeds for every stochastic plot, so rerunning the script produces deterministic numerical content and a stable figure inventory.

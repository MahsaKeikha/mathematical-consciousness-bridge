"""Independent, idealized null stress test for fixed-weight e-process aggregation.

Not a controlled-system experiment or an implementation test of the latent-model witness.
"""
import numpy as np

SEED = 20261023
REPLICATIONS = 20000
ROUNDS = 100
FOLD_ALPHA = 0.04
THRESHOLD = 20.0

rng = np.random.default_rng(SEED)
wealth = np.ones(REPLICATIONS)
maximum = np.ones(REPLICATIONS)
for _ in range(ROUNDS):
    indicators = rng.random((REPLICATIONS, 2)) < FOLD_ALPHA
    e_round = (indicators.astype(float) / FOLD_ALPHA).mean(axis=1)
    wealth *= 0.5 + 0.5 * e_round
    maximum = np.maximum(maximum, wealth)

crossings = int(np.sum(maximum >= THRESHOLD))
print(f"seed={SEED} reps={REPLICATIONS} rounds={ROUNDS} count_cross={crossings} fraction={crossings / REPLICATIONS:.6f} threshold={THRESHOLD:g}")

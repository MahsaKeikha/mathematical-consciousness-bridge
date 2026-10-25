"""Idealized two-fold Bernoulli e-process sensitivity; NOT a controller experiment."""
import numpy as np

SEED = 20261024
N = 20_000
ROUNDS = 100
FOLD_LEVEL = 0.04
THRESHOLD = 20.0

for p, label in [(0.04, "null"), (0.08, "illustrative p=0.08"), (0.12, "illustrative p=0.12")]:
    rng = np.random.default_rng(SEED)
    wealth = np.ones(N, dtype=float)
    first_crossing = np.zeros(N, dtype=np.int32)
    for t in range(1, ROUNDS + 1):
        rejections = rng.random((N, 2)) < p
        round_e = rejections.sum(axis=1) / (2 * FOLD_LEVEL)
        wealth *= 0.5 + 0.5 * round_e
        first_crossing[(first_crossing == 0) & (wealth >= THRESHOLD)] = t
    crossings = int(np.count_nonzero(first_crossing))
    print(f"{label}: crossings={crossings}/{N}; frequency={crossings / N:.6f}")

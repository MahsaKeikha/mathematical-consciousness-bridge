# Proposition 55: Pruning-aware metric switching-cost monotonicity

## Status

**Proved deterministic scheduling theorem.** P55 extends the P53-P54 residual scheduling chain by quantifying how the exact optimal execution cost changes when residual demands decrease after additional sampling or valid safe pruning.

The theorem assumes the same per-sample acquisition cost, the same metric switching geometry, and the same current setup state across the compared residual states. It does not itself justify pruning and does not establish statistical minimaxity of the P48 thresholds.

---

## 1. Setup

Let a residual state be a nonnegative integer demand vector

\[
r=(r_i)_{i\in V},
\qquad r_i\in\mathbb Z_{\ge0},
\]

with positive-demand support

\[
S(r)=\{i:r_i>0\}.
\]

Let \(a>0\) denote deterministic acquisition cost per sample. Let \(c\) be the same finite metric switching cost used in P54, and let \(s\) be the same optional current setup state.

P54 gives the exact deterministic optimum

\[
\boxed{
C^*(r;s)
=
a\sum_i r_i+L^*(S(r);s),
}
\]

where \(L^*(S;s)\) is the shortest Hamiltonian path through \(S\), optionally rooted at \(s\), with no return-to-start requirement.

Consider two sequential states \(r\) and \(r'\) satisfying

\[
\boxed{
r_i'\le r_i\quad\text{for every }i.}
\]

Then automatically

\[
S(r')\subseteq S(r).
\]

---

## 2. Proposition 55A: shortest metric route is monotone under support deletion

For any finite supports \(S'\subseteq S\),

\[
\boxed{
L^*(S';s)\le L^*(S;s).
}
\]

### Proof

Take an optimal P54 path through \(S\). Delete from that path every vertex in \(S\setminus S'\), preserving the order of retained vertices. If deleted vertices occur between two retained route points \(u\) and \(v\), repeated triangle inequality gives

\[
c(u,v)
\le
c(u,x_1)+c(x_1,x_2)+\cdots+c(x_k,v).
\]

The same shortcut argument applies from the fixed start \(s\) when the initial portion of the path is deleted. Hence the retained route through \(S'\) has switching cost no larger than the original optimal route through \(S\). Because \(L^*(S';s)\) is the minimum over all routes through \(S'\), it is no larger than that retained route. Therefore

\[
L^*(S';s)\le L^*(S;s).
\]

\(\square\)

---

## 3. Proposition 55B: exact optimal cost-release decomposition

For componentwise nonincreasing residual demand \(r'\le r\),

\[
\boxed{
C^*(r;s)-C^*(r';s)
=
a\left(\sum_i r_i-\sum_i r_i'\right)
+
\left[L^*(S(r);s)-L^*(S(r');s)\right].
}
\]

Both terms on the right are nonnegative. Therefore

\[
\boxed{
C^*(r';s)\le C^*(r;s).
}
\]

Moreover,

\[
\boxed{
C^*(r;s)-C^*(r';s)
\ge
a\left(\sum_i r_i-\sum_i r_i'\right).
}
\]

Thus every released residual sample produces its direct acquisition saving, while support deletion can create an additional nonnegative switching saving.

### Proof

Subtract the two exact P54 decompositions. Componentwise demand monotonicity makes the acquisition difference nonnegative, and Proposition 55A makes the route difference nonnegative. \(\square\)

---

## 4. Proposition 55C: support-preserving residual decrease

If

\[
S(r')=S(r),
\]

then the metric route problem is identical at the two states, so

\[
L^*(S(r');s)=L^*(S(r);s).
\]

Hence the total optimal release is exactly

\[
\boxed{
C^*(r;s)-C^*(r';s)
=
a\left(\sum_i r_i-\sum_i r_i'\right).
}
\]

This separates two experimental effects cleanly:

- decreasing positive residual magnitudes saves acquisition cost;
- eliminating preparations from the positive-demand support may additionally save switching cost.

---

## 5. Proposition 55D: computable shortcut certificate

Let

\[
\pi^*=(v_1,\ldots,v_m)
\]

be an optimal P54 route through \(S(r)\). Delete every vertex not in \(S(r')\), obtaining the retained route

\[
\pi_{\rm keep}.
\]

Metric shortcutting proves

\[
C_{\rm sw}(\pi_{\rm keep})\le L^*(S(r);s).
\]

Since \(\pi_{\rm keep}\) is feasible for the new support,

\[
L^*(S(r');s)\le C_{\rm sw}(\pi_{\rm keep}).
\]

Therefore the directly observable shortcut saving

\[
\boxed{
\Delta_{\rm shortcut}
=
L^*(S(r);s)-C_{\rm sw}(\pi_{\rm keep})
}
\]

is a certified lower bound on the true optimal route release:

\[
\boxed{
0\le\Delta_{\rm shortcut}
\le
L^*(S(r);s)-L^*(S(r');s).
}
\]

This certificate can be computed from the old optimal route even before resolving the new Hamiltonian-path problem exactly.

---

## 6. Complete sequential scheduling interpretation

P53 established monotonicity of the residual sample burden. P54 showed that, with metric preparation transitions, deterministic execution cost contains a second geometric term. P55 proves that the combined optimum remains monotone:

\[
\boxed{
\text{additional samples / safe pruning}
\Longrightarrow
r'\le r
\Longrightarrow
S(r')\subseteq S(r)
\Longrightarrow
C^*(r';s)\le C^*(r;s).
}
\]

The total gain has the exact decomposition

\[
\boxed{
\text{optimal cost release}
=
\text{acquisition release}
+
\text{metric route release}.
}
\]

This matters experimentally because pruning can have a discontinuous operational benefit. Reducing a demand from 100 samples to 1 sample changes acquisition burden but not route support. Reducing it from 1 sample to 0 can additionally remove an entire preparation setup from the optimal switching path.

---

## 7. Assumptions that cannot be dropped silently

The route monotonicity theorem relies on the same metric assumption as P54. For an arbitrary nonmetric transition-cost matrix, deleting a preparation may remove a cheap intermediate waypoint and increase the direct transition cost. P55 therefore does not assert route monotonicity outside the metric regime.

The comparison also holds the start/setup state fixed. If an experiment physically ends one state at a different setup and uses that new setup as the start for the next optimization, that changed start state is an additional variable and requires a separate theorem.

---

## 8. Implementation and reproducibility

The executable implementation is

[`src/consciousness_bridge/pruning_aware_switching_monotonicity.py`](../src/consciousness_bridge/pruning_aware_switching_monotonicity.py).

It provides:

- positive-support extraction;
- componentwise residual monotonicity checks;
- exact old/new P54 cost decomposition;
- support-preserving acquisition-release evaluation;
- old-route metric shortcut certificates.

Regression tests are in

[`tests/test_pruning_aware_switching_monotonicity.py`](../tests/test_pruning_aware_switching_monotonicity.py).

The theorem visual is

[`docs/figures/p55_pruning_aware_switching_monotonicity.svg`](figures/p55_pruning_aware_switching_monotonicity.svg).

---

## 9. Scientific boundary

P55 is a deterministic resource-scheduling theorem conditional on valid residual demands, a fixed setup state, and a declared metric switching geometry. It does not independently establish that an edge should be pruned, does not prove information-theoretic optimality of the underlying statistical thresholds, and does not identify any graph, route, metric, or scheduling quantity with consciousness. It makes no claim that quantum mechanics is incomplete.

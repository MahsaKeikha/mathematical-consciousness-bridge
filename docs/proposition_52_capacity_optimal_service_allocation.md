# Proposition 52: Capacity-optimal service allocation

## Status

**Proved exact minimax service-allocation theorem for satisfying finite witness-graph sampling demands under a fixed global sampling capacity.**

P51 gives preparation-specific finite-window service guarantees. P52 asks the inverse design question: if the experimenter may choose the long-run service shares subject to a total capacity constraint, which shares minimize the worst deterministic time needed to satisfy all declared local sample demands?

P52 solves that optimization exactly. It is a scheduling theorem for P48/P51 sufficient thresholds, not a theorem that minimizes the actual random statistical stopping time.

---

## 1. Vertex demands induced by edge thresholds

Let \(G=(V,E)\) be the declared finite witness graph. Suppose P48 assigns each edge \(e\in E\) a finite local threshold \(N_e\).

To guarantee that every edge \(e=\{i,j\}\) has both endpoints at or above its threshold, preparation \(i\) must receive at least

\[
\boxed{
d_i=\max\{N_e:e\ni i\}.
}
\]

For an isolated vertex, define \(d_i=0\).

This demand vector is componentwise minimal for threshold saturation: lowering any positive \(d_i\) below the maximum incident edge threshold leaves at least one incident edge without the declared endpoint sample requirement.

---

## 2. Continuous capacity model

Let \(C>0\) denote the total service capacity, measured in preparation-level samples per global unit time. Let \(\pi_i\ge0\) be the service rate assigned to preparation \(i\), subject to

\[
\boxed{
\sum_{i\in V}\pi_i\le C.
}
\]

For a positive demand \(d_i>0\), the deterministic completion time implied by rate \(\pi_i\) is

\[
\frac{d_i}{\pi_i}.
\]

If \(d_i>0\) and \(\pi_i=0\), the completion time is infinite.

The family threshold-saturation time is therefore

\[
\boxed{
T(\pi)=\max_{i:d_i>0}\frac{d_i}{\pi_i}.
}
\]

P52 solves

\[
\boxed{
\min_{\pi_i\ge0,\ \sum_i\pi_i\le C}
\max_{i:d_i>0}\frac{d_i}{\pi_i}.
}
\]

---

## 3. Proposition 52A: universal lower bound

For any feasible allocation with finite completion time \(T\),

\[
d_i\le T\pi_i
\]

for every positive-demand vertex. Summing gives

\[
\sum_i d_i
\le
T\sum_i\pi_i
\le
TC.
\]

Hence every feasible allocation satisfies

\[
\boxed{
T(\pi)\ge\frac{\sum_i d_i}{C}.
}
\]

This lower bound uses only conservation of sampling capacity.

---

## 4. Proposition 52B: exact minimax allocation

Let

\[
D=\sum_i d_i.
\]

When \(D>0\), define

\[
\boxed{
\pi_i^*=C\frac{d_i}{D}
}
\]

for positive-demand vertices, and \(\pi_i^*=0\) for zero-demand vertices.

Then

\[
\sum_i\pi_i^*=C,
\]

and for every positive-demand vertex,

\[
\frac{d_i}{\pi_i^*}
=
\frac{D}{C}.
\]

Therefore

\[
\boxed{
T(\pi^*)=\frac{D}{C}.
}
\]

Combined with the lower bound,

\[
\boxed{
T^*=\frac{\sum_i d_i}{C}.
}
\]

Thus proportional-to-demand service is minimax optimal.

---

## 5. Proposition 52C: uniqueness on the positive-demand support

Suppose a feasible allocation achieves the optimum \(D/C\). Then for every positive-demand vertex,

\[
\frac{d_i}{\pi_i}\le\frac{D}{C},
\]

so

\[
\pi_i\ge C\frac{d_i}{D}.
\]

Summing these inequalities over all positive-demand vertices yields

\[
\sum_i\pi_i\ge C.
\]

Feasibility gives the reverse inequality. Hence equality must hold everywhere, implying

\[
\boxed{
\pi_i=C\frac{d_i}{D}
}
\]

for every positive-demand preparation.

The minimax allocation is therefore unique on the support of positive demand.

---

## 6. Equalized bottlenecks

At the optimum,

\[
\boxed{
\frac{d_i}{\pi_i^*}=T^*
\qquad
\forall i:d_i>0.
}
\]

Thus P52 equalizes the deterministic completion bottleneck across all required preparations.

Any transfer of service away from one positive-demand preparation without a compensating change in its demand makes that preparation slower than the common optimum and cannot improve the maximum completion time.

---

## 7. Exact discrete unit-capacity result

Now assume all demands \(d_i\) are nonnegative integers and exactly one preparation-level sample can be collected per global round.

Every valid schedule that satisfies all demands must contain at least

\[
\boxed{
D=\sum_i d_i
}
\]

rounds, because one round contributes at most one unit toward the total remaining demand.

A schedule that selects each preparation exactly \(d_i\) times has length exactly \(D\). Therefore

\[
\boxed{
T_{\rm discrete}^*=\sum_i d_i.
}
\]

This discrete quota result is exact for threshold saturation.

The ordering of those quota samples may still be chosen adaptively, subject to P47 non-anticipation and whatever finite-window guarantees are required for intermediate stopping behavior.

---

## 8. Relation to P51

P51 accepts service guarantees \((W_i,q_i)\) and derives a stopping bound. P52 determines the ideal continuous target rates before those finite-window guarantees are discretized.

Writing

\[
\rho_i=\frac{q_i}{W_i},
\]

P51 behaves approximately like a finite-window implementation of a service rate \(\rho_i\).

P52 says that for complete threshold saturation, the ideal rate proportions are

\[
\boxed{
\rho_i\propto d_i.
}
\]

A practical scheduler can therefore choose integer windows and quotas whose ratios \(q_i/W_i\) approximate the P52 service shares while preserving the finite-window anti-starvation property required by P51.

---

## 9. Relation to P45

P45 allocates statistical precision according to shared graph incidence before fixed thresholds have been resolved. P52 solves a different downstream problem: once finite local demands are available, it allocates global service capacity to meet them in minimum worst-case deterministic time.

The two layers therefore compose as

\[
\boxed{
\text{P45: where precision is statistically valuable}
\quad\longrightarrow\quad
\text{P48: finite local thresholds}
\quad\longrightarrow\quad
\text{P52: capacity-optimal service rates}.
}
\]

P52 does not replace P45 and does not claim that a threshold derived from a conservative P48 envelope is information-theoretically minimal.

---

## 10. Relation to P47-P51

The sequential design chain is now

\[
\boxed{
\begin{array}{c}
\text{P47: anytime-valid adaptive inference}\\
\Downarrow\\
\text{P48: finite gap-dependent local thresholds}\\
\Downarrow\\
\text{P49: logarithmic certification checkpoints}\\
\Downarrow\\
\text{P50: common bounded-starvation global-time bound}\\
\Downarrow\\
\text{P51: heterogeneous finite-window service bound}\\
\Downarrow\\
\text{P52: exact capacity-optimal service allocation.}
\end{array}
}
\]

P47 supplies validity. P48 supplies required local precision. P49 reduces certification computation. P50-P51 convert local precision to global time. P52 optimizes the service shares used to deliver that precision.

---

## 11. Scientific boundary

P52 proves an exact deterministic scheduling statement for declared sampling thresholds.

It does not prove that P48 thresholds are minimax statistical sample complexities.

It does not prove that proportional service minimizes the actual data-dependent stopping time of every adaptive experiment.

It does not establish quantum incompleteness, an additional physical dimension, or consciousness.

The conclusion remains conditional on the declared witness graph, bridge regularity class, confidence model, and local threshold construction.

---

## 12. Next theorem target

P52 optimizes complete-family threshold saturation when the demand vector is known. A stronger adaptive question remains: can service be reallocated after P47 safely eliminates edges, while proving a quantitative reduction in remaining completion time relative to the original P52 schedule?

A natural P53 target is a **residual-demand reoptimization theorem**. It should prove monotonicity of the optimal remaining capacity time under safe graph pruning and characterize the exact capacity released when vertices or incident threshold constraints disappear.

---

## 13. Reproducibility

Implementation: [`capacity_optimal_service_allocation.py`](../src/consciousness_bridge/capacity_optimal_service_allocation.py)

Regression tests: [`test_capacity_optimal_service_allocation.py`](../tests/test_capacity_optimal_service_allocation.py)

Publication visual: [`p52_capacity_optimal_service_allocation.svg`](figures/p52_capacity_optimal_service_allocation.svg)

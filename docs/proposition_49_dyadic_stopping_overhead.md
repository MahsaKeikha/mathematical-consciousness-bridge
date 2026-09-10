# Proposition 49: Dyadic certification schedules with less-than-two stopping overhead

## Status

**Proved deterministic scheduling theorem for the P48 sequential stopping bound.**

P48 gives an explicit sufficient local sample threshold \(N_e\) for each nonzero-margin edge. P49 shows that the experiment does not need to recompute the full P47 certification state after every new sample. If certification is checked only at dyadic sample counts

\[
1,2,4,8,\ldots,
\]

then the first checkpoint at or above any finite P48 threshold is strictly less than twice that threshold.

The number of certification looks is therefore logarithmic in the P48 stopping count, while the sample-count overhead is less than a factor of two.

P49 is a scheduling theorem. It does not claim minimax optimality, adaptive optimality, quantum incompleteness, a new physical dimension, or consciousness.

---

## 1. Why a separate scheduling theorem matters

P47 provides time-uniform validity under repeated inspection.

P48 provides an explicit sufficient sample threshold.

Those two results still leave a practical design question:

\[
\boxed{
\text{Must the entire witness graph be re-evaluated after every single new sample?}
}
\]

The answer is no.

A sparse checkpoint schedule can reduce computational and administrative overhead while preserving a finite stopping guarantee.

P49 uses the simplest exact schedule:

\[
\boxed{
n_k=2^k,\qquad k=0,1,2,\ldots
}
\]

and quantifies its cost.

---

## 2. P48 threshold recalled

For each declared edge \(e\), P48 supplies a finite sufficient local sample count

\[
N_e\ge1
\]

whenever the population regularity margin is nonzero.

At or beyond that count, the P47 simultaneous interval has the correct sign on the P47 good event.

For a positive edge,

\[
M_e>0
\quad\Longrightarrow\quad
\underline M_e(n)>0
\qquad
\forall n\ge N_e.
\]

For a negative edge,

\[
M_e<0
\quad\Longrightarrow\quad
\overline M_e(n)<0
\qquad
\forall n\ge N_e.
\]

P49 does not alter the construction of \(N_e\). It only changes when the experiment checks whether the threshold has already been reached.

---

## 3. Dyadic ceiling

For any positive integer \(N\), define

\[
\boxed{
D(N)=2^{\lceil\log_2 N\rceil}.
}
\]

Equivalently, \(D(N)\) is the smallest power of two that is greater than or equal to \(N\).

Examples are

\[
D(1)=1,
\qquad
D(3)=4,
\qquad
D(8)=8,
\qquad
D(33)=64.
\]

---

## 4. Proposition 49A: dyadic ceiling overhead

For every positive integer \(N\),

\[
\boxed{
N\le D(N)<2N.
}
\]

### Proof

The lower bound follows immediately from the definition of \(D(N)\).

Let

\[
k=\lceil\log_2N\rceil.
\]

Then

\[
k-1<\log_2N\le k
\]

unless \(N\) is itself an exact power of two, in which case \(D(N)=N\) and the result is immediate.

In the non-power-of-two case,

\[
2^{k-1}<N,
\]

so

\[
2^k<2N.
\]

Since

\[
D(N)=2^k,
\]

we obtain

\[
\boxed{
D(N)<2N.
}
\]

The same strict inequality also holds when \(N\) is a power of two because then \(D(N)=N<2N\).

---

## 5. Number of certification looks

Suppose the experiment checks the full P47 witness graph only at

\[
1,2,4,\ldots,D(N).
\]

The number of checks is

\[
\boxed{
L(N)
=
\lceil\log_2N\rceil+1.
}
\]

Thus

\[
\boxed{
L(N)=O(\log N).
}
\]

This is a computational advantage relative to checking after every local sample, which would require \(O(N)\) full certification evaluations.

The theorem does not say that data acquisition itself becomes logarithmic. It says the **number of full statistical looks** becomes logarithmic while sample acquisition remains within a factor strictly below two of the P48 stopping threshold.

---

## 6. Edgewise dyadic stopping threshold

For each nonzero-gap edge, define

\[
\boxed{
\widetilde N_e=D(N_e).
}
\]

By Proposition 49A,

\[
\boxed{
N_e
\le
\widetilde N_e
<
2N_e.
}
\]

Since P48 guarantees the correct sign for every local count at or beyond \(N_e\), the P47 edge interval has the correct sign at the first dyadic checkpoint \(\widetilde N_e\).

Therefore, on the P47 simultaneous good event,

\[
M_e>0
\Longrightarrow
\underline M_e(\widetilde N_e)>0,
\]

and

\[
M_e<0
\Longrightarrow
\overline M_e(\widetilde N_e)<0.
\]

---

## 7. Proposition 49B: positive-witness dyadic stopping bound

Let

\[
E_+
=
\{e\in E:M_e>0\}.
\]

Assume

\[
E_+\ne\varnothing.
\]

P48 gives

\[
K_+
=
\min_{e\in E_+}N_e.
\]

Under dyadic checking, define

\[
\boxed{
\widetilde K_+
=
\min_{e\in E_+}D(N_e).
}
\]

Because \(D(\cdot)\) is monotone,

\[
\widetilde K_+
=
D(K_+).
\]

Therefore Proposition 49A gives

\[
\boxed{
K_+
\le
\widetilde K_+
<
2K_+.
}
\]

On the P47 good event, the positive edge attaining \(K_+\) has already reached its P48 sufficient threshold by dyadic epoch \(\widetilde K_+\). Hence the dyadic-check procedure must stop with a positive witness no later than that checkpoint.

Thus

\[
\boxed{
\Pr\left(
\tau_{+,\mathrm{dyad}}
\le
\widetilde K_+
\right)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

---

## 8. Proposition 49C: all-negative dyadic stopping bound

Suppose

\[
M_e<0
\qquad
\forall e\in E.
\]

P48 gives

\[
K_-
=
\max_{e\in E}N_e.
\]

Define

\[
\boxed{
\widetilde K_-
=
\max_{e\in E}D(N_e).
}
\]

Again, monotonicity of \(D\) gives

\[
\widetilde K_-
=
D(K_-).
\]

Hence

\[
\boxed{
K_-
\le
\widetilde K_-
<
2K_-.
}
\]

By the checkpoint \(\widetilde K_-\), every declared negative edge has crossed its P48 sufficient local threshold and therefore has a certified negative upper margin on the P47 good event.

Thus

\[
\boxed{
\Pr\left(
\tau_{0,\mathrm{dyad}}
\le
\widetilde K_-
\right)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

---

## 9. Zero-gap boundary is preserved

Suppose no positive edge exists and at least one edge satisfies

\[
M_e=0.
\]

P48 provides no generic finite sign-separation threshold for that edge.

Therefore there is no finite quantity to which the dyadic ceiling can be applied.

P49 correctly returns

\[
\boxed{
\text{no finite dyadic sign-gap bound}.
}
\]

A sparse checkpoint schedule cannot create statistical separation that the underlying population problem does not possess.

---

## 10. Why P47 validity is preserved

P47 establishes an event on which the declared edge intervals are valid at **every** global time and every realized local sample count.

A dyadic schedule inspects only a deterministic subset of those times.

Therefore the dyadic procedure requires no new multiple-look correction beyond the P47 construction.

Formally, if

\[
\mathcal T_{\rm dyad}
=
\{1,2,4,8,\ldots\},
\]

then

\[
\mathcal T_{\rm dyad}
\subset
\mathbb N.
\]

Since P47 already proves simultaneous validity for all

\[
t\in\mathbb N,
\]

it follows immediately that the same event controls all

\[
t\in\mathcal T_{\rm dyad}.
\]

Thus P49 changes computation and batching, not the probability guarantee.

---

## 11. Certification-look complexity

In the positive case, the number of complete witness-graph evaluations required through the P49 stopping checkpoint is

\[
\boxed{
L_+
=
\lceil\log_2K_+\rceil+1.
}
\]

In the all-negative case,

\[
\boxed{
L_-
=
\lceil\log_2K_-\rceil+1.
}
\]

Thus the number of full certification evaluations grows logarithmically with the P48 sample threshold.

For example, a P48 threshold of

\[
N=1000
\]

would require 1000 checks under per-sample inspection but only

\[
1,2,4,8,16,32,64,128,256,512,1024,
\]

which is 11 dyadic looks.

The corresponding sample count is 1024, only 2.4 percent above the P48 threshold in that example.

---

## 12. Linear acquisition-cost overhead

Suppose the P48 full-family acquisition-cost upper bound is linear in the epoch count:

\[
C_{\rm full}(K)
=
K\sum_{i\in V}c_i.
\]

Replacing \(K\) by its dyadic ceiling gives

\[
C_{\rm dyad}(K)
=
D(K)\sum_{i\in V}c_i.
\]

By Proposition 49A,

\[
\boxed{
C_{\rm full}(K)
\le
C_{\rm dyad}(K)
<
2C_{\rm full}(K).
}
\]

Thus the same less-than-two overhead factor applies to any acquisition-cost upper bound that is linear in the common epoch count.

P47 safe pruning can still reduce realized cost below this full-family reference.

---

## 13. Computational versus sampling overhead

P49 separates two distinct resources.

### Statistical looks

The number of times the complete graph must be re-evaluated drops from at most

\[
K
\]

per-sample looks to

\[
\boxed{
\lceil\log_2K\rceil+1.
}
\]

### Acquired samples

The worst-case stopping threshold rises from

\[
K
\]

to

\[
D(K),
\]

with

\[
\boxed{
D(K)<2K.
}
\]

This tradeoff is deterministic and exact.

---

## 14. General geometric schedules

Dyadic scheduling is the special case with multiplicative ratio two.

More generally, one may consider checkpoints growing approximately as

\[
1,r,r^2,r^3,\ldots
\qquad
r>1.
\]

The expected qualitative tradeoff is:

- ratios closer to one produce more certification looks and smaller sampling overshoot;
- larger ratios produce fewer looks and larger overshoot.

P49 proves only the exact integer dyadic case. A careful general geometric theorem requires explicit handling of integer rounding and duplicate checkpoints and is left separate rather than hidden inside the dyadic statement.

---

## 15. Scientific boundary

P49 proves a scheduling result for a declared sequential regularity-witness experiment.

It shows that sparse deterministic certification times can preserve P47 validity and P48 finite stopping while incurring less than a factor of two sample-count overhead.

It does not prove that the regularity witness is consciousness.

It does not prove quantum incompleteness.

It does not prove an extra physical or spacetime dimension.

It does not prove that dyadic scheduling is statistically or computationally optimal among all possible schedules.

---

## 16. The sequential chain after P49

The end-to-end sequential branch is now

\[
\boxed{
\begin{array}{c}
\text{P47: anytime-valid adaptive witness graph}\\
\Downarrow\\
\text{P48: explicit gap-dependent stopping threshold}\\
\Downarrow\\
\text{P49: logarithmic certification looks with less-than-two threshold overhead.}
\end{array}
}
\]

P47 answers validity.

P48 answers finite stopping.

P49 answers checkpoint efficiency.

---

## 17. Next theorem target

P49 reduces the number of complete certification evaluations but does not improve the full-family sampling strategy itself.

The next mathematically meaningful target is a **preparation-asynchronous allocation theorem** in which different vertices accumulate different local sample counts and the policy prioritizes the preparation whose next sample produces the largest certified reduction in active edge uncertainty.

A serious next theorem should compare that asynchronous policy with a declared benchmark and prove a finite overhead bound. It should not label the policy optimal merely because it is intuitive.

---

## 18. Reproducibility

Implementation:
[`dyadic_stopping_overhead.py`](../src/consciousness_bridge/dyadic_stopping_overhead.py)

Regression tests:
[`test_dyadic_stopping_overhead.py`](../tests/test_dyadic_stopping_overhead.py)

Publication visual:
[`p49_dyadic_stopping_overhead.svg`](figures/p49_dyadic_stopping_overhead.svg)

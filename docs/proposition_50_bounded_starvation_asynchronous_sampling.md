# Proposition 50: Bounded-starvation asynchronous sampling

## Status

**Proved global-round stopping theorem for asynchronous priority-based sampling under an explicit bounded-starvation condition.**

P47 permits non-anticipating adaptive preparation sampling while preserving time-uniform statistical validity. P48 gives finite stopping thresholds in terms of local samples received by each required preparation. P50 closes the gap between those two statements by imposing a minimal progress condition on an asynchronous policy.

The theorem does not claim the policy is optimal. It proves that a finite local-sample threshold becomes a finite global-round threshold when no still-active preparation can be ignored for more than a declared number of rounds.

P50 is an experimental-design theorem. It does not establish quantum incompleteness, an additional physical dimension, or consciousness.

---

## 1. Global asynchronous rounds

Let

\[
G_t=(V_t,E_t)
\]

be the currently active P47 witness graph at global round \(t\).

Unlike P48's active round-robin construction, P50 permits the policy to choose only one active preparation per global round.

Let

\[
I_t\in V_t
\]

be the preparation selected at round \(t\).

A selection of preparation \(i\) means that the protocol obtains the declared paired update required by the P48 local threshold, for example one target observation and one quantum/tomography observation for that preparation.

Let

\[
N_i(t)
\]

be the number of times preparation \(i\) has been selected by global time \(t\).

These local counts may differ substantially across preparations.

---

## 2. Bounded-starvation condition

Fix an integer

\[
H\ge1.
\]

The asynchronous policy is called **\(H\)-fair** if every preparation that remains active throughout any block of \(H\) consecutive global rounds is selected at least once inside that block.

Formally, for every \(i\) and every block

\[
\{s,s+1,\ldots,s+H-1\},
\]

if

\[
i\in V_t
\qquad
\forall t\in\{s,\ldots,s+H-1\},
\]

then there exists at least one round \(u\) in the same block such that

\[
\boxed{I_u=i.}
\]

The constant \(H\) is a starvation horizon.

A smaller value forces more uniform sampling. A larger value allows stronger priority bias.

---

## 3. Local-count growth lemma

Suppose preparation \(i\) remains active throughout the first \(T\) global rounds.

Partition the first

\[
H\left\lfloor\frac{T}{H}\right\rfloor
\]

rounds into disjoint blocks of length \(H\).

By \(H\)-fairness, preparation \(i\) is selected at least once in every block.

Therefore

\[
\boxed{
N_i(T)
\ge
\left\lfloor\frac{T}{H}\right\rfloor.
}
\]

In particular, after

\[
\boxed{HN}
\]

global rounds, any preparation that remained active throughout those rounds has accumulated at least

\[
\boxed{N}
\]

local paired samples.

This is the basic conversion from local P48 thresholds to global P50 time.

---

## 4. Why positive edges remain active

Let

\[
e=\{i,j\}
\]

be a declared edge with

\[
M_e>0.
\]

On the P47 simultaneous good event,

\[
M_e\le\overline M_e(t)
\qquad
\forall t.
\]

Hence

\[
\overline M_e(t)>0
\]

for every time before the edge is positively certified.

The P47 safe-elimination rule removes an edge only when

\[
\overline M_e(t)<0.
\]

Therefore a truly positive edge cannot be removed on the P47 good event.

Consequently, neither endpoint of that edge can be pruned as an isolated vertex while the edge remains unresolved.

Both endpoints therefore remain active until positive certification.

---

## 5. Proposition 50A: positive-witness global-round bound

Let the P48 sufficient local threshold for edge \(e\) be

\[
N_e.
\]

Let

\[
E_+
=
\{e\in E:M_e>0\}
\]

and assume

\[
E_+\ne\varnothing.
\]

Define the P48 positive local threshold

\[
\boxed{
K_+
=
\min_{e\in E_+}N_e.
}
\]

Choose

\[
e_*=\{i_*,j_*\}
\in
\arg\min_{e\in E_+}N_e.
\]

By the positive-edge persistence argument, both endpoints remain active until certification.

Under \(H\)-fairness, after

\[
HK_+
\]

global rounds, each endpoint has accumulated at least

\[
K_+
\]

local samples.

P48 then guarantees the positive sign certificate

\[
\underline M_{e_*}>0.
\]

Thus on the P47 simultaneous good event,

\[
\boxed{
\tau_{+,H}
\le
HK_+.
}
\]

Therefore

\[
\boxed{
\Pr\left(
\tau_{+,H}
\le
HK_+
\right)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

The factor \(H\) is the exact price paid by this theorem for allowing asynchronous priority-based scheduling instead of requiring all active preparations to advance together.

---

## 6. Negative edges either disappear early or accumulate enough data

Now let

\[
M_e<0.
\]

Consider its P48 sufficient local threshold \(N_e\).

There are only two possibilities before global round

\[
HN_e.
\]

First, the edge may already have been safely eliminated because its P47 upper margin became negative.

Second, if the edge has not been eliminated, both of its endpoints must still be active. Under \(H\)-fairness, each endpoint then receives at least \(N_e\) local samples by round \(HN_e\).

P48 therefore forces

\[
\overline M_e<0
\]

by that time, so the edge is eliminated.

Hence every strictly negative edge disappears no later than

\[
\boxed{HN_e}
\]

global rounds.

---

## 7. Proposition 50B: all-negative global-round bound

Suppose

\[
\boxed{
M_e<0
\qquad
\forall e\in E.
}
\]

Define the P48 all-negative threshold

\[
\boxed{
K_-
=
\max_{e\in E}N_e.
}
\]

By the previous argument, every edge \(e\) must have been removed by global round

\[
HN_e.
\]

Therefore all declared edges are gone by

\[
\boxed{HK_-}.
\]

Thus on the P47 simultaneous good event,

\[
\boxed{
\tau_{0,H}
\le
HK_-.
}
\]

and consequently

\[
\boxed{
\Pr\left(
\tau_{0,H}
\le
HK_-
\right)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

---

## 8. Proposition 50C: no finite global-time guarantee without a progress condition

The bounded-starvation premise is not cosmetic.

Suppose there is a positive edge

\[
e=\{i,j\}
\]

whose P48 threshold is finite.

An adaptive policy that repeatedly samples unrelated preparations while never sampling \(i\) or \(j\) leaves

\[
N_i(t)=N_j(t)=0
\]

for arbitrarily long global time.

P47 statistical validity remains intact because the confidence statement is valid at every realized local count.

But P48's local threshold is never reached.

Since the delay can be made arbitrarily large, there is no finite deterministic function of the P48 thresholds alone that upper-bounds global stopping time for completely unrestricted adaptive sampling.

Therefore

\[
\boxed{
\text{P47 validity}
\not\Longrightarrow
\text{finite global-time progress}.
}
\]

A progress assumption such as \(H\)-fairness is mathematically necessary for a theorem of the P50 type.

---

## 9. Relation to active round robin

Suppose there are

\[
m
\]

active preparations and the policy uses exact round robin.

Then every active preparation is sampled once in every block of

\[
m
\]

global rounds.

Thus round robin is

\[
\boxed{H=m}
\]

fair.

P50 then converts a P48 local threshold \(K\) into the global single-preparation-selection bound

\[
\boxed{mK}.
\]

This is exactly what one expects: \(K\) full active-graph epochs contain \(mK\) individual preparation updates when no pruning occurs.

Priority-based policies may use the same theorem with a larger or dynamically enforced starvation horizon.

---

## 10. Priority sampling is allowed

P50 does not require equal sampling frequencies.

Inside each \(H\)-round block, the policy may sample some active preparations repeatedly and others only once.

Therefore it may use:

- P45 shared-uncertainty pressure;
- P46 graph value;
- P47 current lower or upper margin;
- P48 predicted threshold reduction;
- P49 batched certification state;
- any other non-anticipating priority score.

The only progress requirement is that no preparation that remains active for the complete \(H\)-round block is omitted from that block.

Thus the theorem cleanly separates

\[
\boxed{
\text{priority freedom}
\quad\text{from}\quad
\text{starvation prevention}.
}
\]

---

## 11. Dynamic pruning is compatible with H-fairness

The fairness obligation applies only while a preparation remains active.

If P47 safely eliminates every incident edge of preparation \(i\), then \(i\) may be pruned.

After pruning, future \(H\)-round blocks impose no sampling obligation on \(i\).

This is important because otherwise a fairness rule would waste samples on preparations whose entire witness neighborhood is already certified negative.

P50 therefore supports adaptive graph shrinkage without weakening the finite stopping argument.

---

## 12. Local versus global complexity

P48 measures complexity in local paired samples.

P50 measures complexity in global asynchronous selection rounds.

The conversion is

\[
\boxed{
K
\longmapsto
HK.
}
\]

This factor is independent of the statistical confidence level because the confidence accounting already occurred in P47-P48.

The value of \(H\) is instead a scheduling property.

---

## 13. Combining P49 batching with P50 asynchronous sampling

P49 allows full certification checks only at dyadic local thresholds.

P50 allows preparations to accumulate those local samples asynchronously.

If a required edge has dyadic local threshold

\[
\widetilde N_e=D(N_e),
\]

then under \(H\)-fair asynchronous sampling both endpoints reach that dyadic threshold by global round

\[
\boxed{H\widetilde N_e}.
\]

Since

\[
\widetilde N_e<2N_e,
\]

we obtain

\[
\boxed{
H\widetilde N_e
<
2HN_e.
}
\]

Thus P49's less-than-two batching overhead composes directly with P50's fairness factor.

---

## 14. Scientific interpretation boundary

P50 proves a scheduling statement.

It does not change the meaning of the regularity margin.

It does not strengthen a population regularity obstruction into a claim about ontology.

It does not prove quantum mechanics incomplete.

It does not prove an additional physical or spacetime dimension.

It does not prove that the independently defined target is consciousness.

Its valid conclusion is narrower:

\[
\boxed{
\text{finite P48 local threshold}
+
\text{P47 validity}
+
\text{H-fair progress}
\Longrightarrow
\text{finite global asynchronous stopping bound}.
}
\]

---

## 15. Sequential theorem chain after P50

The sequence now reads

\[
\boxed{
\begin{array}{c}
\text{P47: anytime-valid adaptive inference}\\
\Downarrow\\
\text{P48: finite gap-dependent local stopping}\\
\Downarrow\\
\text{P49: sparse dyadic certification looks}\\
\Downarrow\\
\text{P50: asynchronous priority sampling with bounded starvation.}
\end{array}
}
\]

P47 supplies validity.

P48 supplies finite local precision requirements.

P49 reduces complete-certification frequency.

P50 permits unequal preparation sampling while preserving a finite global-time theorem.

---

## 16. Next theorem target

P50 allows priority freedom but controls it only through a worst-case starvation horizon \(H\).

The next mathematically meaningful step is to replace the coarse \(H\)-factor by an **instance-dependent service-rate theorem**.

If preparation \(i\) is guaranteed an asymptotic or finite-window service fraction \(\pi_i>0\), then an edge \(\{i,j\}\) should inherit a global stopping bound controlled by the slower endpoint service rate rather than one common worst-case \(H\).

A rigorous next theorem should state finite-window service conditions precisely and derive the resulting per-edge stopping bound without assuming independence between the adaptive policy and observed data.

---

## 17. Reproducibility

Implementation:
[`bounded_starvation_sampling.py`](../src/consciousness_bridge/bounded_starvation_sampling.py)

Regression tests:
[`test_bounded_starvation_sampling.py`](../tests/test_bounded_starvation_sampling.py)

Publication visual:
[`p50_bounded_starvation_asynchronous_sampling.svg`](figures/p50_bounded_starvation_asynchronous_sampling.svg)

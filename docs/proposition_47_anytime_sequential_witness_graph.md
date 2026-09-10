# Proposition 47: Anytime-valid sequential witness-graph refinement

## Status

**Proved time-uniform finite-family certification theorem for adaptive preparation sampling, graph refinement, witness selection, and stopping.**

P47 combines the statistical logic of P24 and P44 with the shared-preparation design geometry of P45 and the discrete witness-graph layer of P46.

The central point is simple but essential: an adaptive experiment may repeatedly inspect the data and change which preparation it samples next, but the validity statement must already cover every local sample size for every declared preparation stream. Once that stronger simultaneous event is established, the adaptive graph policy can be treated as a measurable choice made inside an event on which all candidate certificates are already valid.

P47 is a statistical and experimental-design theorem. It does not establish quantum incompleteness, physical completeness, or consciousness.

---

## 1. Why P47 is needed

P46 ends with the practical experiment that the earlier propositions do not yet fully justify:

1. collect a small amount of data from several preparations;
2. inspect the current candidate witness graph;
3. identify promising edges;
4. allocate additional samples to shared vertices;
5. eliminate candidates whose population regularity margin is already certified negative;
6. possibly add or retain preparations under a hard budget;
7. stop when one candidate has a strictly positive certified population margin.

P24 permits repeated inspection and stopping for one fixed IID stream. P44 permits post-data selection inside a finite predeclared family at one valid confidence event. P45 optimizes shared preparation-level precision. P46 selects a preparation subset under a hard discrete budget.

The missing theorem is validity when the local sample counts themselves are random because the experiment adaptively decides which preparation to sample next.

P47 closes that gap under a finite declared preparation family and time-uniform confidence sequences for every preparation-level data stream.

---

## 2. Declared witness family

Let

\[
G=(V,E)
\]

be a finite undirected graph. Vertices are declared preparations and edges are candidate regularity witnesses.

For each edge

\[
e=\{i,j\}\in E,
\]

define the population target separation

\[
d_{Y,e}=\|P_i-P_j\|_{\rm TV},
\]

the population quantum separation

\[
d_{Q,e}=D(\rho_i,\rho_j),
\]

and a predeclared bridge regularity constant

\[
L_e\ge0.
\]

The population regularity margin is

\[
\boxed{
M_e=d_{Y,e}-L_e d_{Q,e}.
}
\]

A positive value

\[
M_e>0
\]

is a population obstruction to the declared \(L_e\)-Lipschitz bridge class for that preparation pair. It is not by itself evidence that quantum mechanics is incomplete and is not an experiential conclusion.

---

## 3. Preparation-level data streams

For every preparation \(i\in V\), suppose the experiment has two potential infinite data streams.

The target stream is

\[
Y_{i,1},Y_{i,2},\ldots
\]

with population law \(P_i\).

The quantum-tomography stream is

\[
X_{i,1},X_{i,2},\ldots
\]

under the fixed declared measurement model associated with \(\rho_i\).

The streams need not be physically generated in advance. The mathematical construction only requires that whenever the adaptive policy requests the next observation from stream \(i\), that observation has the declared law and is not altered by the policy's previous choices.

A sufficient model is that each preparation-level stream is IID and that the sampling decision at round \(t\) is measurable with respect to information available before the newly requested outcomes are observed.

This is the non-anticipation condition.

---

## 4. Local time-uniform confidence sequences

For preparation \(i\), let

\[
\widehat P_{i,n}
\]

be the target empirical law after \(n\) target observations and let

\[
\widehat\rho_{i,n}
\]

be the quantum reconstruction after \(n\) quantum observations.

Suppose the target confidence sequence satisfies

\[
\boxed{
\Pr\left(
\|\widehat P_{i,n}-P_i\|_{\rm TV}
\le
\varepsilon_i(n)
\quad\forall n\ge1
\right)
\ge
1-\alpha_{Y,i}.
}
\]

Suppose the quantum confidence sequence satisfies

\[
\boxed{
\Pr\left(
D(\widehat\rho_{i,n},\rho_i)
\le
r_i(n)
\quad\forall n\ge1
\right)
\ge
1-\alpha_{Q,i}.
}
\]

P47 does not require a particular confidence-sequence construction. P24 supplies one transparent option: allocate the stream-level error budget across local sample sizes using

\[
\boxed{
\alpha_{i,n}
=
\frac{6\alpha_i}{\pi^2n^2},
}
\]

and apply a fixed-sample concentration theorem at each local \(n\). Since

\[
\sum_{n=1}^{\infty}\alpha_{i,n}=\alpha_i,
\]

a union bound produces a valid all-local-sample-size event for stream \(i\).

Sharper martingale, e-process, or mixture confidence sequences may replace this conservative construction without changing the deterministic P47 argument.

---

## 5. Finite-family confidence allocation

Require

\[
\boxed{
\sum_{i\in V}\alpha_{Y,i}\le\alpha_Y,
\qquad
\sum_{i\in V}\alpha_{Q,i}\le\alpha_Q.
}
\]

The allocation can be equal or can use positive scientific design weights declared before the certification evidence is inspected.

Define the preparation-level good events

\[
\mathcal E_{Y,i}
=
\left\{
\|\widehat P_{i,n}-P_i\|_{\rm TV}
\le\varepsilon_i(n)
\quad\forall n\ge1
\right\},
\]

and

\[
\mathcal E_{Q,i}
=
\left\{
D(\widehat\rho_{i,n},\rho_i)
\le r_i(n)
\quad\forall n\ge1
\right\}.
\]

Let

\[
\boxed{
\mathcal E_*
=
\bigcap_{i\in V}
\left(
\mathcal E_{Y,i}\cap\mathcal E_{Q,i}
\right).
}
\]

---

## 6. Proposition 47A: one event controls every preparation and every local sample size

By the union bound,

\[
\Pr(\mathcal E_*^c)
\le
\sum_{i\in V}\Pr(\mathcal E_{Y,i}^c)
+
\sum_{i\in V}\Pr(\mathcal E_{Q,i}^c).
\]

Therefore

\[
\boxed{
\Pr(\mathcal E_*)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

No independence assumption among the confidence events is required for this union-bound statement.

The event \(\mathcal E_*\) is stronger than a guarantee at one globally fixed sample size. It controls every positive local sample size of every declared stream simultaneously.

This is the key object that permits adaptive allocation.

---

## 7. Adaptive global rounds and random local sample counts

Let

\[
\mathcal F_t
\]

denote the information available after global round \(t\).

At the start of round \(t+1\), the experiment may use all currently observed information to decide:

- which preparation or preparations to sample next;
- whether the next sample is target, quantum, or both;
- which preparation subset \(S_t\subseteq V\) remains active;
- which induced witness graph is retained;
- how P45 shared precision priorities are changed;
- how P46 design values are updated from already observed information;
- which edge appears most promising;
- whether the experiment stops.

Let

\[
N_{Y,i}(t)
\]

and

\[
N_{Q,i}(t)
\]

be the random numbers of target and quantum observations collected from preparation \(i\) by global time \(t\).

These counts can depend arbitrarily on the previously observed history, subject to non-anticipation and any external budget constraints.

---

## 8. Proposition 47B: adaptive local-count substitution is valid

On \(\mathcal E_*\), the confidence inequalities hold for **every** deterministic local sample size \(n\ge1\).

Therefore they also hold at the random local counts generated by the adaptive policy:

\[
\boxed{
\|\widehat P_{i,N_{Y,i}(t)}-P_i\|_{\rm TV}
\le
\varepsilon_i(N_{Y,i}(t))
}
\]

and

\[
\boxed{
D(\widehat\rho_{i,N_{Q,i}(t)},\rho_i)
\le
r_i(N_{Q,i}(t))
}
\]

for every preparation \(i\) and every global time \(t\) for which the corresponding local count is positive.

No optional-stopping correction is needed at this substitution step because the stronger all-local-sample-size event has already been established.

This is the mathematical reason adaptive interleaving of preparation streams is allowed.

---

## 9. Pairwise distance envelopes at adaptive times

For edge

\[
e=\{i,j\},
\]

write the empirical target and quantum distances at global time \(t\) as

\[
\widehat d_{Y,e}(t)
=
\|\widehat P_i(t)-\widehat P_j(t)\|_{\rm TV},
\]

and

\[
\widehat d_{Q,e}(t)
=
D(\widehat\rho_i(t),\widehat\rho_j(t)).
\]

Define the current target uncertainty sum

\[
E_{Y,e}(t)
=
\varepsilon_i(N_{Y,i}(t))
+
\varepsilon_j(N_{Y,j}(t)),
\]

and quantum uncertainty sum

\[
E_{Q,e}(t)
=
r_i(N_{Q,i}(t))
+r_j(N_{Q,j}(t)).
\]

By the triangle inequality and reverse triangle inequality, on \(\mathcal E_*\),

\[
\max\{0,\widehat d_{Y,e}(t)-E_{Y,e}(t)\}
\le d_{Y,e}
\le
\min\{1,\widehat d_{Y,e}(t)+E_{Y,e}(t)\},
\]

and

\[
\max\{0,\widehat d_{Q,e}(t)-E_{Q,e}(t)\}
\le d_{Q,e}
\le
\min\{1,\widehat d_{Q,e}(t)+E_{Q,e}(t)\}.
\]

Hence define

\[
\boxed{
\underline M_e(t)
=
\max\{0,\widehat d_{Y,e}(t)-E_{Y,e}(t)\}
-
L_e\min\{1,\widehat d_{Q,e}(t)+E_{Q,e}(t)\},
}
\]

and

\[
\boxed{
\overline M_e(t)
=
\min\{1,\widehat d_{Y,e}(t)+E_{Y,e}(t)\}
-
L_e\max\{0,\widehat d_{Q,e}(t)-E_{Q,e}(t)\}.
}
\]

Then on \(\mathcal E_*\),

\[
\boxed{
\underline M_e(t)
\le M_e\le
\overline M_e(t)
\qquad
\forall e\in E,
\quad
\forall t.
}
\]

The complete edge family is therefore controlled simultaneously across the entire adaptive experiment.

---

## 10. Proposition 47C: arbitrary adaptive graph and witness selection

At global time \(t\), let the experiment choose an active preparation subset

\[
\widehat S_t
=
\mathcal S_t(\mathcal F_t),
\]

and an active edge family

\[
\widehat E_t
\subseteq E[\widehat S_t].
\]

Let it then select any candidate witness edge

\[
\widehat e_t
=
\mathcal W_t(\mathcal F_t)
\in\widehat E_t.
\]

The selection rule may depend on:

- the current lower margin;
- the current upper margin;
- a P45 shared-allocation score;
- a P46 budgeted graph score;
- current uncertainty width;
- any other measurable function of the observed history.

On \(\mathcal E_*\), every declared edge interval is valid before the random selection is applied. Therefore the selected interval is also valid:

\[
\boxed{
\underline M_{\widehat e_t}(t)
\le
M_{\widehat e_t}
\le
\overline M_{\widehat e_t}(t)
\qquad
\forall t.
}
\]

Consequently,

\[
\boxed{
\underline M_{\widehat e_t}(t)>0
\Longrightarrow
M_{\widehat e_t}>0
}
\]

with global confidence at least

\[
\boxed{
1-\alpha_Y-\alpha_Q.
}
\]

No additional candidate-count penalty is required after selection because the declared finite family was already covered simultaneously.

---

## 11. Proposition 47D: anytime-valid stopping rule

Let \(\tau\) be any stopping time with respect to the observed experimental history.

Examples include

\[
\tau_+
=
\inf\left\{
t:
\max_{e\in\widehat E_t}
\underline M_e(t)>0
\right\},
\]

or a rule that also requires a minimum robustness reserve

\[
\tau_\gamma
=
\inf\left\{
t:
\max_{e\in\widehat E_t}
\underline M_e(t)>\gamma
\right\},
\qquad
\gamma>0.
\]

Because \(\mathcal E_*\) makes every edge certificate valid at every global time, it remains valid at the random time \(\tau\).

Therefore

\[
\boxed{
\Pr\left(
\tau<\infty
\Longrightarrow
\left[
\underline M_{\widehat e_\tau}(\tau)>0
\Longrightarrow
M_{\widehat e_\tau}>0
\right]
\right)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

If \(\tau<\infty\) almost surely and the experiment stops only after a positive lower bound is observed, then

\[
\boxed{
\Pr\left(
M_{\widehat e_\tau}>0
\right)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

The stopping rule may be chosen adaptively and may depend on the same data used to select the witness edge.

---

## 12. Proposition 47E: safe elimination and vertex pruning

The simultaneous upper margin provides the complementary safe-elimination rule.

If at time \(t\)

\[
\boxed{
\overline M_e(t)<0,
}
\]

then on \(\mathcal E_*\),

\[
M_e<0.
\]

Thus the edge cannot be a positive-margin witness under the declared bridge regularity class.

A preparation \(i\) can be removed from the active witness search if every declared active edge incident to \(i\) satisfies

\[
\boxed{
\overline M_e(t)<0.
}
\]

On \(\mathcal E_*\), this pruning cannot remove any positive-margin witness edge from the declared family because every removed incident edge has already been certified negative.

This gives a mathematically valid mechanism for shrinking the P46 graph during the experiment.

---

## 13. P45 shared allocation inside P47

P45 supplies the preparation-level uncertainty geometry

\[
\varepsilon_i
\propto
n_{Y,i}^{-1/2},
\qquad
r_i
\propto
n_{Q,i}^{-1/2},
\]

and the incidence-weighted KKT law for efficient shared sampling.

P47 does not require the experiment to follow the exact P45 optimum at every round. Instead, P45 can be used as a policy engine inside the P47 validity envelope.

At time \(t\), the experiment may compute a history-dependent set of active constraints and request the next samples from the preparations with the greatest predicted reduction in active edge uncertainty.

Because the P47 event controls every local count of every stream, such adaptive shared allocation does not invalidate the final simultaneous certificate.

The logical separation is

\[
\boxed{
\text{P45 chooses where precision is valuable}
\quad+
\quad
\text{P47 guarantees validity under adaptive delivery of that precision}.
}
\]

---

## 14. P46 graph selection inside P47

P46 showed that selecting a hard-budget preparation subset to maximize induced witness value is NP-hard in general.

P47 does not remove that computational hardness. It permits P46 or any approximate P46 policy to be used adaptively without converting the optimization heuristic into a statistical assumption.

At time \(t\), the experiment may assign history-dependent design values

\[
w_e(t)
\]

using already observed data and then solve or approximate

\[
\max_{S\subseteq V}
\sum_{e\subseteq S}w_e(t)
\quad
\text{subject to the remaining budget.}
\]

The resulting set \(\widehat S_t\) is allowed to depend on the data because the P47 confidence event already covers every declared edge in the original finite family.

What is not allowed without additional accounting is to introduce a completely new preparation or edge after looking at the certification evidence if that object was absent from the original family-level error allocation.

---

## 15. Proposition 47F: eventual detection under persistent sampling

Statistical validity does not by itself guarantee that a true positive edge will ever receive enough samples. A policy could simply stop sampling it.

Suppose instead that for one edge

\[
e=\{i,j\}
\]

with

\[
M_e>0,
\]

the adaptive policy samples all four required endpoint streams infinitely often:

\[
N_{Y,i}(t),N_{Y,j}(t),N_{Q,i}(t),N_{Q,j}(t)
\longrightarrow\infty.
\]

Assume also that

\[
\varepsilon_i(n),\varepsilon_j(n),r_i(n),r_j(n)
\longrightarrow0
\]

and that the empirical target and quantum distances converge almost surely to their population distances.

Then

\[
\underline M_e(t)
\longrightarrow
M_e
>0
\]

along the sampled sequence.

Therefore, with probability one under those consistency assumptions, there exists a finite random round after which

\[
\boxed{
\underline M_e(t)>0.
}
\]

P47 thus separates two questions cleanly:

\[
\boxed{
\text{validity}
\quad\text{from}\quad
\text{sampling efficiency}.
}
\]

Validity holds for any non-anticipating adaptive policy satisfying the declared confidence-sequence premises. Eventual detection requires that truly informative edges continue to receive data.

---

## 16. Complete P24 + P44 + P45 + P46 composition

The theorem chain can now be written as

\[
\boxed{
\begin{array}{c}
\text{P24: time-uniform confidence logic}\\
+\\
\text{P44: simultaneous finite-family post-selection}\\
+\\
\text{P45: shared preparation-level precision geometry}\\
+\\
\text{P46: hard-budget witness-graph selection}\\
\Downarrow\\
\text{P47: anytime-valid sequential graph refinement and stopping.}
\end{array}
}
\]

The roles are distinct.

P24 supplies all-time validity.

P44 supplies family-level post-selection logic.

P45 supplies efficient precision sharing across incident edges.

P46 supplies the discrete preparation-selection layer.

P47 proves that these can be composed without losing the global confidence guarantee when the local sample counts are themselves chosen adaptively.

---

## 17. A valid sequential procedure

One scientifically disciplined P47 procedure is:

1. predeclare \(V\), \(E\), \(L_e\), the target and tomography models, and total error budgets;
2. allocate \(\alpha_Y\) and \(\alpha_Q\) across preparation-level streams;
3. construct all-local-sample-size confidence sequences for every declared stream;
4. collect a pilot sample from the desired initial preparations;
5. compute simultaneous \([\underline M_e(t),\overline M_e(t)]\) intervals;
6. eliminate edges with \(\overline M_e(t)<0\);
7. prune vertices whose remaining incident edges are all certified negative;
8. use P45 uncertainty pressure and P46 budget structure to choose the next preparation-level samples;
9. repeat the interval update after each global round;
10. stop when a predeclared rule such as \(\max_e\underline M_e(t)>0\) is satisfied or when the external resource budget is exhausted.

At every step, the adaptive decisions affect efficiency but not the already established simultaneous coverage event.

---

## 18. What would invalidate the theorem

P47 does not justify unrestricted adaptivity. The proof can fail if any of the following occurs without new accounting:

1. **New candidates are invented after inspection.** A preparation or edge outside the predeclared family is not automatically covered by the original finite-family error budget.
2. **Sampling changes the population law.** If adaptive intervention history changes \(P_i\) or \(\rho_i\), the fixed-stream model is no longer the declared model.
3. **The policy anticipates unobserved outcomes.** Sampling decisions must be based only on already available information.
4. **Fixed-sample intervals are substituted for confidence sequences.** Random local sample sizes require simultaneous local-time validity or another theorem that handles adaptive sampling.
5. **The bridge regularity class changes after seeing the same evidence.** Data-dependent tuning of \(L_e\) is not covered unless the full admissible regularity family is itself included in the simultaneous inference.
6. **Model misspecification is ignored.** Tomography calibration error, target-label misspecification, dependence, drift, or hidden intervention changes are not repaired by optional-stopping mathematics.

---

## 19. Scientific boundary

P47 proves a statistical statement of the form

\[
\boxed{
\text{adaptive data collection}
+
\text{adaptive graph refinement}
+
\text{adaptive witness selection}
+
\text{adaptive stopping}
}
\]

can preserve a declared global coverage level when the experiment begins with simultaneous time-uniform confidence sequences for every member of the finite preparation family.

It does not prove that the quantum state is ontologically complete.

It does not prove that a target variable is experiential.

It does not prove that a positive regularity margin reveals a new physical dimension.

It does not prove that consciousness lies outside spacetime or outside quantum theory.

The valid conclusion remains narrower:

\[
\boxed{
\underline M_{\widehat e_\tau}(\tau)>0
\Longrightarrow
M_{\widehat e_\tau}>0
}
\]

for the declared population distances and declared bridge regularity class, at the stated simultaneous confidence level.

That narrower claim is exactly what makes the result scientifically usable.

---

## 20. Next theorem target

P47 solves the validity problem for adaptive sequential witness-graph search, but it intentionally leaves the **efficiency** problem open.

The next natural theorem is an oracle-efficiency or sample-complexity result for a concrete sequential acquisition rule.

A P48 target should compare an implementable adaptive policy against an oracle that knows the true margins and should quantify the extra sampling cost needed to:

\[
\boxed{
\text{identify one positive-margin edge}
\quad\text{or}\quad
\text{certify that no declared edge exceeds a target margin}.
}
\]

That theorem would move the program from valid adaptive experimentation to provably efficient adaptive experimentation.

---

## 21. Reproducibility

Implementation:
[`sequential_witness_graph.py`](../src/consciousness_bridge/sequential_witness_graph.py)

Regression tests:
[`test_sequential_witness_graph.py`](../tests/test_sequential_witness_graph.py)

Main visual:
[`p47_sequential_graph_refinement.svg`](figures/p47_sequential_graph_refinement.svg)

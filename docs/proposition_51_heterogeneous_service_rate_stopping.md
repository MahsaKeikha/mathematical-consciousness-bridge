# Proposition 51: Heterogeneous finite-window service-rate stopping

## Status

**Proved instance-dependent global-round stopping theorem under preparation-specific finite-window service guarantees.**

P50 uses one common starvation horizon \(H\) for every active preparation. P51 sharpens that bound by allowing each preparation \(i\) to have its own service window and quota,

\[
(W_i,q_i),
\qquad
1\le q_i\le W_i.
\]

Whenever preparation \(i\) remains active throughout any block of \(W_i\) consecutive global rounds, it must be sampled at least \(q_i\) times in that block.

This yields an exact finite-window service rate

\[
\pi_i=\frac{q_i}{W_i},
\]

but the theorem retains the integer window structure rather than replacing it by an asymptotic approximation.

P51 is a scheduling theorem. It does not claim optimality and does not establish quantum incompleteness, an extra physical dimension, or consciousness.

---

## 1. Preparation-specific service guarantee

For each active preparation \(i\), declare integers

\[
W_i\ge1,
\qquad
1\le q_i\le W_i.
\]

The policy satisfies the \((W_i,q_i)\) service guarantee if, whenever \(i\) stays active throughout a consecutive block of \(W_i\) rounds, that block contains at least \(q_i\) selections of \(i\).

Different preparations may therefore receive different guaranteed service rates.

---

## 2. Proposition 51A: finite-window local-count growth

Suppose preparation \(i\) remains active throughout the first \(T\) global rounds.

Partition the first

\[
W_i\left\lfloor\frac{T}{W_i}\right\rfloor
\]

rounds into disjoint windows of length \(W_i\).

Each complete window contributes at least \(q_i\) selections of \(i\). Therefore

\[
\boxed{
N_i(T)
\ge
q_i\left\lfloor\frac{T}{W_i}\right\rfloor.
}
\]

To guarantee at least \(N\ge1\) local samples, it is sufficient to choose

\[
\boxed{
T_i(N)
=
W_i\left\lceil\frac{N}{q_i}\right\rceil.
}
\]

Indeed,

\[
\left\lfloor\frac{T_i(N)}{W_i}\right\rfloor
=
\left\lceil\frac{N}{q_i}\right\rceil,
\]

so

\[
N_i(T_i(N))
\ge
q_i\left\lceil\frac{N}{q_i}\right\rceil
\ge N.
\]

---

## 3. Edge stopping time under heterogeneous service

Let edge

\[
e=\{i,j\}
\]

have P48 sufficient local threshold \(N_e\).

Both endpoints must reach that local threshold. Define

\[
T_i(e)=W_i\left\lceil\frac{N_e}{q_i}\right\rceil,
\qquad
T_j(e)=W_j\left\lceil\frac{N_e}{q_j}\right\rceil.
\]

The edge-level global-round threshold is therefore

\[
\boxed{
T_e
=
\max\{T_i(e),T_j(e)\}.
}
\]

This maximum identifies the endpoint service bottleneck for that edge.

---

## 4. Proposition 51B: positive-witness stopping bound

Let

\[
E_+=\{e\in E:M_e>0\}.
\]

On the P47 simultaneous good event, a truly positive edge cannot be removed by the certified-negative pruning rule. Therefore both of its endpoints remain active until positive certification.

For every positive edge \(e=\{i,j\}\), P51A guarantees that both endpoints reach the P48 local threshold \(N_e\) by global round \(T_e\).

Hence define

\[
\boxed{
T_+
=
\min_{e\in E_+}
\max\left\{
W_i\left\lceil\frac{N_e}{q_i}\right\rceil,
W_j\left\lceil\frac{N_e}{q_j}\right\rceil
\right\}.
}
\]

Then

\[
\boxed{
\Pr(\tau_+\le T_+)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

Unlike P50's common \(HK_+\) bound, P51 allows a positive edge with well-served endpoints to certify substantially earlier even if unrelated preparations have slower service guarantees.

---

## 5. Proposition 51C: all-negative stopping bound

Suppose

\[
M_e<0
\qquad
\forall e\in E.
\]

For each negative edge \(e=\{i,j\}\), either it is eliminated earlier, or it remains active long enough that both endpoints receive their P48 local threshold by global round \(T_e\). At that time P48 forces the negative sign certificate on the P47 good event.

Therefore define

\[
\boxed{
T_-
=
\max_{e\in E}
\max\left\{
W_i\left\lceil\frac{N_e}{q_i}\right\rceil,
W_j\left\lceil\frac{N_e}{q_j}\right\rceil
\right\}.
}
\]

Then

\[
\boxed{
\Pr(\tau_0\le T_-)
\ge
1-\alpha_Y-\alpha_Q.
}
\]

---

## 6. P50 is an exact special case

Set

\[
W_i=H,
\qquad
q_i=1
\]

for every preparation.

Then

\[
T_i(N)=H\left\lceil\frac{N}{1}\right\rceil=HN.
\]

Therefore P51 reduces exactly to P50:

\[
\boxed{
T_e=HN_e.
}
\]

The new theorem is thus a strict structural generalization of the common bounded-starvation model.

---

## 7. Finite-window rate interpretation

Define

\[
\pi_i=\frac{q_i}{W_i}.
\]

Ignoring integer rounding for interpretation only,

\[
T_i(N)
\approx
\frac{N}{\pi_i}.
\]

Thus the slower endpoint of an edge controls its global stopping time.

However P51 does **not** replace the exact theorem by

\[
N_i(T)\ge\pi_i T.
\]

That stronger inequality need not hold for every finite \(T\) because service can be delayed within each window. The rigorous statement is the integer finite-window bound

\[
\boxed{
N_i(T)
\ge
q_i\left\lfloor\frac{T}{W_i}\right\rfloor.
}
\]

This distinction prevents an asymptotic service-rate heuristic from being mistaken for a finite-time theorem.

---

## 8. Dynamic pruning remains compatible

The service obligation applies only to windows in which a preparation remains active throughout the complete window.

Once P47 safe pruning removes all incident unresolved edges of preparation \(i\), future windows impose no service quota on \(i\).

Thus heterogeneous service guarantees do not force wasted sampling of already resolved preparations.

---

## 9. Zero-gap boundary remains unchanged

If no positive edge exists and some edge satisfies

\[
M_e=0,
\]

then P48 has no generic finite sign-separation threshold for that edge.

P51 only converts finite local thresholds into global scheduling bounds. Therefore it cannot produce a finite global stopping guarantee where the required local threshold does not exist.

---

## 10. Why finite-window guarantees are stronger than asymptotic frequencies

An asymptotic statement such as

\[
\liminf_{T\to\infty}\frac{N_i(T)}{T}\ge\pi_i>0
\]

allows arbitrarily long finite starvation intervals before the asymptotic rate becomes visible.

That is insufficient for a deterministic finite global-round upper bound of the P51 form.

P51 therefore assumes explicit finite-window service guarantees rather than asymptotic sampling fractions.

This is a deliberate scientific constraint: finite stopping theorems require finite-time progress assumptions.

---

## 11. Scientific boundary

P51 proves only the scheduling implication

\[
\boxed{
\text{P47 validity}
+
\text{P48 finite local thresholds}
+
\text{preparation-specific finite-window service}
\Longrightarrow
\text{instance-dependent finite global stopping}.
}
\]

It does not prove that the service quotas are optimal.

It does not prove that the P48 witness is consciousness.

It does not prove quantum mechanics incomplete.

It does not prove an additional physical or spacetime dimension.

---

## 12. Sequential theorem chain after P51

\[
\boxed{
\begin{array}{c}
\text{P47: anytime-valid adaptive inference}\\
\Downarrow\\
\text{P48: finite local stopping thresholds}\\
\Downarrow\\
\text{P49: sparse dyadic certification}\\
\Downarrow\\
\text{P50: common bounded-starvation global stopping}\\
\Downarrow\\
\text{P51: heterogeneous finite-window service-rate stopping.}
\end{array}
}
\]

P51 replaces one global worst-case fairness factor by endpoint-specific scheduling geometry.

---

## 13. Next theorem target

P51 assumes the service guarantees \((W_i,q_i)\) are already declared.

The next meaningful design question is how to choose those quotas under a global capacity constraint. A rigorous theorem should optimize preparation-specific service allocations against the edge stopping objective while respecting

\[
\sum_i \pi_i\le1,
\]

or its exact finite-window analogue.

That would connect P45's shared-preparation resource geometry to the sequential P47-P51 branch without calling a heuristic allocation optimal unless the optimization problem is explicitly solved.

---

## 14. Reproducibility

Implementation:
[`heterogeneous_service_stopping.py`](../src/consciousness_bridge/heterogeneous_service_stopping.py)

Regression tests:
[`test_heterogeneous_service_stopping.py`](../tests/test_heterogeneous_service_stopping.py)

Publication visual:
[`p51_heterogeneous_service_rate_stopping.svg`](figures/p51_heterogeneous_service_rate_stopping.svg)

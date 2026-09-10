# Proposition 70: exact primal-dual gap decomposition and diagnostic attribution

**Status:** proved optimization-certificate theorem for the declared P63/P68/P69 calibration surrogate.

## 1. Purpose

P68 proves that every positive Lagrange multiplier gives a rigorous lower bound on the unrestricted P63 integer calibration optimum. P69 then optimizes that one-dimensional dual family to a certified numerical tolerance.

Those results answer the question

> How far is a feasible candidate above a valid lower bound?

but a single scalar gap does not explain **why** the certificate is nonzero.

P70 gives an exact decomposition of that scalar gap. For any feasible integer allocation and any declared multiplier \(\lambda>0\), the candidate-to-dual gap splits into two nonnegative parts:

1. **edgewise Lagrangian regret**, measuring how far each chosen count is from minimizing its one-edge Lagrangian term at that common multiplier; and
2. **budget-slack penalty**, measuring the cost of leaving declared budget unused at that multiplier.

The decomposition is algebraically exact. It is also diagnostic rather than causal: an edge's regret is **not** the amount by which the coupled primal objective would improve if that edge alone were changed, because all coordinates share the same budget constraint.

---

## 2. P63 primal problem

Let \(E\) be a finite edge set. For every \(e\in E\), let

- \(b_e>0\) be the effective uncertainty-sensitivity coefficient,
- \(c_e\in\mathbb N\) be the positive integer cost per observation,
- \(k_e\in\mathbb N\), \(k_e\ge1\), be the integer observation count,
- \(B\in\mathbb N\) be the total budget.

For an allocation \(k=(k_e)_{e\in E}\), define

\[
\boxed{
U(k)=\sum_{e\in E}\frac{b_e}{\sqrt{k_e}}.
}
\]

The unrestricted P63 problem is

\[
\boxed{
U_{\rm int}^*(B)
=
\min_{k_e\ge1,\;k_e\in\mathbb N}
\left\{
U(k):\sum_e c_ek_e\le B
\right\}.
}
\]

P70 assumes throughout that the declared candidate \(k\) is feasible:

\[
\boxed{
\sum_e c_ek_e\le B.
}
\]

---

## 3. P68 dual lower bound

For a fixed positive multiplier \(\lambda>0\), define the edgewise Lagrangian term

\[
\ell_e(j;\lambda)
=
\frac{b_e}{\sqrt j}+\lambda c_ej,
\qquad j\in\mathbb N,\;j\ge1.
\]

Define its exact integer minimum

\[
\boxed{
\phi_e(\lambda)
=
\min_{j\ge1}\ell_e(j;\lambda).
}
\]

The P68 dual function is

\[
\boxed{
q(\lambda)
=
\sum_e\phi_e(\lambda)-\lambda B.
}
\]

P68 proves weak duality:

\[
\boxed{
q(\lambda)\le U_{\rm int}^*(B)
\qquad\forall\lambda>0.
}
\]

Consequently, every feasible candidate satisfies

\[
\boxed{
U(k)-q(\lambda)\ge0.
}
\]

P70 refines this nonnegative number into exact nonnegative components.

---

## 4. Edgewise Lagrangian regret

For each edge, define

\[
\boxed{
r_e(k_e;\lambda)
=
\ell_e(k_e;\lambda)-\phi_e(\lambda).
}
\]

Equivalently,

\[
\boxed{
r_e(k_e;\lambda)
=
\frac{b_e}{\sqrt{k_e}}+
\lambda c_ek_e
-
\min_{j\ge1}
\left(
\frac{b_e}{\sqrt j}+\lambda c_ej
\right).
}
\]

Because \(\phi_e(\lambda)\) is the minimum over all admissible positive integers,

\[
\boxed{r_e(k_e;\lambda)\ge0.}
\]

Moreover,

\[
\boxed{
r_e(k_e;\lambda)=0
\iff
k_e\in\arg\min_{j\ge1}\ell_e(j;\lambda).
}
\]

Thus an edge has zero diagnostic regret exactly when its chosen count is individually Lagrangian-optimal at the common multiplier.

---

## 5. Budget slack and its penalty

Define the used budget

\[
C(k)=\sum_e c_ek_e
\]

and the budget slack

\[
\boxed{s(k)=B-C(k).}
\]

Feasibility gives

\[
\boxed{s(k)\ge0.}
\]

At multiplier \(\lambda>0\), define the slack penalty

\[
\boxed{p_{\rm slack}(k;\lambda)=\lambda s(k).}
\]

Therefore

\[
\boxed{p_{\rm slack}(k;\lambda)\ge0,}
\]

with

\[
\boxed{p_{\rm slack}(k;\lambda)=0\iff C(k)=B.}
\]

The positivity of \(\lambda\) matters here. P70 uses the same positive-multiplier domain as P68 and P69.

---

## 6. Exact decomposition theorem

Starting from the sum of edgewise regrets,

\[
\sum_e r_e(k_e;\lambda)
=
\sum_e
\left[
\frac{b_e}{\sqrt{k_e}}+\lambda c_ek_e-\phi_e(\lambda)
\right].
\]

Collect terms:

\[
\sum_e r_e(k_e;\lambda)
=
U(k)+\lambda C(k)-\sum_e\phi_e(\lambda).
\]

Add the slack penalty:

\[
\sum_e r_e(k_e;\lambda)+\lambda[B-C(k)]
=
U(k)+\lambda C(k)-\sum_e\phi_e(\lambda)
+\lambda B-\lambda C(k).
\]

The \(\lambda C(k)\) terms cancel, giving

\[
\sum_e r_e(k_e;\lambda)+\lambda[B-C(k)]
=
U(k)-\left[\sum_e\phi_e(\lambda)-\lambda B\right].
\]

Using the definition of \(q\),

\[
\boxed{
U(k)-q(\lambda)
=
\sum_e r_e(k_e;\lambda)
+
\lambda\left(B-\sum_e c_ek_e\right).
}
\]

This is an identity, not an inequality.

Because every term on the right is nonnegative, P70 also yields a constructive proof of the P68 candidate-to-dual nonnegativity relation:

\[
\boxed{
U(k)-q(\lambda)\ge0.
}
\]

---

## 7. Zero-decomposition characterization

Since the right-hand side is a finite sum of nonnegative quantities,

\[
U(k)-q(\lambda)=0
\]

if and only if every one of those quantities vanishes.

Therefore

\[
\boxed{
U(k)=q(\lambda)
}
\]

if and only if both conditions hold:

\[
\boxed{
\sum_e c_ek_e=B
}
\]

and

\[
\boxed{
k_e\in\arg\min_{j\ge1}\ell_e(j;\lambda)
\quad\forall e.
}
\]

This is exactly the structural content needed by P67: a budget-tight integer allocation whose every coordinate minimizes its one-edge Lagrangian term at one common positive multiplier.

Hence the P70 zero case recovers the P67 sufficient certificate:

\[
\boxed{
\text{P70 zero decomposition}
\Longrightarrow
\text{P67 global-optimality certificate}
\Longrightarrow
U(k)=U_{\rm int}^*(B).
}
\]

Conversely, P67's certified witness multiplier makes every edge regret zero and the budget slack zero, so its P70 decomposition is exactly zero.

Thus, within the declared P67 witness conditions,

\[
\boxed{
\text{P67 certificate at }\lambda
\iff
\text{P70 decomposition at }\lambda\text{ is zero}.
}
\]

This equivalence concerns the certificate structure at the common multiplier. It does not claim that every globally optimal P63 allocation must admit such a multiplier.

---

## 8. What a nonzero edge regret means

Suppose

\[
r_e(k_e;\lambda)>0.
\]

Then the declared count \(k_e\) is not an edgewise minimizer of

\[
\frac{b_e}{\sqrt j}+\lambda c_ej.
\]

This identifies a coordinate-level failure of the common-multiplier optimality conditions.

However, it does **not** imply that replacing \(k_e\) by an edgewise Lagrangian minimizer while holding all other counts fixed will improve the feasible primal allocation. Such a replacement can increase spend and violate the shared budget. Even when it remains feasible, the Lagrangian regret includes the multiplier-weighted cost change and is not identical to a direct primal objective improvement.

Therefore P70 supports the statement

> edge \(e\) contributes this amount to the current primal-dual certificate gap at multiplier \(\lambda\),

but not the stronger statement

> changing edge \(e\) alone will improve the primal objective by exactly this amount.

The implementation's `ranked_edge_regrets()` follows precisely this interpretation.

---

## 9. P69-powered strongest-dual diagnostic

P69 certifies the strongest value in the P68 dual family. Let

\[
q^*:=\sup_{\lambda>0}q(\lambda).
\]

Suppose P69 returns

\[
\boxed{
Q_{\rm low}\le q^*\le Q_{\rm up}
}
\]

with

\[
\boxed{
Q_{\rm up}-Q_{\rm low}\le\varepsilon_{\rm dual}.
}
\]

For a fixed feasible candidate \(k\), subtract this bracket from \(U(k)\). Because subtraction reverses order,

\[
U(k)-Q_{\rm up}
\le
U(k)-q^*
\le
U(k)-Q_{\rm low}.
\]

The candidate-to-best-dual gap is nonnegative, so a numerically convenient lower endpoint is

\[
\boxed{
G_{\rm low}
=
\max\{0,U(k)-Q_{\rm up}\}.
}
\]

Define

\[
\boxed{
G_{\rm up}
=
\max\{0,U(k)-Q_{\rm low}\}.
}
\]

Then

\[
\boxed{
G_{\rm low}
\le
U(k)-q^*
\le
G_{\rm up}.
}
\]

When P69's returned multiplier \(\hat\lambda\) realizes \(Q_{\rm low}=q(\hat\lambda)\), the ordinary P70 decomposition at \(\hat\lambda\) gives

\[
\boxed{
G_{\rm up}
=
U(k)-q(\hat\lambda)
=
\sum_e r_e(k_e;\hat\lambda)
+
\hat\lambda\,[B-C(k)].
}
\]

Also,

\[
\boxed{
G_{\rm up}-G_{\rm low}
\le
Q_{\rm up}-Q_{\rm low}
\le
\varepsilon_{\rm dual},
}
\]

except that the explicit truncation at zero can only make the gap interval narrower.

Thus P69 and P70 together give a certified near-best decomposition **within the P68 dual family**.

---

## 10. Relation to the true P63 primal suboptimality

Weak duality gives

\[
q^*\le U_{\rm int}^*(B).
\]

For every feasible candidate,

\[
U_{\rm int}^*(B)\le U(k).
\]

Therefore

\[
0
\le
U(k)-U_{\rm int}^*(B)
\le
U(k)-q^*.
\]

Combining with the P69/P70 diagnostic interval gives

\[
\boxed{
0
\le
U(k)-U_{\rm int}^*(B)
\le
U(k)-q^*
\le
G_{\rm up}.
}
\]

So the P70 upper diagnostic is a rigorous upper bound on the candidate's true P63 objective suboptimality.

The lower endpoint \(G_{\rm low}\) is **not** generally a lower bound on the true primal suboptimality. It is a lower bound on the candidate-to-best-dual gap. A nonzero duality gap can remain even for a primal-optimal candidate.

This distinction prevents an important overclaim.

---

## 11. Special cases

### 11.1 Tight budget

If

\[
C(k)=B,
\]

then the slack term vanishes and

\[
\boxed{
U(k)-q(\lambda)=\sum_e r_e(k_e;\lambda).
}
\]

The complete certificate gap is then attributable to edgewise mismatch at the declared multiplier.

### 11.2 All edges individually minimizing, but budget slack remains

If every edge regret is zero but

\[
C(k)<B,
\]

then

\[
\boxed{
U(k)-q(\lambda)=\lambda[B-C(k)]>0.
}
\]

The common multiplier makes the chosen counts individually optimal, but the candidate cannot satisfy the P67 tight-budget certificate.

### 11.3 P67 exact witness

If the candidate is budget-tight and all edges minimize at one common positive multiplier,

\[
\boxed{
U(k)-q(\lambda)=0.
}
\]

Weak duality then forces

\[
\boxed{
U(k)=q(\lambda)=U_{\rm int}^*(B).
}
\]

### 11.4 Exact P63 optimum without a proved P67 witness

P70 does not assert that a globally optimal integer allocation must have zero decomposition for some positive multiplier. The P67 condition is sufficient, and P70 characterizes exactly when that sufficient certificate closes the gap.

---

## 12. Numerical implementation

The implementation is in

`src/consciousness_bridge/primal_dual_gap_decomposition.py`.

For a declared candidate and multiplier it computes:

- the direct candidate objective \(U(k)\),
- the P68 dual lower bound \(q(\lambda)\),
- every exact one-edge minimizing-count set inherited from P68,
- every edge regret \(r_e(k_e;\lambda)\),
- used budget and budget slack,
- the slack penalty \(\lambda[B-C(k)]\),
- the directly evaluated gap \(U(k)-q(\lambda)\),
- the reconstructed decomposition sum,
- whether the decomposition is numerically zero,
- whether the separate P67 implementation certifies the candidate globally optimal.

The implementation checks the identity numerically and raises rather than silently returning an inconsistent decomposition if floating-point error exceeds the declared internal tolerance.

The P69-powered helper `strongest_dual_gap_diagnostic()` additionally returns the certified interval

\[
G_{\rm low}
\le
U(k)-q^*
\le
G_{\rm up}.
\]

---

## 13. Regression tests

The P70 test suite checks:

1. exact reconstruction with positive budget slack;
2. tight-budget cases where the entire gap is edgewise;
3. the P67 common-multiplier witness as an exact zero decomposition;
4. failure of zero decomposition when either slack or edge mismatch remains;
5. the P69 strongest-dual diagnostic interval;
6. the true P63 candidate gap lying below the P70 upper diagnostic on an exact small instance;
7. complete nonincreasing edge-regret ranking;
8. direct agreement of the candidate objective with its defining formula; and
9. rejection of invalid multipliers, mismatched edge sets, and infeasible candidates.

These tests validate the implemented theorem contract. They do not replace the proof above.

---

## 14. Dependency chain

P70 uses the following established results:

\[
\boxed{
\text{P63 exact integer primal}
\longrightarrow
\text{P67 common-multiplier exactness certificate}
\longrightarrow
\text{P68 Lagrangian lower bound}
\longrightarrow
\text{P69 certified dual optimization}
\longrightarrow
\text{P70 exact gap decomposition}.
}
\]

The logical role of each is different:

- P63 defines and exactly solves the integer primal problem by dynamic programming.
- P67 gives a sufficient zero-gap global-optimality certificate.
- P68 gives a valid lower bound for any positive multiplier.
- P69 finds the strongest such lower bound to a declared tolerance.
- P70 explains exactly where the candidate-to-dual certificate gap comes from.

---

## 15. Scientific boundary

P70 is a theorem about a declared integer resource-allocation surrogate used in the transition-calibration branch of this repository.

It does **not** prove that the surrogate is consciousness. It does not establish an experiential bridge law. It does not show that consciousness is quantum, classical, informational, integrated, or a state of matter. It does not show that quantum theory is incomplete. It does not turn an optimization certificate into evidence about ontology.

Its contribution is narrower and exact:

\[
\boxed{
\text{candidate-to-dual gap}
=
\text{edgewise certificate mismatch}
+
\text{unused-budget penalty}.
}
\]

That decomposition makes the optimization certificate inspectable rather than opaque while preserving the separation between resource-allocation mathematics and the unresolved physical-to-experiential bridge problem.

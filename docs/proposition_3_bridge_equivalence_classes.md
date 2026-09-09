# Proposition 3: observational bridge-equivalence classes

## Physical question

Proposition 2 showed how to decide whether two complete consciousness bridge theories are distinguishable relative to a physical experiment class.

For a serious theory space, pairwise comparison is not enough. Many formally different bridge theories may induce exactly the same observable predictions under every admissible experiment.

The scientifically identifiable object is then not an individual named theory but an equivalence class of theories sharing the same observable fingerprint.

Proposition 3 makes that structure exact.

---

# 1. Theory space and observable fingerprint

Fix:

- a physical equivalence class \(q\in\mathcal Q_P\);
- an admissible experiment class \(\Pi\);
- a set \(\Theta\) of complete bridge theories.

For each theory \(\mathfrak T\in\Theta\) and protocol \(\pi\in\Pi\), let

\[
P_{\mathfrak T}^{\pi,q}
\]

be the observable probability law predicted by the theory.

Define the complete observational fingerprint

\[
\boxed{
\Phi_{\Pi,q}(\mathfrak T)
=
\left(
P_{\mathfrak T}^{\pi,q}
\right)_{\pi\in\Pi}.
}
\]

Thus

\[
\Phi_{\Pi,q}:
\Theta
\longrightarrow
\prod_{\pi\in\Pi}
\mathcal P(\mathcal Y_\pi),
\]

where \(\mathcal P(\mathcal Y_\pi)\) denotes the probability measures on the outcome space of protocol \(\pi\).

---

# 2. Bridge-equivalence relation

Define

\[
\boxed{
\mathfrak T_1
\sim_{\Pi,q}
\mathfrak T_2
}
\]

when

\[
\boxed{
P_{\mathfrak T_1}^{\pi,q}
=
P_{\mathfrak T_2}^{\pi,q}
\quad
\text{for every }\pi\in\Pi.
}
\]

By Proposition 2 this is equivalent to

\[
\boxed{
\Delta_\Pi(\mathfrak T_1,\mathfrak T_2;q)=0.
}
\]

The equivalence class of \(\mathfrak T\) is

\[
[\mathfrak T]_{\Pi,q}
=
\left\{
\mathfrak S\in\Theta:
\mathfrak S\sim_{\Pi,q}\mathfrak T
\right\}.
\]

---

# 3. Proposition

## Proposition 3

For fixed \((\Pi,q)\):

### A. Observational equivalence is an equivalence relation

The relation

\[
\sim_{\Pi,q}
\]

is reflexive, symmetric, and transitive on \(\Theta\).

Therefore the quotient

\[
\boxed{
\Theta/{\sim_{\Pi,q}}
}
\]

is well defined.

### B. Equivalence classes are exactly the fibers of the observational fingerprint

For every \(\mathfrak T\in\Theta\),

\[
\boxed{
[\mathfrak T]_{\Pi,q}
=
\Phi_{\Pi,q}^{-1}
\left(
\Phi_{\Pi,q}(\mathfrak T)
\right).
}
\]

### C. The empirically identifiable quotient is isomorphic to the fingerprint image

Define

\[
\widetilde\Phi_{\Pi,q}:
\Theta/{\sim_{\Pi,q}}
\longrightarrow
\operatorname{Im}(\Phi_{\Pi,q})
\]

by

\[
\boxed{
\widetilde\Phi_{\Pi,q}
([\mathfrak T]_{\Pi,q})
=
\Phi_{\Pi,q}(\mathfrak T).
}
\]

Then \(\widetilde\Phi_{\Pi,q}\) is a bijection.

Consequently, the maximum theory-level information available from the declared experiment class is exactly the observational fingerprint class, not necessarily the original theory label.

---

# 4. Proof

## 4.1 Part A

### Reflexivity

For every \(\mathfrak T\in\Theta\),

\[
P_{\mathfrak T}^{\pi,q}
=
P_{\mathfrak T}^{\pi,q}
\]

for every protocol, so

\[
\mathfrak T\sim_{\Pi,q}\mathfrak T.
\]

### Symmetry

If

\[
\mathfrak T_1\sim_{\Pi,q}\mathfrak T_2,
\]

then

\[
P_{\mathfrak T_1}^{\pi,q}
=
P_{\mathfrak T_2}^{\pi,q}
\]

for every \(\pi\). Equality is symmetric, hence

\[
\mathfrak T_2\sim_{\Pi,q}\mathfrak T_1.
\]

### Transitivity

If

\[
\mathfrak T_1\sim_{\Pi,q}\mathfrak T_2
\]

and

\[
\mathfrak T_2\sim_{\Pi,q}\mathfrak T_3,
\]

then for every \(\pi\),

\[
P_{\mathfrak T_1}^{\pi,q}
=
P_{\mathfrak T_2}^{\pi,q}
=
P_{\mathfrak T_3}^{\pi,q}.
\]

Therefore

\[
\mathfrak T_1\sim_{\Pi,q}\mathfrak T_3.
\]

Thus \(\sim_{\Pi,q}\) is an equivalence relation.

## 4.2 Part B

By definition,

\[
\mathfrak S\in[\mathfrak T]_{\Pi,q}
\]

if and only if

\[
P_{\mathfrak S}^{\pi,q}
=
P_{\mathfrak T}^{\pi,q}
\]

for every \(\pi\in\Pi\).

That holds if and only if

\[
\Phi_{\Pi,q}(\mathfrak S)
=
\Phi_{\Pi,q}(\mathfrak T).
\]

Therefore the equivalence class is exactly the fiber of \(\Phi_{\Pi,q}\) through \(\mathfrak T\).

## 4.3 Part C

The map \(\widetilde\Phi_{\Pi,q}\) is well defined by Part B: changing the representative inside an equivalence class does not change the fingerprint.

It is surjective by definition of \(\operatorname{Im}(\Phi_{\Pi,q})\).

It is injective because if

\[
\widetilde\Phi_{\Pi,q}([\mathfrak T_1])
=
\widetilde\Phi_{\Pi,q}([\mathfrak T_2]),
\]

then

\[
\Phi_{\Pi,q}(\mathfrak T_1)
=
\Phi_{\Pi,q}(\mathfrak T_2),
\]

so \(\mathfrak T_1\sim_{\Pi,q}\mathfrak T_2\), hence

\[
[\mathfrak T_1]=[\mathfrak T_2].
\]

Therefore \(\widetilde\Phi_{\Pi,q}\) is bijective.

\[
\boxed{\text{QED}}
\]

---

# 5. No-go consequence

Suppose two theories assign different experiential structures,

\[
\bar B_1(q)\ne\bar B_2(q),
\]

but belong to the same observational equivalence class:

\[
\mathfrak T_1\sim_{\Pi,q}\mathfrak T_2.
\]

Then every admissible protocol has the same data distribution under both theories.

No estimator, classifier, Bayesian update, likelihood-ratio procedure, neural decoder, or other statistical method using only data generated from \(\Pi\) can recover which individual theory is correct from those data, because the data-generating law is identical.

The scientific object identified by the experiment class is therefore

\[
\boxed{
[\mathfrak T]_{\Pi,q},
}
\]

not necessarily \(\mathfrak T\) itself.

---

# 6. Experiment-class refinement

Let

\[
\Pi_1\subseteq\Pi_2.
\]

Then observational equivalence under the richer experiment class can only become finer:

\[
\boxed{
\mathfrak T_1\sim_{\Pi_2,q}\mathfrak T_2
\Longrightarrow
\mathfrak T_1\sim_{\Pi_1,q}\mathfrak T_2.
}
\]

Equivalently, adding admissible experiments can split a previously indistinguishable equivalence class, but cannot merge theories whose predictions were already different under the smaller class.

This gives a precise mathematical reason to enrich consciousness experiments with interventions when passive observation leaves theory classes unresolved.

---

# 7. Physical interpretation

The theorem changes how the project treats competing consciousness theories.

Instead of asking only

> Which named theory is correct?

we first ask

> Which theory distinctions are physically visible to the experiments we can actually perform?

If several theories occupy one bridge-equivalence class, further statistical analysis of the same experiment family cannot resolve them. Progress requires at least one of:

- a richer intervention class;
- a new measurement channel;
- a sharper bridge prediction;
- a stronger physical model;
- or acknowledgment that the difference is empirically underdetermined in the current regime.

---

# 8. Relation to the universal proof target

A universal consciousness theorem cannot be established merely by selecting one formal bridge from an observational equivalence class.

The program must either:

1. find experiments that split the relevant equivalence class; or
2. identify additional first principles that rule out the competing bridges for independently justified reasons.

This makes bridge-equivalence analysis a required stage of the universal proof target.

---

# 9. Status and next result

| Item | Status |
| --- | --- |
| observational bridge-equivalence relation | defined |
| equivalence relation theorem | proved |
| fiber characterization | proved |
| quotient-to-fingerprint bijection | proved |
| experiment-class refinement property | proved |
| bridge selection inside unresolved class | not identifiable from \(\Pi\) alone |

The next result will address **optimal discriminating experiment design**: how to choose protocols that split observational equivalence classes as efficiently as possible.

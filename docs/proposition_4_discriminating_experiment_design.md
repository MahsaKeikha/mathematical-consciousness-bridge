# Proposition 4: optimal discriminating experiment design

## Physical question

Proposition 3 partitions candidate consciousness theories into observational equivalence classes under a declared experiment family.

The next problem is constructive:

> Which experiment, or smallest family of experiments, should be performed to separate the theory classes that are in principle distinguishable?

This is not only a philosophical question. Once each complete bridge theory predicts an observable probability law for each protocol, the problem becomes a finite statistical experiment-design problem.

Proposition 4 gives two complementary constructions:

1. a maximin protocol for one-experiment discrimination;
2. an exact minimum protocol-set formulation when different theory pairs require different experiments.

---

# 1. Setup

Fix a physical equivalence class

\[
q\in\mathcal Q_P,
\]

a finite candidate theory family

\[
\Theta=\{\mathfrak T_1,\ldots,\mathfrak T_K\},
\]

and a finite admissible protocol family

\[
\Pi=\{\pi_1,\ldots,\pi_M\}.
\]

For every theory pair and protocol define

\[
\boxed{
d_{ij}(\pi)
=
\left\|
P_i^{\pi,q}-P_j^{\pi,q}
\right\|_{\mathrm{TV}}.
}
\]

By Proposition 2,

\[
0\le d_{ij}(\pi)\le1.
\]

Let

\[
\mathcal U
=
\left\{
\{i,j\}:
\mathfrak T_i\not\sim_{\Pi,q}\mathfrak T_j
\right\}
\]

be the set of theory pairs that are distinguishable somewhere in the full admissible experiment class.

Pairs not in \(\mathcal U\) are members of the same Proposition 3 observational equivalence class and cannot be separated by any protocol in \(\Pi\).

---

# 2. Single-protocol maximin utility

For one protocol \(\pi\), define its worst distinguishable-pair separation

\[
\boxed{
U_1(\pi)
=
\min_{\{i,j\}\in\mathcal U}
 d_{ij}(\pi).
}
\]

A maximin single protocol is

\[
\boxed{
\pi^*
\in
\arg\max_{\pi\in\Pi}U_1(\pi).
}
\]

The corresponding value is

\[
\boxed{
U_1^*
=
\max_{\pi\in\Pi}
\min_{\{i,j\}\in\mathcal U}
d_{ij}(\pi).
}
\]

If

\[
U_1^*>0,
\]

then one protocol separates every pair of distinct observational equivalence classes.

If

\[
U_1^*=0,
\]

then no single protocol distinguishes every distinguishable pair, even though the complete experiment class may do so collectively.

---

# 3. Protocol-set utility

For a subset

\[
S\subseteq\Pi,
\]

define the pairwise separation achieved by the set as

\[
\boxed{
d_{ij}(S)
=
\max_{\pi\in S}d_{ij}(\pi).
}
\]

Define the worst-pair set utility

\[
\boxed{
U(S)
=
\min_{\{i,j\}\in\mathcal U}
d_{ij}(S).
}
\]

Then

\[
U(S)>0
\]

if and only if every distinguishable theory pair is separated by at least one protocol in \(S\).

For a protocol budget \(k\), the maximin design problem is

\[
\boxed{
S_k^*
\in
\arg\max_{S\subseteq\Pi,\ |S|\le k}
U(S).
}
\]

This selects the protocol set whose weakest still-distinguishable theory pair is separated as strongly as possible.

---

# 4. Exact coverage formulation

For each protocol define the set of distinguishable pairs it separates:

\[
\boxed{
C_\pi
=
\left\{
\{i,j\}\in\mathcal U:
d_{ij}(\pi)>0
\right\}.
}
\]

A protocol set \(S\subseteq\Pi\) is **complete for the theory family** if

\[
\boxed{
\bigcup_{\pi\in S}C_\pi
=
\mathcal U.
}
\]

The minimum-cardinality complete design is

\[
\boxed{
S_{\min}
\in
\arg\min_{S\subseteq\Pi}
|S|
\quad\text{subject to}\quad
\bigcup_{\pi\in S}C_\pi=\mathcal U.
}
\]

If each protocol has physical, financial, ethical, or participant-burden cost \(c_\pi>0\), the weighted design is

\[
\boxed{
S_c^*
\in
\arg\min_{S\subseteq\Pi}
\sum_{\pi\in S}c_\pi
\quad\text{subject to}\quad
\bigcup_{\pi\in S}C_\pi=\mathcal U.
}
\]

This is exactly a set-cover formulation over the universe of empirically distinguishable theory pairs.

---

# 5. Proposition

## Proposition 4

For finite \(\Theta\) and \(\Pi\), with \(\mathcal U\) defined above:

### A. Monotonicity

If

\[
S\subseteq T\subseteq\Pi,
\]

then

\[
\boxed{
U(S)\le U(T).
}
\]

Adding admissible protocols cannot reduce the best available separation for any theory pair.

### B. Exact completeness criterion

\[
\boxed{
U(S)>0
\iff
\bigcup_{\pi\in S}C_\pi=\mathcal U.
}
\]

Thus positive worst-pair utility is exactly equivalent to splitting every pair of distinct observational equivalence classes.

### C. Single-protocol criterion

\[
\boxed{
U_1^*>0
}
\]

if and only if at least one protocol individually covers all pairs in \(\mathcal U\).

### D. Minimum experiment family

The smallest protocol family capable of resolving every distinction that is resolvable somewhere in \(\Pi\) is exactly the minimum set cover of \(\mathcal U\) by \(\{C_\pi:\pi\in\Pi\}\).

---

# 6. Proof

## 6.1 Part A

For every theory pair,

\[
d_{ij}(S)
=
\max_{\pi\in S}d_{ij}(\pi).
\]

If \(S\subseteq T\), maximization over the larger set cannot decrease the value:

\[
d_{ij}(S)\le d_{ij}(T).
\]

Taking the minimum over \(\mathcal U\) preserves the inequality, so

\[
U(S)\le U(T).
\]

## 6.2 Part B

Suppose \(U(S)>0\). Then for every \(\{i,j\}\in\mathcal U\),

\[
d_{ij}(S)>0.
\]

Therefore some \(\pi\in S\) has

\[
d_{ij}(\pi)>0,
\]

so \(\{i,j\}\in C_\pi\). Hence every pair in \(\mathcal U\) belongs to the union of the \(C_\pi\).

Conversely, suppose

\[
\bigcup_{\pi\in S}C_\pi=\mathcal U.
\]

Then every \(\{i,j\}\in\mathcal U\) is separated by at least one protocol in \(S\), so

\[
d_{ij}(S)>0.
\]

Because \(\mathcal U\) is finite, the minimum of these finitely many positive values is positive. Therefore

\[
U(S)>0.
\]

## 6.3 Part C

For a singleton set \(S=\{\pi\}\), Part B gives

\[
U_1(\pi)>0
\iff
C_\pi=\mathcal U.
\]

Maximizing over protocols proves the statement.

## 6.4 Part D

By Part B, a protocol set resolves all distinctions in \(\mathcal U\) exactly when the corresponding coverage sets cover \(\mathcal U\). Minimizing the number of selected protocols is therefore precisely the minimum set-cover problem.

\[
\boxed{\text{QED}}
\]

---

# 7. Statistical meaning of the utility

Total variation has a direct testing interpretation from Proposition 2. For a fixed theory pair and protocol,

\[
R_{ij,\pi}^*
=
\frac12(1-d_{ij}(\pi)).
\]

Therefore maximizing the minimum total-variation separation is equivalent to minimizing the worst optimal equal-prior one-shot error across theory pairs.

For a protocol set \(S\), the quantity

\[
U(S)
\]

is therefore not an arbitrary score. It has a direct operational meaning: it controls the hardest pairwise discrimination remaining after the selected experiments are available.

---

# 8. Physical interpretation for consciousness science

Different consciousness theories can disagree along different physical dimensions.

One pair may differ under perturbation of recurrence. Another may differ under disruption of global broadcasting. Another may differ only under a composition or connectivity intervention.

A single experiment can therefore be a poor universal discriminator even when the theories are jointly distinguishable.

Proposition 4 formalizes a research strategy:

1. derive explicit observable laws from each bridge theory;
2. calculate pairwise separations for candidate protocols;
3. identify unresolved observational equivalence classes;
4. select the smallest or strongest experiment family that splits the resolvable classes;
5. preregister the corresponding theory predictions and failure criteria.

This generalizes the logic of adversarial collaboration into a mathematical experiment-design problem.

---

# 9. Relation to contemporary adversarial testing

The 2025 Cogitate Consortium study preregistered divergent predictions of IIT and global neuronal workspace theory and tested them with multiple modalities.

Proposition 4 abstracts that philosophy. Rather than choosing experiments only from one theory's preferred mechanism, candidate protocols are evaluated by how strongly they separate the full declared theory family.

The framework can therefore be used to design future adversarial comparisons before data collection.

---

# 10. Status and next step

| Item | Status |
| --- | --- |
| pairwise protocol separation \(d_{ij}(\pi)\) | defined |
| single-protocol maximin utility | defined |
| protocol-set utility | defined |
| monotonicity | proved |
| completeness iff positive utility | proved |
| minimum discriminating set | exact set-cover reduction proved |
| cost-weighted experiment design | formulated |
| empirical theory family | future application |

The next research layer is no longer purely meta-theoretical. The program must begin constructing **candidate bridge families with explicit physical predictions** so that P2-P4 can be applied to real consciousness theories and eventually to a new bridge proposed by this project.

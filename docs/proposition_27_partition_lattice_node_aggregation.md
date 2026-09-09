# Proposition 27: Partition-Lattice Transport Under Node Aggregation

## Status

**Repository theorem.** Proposition 27 formalizes when a partition of fine physical nodes has a mathematically well-defined counterpart after several fine nodes are represented by one coarse node.

The theorem extends the P26 scale program from a fixed partition under compatible observation to the harder case in which the **node set itself changes**. It is a theorem about declared physical representation and finite response laws. It does not establish genuine physical fusion, physical completeness, or an experiential interpretation.

---

# 1. Problem

P26 assumes that the partition semantics remain fixed while the response variables are observed more coarsely. That assumption is no longer available if multiple fine nodes become one coarse node.

Let

\[
V_f
\]

be the fine node set and

\[
V_c
\]

be the coarse node set. A node-aggregation map is a surjection

\[
\boxed{
a:V_f\twoheadrightarrow V_c.
}
\]

For each coarse node \(c\in V_c\), define its fine aggregation fiber

\[
\boxed{
F_c=a^{-1}(c).
}
\]

The central question is:

> Which partitions of \(V_f\) still have an unambiguous meaning after the nodes inside every fiber \(F_c\) have become one coarse node?

---

# 2. Aggregation saturation

Let

\[
\pi_f=\{B_1,\ldots,B_r\}
\]

be a partition of \(V_f\).

## Definition

The fine partition \(\pi_f\) is **aggregation saturated** with respect to \(a\) when every aggregation fiber is contained wholly inside one partition block:

\[
\boxed{
\forall c\in V_c\;\exists B\in\pi_f:
F_c\subseteq B.
}
\]

Equivalently,

\[
\boxed{
a(i)=a(j)
\Longrightarrow
i\sim_{\pi_f}j.
}
\]

This means that no coarse node is forced to belong to two different fine partition blocks.

---

# 3. Exact descent criterion

## Proposition 27A

A fine partition \(\pi_f\) has a well-defined coarse partition \(\pi_c\) satisfying

\[
\pi_f
=
\{a^{-1}(B):B\in\pi_c\}
\]

if and only if \(\pi_f\) is aggregation saturated.

Therefore

\[
\boxed{
\pi_f\text{ descends through }a
\iff
\pi_f\text{ is }a\text{-saturated}.
}
\]

### Proof: necessity

Suppose \(\pi_f\) is the inverse-image lift of a coarse partition. Every fiber \(F_c\) belongs to the inverse image of the unique coarse block containing \(c\). Hence every fiber is contained in one fine block.

### Proof: sufficiency

Assume every fiber \(F_c\) is contained in one block of \(\pi_f\). For each fine block \(B\), define its coarse image

\[
a(B)=\{a(v):v\in B\}.
\]

Saturation prevents two distinct fine blocks from sharing a coarse node. Because the fine blocks are disjoint and cover \(V_f\), their images are disjoint and cover \(V_c\). Thus

\[
\boxed{
D_a(\pi_f)=\{a(B):B\in\pi_f\}
}
\]

is a coarse partition, and inverse-image lifting recovers \(\pi_f\).

---

# 4. Non-saturated partitions have no exact coarse meaning

If a fiber \(F_c\) intersects two distinct fine blocks, then the single coarse node \(c\) would have to belong to two distinct coarse blocks. This is impossible for a set partition.

Thus the obstruction is structural, not statistical:

\[
\boxed{
\exists c:\;F_c\cap B_1\ne\varnothing,
\quad
F_c\cap B_2\ne\varnothing,
\quad B_1\ne B_2
\Longrightarrow
\pi_f\text{ has no coarse descent}.
}
\]

No increase in sample size can remove this incompatibility. The aggregation map itself has erased the distinction required by the fine partition.

---

# 5. Lift and descent maps

For a coarse partition

\[
\pi_c=\{C_1,\ldots,C_s\},
\]

define the lift

\[
\boxed{
L_a(\pi_c)
=
\{a^{-1}(C):C\in\pi_c\}.
}
\]

Let

\[
\operatorname{Part}(V_c)
\]

be the partition lattice of the coarse node set, and let

\[
\operatorname{Part}_{\mathrm{sat}}(V_f;a)
\]

be the set of all \(a\)-saturated fine partitions.

P27A gives inverse maps

\[
\boxed{
L_a:
\operatorname{Part}(V_c)
\longrightarrow
\operatorname{Part}_{\mathrm{sat}}(V_f;a)
}
\]

and

\[
\boxed{
D_a:
\operatorname{Part}_{\mathrm{sat}}(V_f;a)
\longrightarrow
\operatorname{Part}(V_c).
}
\]

They satisfy

\[
\boxed{
D_a\circ L_a=\operatorname{id},
\qquad
L_a\circ D_a=\operatorname{id}
}
\]

on their declared domains.

Hence

\[
\boxed{
\operatorname{Part}(V_c)
\cong
\operatorname{Part}_{\mathrm{sat}}(V_f;a).
}
\]

---

# 6. Refinement-order isomorphism

Use the convention

\[
\pi\preceq\sigma
\]

when \(\pi\) refines \(\sigma\), meaning every block of \(\pi\) lies inside some block of \(\sigma\).

## Proposition 27B

For coarse partitions \(\pi_c,\sigma_c\),

\[
\boxed{
\pi_c\preceq\sigma_c
\iff
L_a(\pi_c)\preceq L_a(\sigma_c).
}
\]

### Proof

If \(C\subseteq S\) at the coarse level, then

\[
a^{-1}(C)\subseteq a^{-1}(S).
\]

Thus refinement is preserved by lifting. Applying the inverse descent map gives the converse.

Therefore the lift/descent bijection is an order isomorphism.

---

# 7. Lattice preservation

The partition lattice has a meet \(\wedge\), the finest common refinement, and a join \(\vee\), the coarsest common coarsening.

Because \(L_a\) is an order isomorphism between finite lattices, it preserves both operations. Explicitly,

\[
\boxed{
L_a(\pi_c\wedge\sigma_c)
=
L_a(\pi_c)\wedge L_a(\sigma_c),
}
\]

and

\[
\boxed{
L_a(\pi_c\vee\sigma_c)
=
L_a(\pi_c)\vee L_a(\sigma_c).
}
\]

Thus

\[
\boxed{
\operatorname{Part}(V_c)
\simeq_{\mathrm{lattice}}
\operatorname{Part}_{\mathrm{sat}}(V_f;a).
}
\]

This identifies exactly which part of the fine partition lattice survives node aggregation.

---

# 8. Aggregation-compatible coarse state maps

Node-label compatibility is necessary but not sufficient for the probabilistic P11 quantity. The coarse response coordinates must also respect the node aggregation.

Write a fine response outcome as

\[
x=(x_v)_{v\in V_f}.
\]

For each coarse node \(c\), let

\[
g_c:
\prod_{v\in F_c}\Omega_v
\to
\overline\Omega_c
\]

be a deterministic aggregate-state map acting only on the states inside the fiber \(F_c\).

Then define

\[
\boxed{
C_a(x)
=
\bigl(g_c(x_{F_c})\bigr)_{c\in V_c}.
}
\]

This is an **aggregation-compatible state map**.

It changes both the node count and the response alphabet while retaining an explicit statement of which fine degrees of freedom contribute to each coarse coordinate.

---

# 9. Partition productization commutes for descendable partitions

Let \(\pi_f=L_a(\pi_c)\) be an aggregation-saturated fine partition. For an intervention-conditioned fine response law \(P\), define

\[
P_{\pi_f}
=
\bigotimes_{B\in\pi_f}P_B.
\]

Because every coarse aggregation fiber lies wholly inside one block of \(\pi_f\), and every coarse coordinate depends only on its own fiber, the aggregate map is block-separable with respect to \(\pi_f\) and \(\pi_c\).

Therefore

\[
\boxed{
(C_a)_\#P_{\pi_f}
=
\bigotimes_{C\in\pi_c}
\bigl[(C_a)_\#P\bigr]_C.
}
\]

Equivalently,

\[
\boxed{
(C_a)_\#P_{\pi_f}
=
\bigl((C_a)_\#P\bigr)_{\pi_c}.
}
\]

This is the probabilistic commutation identity required to compare P11 irreducibility across an actual change in node set.

---

# 10. Irreducibility contraction under node aggregation

Define

\[
\kappa_f(\pi_f)
=
\|P-P_{\pi_f}\|_{\mathrm{TV}}
\]

and

\[
\kappa_c(\pi_c)
=
\|(C_a)_\#P-igl((C_a)_\#P\bigr)_{\pi_c}\|_{\mathrm{TV}}.
\]

Using the commutation identity and total-variation data processing,

\[
\kappa_c(\pi_c)
=
\|(C_a)_\#P-(C_a)_\#P_{\pi_f}\|_{\mathrm{TV}}
\le
\|P-P_{\pi_f}\|_{\mathrm{TV}}.
\]

Hence

\[
\boxed{
\kappa_c(\pi_c)
\le
\kappa_f(L_a\pi_c).
}
\]

A valid node aggregation can therefore erase dependence visible across a descendable fine partition, but it cannot create more total-variation irreducibility relative to the corresponding coarse partition.

---

# 11. P18 reconstruction-controlled loss

Let

\[
D=R_\#(C_a)_\#
\]

be a fiber-consistent P18 reconstruction operator and define

\[
\rho(Q)=\|Q-DQ\|_{\mathrm{TV}}.
\]

Apply P18 to the pair

\[
P,
\qquad
P_{\pi_f}.
\]

Then

\[
\boxed{
0
\le
\kappa_f(\pi_f)-\kappa_c(\pi_c)
\le
\rho(P)+\rho(P_{\pi_f}).
}
\]

Thus the node-count reduction has a quantitative certificate whenever the actual response law and the corresponding factorized null are approximately reconstructible.

If

\[
\rho(P)=\rho(P_{\pi_f})=0,
\]

then

\[
\boxed{
\kappa_c(\pi_c)=\kappa_f(\pi_f).
}
\]

---

# 12. Two different sources of scale loss

P27 separates two mathematically different reasons why a fine partition may not survive coarse description.

## 12.1 Semantic obstruction

The partition is not aggregation saturated. Then no coarse partition with the same split exists at all.

## 12.2 Statistical / observational loss

The partition is saturated and descends, but the aggregate-state map discards information. Then the partition exists at both scales, but

\[
\kappa_c<\kappa_f
\]

may occur.

These must not be conflated:

\[
\boxed{
\text{partition has no coarse descent}
\neq
\text{partition descends but its irreducibility is attenuated}.
}
\]

---

# 13. Lossless node-count reduction example

Take fine nodes

\[
V_f=\{1,2,3\}
\]

and coarse nodes

\[
V_c=\{A,B\}
\]

with

\[
a(1)=a(2)=A,
\qquad
a(3)=B.
\]

The fine partition

\[
\pi_f=\{\{1,2\},\{3\}\}
\]

is saturated and descends to

\[
\pi_c=\{\{A\},\{B\}\}.
\]

If the state of coarse node \(A\) retains the ordered pair \((x_1,x_2)\) and \(B\) retains \(x_3\), then the node count has changed while the state map remains invertible on support. The P11 partition irreducibility is therefore preserved exactly.

This demonstrates an important distinction:

\[
\boxed{
\text{fewer declared nodes}
\not\Rightarrow
\text{information loss}.
}
\]

Node aggregation and state compression are separate operations.

---

# 14. Information-destroying node aggregation example

Use the same node map but replace the state of aggregate node \(A\) by one constant symbol. This erases all state distinctions inside the fiber \(\{1,2\}\).

For a fine response distribution with dependence between the \(\{1,2\}\) block and node \(3\), one obtains

\[
\kappa_f(\pi_f)>0
\]

while the coarse response may satisfy

\[
\boxed{
\kappa_c(\pi_c)=0.
}
\]

Thus even a perfectly descendable partition can lose all visible irreducibility when the aggregate-state map destroys the relevant dependence.

---

# 15. Logical dependency

The P27 branch is

\[
\boxed{
\text{P11 partition irreducibility}
+
\text{P17 contraction}
+
\text{P18 reconstruction}
+
\text{P26 compatible partition scale}
+
\text{partition-lattice transport}
\Longrightarrow
\text{P27 node-aggregation certificate}.
}
\]

P26 handles the case in which the node partition is fixed and observation is compatible with it. P27 determines which partitions survive when the node set itself is quotiented by a surjective aggregation map.

---

# 16. Scope boundary

P27 establishes a rigorous transport theorem for the partition component \(\mathcal K\) under declared node aggregation. It does **not** yet establish:

- aggregation of intervention channels;
- how a perturbation targeted at one fine source becomes a perturbation of an aggregate source;
- preservation of the directed-influence component \(\mathcal A\) under source-node aggregation;
- preservation of the complete P11 structure \(\mathfrak C\);
- genuine dynamical fusion or split events;
- physical completeness;
- experiential equivalence;
- consciousness.

The next physical problem is therefore not to make a stronger consciousness claim. It is to formalize **intervention compatibility under source-node aggregation**, so that P25 directed influence can be transported through the same changing node set.

---

# 17. Executable realization

Implementation:

[`src/consciousness_bridge/partition_lattice_node_aggregation.py`](../src/consciousness_bridge/partition_lattice_node_aggregation.py)

Regression tests:

[`tests/test_partition_lattice_node_aggregation.py`](../tests/test_partition_lattice_node_aggregation.py)

The executable suite checks the exact saturation criterion, lift/descent inverses, refinement-order preservation, meet and join preservation, exact irreducibility preservation under lossless node-count reduction, complete loss under information-destroying aggregation, and rejection of a partition that splits an aggregation fiber.

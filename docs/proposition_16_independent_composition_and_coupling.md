# Proposition 16: independent composition and controlled coupling

## Physical question

Propositions 11-15 define a structured physical candidate, audit its internal components, track that structure through physical time, and propagate finite-sample uncertainty through the temporal metric.

A further structural question is unavoidable:

> If two physical systems are placed side by side, when does the intervention-resolved response structure of the joint system reduce to independent composition, and how can departure from that null model be measured?

This question matters before any treatment of splitting or merging because a theory must distinguish **mere coexistence** from **genuine cross-system physical coupling**.

Proposition 16 works at the level of intervention-conditioned response laws themselves. It therefore does not introduce a new consciousness score.

---

# 1. Two finite intervention-response systems

Let systems \(A\) and \(B\) have disjoint response blocks

\[
V_A=\{1,\ldots,m_A\},
\qquad
V_B=\{1,\ldots,m_B\},
\]

with intervention families \(\mathcal U_A,\mathcal U_B\) and a shared finite delay family \(\mathcal T\).

For every delay \(\tau\), write

\[
P_A^{u_A,\tau},
\qquad
P_B^{u_B,\tau}
\]

for the two intervention-conditioned response laws.

The independent product-response composition is defined by

\[
\boxed{
P_{A\otimes B}^{(u_A,u_B),\tau}
=
P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
}
\]

This is a physical null model: the response of one subsystem may depend on its own intervention, but the joint response law factorizes across the declared \(A|B\) split.

---

# 2. Proposition 16A - response-geometry bounds under independent composition

For intervention pairs

\[
(u_A,u_B),
\qquad
(v_A,v_B),
\]

define

\[
d_A
=
\left\|P_A^{u_A,\tau}-P_A^{v_A,\tau}\right\|_{\mathrm{TV}},
\]

\[
d_B
=
\left\|P_B^{u_B,\tau}-P_B^{v_B,\tau}\right\|_{\mathrm{TV}},
\]

and

\[
d_{AB}
=
\left\|
P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}
-
P_A^{v_A,\tau}\otimes P_B^{v_B,\tau}
\right\|_{\mathrm{TV}}.
\]

Then

\[
\boxed{
\max\{d_A,d_B\}
\le
 d_{AB}
\le
 d_A+d_B.
}
\]

A sharper upper bound also follows from maximal couplings:

\[
\boxed{
 d_{AB}
\le
1-(1-d_A)(1-d_B)
=
d_A+d_B-d_Ad_B.
}
\]

## Proof

### Lower bound

Marginalization is a measurable map, and total variation cannot increase under a measurable map. Marginalizing the joint product laws onto subsystem \(A\) yields

\[
d_A\le d_{AB},
\]

and marginalizing onto \(B\) gives

\[
d_B\le d_{AB}.
\]

Hence

\[
\max\{d_A,d_B\}\le d_{AB}.
\]

### Upper bound

Insert the intermediate product law

\[
P_A^{v_A,\tau}\otimes P_B^{u_B,\tau}.
\]

By the triangle inequality,

\[
\begin{aligned}
d_{AB}
&\le
\left\|P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}
-P_A^{v_A,\tau}\otimes P_B^{u_B,\tau}\right\|_{\mathrm{TV}}\\
&\quad+
\left\|P_A^{v_A,\tau}\otimes P_B^{u_B,\tau}
-P_A^{v_A,\tau}\otimes P_B^{v_B,\tau}\right\|_{\mathrm{TV}}.
\end{aligned}
\]

Tensoring both measures with the same probability law preserves total variation, so the two terms are \(d_A\) and \(d_B\). Thus

\[
d_{AB}\le d_A+d_B.
\]

For the sharper bound, choose maximal couplings of the \(A\) pair and the \(B\) pair. The probability that at least one component differs is

\[
1-(1-d_A)(1-d_B),
\]

which is an admissible coupling upper bound on total variation. \(\square\)

---

# 3. Proposition 16B - exact one-factor invariance

If the intervention pair changes only subsystem \(A\), so that \(u_B=v_B\), then

\[
\boxed{
 d_{AB}=d_A.
}
\]

Likewise, if \(u_A=v_A\), then

\[
\boxed{
 d_{AB}=d_B.
}
\]

## Proof

When the \(B\) response law is shared,

\[
\left\|P_A^{u_A,\tau}\otimes R_B-P_A^{v_A,\tau}\otimes R_B\right\|_{\mathrm{TV}}
=
\left\|P_A^{u_A,\tau}-P_A^{v_A,\tau}\right\|_{\mathrm{TV}}.
\]

The same argument holds with \(A\) and \(B\) exchanged. \(\square\)

This result is important for interpreting directed influence in the composed system: adding an independent subsystem does not dilute or amplify an intervention-response distance generated entirely inside the other subsystem.

---

# 4. Proposition 16C - zero cross-system directed influence

Construct source-pair families in the joint intervention space so that an \(A\)-source pair changes only an intervention coordinate belonging to \(A\) while holding the complete \(B\) intervention fixed.

Under independent product-response composition, for every source block \(i\in V_A\), every target block \(j\in V_B\), and every delay \(\tau\),

\[
\boxed{
A_{ij}^{A\otimes B}(\tau)=0.
}
\]

Similarly,

\[
\boxed{
A_{ji}^{A\otimes B}(\tau)=0.
}
\]

for \(j\in V_B\) and \(i\in V_A\).

## Proof

Take any matched intervention pair differing only at an \(A\)-source coordinate. The \(B\) intervention is identical in the pair, so the \(B\)-marginal response law is identical under both joint interventions:

\[
P_{B,j}^{(u_A,u_B),\tau}
=
P_{B,j}^{(v_A,u_B),\tau}.
\]

Their total-variation distance is therefore zero. Taking the supremum over the declared source-pair family remains zero. The reverse direction is identical. \(\square\)

---

# 5. Proposition 16D - exact factorization across the subsystem partition

Let

\[
\pi_{A|B}=\{V_A,V_B\}
\]

be the partition separating the two complete subsystems.

For every independent product-response composition,

\[
\boxed{
\kappa_{A\otimes B}^{\tau}(\pi_{A|B})=0
\qquad\forall\tau\in\mathcal T.
}
\]

## Proof

By construction,

\[
P_{A\otimes B}^{(u_A,u_B),\tau}
=
P_A^{u_A,\tau}\otimes P_B^{u_B,\tau}.
\]

The two marginals induced by \(\pi_{A|B}\) are exactly \(P_A^{u_A,\tau}\) and \(P_B^{u_B,\tau}\). Their partition-product model is therefore the original joint response law. Consequently every intervention-wise total-variation distance to the partition product is zero, and so is the supremum. \(\square\)

---

# 6. Coupling defect

Let \(P_{AB}^{(u_A,u_B),\tau}\) now be an arbitrary observed joint response law, not assumed to factorize.

Let its measured subsystem marginals be

\[
P_{A,\mathrm{marg}}^{(u_A,u_B),\tau},
\qquad
P_{B,\mathrm{marg}}^{(u_A,u_B),\tau}.
\]

Define the response-level coupling defect

\[
\boxed{
\chi_{A|B}(\tau)
=
\sup_{(u_A,u_B)}
\left\|
P_{AB}^{(u_A,u_B),\tau}
-
P_{A,\mathrm{marg}}^{(u_A,u_B),\tau}
\otimes
P_{B,\mathrm{marg}}^{(u_A,u_B),\tau}
\right\|_{\mathrm{TV}}.
}
\]

This is exactly the P11 partition irreducibility for the declared \(A|B\) split:

\[
\boxed{
\chi_{A|B}(\tau)
=
\kappa_{AB}^{\tau}(\pi_{A|B}).
}
\]

Therefore

\[
\boxed{
\chi_{A|B}(\tau)=0
\iff
P_{AB}^{(u_A,u_B),\tau}
=
P_{A,\mathrm{marg}}^{(u_A,u_B),\tau}
\otimes
P_{B,\mathrm{marg}}^{(u_A,u_B),\tau}
\quad\forall(u_A,u_B).
}
\]

This gives an exact **response-factorization certificate** across the declared subsystem split.

---

# 7. What the coupling defect does and does not establish

A positive defect

\[
\chi_{A|B}(\tau)>0
\]

certifies that the observed joint response law does not factorize across the declared split at that delay.

A zero defect certifies response factorization for the measured intervention family and observable response variables.

It does **not** by itself prove the absence of every possible hidden mechanistic interaction. A hidden interaction can remain empirically invisible if the declared interventions and observables fail to expose it. This is an identifiability issue and belongs to the P2-P4/P7 framework.

Thus the scientifically correct hierarchy is

\[
\boxed{
\text{mechanistic independence}
\Longrightarrow
\text{response factorization}
\Longrightarrow
\chi_{A|B}=0,
}
\]

while the reverse implication to mechanistic independence requires additional observability and intervention assumptions.

---

# 8. Composition consistency requirement for a future bridge

Suppose a future bridge assigns experiential equivalence classes to physical systems.

Independent physical composition creates a necessary consistency question:

\[
\boxed{
F_{\mathrm{causal}}(A\otimes B)
\text{ is physically decomposable across }A|B.
}
\]

Any bridge theory that claims the composed physical system corresponds to one, two, or another organization of experiential units must state an additional bridge principle explaining how experiential composition depends on this physical decomposition.

P16 supplies the physical theorem needed to pose that question precisely. It does not choose the experiential answer.

---

# 9. Relation to splitting and merging

P16 treats the fixed partition \(A|B\). It creates the baseline for later structural events:

- **splitting:** coupling defect across a previously integrated split approaches or reaches the independent-response regime;
- **merging:** a previously factorized split develops nonzero cross-structure;
- **controlled coupling:** intervention-dependent cross influence and/or partition defect emerges continuously as coupling is introduced.

A later theorem must define these transitions under changing block sets and finite-data uncertainty.

---

# 10. Mathematical lineage

The proof uses standard properties of total variation under measurable maps, products, triangle inequalities, and couplings. Relevant statistical references already used in the repository include:

- Lucien Le Cam and Grace Lo Yang, *Asymptotics in Statistics: Some Basic Concepts*, 2nd ed., Springer, 2000. DOI: 10.1007/978-1-4612-1166-2.
- Alexandre B. Tsybakov, *Introduction to Nonparametric Estimation*, Springer, 2009. DOI: 10.1007/b13794.

The physical use of controlled interventions follows the causal-intervention framework cited for Proposition 11:

- Judea Pearl, *Causality: Models, Reasoning, and Inference*, 2nd ed., Cambridge University Press, 2009.

The specific composition theorem, coupling-defect interpretation within this physical candidate, and its connection to future bridge-composition consistency are developed in this repository.

---

# 11. Scope and limitations

P16 currently assumes:

1. finite discrete response laws;
2. a declared split into two non-overlapping subsystem block sets;
3. a shared delay family;
4. a product intervention space for the independent-composition null model;
5. observables rich enough to define the declared joint response law.

It does not yet establish:

- finite-sample confidence intervals for the coupling defect;
- composition with changing block counts;
- split/merge event detection;
- continuous-time coupling generators;
- whether physical factorization corresponds to experiential multiplicity.

Those are explicit next steps.

# Physical Foundation

## 1. Why the physical layer must be explicit

A mathematical consciousness bridge cannot operate on an undefined notion of a "system." The physical input must specify what counts as a state, how states evolve, what interventions are admissible, and what observations are available.

The baseline physical object is therefore

\[
\boxed{
p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O).
}
\]

Here:

- \(\mathcal X\) is the physical state space;
- \(\mathcal D\) is the dynamical law or stochastic transition structure;
- \(\mathfrak I\) is the declared class of physically admissible interventions;
- \(\mathcal O\) is the measurement map.

For a deterministic continuous-time model,

\[
\dot x(t)=F(x(t),u(t)),
\qquad
y(t)=h(x(t)),
\]

with \(u\in\mathfrak I\) and \(y=\mathcal O(x)\).

For a stochastic model,

\[
dX_t=f(X_t,u_t)\,dt+G(X_t,u_t)\,dW_t,
\]

or more abstractly,

\[
X_{t+\Delta t}\sim K_{\Delta t}(\cdot\mid X_t,u_t),
\]

where \(K_{\Delta t}\) is a transition kernel.

The bridge theory must state which level of physical description it takes as primitive.

---

## 2. Representation versus physical content

The same physical system can be represented in many coordinate systems.

For an invertible state reparameterization

\[
z=\varphi(x),
\]

the transformed deterministic dynamics are

\[
\dot z
=
D\varphi(x)F(x,u),
\qquad
x=\varphi^{-1}(z).
\]

If \(\varphi\) is only a change of representation, the underlying physical realization has not changed.

A candidate consciousness bridge that assigns different experiential states to \(x\) and \(z=\varphi(x)\) solely because of the coordinate chart would be representation dependent.

This motivates the physical equivalence relation

\[
p\sim_P p'.
\]

The exact content of \(\sim_P\) is itself theory dependent. It may include:

- coordinate relabelings;
- unit changes;
- permutations of physically indistinguishable labels;
- invertible state encodings;
- other transformations proven to preserve the declared physical/intervention structure.

The equivalence class

\[
[p]_{\sim_P}
\]

is the physically meaningful input to the bridge.

---

## 3. Intervention structure

If a bridge theory depends on causal organization, the intervention class cannot remain implicit.

Let

\[
\mathfrak I=\{\iota_\alpha\}_{\alpha\in A}
\]

be a family of admissible interventions. Each intervention induces a modified law

\[
\mathcal D^{(\alpha)}.
\]

Two descriptions should be regarded as causally equivalent only if the declared transformation preserves the intervention-response structure relevant to the theory.

A strong equivalence condition is

\[
\boxed{
P_p^\iota(Y\in A)
=
P_{p'}^{\Phi(\iota)}(Y'\in \Psi(A))
}
\]

for every admissible intervention \(\iota\), measurable outcome set \(A\), and the corresponding transformed intervention and observable maps.

This is stronger than matching one passive observational distribution.

---

## 4. Relation to the companion observer project

Spatiotemporal Observer Mathematics can supply a statistically certified candidate subsystem or world-tube

\[
\mathcal W=(S_0,\ldots,S_{T-1})
\]

inside a larger physical process.

The present repository does not identify that world-tube with consciousness. Instead it may use the certified world-tube as part of the physical input

\[
p_{\mathcal W}
\in\mathcal P.
\]

The bridge problem then begins from the equivalence class

\[
[p_{\mathcal W}]_{\sim_P}.
\]

This preserves a clean logical separation:

\[
\boxed{
\text{system identification}
\neq
\text{consciousness bridge}.
}
\]

---

## 5. External physical lineage

The role of Tegmark 2015 is conceptual: physical organization, information, integration, independence, and dynamics are investigated as candidate principles relevant to observer-like structure.

The present physical layer is more general. It permits deterministic or stochastic dynamics, explicit intervention families, observational maps, and physical equivalence classes before any bridge to experience is imposed.

See [Literature Map](literature_map.md) and [`references.bib`](../references.bib).

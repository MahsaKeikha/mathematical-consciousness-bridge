# Proposition 18: scale sufficiency by approximate reconstruction

## Physical question

Proposition 17 proves that deterministic coarse-graining cannot increase total-variation distinguishability and can erase fine-scale distinctions completely. That result is a necessary warning, but by itself it does not answer the complementary question:

> When is a particular coarse description nevertheless sufficient for a declared family of physical response laws?

Proposition 18 gives a quantitative answer. The key object is not global injectivity of the coarse map. Instead, it is whether the fine response laws relevant to the experiment can be reconstructed from the coarse laws with uniformly small error.

The result is a **scale-sufficiency certificate for intervention-conditioned response laws**. It does not identify any scale with consciousness, and it does not claim that arbitrary coarse-graining preserves every component of the intervention-resolved causal structure.

---

# 1. Fine and coarse response laws

Let

\[
C:\Omega_f\to\Omega_c
\]

be a deterministic coarse-graining map between finite response spaces.

For a fine response law \(P\), define

\[
C_{\#}P(y)
=
\sum_{x:C(x)=y}P(x).
\]

By Proposition 17,

\[
\boxed{
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}.
}
\]

Thus coarse-graining is always non-expansive in total variation.

---

# 2. Fiber-consistent stochastic decoder

Let

\[
R(x\mid y)
\]

be a stochastic decoder from coarse outcomes back to fine outcomes. For physical consistency with the declared coarse map, require

\[
R(x\mid y)>0
\Longrightarrow
C(x)=y.
\]

For a coarse law \(\widetilde P\), define the decoded fine law

\[
(R_{\#}\widetilde P)(x)
=
\sum_{y\in\Omega_c}
R(x\mid y)\widetilde P(y).
\]

The coarse/decode reconstruction operator is

\[
\boxed{
D
=
R_{\#}C_{\#}.
}
\]

For a fine law \(P\), define its reconstruction error

\[
\boxed{
\rho(P)
=
\|P-DP\|_{\mathrm{TV}}.
}
\]

For a declared finite response family \(\mathcal F\), define the uniform reconstruction defect

\[
\boxed{
\rho_{\mathcal F}
=
\sup_{P\in\mathcal F}\rho(P).
}
\]

This quantity is operational: it asks how much fine-scale response information is lost after coarse-graining and best-effort reconstruction with the declared decoder.

---

# 3. Proposition 18A - quantitative response-geometry preservation

For any \(P,Q\in\mathcal F\),

\[
\boxed{
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}
\le
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
+
\rho(P)+\rho(Q).
}
\]

Therefore

\[
\boxed{
0
\le
\|P-Q\|_{\mathrm{TV}}
-
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
\le
2\rho_{\mathcal F}.
}
\]

So a coarse representation with reconstruction defect \(\rho_{\mathcal F}\) preserves every pairwise total-variation response distance to additive error at most \(2\rho_{\mathcal F}\).

## Proof

The lower inequality is Proposition 17.

For the upper inequality, apply the triangle inequality:

\[
\begin{aligned}
\|P-Q\|_{\mathrm{TV}}
&\le
\|P-DP\|_{\mathrm{TV}}
+
\|DP-DQ\|_{\mathrm{TV}}
+
\|DQ-Q\|_{\mathrm{TV}}\\
&=
\rho(P)
+
\|R_{\#}C_{\#}P-R_{\#}C_{\#}Q\|_{\mathrm{TV}}
+
\rho(Q).
\end{aligned}
\]

A stochastic kernel is non-expansive in total variation, hence

\[
\|R_{\#}C_{\#}P-R_{\#}C_{\#}Q\|_{\mathrm{TV}}
\le
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}.
\]

Therefore

\[
\|P-Q\|_{\mathrm{TV}}
\le
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
+
\rho(P)+\rho(Q).
\]

Taking the uniform bound over \(\mathcal F\) gives the \(2\rho_{\mathcal F}\) result.

\(\square\)

---

# 4. Proposition 18B - exact family sufficiency without global injectivity

If

\[
\boxed{
\rho_{\mathcal F}=0,
}
\]

then for every \(P,Q\in\mathcal F\),

\[
\boxed{
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}
=
\|P-Q\|_{\mathrm{TV}}.
}
\]

This can occur even when \(C\) is globally many-to-one.

The important distinction is:

\[
\boxed{
\text{global injectivity of }C
\quad\text{is sufficient but not necessary for}
\quad
\text{exact preservation on a restricted family}.
}
\]

A many-to-one coarse map can be exactly sufficient for a restricted physical family when the conditional fine structure inside each coarse fiber is fixed across that family.

This is the scale analogue of a sufficient statistic: the coarse law can retain all distinctions relevant to the declared response family even though it does not retain every possible fine-state distinction.

---

# 5. Proposition 18C - finite-family identifiability margin

For a finite family \(\mathcal F\), define the minimum fine-scale separation

\[
\boxed{
\delta_f
=
\min_{P\ne Q\in\mathcal F}
\|P-Q\|_{\mathrm{TV}}.
}
\]

Define the corresponding minimum coarse separation

\[
\boxed{
\delta_c
=
\min_{P\ne Q\in\mathcal F}
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}.
}
\]

By Proposition 18A,

\[
\boxed{
\delta_c
\ge
\delta_f-2\rho_{\mathcal F}.
}
\]

Therefore, if

\[
\boxed{
\delta_f>2\rho_{\mathcal F},
}
\]

then

\[
\boxed{
\delta_c>0.
}
\]

Hence all distinct response laws in the declared family remain distinct after coarse-graining.

This gives a directly auditable scale-identifiability condition:

\[
\boxed{
\text{fine-family separation}
>
2\times\text{reconstruction defect}
\Longrightarrow
\text{coarse-family identifiability}.
}
\]

---

# 6. Sharp collapsed-fiber witness

The factor of two cannot in general be improved using only a uniform reconstruction defect.

Let

\[
C(x_0)=C(x_1)=y,
\]

and consider

\[
P=\delta_{x_0},
\qquad
Q=\delta_{x_1}.
\]

Choose the symmetric decoder

\[
R(\cdot\mid y)
=
\tfrac12\delta_{x_0}
+
\tfrac12\delta_{x_1}.
\]

Then

\[
\rho(P)=\rho(Q)=\frac12,
\qquad
\rho_{\mathcal F}=\frac12,
\]

while

\[
\|P-Q\|_{\mathrm{TV}}=1
\]

and

\[
\|C_{\#}P-C_{\#}Q\|_{\mathrm{TV}}=0.
\]

Thus

\[
\boxed{
1-0
=
2\rho_{\mathcal F}.
}
\]

The bound is attained exactly.

---

# 7. Intervention-response geometry corollary

For intervention-conditioned laws \(P_p^{u,\tau}\), define

\[
d_p^{\tau}(u,v)
=
\|P_p^{u,\tau}-P_p^{v,\tau}\|_{\mathrm{TV}},
\]

and after coarse-graining

\[
\widetilde d_p^{\tau}(u,v)
=
\|C_{\#}P_p^{u,\tau}-C_{\#}P_p^{v,\tau}\|_{\mathrm{TV}}.
\]

If the decoder reconstructs every law in the declared intervention-delay family with error at most \(\rho\), then

\[
\boxed{
0
\le
d_p^{\tau}(u,v)-\widetilde d_p^{\tau}(u,v)
\le
2\rho
}
\]

for every compared intervention pair and delay in that family.

Therefore the response-geometry component \(\mathcal G_p\) admits a quantitative scale-stability certificate.

---

# 8. What P18 does not prove

The full candidate physical signature is

\[
\mathfrak C_p
=
(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p).
\]

P18 directly certifies the response-law family and therefore the induced total-variation response geometry \(\mathcal G_p\).

It does **not** automatically prove preservation of:

- directed interventional influence \(\mathcal A_p\) under arbitrary block-changing coarse maps;
- partition irreducibility \(\mathcal K_p\) when the partition lattice itself changes;
- intervention semantics when coarse-graining removes or merges intervention channels;
- physical split/merge dynamics that alter the underlying dynamical law;
- any experiential property.

Those require additional compatibility assumptions and separate theorems.

This boundary is scientifically important. P18 is a scale-sufficiency theorem for a declared response family, not a scale-invariance theorem for consciousness.

---

# 9. Computational certificate

The repository implementation computes:

1. the coarse pushforward \(C_{\#}P\);
2. the decoded law \(R_{\#}C_{\#}P\);
3. each reconstruction error \(\rho(P)\);
4. the uniform family defect \(\rho_{\mathcal F}\);
5. the minimum fine separation \(\delta_f\);
6. the minimum coarse separation \(\delta_c\);
7. the guaranteed lower bound

\[
\boxed{
\delta_c
\ge
\max\{0,\delta_f-2\rho_{\mathcal F}\}.
}
\]

See [`causal_structure_scale_certification.py`](../src/consciousness_bridge/causal_structure_scale_certification.py) and its dedicated tests.

---

# 10. Scientific consequence

P17 says that coarse-graining can destroy information.

P18 adds the complementary positive criterion:

\[
\boxed{
\text{coarse-graining}
+
\text{small reconstructibility defect}
\Longrightarrow
\text{controlled response-geometry distortion}.
}
\]

The scientific question is therefore no longer simply

> Is the coarse map one-to-one?

but rather

> Is the chosen scale sufficient for the physically admissible response family, with a reconstruction defect small relative to the distinctions the experiment must resolve?

That criterion is more appropriate for real multiscale systems, where global microscopic reconstruction is usually impossible and unnecessary, but preservation of experimentally relevant physical distinctions may still be testable.

---

# 11. Provenance

The total-variation contraction steps are standard data-processing facts for deterministic maps and stochastic kernels. The reconstruction-defect formulation, the response-family scale-sufficiency certificate, the explicit \(2\rho\) geometry bound as used in this bridge program, and its role in the intervention-resolved causal-structure hierarchy are repository results.

See:

- [P5 - Physical Feature Sufficiency](proposition_5_feature_sufficiency.md)
- [P7 - Experimental Signature Recovery](proposition_7_experimental_signature_recovery.md)
- [P11 - Intervention-Resolved Causal Structure](proposition_11_intervention_resolved_causal_structure.md)
- [P17 - Coarse-Graining and Refinement](proposition_17_coarse_graining_and_refinement.md)
- [Multiscale Physical Hierarchy](multiscale_physical_hierarchy.md)
- [Equation and Citation Map](equation_and_citation_map.md)
- [`references.bib`](../references.bib)

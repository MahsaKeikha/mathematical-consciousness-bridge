# Proposition 40: Continuous quantum confidence regions and regularity obstructions

## Status

**Proved finite-preparation no-go theorem plus a continuous-region regularity certificate.** P40 addresses the next limitation exposed by P39. A continuous tomography confidence region generally contains quantum state assignments that are distinct but arbitrarily close. If the bridge from quantum state to target law is completely unrestricted, closeness alone cannot refute factorization on a finite preparation set.

P40 therefore proves two complementary results:

1. an unrestricted-factorization no-go statement for injective quantum descriptors;
2. a robust non-factorization certificate for bridge classes with an explicitly declared modulus of continuity.

The theorem remains relative to the declared quantum confidence region, target confidence bounds, and bridge-regularity class. It does not establish that quantum mechanics is incomplete and does not identify the target with consciousness.

---

## 1. Setup

Let

\[
\mathcal X=\{x_1,\ldots,x_n\}
\]

be a finite set of preparations. A candidate quantum descriptor assigns

\[
Q:x\mapsto\rho_x\in\mathcal D(\mathcal H).
\]

Let \(P_x\) be an independently defined target distribution associated with preparation \(x\).

Suppose tomography produces a continuous confidence region

\[
\mathcal C_Q
\]

over admissible quantum descriptor assignments, with

\[
\boxed{
\Pr(Q_*\in\mathcal C_Q)\ge1-\alpha_Q.
}
\]

Suppose target estimation gives simultaneous lower bounds

\[
L_{xx'}
\le
\|P_x-P_{x'}\|_{\mathrm{TV}}
\]

for every preparation pair on an event of probability at least \(1-\alpha_Y\).

---

## 2. P40A: injective-descriptor no-go for unrestricted bridges

Assume a candidate descriptor \(Q\) is injective on the finite preparation set:

\[
\rho_x\neq\rho_{x'}
\qquad
\forall x\neq x'.
\]

Then for any deterministic target assignment \(y:\mathcal X\to\mathcal Y\), there exists a map

\[
g:\operatorname{Im}(Q)\to\mathcal Y
\]

such that

\[
\boxed{y=g\circ Q.}
\]

### Proof

Because \(Q\) is injective on \(\mathcal X\), every point \(\rho_x\in\operatorname{Im}(Q)\) has a unique preparation preimage. Define

\[
g(\rho_x)=y(x).
\]

This is well defined and gives \(g(Q(x))=y(x)\) for every preparation. \(\square\)

The same construction applies to arbitrary target laws \(P_x\): define the bridge on the finite image by

\[
g(\rho_x)=P_x.
\]

Therefore

\[
\boxed{
\text{injective finite quantum descriptor}
+
\text{unrestricted bridge}
\Longrightarrow
\text{factorization is always possible on the sampled preparations}.
}
\]

This is a genuine identifiability limitation, not a failure of statistical power.

---

## 3. Consequence for continuous tomography regions

If the quantum confidence region \(\mathcal C_Q\) contains at least one descriptor assignment that is injective on \(\mathcal X\), then arbitrary target differences do not by themselves refute unrestricted factorization over the whole region.

In particular, small but nonzero trace distances do not help. For every pair with

\[
D(\rho_x,\rho_{x'})>0,
\]

an unrestricted bridge may assign unrelated target laws to those two distinct state points.

Hence

\[
\boxed{
\text{continuous state closeness}
\not\Rightarrow
\text{factorization obstruction without additional structure}.
}
\]

This sharpens the P39 warning. P39 required exact state-fiber hypotheses. P40 explains why that exactness mattered.

---

## 4. Regular bridge class

To obtain a continuous-region obstruction without exact collisions, declare a bridge regularity condition explicitly.

Let

\[
\omega:[0,1]\to[0,1]
\]

be nondecreasing with

\[
\omega(0)=0.
\]

A bridge \(g\) belongs to the declared regularity class when

\[
\boxed{
\|g(\rho)-g(\sigma)\|_{\mathrm{TV}}
\le
\omega\bigl(D(\rho,\sigma)\bigr)
}
\]

for all quantum states relevant to the confidence region.

A common special case is an \(L\)-Lipschitz bridge,

\[
\omega(r)=Lr.
\]

The regularity assumption is not derived from quantum mechanics. It is an additional bridge-model hypothesis and must be scientifically justified separately.

---

## 5. Continuous quantum-distance envelope

For each preparation pair define the confidence-region upper envelope

\[
\boxed{
U_{xx'}
=
\sup_{Q\in\mathcal C_Q}
D(\rho_x^Q,\rho_{x'}^Q).
}
\]

Because \(\omega\) is nondecreasing, every descriptor \(Q\in\mathcal C_Q\) and every bridge in the regularity class obey

\[
\|g(\rho_x^Q)-g(\rho_{x'}^Q)\|_{\mathrm{TV}}
\le
\omega(U_{xx'}).
\]

---

## 6. P40B: pairwise regularity obstruction

Suppose for some pair \(x,x'\),

\[
\boxed{
L_{xx'}>\omega(U_{xx'}).
}
\]

Then no descriptor \(Q\in\mathcal C_Q\) can support a bridge in the declared regularity class that reproduces the true target laws on that pair.

### Proof

On the target-confidence event,

\[
\|P_x-P_{x'}\|_{\mathrm{TV}}
\ge L_{xx'}.
\]

For any \(Q\in\mathcal C_Q\),

\[
D(\rho_x^Q,\rho_{x'}^Q)
\le U_{xx'}.
\]

If \(P_x=g(\rho_x^Q)\) and \(P_{x'}=g(\rho_{x'}^Q)\) for a bridge obeying the declared modulus, then

\[
\|P_x-P_{x'}\|_{\mathrm{TV}}
\le
\omega\left(D(\rho_x^Q,\rho_{x'}^Q)\right)
\le
\omega(U_{xx'}).
\]

This contradicts \(L_{xx'}>\omega(U_{xx'})\). \(\square\)

---

## 7. Robust obstruction margin

Define the pairwise obstruction margin

\[
M_{xx'}
=
L_{xx'}-\omega(U_{xx'}).
\]

Then define

\[
\boxed{
M_*=\max_{x\neq x'}M_{xx'}.
}
\]

If

\[
\boxed{M_*>0,}
\]

then every quantum descriptor in the confidence region is incompatible with every bridge in the declared regularity class, on the joint quantum and target confidence event.

Using the union bound,

\[
\boxed{
\Pr(\text{P40 regularity obstruction is valid})
\ge
1-\alpha_Q-\alpha_Y.
}
\]

No statistical independence assumption between tomography and target estimation is required for this elementary coverage statement.

---

## 8. Lipschitz corollary

For

\[
\omega(r)=Lr,
\]

the condition becomes

\[
\boxed{
L_{xx'}>L\,U_{xx'}.
}
\]

Equivalently, whenever \(U_{xx'}>0\), any admissible bridge fitting that pair must have local effective slope at least

\[
\boxed{
L_{\min}(x,x')
=
\frac{L_{xx'}}{U_{xx'}}.
}
\]

Thus finite data can provide a lower bound on the regularity required of any quantum-state bridge, even when exact state equality cannot be established.

If \(U_{xx'}=0\) and \(L_{xx'}>0\), the theorem reduces to an exact P38/P39 style collision obstruction.

---

## 9. Why the theorem uses an upper quantum-distance envelope

A common error would be to compare target separation with the distance between two point estimates of quantum states. That does not give a robust confidence-region statement.

P40 instead uses

\[
U_{xx'}
=
\sup_{Q\in\mathcal C_Q}D(\rho_x^Q,\rho_{x'}^Q),
\]

which asks for the largest quantum separation still allowed anywhere in the entire declared confidence region.

This is deliberately conservative. If target separation exceeds the bridge modulus even at that largest allowed quantum separation, then every smaller separation in the region is also ruled out.

---

## 10. Relation to P38 and P39

P38 gives the exact factorization theorem:

\[
\rho_x=\rho_{x'}
\Longrightarrow
P_x=P_{x'}.
\]

P39 gives a finite-data certificate when tomography produces a confidence set of models with exact state fibers.

P40 handles continuous confidence regions and proves the missing logical fact:

\[
\boxed{
\text{without exact collisions or bridge regularity, finite-preparation target data cannot rule out unrestricted factorization if an injective descriptor remains admissible.}
}
\]

With a declared regularity class, P40 replaces exact equality by a quantitative incompatibility inequality.

---

## 11. Scientific boundary

P40 can support only a statement of the form

\[
\boxed{
\text{no descriptor in the declared quantum confidence region supports a bridge in the declared regularity class.}
}
\]

It does not establish

\[
\text{no quantum description can support the target},
\]

and it does not establish

\[
\text{the target is nonphysical or experiential}.
\]

A positive obstruction may instead show that the chosen system boundary is too small, the quantum confidence region is misspecified, the regularity class is too restrictive, relevant environmental variables are omitted, target confidence bounds are invalid, or the target itself is poorly defined.

---

## 12. Next theorem target

P40 reduces the continuous-confidence problem to a computable geometric quantity:

\[
U_{xx'}
=
\sup_{Q\in\mathcal C_Q}D(\rho_x^Q,\rho_{x'}^Q).
\]

The next theorem burden is to derive certified upper bounds on \(U_{xx'}\) directly from experimentally specified tomography regions, such as trace-norm balls, likelihood regions, or measurement-frequency confidence sets, and propagate those bounds into an end-to-end sample-complexity guarantee for the regularity obstruction.

---

## 13. Reproducibility

Implementation:
[`continuous_quantum_region_regularity.py`](../src/consciousness_bridge/continuous_quantum_region_regularity.py)

Regression tests:
[`test_continuous_quantum_region_regularity.py`](../tests/test_continuous_quantum_region_regularity.py)

# Proposition 10: robust experiment design for bridge-signature recovery

## Physical question

Propositions 8 and 9 show that exact finite-data recovery of a proposed complete bridge signature is controlled by the robust experimental gap

\[
\gamma_S
=
\delta_S-\omega_S,
\]

where:

- \(\delta_S\) is the smallest experimental separation between physical systems assigned to different signature classes;
- \(\omega_S\) is the largest experimental separation between physical systems assigned to the same signature class.

The natural design problem is therefore not simply to collect more measurements. It is to choose protocols that enlarge between-signature separation without introducing even larger irrelevant within-signature variation.

Proposition 10 formalizes this design problem and proves that adding a protocol can make robust signature recovery worse.

---

# 1. Finite design space

Let

\[
\mathcal Q_0
\]

be a finite physical domain with target signature

\[
F_*:\mathcal Q_0\to\mathcal Z_*.
\]

Let

\[
\Pi_0
=
\{\pi_1,\ldots,\pi_m\}
\]

be a finite library of admissible candidate protocols.

For each protocol \(\pi\) and physical pair \(p,p'\), define

\[
\boxed{
d_\pi(p,p')
=
\|P^{\pi,p}-P^{\pi,p'}\|_{\mathrm{TV}}.
}
\]

For a nonempty protocol family \(S\subseteq\Pi_0\), define

\[
\boxed{
d_S(p,p')
=
\max_{\pi\in S}d_\pi(p,p').
}
\]

and, as in Proposition 8,

\[
\omega(S)
=
\max_{F_*(p)=F_*(p')}d_S(p,p'),
\]

\[
\delta(S)
=
\min_{F_*(p)\ne F_*(p')}d_S(p,p'),
\]

with robust design objective

\[
\boxed{
\Gamma(S)
=
\delta(S)-\omega(S).
}
\]

---

# 2. Budgeted robust design

Let each protocol have nonnegative declared cost

\[
c(\pi)\ge0
\]

and define additive family cost

\[
C(S)
=
\sum_{\pi\in S}c(\pi).
\]

For budget \(B\), define the feasible family

\[
\mathfrak S_B
=
\{S\subseteq\Pi_0:S\ne\varnothing,\ C(S)\le B\}.
\]

The exact robust design is

\[
\boxed{
S_B^*
\in
\arg\max_{S\in\mathfrak S_B}
\Gamma(S).
}
\]

For a protocol-count budget \(b\), set \(c(\pi)=1\) and \(B=b\).

---

# 3. Proposition 10A: existence and finite optimality

If \(\Pi_0\) and \(\mathcal Q_0\) are finite and \(\mathfrak S_B\ne\varnothing\), then an optimal family \(S_B^*\) exists.

Moreover, exhaustive evaluation of \(\Gamma(S)\) over \(\mathfrak S_B\) returns a globally optimal robust design.

## Proof

The finite protocol library has finitely many subsets. Therefore \(\mathfrak S_B\) is finite. Since \(\Gamma(S)\in[-1,1]\) is a real number for every feasible nonempty family, the finite set

\[
\{\Gamma(S):S\in\mathfrak S_B\}
\]

has a maximum. Every family attaining that maximum is globally optimal.

\[
\boxed{\text{QED}}
\]

This result is computational rather than asymptotic: for a modest protocol library, the exact optimum can be audited directly.

---

# 4. Proposition 10B: adding a protocol is not monotone in robust value

Let \(S\subseteq\Pi_0\) and \(\rho\notin S\).

Because

\[
d_{S\cup\{\rho\}}(p,p')
=
\max\{d_S(p,p'),d_\rho(p,p')\},
\]

we always have

\[
\boxed{
\delta(S\cup\{\rho\})
\ge
\delta(S)
}
\]

and

\[
\boxed{
\omega(S\cup\{\rho\})
\ge
\omega(S).
}
\]

Define the marginal between-class gain

\[
\boxed{
a_\rho(S)
=
\delta(S\cup\{\rho\})-\delta(S)
\ge0
}
\]

and marginal within-class inflation

\[
\boxed{
b_\rho(S)
=
\omega(S\cup\{\rho\})-\omega(S)
\ge0.
}
\]

Then

\[
\boxed{
\Gamma(S\cup\{\rho\})-\Gamma(S)
=
a_\rho(S)-b_\rho(S).
}
\]

Therefore:

\[
\boxed{
\Gamma(S\cup\{\rho\})>\Gamma(S)
\iff
a_\rho(S)>b_\rho(S).
}
\]

Likewise, adding \(\rho\) makes the robust gap worse exactly when

\[
\boxed{
a_\rho(S)<b_\rho(S).}
\]

## Proof

The monotonicity of \(\delta\) and \(\omega\) follows because replacing every pair distance by a maximum with one additional nonnegative protocol distance cannot decrease any pair distance. Taking a minimum over between-class pairs or maximum over within-class pairs preserves the stated nondecrease.

Finally,

\[
\begin{aligned}
\Gamma(S\cup\{\rho\})-\Gamma(S)
&=
[\delta(S\cup\{\rho\})-\omega(S\cup\{\rho\})]
-
[\delta(S)-\omega(S)]\\
&=
a_\rho(S)-b_\rho(S).
\end{aligned}
\]

The equivalences follow immediately.

\[
\boxed{\text{QED}}
\]

---

# 5. Explicit nonmonotonicity counterexample

Consider three physical systems

\[
p_1,p_2,p_3
\]

with

\[
F_*(p_1)=F_*(p_2)\ne F_*(p_3).
\]

Suppose protocol \(\pi_A\) produces pair distances

\[
d_A(p_1,p_2)=0.05,
\qquad
d_A(p_1,p_3)=0.60,
\qquad
d_A(p_2,p_3)=0.55.
\]

Then

\[
\omega(\{A\})=0.05,
\qquad
\delta(\{A\})=0.55,
\]

so

\[
\boxed{
\Gamma(\{A\})=0.50.
}
\]

Now add protocol \(\pi_B\) with

\[
d_B(p_1,p_2)=0.50,
\qquad
d_B(p_1,p_3)=0.62,
\qquad
d_B(p_2,p_3)=0.58.
\]

Using the max-over-protocol family distance,

\[
\omega(\{A,B\})=0.50,
\qquad
\delta(\{A,B\})=0.58,
\]

so

\[
\boxed{
\Gamma(\{A,B\})=0.08<0.50.
}
\]

The second protocol creates a small improvement in the weakest between-class distinction but a much larger increase in irrelevant within-signature separation.

Thus more measurement channels or perturbations are not automatically better for bridge-signature recovery.

---

# 6. Proposition 10C: direct connection to the Proposition 9 trial bound

Define the conservative Proposition 9 per-cell trial requirement for a family \(S\) with positive robust gap by

\[
\boxed{
N_{\mathrm{P9}}(S)
=
\left\lceil
\frac{8K^2}{\Gamma(S)^2}
\log\left(
\frac{2N_P|S|K}{\alpha}
\right)
\right\rceil.
}
\]

For two protocol families with the same cardinality and the same \(N_P,K,\alpha\),

\[
\boxed{
\Gamma(S_1)>\Gamma(S_2)>0
\Longrightarrow
N_{\mathrm{P9}}(S_1)
\le
N_{\mathrm{P9}}(S_2).
}
\]

Therefore maximizing \(\Gamma(S)\) at fixed protocol count directly minimizes the current conservative P9 trial bound.

If protocol counts differ, the design objective contains a tradeoff: increasing \(|S|\) raises the logarithmic multiplicity term but may also enlarge or shrink the robust gap.

---

# 7. Cost-aware statistical design

A direct finite-sample/cost objective is

\[
\boxed{
J_\lambda(S)
=
N_{\mathrm{P9}}(S)
+
\lambda C(S),
}
\]

for \(\Gamma(S)>0\), with \(J_\lambda(S)=+\infty\) when \(\Gamma(S)\le0\).

Alternatively, one can solve

\[
\boxed{
\max_{C(S)\le B}\Gamma(S)
}
\]

or

\[
\boxed{
\min_{\Gamma(S)\ge\gamma_0}C(S).
}
\]

These are declared optimization problems, not claims that one objective is universally preferable. Experimental ethics, invasiveness, duration, cost, and biological constraints can enter through the feasible family and cost function.

---

# 8. Difference from Proposition 4

Proposition 4 asks whether a protocol family separates every competing **theory pair**.

Proposition 10 asks whether a protocol family cleanly separates different classes of a proposed **physical bridge signature** while suppressing irrelevant differences within a signature class.

The two objectives need not select the same experiments.

A protocol can be excellent for distinguishing two theories yet poor for recovering a substrate-general signature if it is highly sensitive to implementation details that the bridge regards as experientially irrelevant.

This distinction is central to the universal-proof program.

---

# 9. Scientific interpretation

A mature consciousness experiment should not maximize neural difference for its own sake.

The correct target depends on the theorem being tested.

For a candidate complete bridge signature, a high-quality experiment family should create the geometry

\[
\boxed{
\text{small within-signature variation}
\quad\ll\quad
\text{large between-signature variation}.
}
\]

The robust gap

\[
\Gamma(S)
=
\delta(S)-\omega(S)
\]

quantifies that geometry directly.

This makes a general methodological prediction of the framework:

> Multimodal or multi-perturbation consciousness experiments should be evaluated by whether each added modality increases **bridge-relevant separation relative to bridge-irrelevant variation**, not simply whether it adds statistically significant signal.

---

# 10. Status and next frontier

| Item | Status |
| --- | --- |
| robust protocol-family objective \(\Gamma(S)\) | defined |
| finite budgeted optimum existence | proved |
| exact finite exhaustive optimum | proved |
| nonmonotonicity under adding protocols | proved |
| marginal improvement criterion | proved |
| connection to P9 trial requirement | proved |
| efficient large-library approximation algorithms | open |
| protocol-cost and ethical constraint models | application dependent |

The next scientific frontier is no longer another abstract identifiability theorem. It is the construction of **original candidate physical signatures** and systematic counterexample searches under Propositions 5-10.

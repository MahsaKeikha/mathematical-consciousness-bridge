# Theorem Roadmap

This roadmap records the current proved theorem chain and the open route toward a scientifically meaningful physical-to-experiential bridge.

The program is deliberately layered. A theorem about a physical feature is not promoted to a theorem about consciousness unless the bridge dependency and empirical evidence are explicit.

---

# Layer A. Physical and representational well-definedness

## Proposition 1 - representation-invariant consciousness bridges

A bridge assignment descends uniquely from raw physical descriptions to physical equivalence classes if and only if it is constant on each declared physical-equivalence class:

\[
\boxed{
p\sim_Pp'
\Longrightarrow
B(p)=B(p').
}
\]

Equivalent quotient form:

\[
\bar B:\mathcal P/{\sim_P}\to\mathcal E/{\sim_E}.
\]

**Scientific role:** prevents coordinate systems, units, encodings, or physically irrelevant relabelings from changing the bridge assignment.

---

# Layer B. Theory identifiability and experimental no-go structure

## Proposition 2 - experiment-class bridge identifiability

Defines

\[
\Delta_\Pi(\mathfrak T_1,\mathfrak T_2;q)
=
\sup_{\pi\in\Pi}
\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}.
\]

Proves

\[
\boxed{
\Delta_\Pi=0
\iff
P_1^{\pi,q}=P_2^{\pi,q}
\quad\forall\pi\in\Pi.
}
\]

For equal prior probabilities,

\[
R_\pi^*
=
\frac12
\left(1-\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}\right).
\]

**Scientific role:** makes empirical distinguishability of bridge theories an exact statistical property.

## Proposition 3 - observational bridge-equivalence classes

Defines the complete observable fingerprint

\[
\Phi_{\Pi,q}(\mathfrak T)
=
(P_{\mathfrak T}^{\pi,q})_{\pi\in\Pi}.
\]

Proves

\[
\boxed{
\Theta/{\sim_{\Pi,q}}
\cong
\operatorname{Im}(\Phi_{\Pi,q}).
}
\]

**Scientific role:** identifies the empirically accessible object as an observational equivalence class of theories whenever named theories make identical predictions.

## Proposition 4 - optimal discriminating experiment families

For pairwise protocol separation

\[
d_{ij}(\pi)
=
\|P_i^{\pi,q}-P_j^{\pi,q}\|_{\mathrm{TV}},
\]

defines

\[
U(S)
=
\min_{\{i,j\}\in\mathcal U}
\max_{\pi\in S}d_{ij}(\pi).
\]

Proves

\[
\boxed{
U(S)>0
\iff
\bigcup_{\pi\in S}C_\pi=\mathcal U.
}
\]

Minimum complete finite protocol design is therefore a set-cover problem over distinguishable theory pairs.

**Scientific role:** converts adversarial consciousness-experiment design into an optimization problem.

---

# Layer C. Physical-feature sufficiency and complete bridge signatures

## Proposition 5 - physical-feature sufficiency

For

\[
F:\mathcal Q_P\to\mathcal Z,
\qquad
\bar B:\mathcal Q_P\to\mathcal Q_E,
\]

proves the equivalence

\[
\boxed{
\bar B=g\circ F
\iff
F(p)=F(p')\Rightarrow\bar B(p)=\bar B(p').
}
\]

A single pair satisfying

\[
F(p)=F(p'),
\qquad
\bar B(p)\ne\bar B(p')
\]

refutes sufficiency on the declared domain.

**Scientific role:** turns the statement "physical feature \(F\) is sufficient for the bridge" into a precise factorization claim with a universal counterexample template.

## Proposition 6 - canonical complete bridge signature

Defines

\[
p\sim_Bp'
\iff
\bar B(p)=\bar B(p')
\]

and

\[
C_B(p)=[p]_{\sim_B}.
\]

Proves

\[
\boxed{
C_B(p)=C_B(p')
\iff
\bar B(p)=\bar B(p').
}
\]

and

\[
\boxed{
\mathcal Q_B
\cong
\operatorname{Im}(\bar B).
}
\]

Every bridge-sufficient feature determines the canonical signature; every bridge-complete feature is isomorphic to it on its realized image.

**Scientific role:** gives the exact mathematical target for a complete physical signature of a declared bridge.

---

# Layer D. Experimental recoverability and finite-data certification

## Proposition 7 - experimental signature recovery

For the complete experimental fingerprint

\[
\Psi_\Pi(p)
=
(P^{\pi,p})_{\pi\in\Pi},
\]

proves that a target signature \(F_*\) is recoverable exactly when

\[
\boxed{
\Psi_\Pi(p)=\Psi_\Pi(p')
\Longrightarrow
F_*(p)=F_*(p').
}
\]

A signature-different pair with identical observable fingerprints is an exact no-go counterexample for that experiment class.

**Scientific role:** separates existence of a mathematical complete signature from experimental ability to determine it.

## Proposition 8 - robust signature recovery under distribution error

Defines

\[
d_S(p,p')
=
\max_{\pi\in S}
\|P^{\pi,p}-P^{\pi,p'}\|_{\mathrm{TV}},
\]

within-signature spread \(\omega_S\), between-signature separation \(\delta_S\), and robust gap

\[
\boxed{
\gamma_S=\delta_S-\omega_S.
}
\]

If

\[
\sup_{p,\pi}
\|\widehat P^{\pi,p}-P^{\pi,p}\|_{\mathrm{TV}}
\le\varepsilon,
\]

then

\[
|\widehat d_S-d_S|\le2\varepsilon.
\]

If

\[
\boxed{
\gamma_S>4\varepsilon,
}
\]

an explicit threshold recovers the complete signature partition exactly.

**Scientific role:** establishes the first deterministic finite-error bridge-signature recovery condition.

## Proposition 9 - finite categorical sample complexity

For \(N_P\) physical systems, \(N_\pi\) protocols, categorical alphabet size at most \(K\), and \(n\) IID repetitions per system/protocol cell, a sufficient trial count for exact signature-partition recovery with confidence at least \(1-\alpha\) is

\[
\boxed{
n
\ge
\frac{8K^2}{\gamma_S^2}
\log\left(
\frac{2N_PN_\pi K}{\alpha}
\right).
}
\]

**Scientific role:** closes the first end-to-end chain from candidate complete physical signature to explicit finite-data recovery requirement.

---

# Layer E. Robust protocol design

## Proposition 10 - robust experiment design for signature recovery

For a finite admissible protocol family \(S\), defines

\[
\boxed{
\Gamma(S)=\delta(S)-\omega(S).
}
\]

Under a finite protocol library and finite budget, an optimal family exists and exhaustive finite search returns a global optimum.

For a newly added protocol \(\rho\), defines

\[
a_\rho(S)=\delta(S\cup\{\rho\})-\delta(S),
\]

\[
b_\rho(S)=\omega(S\cup\{\rho\})-\omega(S),
\]

and proves

\[
\boxed{
\Gamma(S\cup\{\rho\})-\Gamma(S)
=
a_\rho(S)-b_\rho(S).
}
\]

Therefore

\[
\boxed{
\Gamma(S\cup\{\rho\})>\Gamma(S)
\iff
a_\rho(S)>b_\rho(S).
}
\]

A realizable Bernoulli counterexample demonstrates that an added protocol can leave the weakest between-signature separation unchanged while substantially inflating within-signature variation.

At fixed protocol count, maximizing \(\Gamma(S)\) minimizes the current conservative Proposition 9 trial requirement because

\[
n\propto\Gamma(S)^{-2}.
\]

**Scientific role:** establishes that multimodal or multi-perturbation measurement should be selected by bridge-relevant separation rather than raw signal abundance.

---

# Layer F. First original physical candidate

## Proposition 11 - Intervention-Resolved Causal Geometry (IRCG)

For a physical subsystem \(p\), admissible interventions \(u\in\mathcal U_p\), and physical delays \(\tau\in\mathcal T\), define the intervention-conditioned joint response law

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L(Y_{t+\tau}^V\mid do(u),p).
}
\]

The intervention-response geometry is

\[
\boxed{
d_p^\tau(u,v)
=
\|P_p^{u,\tau}-P_p^{v,\tau}\|_{\mathrm{TV}}.
}
\]

Directed interventional influence is

\[
\boxed{
A_{ij}^p(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\|P_{p,j}^{u,\tau}-P_{p,j}^{v,\tau}\|_{\mathrm{TV}}.
}
\]

For nontrivial partition \(\pi\), partition response irreducibility is

\[
\boxed{
\kappa_p^\tau(\pi)
=
\sup_{u\in\mathcal U_p}
\left\|
P_p^{u,\tau}
-
\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}
\right\|_{\mathrm{TV}}.
}
\]

The raw causal object is

\[
\mathfrak C_p
=
(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p),
\]

and the representation-invariant candidate signature is its compatible isomorphism class

\[
\boxed{
F_{\mathrm{IRCG}}(p)
=
[\mathfrak C_p]_{\cong}.
}
\]

Proposition 11 proves:

1. invariance under compatible bijective physical reparameterization;
2. the exact partition-factorization certificate
   \[
   \kappa_p^\tau(\pi)=0
   \iff
   P_p^{u,\tau}
   =
   \bigotimes_{B\in\pi}P_{p,B}^{u,\tau}
   \quad\forall u;
   \]
3. an acyclic directed-influence graph contains no perturbational return loop among distinct physical blocks.

IRCG is a structured physical candidate rather than a scalar consciousness score. Its intended strongest future target is

\[
F_{\mathrm{IRCG}}(p)=F_{\mathrm{IRCG}}(p')
\iff
C_B(p)=C_B(p'),
\]

but Proposition 11 does not assume or establish that biconditional.

**Scientific role:** provides the first intervention-grounded physical object rich enough to be attacked by the sufficiency, counterexample, recovery, and experiment-design theorems already proved.

---

# Current dependency graph

\[
\boxed{
\begin{array}{ccccccccccccc}
P1
&\to&P5
&\to&P6
&\to&P7
&\to&P8
&\to&P9
&\to&P10
\to P11\\
&&&&&&\uparrow\\
P2&\to&P3&\to&P4
&&\text{experiment design}
\end{array}
}
\]

Interpretation:

- P1 determines whether a physical feature or bridge is representation well defined.
- P5-P6 determine what sufficiency and completeness mean.
- P2-P4 determine what competing bridge claims can be empirically distinguished and how to design theory-discriminating experiments.
- P7-P9 determine whether a proposed complete signature can be recovered from finite experiments.
- P10 chooses protocol families that preserve bridge-relevant separation while suppressing within-signature nuisance variation.
- P11 introduces the first original physical candidate on which those abstract tests can operate.

---

# Immediate scientific frontier

## Proposition 12 - component insufficiency and minimal-feature audit

The next step is to prevent the new candidate from becoming a kitchen-sink theory by proving which summaries lose essential information.

Let

\[
F_G(p)=\mathcal G_p,
\qquad
F_A(p)=\mathcal A_p,
\qquad
F_K(p)=\mathcal K_p
\]

denote the response-geometry, directed-influence, and partition-irredundancy projections of IRCG.

The target is to construct explicit finite pairs \(p,p'\) satisfying collisions such as

\[
F_G(p)=F_G(p')
\quad\text{but}\quad
F_{\mathrm{IRCG}}(p)\ne F_{\mathrm{IRCG}}(p'),
\]

and analogously for \(F_A\), \(F_K\), and scalar summaries such as response diameter or minimum partition irreducibility.

Such constructions would prove that the corresponding projection cannot reconstruct full IRCG on the declared domain, by the same factorization logic used in Proposition 5.

The strongest useful outcome is a **minimal-feature theorem** identifying which components are genuinely required before any empirical bridge analysis begins.

---

# Later structural frontiers

If IRCG survives controlled counterexample searches, the program should address:

1. **composition consistency:** how signature and bridge classes behave under system coupling, splitting, and merging;
2. **temporal continuation:** when time-indexed bridge assignments define one coherent experiential history;
3. **observer-to-bridge interface:** how a certified moving subsystem from Spatiotemporal Observer Mathematics supplies the physical domain for the bridge;
4. **cross-theory empirical tests:** source-faithful IIT, GNWT, RPT, HOT, predictive/neurorepresentational, and future bridge families;
5. **conditional consciousness theorem:** only after the bridge premises themselves have survived the preceding mathematical and empirical tests.

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

# Current dependency graph

\[
\boxed{
\begin{array}{ccccccccccc}
P1
&\to&P5
&\to&P6
&\to&P7
&\to&P8
&\to&P9
\to P10\\
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

---

# Immediate scientific frontier

## Candidate A - intervention-resolved causal geometry

The next step is to construct a physical signature independently of an assumed experiential label and then try to break it using Propositions 5-10.

The candidate should be based on the **full geometry of controlled perturbational responses**, not a single complexity number. A generic starting object is

\[
\boxed{
\mathcal R_p
=
\left\{
P^{u,\tau}_p
:
u u\in\mathcal U_p,\ 	au\in\mathcal T
\right\},
}
\]

where \(P^{u,\tau}_p\) is the response law of the certified physical subsystem at delay \(\tau\) after admissible intervention \(u\).

The associated intervention-response geometry is

\[
\boxed{
d_p^\tau(u,v)
=
\|P^{u,\tau}_p-P^{v,\tau}_p\|_{\mathrm{TV}}.
}
\]

The candidate program must then test whether this geometry, augmented only by mathematically justified irreducibility and temporal structure, can distinguish:

1. integrated recurrent systems from decomposable systems;
2. sustained differentiated responses from stereotyped global responses;
3. conscious conditions from matched unconscious conditions;
4. biological realizations from substrate changes that preserve the relevant causal geometry;
5. sophisticated controllers or simulations that provide P5 counterexamples.

No consciousness claim follows merely from constructing this object. Its value is that it produces a precise, perturbation-based candidate that can be exposed to the complete falsification machinery already proved.

---

# Later structural frontiers

If Candidate A survives controlled counterexample searches, the program should address:

1. **feature-lattice minimality:** which components of the intervention-resolved geometry are necessary, redundant, or jointly sufficient;
2. **composition consistency:** how signature and bridge classes behave under system coupling, splitting, and merging;
3. **temporal continuation:** when time-indexed bridge assignments define one coherent experiential history;
4. **observer-to-bridge interface:** how a certified moving subsystem from Spatiotemporal Observer Mathematics supplies the physical domain for the bridge;
5. **cross-theory empirical tests:** source-faithful IIT, GNWT, RPT, HOT, predictive/neurorepresentational, and future bridge families;
6. **conditional consciousness theorem:** only after the bridge premises themselves have survived the preceding mathematical and empirical tests.

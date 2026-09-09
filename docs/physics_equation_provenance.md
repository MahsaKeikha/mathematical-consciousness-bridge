# Physics Equation Provenance Map

This page is the physics-facing provenance layer for the Mathematical Consciousness Bridge program. It distinguishes **standard physical laws and mathematical identities**, **repository constructions**, **empirical observables**, and **open bridge objects**.

The governing discipline is

\[
\boxed{
\text{equation}
\neq
\text{physical interpretation}
\neq
\text{measurement}
\neq
\text{empirical evidence}
\neq
\text{experiential conclusion}.
}
\]

For a broader source map, see [Foundational Physics, Mathematics, and Spaceflight Bibliography](foundational_physics_mathematics_bibliography.md). For the consciousness-theory and proposition-specific map, see [Equation and Citation Map](equation_and_citation_map.md).

---

# 1. Physical dynamics

## Controlled stochastic dynamics

\[
\boxed{
dX_t
=
f(X_t,u_t)\,dt
+G(X_t,u_t)\,dW_t.
}
\]

| Field | Role |
| --- | --- |
| object | stochastic physical trajectory |
| status | standard modeling form |
| measurement interface | time-resolved physical, physiological, neural, or sensor state variables |
| bridge status | physical substrate model only |
| source lineage | stochastic differential equations; nonequilibrium dynamics |

A discrete alternative is

\[
\boxed{
X_{t+\Delta t}
\sim
K_{\Delta t}(\cdot\mid X_t,u_t).
}
\]

The repository does not assume one universal microscopic dynamical law. The state variables and intervention semantics must be declared for each application.

---

# 2. Information theory

## Shannon entropy

\[
\boxed{
H(X)
=
-\sum_x p(x)\log p(x).
}
\]

**Primary source:** Claude E. Shannon, *A Mathematical Theory of Communication* (1948).

**Physical meaning:** uncertainty of a probability law under a chosen logarithmic unit.

**Consciousness-science role:** basic information-theoretic quantity used by many models; not a consciousness variable by itself.

## Mutual information

\[
\boxed{
I(X;Y)
=
D_{\mathrm{KL}}
\left(P_{XY}\Vert P_XP_Y\right).
}
\]

**Primary sources:** Shannon 1948; Cover and Thomas 2006.

**Physical meaning:** statistical dependence between measured variables.

**Important distinction:** mutual information is symmetric and does not identify causal direction without additional assumptions or interventions.

---

# 3. Information geometry

For a smooth family of probability laws \(p(x\mid\theta)\), define the Fisher information metric

\[
\boxed{
g_{ij}(\theta)
=
\mathbb E_\theta
\left[
\partial_i\log p(X\mid\theta)
\partial_j\log p(X\mid\theta)
\right].
}
\]

The associated local line element is

\[
\boxed{
ds^2
=
g_{ij}(\theta)d\theta^i d\theta^j.
}
\]

**Primary sources:** Shun-ichi Amari 2016; Ay, Jost, Le, and Schwachhofer 2017.

**Physical meaning:** local statistical distinguishability in a parameterized family of probability laws.

**Repository frontier:** investigate whether families of intervention-conditioned response laws form useful representation-independent statistical manifolds beyond total-variation geometry.

**Bridge status:** no experiential metric is inferred from the Fisher metric without an additional bridge principle.

---

# 4. Causal intervention

The repository's causal-response layer begins from

\[
\boxed{
P_p^{u,\tau}
=
\mathcal L
\left(
Y_{t+\tau}^{V}
\mid do(u),p
\right).
}
\]

**Primary causal lineage:** Judea Pearl 2009; Peters, Bauer, and Pfister 2020 for dynamical causal models.

**Physical meaning:** probability law of a declared response after controlled intervention \(u\), at physical delay \(\tau\).

**Measurement interface:** controlled stimulation, perturbation, intervention, or experimentally justified natural intervention.

The response distance used in Proposition 11 is

\[
\boxed{
d_p^\tau(u,v)
=
\left\|
P_p^{u,\tau}
-P_p^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

This is a repository construction built from standard total variation.

---

# 5. Partition irreducibility

For partition \(\pi\), define the factorized response law

\[
P_{p,\pi}^{u,\tau}
=
\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}.
\]

The repository defines

\[
\boxed{
\kappa_p^\tau(\pi)
=
\sup_u
\left\|
P_p^{u,\tau}
-P_{p,\pi}^{u,\tau}
\right\|_{\mathrm{TV}}.
}
\]

| Field | Role |
| --- | --- |
| status | repository definition, P11 |
| physical meaning | response-level departure from factorization across a declared partition |
| zero case | exact factorization of the declared response laws for all interventions |
| empirical motivation | integrated causal structure, perturbational complexity, synergy/integration literature |
| bridge status | candidate physical structure only |

The exact P11 certificate is

\[
\boxed{
\kappa_p^\tau(\pi)=0
\iff
P_p^{u,\tau}
=
\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}
\quad\forall u.
}
\]

---

# 6. Directed interventional influence

For source-pair family \(\mathcal E_i\),

\[
\boxed{
A_{ij}^{p}(\tau)
=
\sup_{(u,v)\in\mathcal E_i}
\left\|
P_{p,j}^{u,\tau}
-P_{p,j}^{v,\tau}
\right\|_{\mathrm{TV}}.
}
\]

**Status:** repository definition, P11.

**Physical meaning:** maximal change in a target-block response generated by a declared source-local intervention contrast.

**Empirical motivation:** recurrent-processing, global-workspace, perturbational, and dynamical-control literatures.

**Important boundary:** marginal directed influence may miss changes confined to joint dependence structure; Proposition 12 gives an explicit collision example.

---

# 7. Temporal geometry

For finite causal-structure fingerprint \(c=(g,a,k)\),

\[
\boxed{
D_w(c,c')
=
\max
\left\{
w_G\|g-g'\|_\infty,
\;w_A\|a-a'\|_\infty,
\;w_K\|k-k'\|_\infty
\right\}.
}
\]

After quotienting a declared finite relabeling group \(\mathcal H\),

\[
\boxed{
\overline D_w([c],[c'])
=
\min_{h\in\mathcal H}D_w(c,hc').
}
\]

**Status:** repository construction/proof, P14.

**Physical meaning:** representation-invariant distance between two declared causal-structure fingerprints.

Path variation is

\[
\boxed{
V_{0:T}
=
\sum_{t=0}^{T-1}
\overline D_w([c_t],[c_{t+1}]).
}
\]

This is a physical temporal-organization measure, not an experiential continuity variable by definition.

---

# 8. Finite-data temporal uncertainty

If

\[
D_w(c_t,\widehat c_t)
\le
\varepsilon_t,
\]

then P15 proves

\[
\boxed{
|\widehat d_{st}-d_{st}|
\le
\varepsilon_s+arepsilon_t.
}
\]

**Status:** repository theorem, P15.

**Scientific role:** prevents uncertainty in estimated physical structure from being hidden behind a binary state label.

---

# 9. Independent composition and coupling

Independent response-level composition is

\[
\boxed{
P_{A\otimes B}^{(u_A,u_B),\tau}
=
P_A^{u_A,\tau}
\otimes
P_B^{u_B,\tau}.
}
\]

P16 proves

\[
\boxed{
\max\{d_A,d_B\}
\le d_{AB}
\le d_A+d_B-d_Ad_B.
}
\]

Under the independent null model,

\[
A_{ij}^{A\otimes B}(\tau)=0
\quad(i\in A,j\in B),
\]

and

\[
\boxed{
\kappa_{A\otimes B}^{\tau}(\pi_{A|B})=0.
}
\]

The coupling defect is

\[
\boxed{
\chi_{A|B}(\tau)
=
\kappa_{AB}^{\tau}(\pi_{A|B}).
}
\]

**Physical meaning:** departure of the observed response law from factorization across a declared subsystem split.

**Bridge status:** coupling is a physical structural property; experiential unity requires a separate argument.

---

# 10. Coarse-graining and physical scale

For deterministic coarse-graining

\[
C:\Omega_f\to\Omega_c,
\]

define pushforward

\[
\boxed{
C_\#P(y)
=
\sum_{x:C(x)=y}P(x).
}
\]

P17 proves total-variation contraction:

\[
\boxed{
\|C_\#P-C_\#Q\|_{\mathrm{TV}}
\le
\|P-Q\|_{\mathrm{TV}}.
}
\]

If \(C\) is many-to-one, exact collision witnesses exist:

\[
x\ne x',
\qquad C(x)=C(x'),
\]

\[
\|\delta_x-\delta_{x'}\|_{\mathrm{TV}}=1,
\qquad
\boxed{
\|C_\#\delta_x-C_\#\delta_{x'}\|_{\mathrm{TV}}=0.
}
\]

**Physical meaning:** coarse descriptions can erase distinctions present at finer scales.

**Bridge consequence:** a physical-to-experiential theory must declare what scale or equivalence class is relevant and how its claims behave under scale change.

---

# 11. Thermodynamics of information

## Landauer bound

\[
\boxed{
W_{\mathrm{erase}}
\ge
k_B T\ln 2.
}
\]

**Primary source:** Landauer 1961.

**Status:** thermodynamic lower bound for logically irreversible erasure under the standard idealized assumptions.

**Repository role:** physical embodiment of information processing and a future constraint on candidate dynamical processes.

**Bridge status:** not a consciousness threshold.

## Stochastic thermodynamics

A standard entropy-production decomposition is represented schematically as

\[
\boxed{
\Delta s_{\mathrm{tot}}
=
\Delta s_{\mathrm{sys}}
+
\Delta s_{\mathrm{med}}.
}
\]

with nonnegative mean total entropy production under the appropriate nonequilibrium framework:

\[
\boxed{
\langle\Delta s_{\mathrm{tot}}\rangle
\ge 0.
}
\]

**Primary source:** Seifert 2012.

**Repository frontier:** connect measurable intervention-response structure to energetic fluxes and entropy production without assuming that energetic cost itself determines experience.

---

# 12. Variational free energy

A common variational form is

\[
\boxed{
F[q]
=
\mathbb E_q
\left[
\log q(z)-\log p(y,z)
\right].
}
\]

**Primary source context:** Friston 2010 and the broader variational-inference literature.

**Physical/biological role:** formalizes a bound on model evidence and supports predictive-processing / active-inference frameworks.

**Bridge status:** free-energy minimization is not used here as an identity with consciousness.

---

# 13. Empirical consciousness interfaces

| Empirical interface | Physical quantity | Representative source | Repository use |
| --- | --- | --- | --- |
| TMS-EEG perturbation | distributed response complexity | Casali et al. 2013 | motivates perturbation-response analysis |
| spontaneous EEG criticality | dynamical regime / susceptibility | Maschke et al. 2024 | motivates temporal/dynamical robustness tests |
| integrated information decomposition | synergy / redundancy / integration | Luppi et al. 2024 | motivates multicomponent information structure |
| anesthesia across mammalian brains | integration and dynamical control | Luppi et al. 2026 | motivates cross-state and cross-species tests |
| adversarial IIT/GNWT comparison | theory-specific observable predictions | Cogitate Consortium et al. 2025 | motivates P2-P4 discrimination program |

The evidence supports or challenges particular empirical relations. It does not automatically validate the repository's bridge target.

---

# 14. Spaceflight and extreme-environment application layer

NASA sources are included as an **application / robustness-testing domain**.

Relevant stressors include

\[
\boxed{
\text{altered gravity}
+
\text{radiation}
+
\text{sleep/circadian disruption}
+
\text{isolation}
+
\text{workload}.
}
\]

| Source | Scientific role in this repository |
| --- | --- |
| NASA Human Research Program | umbrella human-performance and health research context |
| NASA Human Factors and Behavioral Performance | cognition, sleep, team performance, behavioral health, human-system interaction |
| NASA HFBP risk portfolio | operational and behavioral risk framework |
| NASA sleep/circadian/workload risk | evidence synthesis on performance effects of sleep loss and circadian disruption |
| NASA ARCHeR | longitudinal Artemis crew-health and behavioral-performance data context |

No NASA source is used as evidence for a consciousness bridge. The relevance is that extreme operational environments provide demanding conditions under which candidate physical and cognitive markers can be stress-tested.

---

# 15. Provenance hierarchy

The repository uses the following hierarchy whenever an equation appears:

| Level | Question |
| --- | --- |
| **standard mathematics / physics** | Is this an established identity, bound, or modeling framework? |
| **repository definition** | Is the mathematical object introduced here? |
| **repository theorem** | What follows rigorously from the declared assumptions? |
| **measurement model** | How is the mathematical object estimated from data? |
| **empirical evidence** | What observations support the physical interpretation? |
| **bridge premise** | What additional statement connects physical and experiential structure? |
| **bridge conclusion** | What experiential property follows if the bridge premise is supported? |

The final research goal requires these layers to connect explicitly. None is allowed to substitute silently for another.
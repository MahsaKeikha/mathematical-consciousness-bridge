# Equation and Citation Map

This page distinguishes repository definitions, standard mathematics, physical modeling assumptions, candidate physical hypotheses, bridge hypotheses, theorem statements, theory-family translations, and external empirical evidence.

The purpose is provenance: a reader should be able to see immediately whether an equation is introduced here, inherited from standard mathematics, adapted from an external theory, or motivated by experiment.

---

# 1. Physical and bridge objects

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(p=(\mathcal X,\mathcal D,\mathfrak I,\mathcal O)\) | physical-system object | repository definition | physical modeling framework |
| \(dX_t=f(X_t,u_t)dt+G(X_t,u_t)dW_t\) | example stochastic physical model | standard modeling form | stochastic dynamics |
| \(K_{\Delta t}(\cdot\mid X_t,u_t)\) | transition-kernel representation | standard probability object | Markov/stochastic modeling |
| \(\mathcal B\subseteq\mathcal P\times\mathcal E\) | general physical-to-experiential bridge relation | repository definition | bridge formulation |
| \(p\sim_Pp'\) | physically irrelevant representation equivalence | repository definition, theory dependent | quotient framework |
| \(e\sim_Ee'\) | experiential equivalence | repository definition, open formalization | mathematical-consciousness context |
| \(\mathcal Q_P=\mathcal P/{\sim_P}\) | physical quotient | repository construction using standard quotient mathematics | P1 |
| \(\mathcal Q_E=\mathcal E/{\sim_E}\) | experiential quotient | repository construction using standard quotient mathematics | P1 |
| \(\bar B:\mathcal Q_P\to\mathcal Q_E\) | quotient-level bridge | repository construction | P1 |
| \(B=\bar B\circ\pi_P\) | bridge factorization through physical quotient | proved | P1 + standard quotient logic |

---

# 2. P1-P4 - representation, identifiability, and theory comparison

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(p\sim_Pp'\Rightarrow B(p)=B(p')\) | representation-invariance criterion | proved equivalent to quotient factorization | P1 |
| \(P_i^{\pi,q}\) | observable law predicted by complete bridge theory \(i\) | repository notation | P2 |
| \(\|P-Q\|_{\mathrm{TV}}\) | probability distance controlling binary distinguishability | standard probability/statistics | Le Cam-Yang; Tsybakov |
| \(\Delta_\Pi=\sup_{\pi\in\Pi}\|P_1^{\pi,q}-P_2^{\pi,q}\|_{\mathrm{TV}}\) | experiment-class bridge discriminability | repository construction | P2 |
| \(R_\pi^*=\tfrac12(1-\|P_1-P_2\|_{\mathrm{TV}})\) | optimal equal-prior binary testing error | standard identity applied here | decision theory; P2 |
| \(\exp(-n\eta^2/2)\) | repeated-event discrimination error bound | standard concentration applied here | Hoeffding 1963; P2 |
| \(\Phi_{\Pi,q}(\mathfrak T)=(P_{\mathfrak T}^{\pi,q})_{\pi\in\Pi}\) | complete observable theory fingerprint | repository construction | P3 |
| \(\Theta/{\sim_{\Pi,q}}\cong\operatorname{Im}(\Phi_{\Pi,q})\) | observational theory quotient | proved | P3 + quotient logic |
| \(d_{ij}(\pi)=\|P_i^{\pi,q}-P_j^{\pi,q}\|_{\mathrm{TV}}\) | protocol-specific theory-pair separation | repository construction | P4 |
| \(U(S)=\min_{\{i,j\}\in\mathcal U}\max_{\pi\in S}d_{ij}(\pi)\) | worst-pair protocol-family separation | repository construction | P4 |
| \(U(S)>0\iff\bigcup_{\pi\in S}C_\pi=\mathcal U\) | complete-discrimination / set-cover equivalence | proved | P4 |

---

# 3. P5-P6 - physical-feature sufficiency and bridge completeness

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(F:\mathcal Q_P\to\mathcal Z\) | proposed representation-invariant physical feature | generic repository notation | P5 |
| \(\bar B=g\circ F\) | bridge factorization through physical feature | definition of sufficiency | P5 |
| \(F(p)=F(p')\Rightarrow\bar B(p)=\bar B(p')\) | fiber-constancy criterion | proved equivalent to factorization | P5 |
| \(p\sim_Bp'\iff\bar B(p)=\bar B(p')\) | bridge-induced physical equivalence | repository definition | P6 |
| \(\mathcal Q_B=\mathcal Q_P/{\sim_B}\) | canonical bridge quotient | repository construction | P6 |
| \(C_B(p)=[p]_{\sim_B}\) | canonical complete bridge signature | repository construction | P6 |
| \(C_B(p)=C_B(p')\iff\bar B(p)=\bar B(p')\) | exact canonical completeness | proved | P6 |
| \(\mathcal Q_B\cong\operatorname{Im}(\bar B)\) | quotient / bridge-image equivalence | proved | P6 |
| \(F_*(p)=F_*(p')\iff\bar B(p)=\bar B(p')\) | complete physical-signature target | repository theorem target | P6 / Universal Proof Target |

---

# 4. P7-P10 - recoverability, finite data, and experiment design

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(\Psi_\Pi(p)=(P^{\pi,p})_{\pi\in\Pi}\) | complete experimental fingerprint of a physical realization | repository construction | P7 |
| \(\Psi_\Pi(p)=\Psi_\Pi(p')\Rightarrow F_*(p)=F_*(p')\) | exact recoverability criterion | proved | P7 |
| \(d_S(p,p')=\max_{\pi\in S}\|P^{\pi,p}-P^{\pi,p'}\|_{\mathrm{TV}}\) | protocol-family physical distance | repository construction | P8 |
| \(\omega_S\) | maximum within-signature spread | repository definition | P8 |
| \(\delta_S\) | minimum between-signature separation | repository definition | P8 |
| \(\gamma_S=\delta_S-\omega_S\) | robust signature gap | repository construction | P8 |
| \(|\widehat d_S-d_S|\le2\varepsilon\) | distance perturbation bound | proved from TV triangle inequality | P8 |
| \(\gamma_S>4\varepsilon\) | sufficient exact-partition recovery condition | proved | P8 |
| \(\Pr(|\widehat p_j-p_j|>a)\le2e^{-2na^2}\) | one-category empirical-frequency concentration | standard inequality | Hoeffding 1963 |
| \(2N_PN_\pi K\exp(-8n\varepsilon^2/K^2)\) | uniform categorical failure bound | proved from Hoeffding + union bounds | P9 |
| \(n\ge\frac{8K^2}{\gamma_S^2}\log\frac{2N_PN_\pi K}{\alpha}\) | sufficient per-cell trials for exact signature recovery | proved | P9 |
| \(\Gamma(S)=\delta(S)-\omega(S)\) | robust protocol-family design objective | repository construction | P10 |
| \(\Gamma(S\cup\{\rho\})-\Gamma(S)=a_\rho(S)-b_\rho(S)\) | exact marginal protocol-value identity | proved | P10 |
| \(\Gamma(S\cup\{\rho\})>\Gamma(S)\iff a_\rho(S)>b_\rho(S)\) | added-protocol improvement criterion | proved | P10 |

---

# 5. P11 - Intervention-Resolved Causal Geometry

IRCG is a repository-original **candidate physical signature**. The following equations are definitions or theorems about that physical object; they are not imported as a consciousness identity from any external theory.

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(P_p^{u,\tau}=\mathcal L(Y_{t+\tau}^V\mid do(u),p)\) | intervention-conditioned joint response law | repository definition using standard intervention semantics | P11; Pearl for \(do\)-notation context |
| \(d_p^\tau(u,v)=\|P_p^{u,\tau}-P_p^{v,\tau}\|_{\mathrm{TV}}\) | intervention-response pseudometric | repository construction | P11 + standard TV distance |
| \(\mathcal G_p=\{d_p^\tau:\tau\in\mathcal T\}\) | response-geometry family | repository definition | P11 |
| \(A_{ij}^{p}(\tau)=\sup_{(u,v)\in\mathcal E_i}\|P_{p,j}^{u,\tau}-P_{p,j}^{v,\tau}\|_{\mathrm{TV}}\) | directed perturbational influence | repository construction | P11 |
| \(\mathcal A_p=\{A_{ij}^{p}(\tau)\}_{i,j,\tau}\) | directed influence tensor | repository definition | P11 |
| \(P_{p,\pi}^{u,\tau}=\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}\) | productized partition response | standard product measure applied here | P11 |
| \(\kappa_p^\tau(\pi)=\sup_u\|P_p^{u,\tau}-P_{p,\pi}^{u,\tau}\|_{\mathrm{TV}}\) | partition response irreducibility | repository construction | P11 |
| \(\mathcal K_p=\{\kappa_p^\tau(\pi)\}_{\pi,\tau}\) | complete partition landscape | repository definition | P11 |
| \(\mathfrak C_p=(V,\mathcal U_p,\mathcal T,\mathcal G_p,\mathcal A_p,\mathcal K_p)\) | raw IRCG object | repository definition | P11 |
| \(F_{\mathrm{IRCG}}(p)=[\mathfrak C_p]_{\cong}\) | representation-invariant IRCG signature | repository construction | P11 |
| \(\kappa_p^\tau(\pi)=0\iff P_p^{u,\tau}=\bigotimes_{B\in\pi}P_{p,B}^{u,\tau}\ \forall u\) | exact factorization certificate | proved | P11 |
| DAG influence graph \(\Rightarrow\) no directed return loop | feedforward no-return certificate | proved | P11 + graph-theoretic definition |

## P11 empirical motivation map

| Physical idea motivating measurement | External evidence / theory role | Citation |
| --- | --- | --- |
| direct perturbation + differentiated distributed response | perturbational-complexity evidence | Casali et al. 2013; Maschke et al. 2024 |
| intrinsic causal organization / irreducibility | existing bridge theory motivation | Albantakis et al. 2023 |
| recurrent and distributed processing | theory-family motivation | Mashour et al. 2020; Lamme 2006; Changeux-Farisco 2026 |
| synergistic integration changing with consciousness | empirical information-integration evidence | Luppi et al. 2024 |
| integration and controllability under anesthesia | cross-species empirical evidence | Luppi et al. 2026 |

These sources motivate what is worth measuring. They do not establish the IRCG bridge-completeness target.

---

# 6. P12 - component minimality and projection collisions

| Equation or object | Role | Status | Primary provenance |
| --- | --- | --- | --- |
| \(H(x)=H(x')\) but \(F(x)\ne F(x')\) | projection collision | repository definition of collision witness | P12 |
| collision \(\Rightarrow\nexists g:F=g\circ H\) | compression non-reconstructibility theorem | proved | P12 + P5 factorization logic |
| \(\mathcal G_C=\mathcal G_P\) but \(\kappa_C\ne\kappa_P\) | response-geometry collision | explicit realizable construction | P12 |
| \(\mathcal K_D=\mathcal K_S\) but \(\mathcal G_D\ne\mathcal G_S\) | partition-landscape collision | explicit realizable construction | P12 |
| \(\mathcal A_R=\mathcal A_I\) but \(\mathcal G_R\ne\mathcal G_I\) | directed-influence collision | explicit realizable construction | P12 |
| \(\operatorname{Diam}_p(\tau)\) | scalar response-diameter compression | proved incomplete on explicit domain | P12 |
| \(\kappa_p^*\) | minimum irreducibility scalar | proved incomplete on explicit domain | P12 |
| cycle/no-cycle indicator | Boolean recurrence compression | proved incomplete for influence strength | P12 |

P12 is a **physical-signature minimality theorem**, not an experiential theorem. It demonstrates why a simple scalar or one-component summary cannot be assumed to preserve the physical information retained by IRCG.

---

# 7. Candidate consciousness-theory feature families

The following are source-grounded translations into the generic feature notation. They are not claims that each named theory reduces to one scalar or one universally agreed implementation.

| Theory family | Generic feature notation in this repository | Primary source role |
| --- | --- | --- |
| IIT 4.0 | \(\mathcal F_{\mathrm{IIT}}(p)=\) intrinsic cause-effect structure and maximal-substrate organization | Albantakis et al. 2023 |
| GNWT | \(\mathcal F_{\mathrm{GNW}}(p)=\) multilevel workspace organization, ignition, and global availability | Dehaene-Changeux 2011; Mashour et al. 2020; Changeux-Farisco 2026 |
| RPT | \(\mathcal F_{\mathrm{RPT}}(p)=\) relevant recurrent-processing structure and dynamics | Lamme 2006 |
| HOT | \(\mathcal F_{\mathrm{HOT}}(p)=\) theory-specific higher-order representational relation | Brown-Lau-LeDoux 2019 |
| predictive / NR / active-inference families | \(\mathcal F_{\mathrm{PP}}(p)=\) theory-specific predictive, inferential, and representational structure | Seth-Hohwy 2021; Pennartz 2022; Corcoran et al. 2026 |
| IRCG | \(F_{\mathrm{IRCG}}(p)=[\mathfrak C_p]_{\cong}\) | repository-original candidate physical signature | P11-P12 |

Detailed caveats and source roles are maintained in [Candidate Theory Families](candidate_theory_families.md) and [Literature Map](literature_map.md).

---

# 8. Citation discipline

A result is cited as a repository result when the bridge-specific statement, construction, or counterexample is introduced here.

External literature is cited only for the conceptual, mathematical, statistical, physical, or empirical role it supplies.

The project maintains the distinction

\[
\boxed{
\text{definition}
\neq
\text{bridge axiom}
\neq
\text{candidate physical signature}
\neq
\text{theorem}
\neq
\text{empirical evidence}.
}
\]

This distinction is central to the final proof target: mathematics establishes what follows from premises, while the physical-to-experiential premises themselves require independently discriminating evidence.
from pathlib import Path
import json

import matplotlib.pyplot as plt
import numpy as np

plt.switch_backend("Agg")

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "figures" / "quantum"
OUT.mkdir(parents=True, exist_ok=True)
for path in OUT.glob("qm*.svg"):
    path.unlink()

plt.rcParams.update(
    {
        "figure.figsize": (7.6, 4.7),
        "figure.dpi": 120,
        "font.size": 9.5,
        "axes.titlesize": 13,
        "axes.labelsize": 9.5,
        "axes.grid": True,
        "grid.alpha": 0.22,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "svg.fonttype": "none",
    }
)

META = []


def finish(fig, filename, title, equation, fact, status):
    fig.tight_layout()
    fig.savefig(OUT / filename, format="svg", bbox_inches="tight")
    plt.close(fig)
    META.append(
        {
            "file": filename,
            "title": title,
            "equation": equation,
            "fact": fact,
            "status": status,
        }
    )


# QM01 — Free Gaussian wavepacket spreading
hbar = 1.0
mass = 1.0
sigma0 = 0.65
x = np.linspace(-8.0, 8.0, 600)
times = np.linspace(0.0, 8.0, 240)
density = np.empty((len(times), len(x)))
for i, time in enumerate(times):
    sigma_t = sigma0 * np.sqrt(
        1.0 + (hbar * time / (2.0 * mass * sigma0**2)) ** 2
    )
    density[i] = np.exp(-x**2 / (2.0 * sigma_t**2)) / (
        np.sqrt(2.0 * np.pi) * sigma_t
    )
fig, ax = plt.subplots()
image = ax.imshow(
    density,
    origin="lower",
    aspect="auto",
    extent=[x.min(), x.max(), times.min(), times.max()],
)
fig.colorbar(image, ax=ax, label="probability density")
ax.set(
    title="QM01 · Free Gaussian wavepacket spreading",
    xlabel="position x",
    ylabel="time t",
)
finish(
    fig,
    "qm01_free_gaussian_wavepacket.svg",
    "Free Gaussian wavepacket spreading",
    "i hbar d_t psi = -(hbar^2/2m) d_x^2 psi",
    "A minimum-uncertainty free Gaussian broadens because different momentum components acquire different phases.",
    "Exact free-particle Gaussian solution in dimensionless units",
)

# QM02 — Infinite square-well eigenstates
well_x = np.linspace(0.0, 1.0, 700)
fig, ax = plt.subplots()
for n in (1, 2, 3, 4):
    energy = n**2
    psi = np.sqrt(2.0) * np.sin(n * np.pi * well_x)
    ax.plot(well_x, energy + 0.7 * psi, lw=1.8, label=f"n={n}")
    ax.axhline(energy, lw=0.7, alpha=0.5)
ax.set(
    title="QM02 · Quantized stationary states in a one-dimensional box",
    xlabel="x / L",
    ylabel="energy offset + scaled eigenfunction",
)
ax.legend()
finish(
    fig,
    "qm02_infinite_well_eigenstates.svg",
    "Infinite square-well eigenstates",
    "E_n = n^2 pi^2 hbar^2/(2mL^2), psi_n=sqrt(2/L) sin(n pi x/L)",
    "Boundary conditions discretize the allowed stationary energies and eigenmodes.",
    "Standard quantum-mechanical eigenvalue problem",
)

# QM03 — Double-slit interference
angle = np.linspace(-0.12, 0.12, 900)
wavelength = 1.0
slit_width = 4.0
slit_separation = 20.0
beta = np.pi * slit_width * np.sin(angle) / wavelength
alpha = np.pi * slit_separation * np.sin(angle) / wavelength
envelope = np.sinc(beta / np.pi) ** 2
intensity = envelope * np.cos(alpha) ** 2
fig, ax = plt.subplots()
ax.plot(angle, intensity, lw=2.0)
ax.plot(angle, envelope, ls="--", lw=1.1, label="single-slit envelope")
ax.set(
    title="QM03 · Double-slit interference inside a diffraction envelope",
    xlabel="observation angle (radians)",
    ylabel="normalized intensity",
)
ax.legend()
finish(
    fig,
    "qm03_double_slit_interference.svg",
    "Double-slit interference",
    "I(theta) proportional sinc^2(beta) cos^2(alpha)",
    "Amplitude superposition produces interference fringes whose visibility is constrained by the single-slit envelope.",
    "Standard wave-mechanical interference law",
)

# QM04 — Heisenberg uncertainty frontier
sigma_x = np.linspace(0.12, 4.0, 700)
minimum_sigma_p = hbar / (2.0 * sigma_x)
fig, ax = plt.subplots()
ax.plot(sigma_x, minimum_sigma_p, lw=2.4, label="Heisenberg boundary")
ax.fill_between(
    sigma_x,
    minimum_sigma_p,
    np.full_like(sigma_x, 4.5),
    alpha=0.10,
    label="allowed region",
)
for squeeze in (0.35, 0.65, 1.0, 1.6, 2.8):
    ax.scatter([squeeze], [hbar / (2.0 * squeeze)], s=34)
ax.set(
    xlim=(0.0, 4.0),
    ylim=(0.0, 4.5),
    title="QM04 · Heisenberg position-momentum uncertainty frontier",
    xlabel="Delta x",
    ylabel="Delta p",
)
ax.legend()
finish(
    fig,
    "qm04_uncertainty_frontier.svg",
    "Heisenberg uncertainty frontier",
    "Delta x Delta p >= hbar/2",
    "Gaussian minimum-uncertainty states saturate the boundary while squeezing trades position variance against momentum variance.",
    "Standard quantum-mechanical uncertainty relation",
)

# QM05 — Bloch sphere
fig = plt.figure(figsize=(8.0, 7.2))
ax = fig.add_subplot(111, projection="3d")
u = np.linspace(0.0, 2.0 * np.pi, 45)
v = np.linspace(0.0, np.pi, 24)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones_like(u), np.cos(v))
ax.plot_wireframe(xs, ys, zs, rstride=3, cstride=3, linewidth=0.4, alpha=0.32)
for theta, phi in ((0.7, 0.4), (1.45, 2.1), (2.35, 4.8)):
    vector = np.array(
        [
            np.sin(theta) * np.cos(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(theta),
        ]
    )
    ax.quiver(0, 0, 0, *vector, length=1.0, normalize=True, linewidth=1.8)
ax.set(
    title="QM05 · Pure qubit states as points on the Bloch sphere",
    xlabel="<sigma_x>",
    ylabel="<sigma_y>",
    zlabel="<sigma_z>",
    xlim=(-1.05, 1.05),
    ylim=(-1.05, 1.05),
    zlim=(-1.05, 1.05),
)
finish(
    fig,
    "qm05_bloch_sphere.svg",
    "Bloch-sphere state geometry",
    "rho = (I + r dot sigma)/2; pure states satisfy |r|=1",
    "A qubit density matrix maps to a Bloch vector; pure states lie on the unit sphere and mixed states lie inside it.",
    "Standard finite-dimensional quantum-state geometry",
)

# QM06 — Born probability
polar_angle = np.linspace(0.0, np.pi, 500)
p_zero = np.cos(polar_angle / 2.0) ** 2
p_one = np.sin(polar_angle / 2.0) ** 2
fig, ax = plt.subplots()
ax.plot(polar_angle, p_zero, lw=2.3, label="P(0)")
ax.plot(polar_angle, p_one, lw=2.3, label="P(1)")
ax.set(
    title="QM06 · Born probabilities for a rotated qubit",
    xlabel="polar angle theta",
    ylabel="measurement probability",
)
ax.legend()
finish(
    fig,
    "qm06_born_probabilities.svg",
    "Born probabilities",
    "P(0)=cos^2(theta/2), P(1)=sin^2(theta/2)",
    "Measurement probabilities are squared projection amplitudes and sum to one for a complete projective measurement.",
    "Standard Born rule for a pure qubit",
)

# QM07 — Rabi oscillations
rabi_time = np.linspace(0.0, 8.0 * np.pi, 700)
p_excited = np.sin(rabi_time / 2.0) ** 2
fig, ax = plt.subplots()
ax.plot(rabi_time, p_excited, lw=2.2)
ax.set(
    title="QM07 · Coherent Rabi population oscillations",
    xlabel="dimensionless time Omega t",
    ylabel="excited-state probability",
)
finish(
    fig,
    "qm07_rabi_oscillations.svg",
    "Rabi oscillations",
    "P_e(t)=sin^2(Omega t/2)",
    "A resonantly driven two-level system exchanges population coherently between basis states.",
    "Standard two-level coherent dynamics",
)

# QM08 — Pure dephasing coherence decay
gamma = 0.45
dephase_time = np.linspace(0.0, 12.0, 600)
coherence = 0.5 * np.exp(-gamma * dephase_time)
fig, ax = plt.subplots()
ax.plot(dephase_time, coherence, lw=2.2)
ax.set(
    title="QM08 · Off-diagonal coherence under Markovian pure dephasing",
    xlabel="time",
    ylabel="|rho_01(t)|",
)
finish(
    fig,
    "qm08_dephasing_coherence.svg",
    "Pure-dephasing coherence decay",
    "|rho_01(t)|=|rho_01(0)| exp(-Gamma t)",
    "Pure dephasing suppresses off-diagonal density-matrix coherence while leaving basis populations unchanged.",
    "Lindblad pure-dephasing model",
)

# QM09 — Purity under dephasing
purity = 0.5 * (1.0 + np.exp(-2.0 * gamma * dephase_time))
fig, ax = plt.subplots()
ax.plot(dephase_time, purity, lw=2.2)
ax.axhline(0.5, ls="--", lw=1.0, label="maximally mixed qubit")
ax.set(
    title="QM09 · Purity loss for an initially coherent qubit",
    xlabel="time",
    ylabel="Tr(rho^2)",
)
ax.legend()
finish(
    fig,
    "qm09_purity_under_dephasing.svg",
    "Purity under dephasing",
    "Tr(rho^2)=[1+exp(-2 Gamma t)]/2 for initial |+><+|",
    "The initial pure state approaches a basis-dephased mixed state with purity one half.",
    "Closed-form Lindblad dephasing result",
)

# QM10 — von Neumann entropy of a qubit spectrum
probability = np.linspace(1e-5, 1.0 - 1e-5, 700)
entropy = -probability * np.log2(probability) - (
    1.0 - probability
) * np.log2(1.0 - probability)
fig, ax = plt.subplots()
ax.plot(probability, entropy, lw=2.3)
ax.set(
    title="QM10 · Von Neumann entropy of a two-level spectrum",
    xlabel="eigenvalue p",
    ylabel="entropy S(rho) in bits",
)
finish(
    fig,
    "qm10_von_neumann_entropy.svg",
    "Von Neumann entropy",
    "S(rho)=-Tr(rho log2 rho)",
    "For eigenvalues p and 1-p, entropy is zero for a pure state and one bit for a maximally mixed qubit.",
    "Standard quantum-information entropy",
)

# QM11 — Entanglement entropy of a Schmidt pair
schmidt_angle = np.linspace(0.0, np.pi / 2.0, 600)
lam = np.cos(schmidt_angle) ** 2
safe_lam = np.clip(lam, 1e-12, 1.0 - 1e-12)
entanglement_entropy = -safe_lam * np.log2(safe_lam) - (
    1.0 - safe_lam
) * np.log2(1.0 - safe_lam)
fig, ax = plt.subplots()
ax.plot(schmidt_angle, entanglement_entropy, lw=2.3)
ax.set(
    title="QM11 · Entanglement entropy for a two-qubit Schmidt family",
    xlabel="Schmidt angle theta",
    ylabel="subsystem entropy in bits",
)
finish(
    fig,
    "qm11_entanglement_entropy.svg",
    "Two-qubit entanglement entropy",
    "|psi>=cos(theta)|00>+sin(theta)|11>",
    "The reduced-state entropy is zero for product states and reaches one bit at maximal entanglement.",
    "Standard pure-state bipartite entanglement result",
)

# QM12 — Bell-CHSH quantum violation
chsh_angle = np.linspace(0.0, np.pi / 2.0, 700)
chsh_value = np.abs(-3.0 * np.cos(chsh_angle) + np.cos(3.0 * chsh_angle))
fig, ax = plt.subplots()
ax.plot(chsh_angle, chsh_value, lw=2.3, label="singlet-state family")
ax.axhline(2.0, ls="--", lw=1.2, label="local hidden-variable bound")
ax.axhline(2.0 * np.sqrt(2.0), ls=":", lw=1.2, label="Tsirelson bound")
ax.set(
    title="QM12 · CHSH correlation: local bound and quantum maximum",
    xlabel="analyzer angle theta",
    ylabel="|S_CHSH|",
)
ax.legend()
finish(
    fig,
    "qm12_chsh_violation.svg",
    "Bell-CHSH correlation",
    "|S_CHSH|<=2 classically; |S_CHSH|<=2 sqrt(2) quantum mechanically",
    "Entangled quantum correlations can violate the local hidden-variable CHSH bound without permitting superluminal signalling.",
    "Standard Bell-test quantum prediction",
)

# QM13 — Wigner negativity for the first excited oscillator state
phase_x = np.linspace(-3.2, 3.2, 300)
phase_p = np.linspace(-3.2, 3.2, 300)
xx, pp = np.meshgrid(phase_x, phase_p)
r2 = xx**2 + pp**2
wigner_one = (2.0 * r2 - 1.0) * np.exp(-r2) / np.pi
fig, ax = plt.subplots()
levels = np.linspace(wigner_one.min(), wigner_one.max(), 31)
contour = ax.contourf(xx, pp, wigner_one, levels=levels)
fig.colorbar(contour, ax=ax, label="W_1(x,p)")
ax.contour(xx, pp, wigner_one, levels=[0.0], linewidths=1.2)
ax.set(
    title="QM13 · Wigner quasiprobability of the first excited oscillator state",
    xlabel="dimensionless position x",
    ylabel="dimensionless momentum p",
    aspect="equal",
)
finish(
    fig,
    "qm13_wigner_negativity.svg",
    "Wigner-function negativity",
    "W_1(x,p)=(2 r^2-1) exp(-r^2)/pi in the chosen scaling",
    "The first excited harmonic-oscillator state has a negative central Wigner region, a nonclassical quasiprobability feature.",
    "Standard harmonic-oscillator Wigner-function example",
)

# QM14 — Hilbert-space dimension growth
qubits = np.arange(1, 31)
hilbert_dimension = 2.0**qubits
fig, ax = plt.subplots()
ax.semilogy(qubits, hilbert_dimension, lw=2.3)
ax.set(
    title="QM14 · Exponential Hilbert-space dimension for N qubits",
    xlabel="number of qubits N",
    ylabel="Hilbert-space dimension 2^N",
)
finish(
    fig,
    "qm14_hilbert_space_dimension.svg",
    "Hilbert-space dimension scaling",
    "dim[(C^2)^(tensor N)] = 2^N",
    "The state-vector dimension of N qubits grows exponentially with subsystem count.",
    "Standard tensor-product dimension fact",
)

# QM15 — Trace-distance contraction under depolarizing noise
noise = np.linspace(0.0, 1.0, 600)
for initial_distance in (0.25, 0.5, 0.75, 1.0):
    ax_label = f"D_in={initial_distance:.2f}"
    if initial_distance == 0.25:
        fig, ax = plt.subplots()
    ax.plot(noise, (1.0 - noise) * initial_distance, lw=2.0, label=ax_label)
ax.set(
    title="QM15 · Trace-distance contraction under a qubit depolarizing channel",
    xlabel="depolarizing strength p",
    ylabel="output trace distance",
)
ax.legend()
finish(
    fig,
    "qm15_trace_distance_contraction.svg",
    "Quantum distinguishability contraction",
    "Lambda_p(rho)=(1-p)rho+p I/2; D(Lambda rho,Lambda sigma)=(1-p)D(rho,sigma)",
    "Depolarizing noise contracts operational distinguishability, directly paralleling classical data-processing loss under coarse descriptions.",
    "Standard CPTP-channel trace-distance contraction example",
)

# QM16 — Pure-state fidelity and trace distance
state_angle = np.linspace(0.0, np.pi, 600)
fidelity = np.cos(state_angle / 2.0) ** 2
trace_distance = np.sin(state_angle / 2.0)
fig, ax = plt.subplots()
ax.plot(state_angle, fidelity, lw=2.2, label="fidelity")
ax.plot(state_angle, trace_distance, lw=2.2, label="trace distance")
ax.set(
    title="QM16 · Geometry of two pure qubit states",
    xlabel="Bloch-sphere angular separation",
    ylabel="dimensionless similarity / distance",
)
ax.legend()
finish(
    fig,
    "qm16_fidelity_trace_distance.svg",
    "Pure-state fidelity and trace distance",
    "F=cos^2(theta/2), D=sqrt(1-F)=sin(theta/2)",
    "Pure states become less faithful and more distinguishable as their projective angle increases.",
    "Standard pure-state quantum-information identity",
)

# QM17 — Quantum Zeno survival
zeno_time = np.linspace(0.0, np.pi, 500)
fig, ax = plt.subplots()
for measurements in (1, 2, 5, 20, 100):
    survival = np.cos(zeno_time / (2.0 * measurements)) ** (2 * measurements)
    ax.plot(zeno_time, survival, lw=1.8, label=f"N={measurements}")
ax.set(
    title="QM17 · Idealized quantum-Zeno survival under repeated projection",
    xlabel="dimensionless total evolution angle",
    ylabel="survival probability",
)
ax.legend()
finish(
    fig,
    "qm17_quantum_zeno_survival.svg",
    "Quantum Zeno effect",
    "P_N(t)=cos^(2N)(Omega t/(2N))",
    "In the ideal projective limit, increasingly frequent survival measurements suppress coherent transition away from the initial state.",
    "Idealized repeated-projective-measurement result",
)

# QM18 — Reduced-state spectrum of an entangled pair
reduced_lambda_one = np.cos(schmidt_angle) ** 2
reduced_lambda_two = np.sin(schmidt_angle) ** 2
fig, ax = plt.subplots()
ax.plot(schmidt_angle, reduced_lambda_one, lw=2.2, label="lambda_1")
ax.plot(schmidt_angle, reduced_lambda_two, lw=2.2, label="lambda_2")
ax.set(
    title="QM18 · Reduced density-matrix spectrum of an entangled pair",
    xlabel="Schmidt angle theta",
    ylabel="reduced-state eigenvalue",
)
ax.legend()
finish(
    fig,
    "qm18_reduced_density_spectrum.svg",
    "Reduced-state spectrum under partial trace",
    "rho_A=Tr_B |psi><psi| has eigenvalues cos^2(theta), sin^2(theta)",
    "A globally pure entangled state can induce a mixed local reduced state after tracing out its partner.",
    "Standard partial-trace result for a Schmidt pair",
)

manifest = {
    "figure_count": len(META),
    "scope": "quantum foundations and quantum-information mathematics",
    "scientific_boundary": (
        "These figures establish or illustrate standard quantum-mechanical structure. "
        "They do not establish that consciousness is quantum, that consciousness is a "
        "new physical dimension, or that quantum formalism is incomplete."
    ),
    "figures": META,
}
(OUT / "quantum_figure_manifest.json").write_text(
    json.dumps(manifest, indent=2) + "\n",
    encoding="utf-8",
)

print(f"Generated {len(META)} quantum-foundations figures in {OUT}")

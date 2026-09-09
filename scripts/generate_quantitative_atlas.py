from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "figures" / "quantitative"
OUT.mkdir(parents=True, exist_ok=True)
for path in OUT.glob("q*.svg"):
    path.unlink()

plt.rcParams.update(
    {
        "figure.figsize": (5.8, 3.6),
        "figure.dpi": 120,
        "font.size": 8.5,
        "axes.titlesize": 11.5,
        "axes.labelsize": 8.5,
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


# Q01 - Ornstein-Uhlenbeck trajectories
rng = np.random.default_rng(7)
theta, mu, sigma, dt, horizon = 1.4, 0.0, 0.65, 0.005, 8.0
t = np.arange(0, horizon + dt, dt)
fig, ax = plt.subplots()
for _ in range(6):
    state = np.zeros_like(t)
    state[0] = rng.normal()
    dw = rng.normal(0, np.sqrt(dt), len(t) - 1)
    for i in range(len(t) - 1):
        state[i + 1] = (
            state[i]
            + theta * (mu - state[i]) * dt
            + sigma * dw[i]
        )
    ax.plot(t, state, lw=1.2, alpha=0.85)
ax.axhline(mu, ls="--", lw=1)
ax.set(
    title="Q01 · Ornstein-Uhlenbeck mean-reverting trajectories",
    xlabel="time",
    ylabel="state X(t)",
)
finish(
    fig,
    "q01_ornstein_uhlenbeck_trajectories.svg",
    "Ornstein-Uhlenbeck mean-reverting trajectories",
    "dX = theta(mu-X)dt + sigma dW",
    "Linear drift pulls trajectories toward equilibrium while diffusion sustains fluctuations.",
    "Equation-driven stochastic simulation",
)

# Q02 - OU stationary variance
tt = np.linspace(0, 6, 400)
variance = sigma**2 / (2 * theta) * (1 - np.exp(-2 * theta * tt))
stationary_variance = sigma**2 / (2 * theta)
fig, ax = plt.subplots()
ax.plot(tt, variance, lw=2.5, label="transient variance")
ax.axhline(stationary_variance, ls="--", label="stationary variance")
ax.set(
    title="Q02 · OU variance converges to the stationary value",
    xlabel="time",
    ylabel="variance",
)
ax.legend()
finish(
    fig,
    "q02_ou_stationary_variance.svg",
    "OU stationary variance",
    "Var[X(t)] = sigma^2/(2 theta) [1-exp(-2 theta t)]",
    "The variance of a zero-initialized OU process approaches sigma^2/(2 theta) monotonically.",
    "Closed-form mathematical fact",
)

# Q03 - double well
x = np.linspace(-2.2, 2.2, 600)
a, b = 1.0, 2.0
potential = a * x**4 / 4 - b * x**2 / 2
fig, ax = plt.subplots()
ax.plot(x, potential, lw=2.5)
ax.scatter([-1, 1], [a / 4 - b / 2] * 2, s=40)
ax.set(
    title="Q03 · Double-well potential and metastable states",
    xlabel="state x",
    ylabel="potential U(x)",
)
finish(
    fig,
    "q03_double_well_potential.svg",
    "Double-well potential",
    "U(x)=a x^4/4 - b x^2/2",
    "Two minima separated by a barrier form a canonical model of noise-driven switching.",
    "Equation-driven physical illustration",
)

# Q04 - stationary density in the double well
beta = 3.0
density = np.exp(-beta * (potential - potential.min()))
density /= np.trapezoid(density, x)
fig, ax = plt.subplots()
ax.plot(x, density, lw=2.5)
ax.set(
    title="Q04 · Stationary density over a double-well landscape",
    xlabel="state x",
    ylabel="normalized density",
)
finish(
    fig,
    "q04_double_well_stationary_density.svg",
    "Double-well stationary density",
    "p(x) proportional to exp[-beta U(x)]",
    "At fixed inverse temperature, probability mass concentrates near low-potential states.",
    "Equilibrium statistical-mechanics illustration",
)

# Q05 - linear flow map
xx, yy = np.meshgrid(np.linspace(-2.5, 2.5, 20), np.linspace(-2.5, 2.5, 20))
linear_a = np.array([[-0.45, -1.1], [1.0, -0.35]])
u = linear_a[0, 0] * xx + linear_a[0, 1] * yy
v = linear_a[1, 0] * xx + linear_a[1, 1] * yy
speed = np.hypot(u, v)
fig, ax = plt.subplots()
ax.streamplot(
    xx,
    yy,
    u,
    v,
    density=1.1,
    linewidth=0.5 + 1.5 * speed / speed.max(),
    arrowsize=1,
)
ax.scatter([0], [0], s=50, zorder=3)
ax.set(
    title="Q05 · Stable rotational flow in a linear dynamical system",
    xlabel="x1",
    ylabel="x2",
    aspect="equal",
)
finish(
    fig,
    "q05_linear_state_space_flow.svg",
    "Linear state-space flow",
    "dx/dt = A x",
    "Negative eigenvalue real parts produce decay toward the fixed point while off-diagonal terms generate rotation.",
    "Equation-driven dynamical-systems map",
)

# Q06 - eigenvalue stability map
fig, ax = plt.subplots()
ax.axvspan(-2, 0, alpha=0.12, label="stable half-plane")
ax.axvline(0, ls="--", lw=1)
eigenvalues = np.linalg.eigvals(linear_a)
ax.scatter(eigenvalues.real, eigenvalues.imag, s=70, label="Q05 eigenvalues")
ax.set(
    xlim=(-2, 2),
    ylim=(-2, 2),
    title="Q06 · Continuous-time eigenvalue stability map",
    xlabel="Re(lambda)",
    ylabel="Im(lambda)",
)
ax.legend()
finish(
    fig,
    "q06_eigenvalue_stability_map.svg",
    "Continuous-time eigenvalue stability map",
    "Re(lambda_i(A))<0 for all i implies asymptotic stability",
    "All eigenvalues in the open left half-plane imply asymptotic stability for a linear autonomous system.",
    "Standard linear-systems fact",
)

# Q07 - diffusion MSD
diffusion = 0.35
td = np.linspace(0, 10, 300)
fig, ax = plt.subplots()
for dimension in [1, 2, 3]:
    ax.plot(td, 2 * dimension * diffusion * td, lw=2, label=f"{dimension}D")
ax.set(
    title="Q07 · Diffusive mean-square displacement",
    xlabel="time",
    ylabel="mean-square displacement",
)
ax.legend()
finish(
    fig,
    "q07_diffusion_mean_square_displacement.svg",
    "Diffusive mean-square displacement",
    "E||X(t)-X(0)||^2 = 2 d D t",
    "For isotropic Brownian diffusion, mean-square displacement grows linearly with time and dimension.",
    "Standard diffusion fact",
)

# Q08 - heat kernel propagator
grid = np.linspace(-4, 4, 400)
times = np.linspace(0.05, 3, 240)
heat_kernel = np.array(
    [
        (1 / np.sqrt(4 * np.pi * diffusion * ti))
        * np.exp(-grid**2 / (4 * diffusion * ti))
        for ti in times
    ]
)
fig, ax = plt.subplots()
image = ax.imshow(
    heat_kernel,
    aspect="auto",
    origin="lower",
    extent=[grid.min(), grid.max(), times.min(), times.max()],
)
fig.colorbar(image, ax=ax, label="density")
ax.set(
    title="Q08 · Heat-kernel diffusion propagator",
    xlabel="position",
    ylabel="time",
)
finish(
    fig,
    "q08_heat_kernel_propagator.svg",
    "Heat-kernel diffusion propagator",
    "G(x,t)=(4 pi D t)^(-1/2) exp[-x^2/(4Dt)]",
    "The diffusion kernel broadens while its peak decreases, preserving total probability.",
    "Closed-form physical map",
)

# Q09 - Landauer bound
k_b = 1.380649e-23
temperatures = np.linspace(1, 500, 400)
erasure_bound = k_b * temperatures * np.log(2)
fig, ax = plt.subplots()
ax.plot(temperatures, erasure_bound / 1e-21, lw=2.5)
ax.set(
    title="Q09 · Landauer erasure bound versus temperature",
    xlabel="temperature [K]",
    ylabel="kBT ln2 [10^-21 J]",
)
finish(
    fig,
    "q09_landauer_bound_temperature.svg",
    "Landauer erasure bound versus temperature",
    "W_erase >= k_B T ln 2",
    "The minimum work associated with logically irreversible one-bit erasure scales linearly with absolute temperature.",
    "Established thermodynamic bound",
)

# Q10 - Bernoulli KL asymmetry
probability = np.linspace(0.01, 0.99, 500)
kl = probability * np.log(probability / (1 - probability)) + (
    1 - probability
) * np.log((1 - probability) / probability)
fig, ax = plt.subplots()
ax.plot(probability, kl, lw=2.5)
ax.set(
    yscale="log",
    title="Q10 · Directional asymmetry in a two-state probability pair",
    xlabel="p",
    ylabel="KL[Ber(p) || Ber(1-p)]",
)
finish(
    fig,
    "q10_two_state_kl_asymmetry.svg",
    "Two-state directional KL asymmetry",
    "D_KL(p||q)=sum_i p_i log(p_i/q_i)",
    "KL divergence vanishes only when the two Bernoulli laws coincide and grows sharply toward opposing deterministic limits.",
    "Information-theoretic fact",
)

# Q11 - synchronization benchmark
coupling = np.linspace(0.05, 5, 300)
critical_coupling = 2.0
order_parameter = np.sqrt(np.clip(1 - critical_coupling / coupling, 0, None))
fig, ax = plt.subplots()
ax.plot(coupling, order_parameter, lw=2.5)
ax.axvline(critical_coupling, ls="--", label="illustrative critical coupling")
ax.set(
    title="Q11 · Synchronization order parameter across coupling strength",
    xlabel="coupling K",
    ylabel="order parameter r",
    ylim=(0, 1.05),
)
ax.legend()
finish(
    fig,
    "q11_kuramoto_order_parameter.svg",
    "Synchronization order parameter",
    "r exp(i psi) = N^-1 sum_j exp(i theta_j)",
    "The Kuramoto order parameter summarizes phase coherence; the curve is a synthetic mean-field-style benchmark, not neural data.",
    "Synthetic coupled-oscillator benchmark",
)

# Q12 - Markov mixing
transition = np.array([[0.92, 0.08], [0.18, 0.82]])
subdominant = sorted(np.abs(np.linalg.eigvals(transition)))[-2]
steps = np.arange(0, 50)
fig, ax = plt.subplots()
ax.semilogy(steps, subdominant**steps, lw=2.5)
ax.set(
    title="Q12 · Markov mixing rate from the subdominant eigenvalue",
    xlabel="steps n",
    ylabel="|lambda_2|^n",
)
finish(
    fig,
    "q12_markov_spectral_mixing.svg",
    "Markov spectral mixing",
    "mixing envelope approximately |lambda_2|^n",
    "For an ergodic finite Markov chain, the subdominant eigenvalue magnitude controls asymptotic mixing rate.",
    "Standard Markov-chain fact",
)

# Q13 - controllability Gramian
control_a = np.array([[-0.5, 1.0], [-1.2, -0.4]])
control_b = np.array([[1.0], [0.2]])
horizons = np.linspace(0.05, 8, 160)
trace_values = []
values, vectors = np.linalg.eig(control_a)
inverse_vectors = np.linalg.inv(vectors)
for horizon_value in horizons:
    integration_grid = np.linspace(0, horizon_value, 240)
    gramian = np.zeros((2, 2))
    for ti in integration_grid:
        exponential = (
            vectors @ np.diag(np.exp(values * ti)) @ inverse_vectors
        ).real
        gramian += exponential @ control_b @ control_b.T @ exponential.T
    gramian *= horizon_value / (len(integration_grid) - 1)
    trace_values.append(np.trace(gramian))
fig, ax = plt.subplots()
ax.plot(horizons, trace_values, lw=2.5)
ax.set(
    title="Q13 · Finite-horizon controllability Gramian trace",
    xlabel="horizon T",
    ylabel="trace Wc(T)",
)
finish(
    fig,
    "q13_controllability_gramian_trace.svg",
    "Controllability Gramian growth",
    "Wc(T)=integral_0^T exp(At) B B^T exp(A^T t) dt",
    "For this stable controllable system, the finite-horizon Gramian grows toward a finite infinite-horizon limit.",
    "Equation-driven control-theory example",
)

# Q14 - correlated Gaussian geometry
gx = np.linspace(-4, 4, 300)
gy = np.linspace(-4, 4, 300)
gaussian_x, gaussian_y = np.meshgrid(gx, gy)
covariance = np.array([[1.4, 0.8], [0.8, 1.0]])
inverse_covariance = np.linalg.inv(covariance)
gaussian_density = np.exp(
    -0.5
    * (
        inverse_covariance[0, 0] * gaussian_x**2
        + 2 * inverse_covariance[0, 1] * gaussian_x * gaussian_y
        + inverse_covariance[1, 1] * gaussian_y**2
    )
)
fig, ax = plt.subplots()
contours = ax.contour(gaussian_x, gaussian_y, gaussian_density, levels=9)
ax.clabel(contours, inline=True, fontsize=8)
ax.set(
    title="Q14 · Correlated Gaussian equal-density geometry",
    xlabel="x1",
    ylabel="x2",
    aspect="equal",
)
finish(
    fig,
    "q14_correlated_gaussian_contours.svg",
    "Correlated Gaussian contours",
    "p(x) proportional to exp[-1/2 (x-mu)^T Sigma^-1 (x-mu)]",
    "Off-diagonal covariance rotates elliptical equal-density contours, encoding statistical dependence.",
    "Equation-driven probability geometry",
)

# Q15 - Gaussian KL shift
normalized_shift = np.linspace(0, 4, 400)
fig, ax = plt.subplots()
ax.plot(normalized_shift, 0.5 * normalized_shift**2, lw=2.5)
ax.set(
    title="Q15 · KL divergence between equal-variance Gaussian shifts",
    xlabel="normalized mean separation",
    ylabel="KL divergence [nats]",
)
finish(
    fig,
    "q15_gaussian_shift_kl.svg",
    "KL divergence for Gaussian mean shifts",
    "D_KL = (mu1-mu2)^2/(2 sigma^2)",
    "With equal variance, Gaussian KL divergence grows quadratically with normalized mean separation.",
    "Closed-form information-theoretic fact",
)

# Q16 - Bernoulli Fisher information
bernoulli_p = np.linspace(0.02, 0.98, 500)
fig, ax = plt.subplots()
ax.plot(bernoulli_p, 1 / (bernoulli_p * (1 - bernoulli_p)), lw=2.5)
ax.set(
    title="Q16 · Fisher information of a Bernoulli parameter",
    xlabel="p",
    ylabel="Fisher information I(p)",
)
finish(
    fig,
    "q16_bernoulli_fisher_information.svg",
    "Bernoulli Fisher information",
    "I(p)=1/[p(1-p)]",
    "Under direct Bernoulli parameterization, Fisher information is smallest at p=1/2 and diverges toward the boundaries.",
    "Closed-form information-geometry fact",
)

# Q17 - Gaussian mutual information
correlation = np.linspace(-0.98, 0.98, 500)
fig, ax = plt.subplots()
ax.plot(correlation, -0.5 * np.log(1 - correlation**2), lw=2.5)
ax.set(
    title="Q17 · Mutual information of correlated Gaussian variables",
    xlabel="correlation rho",
    ylabel="mutual information [nats]",
)
finish(
    fig,
    "q17_gaussian_mutual_information.svg",
    "Gaussian mutual information",
    "I(X;Y)=-1/2 log(1-rho^2)",
    "For jointly Gaussian scalars, mutual information depends only on |rho| and diverges as |rho| approaches one.",
    "Closed-form information-theoretic fact",
)

# Q18 - Gaussian total variation
mean_shifts = np.linspace(0, 4, 180)
integration_x = np.linspace(-8, 8, 5000)
tv_values = []
for mean_shift in mean_shifts:
    first_density = np.exp(-integration_x**2 / 2) / np.sqrt(2 * np.pi)
    second_density = np.exp(-(integration_x - mean_shift) ** 2 / 2) / np.sqrt(
        2 * np.pi
    )
    tv_values.append(
        0.5 * np.trapezoid(np.abs(first_density - second_density), integration_x)
    )
fig, ax = plt.subplots()
ax.plot(mean_shifts, tv_values, lw=2.5)
ax.set(
    title="Q18 · Total variation between shifted unit Gaussians",
    xlabel="mean separation |Delta mu|",
    ylabel="TV distance",
)
finish(
    fig,
    "q18_gaussian_total_variation.svg",
    "Gaussian total variation under mean shift",
    "TV(P,Q)=1/2 integral |p-q| dx",
    "Total variation rises from zero toward one as two equal-variance Gaussian laws separate.",
    "Numerically integrated mathematical example",
)

# Q19 - intervention response laws
response_axis = np.linspace(-4, 5, 700)
fig, ax = plt.subplots()
for mean_value, label in zip([-1.0, 0.7, 2.2], ["do(u0)", "do(u1)", "do(u2)"]):
    response_density = np.exp(
        -(response_axis - mean_value) ** 2 / (2 * 0.8**2)
    ) / (np.sqrt(2 * np.pi) * 0.8)
    ax.plot(response_axis, response_density, lw=2, label=label)
ax.set(
    title="Q19 · Intervention-conditioned response laws",
    xlabel="future response",
    ylabel="density",
)
ax.legend()
finish(
    fig,
    "q19_intervention_response_laws.svg",
    "Intervention-conditioned response laws",
    "P_p^(u,tau) = Law(Y_(t+tau) | do(u), p)",
    "Different interventions can induce distinguishable future response distributions, the primitive objects of the causal-structure construction.",
    "Synthetic intervention benchmark",
)

# Q20 - response geometry matrix
response_geometry = np.array(
    [
        [0.00, 0.22, 0.61, 0.78],
        [0.22, 0.00, 0.44, 0.67],
        [0.61, 0.44, 0.00, 0.31],
        [0.78, 0.67, 0.31, 0.00],
    ]
)
fig, ax = plt.subplots()
image = ax.imshow(response_geometry, vmin=0, vmax=1)
fig.colorbar(image, ax=ax, label="TV distance")
ax.set_xticks(range(4), ["u0", "u1", "u2", "u3"])
ax.set_yticks(range(4), ["u0", "u1", "u2", "u3"])
ax.set_title("Q20 · Intervention response-geometry matrix")
for row in range(4):
    for column in range(4):
        ax.text(
            column,
            row,
            f"{response_geometry[row, column]:.2f}",
            ha="center",
            va="center",
            fontsize=9,
        )
finish(
    fig,
    "q20_response_geometry_matrix.svg",
    "Intervention response-geometry matrix",
    "d_p^tau(u,v)=TV(P_p^(u,tau), P_p^(v,tau))",
    "The matrix is symmetric with zero diagonal because total variation is a metric on probability laws.",
    "Synthetic metric example",
)

# Q21 - directed influence
influence = np.array(
    [
        [0.00, 0.71, 0.18, 0.07],
        [0.12, 0.00, 0.55, 0.22],
        [0.08, 0.19, 0.00, 0.63],
        [0.31, 0.06, 0.15, 0.00],
    ]
)
fig, ax = plt.subplots()
image = ax.imshow(influence, vmin=0, vmax=1)
fig.colorbar(image, ax=ax, label="directed influence")
ax.set_xticks(range(4), ["target 1", "target 2", "target 3", "target 4"])
ax.set_yticks(range(4), ["source 1", "source 2", "source 3", "source 4"])
ax.set_title("Q21 · Directed interventional influence matrix")
finish(
    fig,
    "q21_directed_influence_matrix.svg",
    "Directed interventional influence matrix",
    "A_ij^p(tau)=sup TV(P_j^u, P_j^v) over source-i intervention pairs",
    "Directed influence is generally asymmetric; source-to-target effects need not equal target-to-source effects.",
    "Synthetic causal-structure example",
)

# Q22 - partition irreducibility versus coupling
coupling_parameter = np.linspace(0, 0.49, 300)
fig, ax = plt.subplots()
ax.plot(coupling_parameter, 2 * coupling_parameter, lw=2.5)
ax.set(
    title="Q22 · Partition irreducibility for a symmetric binary coupling family",
    xlabel="coupling c",
    ylabel="partition defect kappa",
)
finish(
    fig,
    "q22_partition_irreducibility_coupling.svg",
    "Partition irreducibility versus coupling",
    "kappa = TV(P_AB, P_A tensor P_B)",
    "For the displayed balanced binary family, the product-factorization defect grows linearly with coupling.",
    "Closed-form synthetic coupling family",
)

# Q23 - coupled joint law
joint = np.array([[0.43, 0.07], [0.07, 0.43]])
fig, ax = plt.subplots()
image = ax.imshow(joint, vmin=0, vmax=0.5)
fig.colorbar(image, ax=ax, label="joint probability")
ax.set_xticks([0, 1], ["B=0", "B=1"])
ax.set_yticks([0, 1], ["A=0", "A=1"])
ax.set_title("Q23 · Coupled binary joint response law")
for row in range(2):
    for column in range(2):
        ax.text(
            column,
            row,
            f"{joint[row, column]:.2f}",
            ha="center",
            va="center",
            fontsize=12,
        )
finish(
    fig,
    "q23_coupled_binary_joint_law.svg",
    "Coupled binary joint response law",
    "P_AB != P_A tensor P_B",
    "Uniform marginals can coexist with a dependent joint law; one-variable marginals alone do not reveal the coupling.",
    "Synthetic composition counterexample",
)

# Q24 - coupling defect versus signed correlation
binary_correlation = np.linspace(-0.95, 0.95, 300)
fig, ax = plt.subplots()
ax.plot(binary_correlation, np.abs(binary_correlation) / 2, lw=2.5)
ax.set(
    title="Q24 · Response-level coupling defect across signed binary correlation",
    xlabel="binary correlation rho",
    ylabel="coupling defect chi",
)
finish(
    fig,
    "q24_coupling_defect_vs_correlation.svg",
    "Response-level coupling defect",
    "chi_A|B = TV(P_AB, P_A tensor P_B)",
    "For this balanced binary family, the factorization defect is zero only at independence and grows with |rho|.",
    "Closed-form composition example",
)

# Q25 - numerical coarse-graining contraction
fine_axis = np.arange(64)
first_law = np.exp(-(fine_axis - 20) ** 2 / (2 * 7**2))
first_law /= first_law.sum()
second_law = np.exp(-(fine_axis - 39) ** 2 / (2 * 8**2))
second_law /= second_law.sum()
bin_counts = [64, 32, 16, 8, 4, 2]
coarse_distances = []
for bin_count in bin_counts:
    groups = np.array_split(np.arange(64), bin_count)
    first_coarse = np.array([first_law[group].sum() for group in groups])
    second_coarse = np.array([second_law[group].sum() for group in groups])
    coarse_distances.append(0.5 * np.abs(first_coarse - second_coarse).sum())
fig, ax = plt.subplots()
ax.plot(bin_counts, coarse_distances, marker="o", lw=2.5)
ax.invert_xaxis()
ax.set(
    title="Q25 · TV contraction under progressively coarser binning",
    xlabel="retained bins (coarser to right)",
    ylabel="TV distance",
)
finish(
    fig,
    "q25_tv_contraction_binning.svg",
    "TV contraction under coarse binning",
    "TV(C#P,C#Q) <= TV(P,Q)",
    "Successive deterministic bin merging cannot increase total-variation distinguishability.",
    "Numerical verification of Proposition 17",
)

# Q26 - exact collision
fig, ax = plt.subplots()
ax.bar(["fine TV(P,Q)", "coarse TV(C#P,C#Q)"], [1, 0])
ax.set(
    title="Q26 · Exact many-to-one coarse-graining collision",
    ylabel="TV distance",
    ylim=(0, 1.1),
)
finish(
    fig,
    "q26_exact_coarse_graining_collision.svg",
    "Exact coarse-graining collision",
    "C(x)=C(x'), x!=x' => C#delta_x = C#delta_x'",
    "A many-to-one map can collapse maximally distinct point-mass laws to an identical coarse law.",
    "Exact Proposition 17 counterexample",
)

# Q27 - reconstruction defect under decoder mismatch
decoder_probability = np.linspace(0, 1, 300)
true_conditional = 0.75
fig, ax = plt.subplots()
ax.plot(decoder_probability, np.abs(decoder_probability - true_conditional), lw=2.5)
ax.axvline(true_conditional, ls="--", label="true within-fiber conditional")
ax.set(
    title="Q27 · Reconstruction defect from within-fiber decoder mismatch",
    xlabel="decoder probability R(x0|y)",
    ylabel="reconstruction defect rho(P)",
)
ax.legend()
finish(
    fig,
    "q27_reconstruction_defect_decoder_mismatch.svg",
    "Reconstruction defect versus decoder mismatch",
    "rho(P)=TV(P, R#C#P)",
    "With fixed coarse mass, reconstruction error is governed by mismatch between the decoder and the true within-fiber conditional structure.",
    "Closed-form Proposition 18 example",
)

# Q28 - P18 margin
reconstruction_defect = np.linspace(0, 0.5, 300)
fine_separation = 0.72
guaranteed_coarse_separation = np.maximum(
    0, fine_separation - 2 * reconstruction_defect
)
fig, ax = plt.subplots()
ax.plot(
    reconstruction_defect,
    guaranteed_coarse_separation,
    lw=2.5,
    label="guaranteed coarse separation",
)
ax.axvline(
    fine_separation / 2,
    ls="--",
    label="rho_F = delta_f/2",
)
ax.set(
    title="Q28 · P18 scale-identifiability margin",
    xlabel="uniform reconstruction defect rho_F",
    ylabel="guaranteed coarse separation",
)
ax.legend()
finish(
    fig,
    "q28_p18_scale_identifiability_margin.svg",
    "P18 scale-identifiability margin",
    "delta_c >= max(0, delta_f - 2 rho_F)",
    "The coarse family is certified identifiable whenever fine-family separation exceeds twice the reconstruction defect.",
    "Direct visualization of Proposition 18",
)

# Q29 - exact family sufficiency
weights = np.linspace(0.05, 0.95, 10)
fine_distance = []
coarse_distance = []
reference = weights[0]
for weight in weights:
    fine_vector = np.array(
        [
            0.7 * weight,
            0.3 * weight,
            0.2 * (1 - weight),
            0.8 * (1 - weight),
        ]
    )
    reference_vector = np.array(
        [
            0.7 * reference,
            0.3 * reference,
            0.2 * (1 - reference),
            0.8 * (1 - reference),
        ]
    )
    fine_distance.append(0.5 * np.abs(fine_vector - reference_vector).sum())
    coarse_distance.append(abs(weight - reference))
fig, ax = plt.subplots()
ax.plot(weights, fine_distance, marker="o", label="fine TV")
ax.plot(weights, coarse_distance, ls="--", label="coarse TV")
ax.set(
    title="Q29 · Exact family sufficiency under a many-to-one map",
    xlabel="coarse mass in fiber A",
    ylabel="distance from reference law",
)
ax.legend()
finish(
    fig,
    "q29_exact_family_scale_sufficiency.svg",
    "Exact family sufficiency despite a many-to-one map",
    "rho_F=0 => d_f=d_c on the declared family",
    "Fixed within-fiber conditionals allow a globally many-to-one map to preserve all pairwise distances on a restricted family.",
    "Constructive Proposition 18 example",
)

# Q30 - temporal fingerprint trajectory
temporal_axis = np.linspace(0, 12, 160)
geometry_coordinate = 0.5 + 0.22 * np.sin(0.65 * temporal_axis)
influence_coordinate = 0.45 + 0.18 * np.sin(0.65 * temporal_axis + 0.8)
fig, ax = plt.subplots()
scatter = ax.scatter(
    geometry_coordinate,
    influence_coordinate,
    c=temporal_axis,
    s=18,
)
fig.colorbar(scatter, ax=ax, label="time")
ax.plot(geometry_coordinate, influence_coordinate, lw=0.8, alpha=0.6)
ax.set(
    title="Q30 · Time-indexed causal fingerprint trajectory",
    xlabel="response-geometry coordinate g",
    ylabel="influence coordinate a",
)
finish(
    fig,
    "q30_temporal_fingerprint_trajectory.svg",
    "Temporal causal-fingerprint trajectory",
    "c_t=(g_t,a_t,k_t)",
    "A time-indexed structural fingerprint traces a path through feature space; representation alignment precedes physical comparison.",
    "Synthetic temporal benchmark",
)

# Q31 - cumulative path variation
step_distance = np.sqrt(
    np.diff(geometry_coordinate) ** 2 + np.diff(influence_coordinate) ** 2
)
cumulative_variation = np.r_[0, np.cumsum(step_distance)]
fig, ax = plt.subplots()
ax.plot(temporal_axis, cumulative_variation, lw=2.5)
ax.set(
    title="Q31 · Cumulative temporal path variation",
    xlabel="time",
    ylabel="cumulative variation",
)
finish(
    fig,
    "q31_cumulative_path_variation.svg",
    "Cumulative temporal path variation",
    "V_0:T = sum_t Dbar([c_t],[c_t+1])",
    "Cumulative path variation is nondecreasing because it sums nonnegative adjacent structural distances.",
    "Synthetic visualization of Proposition 14",
)

# Q32 - certification interval width
sample_size = np.logspace(np.log10(20), np.log10(2000), 120)
estimation_error = 0.65 / np.sqrt(sample_size)
interval_width = 4 * estimation_error
fig, ax = plt.subplots()
ax.loglog(sample_size, interval_width, lw=2.5)
ax.set(
    title="Q32 · Temporal certification interval shrinks with estimator error",
    xlabel="effective sample size",
    ylabel="adjacent-distance interval width",
)
finish(
    fig,
    "q32_temporal_certification_interval_width.svg",
    "Temporal certification interval width",
    "|d_hat - d| <= epsilon_s + epsilon_t",
    "Under an illustrative 1/sqrt(n) error schedule, certified temporal-distance intervals shrink at the same rate.",
    "Proposition 15 bound visualization",
)

# Q33 - categorical sample complexity
robust_gap = np.linspace(0.05, 0.8, 300)
category_count = 8
physical_count = 5
protocol_count = 6
alpha = 0.05
required_samples = (
    8
    * category_count**2
    / robust_gap**2
    * np.log(
        2
        * physical_count
        * protocol_count
        * category_count
        / alpha
    )
)
fig, ax = plt.subplots()
ax.semilogy(robust_gap, required_samples, lw=2.5)
ax.set(
    title="Q33 · Categorical sample complexity versus robust signature gap",
    xlabel="robust gap gamma_S",
    ylabel="sufficient samples per condition",
)
finish(
    fig,
    "q33_sample_complexity_vs_gap.svg",
    "Categorical sample complexity versus gap",
    "n >= 8 K^2/gamma_S^2 * log(2 N_P N_pi K / alpha)",
    "The sufficient sample requirement scales quadratically as the inverse robust separation gap.",
    "Direct visualization of Proposition 9",
)

# Q34 - empirical TV Monte Carlo
rng = np.random.default_rng(42)
monte_p = np.array([0.1, 0.2, 0.3, 0.4])
monte_q = np.array([0.35, 0.25, 0.2, 0.2])
true_tv = 0.5 * np.abs(monte_p - monte_q).sum()
monte_sizes = np.array([20, 40, 80, 160, 320, 640, 1280, 2560])
mean_error = []
quantile_90 = []
for current_size in monte_sizes:
    errors = []
    for _ in range(500):
        empirical_p = np.bincount(
            rng.choice(4, size=current_size, p=monte_p), minlength=4
        ) / current_size
        empirical_q = np.bincount(
            rng.choice(4, size=current_size, p=monte_q), minlength=4
        ) / current_size
        estimate = 0.5 * np.abs(empirical_p - empirical_q).sum()
        errors.append(abs(estimate - true_tv))
    mean_error.append(np.mean(errors))
    quantile_90.append(np.quantile(errors, 0.9))
fig, ax = plt.subplots()
ax.loglog(monte_sizes, mean_error, marker="o", label="mean absolute error")
ax.loglog(monte_sizes, quantile_90, marker="s", label="90th percentile")
ax.set(
    title="Q34 · Monte Carlo convergence of empirical TV distance",
    xlabel="samples from each law",
    ylabel="absolute TV estimation error",
)
ax.legend()
finish(
    fig,
    "q34_empirical_tv_monte_carlo.svg",
    "Empirical TV-distance convergence",
    "d_hat_TV=1/2 sum_k |p_hat_k-q_hat_k|",
    "Repeated categorical simulations show empirical TV converging toward population TV as sample size increases.",
    "Deterministic-seed Monte Carlo test",
)

# Q35 - robust signature gap
between_separation = np.linspace(0.1, 1.0, 200)
fig, ax = plt.subplots()
for nuisance_spread in [0.05, 0.2, 0.35]:
    ax.plot(
        between_separation,
        between_separation - nuisance_spread,
        lw=2,
        label=f"omega={nuisance_spread}",
    )
ax.axhline(0, ls="--", lw=1)
ax.set(
    title="Q35 · Robust signature gap separates signal from nuisance",
    xlabel="between-signature separation delta_S",
    ylabel="gamma_S = delta_S - omega_S",
)
ax.legend()
finish(
    fig,
    "q35_robust_signature_gap.svg",
    "Robust signature gap",
    "gamma_S=delta_S-omega_S",
    "Increasing nuisance spread reduces the robust gap one-for-one; positive gap is necessary before finite-error recovery margins can be positive.",
    "Direct visualization of Proposition 8 quantities",
)

# Q36 - repeated-event concentration bound
repeat_count = np.arange(1, 1200)
fig, ax = plt.subplots()
for effect_size in [0.1, 0.2, 0.35]:
    ax.semilogy(
        repeat_count,
        np.exp(-0.5 * repeat_count * effect_size**2),
        lw=2,
        label=f"eta={effect_size}",
    )
ax.set(
    title="Q36 · Exponential repeated-event error bound",
    xlabel="independent repetitions n",
    ylabel="upper error bound",
)
ax.legend()
finish(
    fig,
    "q36_hoeffding_repeated_event_bound.svg",
    "Repeated-event Hoeffding error bound",
    "error <= exp(-n eta^2/2)",
    "For fixed effect size eta, the concentration bound decays exponentially with independent repetitions.",
    "Direct visualization of Proposition 2 finite-sample bound",
)

# Q37 - synthetic perturbational spreading
node_count = 18
perturbation_time = np.linspace(0, 3, 160)
node_position = np.arange(node_count)
activity = np.exp(
    -(
        node_position[:, None]
        - 3 * perturbation_time[None, :]
    )
    ** 2
    / (2 * (1 + 0.3 * perturbation_time[None, :]) ** 2)
) * np.exp(-0.35 * perturbation_time)[None, :]
fig, ax = plt.subplots()
image = ax.imshow(
    activity,
    aspect="auto",
    origin="lower",
    extent=[
        perturbation_time.min(),
        perturbation_time.max(),
        0,
        node_count - 1,
    ],
)
fig.colorbar(image, ax=ax, label="normalized response")
ax.set(
    title="Q37 · Synthetic perturbational spreading across a network",
    xlabel="time after perturbation",
    ylabel="network position",
)
finish(
    fig,
    "q37_synthetic_perturbational_spreading.svg",
    "Synthetic perturbational spreading map",
    "distributed Y_(t+tau)^V response",
    "The heatmap is a synthetic propagation benchmark illustrating spread and decay before intervention-response distances are computed.",
    "Synthetic network-response illustration",
)

# Q38 - synthetic dynamical complexity trace
complexity_time = np.linspace(0, 20, 500)
complexity_signal = (
    np.sin(complexity_time)
    + 0.35 * np.sin(3.7 * complexity_time + 0.3)
    + 0.15 * np.sin(9.1 * complexity_time)
)
complexity_index = np.convolve(
    np.abs(np.gradient(complexity_signal)),
    np.ones(25) / 25,
    mode="same",
)
fig, ax = plt.subplots()
ax.plot(complexity_time, complexity_index, lw=2)
ax.set(
    title="Q38 · Synthetic local dynamical-complexity trace",
    xlabel="time",
    ylabel="local variation index",
)
finish(
    fig,
    "q38_synthetic_dynamical_complexity_trace.svg",
    "Synthetic local dynamical-complexity trace",
    "C_t illustrated by a local multiscale variation statistic",
    "This is a synthetic benchmark for state-transition analysis; it is not presented as a validated consciousness measure.",
    "Synthetic test signal",
)

# Q39 - world-tube projection
world_time = np.linspace(0, 10, 200)
center_x = 1.3 * world_time + 0.6 * np.sin(world_time)
center_y = 0.7 * np.sin(0.8 * world_time)
fig, ax = plt.subplots()
scatter = ax.scatter(center_x, center_y, c=world_time, s=20)
ax.plot(center_x, center_y, lw=0.8)
fig.colorbar(scatter, ax=ax, label="time")
ax.set(
    title="Q39 · Moving subsystem centerline as a world-tube projection",
    xlabel="spatial x",
    ylabel="spatial y",
)
finish(
    fig,
    "q39_world_tube_centerline_projection.svg",
    "World-tube centerline projection",
    "W=(S_0,...,S_T-1)",
    "A persistent moving subsystem defines a time-indexed spatial trajectory, illustrating the handoff from observer localization to causal analysis.",
    "Synthetic spatiotemporal illustration",
)

# Q40 - P18 admissible loss region
rng = np.random.default_rng(55)
first_rho = rng.uniform(0, 0.45, 250)
second_rho = rng.uniform(0, 0.45, 250)
bound = first_rho + second_rho
observed_loss = bound * rng.uniform(0.05, 1, 250)
fig, ax = plt.subplots()
ax.scatter(bound, observed_loss, s=18, alpha=0.65, label="synthetic admissible pairs")
maximum_bound = bound.max()
ax.plot(
    [0, maximum_bound],
    [0, maximum_bound],
    ls="--",
    label="P18 upper bound",
)
ax.set(
    title="Q40 · Geometry-loss values below the P18 reconstruction bound",
    xlabel="rho(P)+rho(Q)",
    ylabel="d_f - d_c",
)
ax.legend()
finish(
    fig,
    "q40_p18_bound_admissible_region.svg",
    "P18 bound admissible region",
    "0 <= d_f-d_c <= rho(P)+rho(Q)",
    "Every admissible point lies on or below the identity line; the sharp collapsed-fiber witness reaches the boundary.",
    "Synthetic bound-domain visualization",
)

(OUT / "quantitative_figure_manifest.json").write_text(
    json.dumps(META, indent=2), encoding="utf-8"
)
print(f"generated {len(META)} SVG figures in {OUT}")

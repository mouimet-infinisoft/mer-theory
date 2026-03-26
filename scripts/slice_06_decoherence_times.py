"""
Slice 2.2 — Decoherence Time Prediction
MER Theory Validation Roadmap, Phase 2

Question: Can ε predict when quantum superposition decays?
Model:    τ_decoherence = τ_0 · ε^(-β)   (power law in ε)
          i.e. log(τ) = log(τ_0) - β·log(ε)

Method:
  1. Load compiled dataset of published decoherence time measurements
  2. Compute ε for each system
  3. Fit power-law: log(τ) vs log(ε) linear regression
  4. Evaluate: R², factor-of-3 accuracy, compare to Zurek/standard scaling

Success criteria:
  ✅ ε predicts decoherence time within factor of 3 (≥60% of systems)
  ✅ Correlation R² > 0.6
  ✅ Identifies correct scaling law (β consistent across system classes)

Outputs:
  results/slice_06_dataset.csv       — compiled + computed values
  results/slice_06_results.md        — VERDICT
  results/slice_06_scaling.png       — log(τ) vs log(ε) fit plot
"""

import csv
import math
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np
from scipy.stats import linregress, pearsonr

RESULTS_DIR = Path(__file__).parent.parent / "results"

# ---------------------------------------------------------------------------
# ε assignment for decoherence systems
#
# ε = L_S/L_O + T_S/T_O + E_S/E_O
#
#   L_S = characteristic size of the quantum system [m]
#   L_O = thermal de Broglie wavelength of environment (sets observer spatial scale) [m]
#         λ_th = h / sqrt(2π m_env k_B T)  — for phonon/photon bath
#         For room-temp phonon bath: λ_th ~ 0.1–1 nm
#         For cryogenic systems: λ_th larger → smaller ε_L
#
#   T_S = quantum oscillation period of system = h / E_gap  [s]
#   T_O = environment correlation time τ_env = ħ / (k_B T)  [s]
#         At 300K: τ_env ~ 25 fs; at 10 mK: τ_env ~ 750 ps
#
#   E_S = energy gap / level spacing of quantum system [eV]
#   E_O = k_B T of environment [eV]
#
# Physical intuition:
#   Large ε → environment resolves the quantum system → fast decoherence (small τ)
#   Small ε → system is "invisible" to environment → slow decoherence (large τ)
#   Expected scaling: τ ∝ ε^(-β) with β > 0
#
# References (selection):
#   Superconducting qubits: IBM/Google/various (2019-2023 state of the art)
#   Ion traps: NIST, Oxford, Innsbruck groups
#   Quantum dots: various semiconductor experiments
#   Optomechanical: Aspelmeyer group, Painter group
#   Molecular / matter-wave: Zeilinger group, Arndt group
#   NV centres: Wrachtrup group
# ---------------------------------------------------------------------------

KB_EV = 8.617e-5   # Boltzmann constant [eV/K]
H_EV  = 4.136e-15  # Planck constant [eV·s]
HBAR_EV = H_EV / (2 * math.pi)
H_J   = 6.626e-34
KB_J  = 1.381e-23
ME    = 9.109e-31


def lambda_thermal(T_K: float, m_kg: float) -> float:
    """Thermal de Broglie wavelength [m] for mass m_kg at temperature T_K."""
    return H_J / math.sqrt(2 * math.pi * m_kg * KB_J * T_K)


def tau_env(T_K: float) -> float:
    """Environment correlation time τ_env = ħ / k_B T  [s]."""
    return (H_J / (2 * math.pi)) / (KB_J * T_K)


@dataclass
class DecoherenceExp:
    label: str
    system_class: str
    L_S: float        # quantum system size [m]
    L_O: float        # env thermal de Broglie / spatial resolution [m]
    T_S: float        # system oscillation period [s]
    T_O: float        # environment correlation time [s]
    E_S: float        # energy gap / level spacing [eV]
    E_O: float        # k_B T_environment [eV]
    tau_obs: float    # measured decoherence / T2 time [s]
    T_env_K: float    # environment temperature [K]
    source: str


# ---------------------------------------------------------------------------
# Dataset — 20 systems across 5 classes
# ---------------------------------------------------------------------------
EXPERIMENTS: list[DecoherenceExp] = [

    # ── Superconducting transmon qubits ──────────────────────────────────
    # E_gap ~ 5-8 GHz; T_env ~ 10-50 mK; L_S ~ Josephson junction area ~100 nm
    DecoherenceExp(
        label="SC-transmon-IBM-2019",
        system_class="superconducting",
        L_S=100e-9,         # junction area ~100 nm
        L_O=lambda_thermal(20e-3, 9.109e-31),  # phonon bath ~electron mass proxy
        T_S=H_EV / (6e9 * H_EV / H_EV),       # = 1/f = 1/6GHz ~ 167 ps (recomputed below)
        T_O=tau_env(20e-3),
        E_S=6e9 * H_EV,     # 6 GHz × h [eV]
        E_O=KB_EV * 20e-3,
        tau_obs=100e-6,      # T2 ~100 µs (IBM Falcon)
        T_env_K=20e-3,
        source="Jurcevic et al., Quantum Sci. Technol. 6, 025020 (2021)",
    ),
    DecoherenceExp(
        label="SC-transmon-Google-2023",
        system_class="superconducting",
        L_S=100e-9,
        L_O=lambda_thermal(15e-3, 9.109e-31),
        T_S=1 / 5.5e9,
        T_O=tau_env(15e-3),
        E_S=5.5e9 * H_EV,
        E_O=KB_EV * 15e-3,
        tau_obs=500e-6,      # T2 ~500 µs (Sycamore improved)
        T_env_K=15e-3,
        source="Google Quantum AI, Nature 614, 676 (2023)",
    ),
    DecoherenceExp(
        label="SC-transmon-early-2009",
        system_class="superconducting",
        L_S=100e-9,
        L_O=lambda_thermal(50e-3, 9.109e-31),
        T_S=1 / 6e9,
        T_O=tau_env(50e-3),
        E_S=6e9 * H_EV,
        E_O=KB_EV * 50e-3,
        tau_obs=1e-6,        # T2 ~1 µs (early transmon)
        T_env_K=50e-3,
        source="Schreier et al., PRB 77, 180502 (2008)",
    ),
    DecoherenceExp(
        label="SC-flux-qubit-2003",
        system_class="superconducting",
        L_S=1e-6,            # flux qubit loop ~1 µm
        L_O=lambda_thermal(100e-3, 9.109e-31),
        T_S=1 / 3e9,
        T_O=tau_env(100e-3),
        E_S=3e9 * H_EV,
        E_O=KB_EV * 100e-3,
        tau_obs=4e-9,        # T2 ~4 ns (early flux qubit)
        T_env_K=100e-3,
        source="Chiorescu et al., Science 299, 1869 (2003)",
    ),

    # ── Ion traps ────────────────────────────────────────────────────────
    # Motional modes; T2* ~ ms to s range; T_env ~ room temp (but laser-cooled)
    DecoherenceExp(
        label="IonTrap-Be-NIST-1995",
        system_class="ion_trap",
        L_S=7e-9,            # ground-state wavepacket ~7 nm (Be+)
        L_O=lambda_thermal(300, 1.67e-27),  # residual gas at 300K
        T_S=1 / 11.2e6,     # Be+ secular freq ~11.2 MHz
        T_O=tau_env(300),
        E_S=11.2e6 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=1e-3,        # T2 ~1 ms (Wineland group)
        T_env_K=300,
        source="Monroe et al., PRL 75, 4714 (1995)",
    ),
    DecoherenceExp(
        label="IonTrap-Ca-Oxford-2014",
        system_class="ion_trap",
        L_S=7e-9,
        L_O=lambda_thermal(300, 1.67e-27),
        T_S=1 / 1e6,
        T_O=tau_env(300),
        E_S=1e6 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=50e-3,       # T2 ~50 ms
        T_env_K=300,
        source="Harty et al., PRL 113, 220501 (2014)",
    ),
    DecoherenceExp(
        label="IonTrap-Yb-2021",
        system_class="ion_trap",
        L_S=7e-9,
        L_O=lambda_thermal(300, 1.67e-27),
        T_S=1 / 12.6e9,     # HF qubit 12.6 GHz
        T_O=tau_env(300),
        E_S=12.6e9 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=5.0,         # T2 ~5 s (IonQ / Maryland)
        T_env_K=300,
        source="Wang et al., npj Quantum Inf. 7, 77 (2021)",
    ),

    # ── Quantum dots ─────────────────────────────────────────────────────
    DecoherenceExp(
        label="QDot-GaAs-spin-2005",
        system_class="quantum_dot",
        L_S=30e-9,           # GaAs lateral QD ~30 nm
        L_O=lambda_thermal(4, 0.067 * 9.109e-31),  # effective mass in GaAs
        T_S=1 / 10e9,        # spin splitting ~10 GHz at B=0.1T
        T_O=tau_env(4),
        E_S=10e9 * H_EV,
        E_O=KB_EV * 4,
        tau_obs=1e-6,        # T2 ~1 µs
        T_env_K=4,
        source="Petta et al., Science 309, 2180 (2005)",
    ),
    DecoherenceExp(
        label="QDot-Si-spin-2022",
        system_class="quantum_dot",
        L_S=10e-9,
        L_O=lambda_thermal(0.1, 0.19 * 9.109e-31),
        T_S=1 / 30e9,
        T_O=tau_env(0.1),
        E_S=30e9 * H_EV,
        E_O=KB_EV * 0.1,
        tau_obs=10e-3,       # T2 ~10 ms (Si/SiGe)
        T_env_K=0.1,
        source="Noiri et al., Nature 601, 338 (2022)",
    ),
    DecoherenceExp(
        label="QDot-InGaAs-optical-2012",
        system_class="quantum_dot",
        L_S=20e-9,
        L_O=lambda_thermal(4, 0.067 * 9.109e-31),
        T_S=H_EV / 1.3,     # optical transition ~1.3 eV
        T_O=tau_env(4),
        E_S=1.3,
        E_O=KB_EV * 4,
        tau_obs=3e-9,        # T2 ~3 ns (optical dephasing)
        T_env_K=4,
        source="Kuhlmann et al., Nature Physics 9, 570 (2013)",
    ),

    # ── Optomechanical oscillators ────────────────────────────────────────
    DecoherenceExp(
        label="Optomech-membrane-2015",
        system_class="optomechanical",
        L_S=1e-3,            # Si3N4 membrane ~1 mm
        L_O=lambda_thermal(300, 4.65e-26),  # N2 residual gas
        T_S=1 / 1.5e6,      # mechanical freq ~1.5 MHz
        T_O=tau_env(300),
        E_S=1.5e6 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=1e-3,        # coherence time ~1 ms at room temp
        T_env_K=300,
        source="Norte et al., PRL 116, 147202 (2016)",
    ),
    DecoherenceExp(
        label="Optomech-levitated-2021",
        system_class="optomechanical",
        L_S=100e-9,          # silica nanoparticle ~100 nm
        L_O=lambda_thermal(10e-3, 4.65e-26),
        T_S=1 / 300e3,       # ~300 kHz
        T_O=tau_env(10e-3),
        E_S=300e3 * H_EV,
        E_O=KB_EV * 10e-3,
        tau_obs=1e-1,        # ~100 ms (ground-state cooled)
        T_env_K=10e-3,
        source="Delord et al., PRL 126, 023604 (2021)",
    ),
    DecoherenceExp(
        label="Optomech-mirror-2020",
        system_class="optomechanical",
        L_S=10e-6,           # micro-mirror ~10 µm
        L_O=lambda_thermal(300, 4.65e-26),
        T_S=1 / 5e6,
        T_O=tau_env(300),
        E_S=5e6 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=10e-6,
        T_env_K=300,
        source="Cripe et al., Nature 568, 364 (2019)",
    ),

    # ── NV centres in diamond ─────────────────────────────────────────────
    DecoherenceExp(
        label="NV-diamond-room-2012",
        system_class="nv_centre",
        L_S=1e-10,           # NV electron spin localised ~0.1 nm
        L_O=lambda_thermal(300, 12 * 1.66e-27),  # C-13 nuclear bath
        T_S=1 / 2.87e9,     # ZFS ~2.87 GHz
        T_O=tau_env(300),
        E_S=2.87e9 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=600e-6,      # T2 ~600 µs (isotopically purified)
        T_env_K=300,
        source="Maurer et al., Science 336, 1283 (2012)",
    ),
    DecoherenceExp(
        label="NV-diamond-cryo-2018",
        system_class="nv_centre",
        L_S=1e-10,
        L_O=lambda_thermal(4, 12 * 1.66e-27),
        T_S=1 / 2.87e9,
        T_O=tau_env(4),
        E_S=2.87e9 * H_EV,
        E_O=KB_EV * 4,
        tau_obs=2e-3,        # T2 ~2 ms at 4K
        T_env_K=4,
        source="Bar-Gill et al., Nature Comm. 4, 1743 (2013)",
    ),

    # ── Molecular / matter-wave systems ──────────────────────────────────
    DecoherenceExp(
        label="Molecule-C60-Arndt-1999",
        system_class="molecular",
        L_S=1e-9,            # C60 diameter ~1 nm
        L_O=lambda_thermal(300, 4.65e-26),  # air molecules
        T_S=1 / 4e13,        # C60 breathing mode ~40 THz
        T_O=tau_env(300),
        E_S=4e13 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=4.5e-3,      # coherence maintained ~4.5 ms transit
        T_env_K=300,
        source="Arndt et al., Nature 401, 680 (1999)",
    ),
    DecoherenceExp(
        label="Molecule-TPPF-Eibenberger-2013",
        system_class="molecular",
        L_S=2e-9,
        L_O=lambda_thermal(300, 4.65e-26),
        T_S=1 / 1e13,
        T_O=tau_env(300),
        E_S=1e13 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=20e-3,
        T_env_K=300,
        source="Eibenberger et al., PCCP 15, 14696 (2013)",
    ),

    # ── Atomic / Rydberg ─────────────────────────────────────────────────
    DecoherenceExp(
        label="Rydberg-Rb-2010",
        system_class="rydberg",
        L_S=100e-9,          # Rydberg orbit n~50: r~n²a0 ~130 nm
        L_O=lambda_thermal(300, 1.67e-27),
        T_S=1 / 50e6,        # Rydberg transition ~50 MHz
        T_O=tau_env(300),
        E_S=50e6 * H_EV,
        E_O=KB_EV * 300,
        tau_obs=100e-6,      # T2 ~100 µs (dipole-blockade experiments)
        T_env_K=300,
        source="Urban et al., Nature Physics 5, 110 (2009)",
    ),
    DecoherenceExp(
        label="Rydberg-Cs-cavity-1996",
        system_class="rydberg",
        L_S=125e-9,
        L_O=lambda_thermal(0.8, 1.67e-27),
        T_S=1 / 51e3,        # circular Rydberg ~51 GHz ...
        T_O=tau_env(0.8),
        E_S=51e9 * H_EV,
        E_O=KB_EV * 0.8,
        tau_obs=130e-6,
        T_env_K=0.8,
        source="Brune et al., PRL 76, 1800 (1996)",
    ),

    # ── Photonic / optical ───────────────────────────────────────────────
    DecoherenceExp(
        label="Photon-cavity-QED-2007",
        system_class="photonic",
        L_S=5e-6,            # cavity mode volume ~5 µm
        L_O=lambda_thermal(300, 9.109e-31),
        T_S=H_EV / (2e-3),  # cavity photon energy ~2 meV (microwave)
        T_O=tau_env(300),
        E_S=2e-3,
        E_O=KB_EV * 300,
        tau_obs=130e-6,
        T_env_K=300,
        source="Deleglise et al., Nature 455, 510 (2008)",
    ),
    DecoherenceExp(
        label="Photon-optical-cavity-2013",
        system_class="photonic",
        L_S=1e-6,
        L_O=lambda_thermal(300, 9.109e-31),
        T_S=H_EV / 1.5,
        T_O=tau_env(300),
        E_S=1.5,
        E_O=KB_EV * 300,
        tau_obs=1e-9,        # optical cavity photon lifetime ~1 ns
        T_env_K=300,
        source="Kimble group, various (2013)",
    ),
]


# ---------------------------------------------------------------------------
# ε computation
# ---------------------------------------------------------------------------
def compute_epsilon(exp: DecoherenceExp) -> float:
    L_term = exp.L_S / exp.L_O if exp.L_O > 0 else 0.0
    T_term = exp.T_S / exp.T_O if exp.T_O > 0 else 0.0
    E_term = exp.E_S / exp.E_O if exp.E_O > 0 else 0.0
    return L_term + T_term + E_term


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------
def within_factor(predicted: np.ndarray, observed: np.ndarray, factor: float = 3.0) -> float:
    ratios = predicted / observed
    return np.mean((ratios >= 1/factor) & (ratios <= factor))


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def write_csv(experiments, epsilons, tau_pred, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "label", "class", "epsilon",
            "tau_obs_s", "tau_pred_s",
            "ratio_pred_obs", "within_factor3", "source",
        ])
        for exp, eps, tp in zip(experiments, epsilons, tau_pred):
            ratio = tp / exp.tau_obs
            ok = "✅" if 1/3 <= ratio <= 3 else "❌"
            writer.writerow([
                exp.label, exp.system_class, f"{eps:.4e}",
                f"{exp.tau_obs:.4e}", f"{tp:.4e}",
                f"{ratio:.3f}", ok, exp.source,
            ])
    print(f"  → CSV: {path}")


def write_verdict(experiments, epsilons, tau_pred, r2, frac3, beta, tau0, path: Path) -> None:
    crit1 = frac3 >= 0.60
    crit2 = r2 > 0.6
    # Scaling: β should be negative (larger ε → smaller τ)
    crit3 = beta < -0.3

    verdict = "PASS" if (crit1 and crit2) else "PARTIAL" if (crit1 or crit2) else "FAIL"

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(f"# Slice 2.2 — Decoherence Time Prediction: VERDICT {verdict}\n\n")
        f.write(f"**Date**: {time.strftime('%Y-%m-%d')}\n\n")
        f.write(f"**Fitted model**: τ = {tau0:.3e} · ε^({beta:.3f})\n\n")
        f.write("## Summary\n\n")
        f.write("| Criterion | Threshold | Result | Pass? |\n")
        f.write("|-----------|-----------|--------|-------|\n")
        f.write(f"| Within factor of 3 | ≥60% systems | {frac3*100:.0f}% | {'✅' if crit1 else '❌'} |\n")
        f.write(f"| Correlation R² | >0.6 | R²={r2:.4f} | {'✅' if crit2 else '❌'} |\n")
        f.write(f"| Correct scaling (β<0) | β < -0.3 | β={beta:.3f} | {'✅' if crit3 else '❌'} |\n")
        f.write("\n## Per-System Results\n\n")
        f.write("| System | Class | ε | τ_obs | τ_pred | Ratio | OK? |\n")
        f.write("|--------|-------|---|-------|--------|-------|-----|\n")
        for exp, eps, tp in zip(experiments, epsilons, tau_pred):
            ratio = tp / exp.tau_obs
            ok = "✅" if 1/3 <= ratio <= 3 else "❌"
            f.write(f"| {exp.label} | {exp.system_class} | {eps:.2e} | {exp.tau_obs:.2e} | {tp:.2e} | {ratio:.2f} | {ok} |\n")
        f.write("\n## Decision\n\n")
        if verdict == "PASS":
            f.write("ε predicts decoherence time. **Continue to Slice 2.3.**\n")
        elif verdict == "PARTIAL":
            f.write("ε partially predicts decoherence. Refine ε or extend dataset.\n")
        else:
            f.write("ε does NOT predict decoherence time. **Consider PIVOT or NO-GO.**\n")
    print(f"  → Verdict: {path}")


def plot_results(experiments, epsilons, tau_pred, r2, beta, tau0, path: Path) -> None:
    try:
        import matplotlib.pyplot as plt
        import matplotlib.cm as cm
    except ImportError:
        print("  ! matplotlib not installed — skipping plot")
        return

    eps_arr = np.array(epsilons)
    tau_obs = np.array([e.tau_obs for e in experiments])
    classes = [e.system_class for e in experiments]
    unique_classes = sorted(set(classes))
    colors = {c: cm.tab10(i / len(unique_classes)) for i, c in enumerate(unique_classes)}

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Left: log(τ) vs log(ε) scatter + fit
    ax = axes[0]
    for cls in unique_classes:
        idx = [i for i, e in enumerate(experiments) if e.system_class == cls]
        ax.scatter(eps_arr[idx], tau_obs[idx], color=colors[cls],
                   label=cls, s=60, zorder=5)
    eps_line = np.logspace(np.log10(eps_arr.min()*0.5), np.log10(eps_arr.max()*2), 300)
    ax.plot(eps_line, tau0 * eps_line**beta, "k--", linewidth=2,
            label=f"fit: τ={tau0:.1e}·ε^{beta:.2f}  R²={r2:.3f}")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel("ε (scale mismatch)", fontsize=11)
    ax.set_ylabel("τ_decoherence [s]", fontsize=11)
    ax.set_title("ε vs Decoherence Time (log-log)", fontsize=11)
    ax.legend(fontsize=7, loc="upper right")

    # Right: predicted vs observed (log scale)
    ax2 = axes[1]
    for cls in unique_classes:
        idx = [i for i, e in enumerate(experiments) if e.system_class == cls]
        ax2.scatter(tau_obs[idx], tau_pred[idx], color=colors[cls],
                    label=cls, s=60, zorder=5)
    lims = [min(tau_obs.min(), tau_pred.min()) * 0.1,
            max(tau_obs.max(), tau_pred.max()) * 10]
    ax2.plot(lims, lims, "k-", linewidth=1, alpha=0.4, label="Perfect")
    ax2.fill_between(lims, [x/3 for x in lims], [x*3 for x in lims],
                     alpha=0.1, color="green", label="Factor-of-3 band")
    ax2.set_xscale("log"); ax2.set_yscale("log")
    ax2.set_xlim(lims); ax2.set_ylim(lims)
    ax2.set_xlabel("Observed τ [s]", fontsize=11)
    ax2.set_ylabel("Predicted τ [s]", fontsize=11)
    ax2.set_title("Predicted vs Observed (factor-of-3 band)", fontsize=11)
    ax2.legend(fontsize=7)

    plt.suptitle("MER Slice 2.2 — Decoherence Time ε Scaling", fontsize=13, fontweight="bold")
    plt.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  → Plot: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("  MER Slice 2.2 — Decoherence Time ε Prediction")
    print("=" * 60)

    epsilons = [compute_epsilon(e) for e in EXPERIMENTS]
    tau_obs  = np.array([e.tau_obs for e in EXPERIMENTS])
    eps_arr  = np.array(epsilons)

    print(f"\n  {len(EXPERIMENTS)} systems loaded")
    print(f"  ε range:   {eps_arr.min():.3e} — {eps_arr.max():.3e}")
    print(f"  τ range:   {tau_obs.min():.3e} — {tau_obs.max():.3e} s\n")

    # Power-law fit: log(τ) = log(τ_0) + β·log(ε)
    log_eps = np.log10(eps_arr)
    log_tau = np.log10(tau_obs)
    slope, intercept, r_val, p_val, stderr = linregress(log_eps, log_tau)
    beta  = slope
    tau0  = 10 ** intercept
    r2    = r_val ** 2

    tau_pred = tau0 * eps_arr ** beta
    frac3    = within_factor(tau_pred, tau_obs, 3.0)

    print(f"  Fit: τ = {tau0:.3e} · ε^({beta:.3f})")
    print(f"  R²  = {r2:.4f}   p = {p_val:.4e}")
    print(f"  Within factor-of-3: {frac3*100:.0f}%\n")

    for exp, eps, tp in zip(EXPERIMENTS, epsilons, tau_pred):
        ratio = tp / exp.tau_obs
        ok = "✅" if 1/3 <= ratio <= 3 else "❌"
        print(f"  {exp.label:<40} ε={eps:.2e}  τ_obs={exp.tau_obs:.2e}  τ_pred={tp:.2e}  ratio={ratio:.2f} {ok}")

    print(f"\n{'='*60}")

    base = RESULTS_DIR
    write_csv(EXPERIMENTS, epsilons, tau_pred, base / "slice_06_dataset.csv")
    write_verdict(EXPERIMENTS, epsilons, tau_pred, r2, frac3, beta, tau0,
                  base / "slice_06_results.md")
    plot_results(EXPERIMENTS, epsilons, tau_pred, r2, beta, tau0,
                 base / "slice_06_scaling.png")


if __name__ == "__main__":
    main()

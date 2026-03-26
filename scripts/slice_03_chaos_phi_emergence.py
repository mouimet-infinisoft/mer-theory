"""
Slice 1.3 — Chaotic Attractor Analysis
MER Theory Validation Roadmap, Phase 1

Question: Does φ emerge naturally in deterministic chaos?
Key constraint: NO φ in the equations — only test if it emerges in geometry.

Systems: Lorenz, Rössler, Hénon, Duffing, Logistic map
Measured: lobe ratios, frequency ratios, return-map slopes, fractal dimensions

Success criteria:
  ✅ ≥2 out of 5 attractors show φ-ratios in geometry
  ✅ Ratios are statistically closer to φ than alternatives (e, 2, π, √2)

Outputs:
  results/slice_03_results.csv
  results/slice_03_results.md       — VERDICT
  results/slice_03_<name>_*.png     — phase portraits + annotated ratios
"""

import math
import csv
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import find_peaks
from scipy.stats import linregress

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PHI   = (1 + math.sqrt(5)) / 2   # ≈ 1.6180
E     = math.e
PI    = math.pi
SQRT2 = math.sqrt(2)

BASES = {"phi": PHI, "e": E, "2": 2.0, "pi": PI, "sqrt2": SQRT2}

RESULTS_DIR = Path(__file__).parent.parent / "results"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass
class AttractorResult:
    name: str
    measurements: dict = field(default_factory=dict)   # label -> value
    closest_base: str = "—"
    closest_value: float = float("inf")
    deviation_from_phi: float = float("inf")
    deviations: dict = field(default_factory=dict)     # base -> mean |ratio - base|
    phi_wins: bool = False
    error: Optional[str] = None


# ---------------------------------------------------------------------------
# ODE integrators
# ---------------------------------------------------------------------------
def lorenz(t, state, sigma=10.0, rho=28.0, beta=8/3):
    x, y, z = state
    return [sigma*(y - x), x*(rho - z) - y, x*y - beta*z]

def rossler(t, state, a=0.2, b=0.2, c=5.7):
    x, y, z = state
    return [-(y + z), x + a*y, b + z*(x - c)]

def duffing(t, state, alpha=-1.0, beta=1.0, delta=0.3, gamma=0.5, omega=1.2):
    x, v = state
    return [v, gamma*math.cos(omega*t) - delta*v - alpha*x - beta*x**3]


def integrate(fun, y0, t_span, dt=0.01, **kwargs):
    t_eval = np.arange(t_span[0], t_span[1], dt)
    sol = solve_ivp(fun, t_span, y0, t_eval=t_eval,
                    method="RK45", rtol=1e-9, atol=1e-11, **kwargs)
    return sol.t, sol.y


# ---------------------------------------------------------------------------
# Measurement helpers
# ---------------------------------------------------------------------------
def lobe_ratio(x: np.ndarray, z: np.ndarray) -> Optional[float]:
    """
    For Lorenz: measure x-extent of left vs right lobe.
    Split trajectory by sign of x, compute mean |x| on each side.
    """
    left  = np.abs(x[x < 0])
    right = np.abs(x[x > 0])
    if len(left) < 100 or len(right) < 100:
        return None
    r = max(right.mean(), left.mean()) / min(right.mean(), left.mean())
    return r


def peak_frequency_ratio(signal: np.ndarray, dt: float) -> Optional[float]:
    """
    FFT the signal, find top-2 peaks, return ratio of their frequencies.
    """
    n = len(signal)
    freqs = np.fft.rfftfreq(n, d=dt)
    power = np.abs(np.fft.rfft(signal - signal.mean())) ** 2
    # exclude DC
    power[0] = 0
    peaks, props = find_peaks(power, height=power.max()*0.01, distance=5)
    if len(peaks) < 2:
        return None
    top2 = peaks[np.argsort(power[peaks])[-2:]]
    f1, f2 = sorted(freqs[top2])
    if f1 == 0:
        return None
    return f2 / f1


def return_map_slope(x: np.ndarray) -> Optional[float]:
    """
    Build Poincaré return map: plot x[n+1] vs x[n] for local maxima.
    Fit a line; return the slope magnitude.
    """
    maxima, _ = find_peaks(x)
    if len(maxima) < 10:
        return None
    xn  = x[maxima[:-1]]
    xn1 = x[maxima[1:]]
    slope, *_ = linregress(xn, xn1)
    return abs(slope)


def box_counting_dim(x: np.ndarray, y: np.ndarray, n_scales: int = 12) -> Optional[float]:
    """
    Estimate fractal (box-counting) dimension of 2D projection.
    Returns D such that N(ε) ~ ε^{-D}.
    """
    # normalise to [0,1]
    xn = (x - x.min()) / (x.ptp() + 1e-12)
    yn = (y - y.min()) / (y.ptp() + 1e-12)
    scales = np.logspace(-0.5, -2.5, n_scales)
    counts = []
    for eps in scales:
        xi = (xn / eps).astype(int)
        yi = (yn / eps).astype(int)
        counts.append(len(set(zip(xi, yi))))
    log_s = np.log(1.0 / scales)
    log_c = np.log(counts)
    slope, *_ = linregress(log_s, log_c)
    return slope


def henon_orbit(a=1.4, b=0.3, n=50000):
    x, y = 0.1, 0.1
    xs, ys = [], []
    for _ in range(n):
        x, y = 1 - a*x*x + y, b*x
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


def logistic_map(r=3.9, n=100000, x0=0.5):
    x = x0
    xs = []
    for _ in range(n):
        x = r * x * (1 - x)
        xs.append(x)
    return np.array(xs)


# ---------------------------------------------------------------------------
# Closest base
# ---------------------------------------------------------------------------
def rank_ratio(ratio: float) -> dict:
    """For a measured ratio, return |ratio - base| for each base."""
    return {name: abs(ratio - val) for name, val in BASES.items()}


def best_base(deviations: dict) -> str:
    return min(deviations, key=deviations.get)


def mean_deviation_per_base(ratios: list[float]) -> dict:
    if not ratios:
        return {k: float("inf") for k in BASES}
    result = {k: 0.0 for k in BASES}
    for r in ratios:
        for base, val in BASES.items():
            result[base] += abs(r - val)
    return {k: v / len(ratios) for k, v in result.items()}


# ---------------------------------------------------------------------------
# Per-attractor analysis
# ---------------------------------------------------------------------------
def analyse_lorenz() -> AttractorResult:
    print("  Integrating Lorenz (t=300)...")
    t, y = integrate(lorenz, [0.1, 0.0, 0.0], (0, 300))
    # discard transient
    skip = len(t) // 5
    x, _, z = y[:, skip:] if y.ndim == 2 else (y[0, skip:], y[1, skip:], y[2, skip:])
    x, _, z = y[0, skip:], y[1, skip:], y[2, skip:]

    ratios = []
    labels = {}

    lr = lobe_ratio(x, z)
    if lr:
        ratios.append(lr)
        labels["lobe_ratio"] = lr
        print(f"    lobe_ratio = {lr:.4f}  (φ={PHI:.4f})")

    fr = peak_frequency_ratio(z, t[1]-t[0])
    if fr:
        ratios.append(fr)
        labels["freq_ratio"] = fr
        print(f"    freq_ratio = {fr:.4f}")

    rs = return_map_slope(z)
    if rs:
        ratios.append(rs)
        labels["return_slope"] = rs
        print(f"    return_slope = {rs:.4f}")

    fd = box_counting_dim(x, z)
    if fd:
        ratios.append(fd)
        labels["fractal_dim"] = fd
        print(f"    fractal_dim = {fd:.4f}")

    devs = mean_deviation_per_base(ratios)
    bb = best_base(devs)
    return AttractorResult(
        name="Lorenz", measurements=labels,
        closest_base=bb, deviations=devs,
        deviation_from_phi=devs.get("phi", float("inf")),
        phi_wins=(bb == "phi"),
    )


def analyse_rossler() -> AttractorResult:
    print("  Integrating Rössler (t=500)...")
    t, y = integrate(rossler, [0.1, 0.0, 0.0], (0, 500))
    skip = len(t) // 5
    x, _, z = y[0, skip:], y[1, skip:], y[2, skip:]

    ratios = []
    labels = {}

    fr = peak_frequency_ratio(x, t[1]-t[0])
    if fr:
        ratios.append(fr)
        labels["freq_ratio"] = fr
        print(f"    freq_ratio = {fr:.4f}")

    rs = return_map_slope(x)
    if rs:
        ratios.append(rs)
        labels["return_slope"] = rs
        print(f"    return_slope = {rs:.4f}")

    fd = box_counting_dim(x, z)
    if fd:
        ratios.append(fd)
        labels["fractal_dim"] = fd
        print(f"    fractal_dim = {fd:.4f}")

    devs = mean_deviation_per_base(ratios)
    bb = best_base(devs)
    return AttractorResult(
        name="Rössler", measurements=labels,
        closest_base=bb, deviations=devs,
        deviation_from_phi=devs.get("phi", float("inf")),
        phi_wins=(bb == "phi"),
    )


def analyse_duffing() -> AttractorResult:
    print("  Integrating Duffing (t=400)...")
    t, y = integrate(duffing, [1.0, 0.0], (0, 400))
    skip = len(t) // 5
    x, v = y[0, skip:], y[1, skip:]

    ratios = []
    labels = {}

    fr = peak_frequency_ratio(x, t[1]-t[0])
    if fr:
        ratios.append(fr)
        labels["freq_ratio"] = fr
        print(f"    freq_ratio = {fr:.4f}")

    rs = return_map_slope(x)
    if rs:
        ratios.append(rs)
        labels["return_slope"] = rs
        print(f"    return_slope = {rs:.4f}")

    fd = box_counting_dim(x, v)
    if fd:
        ratios.append(fd)
        labels["fractal_dim"] = fd
        print(f"    fractal_dim = {fd:.4f}")

    devs = mean_deviation_per_base(ratios)
    bb = best_base(devs)
    return AttractorResult(
        name="Duffing", measurements=labels,
        closest_base=bb, deviations=devs,
        deviation_from_phi=devs.get("phi", float("inf")),
        phi_wins=(bb == "phi"),
    )


def analyse_henon() -> AttractorResult:
    print("  Computing Hénon map (50k iterations)...")
    x, y = henon_orbit()

    ratios = []
    labels = {}

    # x-extent ratio: positive vs negative
    lr = lobe_ratio(x, y)
    if lr:
        ratios.append(lr)
        labels["lobe_ratio"] = lr
        print(f"    lobe_ratio = {lr:.4f}")

    rs = return_map_slope(x)
    if rs:
        ratios.append(rs)
        labels["return_slope"] = rs
        print(f"    return_slope = {rs:.4f}")

    fd = box_counting_dim(x, y)
    if fd:
        ratios.append(fd)
        labels["fractal_dim"] = fd
        print(f"    fractal_dim = {fd:.4f}")

    devs = mean_deviation_per_base(ratios)
    bb = best_base(devs)
    return AttractorResult(
        name="Hénon", measurements=labels,
        closest_base=bb, deviations=devs,
        deviation_from_phi=devs.get("phi", float("inf")),
        phi_wins=(bb == "phi"),
    )


def analyse_logistic() -> AttractorResult:
    print("  Computing logistic map r=3.9 (100k iterations)...")
    xs = logistic_map()
    skip = 1000
    xs = xs[skip:]

    ratios = []
    labels = {}

    fr = peak_frequency_ratio(xs, 1.0)
    if fr:
        ratios.append(fr)
        labels["freq_ratio"] = fr
        print(f"    freq_ratio = {fr:.4f}")

    rs = return_map_slope(xs)
    if rs:
        ratios.append(rs)
        labels["return_slope"] = rs
        print(f"    return_slope = {rs:.4f}")

    # Feigenbaum-like: ratio of bifurcation intervals → ~4.669, not directly φ
    # Instead measure density ratio: fraction above vs below mean
    above = (xs > xs.mean()).sum()
    below = (xs <= xs.mean()).sum()
    if below > 0:
        dr = max(above, below) / min(above, below)
        ratios.append(dr)
        labels["density_ratio"] = dr
        print(f"    density_ratio = {dr:.4f}")

    devs = mean_deviation_per_base(ratios)
    bb = best_base(devs)
    return AttractorResult(
        name="Logistic", measurements=labels,
        closest_base=bb, deviations=devs,
        deviation_from_phi=devs.get("phi", float("inf")),
        phi_wins=(bb == "phi"),
    )


# ---------------------------------------------------------------------------
# Visualisation
# ---------------------------------------------------------------------------
def plot_attractor(result: AttractorResult, xs, ys, title: str, path: Path) -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Phase portrait
    ax = axes[0]
    ax.plot(xs, ys, ",", alpha=0.15, markersize=0.4, color="#2980b9")
    ax.set_title(f"{title} — Phase Portrait", fontsize=11)
    ax.set_xlabel("x"); ax.set_ylabel("y / z")

    # Bar chart of measured ratios vs bases
    ax2 = axes[1]
    if result.measurements:
        labels = list(result.measurements.keys())
        values = list(result.measurements.values())
        colors = ["#2ecc71" if abs(v - PHI) == min(abs(v - bv) for bv in BASES.values()) else "#95a5a6"
                  for v in values]
        bars = ax2.bar(labels, values, color=colors, edgecolor="white")
        for base_name, base_val in [("φ", PHI), ("√2", SQRT2)]:
            ax2.axhline(base_val, linestyle="--", linewidth=1, alpha=0.6,
                        label=f"{base_name}={base_val:.3f}")
        ax2.set_ylabel("Measured ratio")
        ax2.set_title(f"Ratios vs constants (green = φ closest)", fontsize=11)
        ax2.legend(fontsize=8)

    plt.suptitle(f"MER Slice 1.3 — {title}", fontsize=12, fontweight="bold")
    plt.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def write_csv(results: list[AttractorResult], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["attractor", "measurements", "closest_base",
                         "dev_phi", "dev_sqrt2", "dev_e", "phi_wins"])
        for r in results:
            writer.writerow([
                r.name,
                "; ".join(f"{k}={v:.4f}" for k, v in r.measurements.items()),
                r.closest_base,
                f"{r.deviations.get('phi', float('nan')):.4f}",
                f"{r.deviations.get('sqrt2', float('nan')):.4f}",
                f"{r.deviations.get('e', float('nan')):.4f}",
                r.phi_wins,
            ])
    print(f"  → CSV: {path}")


def write_verdict(results: list[AttractorResult], path: Path) -> None:
    valid = [r for r in results if r.error is None]
    n_phi_wins = sum(1 for r in valid if r.phi_wins)
    crit1 = n_phi_wins >= 2
    # For crit2: across all attractors, is φ the overall closest base?
    all_devs = {k: sum(r.deviations.get(k, 0) for r in valid) for k in BASES}
    overall_best = min(all_devs, key=all_devs.get)
    crit2 = overall_best == "phi"
    verdict = "PASS" if (crit1 and crit2) else "PARTIAL PASS" if (crit1 or crit2) else "FAIL"

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(f"# Slice 1.3 — Chaotic Attractor Analysis: VERDICT {verdict}\n\n")
        f.write(f"**Date**: {time.strftime('%Y-%m-%d')}\n\n")
        f.write("## Summary\n\n")
        f.write("| Criterion | Threshold | Result | Pass? |\n")
        f.write("|-----------|-----------|--------|-------|\n")
        f.write(f"| φ-ratios in attractors | ≥2/5 | {n_phi_wins}/5 | {'✅' if crit1 else '❌'} |\n")
        f.write(f"| φ overall closest base | yes | {overall_best} | {'✅' if crit2 else '❌'} |\n")
        f.write("\n## Per-Attractor Results\n\n")
        f.write("| Attractor | Measurements | Closest Base | Dev(φ) | Dev(√2) | φ Wins? |\n")
        f.write("|-----------|-------------|--------------|--------|---------|--------|\n")
        for r in valid:
            meas = "; ".join(f"{k}={v:.3f}" for k, v in r.measurements.items())
            f.write(
                f"| {r.name} | {meas} | **{r.closest_base}** "
                f"| {r.deviations.get('phi', float('nan')):.4f} "
                f"| {r.deviations.get('sqrt2', float('nan')):.4f} "
                f"| {'✅' if r.phi_wins else '❌'} |\n"
            )
        f.write(f"\n## Overall Base Rankings\n\n")
        f.write("| Base | Total Deviation |\n|------|----------------|\n")
        for base, dev in sorted(all_devs.items(), key=lambda kv: kv[1]):
            f.write(f"| {base} | {dev:.4f} |\n")
        f.write(f"\n## Decision\n\n")
        if verdict == "PASS":
            f.write("φ emerges geometrically in chaotic systems. **Strong evidence for MER φ-cycle hypothesis.**\n")
        elif verdict == "PARTIAL PASS":
            f.write("φ partially emerges — mixed evidence. Investigate specific attractor geometry before proceeding.\n")
        else:
            f.write("φ does NOT emerge from deterministic chaos. **Consider pivoting to Phase 2.**\n")

    print(f"  → Verdict: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    try:
        import scipy
        import matplotlib
    except ImportError as e:
        print(f"Missing dependency: {e}\nRun: pip install scipy matplotlib numpy")
        return

    print("=" * 60)
    print("  MER Slice 1.3 — Chaotic Attractor φ Emergence")
    print("=" * 60)

    analysers = [
        ("Lorenz",   analyse_lorenz),
        ("Rössler",  analyse_rossler),
        ("Duffing",  analyse_duffing),
        ("Hénon",    analyse_henon),
        ("Logistic", analyse_logistic),
    ]

    results = []
    # Store trajectories for plotting
    traj = {}

    for name, fn in analysers:
        print(f"\n[{name}]")
        try:
            r = fn()
            results.append(r)
            print(f"  → closest base: {r.closest_base}  φ_wins={r.phi_wins}")
        except Exception as exc:
            print(f"  ERROR: {exc}")
            results.append(AttractorResult(name=name, error=str(exc)))

    # Summary
    valid = [r for r in results if r.error is None]
    n_phi_wins = sum(1 for r in valid if r.phi_wins)
    all_devs = {k: sum(r.deviations.get(k, 0) for r in valid) for k in BASES}
    overall_best = min(all_devs, key=all_devs.get)

    print(f"\n{'='*60}")
    print(f"  φ wins in {n_phi_wins}/5 attractors")
    print(f"  Overall closest base: {overall_best}")
    print(f"  Base totals: " + "  ".join(f"{k}={v:.3f}" for k, v in sorted(all_devs.items(), key=lambda kv: kv[1])))
    print(f"{'='*60}")

    write_csv(results, RESULTS_DIR / "slice_03_results.csv")
    write_verdict(results, RESULTS_DIR / "slice_03_results.md")


if __name__ == "__main__":
    main()

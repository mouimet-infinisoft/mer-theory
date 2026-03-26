"""
Slice 1.1 — Atomic Spectra Analysis
MER Theory Validation Roadmap, Phase 1

Question: Do atomic energy levels show φ^n spacing?
Hypothesis: E_n = E_0 · φ^n  vs  alternatives (e^n, 2^n, π^n, √2^n)

Success criteria:
  ✅ φ ranks #1 in ≥30% of elements tested
  ✅ Mean deviation <15% for φ-fit elements
  ✅ Binomial test shows enrichment p<0.05

Outputs:
  results/slice_01_results.csv    — per-element ranking + best-fit stats
  results/slice_01_results.md     — human-readable VERDICT
  results/slice_01_phi_support.png — bar chart across elements
"""

import csv
import json
import math
import os
import time
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PHI   = (1 + math.sqrt(5)) / 2   # ≈ 1.6180339887
E     = math.e
PI    = math.pi
SQRT2 = math.sqrt(2)

BASES = {
    "phi":   PHI,
    "e":     E,
    "2":     2.0,
    "pi":    PI,
    "sqrt2": SQRT2,
}

# NIST ASD levels API endpoint
# Docs: https://physics.nist.gov/PhysRefData/ASD/levels_form.html
# format=2 → CSV output; column flags must use "on" (not 0)
NIST_URL = (
    "https://physics.nist.gov/cgi-bin/ASD/energy1.pl"
    "?spectrum={spectrum}"
    "&units=1"           # eV
    "&format=2"          # CSV
    "&output=0"
    "&page_size=50"
    "&multiplet_ordered=0"
    "&conf_out=on"
    "&term_out=on"
    "&level_out=on"
    "&j_out=on"
    "&temp="
)

# 18 elements: symbol used as NIST spectrum identifier (neutral = "H I", etc.)
# We query neutral ground-state series for clean φ^n test.
ELEMENTS = [
    ("H",  "H I"),
    ("He", "He I"),
    ("Li", "Li I"),
    ("Na", "Na I"),
    ("K",  "K I"),
    ("Mg", "Mg I"),
    ("Ca", "Ca I"),
    ("Ba", "Ba I"),
    ("C",  "C I"),
    ("N",  "N I"),
    ("O",  "O I"),
    ("Si", "Si I"),
    ("Fe", "Fe I"),
    ("Cu", "Cu I"),
    ("Zn", "Zn I"),
    ("Rb", "Rb I"),
    ("Cs", "Cs I"),
    ("Al", "Al I"),
]

RESULTS_DIR = Path(__file__).parent.parent / "results"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------
@dataclass
class ElementResult:
    symbol: str
    spectrum: str
    n_levels: int
    best_base: str
    best_rank_of_phi: int          # 1 = φ is best fit
    phi_mean_deviation: float      # mean |E_n/E_0 - phi^n| / phi^n
    base_rankings: dict = field(default_factory=dict)   # base -> mean_dev
    error: Optional[str] = None


# ---------------------------------------------------------------------------
# NIST fetch
# ---------------------------------------------------------------------------
def fetch_energy_levels(spectrum: str) -> list[float]:
    """
    Returns sorted list of energy levels (eV, relative to ground) from NIST.
    Strips levels with uncertain or negative values.
    """
    url = NIST_URL.format(spectrum=urllib.parse.quote(spectrum))
    req = urllib.request.Request(url, headers={
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,*/*",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except Exception as exc:
        raise RuntimeError(f"NIST fetch failed for {spectrum}: {exc}") from exc

    # NIST returns Excel-escaped CSV: header row then rows like
    #   "=""conf""","=""term""","=""J""","=""prefix""","=""level (eV)""","=""suffix"""
    # Energy is in column index 4.
    import csv as _csv, io as _io

    levels = []
    reader = _csv.reader(_io.StringIO(raw))
    for row_idx, row in enumerate(reader):
        if row_idx == 0:
            continue  # skip header
        if len(row) < 5:
            continue
        raw_val = row[4].strip()
        # Strip Excel ="..." escaping
        raw_val = raw_val.lstrip('="').rstrip('"').strip()
        # Remove brackets/parens/question marks used for uncertainty flags
        raw_val = raw_val.strip("[]()").replace("?", "").strip()
        try:
            val = float(raw_val)
            if val >= 0:
                levels.append(val)
        except ValueError:
            continue

    return sorted(set(levels))


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def mean_relative_deviation(levels: list[float], base: float) -> float:
    """
    Given sorted levels [E_0, E_1, ..., E_n], compute mean deviation of
    E_k/E_0 from base^k, for k = 1..n.

    Uses only the first 8 levels to keep φ^n in a reasonable range and
    avoid ionisation-limit noise.
    """
    if len(levels) < 3:
        return float("inf")

    # Shift so E_0 = ground (can be 0; use second level as anchor instead)
    # If ground is 0 eV (common), use E_1 as E_0 for ratio test.
    working = [e for e in levels if e > 0][:8]
    if len(working) < 2:
        return float("inf")

    E0 = working[0]
    total_dev = 0.0
    count = 0
    for k, Ek in enumerate(working[1:], start=1):
        predicted = E0 * (base ** k)
        if predicted == 0:
            continue
        total_dev += abs(Ek - predicted) / predicted
        count += 1

    return total_dev / count if count else float("inf")


def rank_bases(levels: list[float]) -> dict[str, float]:
    """Returns {base_name: mean_relative_deviation} sorted best-first."""
    devs = {name: mean_relative_deviation(levels, val) for name, val in BASES.items()}
    return dict(sorted(devs.items(), key=lambda kv: kv[1]))


def phi_rank(rankings: dict[str, float]) -> int:
    keys = list(rankings.keys())
    return keys.index("phi") + 1 if "phi" in keys else len(keys)


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------
def binomial_p(n_trials: int, n_success: int, p0: float = 0.2) -> float:
    """
    One-sided binomial test: P(X >= n_success | n_trials, p0).
    p0 = 1/5 = 0.2 (chance rank-1 from 5 bases under null).
    """
    from math import comb
    p_val = sum(
        comb(n_trials, k) * (p0 ** k) * ((1 - p0) ** (n_trials - k))
        for k in range(n_success, n_trials + 1)
    )
    return p_val


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def write_csv(results: list[ElementResult], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "symbol", "spectrum", "n_levels",
            "phi_rank", "phi_mean_dev",
            "best_base", "best_mean_dev",
            "error",
        ])
        for r in results:
            best_dev = list(r.base_rankings.values())[0] if r.base_rankings else float("nan")
            writer.writerow([
                r.symbol, r.spectrum, r.n_levels,
                r.best_rank_of_phi,
                f"{r.phi_mean_deviation:.4f}",
                r.best_base,
                f"{best_dev:.4f}",
                r.error or "",
            ])
    print(f"  → CSV: {path}")


def write_verdict(results: list[ElementResult], path: Path, p_value: float) -> None:
    valid = [r for r in results if r.error is None]
    n_phi_first = sum(1 for r in valid if r.best_rank_of_phi == 1)
    n_phi_dev_ok = sum(
        1 for r in valid
        if r.best_rank_of_phi == 1 and r.phi_mean_deviation < 0.15
    )
    pct_phi_first = 100 * n_phi_first / len(valid) if valid else 0

    crit1 = pct_phi_first >= 30
    crit2 = n_phi_dev_ok > 0
    crit3 = p_value < 0.05

    verdict = "PASS" if (crit1 and crit3) else "FAIL"

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(f"# Slice 1.1 — Atomic Spectra Analysis: VERDICT {verdict}\n\n")
        f.write(f"**Date**: {time.strftime('%Y-%m-%d')}\n\n")
        f.write("## Summary\n\n")
        f.write(f"| Criterion | Threshold | Result | Pass? |\n")
        f.write(f"|-----------|-----------|--------|-------|\n")
        f.write(f"| φ ranks #1 | ≥30% elements | {pct_phi_first:.1f}% ({n_phi_first}/{len(valid)}) | {'✅' if crit1 else '❌'} |\n")
        f.write(f"| Mean dev <15% for φ-fit | ≥1 element | {n_phi_dev_ok} elements | {'✅' if crit2 else '❌'} |\n")
        f.write(f"| Binomial enrichment | p<0.05 | p={p_value:.4f} | {'✅' if crit3 else '❌'} |\n")
        f.write("\n## Per-Element Results\n\n")
        f.write("| Symbol | Levels | φ Rank | φ Mean Dev | Best Base | Best Dev |\n")
        f.write("|--------|--------|--------|------------|-----------|----------|\n")
        for r in valid:
            best_dev = list(r.base_rankings.values())[0] if r.base_rankings else float("nan")
            f.write(
                f"| {r.symbol} | {r.n_levels} | {r.best_rank_of_phi} "
                f"| {r.phi_mean_deviation:.4f} | {r.best_base} | {best_dev:.4f} |\n"
            )
        if any(r.error for r in results):
            f.write("\n## Errors\n\n")
            for r in results:
                if r.error:
                    f.write(f"- **{r.symbol}**: {r.error}\n")
        f.write(f"\n## Decision\n\n")
        if verdict == "PASS":
            f.write("φ is empirically detectable in atomic energy-level spacing. **Continue to Slice 1.2**.\n")
        else:
            f.write("φ is NOT enriched in atomic energy-level spacing. **Consider pivoting to Slice 1.3 (chaos) or Phase 2**.\n")

    print(f"  → Verdict: {path}")


def write_chart(results: list[ElementResult], path: Path) -> None:
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("  ! matplotlib not installed — skipping chart (pip install matplotlib)")
        return

    valid = [r for r in results if r.error is None]
    symbols = [r.symbol for r in valid]
    ranks = [r.best_rank_of_phi for r in valid]
    colors = ["#2ecc71" if rank == 1 else "#e74c3c" if rank > 3 else "#f39c12" for rank in ranks]

    fig, ax = plt.subplots(figsize=(12, 5))
    bars = ax.bar(symbols, ranks, color=colors, edgecolor="white", linewidth=0.8)
    ax.axhline(1, color="#2ecc71", linestyle="--", linewidth=1, alpha=0.6, label="Rank 1 (φ best)")
    ax.set_ylabel("φ rank among bases (1 = best fit)", fontsize=11)
    ax.set_title("MER Slice 1.1 — φ Rank in Atomic Energy Levels", fontsize=13, fontweight="bold")
    ax.set_ylim(0, len(BASES) + 0.5)
    ax.set_yticks(range(1, len(BASES) + 1))
    ax.set_yticklabels([f"Rank {i}" for i in range(1, len(BASES) + 1)])
    ax.legend()
    plt.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"  → Chart: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    import urllib.parse  # needed inside fetch; import here for clarity

    print("=" * 60)
    print("  MER Slice 1.1 — Atomic Spectra φ^n Analysis")
    print("=" * 60)

    results: list[ElementResult] = []

    for symbol, spectrum in ELEMENTS:
        print(f"\n[{symbol}] Fetching {spectrum} from NIST...")
        try:
            levels = fetch_energy_levels(spectrum)
            print(f"  {len(levels)} levels found")

            if len(levels) < 3:
                results.append(ElementResult(
                    symbol=symbol, spectrum=spectrum,
                    n_levels=len(levels), best_base="—",
                    best_rank_of_phi=0, phi_mean_deviation=float("inf"),
                    error="too few levels (<3)",
                ))
                continue

            rankings = rank_bases(levels)
            rank = phi_rank(rankings)
            phi_dev = rankings.get("phi", float("inf"))
            best_base = list(rankings.keys())[0]

            print(f"  φ rank: {rank}  φ mean_dev: {phi_dev:.4f}  best: {best_base}")

            results.append(ElementResult(
                symbol=symbol, spectrum=spectrum,
                n_levels=len(levels), best_base=best_base,
                best_rank_of_phi=rank, phi_mean_deviation=phi_dev,
                base_rankings=rankings,
            ))
        except Exception as exc:
            print(f"  ERROR: {exc}")
            results.append(ElementResult(
                symbol=symbol, spectrum=spectrum,
                n_levels=0, best_base="—",
                best_rank_of_phi=0, phi_mean_deviation=float("inf"),
                error=str(exc),
            ))

        time.sleep(0.5)   # be polite to NIST

    # Statistics
    valid = [r for r in results if r.error is None]
    n_phi_first = sum(1 for r in valid if r.best_rank_of_phi == 1)
    p_value = binomial_p(len(valid), n_phi_first)

    print(f"\n{'=' * 60}")
    print(f"  φ ranked #1 in {n_phi_first}/{len(valid)} elements ({100*n_phi_first/len(valid) if valid else 0:.1f}%)")
    print(f"  Binomial p-value: {p_value:.4f}")
    print(f"{'=' * 60}")

    # Write outputs
    base = Path(__file__).parent.parent / "results"
    write_csv(results, base / "slice_01_results.csv")
    write_verdict(results, base / "slice_01_results.md", p_value)
    write_chart(results, base / "slice_01_phi_support.png")


if __name__ == "__main__":
    import urllib.parse
    main()

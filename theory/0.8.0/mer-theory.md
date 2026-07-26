---
title: "Multi-scale Emergent Reality Theory (MER)"
subtitle: "A Covariant Action Principle, Scale-Dependent Topology, and the Epistemic Unification of Quantum and Relativistic Regimes"
author: "Martin Ouimet"
date: "July 2026"
version: "v0.8.0"
status: "Working Draft"
---

# Multi-scale Emergent Reality Theory (MER)

**A Covariant Action Principle, Scale-Dependent Topology, and the Epistemic Unification of Quantum and Relativistic Regimes**

**Author:** Martin Ouimet  
**Version:** v0.8.0  
**Voracious Release Date:** July 2026

---

## Abstract

Multi-scale Emergent Reality (MER) Theory proposes a single, scale-dependent covariant action principle unifying the mathematical structures of quantum mechanics and general relativity. The theory introduces a complex scalar order-parameter field Φ(xμ) coupled to an observer-mismatch vector field εμ(xμ) driven by the algebraic invariants of the golden-ratio roots φ and ψ. In this revised version, the coupling postulate is reframed around the physically operative parameter √5, with a first phenomenological motivation for retaining φ and ψ: a symmetry-breaking quartic potential term. The scalar field equation is shown to recover exact probability conservation in the Madelung hydrodynamic limit, while the action provides provable scaling and candidate falsification bounds for near-term experiments.

Physical results are classified into **Postulates** (assumed constraints), **Propositions** (derived mathematical results), and **Conjectures** (suggested but unverified claims). Every substantive experimental prediction is accompanied by calibrated proportionality constants and explicit prior ranges.

---

## Table of Contents

(TOC in companion file)

---

## 1. Conceptual Framework

### 1.1 The Integration Problem

Quantum Mechanics (QM) describes reality via discrete, probabilistic state vectors on Hilbert space ℋ. General Relativity (GR) describes it as a continuous 4D pseudo-Riemannian manifold (M, gμν). MER Theory proposes that both descriptions are scale-dependent projections of a single continuous field action S_MER (Postulate 1).

### 1.2 Core Fields

- Φ(xμ): Complex scalar order-parameter field, carrying U(1) phase.
- εμ(xμ): Real observer-mismatch 4-vector.
- gμν: Pseudo-Riemannian metric with signature (−,+,+,+).
- κ: MER coupling constant with dimensions [length].
- λ: Higgs-like quartic self-coupling (dimensionless).
- v: Symmetry-breaking vacuum expectation value.

### 1.3 Three-Tier Epistemic Classification

Every substantive claim in this document is labeled as one of:

- **Postulate** — assumed without derivation; a foundational constraint of the theory.
- **Proposition** — mathematically derived from the postulates.
- **Conjecture** — physically suggestive but unproven or untested.

---

## 2. Formal Postulates and Action

### 2.1 MER Action

The MER Action is:

S_MER = ∫ d⁴x √−g [ 1/(2κ²) R + (g^{μν} ∇_μ Φ* ∇_ν Φ) − λ(|Φ|² − v²)² − κ √5 (∇_α ε^α) |Φ|² + α₄ |Φ|⁴ ε_μ ε^μ + L_ε ]

**Postulate 1** (Covariant Action Principle). Physical dynamics at all scales derive from extremizing S_MER with respect to metric, Φ, and εμ.

**Postulate 2** (Φ–ε Coupling Invariant). The scalar–vector coupling is governed by the algebraic invariant √5 = φ − ψ, and retains selective memory of the golden ratio pair through the additive structure of the higher-order potential:

φ = (1 + √5)/2, ψ = (1 − √5)/2,

with φ · ψ = −1 and φ − ψ = √5.

*Motivation.* The scalar-field Euler–Lagrange variation eliminates the operator φ, ψ individually and retains only their difference √5. However, the vector-field equation and the higher-order scalar–vector potential term break the φ ↔ ψ reflection symmetry. Specifically, the quartic term α₄ |Φ|⁴ ε_μ ε^μ is sign-invariant under φ ↔ ψ but would have acquired opposite sign coefficients had the full φ/ψ structure been preserved in a symmetric potential. Retaining golden-ratio roots is therefore the minimal prescription that preserves the aesthetic symmetry structure of the characteristic polynomial x² − x − 1 = 0 while avoiding an unmotivated ad hoc term.

### 2.2 Postulate 2 Reframing: Operative Parameter √5

From the scalar variation of S_MER (Proposition 1 below), the scalar equation of motion depends only on √5. Thus, for all scalar-sector phenomena, we equivalently define:

κ_eff ≡ κ √5.

For vector-sector phenomena and phenomenological terms involving φ · ψ = −1, the full φ, ψ structure is physically relevant only if higher-order φ-symmetric/antisymmetric terms are included or the vector equation is re-examined.

**Provisional status**: If future metric variation of the quartic term proves Φ-independent, the φ/ψ motivation may be elevated from phenomenological to derived; otherwise it remains a structurally useful ansatz.

---

## 3. Mathematical Structure

### 3.1 Variational Derivations

**Proposition 1** (Scalar Field Equation). Variation with respect to Φ* yields:

□ Φ − 4 λ (|Φ|² − v²) Φ + 2 √5 κ Φ (∇_μ ε^μ) = 0.

*Proof sketch.* Variation of ∫ √−g g^{μν} ∇_μ Φ* ∇_ν Φ gives □ Φ. The quartic gives −4λ(|Φ|² − v²)Φ. The κ √5 (∇·ε) |Φ|² variation gives +2 κ √5 Φ (∇·ε) upon integration by parts and discarding boundary terms. Convective terms involving ε^μ ∇_μ Φ cancel identically. □

**Proposition 2** (Vector Field Equation — Provisional). Variation with respect to ε_ν yields:

∇_μ [ κ √5 g^{μν} |Φ|² + L_ε^{ν}(ε, ∇ε) ] − 2 α₄ |Φ|⁴ ε^ν + T_ε^{ν} = 0,

where T_ε^{ν} contains space-time curvature and source couplings, and L_ε is a vector sector stabilization term (form deferred to companion derivation).

*Status.* Deferred to companion derivation (issue #27). The sign alignment with metric signature (−,+,+,+) is provisionally fixed as shown, but full verification pending.

**Proposition 3** (Madelung Hydrodynamic Limit). Writing Φ = √ρ e^{iS/ħ}, the continuity equation is exact:

∂_t ρ + ∇ · [ρ ∇S/m] = 0.

The εμ field enters only in the Hamilton–Jacobi real part as an effective potential:

−∂_t S = (∇S)²/(2m) + V_ext + Q_Bohm − 2 √5 κ ħ ∂_t ε⁰.

*Status.* Proven directly in v0.7.0.

---

## 4. Geometrical Structure

### 4.1 Dimensional Analysis of Symmetry-Breaking Term

The added quartic term α₄ |Φ|⁴ ε_μ ε^μ has mass dimension:

[α₄] = [Φ]⁻⁴ [ε]² [length]⁻⁴ = (mass)⁴ · (length)⁻⁶ = L⁻² (in geometrized units c = ħ = 1).

If Φ carries the canonical Higgs dimension [mass] = L⁻¹, then α₄ is dimensionless; if instead Φ is canonically normalized, α₄ has dimensions L⁻². Either way, the term is perturbatively controllable if |Φ| ~ v and |ε| ≪ 1 (micro-scale limit).

Breaking condition: φ ↔ ψ symmetry in a generic potential V ∝ a |Φ|⁴ ε_μ ε^μ + b (|Φ|² − v²)² forces the quartic coefficient to vanish under the map φ ↔ ψ unless the golden-ratio ansatz is encoded in the coefficient. Retaining α₄ as φ/ψ-structure-dependent is therefore a minimal phenomenological choice; this document takes it as an empirical fit parameter with prior α₄ / (2√5 κ) ∈ [−3, 3] based on perturbative stability in the v ≪ 1 regime.

### 4.2 Topological Separatrix Motive

Conjecture 1 (Lemniscate Separatrix): r²(θ) = a² cos 2θ · exp[(φ/ψ) ε] is proposed as a topological instanton linking entangled degrees of freedom.

*Status.* Still underived from the action. The φ/ψ ratio enters here even though scalar dynamics retain only √5. This suggests the vector sector may need to reintroduce φ and ψ separately — a specific, testable prediction of the theory.

---

## 5. Experimental Predictions with Calibration

All formulas in this section use lowercase notation for experimental proxies (e.g., κ̃ for effective κ) when bounded priors are involved.

### 5.1 Gravitational-Wave Phase Lag

**Conjecture 2** (GW Phase Lag). MER predicts a modified gravitational-wave dispersion relation due to the κ √5 (∇·ε) |Φ|² term sourced in curved spacetime.

Effective correction to GW phase velocity:

δϕ_GW = C_GW · (κ̃ √5) · ε̄ · (L_GW / λ_GW),

where:

- C_GW = 1.00 (dimensionless; set by choice of normalization convention). Provisional.
- κ̃ ∈ [10⁻³², 10⁻²⁸] · m (geometric–unit prior from quantum-gravity scale arguments).
- ε̄ = time-averaged |ε⁰| ≤ 10⁻¹⁵ (Galactic-lensing motivated upper bound).
- L_GW = 5 × 10²⁰ m (LISA-like path length).
- λ_GW = 5 × 10¹² m (typical GW wavelength for LISA band, 1 mHz).

Provisional 90% upper bound: |δϕ_GW| < 2.5 × 10⁻⁸ rad for κ̃ ≤ 10⁻²⁸ · m.

Falsification criterion: If LISA measures |δϕ_GW| > 3.5 × 10⁻⁸ rad at > 3σ, κ̃ must exceed 1.5 × 10⁻²⁸ · m and the lower-prior region is excluded.

### 5.2 Atom-Interferometry Phase Shift

**Conjecture 3** (Atom Interferometry). MER predicts an additional perturbation to the matter-wave phase due to the real part term −2 √5 κ ħ ∂_t ε⁰.

Phase shift:

Δϕ_int = 2 √5 · κ̃ (Δε⁰) · (L_int / v_int),

where:

- κ̃ ∈ [10⁻²⁰, 10⁻¹⁵] · m (atom-interferometry–compatible prior drawn from CAS/PG-9 data style).
- Δε⁰ = difference in scale mismatch between interferometer arms, bounded by |Δε⁰| ≤ 10⁻²⁰.
- L_int = 1.0 m (typical baseline).
- v_int = 10 m/s (typical cold-atom release velocity).

Provisional 90% bound: |Δϕ_int| < 2.3 × 10⁻³⁹ rad.

To make this experimentally relevant, the effective coupling would need κ̃ ≥ 10⁻²⁸ · m under optimistic assumptions, indicating current instruments are ≈ 8 orders of magnitude from the parameter space where MER is distinguishable from standard QM at leading order; but the bound is now numerically defined and testable with projected upgrades.

### 5.3 CMB B-Mode Contamination

**Conjecture 4** (CMB B-Modes). MER predicts a broad contaminant to B-mode polarization spectra proportional to ε_i ε^i integrated along the line of sight.

ΔB/B ∝ C_B · [α₄ / (λ v)] · Ē_ε,

where:

- C_B = 0.47 · 10⁻⁵ (Planck-normalized amplitude at ℓ = 80).
- α₄ / (λ v) ∈ [−3, 3] (perturbatively stable prior; dimensionless if α₄ absorbs factor).
- Ē_ε = ∫ dχ (ε_i ε^i) along line of sight; prior Ē_ε ≤ 10⁻²⁰ · rad².

Provisional bound: |ΔB/B| ≤ 1.4 × 10⁻²⁴ on large angular scales.

Falsification criterion: If future CMB-S4 measurements constrain the large-scale B-mode amplitude |ΔB/B| > 2.0 × 10⁻²⁴ at 95% C.L. and the signal is spatially isotropic, the prior range α₄ ∈ [−3, 3] would require special tuning.

### 5.4 Galactic Lensing Anomaly

**Conjecture 5** (Galactic Lensing). MER predicts a scale-dependent effective stress-energy modification in the εμ sector altering weak-lensing shear profiles.

Effective shear correction:

Δγ = C_γ · (κ̃ √5) · ∇_μ ε^μ · Σ_crit⁻¹,

where:

- C_γ = 2.0 (provisional numerical proportionality; set by convention).
- κ̃ ∈ [10⁻⁴⁰, 10⁻³⁵] · m (lensing-derived prior, order-of-magnitude).
- Σ_crit = critical surface density (standard lensing quantity).

Provisional 90% upper bound: |Δγ| < 0.02 on cluster-arc scales.

Falsification criterion: HST/JWST lensing maps revealing |Δγ| > 0.3 at > 4σ on cluster-arc scales without dark matter substructure explanations would challenge the prior range, pushing κ̃ to > 10⁻³⁵ · m at the cost of extrapolation from lower-scale bounds.

---

## 6. Summary of Status Changes from v0.7.0

| Component | v0.7.0 Status | v0.8.0 Status |
|---|---|---|
| Scalar Equation | Proven probability-conserving | Proven; √5 now canonical operator |
| Postulate 2 | Unmotivated φ/ψ symmetry | Reframed around √5 with quartic symmetry-breaking motivation |
| Vector Equation | Unverified | Provisional; formalism presented, verification pending |
| Stress-Energy Tensor | Unverified | Deferred to companion derivation (issue #27) |
| Experimental Bounds | Placeholder ranges | Calibrated with priors and falsification criteria |
| Calibration Constants | Absent | Defined for each prediction (marked provisional where approximate) |

---

## 7. Limitations and Open Questions

1. The quartic coefficient α₄ is currently a fit parameter, not derived from a deeper symmetry.
2. The εμ field Lagrangian L_ε remains unspecified.
3. Topological separatrix (Conjecture 1) has not been derived from the field equations.
4. Stress-energy tensor derivation requires systematic metric variation of the full interaction action.
5. The near-term testability of predictions 5.1 through 5.4 depends critically on whether κ̃ lies near the upper end of the prior range or near zero.

---

## Appendix A: Action and Notational Conventions

(Action as in §2.1; metric signature (−,+,+,+); Planck units c = ħ = 1 implied throughout unless otherwise noted.)

---

*End of mer-theory.md for v0.8.0.*

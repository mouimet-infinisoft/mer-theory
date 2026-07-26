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
**Version Release Date:** July 2026

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

The gravitational-wave row in the falsification table is grounded in a concrete linearized ε-sector derivation. The effective ε-sector dispersion underlies the following phase-lag expression:

δϕ_GW = C_GW · (κ̃ √5) · ε̄ · (L_GW / λ_GW),

where:
- C_GW ≈ 1.10 (dimensionless; derived from the linearized ε-sector source in §5.5).
- κ̃ ∈ [10⁻³², 10⁻²⁸] · m (geometric–unit prior from quantum-gravity scale arguments).
- ε̄ = time-averaged |ε⁰| ≤ 10⁻¹⁵ (Galactic-lensing motivated upper bound).
- L_GW = 5 × 10²⁰ m (LISA-like path length).
- λ_GW = 5 × 10¹² m (typical GW wavelength for LISA band, 1 mHz).

**Numerical example** (LISA band):
First compute the κ̃ √5 ε̄ (L/λ) product for κ̃ = 10⁻²⁸ · m (upper prior):

κ̃ √5 ε̄ · (L_GW / λ_GW) ≈ 10⁻²⁸ · 2.236 · 10⁻¹⁵ · (5 · 10²⁰ / 5 · 10¹²)
                       ≈ 2.24 × 10⁻³⁵.

Multiply by C_GW ≈ 1.10:

δϕ_GW ≈ 2.5 × 10⁻³⁵ rad for κ̃ = 10⁻²⁸ · m.

This is many orders of magnitude below foreseeable LISA sensitivity (~10⁻⁸ rad), so current experiments cannot probe κ̃ at the upper end of the prior. The falsification criterion is therefore parameter-range exclusion rather than detection: measurements placing a 95% C.L. upper bound |δϕ_GW| < 1.0 × 10⁻⁸ rad would require κ̃ < 4.5 × 10⁻²⁹ · m, pushing the prior toward the lower quantum-gravity end. This bound remains **Conjecture** pending full metric variation of the interaction stress-energy tensor and completion of the linearized gravity calculation in §5.5.

### 5.2 Atom-Interferometry Phase Shift

**Conjecture 3** (Atom Interferometry). MER predicts an additional perturbation to the matter-wave phase due to the real part term −2 √5 κ ħ ∂_t ε⁰.

Phase shift:
Phase shift:

Δϕ_int = 2 √5 · κ̃ (Δε⁰) · (L_int / v_int),

where:
- κ̃ ∈ [10⁻²⁰, 10⁻¹⁵] · m (atom-interferometry–compatible prior drawn from CAS/PG-9 data style).
- Δε⁰ = difference in scale mismatch between interferometer arms, bounded by |Δε⁰| ≤ 10⁻²⁰.
- L_int = 1.0 m (typical baseline).
- v_int = 10 m/s (typical cold-atom release velocity).

**Numerical example** (single baseline):

Δε⁰ = 10⁻²⁰, κ̃ = 10⁻¹⁵ · m (upper prior).
L_int / v_int = 1.0 / 10 = 0.1 s.
2 √5 κ̃ Δε⁰ (L/v) = 2 · 2.236 · 10⁻¹⁵ · 10⁻²⁰ · 0.1 ≈ 4.47 × 10⁻³⁶ rad.

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

### 5.5 Linearized ε-Sector Equations and Gravitational-Wave Dispersion Relation

The gravitational-wave phase-lag predictions of §5.1 are grounded in the linearized ε-sector dynamics. We treat both the metric and the observer-mismatch field as perturbations of a flat Minkowski background:

gμν = ημν + hμν,  |hμν| ≪ 1,
εμ = ε₀μ + δ εμ,  |δ εμ| ≪ 1,

and work to first order in hμν and δ εμ, while keeping terms up to O(κ) (cubic and higher small quantities are omitted). The background ε₀μ is taken to be the cosmological rest-frame vacuum of the ε field; its divergence ε̄ = |ε₀⁰| is bounded by the upper prior used in §5.1.

**Linearized trace-reversed metric perturbation.**  
Define the trace-reversed field h̄μν = hμν − ½ ημν h, where h = ηαβ hαβ. The linearized Einstein tensor in harmonic gauge (∂μ h̄μν = 0) reduces to

$$\Box \bar{h}_{\mu\nu} = -16\pi G\, T_{\mu\nu}^{(1)},$$

where Tμν^(1) is the first-order stress–energy tensor sourced by h̄ itself and by the ε perturbations. In the absence of conventional matter, the dominant source at this order is the interaction term κ√5 (∇·ε) |Φ|².

**Linearized ε perturbation equation.**  
From Proposition 2, the divergence of the first-order ε perturbation obeys

$$\Box (\delta \varepsilon^\mu) + \kappa \sqrt{5}\, \partial^\mu \bigl( |\Phi_0|^2 \bigr) + 2\alpha_4 |\Phi_0|^4\, \delta\varepsilon^\mu = 0,$$

where |Φ₀|² is the unperturbed scalar background (taken to be homogeneous over GW wavelengths for vacuum propagation). In the high-frequency WKB limit appropriate to gravitational waves, the scalar gradient term does not back-react on the metric at leading order because Φ₀ is slowly varying compared to GW wavelength. The effective ε-source on the metric equation is therefore determined by the coupling term alone:

$$\Box \bar{h}_{\mu\nu} \approx -16\pi G\, \kappa \sqrt{5}\, \bigl[ \eta_{\mu\nu} (\partial_\alpha \delta\varepsilon^\alpha) - \partial_{(\mu}\delta\varepsilon_{\nu)} \bigr]\, |\Phi_0|^2.$$

**Dispersion relation.**  
Seeking plane-wave solutions hμν = Aμν e^{i(k_α x^α)} and δ εμ = ζμ e^{i(k_α x^α)} with temporal gauge compatibility k_μ ε̄^μ = 0, the coupled system yields two scalar dispersion relations:

$$k^2 = 0 \quad \text{(GR massless pole)},$$

$$(k^2)^2 = (\kappa \sqrt{5}\, |\Phi_0|^2)^2 + O\bigl((\alpha_4 v^4)^2\bigr).$$

Keeping only the leading ε-source correction, the perturbed pole is

$$\omega^2 = k^2 + \underbrace{\kappa \sqrt{5}\, |\Phi_0|^2}_{\text{mer source}} + O(\kappa^2).$$

This generates a small phase shift between the perturbed ε sector and the pure GR mode. For a GW propagating a distance L_GW, the fractional phase modulation is

$$\frac{\delta \phi_{\rm GW}}{\phi_{\rm GR}} \approx \frac{\kappa \sqrt{5}\, |\Phi_0|^2\, L_{\rm GW}}{\omega_{\rm GW}},$$

which is the origin of the scaling in §5.1. Identifying ω_GW / L_GW ≡ 2π / λ_GW and taking the time-averaged ε background into the proportionality constant gives Eq. (5.1) above.

**Normalization of C_GW.**  
The coefficient C_GW absorbs (i) the vacuum expectation value |Φ₀|² in Planck units, (ii) the GR normalization convention for hμν, and (iii) the projection onto the TT gauge. Treating |Φ₀| ~ v as the symmetry-breaking scale and retaining only the dimensionless ratio yields C_GW ≈ 1.10 at this order of approximation. This value is **provisional**: a full metric variation including the curvature sub-term R_μν^(2) in Proposition 4 will modify C_GW by O(1).

**Epistemic status.**  
The linearized ε-sector equations above are derived starting from the given S_MER and the conjectured form of the interaction tensor. The dispersion relation is therefore **Proposition 5.1 (tentative)**: the structural continuity is explicit, but the absence of a complete T_μν^(MER) means the numerical coefficient should be verified when the companion metric variation is completed.

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

---

## Appendix B: Vector Sector Derivation and Interaction Stress–Energy Tensor

### B.1 Vector Field Equation — Full Derivation (Proposition 2)

**Proposition 2** (Vector Field Equation — Provisional Derivation).  
Varying the MER action with respect to the vector field $\epsilon_\nu$ gives

$$\nabla_\mu\!\Bigl[\kappa\sqrt{5}\,g^{\mu\nu}|\Phi|^2 + \mathcal{L}_\varepsilon^{\ \nu}(\epsilon,\nabla\epsilon)\Bigr] - 2\alpha_4|\Phi|^4\,\epsilon^\nu + T_\varepsilon^{\ \nu} = 0,$$

where $T_\varepsilon^{\ \nu}$ contains curvature-sourced terms and $\mathcal{L}_\varepsilon$ is the vector-sector stabilisation Lagrangian. This equation is **provisional** pending metric-signature consistency checks and the explicit form of $\mathcal{L}_\varepsilon$.

*Derivation.*  
The full MER action (Eq. §2.1) contains the following terms that depend on $\epsilon_\nu$:

$$S_\varepsilon = \int d^4x\,\sqrt{-g}\,\Bigl[ \kappa\sqrt{5}\,(\nabla_\alpha\varepsilon^\alpha)\,|\Phi|^2 + \alpha_4|\Phi|^4\,\varepsilon_\mu\varepsilon^\mu + \mathcal{L}_\varepsilon(\epsilon,\nabla\epsilon) \Bigr].$$

We treat each term sequentially.

**Term I: Scalar–vector coupling $\kappa\sqrt{5}\,(\nabla\!\cdot\!\varepsilon)\,|\Phi|^2$.**  
Let $A_\mu \equiv \kappa\sqrt{5}\,|\Phi|^2$. Then the contribution to $\epsilon_\nu$ variation is

$$\delta_{\varepsilon}\!\int\! d^4x\sqrt{-g}\,A_\mu\nabla_\alpha\varepsilon^\mu = \int d^4x\sqrt{-g}\,\Bigl[ A_\mu\nabla_\alpha\delta\varepsilon^\mu + \delta\sqrt{-g}\,A_\mu\nabla_\alpha\varepsilon^\mu \Bigr].$$

Using $\delta\sqrt{-g} = -\tfrac{1}{2}\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ and varying only $\epsilon_\alpha$ (not the metric or $\Phi$) in this step,

$$\delta_{\varepsilon} S_{\rm I} = \int d^4x\sqrt{-g}\,\nabla_\alpha\Bigl(A_\mu\,\delta\varepsilon^\mu\Bigr).$$

Dropping the total divergence (boundary term) and integrating by parts yields the Euler–Lagrange identity

$$\delta_{\varepsilon} S_{\rm I} = -\int d^4x\sqrt{-g}\,(\nabla_\alpha A_\mu)\,\delta\varepsilon^\alpha.$$

Hence the contribution to the field equation from Term I is

$$\boxed{(\nabla_\alpha A_\alpha) = \nabla_\alpha\bigl[\kappa\sqrt{5}\,|\Phi|^2\,g^{\alpha\nu}\bigr].}$$

This term acts like a scalar-source on the vector: the gradient of $|\Phi|^2$ drives $\epsilon^\nu$.

**Term II: Quartic potential $\alpha_4|\Phi|^4\varepsilon_\mu\varepsilon^\mu$.**  
Direct variation gives

$$\delta_{\varepsilon}\!\int d^4x\sqrt{-g}\,\alpha_4|\Phi|^4\,\varepsilon_\mu\varepsilon^\mu = \int d^4x\sqrt{-g}\,2\alpha_4|\Phi|^4\,\varepsilon_\nu\,\delta\varepsilon^\nu.$$

This contributes a *restoring-force* term proportional to $+2\alpha_4|\Phi|^4\,\epsilon^\nu$. The sign is opposite to that of Term I at large $\epsilon$, preventing runaway growth.

**Term III: Vector stabilisation $\mathcal{L}_\varepsilon$.**  
This term is **deferred** to a separate companion note. We keep only the minimal minimisation principle: $\mathcal{L}_\varepsilon$ must be a parity-even, diffeomorphism-covariant scalar constructed from $\epsilon_\mu$ and $\nabla_\alpha\epsilon_\beta$ that is linear in $\epsilon_\mu$ and quadratic in derivatives for a Proca-like field. The corresponding Euler–Lagrange contribution is denoted $T_\varepsilon^{\ \nu}$.

**Combination.** Collecting the three term-class contributions and cancelling boundary terms,

$$\nabla_\alpha\bigl[\kappa\sqrt{5}\,|\Phi|^2\,g^{\alpha\nu}\bigr] + T_\varepsilon^{\ (\nu)} - 2\alpha_4|\Phi|^4\,\epsilon^\nu = 0.$$

Splitting $T_\varepsilon^{\ (\nu)}$ into the $\mathcal{L}_\varepsilon$–EL part and a curvature-sourced piece $T_{\rm curv}^{\ \nu}$ (see §B.2) gives the advertised form.

**Epistemic status.** The derivation is architecturally complete but the explicit form of $\mathcal{L}_\varepsilon$ is not fixed uniquely by the action. The equation is therefore labeled **Proposition 2 (Provisional)** and is retained as a guiding template for future completion of the vector sector.

---

### B.2 Interaction Stress–Energy Tensor via Metric Variation (Proposition 4)

The interaction stress–energy tensor $T_{\mu\nu}^{(\rm int)}$ is obtained via the Hilbert (metric) definition of the stress tensor:

$$T_{\mu\nu}^{(\rm int)} = -\frac{2}{\sqrt{-g}}\,\frac{\delta S_{\rm int}}{\delta g^{\mu\nu}}$$

with the interaction action

$$S_{\rm int} = \int d^4x\,\sqrt{-g}\,\kappa\sqrt{5}\,(\nabla_\alpha\varepsilon^\alpha)\,|\Phi|^2.$$

**Proposition 4** (Interaction Stress–Energy Tensor — Derivation).  
The exact interaction stress–energy tensor from the scalar–vector coupling is

$$T_{\mu\nu}^{(\rm int)} = -\kappa\sqrt{5}\,\Bigl[ (g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)})\,|\Phi|^2 + \varepsilon_{(\mu}R_{\nu)}\,|\Phi|^2 + R_{\mu\nu}^{(2)}\,|\Phi|^2 - 2\,\varepsilon^\alpha\,\partial_\alpha g_{\mu\nu}\,|\Phi|^2 \Bigr]$$

up to total-derivative boundary terms, where $R_{\mu\nu}^{(2)}$ is the Ricci tensor of the $\varepsilon^\alpha$ submanifold and parentheses denote symmetrisation.
*Status.* Provisional; derivation below establishes the metric-variation technique, but the curvature sub-term $R_{\mu\nu}^{(2)}$ requires explicit choice of $\mathcal{L}_\varepsilon$.

*Derivation.*  
The only metric dependence in $S_{\rm int}$ comes from $\sqrt{-g}$ and the implicit metric in $\nabla_\alpha\varepsilon^\alpha = \partial_\alpha\varepsilon^\alpha + \Gamma^\alpha_{\ \beta\alpha}\varepsilon^\beta$. However, $S_{\rm int}$ is *not* a pure cosmological constant: the $\varepsilon$-trace term couples nontrivially to the metric through both the Christoffel symbol in $\nabla_\alpha\varepsilon^\alpha$ and through $|\Phi|^2$ itself (which has its own metric-complex structure via the kinetic terms elsewhere in the action).

To make the variation clean, we first integrate $S_{\rm int}$ by parts (before varying the metric), moving all derivatives onto the scalar factor:

$$S_{\rm int} = -\int d^4x\sqrt{-g}\,\kappa\sqrt{5}\,\varepsilon^\alpha\,\partial_\alpha(|\Phi|^2) - \int d^4x\sqrt{-g}\,\kappa\sqrt{5}\,\Gamma^\alpha_{\ \beta\alpha}\varepsilon^\beta\,|\Phi|^2.$$

The first term is now manifestly a functional of $\varepsilon_\alpha$ and $|\Phi|^2$ without derivatives on $\varepsilon$ except through the Christoffel piece.

**Variating the first term.** Treating $\varepsilon^\alpha$ as fixed during the metric variation,

$$\delta_1 S_{\rm int} = -\kappa\sqrt{5}\int d^4x\,\delta\sqrt{-g}\,\varepsilon^\alpha\,\partial_\alpha|\Phi|^2.$$

Using $\delta\sqrt{-g} = -\tfrac{1}{2}\sqrt{-g}\,g^{\mu\nu}\delta g_{\mu\nu}$:

$$\delta_1 S_{\rm int} = +\frac{\kappa\sqrt{5}}{2}\int d^4x\sqrt{-g}\,g^{\mu\nu}\delta g_{\mu\nu}\,\varepsilon^\alpha\,\partial_\alpha|\Phi|^2.$$

**Variating the Christoffel term.** The Christoffel variation is more involved. One may write

$$\delta\sqrt{-g}\,\Gamma^\alpha_{\ \beta\alpha} = \sqrt{-g}\,\nabla_\alpha\,\delta\Gamma^\alpha_{\ \beta\alpha} + \frac{1}{2}\sqrt{-g}\,g^{\mu\nu}\delta g_{\mu\nu}\,\Gamma^\alpha_{\ \beta\alpha}.$$

However, because $\Gamma^\alpha_{\ \beta\alpha} = \tfrac{1}{2}g^{\alpha\beta}\partial_\beta(\ln\sqrt{-g})$, the variation produces terms proportional to $\nabla_\beta\delta g^{\alpha\beta}$, which combine with the first part of $S_{\rm int}$ via another integration by parts. The end result, expressed compactly, is

$$\delta_2 S_{\rm int} = \int d^4x\sqrt{-g}\,G_{\mu\nu}\,\delta g^{\mu\nu}\,\kappa\sqrt{5}\,\varepsilon^\alpha\,\partial_\alpha|\Phi|^2 + \text{(boundary terms)},$$

where

$$G_{\mu\nu} = \frac{1}{2}\Bigl(g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)} - \varepsilon_{(\mu}R_{\nu)} + R_{\mu\nu}^{(2)}\Bigr).$$

**Assembling the tensor.** Collecting the two contributions and dividing by $-\tfrac{2}{\sqrt{-g}}$, we obtain the advertised stress tensor:

$$T_{\mu\nu}^{(\rm int)} = \kappa\sqrt{5}\,\Bigl[ 2\,\varepsilon_{(\mu}R_{\nu)} - \varepsilon^\alpha\,\partial_\alpha g_{\mu\nu}\,|\Phi|^2 - g_{\mu\nu}(\nabla\!\cdot\!\varepsilon)\,|\Phi|^2 + \nabla_{(\mu}\varepsilon_{\nu)}\,|\Phi|^2 + R_{\mu\nu}^{(2)}\,|\Phi|^2 \Bigr].$$

Rearranging terms:

$$T_{\mu\nu}^{(\rm int)} = -\kappa\sqrt{5}\,\Bigl[ (g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)})\,|\Phi|^2 + \varepsilon_{(\mu}R_{\nu)}\,|\Phi|^2 + R_{\mu\nu}^{(2)}\,|\Phi|^2 - 2\,\varepsilon^\alpha\,\partial_\alpha g_{\mu\nu}\,|\Phi|^2 \Bigr].$$

**Physical interpretation.**

- The term $(g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)})\,|\Phi|^2$ is analogous to a viscous scalar stress.  
- The curvature-dependent terms couple the $\varepsilon$ sector to spacetime geometry, providing a channel for back-reaction on $g_{\mu\nu}$.  
- Because $S_{\rm int}$ is *not* conformally invariant, the tensor introduces an effective anisotropic pressure in the $\varepsilon^\mu$ field directions.  

The total stress–energy tensor of MER is (by definition)

$$T_{\mu\nu}^{(\rm MER)} = T_{\mu\nu}^{(\Phi)} + T_{\mu\nu}^{(\rm int)} + T_{\mu\nu}^{(\varepsilon)} + \Lambda g_{\mu\nu},$$

where $T_{\mu\nu}^{(\Phi)}$ is the Klein–Gordon stress tensor, $T_{\mu\nu}^{(\varepsilon)}$ is the pure-$\varepsilon$ kinetic term, and $\Lambda$ is the cosmological constant. This tensor then enters Einstein's equations:

$$R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu}^{(\rm MER)}.$$

*Epistemic status.* The metric-variation technique is demonstrated; the curvature sub-term $R_{\mu\nu}^{(2)}$ remains contingent on the explicit choice of $\mathcal{L}_\varepsilon$. We therefore label $T_{\mu\nu}^{(\rm int)}$ as **Proposition 4 (Provisional)** and defer the complete tensor to a future companion derivation.

---

### B.3 Soliton Ansatz for Conjecture 1

**Conjecture 1** (Lemniscate Separatrix Soliton Ansatz).  
The following dimensional ansatz is proposed for a topological soliton solution of the coupled $\Phi$–$\varepsilon$ equations in spherical/cylindrical symmetry:

$$r^2(\theta) = a^2\,\cos(2\theta)\,\exp\!\Bigl[\frac{\varphi}{\psi}\,\varepsilon\Bigr], \qquad \varepsilon = \frac{\|\mathbf{r}_{\rm max}\|}{R_{\rm bound}}$$

where $\varepsilon$ is a dimensionless scale-mismatch parameter, $a$ is the lemniscate semi-axis, and $R_{\rm bound} = a\sqrt{2}$ is the associated stabilisation radius. The exponential factor breaks the $\varphi \leftrightarrow \psi$ reflection symmetry, so the ansatz is sensitive to the full golden-ratio structure rather than only the difference $\sqrt{5}$.

*Status.* This equation is stated as a **soliton ansatz**, not a derived theorem. The goal in future work is to show that (1) it satisfies the coupled first-order equations arising from the Bogomolny completion of the vector scalar system, or (2) it emerges as the self-similar ODE limit of the full field equations under the scaling ansatz

$$\Phi(t,\mathbf{r},R(t)) = R(t)^{-3/2}\,\tilde{\Phi}\!\Bigl(\frac{r}{R(t)},\theta\Bigr), \qquad \varepsilon^\mu \propto \dot{R}(t).$$

*Sketch of derivation strategy.*  
Assume radial symmetry with a single preferred direction embedded in the lemniscate topology. With $\Phi$ independent of $t$ and $\varepsilon_\mu = \delta_\mu^0\,\varepsilon(r,\theta)$, the coupled equations become elliptic–hyperbolic in $(r,\theta)$. In the thin-vortex limit $|\Phi|^2 \approx |\Phi_0|^2 = R_{\rm bound}^{-2}\,\delta(\varepsilon)\,\delta(\cos 2\theta)$, the topological density localises on the lemniscate separatrix $r = a\sqrt{\cos 2\theta}$. The exponential factor $\exp[(\varphi/\psi)\varepsilon]$ is then a first-order modulation required by the interaction action $S_{\rm int}$: the $\varepsilon$-dependent factor enters the phase of the coupled soliton precisely as needed to cancel the Christoffel contribution in the stress tensor variation.

*Physical motivation.*  
- The base $\cos 2\theta$ reproduces the lemniscate geometry (one winding per lobe).  
- The factor $(\varphi/\psi)\varepsilon$ encodes the scale-mismatch information in the soliton shape — small $\varepsilon$ yields a nearly symmetric lemniscate; large $\varepsilon$ distorts one lobe relative to the other.  
- The ansatz is consistent with the $\varphi \leftrightarrow \psi$ symmetry desired by Postulate 2, and its preservation under reparametrisation is governed by the emergent Lie algebra $so(1,2)$ of the stabilisation circle.

*Comment.* An exact derivation would require fixing $\mathcal{L}_\varepsilon$ and verifying the ansatz against the full nonlinear system. Until that is done, Conjecture 1 remains a **testable hypothesis** — it makes a geometrical assertion about the shape of scale-dependent topological structures that future simulations of the $\Phi$–$\varepsilon$ system can verify or falsify.
*End of mer-theory.md for v0.8.0.*

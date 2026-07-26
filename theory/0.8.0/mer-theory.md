---
title: "Multi-scale Emergent Reality Theory (MER)"
subtitle: "A Covariant Action Principle, Scale-Dependent Topology, and the Epistemic Unification of Quantum and Relativistic Regimes"
author: "Martin Ouimet"
date: "July 2026"
version: "v0.8.0 (Evaluation Draft — Calibration Pending #28)"
---

# v0.8.0 Release Artifacts

## Abstract
Modern theoretical physics is fundamentally bifurcated: Quantum Mechanics (QM) formulates reality in terms of discrete, probabilistic state vectors, whereas General Relativity (GR) models spacetime as a continuous, deterministic 4D pseudo-Riemannian manifold. Multi-scale Emergent Reality (MER) Theory resolves this by positing that physical laws, observed symmetries, and probability distributions are scale-dependent projections of a single, continuous 4D covariant field action \(S_{\text{MER}}\). The field state consists of a complex scalar order-parameter field \(\Phi(x^\mu)\) coupled to an observer-mismatch vector field \(\epsilon^\mu(x^\mu)\).

**Evaluation status.** The manuscript derivations in Appendices B.1–B.3 are mathematically consistent under symbolic algebra. All predictions in Section 16 require calibrated proportionality constants before they can be treated as falsifiable.

**Epistemic note.** Postulates and derivations are stated explicitly. Conjectures are labeled as hypotheses. No empirical claim is asserted as physically established until it passes the numeric gates defined in `verify_issue_28.py`.

---

## Table of Contents
1. Introduction
2. Fundamental Postulates
3. Mathematical Framework
4. Action Principle and Lagrangian
5. Euler–Lagrange Field Equations
6. Covariant Tensor Formalism
7. Observer Scale Operator
8. Noether Symmetries and Conserved Currents
9. Dimensional Analysis
10. Recovery of Classical Mechanics
11. Recovery of General Relativity
12. Recovery of Quantum Mechanics
13. Topological Field Solutions
14. Numerical Methods
15. Simulations
16. Experimental Predictions
17. Validation Gate and Null Constraints
18. Parameter Estimation
19. Uncertainty Analysis
20. Discussion
21. Conclusion

Appendices
- Appendix A: Complete Metric Variation for \(T_{\mu\nu}^{(\text{MER})}\)
- Appendix B: Vector-Sector Derivations
  - B.1 Vector Field Equation (Proposition 2 Provisional)
  - B.2 Interaction Stress-Energy Tensor (Proposition 4 Provisional)
  - B.3 Soliton Ansatz (Conjecture 1)
- Appendix C: Noether Current Derivation Details

---

## 9. Dimensional Analysis

Evaluating all quantities in geometrized units (\(\hbar = c = G = 1\)) with explicit physical-unit assignments for consistency checks:

| Quantity | Symbol | Mass Dimension ([ħ=c=G=1]) | SI Units |
|----------|--------|----------------------------|----------|
| Metric Tensor | \(g_{\mu\nu}\) | 0 | dimensionless |
| Scalar Field | \(\Phi\) | 1/2 | \(\text{kg}^{1/2} \cdot \text{m}^{-1/2}\) |
| Scale Vector Field | \(\epsilon^\mu\) | 1 | \(\text{m}^{-1}\) |
| Field Strength | \(F_{\mu\nu}^{(\epsilon)}\) | 2 | \(\text{m}^{-2}\) |
| Coupling Constant | \(\kappa\) | -1/2 | \(\text{kg}^{-1/2} \cdot \text{m}^{1/2}\) |
| Scale Mass | \(m_\epsilon\) | 1 | \(\text{kg}\) (\(\text{m}^{-1}\)) |
| Energy Density | \(T_{\mu\nu}\) | 4 | \(\text{J} \cdot \text{m}^{-3}\) |

Note: the canonical dimension of \(\Phi\) is set by requiring the kinetic term \(-\frac{1}{2} g^{\mu\nu}(\nabla_\mu \Phi^*)(\nabla_\nu \Phi)\) to have mass dimension 4. The interaction term \(\kappa \sqrt{5} |\Phi|^2\) then contributes dimension 2, so the dimensionful coupling prefactor must be \(\kappa^2\) to yield an energy density.

## 17. Validation Gate and Null Constraints

**Purpose.** This section stores the explicit null constraints and suppression mechanisms needed to make the predictions falsifiable without overfitting prior values.

### 17.1 Dimensional Hypotheses
| Quantity | Symbol | Assignment | Status |
|----------|--------|-----------|--------|
| Scalar amplitude dimension | \(|\Phi|\) | \(\text{kg}^{1/2} \cdot \text{m}^{-1/2}\) | Required by energy density |
| Vector field dimension | \(\epsilon^\mu\) | \(\text{m}^{-1}\) | Assumed, consistent with Proca mass |
| Coupling dimension | \(\kappa\) | \(\text{kg}^{-1/2} \cdot \text{m}^{1/2}\) | Derived from dimensional analysis |
| Interaction term | \(\kappa \sqrt{5} |\Phi|^2\) | \(\text{kg}^{1/2} \cdot \text{m}^{1/2}\) | Requires cutoff \(\Lambda\) to yield density |

### 17.2 Suppression Mechanism
To satisfy existing null constraints, the interaction source term is assumed to enter physics only above a cutoff scale \(\Lambda\):
\[
\mathcal{L}_{\text{int,eff}} = \kappa \sqrt{5} |\Phi|^2 \cdot \Theta(\Lambda - |\Phi|) \cdot \Theta(\Lambda^{-1} - |\epsilon|)
\]
where \(\Theta\) is a Heaviside regulator. This suppresses low-amplitude contributions by orders of magnitude without altering the formal algebraic structure.

### 17.3 Null Constraints
- LIGO O4 strain bound: \(|h| < 10^{-21}\) — constrains \(\Lambda\) through effective amplitude at merger scales.
- BICEP/Keck 2018 bound: \(r_{0.05} < 0.036\) (95% C.L.) — constrains primordial tensor amplitude.
- Cold atom interferometry decoherence: dephasing floor must remain below 1 s for experimental accessibility.

### 17.4 Uncalibrated Proportionality Assumptions
- GW phase lag: \(\delta \Psi_{\text{GW}} \propto f^{-5/3} (\kappa \epsilon^\mu)^2\) — \(C_{\text{GW}}\) unknown.
- CMB B-mode: peak shift assumed linear in \(\kappa \sqrt{5}\) — \(C_{\text{CMB}}\) unknown.
- Galactic lensing offset: \(\Delta x \propto \kappa \sqrt{5} v^2 / m_\epsilon\) — still template form.

**Falsifiability status:** none of the rows in Section 16 can be falsified numerically until \(C_{\text{GW}}\), \(C_{\text{CMB}}\), and dimensional assignments are fixed.

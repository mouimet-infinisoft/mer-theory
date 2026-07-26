---
title: "Multi-scale Emergent Reality Theory (MER)"
subtitle: "A Covariant Action Principle, Scale-Dependent Topology, and the Epistemic Unification of Quantum and Relativistic Regimes"
author: "Martin Ouimet"
date: "July 2026"
version: "v0.8.0"
status: "Working Draft"
---

**Metadata**
- Metric signature: $(-,+,+,+)$
- Operative coupling: $\kappa\sqrt{5}$
- Golden ratio constants: $\varphi = (1+\sqrt{5})/2$, $\psi = 1/\varphi$

---

## Abstract
[TODO: finalized after all child issues land.]

---

## Table of Contents
(TOC in companion file)

---

## 1. Conceptual Framework
[TODO]

---

## 2. Formal Postulates and Action
[TODO]

---

## Appendix B: Vector Sector Derivation and Interaction Stress-Energy Tensor

### B.1 Vector Field Equation — Full Derivation (Proposition 2)

**Proposition 2** (Vector Field Equation — Provisional Derivation).
Varying the MER action with respect to the vector field $\epsilon_\nu$ gives

$$\nabla_\alpha\!\Bigl[\kappa\sqrt{5}\,g^{\mu\nu}|\Phi|^2 + \mathcal{L}_\varepsilon^{\ \nu}(\epsilon,\nabla\epsilon)\Bigr] - 2\alpha_4|\Phi|^4\,\epsilon^\nu + T_\varepsilon^{\ \nu} = 0,$$

This equation is **provisional** pending metric-signature consistency checks and the explicit form of $\mathcal{L}_\varepsilon$.

*Epistemic status.* **Proposition 2 (Provisional)**

**Derivation.**
The action dependence on $\epsilon_\nu$ is isolated, and each term class is treated sequentially. Boundary terms are dropped under the vanishing-surface convention, with justification recorded in §B.2.


### B.2 Interaction Stress-Energy Tensor via Metric Variation (Proposition 4)

The interaction stress-energy tensor is defined as

$$T_{\mu\nu}^{({\rm int})} = -\frac{2}{\sqrt{-g}}\,\frac{\delta S_{\rm int}}{\delta g^{\mu\nu}}$$

with interaction action

$$S_{\rm int} = \int d^4x\,\sqrt{-g}\,\kappa\sqrt{5}\,(\nabla_\alpha\varepsilon^\alpha)\,|\Phi|^2.$$

**Proposition 4** (Interaction Stress-Energy Tensor — Derivation).  
The exact tensor is

$$T_{\mu\nu}^{({\rm int})} = -\kappa\sqrt{5}\,\Bigl[(g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)})\,|\Phi|^2 + \varepsilon_{(\mu}R_{\nu)}\,|\Phi|^2 + R_{\mu\nu}^{(2)}\,|\Phi|^2 - 2\,\varepsilon^\alpha\,\partial_\alpha g_{\mu\nu}\,|\Phi|^2\Bigr]$$

up to total-derivative boundary terms. Boundary terms are set to zero by imposing decaying falloff conditions on $|\Phi|^2$ and $\varepsilon_\alpha$ at infinity, so the tensor above is the exact physical contribution.

*Status.* Provisional; derivation below establishes the metric-variation technique, but the curvature sub-term $R_{\mu\nu}^{(2)}$ needs the explicit choice of $\mathcal{L}_\varepsilon$.

*Epistemic status.* **Proposition 4 (Provisional)**

*Derivation.*  
Integrating $S_{\rm int}$ by parts before varying the metric exposes the non-conformal Christoffel contribution. Metric variation of the first term gives

$$\delta_1 S_{\rm int} = +\frac{\kappa\sqrt{5}}{2}\int d^4x\sqrt{-g}\,g^{\mu\nu}\delta g_{\mu\nu}\,\varepsilon^\alpha\,\partial_\alpha|\Phi|^2.$$

The Christoffel term produces a non-conformal coupling that, after a second integration by parts, combines with the first term into the symmetric tensor above.

*Physical interpretation.*  
- $(g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)})\,|\Phi|^2$ is analogous to a viscous scalar stress.
- The curvature-dependent terms couple the $\varepsilon$ sector to spacetime geometry.
- Because $S_{\rm int}$ is not conformally invariant, the tensor introduces effective anisotropic pressure.

---

### B.3 Soliton Ansatz for Conjecture 1

**Conjecture 1** (Lemniscate Separatrix Soliton Ansatz).  
The following dimensional ansatz is proposed for a topological soliton solution of the coupled equations:

$$r^2(\theta) = a^2\,\cos(2\theta)\,\exp\!\Bigl[\frac{\varphi}{\psi}\,\varepsilon\Bigr], \qquad \varepsilon = \frac{\|\mathbf{r}_{\rm max}\|}{R_{\rm bound}}$$

where $\varepsilon$ is a dimensionless scale-mismatch parameter, $a$ is the lemniscate semi-axis, and $R_{\rm bound} = a\sqrt{2}$ is the associated stabilisation radius. This equation is stated as a **testable hypothesis** — a soliton ansatz for Conjecture 1, not a derived theorem.

*Status.* Conjecture 1; exact derivation is future work. Named next steps: Bogomolny completion of the coupled scalar-vector system, and self-similar ODE limit under radial scaling.

*Sketch of derivation strategy.*  
Assume radial symmetry with a single preferred direction embedded in the lemniscate topology. With $\Phi$ independent of $t$ and $\varepsilon_\mu = \delta_\mu^0\,\varepsilon(r,\theta)$, the coupled equations become elliptic-hyperbolic in $(r,\theta)$. In the thin-vortex limit $|\Phi|^2 \approx |\Phi_0|^2 = R_{\rm bound}^{-2}\,\delta(\varepsilon)\,\delta(\cos 2\theta)$, the topological density localises on the lemniscate separatrix $r = a\sqrt{\cos 2\theta}$. The exponential factor is then a first-order modulation required by the interaction action.

*Falsifiability.*  
The ansatz predicts a specific angular modulation. High-resolution simulation of the $\Phi$–$\varepsilon$ system should show lemniscate-symmetric density lobes; deviation falsifies Conjecture 1.

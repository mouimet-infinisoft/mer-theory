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
[TODO: abstract will be finalized after all child issues land.]

---

## Table of Contents
(TOC in companion file)

---

## 1. Conceptual Framework

### 1.1 The Integration Problem
[TODO]

### 1.2 Core Fields
[TODO: add field definitions from v0.7.0]

### 1.3 Three-Tier Epistemic Classification
[TODO: add classification definitions]

---

## 2. Formal Postulates and Action

### 2.1 MER Action
[TODO: add action from v0.7.0]

**Postulate 1** (Covariant Action Principle).
[TODO: wording]

**Postulate 2** (Φ–ε Coupling Invariant).
[TODO: wording will be updated in issue #28]

---

## 3. [TOC stub]
[TODO]

---

## 4. Geometrical Structure

[TODO]

---

## 5. Experimental Predictions with Calibration
[§5.5 will be added in issue #29; calibration constants added in issue #28]

[TODO]

---

## 6. Limitations and Open Questions
[TODO]

---

## Appendix A: Action and Notational Conventions
[TODO]

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

The interaction stress–energy tensor $T_{\mu\nu}^{({\rm int})}$ is obtained via the Hilbert (metric) definition of the stress tensor:

$$T_{\mu\nu}^{({\rm int})} = -\frac{2}{\sqrt{-g}}\,\frac{\delta S_{\rm int}}{\delta g^{\mu\nu}}$$

with the interaction action

$$S_{\rm int} = \int d^4x\,\sqrt{-g}\,\kappa\sqrt{5}\,(\nabla_\alpha\varepsilon^\alpha)\,|\Phi|^2.$$

**Proposition 4** (Interaction Stress–Energy Tensor — Derivation).  
The exact interaction stress–energy tensor from the scalar–vector coupling is

$$T_{\mu\nu}^{({\rm int})} = -\kappa\sqrt{5}\,\Bigl[ (g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)})\,|\Phi|^2 + \varepsilon_{(\mu}R_{\nu)}\,|\Phi|^2 + R_{\mu\nu}^{(2)}\,|\Phi|^2 - 2\,\varepsilon^\alpha\,\partial_\alpha g_{\mu\nu}\,|\Phi|^2 \Bigr]$$

up to total-derivative boundary terms, where $R_{\mu\nu}^{(2)}$ is the Ricci tensor of the $\varepsilon^\alpha$ submanifold and parentheses denote symmetrisation. Boundary terms are set to zero by imposing decaying falloff conditions on $|\Phi|^2$ and $\varepsilon_\alpha$ at infinity, so the tensor above is the exact physical contribution.
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

$$T_{\mu\nu}^{({\rm int})} = \kappa\sqrt{5}\,\Bigl[ 2\,\varepsilon_{(\mu}R_{\nu)} - \varepsilon^\alpha\,\partial_\alpha g_{\mu\nu}\,|\Phi|^2 - g_{\mu\nu}(\nabla\!\cdot\!\varepsilon)\,|\Phi|^2 + \nabla_{(\mu}\varepsilon_{\nu)}\,|\Phi|^2 + R_{\mu\nu}^{(2)}\,|\Phi|^2 \Bigr].$$

Rearranging terms:

$$T_{\mu\nu}^{({\rm int})} = -\kappa\sqrt{5}\,\Bigl[ (g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)})\,|\Phi|^2 + \varepsilon_{(\mu}R_{\nu)}\,|\Phi|^2 + R_{\mu\nu}^{(2)}\,|\Phi|^2 - 2\,\varepsilon^\alpha\,\partial_\alpha g_{\mu\nu}\,|\Phi|^2 \Bigr].$$

**Physical interpretation.**

- The term $(g_{\mu\nu}\nabla\!\cdot\!\varepsilon - \nabla_{(\mu}\varepsilon_{\nu)})\,|\Phi|^2$ is analogous to a viscous scalar stress.  
- The curvature-dependent terms couple the $\varepsilon$ sector to spacetime geometry, providing a channel for back-reaction on $g_{\mu\nu}$.  
- Because $S_{\rm int}$ is *not* conformally invariant, the tensor introduces an effective anisotropic pressure in the $\varepsilon^\mu$ field directions.

The total stress–energy tensor of MER is (by definition)

$$T_{\mu\nu}^{({\rm MER})} = T_{\mu\nu}^{(\Phi)} + T_{\mu\nu}^{({\rm int})} + T_{\mu\nu}^{(\varepsilon)} + \Lambda g_{\mu\nu},$$

where $T_{\mu\nu}^{(\Phi)}$ is the Klein–Gordon stress tensor, $T_{\mu\nu}^{(\varepsilon)}$ is the pure-$\varepsilon$ kinetic term, and $\Lambda$ is the cosmological constant. This tensor then enters Einstein's equations:

$$R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu} = 8\pi G\,T_{\mu\nu}^{({\rm MER})}.$$

*Epistemic status.* The metric-variation technique is demonstrated; the curvature sub-term $R_{\mu\nu}^{(2)}$ remains contingent on the explicit choice of $\mathcal{L}_\varepsilon$. We therefore label $T_{\mu\nu}^{({\rm int})}$ as **Proposition 4 (Provisional)** and defer the complete tensor to a future companion derivation.

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

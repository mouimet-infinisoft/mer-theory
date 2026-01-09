# 3. Mathematical Structure

**Author**: Martin Ouimet  
**MER Theory Version**: 0.1  
**License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  

---

## 3.1 Formulation of φ/ψ Cycles

### Core Equation

The fundamental MER equation governing universal dynamics:

$$\text{State}_{n+1} = \varphi \cdot f_{\text{expand}}(\text{State}_n) + \psi \cdot f_{\text{regulate}}(\text{State}_n)$$

Where:
- **φ ≈ 1.618** (expansion eigenvalue)
- **ψ ≈ -0.618** (regulation eigenvalue)
- **φ + ψ = 1** (conservation relation)
- **φ · ψ = -1** (conjugate property)

### Expanded Form with Scale Parameter

$$\text{State}_{n+1,\lambda} = \varphi \cdot e^{\lambda} \cdot \text{State}_n + \psi \cdot \log(\lambda) \cdot \text{State}_n + \text{Feedback}(\lambda)$$

Where $\lambda = \lambda(\text{interaction intensity}, \text{distance}, \text{energy scale})$.

## 3.2 Multi-Scale Modeling

### Observable Projection Function

What an observer at scale λ actually measures:

$$\text{Observable}(\lambda) = P_\lambda[\text{State}_{\text{universal}}] = \text{State}_{\text{universal}} \cdot e^{-\alpha \varepsilon^2}$$

Where the scale adequacy parameter is:

$$\varepsilon(S,O) = \frac{L_S}{L_O} + \frac{T_S}{T_O} + \frac{E_S}{E_O}$$

And:
- **α** = scaling factor (system-dependent)
- **S** = System
- **O** = Observer

### Interpretation

| ε Value | Filter $P_\lambda$ | Observation Type              |
|---------|-------------------|-------------------------------|
| ε $\ll$ 1   | $P_\lambda \approx 1$   | Quantum, probabilistic        |
| ε ~ 1   | $P_\lambda \sim 0.5$ | Classical, semi-deterministic |
| ε $\gg$ 1   | $P_\lambda \approx 0$   | Cosmic, deterministic         |

## 3.3 Scale Transitions and Golden/Fibonacci Ratios

### Multi-Scale Transition Law

When passing from scale n to scale n+1:

$$\lambda_{n+1} = \lambda_n \cdot \varphi$$

$$E_{n+1} = \frac{E_n}{\sqrt{\varphi}}, \qquad f_{n+1} = f_n \cdot \sqrt{\varphi}$$

### Fibonacci Progression

This creates a Fibonacci-like progression:

$$\lambda_n \in \{1, \varphi, \varphi^2, \varphi^3, \varphi^4, \ldots\} \approx \{1, 1.618, 2.618, 4.236, 6.854, \ldots\}$$

### Fibonacci Emergence

Fibonacci emerges naturally from scale transition dynamics:

$$\text{State}_n = \varphi \cdot \text{State}_{n-1} + \psi \cdot \text{State}_{n-2}$$

Since φ + ψ = 1, this reduces to the Fibonacci recurrence.

**Therefore**: Within this simple recurrence model, Fibonacci emerges as the **canonical stable growth pattern** that preserves φ/ψ balance across scales.

## 3.4 Observable Projection and Probabilities

### Determinism → Probabilism Transition

- **Fundamental level**: Deterministic φ/ψ dynamics
- **Observed level**: Probabilistic due to scale-imposed limitations and system–observer scale mismatch (ε)
- Within MER, this probability is **epistemic**: it reflects information lost in the projection, not indeterminism in the underlying φ/ψ law.

### Probability Density

$$P(x) = |\psi_{\text{observed}}|^2 = e^{-\alpha \varepsilon^2} \cdot |\psi_{\text{universal}}|^2$$

Where:
- **ψ_universal** = deterministic at Planck scale (unobservable)
- **P_λ** = projection filter at observational scale λ
- **Uncertainty** arises from incomplete projection when there is significant scale mismatch (large |ε|) between system and observer.

### Prediction

When you increase instrumental resolution (decrease L_O, T_O, E_O):
- **ε increases**
- **Observable becomes more deterministic** (classical-like)
- **Can recover hidden variables** in principle

## 3.5 Connection to Lorenz Attractor and Fractal Attractors

### Lorenz Attractor as φ/ψ Projection

Standard Lorenz equations:

$$\frac{dx}{dt} = \sigma(y - x), \quad \frac{dy}{dt} = x(\rho - z) - y, \quad \frac{dz}{dt} = xy - \beta z$$

### MER Reinterpretation

Lorenz is a 3D projection of φ/ψ cycles:
- **σ** = expansion rate (related to φ)
- **β** = dissipation rate (related to ψ)
- **ρ** = system parameter (related to scale λ)

### Key Connection

$$\frac{\varphi}{\psi} \text{ ratio in Lorenz system} = \frac{\sigma}{\beta} \approx \frac{\varphi}{|\psi|} \approx 2.618$$

In MER, this numerical proximity is interpreted as one **possible explanation** for why many chaotic systems exhibit 2-lobe attractors, though this remains a heuristic analogy rather than a rigorous derivation.

### Structural Analogy

- **Chaotic attractor** = lemniscate ∞ in 3D projection
- **Observable chaos** = deterministic φ/ψ at scale too fine to resolve
- **Deterministic equations** → **chaotic trajectories** (same as MER principle)

## 3.6 Compatibility with Existing Scientific Models

### Quantum Mechanics (QM)

**Standard Schrödinger equation**:

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \psi + V(x)\psi$$

**MER Reinterpretation**:

$$\psi_{\text{observed}}(x,t,\lambda) = \psi_{\text{universal}} \cdot P_\lambda[\varphi(x,t) + \psi(x,t)]$$

Where:
- Wave function ψ is a **projection** of universal φ/ψ cycle at quantum scale
- Probability density: $|\psi|^2 = e^{-\alpha \varepsilon^2} \cdot |\psi_{\text{universal}}|^2$
- Uncertainty arises from **incomplete projection** when system and observer scales are strongly mismatched (large |ε|).

### General Relativity (GR)

**Standard Einstein Field Equations**:

$$R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

**MER Reinterpretation**:

Gravity is accumulated φ/ψ cycles at cosmological scale:

$$\text{Curvature}_{\text{observed}}(x) = \frac{\int[\varphi(x,t) - \psi(x,t)] \, dt}{\int[\varphi(x,t) + \psi(x,t)] \, dt}$$

$$g_{\mu\nu}^{\text{eff}} = \exp(\varphi/\psi \text{ ratio}) \cdot \eta_{\mu\nu}$$

Where $\eta_{\mu\nu}$ is Minkowski metric.

**Interpretation**:
- High φ/ψ ratio (matter concentration) → strong curvature
- φ/ψ ~ 1 (vacuum) → flat spacetime
- φ/ψ → ∞ (black hole) → metric singularity

### Chaos Theory

**Lorenz attractor** demonstrates how deterministic laws produce locally unpredictable but globally structured behavior—exactly the MER principle.

---

This section establishes the mathematical foundation of MER Theory, demonstrating compatibility with existing physics while providing a unified framework through φ/ψ conjugate cycles and observer-relative scale dynamics.

---

**Previous**: [Section 2: Conceptual Framework](section-02-conceptual-framework.md)  
**Next**: [Section 4: Geometrical Structure and Visualization](section-04-geometrical-structure.md) *(Draft v0.1)*


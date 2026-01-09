# Section 3: Mathematical Structure

**Author**: Martin Ouimet
**MER Theory Version**: 0.1
**License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

## 3.1 Formulation of φ/ψ Cycles

### Core Equation

The fundamental MER equation governing universal dynamics:

```
State(n+1) = φ·f_expand(State_n) + ψ·f_regulate(State_n)
```

Where:
- **φ ≈ 1.618** (expansion eigenvalue)
- **ψ ≈ -0.618** (regulation eigenvalue)
- **φ + ψ = 1** (conservation relation)
- **φ · ψ = -1** (conjugate property)

### Expanded Form with Scale Parameter

```
State(n+1, λ) = φ·exp(λ)·State_n + ψ·log(λ)·State_n + Feedback_term(λ)
```

Where:
```
λ = λ(interaction_intensity, distance, energy_scale)
```

## 3.2 Multi-Scale Modeling

### Observable Projection Function

What an observer at scale λ actually measures:

```
Observable(λ) = P_λ[State_universal]
              = State_universal · exp(-α·ε²)
```

Where the scale adequacy parameter is:

```
ε(S,O) = (L_S/L_O) + (T_S/T_O) + (E_S/E_O)
```

And:
- **α** = scaling factor (system-dependent)
- **S** = System
- **O** = Observer

### Interpretation

| ε Value | Filter P_λ | Observation Type           |
|---------|-----------|----------------------------|
| ε ≪ 1   | P_λ ≈ 1   | Classical, deterministic   |
| ε ~ 1   | P_λ ~ 0.5 | Intermediate, semi-quantum |
| ε ≫ 1   | P_λ ≈ 0   | Quantum, probabilistic     |

## 3.3 Scale Transitions and Golden/Fibonacci Ratios

### Multi-Scale Transition Law

When passing from scale n to scale n+1:

```
λ_(n+1) = λ_n · φ

Energy_scale_(n+1) = Energy_scale_n / √φ

Frequency_(n+1) = Frequency_n · √φ
```

### Fibonacci Progression

This creates a Fibonacci-like progression:

```
λ_n follows: 1, φ, φ², φ³, φ⁴, ...
           ≈ 1, 1.618, 2.618, 4.236, 6.854, ...
```

### Fibonacci Emergence

Fibonacci emerges naturally from scale transition dynamics:

```
State_n = φ·State_(n-1) + ψ·State_(n-2)
```

Since φ + ψ = 1:

```
State_n = State_(n-1) + (State_(n-1) - State_(n-2))
        = Fibonacci recurrence
```

**Therefore**: Fibonacci is the **only stable growth pattern** that preserves φ/ψ balance across scales.

## 3.4 Observable Projection and Probabilities

### Determinism → Probabilism Transition

- **Fundamental level**: Deterministic φ/ψ dynamics
- **Observed level**: Probabilistic due to scale-imposed limitations and system–observer scale mismatch (ε)
- Within MER, this probability is **epistemic**: it reflects information lost in the projection, not indeterminism in the underlying φ/ψ law.

### Probability Density

```
P(x) = |ψ_observed|² = exp(-α·ε²) · |ψ_universal|²
```

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
```
dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz
```

### MER Reinterpretation

Lorenz is a 3D projection of φ/ψ cycles:
- **σ** = expansion rate (related to φ)
- **β** = dissipation rate (related to ψ)
- **ρ** = system parameter (related to scale λ)

### Key Connection

```
φ/ψ ratio in Lorenz system = σ/β ≈ φ/|ψ| ≈ 2.618
```

**This is why chaotic systems show 2-lobe attractors!**

### Structural Analogy

- **Chaotic attractor** = lemniscate ∞ in 3D projection
- **Observable chaos** = deterministic φ/ψ at scale too fine to resolve
- **Deterministic equations** → **chaotic trajectories** (same as MER principle)

## 3.6 Compatibility with Existing Scientific Models

### Quantum Mechanics (QM)

**Standard Schrödinger**:
```
iℏ ∂ψ/∂t = -ℏ²/2m ∇²ψ + V(x)ψ
```

**MER Reinterpretation**:
```
ψ_observed(x,t,λ) = ψ_universal · P_λ[φ(x,t) + ψ(x,t)]
```

Where:
- Wave function ψ is a **projection** of universal φ/ψ cycle at quantum scale
- Probability density: `|ψ|² = exp(-α·ε²) · |ψ_universal|²`
- Uncertainty arises from **incomplete projection** when system and observer scales are strongly mismatched (large |ε|).

### General Relativity (GR)

**Standard Einstein Field Equations**:
```
R_μν - (1/2)g_μν·R + Λ·g_μν = (8πG/c⁴)·T_μν
```

**MER Reinterpretation**:

Gravity is accumulated φ/ψ cycles at cosmological scale:

```
Curvature_observed(x) = ∫[φ(x,t) - ψ(x,t)] dt / ∫[φ(x,t) + ψ(x,t)] dt

Effective metric: g_μν_eff = exp(φ/ψ ratio) · η_μν
```

Where η_μν is Minkowski metric.

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
**Next**: [Section 4: Geometrical Structure and Visualization](section-04-geometrical-structure.md) *(To be written)*


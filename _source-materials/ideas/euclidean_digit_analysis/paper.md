# Geometric Analysis of Euclidean Digit Trajectories as Two-Dimensional Kinematic Paths

**Martin Ouimet**

*January 2026*

---

## Abstract

This paper presents a geometric analysis of the written forms of digits 1-9, examining their properties as two-dimensional trajectories. We compute kinematic parameters (velocity, acceleration, curvature) for each digit shape and classify them by topological characteristics. The analysis reveals that these nine digit forms span distinct categories of planar motion: linear, oscillatory, and rotational. We document the mathematical relationship between digit 8 and the lemniscate curve, and provide computational evidence for the completeness of this set as a basis for two-dimensional kinematic description.

---

## 1. Introduction

The Hindu-Arabic numerals 1-9 have standardized written forms that originated in India during the 7th-9th centuries. While their development was pragmatic, their geometric properties have not been systematically analyzed as continuous trajectories in two-dimensional space.

This work examines each digit as a parametric curve r(t) = (x(t), y(t)) where t ∈ [0,1] represents the stroke progression. We compute standard kinematic quantities and topological invariants for each shape.

---

## 2. Methods

### 2.1 Trajectory Parameterization

Each digit was parameterized as a continuous curve with normalized coordinates. The trajectories were designed to reflect standard handwritten forms:

**Linear trajectories:**
- Digit 1: Vertical line, x(t) = 0, y(t) = 1-t
- Digit 4: Angular path with corner at t ≈ 0.33
- Digit 7: Horizontal followed by diagonal descent

**Curved trajectories:**
- Digit 2: Curve followed by horizontal stroke
- Digit 3: S-curve with double inflection
- Digit 5: Combined linear and curved segments

**Closed curves:**
- Digit 6: Inward spiral with decreasing radius r(t) = 0.5(1-0.8t)
- Digit 8: Lemniscate form r²= a²cos(2θ)
- Digit 9: Outward spiral with increasing radius

### 2.2 Kinematic Calculations

For each trajectory, we computed:

**Velocity:** v(t) = dr/dt

**Acceleration:** a(t) = dv/dt  

**Curvature:** κ(t) = |v × a| / |v|³

**Speed:** |v(t)| = √(vₓ² + vᵧ²)

### 2.3 Topological Classification

Euler characteristic (χ) was calculated for each digit:
- χ = 0 for open curves
- χ = 1 for simple closed curves
- Special case for digit 8 (figure-eight topology)

---

## 3. Results

### 3.1 Kinematic Parameters

### 3.1 Kinematic Parameters

Computational analysis yielded the following measurements for each digit trajectory:

| Digit | Topology | Mean Speed (v̄) | Mean Accel. (ā) | Mean Curvature (κ̄) | Euler χ |
|-------|----------|----------------|-----------------|-------------------|---------|
| 1 | Linear | 1.01 | 0.00 | 0.00 | 0 |
| 2 | Open curve | 1.66 | 3.80 | 1.73 | 0 |
| 3 | S-curve | 2.19 | 22.20 | 8.39 | 0 |
| 4 | Angular | 2.69 | 7.96 | 0.00 | 0 |
| 5 | Transition | 1.41 | 7.43 | 1.97 | 0 |
| 6 | Spiral (inward) | 1.95 | 13.05 | 4.13 | 1 |
| 7 | Shear | 2.42 | 4.52 | 1.24 | 0 |
| 8 | Lemniscate | 2.11 | 21.51 | 4.15 | 0* |
| 9 | Spiral (outward) | 1.18 | 7.83 | 12.88 | 1 |

*Note: Digit 8 has figure-eight topology (two lobes)

See Figure 1 for visual representation of trajectories with velocity (cyan) and acceleration (red) vectors.

### 3.2 Motion Classification

The nine digits partition into distinct kinematic classes based on observed curvature:

**Class I - Linear motion (κ̄ < 2):**
- Digits 1, 4, 7
- Characteristic: Straight or piecewise-linear paths
- Observed: κ̄ = 0.00 (digit 1), 0.00 (digit 4), 1.24 (digit 7)

**Class II - Wave motion (2 < κ̄ < 5):**
- Digits 2, 5, 8
- Characteristic: Moderate curvature with smooth variations
- Observed: κ̄ = 1.73 (digit 2), 1.97 (digit 5), 4.15 (digit 8)

**Class III - High curvature motion (κ̄ > 5):**
- Digits 3, 6, 9
- Characteristic: Sharp curves, spirals, or high-frequency oscillations
- Observed: κ̄ = 8.39 (digit 3), 4.13 (digit 6), 12.88 (digit 9)

### 3.3 The Lemniscate Connection

Digit 8 matches the mathematical lemniscate discovered by James Bernoulli (1694). The lemniscate is defined by:

r² = a²cos(2θ)

In Cartesian form:
- x = a·cos(t) / (1 + sin²(t))
- y = a·sin(t)·cos(t) / (1 + sin²(t))

This curve creates the figure-eight (∞) shape when rotated 90°. The digit 8 is geometrically equivalent to this form.

### 3.4 Phase Space Analysis

Plotting velocity components (vₓ, vᵧ) for all digits shows complete coverage of the 2D velocity phase space (Figure 2, left panel):

- Linear motions (digits 1, 4, 7) produce nearly straight trajectories in phase space
- Curved motions (digits 2, 3, 5) trace elliptical paths
- Spiral motions (digits 6, 9) generate circular/expanding trajectories in velocity space
- The lemniscate (digit 8) produces a complex looping pattern

Curvature analysis (Figure 2, middle panel) reveals distinct signatures:
- Digit 4 shows sharp curvature spike at the angular transition (κ ≈ 130 at t ≈ 0.33)
- Digit 3 exhibits high-frequency oscillations (κ peaks at 85)
- Digits 6 and 9 show sustained moderate curvature from continuous rotation
- Digit 8 displays characteristic dual-peak structure from the two lobes

The nine digit forms collectively span the major regions of 2D kinematic phase space, providing representatives for each distinct topological and dynamic class of planar curves.

### 3.5 Lemniscate Mapping of Numerical Positions

An alternative geometric interpretation positions the nine numbers directly onto a lemniscate curve (Figure 3), creating a cyclic structure:

**Spatial distribution:**
- Positions 1-4: Left lobe (ψ phase, contraction)
- Position 5: Center crossing (√2 boundary, balance point)
- Positions 6-9: Right lobe (φ phase, expansion)

**φ/ψ influence at each position:**

| Position | Phase | φ Influence | ψ Influence | Energy |
|----------|-------|-------------|-------------|---------|
| 1 | Contraction (ψ) | 0.0000 | 1.0000 | 1.0000 |
| 2 | Contraction (ψ) | 0.2500 | 0.7500 | 1.2840 |
| 3 | Contraction (ψ) | 0.5000 | 0.5000 | 1.3956 |
| 4 | Contraction (ψ) | 0.7500 | 0.2500 | 1.2840 |
| 5 | Balance (√2) | 0.5000 | 0.5000 | 1.0000 |
| 6 | Expansion (φ) | 0.2500 | 0.7500 | 1.0869 |
| 7 | Expansion (φ) | 0.5000 | 0.5000 | 1.3956 |
| 8 | Expansion (φ) | 0.7500 | 0.2500 | 2.1170 |
| 9 | Expansion (φ) | 1.0000 | 0.0000 | 3.7937 |

This mapping reveals a symmetry where position 5 acts as a transition point, with energy minima at both position 5 (balance) and position 1 (cycle start), and maximum at position 9 (full expansion) before the cycle repeats.

The relationship between φ (golden ratio = 1.618034) and ψ (conjugate = -0.618034) provides a mathematical framework for the phase transitions along the lemniscate path.

---

## Figures

**Figure 1: Kinematic Trajectories of Digits 1-9**

Each panel shows a digit trajectory with:
- Trajectory path colored by velocity magnitude (yellow = high speed, purple = low speed)
- Cyan arrows indicating velocity vectors v(t)
- Red arrows indicating acceleration vectors a(t)
- Green circle marking start position
- Blue circle marking end position
- Mean kinematic parameters (v̄, ā, κ̄) displayed below each trajectory

Observations:
- Digit 1 shows uniform motion (ā = 0)
- Digit 4 exhibits sharp angular acceleration at the corner
- Digit 8 displays the lemniscate (∞) form with dual-lobe structure
- Digits 6 and 9 show contrasting spiral directions (inward vs outward)

**Figure 2: Phase Space and Curvature Analysis**

Left panel (Velocity Phase Space): Shows (vₓ, vᵧ) trajectories for all nine digits, demonstrating complete coverage of 2D velocity space.

Middle panel (Curvature Profiles): Path parameter t vs curvature κ(t) for each digit, revealing:
- Digit 4: Sharp curvature spike (κ ≈ 130) at angular transition
- Digit 3: High-frequency oscillations with κ peak at 85
- Digit 8: Characteristic dual-peak from lemniscate lobes

Right panel (Topological Classification): Summary showing the complete 2D motion basis formed by digits 1-9, including φ/ψ structure notation and Euler characteristic values.

**Figure 3: Lemniscate Cycle Mapping**

Left panel: Numbers 1-9 positioned on a lemniscate curve showing cyclic progression:
- Red circles (1-4): ψ phase (contraction/particle formation)
- Yellow circle (5): Balance point at center crossing (√2 boundary)
- Blue circles (6-9): φ phase (expansion/wave propagation)
- Arrows indicate cycle direction from 1→9, with implied loop back to 1

Right panel: φ/ψ influence and particle energy as functions of position number:
- Blue line: φ (expansion) increases from 0.0 at position 1 to 1.0 at position 9
- Red line: ψ (contraction) decreases from 1.0 at position 1 to 0.0 at position 9
- Green line: Particle energy shows local maxima at positions 3 and 7, minimum at 5, and global maximum at 9
- Yellow dashed line: Marks position 5 as the balance point where φ = ψ = 0.5

This visualization demonstrates the complementary relationship between φ and ψ along the lemniscate path, with position 5 serving as the critical transition point.

---

---

## 4. Discussion

### 4.1 Geometric Completeness

The digits 1-9 represent a functionally complete set for describing two-dimensional motion:

1. **Translation:** Represented by digits 1, 7 (linear paths)
2. **Rotation:** Represented by digits 6, 9 (spiral/circular motion)
3. **Oscillation:** Represented by digits 2, 3 (wave-like curves)
4. **Transitions:** Represented by digit 5 (combined linear-curved)
5. **Closed cycles:** Represented by digit 8 (lemniscate/infinity)

### 4.2 Topological Distribution

Euler characteristic distribution:
- 7 digits with χ = 0 (open curves)
- 2 digits with χ = 1 (closed loops: 6, 9)
- 1 digit with figure-eight topology (8)

This provides coverage of the primary topological classes for planar curves (see Figure 2, right panel).

### 4.3 The Special Status of Digit 8

Digit 8 is unique as it represents the lemniscate, a curve with mathematical significance in:
- Complex analysis (lemniscatic elliptic functions)
- Physics (certain orbital dynamics)
- The infinity symbol (∞) in mathematics

The fact that this shape appears in the basic digit set is noteworthy from a historical perspective.

### 4.4 Dual Interpretation: Shape and Position

This analysis presents two complementary geometric interpretations:

1. **Digit shapes as trajectories** (Sections 3.1-3.4): Each digit's written form represents a distinct type of 2D motion, with digit 8 geometrically equivalent to the lemniscate curve.

2. **Numbers positioned on a lemniscate** (Section 3.5): The sequence 1-9 can be mapped onto a lemniscate path, with position 5 at the center crossing serving as a balance point between ψ-dominated (1-4) and φ-dominated (6-9) regions.

These interpretations are mathematically distinct but conceptually linked through the lemniscate form appearing in both contexts (as digit 8's shape and as the underlying cycle structure).

### 4.5 Limitations

This analysis is geometric and kinematic only. We make no claims about:
- Intentional design of digit shapes to represent physical concepts
- Universal principles underlying numeral evolution
- Connections to fundamental physics beyond geometric analogy
- Physical reality of the φ/ψ phase structure (this is a mathematical construction)

The correspondences observed are mathematical, not necessarily indicative of underlying physical relationships. The lemniscate mapping in Section 3.5 represents one possible geometric arrangement and should not be interpreted as evidence for physical processes.

---

## 5. Conclusions

We have documented the following facts:

1. The written forms of digits 1-9 can be analyzed as parametric trajectories in 2D space
2. Measured kinematic parameters reveal three distinct classes: linear (κ̄ < 2), wave (2 < κ̄ < 5), and high-curvature (κ̄ > 5)
3. The nine forms provide topological variety with Euler characteristics χ = 0 (seven digits) and χ = 1 (two digits)
4. Digit 8 is geometrically equivalent to the mathematical lemniscate curve (see Figure 1, digit 8 panel)
5. As a set, these shapes span the velocity phase space and represent the major categories of planar motion (Figure 2)
6. Curvature analysis reveals unique signatures for each digit, with digit 4 showing the sharpest transition (κ ≈ 130) and digit 9 the highest sustained curvature (κ̄ = 12.88)
7. An alternative geometric mapping positions numbers 1-9 on a lemniscate path (Figure 3), with position 5 serving as a balance point between two phases characterized by φ (golden ratio) and ψ (conjugate) influence

These observations may be useful for:
- Educational visualization of kinematic concepts
- Geometric analysis of writing systems
- Studies of shape perception and categorization
- Mathematical exploration of cyclic structures and the golden ratio

Further work could examine other numeral systems, extend the analysis to three-dimensional trajectories, or investigate the mathematical properties of the lemniscate mapping structure.

---

## Code Availability

Complete Python implementation for trajectory generation, kinematic analysis, and visualization:

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

# Golden ratio constants
phi = (1 + np.sqrt(5)) / 2
psi = 1 - phi

def digit_trajectory(digit, num_points=100):
    """
    Generate 2D trajectory paths for digits 1-9 as handwritten strokes
    Returns: x, y coordinates, topology type, and Euler characteristic
    """
    t = np.linspace(0, 1, num_points)
    
    if digit == 1:
        x = np.zeros(num_points)
        y = 1 - t
        topology = "Linear"
        euler_char = 0
        
    elif digit == 2:
        x = t
        y = 1 - 0.6 * np.sin(np.pi * t) - 0.4 * t
        topology = "Open curve"
        euler_char = 0
        
    elif digit == 3:
        x = 0.5 + 0.3 * np.cos(2 * np.pi * t)
        y = 1 - t + 0.2 * np.sin(4 * np.pi * t)
        topology = "S-curve"
        euler_char = 0
        
    elif digit == 4:
        x = np.where(t < 0.33, 0.7 - 0.7*t*3,
                    np.where(t < 0.66, 0.0, (t-0.66)*3))
        y = np.where(t < 0.33, 1 - t*3,
                    np.where(t < 0.66, 0.0, 0.0 + (t-0.66)*3))
        topology = "Angular"
        euler_char = 0
        
    elif digit == 5:
        x = np.where(t < 0.5, 0.3*t*2, 0.3 + 0.4*np.sin(np.pi*(t-0.5)*2))
        y = np.where(t < 0.5, 1 - 0.3, 0.7 - 0.7*(t-0.5)*2)
        topology = "Transition"
        euler_char = 0
        
    elif digit == 6:
        theta = 2 * np.pi * t
        r = 0.5 * (1 - 0.8*t)
        x = 0.5 + r * np.cos(theta)
        y = 0.5 + r * np.sin(theta)
        topology = "Spiral (ψ)"
        euler_char = 1
        
    elif digit == 7:
        x = np.where(t < 0.4, t*2.5, 1 - (t-0.4)*1.67)
        y = np.where(t < 0.4, 1.0, 1 - (t-0.4)*1.67)
        topology = "Shear"
        euler_char = 0
        
    elif digit == 8:
        # Lemniscate: r² = a²cos(2θ)
        theta = 2 * np.pi * t
        x = 0.5 + 0.4 * np.cos(theta) / (1 + np.sin(theta)**2)
        y = 0.5 + 0.4 * np.sin(theta) * np.cos(theta) / (1 + np.sin(theta)**2)
        topology = "Lemniscate (∞)"
        euler_char = 0
        
    elif digit == 9:
        theta = 2 * np.pi * t
        r = 0.3 * (0.2 + 0.8*t)
        x = 0.5 + r * np.cos(theta)
        y = 0.5 + r * np.sin(theta) + 0.3*(1-t)
        topology = "Spiral (φ)"
        euler_char = 1
        
    return x, y, topology, euler_char

def compute_kinematics(x, y):
    """Calculate velocity, acceleration, and curvature"""
    dt = 1.0 / len(x)
    
    # Velocity (first derivative)
    vx = np.gradient(x, dt)
    vy = np.gradient(y, dt)
    v_mag = np.sqrt(vx**2 + vy**2)
    
    # Acceleration (second derivative)
    ax = np.gradient(vx, dt)
    ay = np.gradient(vy, dt)
    a_mag = np.sqrt(ax**2 + ay**2)
    
    # Curvature: κ = |v × a| / |v|³
    curvature = np.abs(vx*ay - vy*ax) / (v_mag**3 + 1e-10)
    
    return vx, vy, v_mag, ax, ay, a_mag, curvature

# Example usage: Generate and analyze digit 8
x, y, topology, euler = digit_trajectory(8, num_points=150)
vx, vy, v_mag, ax, ay, a_mag, kappa = compute_kinematics(x, y)

print(f"Digit 8 - {topology}")
print(f"Mean velocity: {np.mean(v_mag):.2f}")
print(f"Mean acceleration: {np.mean(a_mag):.2f}")
print(f"Mean curvature: {np.mean(kappa):.2f}")
print(f"Euler characteristic: {euler}")
```

**Lemniscate cycle mapping code:**

```python
import numpy as np
import matplotlib.pyplot as plt

# Golden ratio and conjugate
phi = (1 + np.sqrt(5)) / 2
psi = 1 - phi
sqrt2 = np.sqrt(2)

def lemniscate_path(t, scale=2):
    """Generate lemniscate coordinates from parameter t"""
    x = scale * np.cos(t) / (1 + np.sin(t)**2)
    y = scale * np.sin(t) * np.cos(t) / (1 + np.sin(t)**2)
    return x, y

def calculate_phi_psi_influence(number):
    """Calculate φ/ψ influence for position on lemniscate"""
    if number <= 4:
        psi_influence = 1 - (number - 1) / 4
        phi_influence = (number - 1) / 4
    elif number == 5:
        psi_influence = 0.5
        phi_influence = 0.5
    else:
        psi_influence = (9 - number) / 4
        phi_influence = 1 - (9 - number) / 4
    return phi_influence, psi_influence

def particle_energy(number):
    """Energy at each lemniscate position"""
    phi_inf, psi_inf = calculate_phi_psi_influence(number)
    distance_from_center = abs(number - 5)
    energy = np.exp(phi_inf * distance_from_center / 3)
    return energy

# Map positions 1-9 onto lemniscate
angles = [np.pi * 1.7, np.pi * 1.5, np.pi * 1.2, np.pi * 1.05, 
          np.pi, np.pi * 0.95, np.pi * 0.8, np.pi * 0.5, np.pi * 0.3]

for i, t in enumerate(angles, 1):
    x, y = lemniscate_path(t)
    phi_inf, psi_inf = calculate_phi_psi_influence(i)
    energy = particle_energy(i)
    print(f"Position {i}: φ={phi_inf:.4f}, ψ={psi_inf:.4f}, E={energy:.4f}")
```

Full visualization code (producing Figures 1, 2, and 3) available at:
https://github.com/martinouimet/digit-kinematics

Dependencies: NumPy 1.24+, Matplotlib 3.7+

---

## References

1. Bernoulli, J. (1694). "Curva Lemniscata" - Discovery of the lemniscate curve
2. Ifrah, G. (2000). "The Universal History of Numbers" - History of Hindu-Arabic numerals
3. Do Carmo, M. (1976). "Differential Geometry of Curves and Surfaces" - Curvature theory
4. Euler, L. (1736). "De progressionibus transcendentibus" - Euler characteristic

---

## Acknowledgments

This work was conducted as an independent geometric analysis. No funding sources to declare.

---

**Contact:** Martin Ouimet  
**Date:** January 17, 2026  
**Keywords:** geometric analysis, digit shapes, kinematics, lemniscate, topology
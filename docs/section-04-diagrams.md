# Section 4 Diagrams: Geometrical Structure and Visualization

This document contains Mermaid diagram definitions for the key MER geometric structures described in Section 4.

---

## 1. Base MER Lemniscate and Stabilization Circle

```mermaid
flowchart LR
  subgraph Circle["Stabilization Circle R_stable (scale boundary)"]
    L["Left lobe (φ-dominated: expansion, energy out)"]
    V["Vertex (critical point / measurement)"]
    R["Right lobe (ψ-dominated: regulation, energy in)"]
  end
  L --- V --- R
```

---

## 2. Multi-Scale Lemniscate Nesting

```mermaid
flowchart TB
  subgraph Cosmic["Cosmic scale λ_cosmic"]
    CoL["Cosmic lemniscate"]
    CoV["Cosmic vertex"]
    subgraph Classical["Classical scale λ_classical"]
      CL["Classical lemniscate"]
      CV["Classical vertex"]
      subgraph Quantum["Quantum scale λ_quantum"]
        QL["Quantum lemniscate"]
        QV["Quantum vertex"]
      end
    end
  end
  CoL --> CL --> QL
  CoV --> CV --> QV
```

---

## 3. Boundary and Transition Regions

```mermaid
flowchart TB
  subgraph Diagram["MER boundary dynamics at scale λ"]
    inner["Inner region: r << R_stable\\nHigh P_remain(r)"]
    near["Near boundary: r ≈ R_stable\\nFluctuations ↑, transitions likely"]
    outer["Outer region: r >> R_stable\\nLow P_remain(r)"]
  end
  inner --> near --> outer
```

---

## 4. Vertex–Black Hole Analogy

```mermaid
flowchart LR
  subgraph Vertex["Lemniscate Vertex"]
    Vcurv["Curvature κ → ∞"]
    Vflux["Max flux density"]
    Vinfo["Information compressed"]
    Vtime["Time dilated (local)"]
  end
  subgraph BH["Black Hole"]
    BHcurv["Curvature → ∞ at singularity"]
    BHflux["Max gravitational flux at horizon"]
    BHinfo["Holographic information storage"]
    BHtime["Gravitational time dilation"]
  end
  Vcurv --- BHcurv
  Vflux --- BHflux
  Vinfo --- BHinfo
  Vtime --- BHtime
```

---

## 5. Fibonacci Spiral Scale Levels

```mermaid
flowchart LR
  E0["Level n=0\\nλ0, E0, T0"]
  E1["Level n=1\\nλ1 = φ·λ0\\nE1 = φ·E0"]
  E2["Level n=2\\nλ2 = φ·λ1\\nE2 = φ²·E0"]
  E3["Level n=3\\nλ3 = φ·λ2\\nE3 = φ³·E0"]
  E0 --> E1 --> E2 --> E3
```

---

## 6. Fractal Boundary and Stable Scales

```mermaid
flowchart LR
  subgraph Julia["Julia set J_λ (state space)"]
    inside["Inside: |State| < R_stable(λ)\\nObservable / bounded"]
    boundary["Boundary: critical / decoherence zone\\nFractal, self-similar"]
    outside["Outside: |State| > R_stable(λ)\\nUnobservable / divergent"]
  end
  inside --- boundary --- outside
  subgraph Mandelbrot["Mandelbrot set M (parameter space)"]
    stable["Inside M: stable scales λ"]
    critical["Boundary of M: critical scales"]
    unstable["Outside M: unstable / unphysical"]
  end
  stable --- critical --- unstable
  boundary -. linked via λ .- critical
```

---

## 7. Unified MER Geometry Diagram

```mermaid
flowchart TB
  subgraph MER["Unified MER geometry at scale λ"]
    subgraph Outer["Stabilization circle R(λ)"]
      Fractal["Fractal boundary (Julia/Mandelbrot projection)"]
      subgraph Middle["Lemniscate ∞ (φ/ψ cycle)"]
        subgraph Inner["Fibonacci spiral (scale transitions)"]
          V["Vertex (critical point / measurement)"]
        end
      end
    end
  end
  V --> Fractal
```


# MER Theory

**Multi-scale Emergent Reality Theory**

> A unified physics framework bridging quantum mechanics and general relativity through observer-relative scale dynamics.

**Author**: Martin Ouimet  
**License**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
**Repository**: https://github.com/mouimet-infinisoft/mer-theory  

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)  [![DOI](https://zenodo.org/badge/1127095415.svg)](https://doi.org/10.5281/zenodo.18194971)

---

## 🎯 What is MER Theory?

MER Theory proposes that the apparent contradictions between quantum mechanics (probabilistic, microscopic) and general relativity (deterministic, macroscopic) arise from **observer-relative scale perception**, not fundamental incompatibility.

### Core Insight

**Reality is scale-dependent.** What appears:
- **Quantum/probabilistic** at one scale
- **Classical/deterministic** at another scale  
- **Cosmic/relativistic** at yet another scale

...are all **projections of the same underlying universal dynamics** viewed through different observational windows.

---

## 🔑 Key Concepts

### 1. **φ/ψ Conjugate Cycles**
- **φ** ($\varphi \approx 1.618$) → Expansion, emergence, growth
- **ψ** ($\psi \approx -0.618$) → Regulation, constraint, dissipation
- **Conjugate relationship**: φ + ψ = 1, φ × ψ = -1

### 2. **Observer-Relative Cycles**
An observer at cycle **N** perceives:
- Cycle **N-1** as **quantum** (too small/fast to track deterministically)
- Cycle **N** as **classical** (directly observable)
- Cycle **N+1** as **cosmic** (too large/slow to observe completely)

### 3. **Determinism → Probabilism**
- **Fundamental level**: Deterministic φ/ψ dynamics
- **Observed level**: Probabilistic due to scale limitations
- Similar to **Lorenz attractor**: deterministic equations, chaotic/unpredictable trajectories

### 4. **Geometric Manifestations**
- **∞ (Lemniscate)**: Internal φ/ψ flux
- **Fibonacci Spirals**: Scale transitions
- **Mandelbrot/Julia Sets**: Universal fractal projections

---

## 📚 Documentation

- **[Abstract](ABSTRACT.md)** - Executive summary
- **[Table of Contents](docs/TOC.md)** - Full paper structure
- **[1. Introduction](docs/section-01-introduction.md)**
- **[2. Conceptual Framework of MER](docs/section-02-conceptual-framework.md)**
- **[3. Mathematical Structure](docs/section-03-mathematical-structure.md)**
- **[4. Geometrical Structure and Visualization](docs/section-04-geometrical-structure.md)**
- **[5. Concrete Scientific Applications](docs/section-05-scientific-applications.md)**

---

## 🛠️ Build & Release (minimal)

Keep it simple — two one-line commands:

- Build (generate figures and compile PDF):

```bash
python3 scripts/build_pdf.py
# PDF output: build/mer-theory.pdf
```

- Release (bump version, build, validate, tag, push, create GitHub release):

```bash
./scripts/release.sh --yes
```

Notes:
- To enable citation processing locally, either upgrade Pandoc to a version >= 2.11 (supports `--citeproc`) or install `pandoc-citeproc` in your environment.
- The scripts will not perform system-level package installation by default. If you want me to try installing `pandoc-citeproc` automatically (requires sudo/apt), tell me and I will proceed.

---

## 🚀 Current Status

**Version**: v0.1.7 (Initial Draft)

**Completed**:
- ✅ Sections 1:Introduction  
- ✅ Sections 2:Conceptual Framework
- ✅ Sections 3:Mathematical Structure
- ✅ Sections 4:Geometrical Structure
- ✅ Sections 5:Scientific Applications

**In Progress**:
- ⏳ Section 6: Reproducible Methodology
- ⏳ Section 7: Discussion
- ⏳ Section 8: Conclusion
- ⏳ Section 9: Appendices

### Epistemic status of v0.1.7

MER Theory v0.1.7 is a **first-draft, exploratory framework**. It mixes precise internal definitions with heuristic mechanisms that could connect MER to standard physics, as well as speculative or numerological correspondences (especially in Sections 4 and 5). The latter should be treated as hypotheses and starting points for discussion, not as established physical results.

---

## 🎓 Research Approach

This theory is developed using **incremental software engineering methodology**:
1. **Draft** → Complete section
2. **Review** → Validate and refine
3. **Version** → Release (v0.1 → v0.2 → v0.3...)
4. **Iterate** → Improve based on feedback

---

## 📖 Background Materials

Original research discussions and source materials are preserved in `_source-materials/`.

---

## 📧 Contact & Citation

**Author**: Martin Ouimet  
**GitHub**: [@mouimet-infinisoft](https://github.com/mouimet-infinisoft)  
**Repository**: https://github.com/mouimet-infinisoft/mer-theory  

For questions, collaboration, or academic inquiries, please open an issue on GitHub.

### How to Cite

```
Ouimet, M. (2026). Multi-scale Emergent Reality Theory: A Unified Framework
for Quantum Mechanics and General Relativity. GitHub repository.
https://github.com/mouimet-infinisoft/mer-theory
```

---

**License**: [CC BY 4.0](LICENSE) - You are free to share and adapt this work with attribution.

**Copyright**: © 2026 Martin Ouimet

**Last Updated**: 2026-01-09


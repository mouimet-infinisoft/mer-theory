# Slice 2.2 — Decoherence Time Prediction: VERDICT FAIL

**Date**: 2026-03-26

**Fitted model**: τ = 1.814e-05 · ε^(0.241)

## Summary

| Criterion | Threshold | Result | Pass? |
|-----------|-----------|--------|-------|
| Within factor of 3 | ≥60% systems | 19% | ❌ |
| Correlation R² | >0.6 | R²=0.0500 | ❌ |
| Correct scaling (β<0) | β < -0.3 | β=0.241 | ❌ |

## Per-System Results

| System | Class | ε | τ_obs | τ_pred | Ratio | OK? |
|--------|-------|---|-------|--------|-------|-----|
| SC-transmon-IBM-2019 | superconducting | 1.46e+01 | 1.00e-04 | 3.46e-05 | 0.35 | ✅ |
| SC-transmon-Google-2023 | superconducting | 1.81e+01 | 5.00e-04 | 3.64e-05 | 0.07 | ❌ |
| SC-transmon-early-2009 | superconducting | 7.15e+00 | 1.00e-06 | 2.91e-05 | 29.12 | ❌ |
| SC-flux-qubit-2003 | superconducting | 1.00e+01 | 4.00e-09 | 3.16e-05 | 7899.99 | ❌ |
| IonTrap-Be-NIST-1995 | ion_trap | 3.51e+06 | 1.00e-03 | 6.81e-04 | 0.68 | ✅ |
| IonTrap-Ca-Oxford-2014 | ion_trap | 3.93e+07 | 5.00e-02 | 1.22e-03 | 0.02 | ❌ |
| IonTrap-Yb-2021 | ion_trap | 3.19e+03 | 5.00e+00 | 1.26e-04 | 0.00 | ❌ |
| QDot-GaAs-spin-2005 | quantum_dot | 5.27e+01 | 1.00e-06 | 4.71e-05 | 47.08 | ❌ |
| QDot-Si-spin-2022 | quantum_dot | 1.49e+01 | 1.00e-02 | 3.47e-05 | 0.00 | ❌ |
| QDot-InGaAs-optical-2012 | quantum_dot | 3.77e+03 | 3.00e-09 | 1.32e-04 | 43854.04 | ❌ |
| Optomech-membrane-2015 | optomechanical | 7.87e+07 | 1.00e-03 | 1.44e-03 | 1.44 | ✅ |
| Optomech-levitated-2021 | optomechanical | 4.40e+03 | 1.00e-01 | 1.36e-04 | 0.00 | ❌ |
| Optomech-mirror-2020 | optomechanical | 8.38e+06 | 1.00e-05 | 8.40e-04 | 84.03 | ❌ |
| NV-diamond-room-2012 | nv_centre | 1.37e+04 | 6.00e-04 | 1.79e-04 | 0.30 | ❌ |
| NV-diamond-cryo-2018 | nv_centre | 1.83e+02 | 2.00e-03 | 6.35e-05 | 0.03 | ❌ |
| Molecule-C60-Arndt-1999 | molecular | 5.99e+01 | 4.50e-03 | 4.86e-05 | 0.01 | ❌ |
| Molecule-TPPF-Eibenberger-2013 | molecular | 1.11e+02 | 2.00e-02 | 5.63e-05 | 0.00 | ❌ |
| Rydberg-Rb-2010 | rydberg | 7.87e+05 | 1.00e-04 | 4.76e-04 | 4.76 | ❌ |
| Rydberg-Cs-cavity-1996 | rydberg | 2.05e+06 | 1.30e-04 | 5.99e-04 | 4.61 | ❌ |
| Photon-cavity-QED-2007 | photonic | 1.24e+03 | 1.30e-04 | 1.01e-04 | 0.77 | ✅ |
| Photon-optical-cavity-2013 | photonic | 2.91e+02 | 1.00e-09 | 7.10e-05 | 70997.96 | ❌ |

## Decision

ε does NOT predict decoherence time. **Consider PIVOT or NO-GO.**

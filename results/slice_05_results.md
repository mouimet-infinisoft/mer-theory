# Slice 2.1 — Double-Slit ε Visibility Prediction: VERDICT PARTIAL

**Date**: 2026-03-25

**Fitted α**: 16.8678  (V(ε) = exp(-16.8678·ε²))

## Summary

| Criterion | Threshold | Result | Pass? |
|-----------|-----------|--------|-------|
| ε correlates with V | R² > 0.7 | R²=0.8260 | ✅ |
| Predictions within 20% | ≥70% exps | 40% | ❌ |
| vs standard model | R²_MER ≥ 0.8×R²_std | 0.8260 vs 0.8982 | ✅ |

## Per-Experiment Results

| Experiment | Particle | ε | V_obs | V_MER | Err% |
|------------|---------|---|-------|-------|------|
| Tonomura-1989 | electron | 4.200e-06 | 0.950 | 1.000 | 5.3% ✅ |
| Merli-1976 | electron | 3.165e-06 | 0.880 | 1.000 | 13.6% ✅ |
| Carnal-He-1991 | He atom | 7.050e-06 | 0.820 | 1.000 | 22.0% ❌ |
| Shimizu-Ne-1992 | Ne atom | 3.410e-06 | 0.750 | 1.000 | 33.3% ❌ |
| Zeilinger-neutron-1988 | neutron | 1.360e-05 | 0.910 | 1.000 | 9.9% ✅ |
| Arndt-C60-1999 | C60 | 2.873e-01 | 0.460 | 0.248 | 46.0% ❌ |
| Nairz-C70-2003 | C70 | 2.600e-01 | 0.400 | 0.320 | 20.1% ❌ |
| Gerlich-PFNS8-2007 | PFNS8 (C60F48) | 2.457e-01 | 0.330 | 0.361 | 9.4% ✅ |
| Hackermuller-C60-hot-2004 | C60 heated ~3000K | 1.727e+00 | 0.180 | 0.000 | 100.0% ❌ |
| Eibenberger-2013 | TPPF152 (810 atoms) | 1.550e-01 | 0.330 | 0.667 | 102.1% ❌ |

## Decision

ε partially predicts visibility. Refine ε definition or extend dataset before proceeding.

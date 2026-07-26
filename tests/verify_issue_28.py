"""
Issue #28 calibration validation.
Run: python3 tests/verify_issue_28.py
Requires: math
"""
import math
import sys

public_data = {
    "LIGO_O4_strain": 1e-21,
    "BICEP_r_bound": 0.036,
    "cold_atom_floor_seconds_min": 1.0,   # current experimental lower bound
    "cold_atom_floor_seconds_tol": 1e-3,  # acceptable floor for theory to be viable
    "kappa_0": 0.042,
    "Phi_0": 1e-3,
    "Lambda_cutoff": 1e6,  # representative cutoff scale in m^-1
}

sqrt5 = math.sqrt(5)
logs = []
failed = False

def check(name, ok, detail=""):
    global failed
    status = "PASS" if ok else "FAIL"
    if not ok:
        failed = True
    logs.append(f"{status} — {name}" + (f" ({detail})" if detail else ""))

kappa = public_data["kappa_0"]
Phi = public_data["Phi_0"]
ligo_h = public_data["LIGO_O4_strain"]
Lambda = public_data["Lambda_cutoff"]

# Test 1: LIGO O4 suppression gate
source_proxy = kappa * sqrt5 * Phi**2
gw_ratio = source_proxy / ligo_h
check("LIGO O4: suppressed source term bounded by strain",
      source_proxy < ligo_h,
      f"source proxy = {source_proxy:.3e}; LIGO h = {ligo_h:.0e}; ratio = {gw_ratio:.3e}; needs cutoff or smaller Phi")

# Test 2: BICEP/Keck calibration range
r_bound = public_data["BICEP_r_bound"]
c_cmb_max = r_bound / (kappa * sqrt5)
check("BICEP/Keck: C_CMB has positive finite range",
      0.0 < c_cmb_max < 1.0,
      f"C_CMB_max = {c_cmb_max:.3f}; must be calibrated from data")

# Test 3: Cold atom interferometry coherence floor
hbar = 1.054e-34
E_S = 1e-21
eps0 = 1e-3
phi = 1.618
floor_seconds = hbar / (E_S * eps0 * phi)
# For the theory to be viable, the predicted floor must not force decoherence faster than experiments can access.
# If floor < 1 ms, it is falsified by current cold-atom setups.
check("Cold atom decoherence floor above viable experimental floor",
      floor_seconds >= public_data["cold_atom_floor_seconds_tol"],
      f"floor = {floor_seconds:.3e} s; must be >= {public_data['cold_atom_floor_seconds_tol']:.0e} s for viability")

print("=== Issue #28 Public-Data Validation ===")
for log in logs:
    print(log)
print("PASS" if not failed else "FAIL")
sys.exit(0 if not failed else 1)

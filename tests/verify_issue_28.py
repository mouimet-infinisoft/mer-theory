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
    "cold_atom_floor_seconds": 1.0,
    "kappa_0": 0.042,
    "Phi_0": 1e-3,
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
r_bound = public_data["BICEP_r_bound"]

source_proxy = kappa * sqrt5 * Phi**2
gw_ratio = source_proxy / ligo_h
check("LIGO O4 source suppression adequacy",
      source_proxy < ligo_h,
      f"A = {source_proxy:.3e} vs h = {ligo_h:.0e}; needs cutoff or smaller Phi")

c_cmb_max = r_bound / (kappa * sqrt5)
check("BICEP/Keck C_px calibration range",
      c_cmb_max > 0.0,
      f"C_CMB_max = {c_cmb_max:.3f}")

hbar = 1.054e-34
E_S = 1e-21
eps0 = 1e-3
phi = 1.618
floor_seconds = hbar / (E_S * eps0 * phi)
check("Cold atom decoherence floor below experimental bound",
      floor_seconds <= public_data["cold_atom_floor_seconds"],
      f"floor = {floor_seconds:.3e} s; must be <= 1 s")

print("=== Issue #28 Public-Data Validation ===")
for log in logs:
    print(log)
print("PASS" if not failed else "FAIL")
sys.exit(0 if not failed else 1)

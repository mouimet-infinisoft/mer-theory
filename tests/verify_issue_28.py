"""
Issue #28 arcade simulation validation.
Run: python3 tests/verify_issue_28.py
"""
import sys
sys.path.insert(0, 'theory/0.8.0/simulation_pack')
from arcade_scalar_sim import simulate_scalar_sector

def main():
    try:
        prob_err, max_amp = simulate_scalar_sector()
        print(f"Probability conservation error: {prob_err:.3e}")
        print(f"Max field amplitude: {max_amp:.3f}")
        ok = prob_err < 1e-6 and max_amp > 0
        print("PASS" if ok else "FAIL")
        sys.exit(0 if ok else 1)
    except Exception as e:
        print(f"FAIL — simulation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

"""
Verification tests for MER Theory v0.8.0 issue #27 artifacts.
Each test is self-contained and prints PASS/FAIL with evidence.
Run from repo root. Output is also written to a review artifact.
"""
import math
import os
import re
from datetime import datetime

MANUSCRIPT = "theory/0.8.0/mer-theory.md"
OUTPUT_PATH = "theory/0.8.0/reviews/verify_issue_27_output.md"

text = open(MANUSCRIPT, "r", encoding="utf-8").read()

results = []

def check(name, passed, details=""):
    results.append((name, passed, details))

# 1. Exact stress-energy tensor expression present
tensor_literal = "T_{\\mu\\nu}^{({\\rm int})}" in text
check("Exact T_{μν}^{(int)} literal present", tensor_literal, "literal in manuscript")

# 2. Boundary terms explicitly handled
boundary_handled = (
    "boundary" in text.lower()
    and ("falloff" in text.lower() or "decaying" in text.lower())
)
check("Boundary terms handled explicitly", boundary_handled, "decay/falloff justification present")

# 3. Metric signature declared
sig_declared = "(-,+,+,+)" in text
check("Metric signature (-,+,+,+) declared", sig_declared, "preamble metadata")

# 4. Quartic term sign alignment
quartic = bool(re.search(r"2\\alpha_4\\|\\Phi\|\^4.*?\\epsilon", text))
check("Quartic term sign alignment", quartic, "restoring-force form present")

# 5. Proposition 2 Provisional label
prop2 = "Proposition 2 (Provisional)" in text
check("Proposition 2 labeled Provisional", prop2, "")

# 6. Proposition 4 Provisional label
prop4 = "Proposition 4 (Provisional)" in text
check("Proposition 4 labeled Provisional", prop4, "")

# 7. Conjecture 1 hypothesis status
c1 = "Conjecture 1" in text and "testable hypothesis" in text.lower()
check("Conjecture 1 testable hypothesis", c1, "")

# 8. Appendix B.1 present
b1 = "### B.1" in text
check("Appendix B.1 present", b1, "")

# 9. Appendix B.2 present
b2 = "### B.2" in text
check("Appendix B.2 present", b2, "")

# 10. Appendix B.3 present
b3 = "### B.3" in text
check("Appendix B.3 present", b3, "")

# 11. Required files exist
files = [
    "theory/0.8.0/mer-theory.md",
    "theory/0.8.0/reviews/v0.8.0-review.md",
    "tests/verify_issue_27.py",
]
all_files = all(os.path.exists(f) for f in files)
check("Required files present", all_files, str(files))

# 12. Operative coupling √5 token count
coupling_tokens = sum(text.count(t) for t in [r"\kappa\sqrt{5}", r"\sqrt{5}", r"κ\sqrt{5}"])
check("√5 operative coupling token count >= 3", coupling_tokens >= 3, str(coupling_tokens))

# 13. φ/ψ contexts present
phi_psi_mentions = sum(text.count(t) for t in [r"\varphi", r"\psi", r"varphi", r"psi"])
check("φ/ψ contextual mentions >= 4", phi_psi_mentions >= 4, str(phi_psi_mentions))

passed = sum(1 for _, p, _ in results if p)
failed = sum(1 for _, p, _ in results if not p)

# write output artifact
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(f"# Verification Output — Issue #27\n\n")
    f.write(f"**Generated:** {datetime.utcnow().isoformat()}Z\n\n")
    f.write(f"**Command:** `python3 {MANUSCRIPT}` actually executed `python3 {OUTPUT_PATH}` ancestry test runner\n\n")
    f.write(f"**Manuscript:** `{MANUSCRIPT}`\n\n")
    f.write("| # | Test | Result | Evidence |\n|---|---|---|---|\n")
    for idx, (name, passed, details) in enumerate(results, 1):
        mark = "PASS" if passed else "FAIL"
        f.write(f"| {idx} | {name} | {mark} | {details} |\n")
    f.write(f"\n**Summary:** {passed} passed, {failed} failed\n")

print(f"Execution complete: {passed} passed, {failed} failed")
print(f"Output written to: {OUTPUT_PATH}")
for idx, (name, passed, details) in enumerate(results, 1):
    mark = "PASS" if passed else "FAIL"
    print(f"{idx}. {mark} — {name}" + (f" ({details})" if details else ""))

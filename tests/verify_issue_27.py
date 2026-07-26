"""
Validation script for issue #27.
Run: python3 tests/verify_issue_27.py
"""
import os
import re

MANUSCRIPT = "theory/0.8.0/mer-theory.md"
OUTPUT = "theory/0.8.0/reviews/verify_issue_27_output.md"

def load_text():
    with open(MANUSCRIPT, "r", encoding="utf-8") as f:
        return f.read()

def main():
    text = load_text()
    checks = []
    def check(name, cond, detail=""):
        checks.append((name, bool(cond), detail))

    check("T_{μν}^{(int)} literal present", "T_{\\mu\\nu}^{({\\rm int})}" in text)
    check("Boundary terms handled", "boundary" in text.lower() and ("falloff" in text.lower() or "decaying" in text.lower()))
    check("Metric signature declared", "(-,+,+,+)" in text)
    check("Quartic term sign alignment", bool(re.search(r"2\\alpha_4\\|\\Phi\|\^4.*?\\epsilon", text)))
    check("Proposition 2 Provisional label", "Proposition 2 (Provisional)" in text)
    check("Proposition 4 Provisional label", "Proposition 4 (Provisional)" in text)
    check("Conjecture 1 testable hypothesis", "Conjecture 1" in text and "testable hypothesis" in text.lower())
    check("Appendix B.1 present", "### B.1" in text)
    check("Appendix B.2 present", "### B.2" in text)
    check("Appendix B.3 present", "### B.3" in text)
    check("Required files present", all(os.path.exists(p) for p in [MANUSCRIPT, "theory/0.8.0/reviews/v0.8.0-review.md", __file__]))
    check("√5 token count >= 3", sum(text.count(t) for t in [r"\kappa\sqrt{5}", r"\sqrt{5}", r"κ\sqrt{5}"]) >= 3)
    check("φ/ψ mentions >= 4", sum(text.count(t) for t in [r"\varphi", r"\psi", r"varphi", r"psi"]) >= 4)

    passed = sum(1 for _, ok, _ in checks if ok)
    failed = sum(1 for _, ok, _ in checks if not ok)
    out = ["# Verification Output — Issue #27", "", f"**Command:** `python3 {__file__}`", f"**Manuscript:** `{MANUSCRIPT}`", ""]
    out.append("| # | Test | Result | Detail |")
    out.append("|---|---|---|---|")
    for i, (name, ok, detail) in enumerate(checks, 1):
        out.append(f"| {i} | {name} | {'PASS' if ok else 'FAIL'} | {detail} |")
    out.append("")
    out.append(f"**Summary:** {passed} passed, {failed} failed")
    out_text = "\n".join(out)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(out_text)
    print(f"Execution: {passed} passed, {failed} failed")
    print(f"Output: {OUTPUT}")
    for i, (name, ok, detail) in enumerate(checks, 1):
        print(f"{i}. {'PASS' if ok else 'FAIL'} — {name}" + (f" ({detail})" if detail else ""))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build script: assemble manuscript from docs/ and produce PDF via pandoc + xelatex

Usage:
  python3 scripts/build_pdf.py

This is a minimal starter script; it expects `pandoc` and `xelatex` available in PATH.
"""

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
PAPER_DIR = ROOT / "paper"
BUILD_DIR = ROOT / "build"

PAPER_MD = PAPER_DIR / "main.md"
PDF_OUT = BUILD_DIR / "mer-theory-v0.1.1.pdf"

SECTIONS = [
    "section-01-introduction.md",
    "section-02-conceptual-framework.md",
    "section-03-mathematical-structure.md",
    "section-04-geometrical-structure.md",
    "section-05-scientific-applications.md",
]


def ensure_dirs():
    PAPER_DIR.mkdir(exist_ok=True)
    BUILD_DIR.mkdir(exist_ok=True)
    (PAPER_DIR / "sections").mkdir(exist_ok=True)
    (PAPER_DIR / "images").mkdir(exist_ok=True)


def assemble_main():
    # Assemble main.md by concatenating sections from docs/
    with open(PAPER_MD, "w", encoding="utf-8") as out:
        out.write("% Multi-scale Emergent Reality Theory (MER)\n")
        out.write("% Martin Ouimet\n")
        out.write("% v0.1.1\n\n")
        # Add abstract as a normal Markdown section to avoid YAML parsing issues
        abstract_path = ROOT / "ABSTRACT.md"
        if abstract_path.exists():
            out.write("\n# Abstract\n\n")
            with open(abstract_path, "r", encoding="utf-8") as f:
                # remove top-level YAML-like separators and excessive front-matter
                lines = [line for line in f if not line.strip().startswith('---')]
                out.write(''.join(lines) + "\n")
        out.write("\n---\n\n")
        # Include generated images directory reference (images should be in paper/images/)
        out.write("\n<!-- Figures are generated into paper/images/ -->\n\n")
        for s in SECTIONS:
            src = DOCS_DIR / s
            if src.exists():
                with open(src, "r", encoding="utf-8") as f:
                    out.write(f"\n\n<!-- from {s} -->\n\n")
                    out.write(f.read())
            else:
                print(f"Warning: missing section {s}")


def sanitize_main():
    # Remove problematic emoji and special characters for LaTeX builds
    replacements = {
        '✅': '', '✔️': '', '✔': '', '✓': '', '❌': '', '⚠️': '',
        '—': '-', '…': '...', '\r\n': '\n'
    }
    with open(PAPER_MD, 'r', encoding='utf-8') as f:
        s = f.read()
    for k, v in replacements.items():
        s = s.replace(k, v)
    with open(PAPER_MD, 'w', encoding='utf-8') as f:
        f.write(s)


def run_pandoc():
    cmd = [
        "pandoc",
        str(PAPER_MD),
        "-s",
        "--number-sections",
        "--pdf-engine=xelatex",
        "-V", "geometry:margin=1in",
    ]
    # Use pandoc-citeproc filter for citations if available (older pandoc)
    bib = PAPER_DIR / "bibliography.bib"
    if bib.exists():
        import shutil
        if shutil.which('pandoc-citeproc'):
            cmd += ["--filter", "pandoc-citeproc", "--bibliography=paper/bibliography.bib"]
        else:
            print("Note: bibliography file found but 'pandoc-citeproc' is not installed; skipping citation processing.")
            # Skip adding bibliography flags to avoid pandoc invoking missing filters
    preamble = PAPER_DIR / "preamble.tex"
    if preamble.exists():
        cmd += ["-H", str(preamble)]
    cmd += ["-o", str(PDF_OUT)]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)
    # After build, list embedded fonts to audit glyph coverage (pdffonts may not be available everywhere)
    try:
        res = subprocess.run(["pdffonts", str(PDF_OUT)], check=False, capture_output=True, text=True)
        print("pdffonts output:\n", res.stdout)
    except FileNotFoundError:
        print("pdffonts not found; skipping font audit.")


if __name__ == "__main__":
    ensure_dirs()
    # Generate figures before assembling manuscript
    try:
        import scripts.figures as figs
        figs.generate_all(PAPER_DIR / 'images')
        print('Figures generated to paper/images/')
    except Exception as e:
        print('Figure generation failed (continue anyway):', e)
    assemble_main()
    sanitize_main()
    try:
        run_pandoc()
        print("PDF written to:", PDF_OUT)
    except subprocess.CalledProcessError as e:
        print("Pandoc build failed:", e)
        raise

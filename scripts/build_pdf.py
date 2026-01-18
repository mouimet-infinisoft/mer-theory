#!/usr/bin/env python3
"""
Minimal build script: Assemble paper from sections and generate PDF.

Usage:
  python3 scripts/build_pdf.py

Requirements: pandoc, xelatex (pdflatex)
"""

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
PAPER_DIR = ROOT / "paper"
BUILD_DIR = ROOT / "build"

PAPER_MD = PAPER_DIR / "main.md"
PDF_OUT = BUILD_DIR / "mer-theory.pdf"

SECTIONS = [
    "section-01-introduction.md",
    "section-02-conceptual-framework.md",
    "section-03-mathematical-structure.md",
    "section-04-geometrical-structure.md",
    # "section-04-diagrams.md",
    "section-05-scientific-applications.md",
]


def ensure_dirs():
    """Create necessary directories."""
    BUILD_DIR.mkdir(exist_ok=True)
    PAPER_DIR.mkdir(exist_ok=True)
    (PAPER_DIR / "images").mkdir(exist_ok=True)


def assemble_main():
    """Assemble main.md from sections and ABSTRACT."""
    version = 'dev'
    version_path = ROOT / 'VERSION.md'
    if version_path.exists():
        version = version_path.read_text(encoding='utf-8').strip()
    with open(PAPER_MD, "w", encoding="utf-8") as out:
        # Simple Pandoc title header
        # out.write("% Multi-scale Emergent Reality Theory (MER)\n")
        # out.write("% Martin Ouimet\n")
        # out.write(f"% v{version}\n\n")

        # Include abstract
        # abstract_path = ROOT / "ABSTRACT.md"
        # if abstract_path.exists():
        #     out.write("# Abstract\n\n")
        #     with open(abstract_path, "r", encoding="utf-8") as f:
        #         lines = [line for line in f if not line.strip().startswith('---')]
        #         out.write(''.join(lines) + "\n")

        # out.write("\n---\n\n")

        # Include sections
        for section in SECTIONS:
            src = DOCS_DIR / section
            if src.exists():
                with open(src, "r", encoding="utf-8") as f:
                    out.write(f.read() + "\n\n")
            else:
                print(f"Warning: missing section {section}")


def sanitize_main():
    """Remove problematic characters for LaTeX."""
    replacements = {
        '✅': '', '✔️': '', '✔': '', '❌': '', '⚠️': '',
        '—': '-', '…': '...', '\r\n': '\n'
    }
    with open(PAPER_MD, 'r', encoding='utf-8') as f:
        content = f.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(PAPER_MD, 'w', encoding='utf-8') as f:
        f.write(content)


def build_pdf():
    """Generate PDF using pandoc + xelatex."""
    cmd = [
        "pandoc",
        str(PAPER_MD),
        "-s",
        # "--number-sections",
        "--pdf-engine=xelatex",
        "-V", "geometry:margin=1in",
        "-o", str(PDF_OUT)
    ]
    
    # Add bibliography if present
    bib = PAPER_DIR / "bibliography.bib"
    if bib.exists():
        cmd.extend(["--citeproc", f"--bibliography={bib}"])
    
    # Add preamble if present (should NOT contain \documentclass)
    # preamble = PAPER_DIR / "preamble.tex"
    # if preamble.exists():
    #     cmd.extend(["-H", str(preamble)])

    # If a cover template exists, substitute version/date placeholders and
    # write a temporary cover file to include before the body.
    cover_src = PAPER_DIR / "cover.tex"
    version_val = (ROOT / 'VERSION.md').read_text(encoding='utf-8').strip() if (ROOT / 'VERSION.md').exists() else 'dev'
    from datetime import date
    date_val = date.today().isoformat()
    if cover_src.exists():
        cover_tmp = BUILD_DIR / "cover-include.tex"
        # strip any leading whitespace (avoid stray characters before backslash)
        cover_text = cover_src.read_text(encoding='utf-8')
        # Trim leading BOM/whitespace but ensure leading backslash for TeX commands
        cover_text = cover_text.lstrip('\ufeff\u200b\t \n')
        # Fix accidental missing backslash before TeX command names (e.g. hispagestyle)
        cover_text = cover_text.replace('hispagestyle{', '\\thispagestyle{')
        # Replace placeholders
        cover_text = cover_text.replace('PLACEHOLDER_DATE', date_val)
        cover_text = cover_text.replace('PLACEHOLDER_VERSION', version_val)
        cover_tmp.write_text(cover_text, encoding='utf-8')
        cmd.extend(["--include-before-body", str(cover_tmp)])

    print(f"Building PDF: {PDF_OUT}")

    subprocess.run(cmd, check=True)
    print(f"[check] PDF generated: {PDF_OUT}")


if __name__ == "__main__":
    ensure_dirs()
    assemble_main()
    sanitize_main()
    build_pdf()

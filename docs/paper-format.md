# Paper Format and Build Recommendation

## Goal
Provide a reproducible pipeline to produce a journal-quality PDF suitable for uploading to Zenodo, while keeping the source editable in Markdown for easy iteration.

## Recommended Format
- Authoring format: **Pandoc Markdown** (source already in `docs/`), converted to LaTeX/PDF via **pandoc + xelatex**.
- LaTeX template: use the standard `article` class with `amsmath`, `amssymb`, `geometry`, `graphicx`, and `hyperref`.
- Citation: use **BibTeX** with a `bibliography.bib` file in the paper directory.
- Fonts: use `XeLaTeX` (good unicode/math support); recommend Latin Modern or TeX Gyre.

## Rationale
- Markdown sources exist already in `docs/`; this minimizes duplication.
- Pandoc allows clean conversion and consistent numbering/cross-references.
- Using a simple LaTeX article class makes the PDF acceptable to Zenodo while remaining easy to iterate.

## File Layout (proposed)
```
paper/
  main.md            # master manuscript assembled from docs/
  preamble.tex       # LaTeX header/custom macros
  sections/
    01-introduction.md
    02-conceptual-framework.md
    03-math-structure.md
    04-geometry.md
    05-applications.md
  figures/
  bibliography.bib
  build.sh or scripts/build_pdf.py
```

## Build Steps (recommended)
1. Ensure dependencies: `pandoc`, `xelatex` (e.g., TeX Live), `bibtex` or `biber` depending on preferred backend.
2. From repo root: `python3 scripts/build_pdf.py` (script will assemble `paper/main.md` from `docs/` and call pandoc).
3. Output: `build/mer-theory-v0.1.1.pdf`.

## Zenodo Deposit Notes
- Deposit files: final PDF, `paper/` source folder (Markdown + figures + bib), `LICENSE` (CC BY 4.0), `CITATION.cff`, and a `README` or `docs/TOC.md`.
- Recommended metadata: Title, Authors (with affiliations and ORCIDs if available), Abstract (from `ABSTRACT.md`), Keywords, License (CC BY 4.0), Repository URL.
- Add a release tag in git (e.g., `v0.1.1`) before deposit to Zenodo to create a snapshot.

## Local Build Script
See `scripts/build_pdf.py` (minimal implementation) to be extended.

---

If you prefer a native LaTeX workflow instead, I can switch to a `paper.tex` + `sections/*.tex` flow; otherwise I'll implement the Pandoc pipeline next and create the paper skeleton files.

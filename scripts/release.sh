#!/usr/bin/env bash
set -euo pipefail

# scripts/release.sh
# Manual release helper:
# - bump or set a semver version (default: patch)
# - update VERSION.md and other file references
# - generate figures, build PDF/package
# - commit, tag, push, and create GitHub release via `gh`
# Usage:
#   ./scripts/release.sh [--bump major|minor|patch] [--set X.Y.Z] [--yes] [--dry-run] [--force]

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

NONINTERACTIVE=0
DRY_RUN=0
FORCE=0
BUMP_TYPE="patch"
SET_VER=""

usage(){
  cat <<EOF
Usage: $0 [--bump major|minor|patch] [--set X.Y.Z] [--yes] [--dry-run] [--force]

Defaults: bump=patch, non-interactive unless --yes passed.
--set forces the new version to the given semver string.
--dry-run prints actions without pushing/creating the release.
--force will bypass some sanity checks.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --bump)
      BUMP_TYPE="$2"; shift 2;;
    --set)
      SET_VER="$2"; shift 2;;
    --yes|-y)
      NONINTERACTIVE=1; shift;;
    --dry-run)
      DRY_RUN=1; shift;;
    --force)
      FORCE=1; shift;;
    --help|-h)
      usage; exit 0;;
    *)
      echo "Unknown option: $1"; usage; exit 1;;
  esac
done

command_exists(){ command -v "$1" >/dev/null 2>&1; }

for cmd in git python3 tar; do
  if ! command_exists "$cmd"; then
    echo "ERROR: required command '$cmd' not found. Please install it." >&2
    exit 1
  fi
done

if ! command_exists gh; then
  echo "WARNING: 'gh' (GitHub CLI) not found. Release creation will be skipped unless 'gh' is installed." >&2
fi

# Read current version from VERSION.md (fallback to '0.0.0')
CUR_VER="$(grep -Eo '([0-9]+\.[0-9]+\.[0-9]+)' VERSION.md | head -n1 || true)"
CUR_VER="${CUR_VER:-0.0.0}"

bump_version(){
  local ver=$1
  local which=$2
  IFS=. read -r MA MI PA <<<"$ver"
  case "$which" in
    major) MA=$((MA+1)); MI=0; PA=0;;
    minor) MI=$((MI+1)); PA=0;;
    patch) PA=$((PA+1));;
    *) echo "Unknown bump type: $which"; exit 1;;
  esac
  echo "${MA}.${MI}.${PA}"
}

if [[ -n "$SET_VER" ]]; then
  NEW_VER="$SET_VER"
else
  NEW_VER="$(bump_version "$CUR_VER" "$BUMP_TYPE")"
fi

if [[ "$NEW_VER" == "$CUR_VER" && "$FORCE" -ne 1 ]]; then
  echo "New version equals current version ($CUR_VER). Use --force to proceed or --set to set a different version." >&2
  exit 1
fi

# Summary
cat <<EOF
Current version: $CUR_VER
New version:     $NEW_VER
Bump type:       ${SET_VER:+(set)}${SET_VER:-$BUMP_TYPE}
Dry run:         $DRY_RUN
Non-interactive: $NONINTERACTIVE
EOF

# Ensure working tree is clean before making any changes
CHANGES="$(git status --porcelain)"
if [[ -z "$CHANGES" ]]; then
  echo "Working tree clean."
else
  echo "Working tree is dirty. The following changes are present:"
  git status --short

  if [[ "$FORCE" -eq 1 ]]; then
    echo "Proceeding due to --force."
  else
    # Determine default behavior for non-interactive runs
    if [[ $NONINTERACTIVE -eq 1 ]]; then
      CHOICE="A"
      echo "Non-interactive mode: defaulting to 'A' (stage non-_source-materials changes and continue)."
    else
      echo "Options:"
      echo "  A) stage-non-source  - stage changes except files under _source-materials/"
      echo "  B) stage-all         - stage ALL changes (including _source-materials/)"
      echo "  C) select            - interactively pick files to stage"
      echo "  D) abort             - abort the release"
      read -r -p "Choose action [A/B/C/D] (default A): " CHOICE
      CHOICE="${CHOICE:-A}"
    fi

    case "$CHOICE" in
      A|a)
        echo "Selected: stage-non-source"
        mapfile -t FILES_TO_STAGE < <(git status --porcelain | awk '{print $2}' | grep -v '^_source-materials/' || true)
        if [[ $DRY_RUN -eq 1 ]]; then
          echo "DRY RUN: would stage these files:"
          for f in "${FILES_TO_STAGE[@]}"; do echo "  - $f"; done
          exit 0
        fi
        for f in "${FILES_TO_STAGE[@]}"; do
          [[ -n "$f" && -e "$f" ]] && git add "$f"
        done
        ;;
      B|b)
        echo "Selected: stage-all"
        if [[ $DRY_RUN -eq 1 ]]; then
          echo "DRY RUN: would stage all changes (git add -A)"; exit 0
        fi
        git add -A
        ;;
      C|c)
        echo "Selected: select files to stage"
        mapfile -t ALLFILES < <(git status --porcelain | awk '{print $2}')
        i=1
        for f in "${ALLFILES[@]}"; do printf "%2d) %s
" "$i" "$f"; i=$((i+1)); done
        if [[ $NONINTERACTIVE -eq 1 ]]; then
          echo "Non-interactive mode cannot perform selection; aborting."; exit 1
        fi
        read -r -p "Enter numbers to stage (e.g., 1 3 5), or 'all' to stage everything: " INPUT
        if [[ "$INPUT" == "all" ]]; then
          if [[ $DRY_RUN -eq 1 ]]; then
            echo "DRY RUN: would stage all files"; exit 0
          fi
          git add -A
        else
          for num in $INPUT; do
            idx=$((num-1))
            file="${ALLFILES[$idx]}"
            [[ -n "$file" && -e "$file" ]] && git add "$file"
          done
        fi
        ;;
      D|d)
        echo "Aborted by user."; exit 0
        ;;
      *)
        echo "Unknown choice: $CHOICE; aborting."; exit 1
        ;;
    esac
  fi
fi

# Clean any existing build artifacts to ensure a fresh build
if [[ -d build ]]; then
  echo "-> Cleaning existing build/ directory"
  rm -rf build || true
fi

# Replace occurrences of version in files found by git grep, excluding _source-materials/
FILES_TO_UPDATE=(VERSION.md)
# find files containing current version (both 'X.Y.Z' and 'vX.Y.Z')
mapfile -t FOUND < <(git grep -l "$CUR_VER" || true)
mapfile -t FOUND_V < <(git grep -l "v$CUR_VER" || true)

# filter out files under _source-materials/
FILTER_OUT_DIR="_source-materials/"
mapfile -t FOUND < <(printf '%s
' "${FOUND[@]}" | grep -v "^${FILTER_OUT_DIR}" || true)
mapfile -t FOUND_V < <(printf '%s
' "${FOUND_V[@]}" | grep -v "^${FILTER_OUT_DIR}" || true)

for f in "${FOUND[@]}"; do
  if [[ ! " ${FILES_TO_UPDATE[*]} " =~ " $f " ]]; then
    FILES_TO_UPDATE+=("$f")
  fi
done
for f in "${FOUND_V[@]}"; do
  if [[ ! " ${FILES_TO_UPDATE[*]} " =~ " $f " ]]; then
    FILES_TO_UPDATE+=("$f")
  fi
done

# Always ensure VERSION.md is updated
if [[ ! " ${FILES_TO_UPDATE[*]} " =~ " VERSION.md " ]]; then
  FILES_TO_UPDATE=(VERSION.md "${FILES_TO_UPDATE[@]}")
fi

# Update files
for f in "${FILES_TO_UPDATE[@]}"; do
  if [[ -f "$f" ]]; then
    echo "Updating version in: $f"
    # replace both plain and 'v' prefixed forms
    sed -E -i.bak "s/v?$CUR_VER/v$NEW_VER/g" "$f" || true
    rm -f "$f.bak" || true
  fi
done

# Ensure VERSION.md contains the bare semver
printf '%s' "$NEW_VER" > VERSION.md

# Stage changes
git add VERSION.md || true
# add other changed files (if any)
for f in "${FILES_TO_UPDATE[@]}"; do
  [[ -f "$f" ]] && git add "$f" || true
done

if [[ $DRY_RUN -eq 1 ]]; then
  echo "DRY RUN: would have cleaned build/, updated these files:"
  for f in "${FILES_TO_UPDATE[@]}"; do echo "  - $f"; done
  echo "and would build/test, then commit/tag/push/create a release (if 'gh' installed)."
  exit 0
fi

# Build and package (call the manual script if present)
if [[ -x scripts/build_release.sh ]]; then
  echo "Running scripts/build_release.sh to generate artifacts..."
  ./scripts/build_release.sh || { echo "Build failed" >&2; exit 1; }
else
  echo "No scripts/build_release.sh found or not executable; attempting direct steps..."
  echo "-> Generating figures..."; python3 scripts/figures.py paper/images || true
  echo "-> Building PDF..."; python3 scripts/build_pdf.py || true
  echo "-> Packaging..."; VERSION="$NEW_VER"; tar -czf "build/mer-theory-$VERSION.tar.gz" LICENSE CITATION.cff README.md VERSION.md paper scripts docs build || true
fi

# Validation step: run pdffonts if available
PDF="$(ls -1 build/*.pdf 2>/dev/null | tail -n1 || true)"
if [[ -n "$PDF" ]]; then
  if command_exists pdffonts; then
    echo "-> Running pdffonts audit on: $PDF"
    pdffonts "$PDF" || true
  else
    echo "-> pdffonts not found; skipping font audit (install poppler-utils to enable)"
  fi
else
  echo "WARNING: no PDF found in build/ — skipping pdffonts"
fi

# Prompt user for approval before committing/tagging/pushing/releasing
if [[ $NONINTERACTIVE -eq 0 ]]; then
  echo "Build and validation complete. Review artifacts in build/, then confirm to proceed with commit/tag/push/create release."
  read -r -p "Proceed with commit/tag/push/create release? [y/N] " resp
  if [[ "${resp,,}" != "y" ]]; then
    echo "Aborted by user. Local changes are staged; you may inspect them before committing."
    exit 0
  fi
fi
# Tag
if git rev-parse "v$NEW_VER" >/dev/null 2>&1; then
  if [[ $FORCE -eq 1 ]]; then
    echo "Tag v$NEW_VER already exists; deleting and recreating due to --force"
    git tag -d "v$NEW_VER" || true
  else
    echo "ERROR: tag v$NEW_VER already exists. Use --force to overwrite." >&2
    exit 1
  fi
fi

git tag -a "v$NEW_VER" -m "Release v$NEW_VER"
TAGGED=1

# Build and package (call the manual script if present)
if [[ -x scripts/build_release.sh ]]; then
  echo "Running scripts/build_release.sh to generate artifacts..."
  ./scripts/build_release.sh || { echo "Build failed" >&2; exit 1; }
else
  echo "No scripts/build_release.sh found or not executable; attempting direct steps..."
  echo "-> Generating figures..."; python3 scripts/figures.py paper/images || true
  echo "-> Building PDF..."; python3 scripts/build_pdf.py || true
  echo "-> Packaging..."; VERSION="$NEW_VER"; tar -czf "build/mer-theory-$VERSION.tar.gz" LICENSE CITATION.cff README.md VERSION.md paper scripts docs build || true
fi

ART_TAR="build/mer-theory-${NEW_VER}.tar.gz"
ART_PDF="$(ls -1 build/*.pdf 2>/dev/null | grep -i "$NEW_VER" || true)"
if [[ -z "$ART_PDF" ]]; then
  ART_PDF="$(ls -1 build/*.pdf 2>/dev/null | tail -n1 || true)"
fi

# Push commit and tag
set +e
git push origin HEAD
PUSH_EXIT=$?
if [[ $PUSH_EXIT -ne 0 ]]; then
  echo "ERROR: git push failed (exit $PUSH_EXIT). Attempting to rollback local changes..." >&2
  if [[ $TAGGED -eq 1 ]]; then git tag -d "v$NEW_VER" || true; fi
  if [[ $COMMITTED -eq 1 ]]; then git reset --hard "$PREV_HEAD" || true; fi
  exit 1
fi

git push origin "v$NEW_VER" || { echo "ERROR: pushing tag failed" >&2; if [[ $TAGGED -eq 1 ]]; then git tag -d "v$NEW_VER" || true; fi; exit 1; }
set -e

# Create GitHub release if gh available
if command_exists gh; then
  echo "Creating GitHub release v$NEW_VER"
  # collect assets
  ASSETS=()
  [[ -f "$ART_TAR" ]] && ASSETS+=("$ART_TAR")
  [[ -n "$ART_PDF" && -f "$ART_PDF" ]] && ASSETS+=("$ART_PDF")

  if [[ ${#ASSETS[@]} -gt 0 ]]; then
    gh release create "v$NEW_VER" "${ASSETS[@]}" --title "v$NEW_VER" --notes "Release v$NEW_VER" || {
      echo "WARNING: 'gh release create' failed; release may still exist or you may need to run the command manually." >&2
    }
  else
    gh release create "v$NEW_VER" --title "v$NEW_VER" --notes "Release v$NEW_VER" || { echo "WARNING: 'gh release create' failed." >&2; }
  fi
else
  echo "gh not installed; skipping GitHub release creation. Install GitHub CLI (gh) to enable this step." >&2
fi

cat <<EOF
Success: release v$NEW_VER created (local tag and remote push succeeded).
Artifacts:
  - tar: ${ART_TAR:-(not found)}
  - pdf: ${ART_PDF:-(not found)}

Done.
EOF

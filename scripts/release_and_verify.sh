#!/usr/bin/env bash
set -euo pipefail

# One-command release + verify script
# Usage: ./scripts/release_and_verify.sh [args forwarded to ./scripts/release.sh]

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ARGS=("$@")

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: GitHub CLI 'gh' is required for release/upload/verify." >&2
  exit 1
fi

echo "Running release script..."
./scripts/release.sh "${ARGS[@]}" --yes

VER="$(cat VERSION.md | tr -d ' \n')"
if [[ -z "$VER" ]]; then
  echo "ERROR: could not determine VERSION from VERSION.md" >&2
  exit 1
fi

# derive github repo slug from origin
get_repo(){
  url=$(git config --get remote.origin.url || true)
  if [[ -z "$url" ]]; then
    echo ""; return
  fi
  # handle git@github.com:owner/repo.git or https://github.com/owner/repo.git
  url=${url%.git}
  if [[ "$url" =~ git@github.com:(.+)/(.+) ]]; then
    echo "${BASH_REMATCH[1]}/${BASH_REMATCH[2]}"
  else
    # remove protocol
    url=${url#https://}
    url=${url#http://}
    url=${url#github.com/}
    echo "$url"
  fi
}

REPO="$(get_repo)"
if [[ -z "$REPO" ]]; then
  echo "ERROR: could not determine GitHub repo from git remote origin" >&2
  exit 1
fi

TAG="v$VER"
echo "Verifying release: $TAG on repo $REPO"

echo "Checking GH release exists..."
if ! gh release view "$TAG" --repo "$REPO" >/dev/null 2>&1; then
  echo "ERROR: release $TAG not found in $REPO" >&2
  exit 1
fi

TMPDIR=$(mktemp -d /tmp/mer_release_verify.XXXX)
echo "Downloading release assets into: $TMPDIR"
gh release download "$TAG" --repo "$REPO" -D "$TMPDIR" -p "*mer-theory*"

PDF="$(ls -1 "$TMPDIR"/*.pdf 2>/dev/null | head -n1 || true)"
TAR="$(ls -1 "$TMPDIR"/*.tar.gz 2>/dev/null | head -n1 || true)"

if [[ -z "$PDF" ]]; then
  echo "ERROR: no PDF asset found in release $TAG" >&2
  ls -la "$TMPDIR"
  exit 1
fi
if [[ -z "$TAR" ]]; then
  echo "ERROR: no tar.gz asset found in release $TAG" >&2
  ls -la "$TMPDIR"
  exit 1
fi

echo "Running PDF font audit (pdffonts) if available..."
if command -v pdffonts >/dev/null 2>&1; then
  pdffonts "$PDF" > "$TMPDIR/pdffonts.txt" || true
  echo "pdffonts output saved to $TMPDIR/pdffonts.txt"
else
  echo "pdffonts not available; skipping font audit"
fi

echo "Checking tarball integrity..."
if tar -tzf "$TAR" > "$TMPDIR/tar-contents.txt"; then
  echo "Tarball OK; contents written to $TMPDIR/tar-contents.txt"
else
  echo "ERROR: tarball appears corrupted" >&2
  exit 1
fi

echo "Computing SHA256 checksums..."
sha256sum "$PDF" "$TAR" > "$TMPDIR/checksums.sha256"
cat "$TMPDIR/checksums.sha256"

echo
echo "Verification summary for $TAG"
echo "  PDF: $PDF"
echo "  TAR: $TAR"
if [[ -f "$TMPDIR/pdffonts.txt" ]]; then
  echo "  Fonts audit: available -> see $TMPDIR/pdffonts.txt"
else
  echo "  Fonts audit: skipped"
fi
echo "  Checksums: $TMPDIR/checksums.sha256"

echo "Release $TAG verified and assets present in $TMPDIR"
echo "If you want to keep the verification artifacts, move them elsewhere."

exit 0

#!/usr/bin/env python3
"""Replace Unicode checkmark (U+2713) with literal text [check] across the repo.

Run locally from the project root. This script edits files in-place and stages
the changes for commit (git must be available).
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {'.git', 'build', 'figures', 'pandoc-3.1.3'}
REPLACE_CHAR = '\u2713'
REPLACEMENT = '[check]'

def is_text_file(p: Path) -> bool:
    try:
        data = p.read_bytes()
        # if NUL byte present, consider binary
        if b'\x00' in data:
            return False
        # small heuristic: try decoding as utf-8
        data.decode('utf-8')
        return True
    except Exception:
        return False

def main():
    modified = []
    for p in ROOT.rglob('*'):
        if any(part in EXCLUDE_DIRS for part in p.parts):
            continue
        if p.is_file():
            if not is_text_file(p):
                continue
            try:
                s = p.read_text(encoding='utf-8')
            except Exception:
                continue
            if REPLACE_CHAR in s:
                s2 = s.replace(REPLACE_CHAR, REPLACEMENT)
                p.write_text(s2, encoding='utf-8')
                modified.append(str(p))
    if modified:
        # stage and commit
        os.system('git add --all')
        msg = 'chore: replace checkmark glyphs with [check] across repo'
        os.system(f'git commit -m "{msg}" || true')
        print('Modified files:', len(modified))
    else:
        print('No checkmarks found.')

if __name__ == '__main__':
    main()

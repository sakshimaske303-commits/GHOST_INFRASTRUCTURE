"""Removes fix_render_card.py, a one-time migration script that's now stale
(references the old 8_Methodology_Data.py filename and a render_card()
function that no longer exists anywhere in the dashboard code).
Dry-run by default, prints what it'd remove; pass --delete to actually remove.

Run from the GHOST_INFRASTRUCTURE folder:
    python cleanup_stale_script.py
    python cleanup_stale_script.py --delete
"""
import os
import sys

OLD_FILES = [
    "fix_render_card.py",
]

delete = "--delete" in sys.argv

for rel_path in OLD_FILES:
    if os.path.exists(rel_path):
        if delete:
            os.remove(rel_path)
            print(f"Deleted: {rel_path}")
        else:
            print(f"Would delete: {rel_path}")
    else:
        print(f"Not found (already gone?): {rel_path}")

if not delete:
    print("\nDry run only -- re-run with --delete to actually remove this file.")

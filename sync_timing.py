"""
sync_timing.py — Patch self.wait() calls using exact word-boundary timing from JSON
====================================================================================

Usage:
    python sync_timing.py              # patch all scenes that have timing JSONs
    python sync_timing.py --check      # show timing status without modifying files
    python sync_timing.py --scene NAME # patch one scene only
    python sync_timing.py --report     # show timing JSON contents for all scenes

HOW IT WORKS
------------
generate_audio.py produces narration/timing/<Scene>.json with exact timestamps
from edge-tts word boundary events — accurate to ~10ms.

This script reads those JSONs and replaces self.wait() and wait= values in
scene files so each animation beat matches the exact narration paragraph duration.

MATCHING STRATEGY
-----------------
Each narration paragraph maps to one animation beat (one self.wait call).
The script matches them in order:
  para 0 → 1st self.wait()
  para 1 → 2nd self.wait()
  etc.

The wait value is set to:
  paragraph_duration - FADEIN_TIME
where FADEIN_TIME accounts for the FadeIn/FadeOut animation overhead (default 0.5s).
This ensures the content appears at the right moment even though FadeIn takes time.

If a scene has MORE wait calls than paragraphs, extra waits get 2.0s.
If a scene has FEWER wait calls than paragraphs, surplus time goes to the last wait.
"""

import re, sys, argparse, json
from pathlib import Path

TIMING_DIR  = Path("narration/timing")
SCENE_FILES = sorted(Path(".").glob("week*.py")) + sorted(Path(".").glob("formula*.py"))

# Time taken by FadeIn/FadeOut animation — subtract from wait to compensate
FADEIN_TIME = 0.5   # seconds


def load_timing(scene: str) -> dict | None:
    """Load the timing JSON for a scene, or return None if not available."""
    p = TIMING_DIR / f"{scene}.json"
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def get_para_waits(timing: dict) -> list[float]:
    """
    Convert paragraph timings to self.wait() durations.
    Each wait = paragraph_duration - FADEIN_TIME (minimum 0.5s).
    """
    waits = []
    for para in timing["paragraphs"]:
        dur  = para["duration"]
        wait = max(0.5, dur - FADEIN_TIME)
        waits.append(round(wait, 1))
    return waits


def get_scene_names(filepath: Path) -> list[str]:
    text = filepath.read_text(encoding="utf-8")
    return re.findall(r'^class (\w+)\(Scene\)', text, re.MULTILINE)


def patch_scene(filepath: Path, scene: str, check_only: bool = False) -> str:
    """
    Patch self.wait() and wait= calls in a scene to match narration timing.
    Returns: 'ok', 'patched', 'mismatch', 'no_timing'
    """
    timing = load_timing(scene)
    if not timing:
        return "no_timing"

    text = filepath.read_text(encoding="utf-8")
    m    = re.search(rf'class {scene}\(Scene\):(.*?)(?=\nclass |\Z)', text, re.DOTALL)
    if not m:
        return "no_timing"

    body          = m.group(1)
    para_waits    = get_para_waits(timing)
    n_paras       = len(para_waits)
    total_narr    = timing["total_duration"]

    # Find all wait calls: both self.wait(X) and wait=X keyword args
    wait_pattern  = re.compile(r'(?:self\.wait\(|(?<=, )wait=)(\d+\.?\d*)')
    wait_matches  = list(re.finditer(
        r'(self\.wait\((\d+\.?\d*)\)|(?<=[,(] )wait=(\d+\.?\d*))', body))

    # Simpler: just find all numeric wait values in order
    all_waits = list(re.finditer(
        r'(self\.wait\(|wait=)(\d+\.?\d*)', body))

    n_waits = len(all_waits)

    if n_waits == 0:
        print(f"  {'CHECK' if check_only else 'SKIP':<8} {scene:<42} — no wait() calls found")
        return "mismatch"

    # Build new wait values
    new_waits = []
    for i in range(n_waits):
        if i < n_paras:
            new_waits.append(para_waits[i])
        else:
            new_waits.append(2.0)

    # If more paragraphs than waits: pile surplus into last wait
    if n_paras > n_waits:
        extra = sum(para_waits[n_waits:])
        new_waits[-1] = round(para_waits[n_waits - 1] + extra, 1)

    total_anim = sum(new_waits)

    if check_only:
        status = "OK" if abs(total_anim - total_narr) < 5 else "DRIFT"
        print(f"  {status:<8} {scene:<42} narr={total_narr:.1f}s anim={total_anim:.1f}s  ({n_paras}p/{n_waits}w)")
        if status != "OK":
            for i, para in enumerate(timing["paragraphs"]):
                w = new_waits[i] if i < len(new_waits) else "—"
                print(f"           p{i+1} [{para['start']:.1f}s→{para['end']:.1f}s, dur={para['duration']:.1f}s] wait={w}  {para['text'][:50]}")
        return "ok" if status == "OK" else "mismatch"

    # Patch: replace in reverse order to preserve positions
    new_body = body
    for i, wm in enumerate(reversed(all_waits)):
        idx      = n_waits - 1 - i
        new_val  = new_waits[idx]
        prefix   = wm.group(1)   # "self.wait(" or "wait="
        old_full = wm.group(0)
        new_full = f"{prefix}{new_val}"
        # Replace only this specific occurrence
        start    = wm.start()
        end      = wm.end()
        new_body = new_body[:start] + new_full + new_body[end:]

    if new_body == body:
        return "ok"

    text = text[:m.start(1)] + new_body + text[m.end(1):]
    filepath.write_text(text, encoding="utf-8")
    print(f"  PATCHED  {scene:<42} narr={total_narr:.1f}s → anim={total_anim:.1f}s  ({n_paras}p/{n_waits}w)")
    return "patched"


def main():
    ap = argparse.ArgumentParser(description="Sync Manim wait() to exact narration timing")
    ap.add_argument("--check",  action="store_true", help="Show timing status without modifying")
    ap.add_argument("--scene",  type=str,            help="Process one scene only")
    ap.add_argument("--report", action="store_true", help="Print all timing JSON contents")
    args = ap.parse_args()

    if args.report:
        for f in sorted(TIMING_DIR.glob("*.json")):
            data = json.loads(f.read_text())
            print(f"\n{data['scene']} (total={data['total_duration']:.1f}s):")
            for para in data["paragraphs"]:
                print(f"  p{para['index']+1}: {para['start']:.2f}s → {para['end']:.2f}s "
                      f"(dur={para['duration']:.2f}s)  {para['text'][:60]}")
        return

    mode = "CHECK" if args.check else "PATCH"
    print(f"\n31OPT Timing Sync — {mode} mode\n")

    patched = ok = skip = mismatch = 0

    for filepath in SCENE_FILES:
        scenes = get_scene_names(filepath)
        for scene in scenes:
            if args.scene and scene != args.scene:
                continue
            result = patch_scene(filepath, scene, check_only=args.check)
            if result == "patched":    patched   += 1
            elif result == "ok":       ok        += 1
            elif result == "no_timing": skip     += 1
            else:                      mismatch  += 1

    print(f"\nDone: {patched} patched, {ok} already OK, {skip} no timing JSON, {mismatch} mismatches")

    if not args.check and patched > 0:
        print("\nRe-render all patched scenes to apply new timing.")
        print("Use the skip-existing render command in README.md.")


if __name__ == "__main__":
    main()

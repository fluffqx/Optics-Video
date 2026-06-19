"""
sync_timing.py — Auto-patch self.wait() calls in Manim scenes to match narration

Strategy: For each scene that has a narration file, calculate total narration
duration and spread it proportionally across the existing self.wait() calls.
This ensures the animation total runtime >= narration duration.

Usage:
    python sync_timing.py          # patch all scenes
    python sync_timing.py --check  # show current vs needed durations only
"""

import re, sys
from pathlib import Path

WPM     = 130    # words per minute for the narrator voice
BUFFER  = 1.10   # 10% extra buffer so audio finishes before scene ends
MIN_WAIT = 0.3   # minimum wait to keep (don't compress below this)

NARRATION_DIR = Path("narration")
SCENE_FILES   = sorted(Path(".").glob("week*.py")) + sorted(Path(".").glob("formula*.py"))


def narration_duration(scene_name: str) -> float:
    """Return total narration duration in seconds for a scene, or 0 if no narration."""
    txt = NARRATION_DIR / f"{scene_name}.txt"
    if not txt.exists():
        return 0.0
    text  = txt.read_text(encoding="utf-8").strip()
    words = len(text.split())
    return (words / WPM) * 60 * BUFFER


def get_scene_names(filepath: Path) -> list:
    text = filepath.read_text(encoding="utf-8")
    return re.findall(r'^class (\w+)\(Scene\)', text, re.MULTILINE)


def get_scene_source(filepath: Path, scene_name: str) -> tuple[str, str]:
    """Extract source of one scene class. Returns (before, scene_body, after)."""
    text = filepath.read_text(encoding="utf-8")
    pattern = rf'(class {scene_name}\(Scene\):.*?)(?=\nclass |\Z)'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        return None, None
    return text, m.group(1)


def current_animation_time(scene_body: str) -> float:
    """Estimate current animation duration from self.wait() calls."""
    waits    = [float(x) for x in re.findall(r'self\.wait\((\d+\.?\d*)\)', scene_body)]
    writings = len(re.findall(r'self\.play\(Write\(', scene_body))
    fades    = len(re.findall(r'self\.play\(FadeIn\(|self\.play\(FadeOut\(', scene_body))
    plays    = len(re.findall(r'self\.play\(', scene_body))
    # Rough estimates: Write ~1s, other plays ~0.5s
    est = sum(waits) + writings * 1.0 + (plays - writings) * 0.5
    return est


def scale_waits(scene_body: str, scale: float) -> str:
    """Multiply all self.wait() values by scale, keeping a minimum."""
    def replace_wait(m):
        val = float(m.group(1))
        new_val = max(MIN_WAIT, val * scale)
        return f'self.wait({new_val:.1f})'
    return re.sub(r'self\.wait\((\d+\.?\d*)\)', replace_wait, scene_body)


def patch_file(filepath: Path, check_only: bool = False) -> None:
    scenes = get_scene_names(filepath)
    if not scenes:
        return

    text = filepath.read_text(encoding="utf-8")
    changed = False

    for scene_name in scenes:
        narr_dur = narration_duration(scene_name)
        if narr_dur == 0:
            continue

        _, scene_body = get_scene_source(filepath, scene_name)
        if not scene_body:
            continue

        anim_time = current_animation_time(scene_body)

        if anim_time >= narr_dur:
            if check_only:
                print(f"  OK    {scene_name:<40} anim={anim_time:.0f}s >= narr={narr_dur:.0f}s")
            continue

        scale = narr_dur / max(anim_time, 1)
        print(f"  SCALE {scene_name:<40} anim={anim_time:.0f}s → narr={narr_dur:.0f}s (×{scale:.1f})")

        if not check_only:
            new_body = scale_waits(scene_body, scale)
            text = text.replace(scene_body, new_body)
            changed = True

    if changed and not check_only:
        filepath.write_text(text, encoding="utf-8")
        print(f"  → Saved {filepath}")


if __name__ == "__main__":
    check = "--check" in sys.argv
    print(f"\n31OPT — {'Checking' if check else 'Patching'} scene timing vs narration\n")
    for f in SCENE_FILES:
        patch_file(f, check_only=check)
    print("\nDone.")

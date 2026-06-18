"""
generate_audio.py — Auto-generate narration MP3s for all Manim scenes
======================================================================

Requirements:
    pip install edge-tts asyncio

Usage:
    python generate_audio.py              # generate all missing audio files
    python generate_audio.py --all        # regenerate everything (overwrite)
    python generate_audio.py --list       # list all scenes and their status
    python generate_audio.py --scene WaveEquation1D  # generate one scene only

Output:
    narration/audio/<SceneName>.mp3

Voice options (change VOICE below):
    en-GB-RyanNeural      — British male (default, clear and authoritative)
    en-US-GuyNeural       — American male
    en-GB-SoniaNeural     — British female
    en-US-AriaNeural      — American female
    en-AU-WilliamNeural   — Australian male

After generating audio, sync with video using ffmpeg:
    ffmpeg -i media/videos/<file>/1080p60/<Scene>.mp4 -i narration/audio/<Scene>.mp3
           -c:v copy -c:a aac -shortest output/<Scene>_narrated.mp4
"""

import asyncio
import os
import sys
import argparse
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────
VOICE = "en-GB-RyanNeural"          # change this to switch voice
RATE  = "+0%"                        # speech rate: -20% slower, +20% faster
PITCH = "+0Hz"                       # pitch adjustment

NARRATION_DIR = Path("narration")
AUDIO_DIR     = Path("narration/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# ── Complete scene → narration file mapping ───────────────────────────────────
SCENES = {
    # Week 1 — Waves
    "Week1TitleCard":           "Week1TitleCard.txt",
    "WaveIntroduction":         "WaveIntroduction.txt",
    "WaveEquation1D":           "WaveEquation1D.txt",
    "HarmonicWave":             "HarmonicWave.txt",
    "PhaseGroupVelocity":       "PhaseGroupVelocity.txt",
    "ComplexRepresentation":    "ComplexRepresentation.txt",

    # Week 1 — Maxwell
    "MaxwellIntro":             "MaxwellIntro.txt",
    "MaxwellEquations":         "MaxwellEquations.txt",
    "EMWaveEquations":          "EMWaveEquations.txt",
    "PoyntingIrradiance":       "PoyntingIrradiance.txt",
    "DispersionScene":          "DispersionScene.txt",

    # Week 2 — Fresnel
    "Week2TitleCard":           "Week2TitleCard.txt",
    "ReflectionRefraction":     "ReflectionRefraction.txt",
    "FresnelEquations":         "FresnelEquations.txt",
    "ReflectivityBrewsterTIR":  "ReflectivityBrewsterTIR.txt",

    # Week 3 — Geometric
    "Week3TitleCard":           "Week3TitleCard.txt",
    "ThinLensScene":            "ThinLensScene.txt",

    # Week 4 — Matrix
    "Week4TitleCard":           "Week4TitleCard.txt",

    # Week 5 — Jones
    "Week5TitleCard":           "Week5TitleCard.txt",

    # Week 6 — Interference
    "Week6TitleCard":           "Week6TitleCard.txt",
    "YoungDoubleSlit":          "YoungDoubleSlit.txt",

    # Week 7 — Diffraction
    "Week7TitleCard":           "Week7TitleCard.txt",
    "SingleSlitScene":          "SingleSlitScene.txt",
    "CircularApertureResolution": "CircularApertureResolution.txt",

    # Week 8 — Fabry-Perot
    "Week8TitleCard":           "Week8TitleCard.txt",
    "FabryPerotScene":          "FabryPerotScene.txt",
}


# ── Core generation function ──────────────────────────────────────────────────
async def generate_one(scene_name: str, txt_file: str, overwrite: bool = False):
    """Generate MP3 for a single scene."""
    try:
        import edge_tts
    except ImportError:
        print("ERROR: edge-tts not installed. Run: pip install edge-tts")
        sys.exit(1)

    txt_path   = NARRATION_DIR / txt_file
    audio_path = AUDIO_DIR / f"{scene_name}.mp3"

    if not txt_path.exists():
        print(f"  SKIP  {scene_name:<40} — no narration file found ({txt_file})")
        return False

    if audio_path.exists() and not overwrite:
        print(f"  EXISTS {scene_name:<40} — {audio_path}")
        return True

    text = txt_path.read_text(encoding="utf-8").strip()
    if not text:
        print(f"  SKIP  {scene_name:<40} — narration file is empty")
        return False

    print(f"  GEN   {scene_name:<40} ...", end="", flush=True)
    try:
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(str(audio_path))
        size_kb = audio_path.stat().st_size // 1024
        print(f" done ({size_kb} KB)")
        return True
    except Exception as e:
        print(f" FAILED: {e}")
        return False


async def generate_all(overwrite: bool = False, only: str = None):
    """Generate audio for all scenes (or just one if only= is set)."""
    scenes = SCENES
    if only:
        if only not in SCENES:
            print(f"ERROR: scene '{only}' not found. Available scenes:")
            for s in SCENES:
                print(f"  {s}")
            sys.exit(1)
        scenes = {only: SCENES[only]}

    print(f"\n31OPT Optics — Narration Audio Generator")
    print(f"Voice: {VOICE}  |  Rate: {RATE}  |  Output: {AUDIO_DIR}\n")

    ok = fail = skip = 0
    for scene_name, txt_file in scenes.items():
        result = await generate_one(scene_name, txt_file, overwrite)
        if result is True:
            ok += 1
        elif result is False:
            txt_path = NARRATION_DIR / txt_file
            if not txt_path.exists():
                skip += 1
            else:
                fail += 1

    print(f"\nDone: {ok} generated, {skip} skipped (no txt), {fail} failed")
    print(f"Audio files saved to: {AUDIO_DIR.resolve()}")


def list_scenes():
    """Print status of all scenes."""
    print(f"\n{'Scene':<42} {'Narration':<12} {'Audio':<12}")
    print("-" * 70)
    for scene, txt in SCENES.items():
        txt_path   = NARRATION_DIR / txt
        audio_path = AUDIO_DIR / f"{scene}.mp3"
        txt_status   = "YES" if txt_path.exists()   else "MISSING"
        audio_status = "YES" if audio_path.exists() else "not yet"
        print(f"{scene:<42} {txt_status:<12} {audio_status:<12}")


# ── ffmpeg sync helper ────────────────────────────────────────────────────────
def print_sync_commands(quality: str = "1080p60"):
    """Print ffmpeg commands to merge video + audio for every scene."""
    print("\n# ffmpeg commands to merge narration audio into rendered videos:")
    print("# Run these after both manim rendering AND audio generation are done.\n")

    output_dir = Path("output_narrated")
    output_dir.mkdir(exist_ok=True)

    for scene, txt_file in SCENES.items():
        # find which python file contains this scene
        py_file = None
        for f in Path(".").glob("*.py"):
            if f.name in ("main.py", "utils.py", "generate_audio.py"):
                continue
            try:
                content = f.read_text(encoding="utf-8")
                if f"class {scene}(" in content:
                    py_file = f.stem
                    break
            except Exception:
                pass

        if not py_file:
            continue

        video = f"media/videos/{py_file}/{quality}/{scene}.mp4"
        audio = f"narration/audio/{scene}.mp3"
        out   = f"output_narrated/{scene}.mp4"

        print(f"ffmpeg -i \"{video}\" -i \"{audio}\" "
              f"-c:v copy -c:a aac -shortest \"{out}\"")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate narration audio for 31OPT Optics Manim scenes"
    )
    parser.add_argument("--all",    action="store_true",
                        help="Regenerate all audio, overwriting existing files")
    parser.add_argument("--list",   action="store_true",
                        help="List all scenes and their narration/audio status")
    parser.add_argument("--sync",   action="store_true",
                        help="Print ffmpeg commands to merge video + audio")
    parser.add_argument("--scene",  type=str, default=None,
                        help="Generate audio for one specific scene only")
    args = parser.parse_args()

    if args.list:
        list_scenes()
    elif args.sync:
        print_sync_commands()
    else:
        asyncio.run(generate_all(overwrite=args.all, only=args.scene))

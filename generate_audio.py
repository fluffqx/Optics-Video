"""
generate_audio.py — Auto-generate narration MP3s and merge with video
=====================================================================

Requirements:
    pip install edge-tts

Usage:
    python generate_audio.py              # generate all missing MP3s
    python generate_audio.py --all        # regenerate everything (overwrite)
    python generate_audio.py --list       # check status of all scenes
    python generate_audio.py --scene WaveEquation1D   # one scene only
    python generate_audio.py --merge      # merge all video+audio into output_narrated/
    python generate_audio.py --concat     # concatenate all narrated videos into one

Voice options (change VOICE below):
    en-GB-RyanNeural      — British male (default)
    en-US-GuyNeural       — American male
    en-GB-SoniaNeural     — British female
    en-AU-WilliamNeural   — Australian male
    en-US-AriaNeural      — American female
"""

import asyncio, os, sys, argparse, subprocess
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────
VOICE       = "en-GB-RyanNeural"
RATE        = "+0%"
PITCH       = "+0Hz"
QUALITY     = "1080p60"    # match your manim render quality

NARRATION_DIR  = Path("narration")
AUDIO_DIR      = Path("narration/audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR     = Path("output_narrated")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Scene → narration file mapping ───────────────────────────────────────────
# Any scene not listed here gets no narration (instrumental/visual only)
SCENES = {
    # Week 1 — Waves
    "Week1TitleCard":              "Week1TitleCard.txt",
    "WaveIntroduction":            "WaveIntroduction.txt",
    "WaveEquation1D":              "WaveEquation1D.txt",
    "WaveEquationProof":           "WaveEquationProof.txt",
    "HarmonicWave":                "HarmonicWave.txt",
    "HarmonicWaveExample":         "HarmonicWaveExample.txt",
    "SuperpositionPrinciple":      "SuperpositionPrinciple.txt",
    "PhaseGroupVelocity":          "PhaseGroupVelocity.txt",
    "ComplexRepresentation":       "ComplexRepresentation.txt",
    "ThreeDWaves":                 "ThreeDWaves.txt",
    "Week1WavesSummary":           "Week1WavesSummary.txt",
    # Week 1 — Maxwell
    "MaxwellIntro":                "MaxwellIntro.txt",
    "VectorCalculusNotation":      "VectorCalculusNotation.txt",
    "MaxwellEquations":            "MaxwellEquations.txt",
    "MaxwellVacuum":               "MaxwellVacuum.txt",
    "EMWaveDerivation":            "EMWaveDerivation.txt",
    "EMWaveProperties":            "EMWaveProperties.txt",
    "EMWaveExample":               "EMWaveExample.txt",
    "PoyntingIrradiance":          "PoyntingIrradiance.txt",
    "RadiationPressure":           "RadiationPressure.txt",
    "DispersionScene":             "DispersionScene.txt",
    # Week 2
    "Week2TitleCard":              "Week2TitleCard.txt",
    "Week2Intro":                  "Week2Intro.txt",
    "FermatPrinciple":             "FermatPrinciple.txt",
    "ReflectionRefraction":        "ReflectionRefraction.txt",
    "FresnelEquationsDerivation":  "FresnelEquationsDerivation.txt",
    "FresnelEquations":            "FresnelEquations.txt",
    "FresnelFullExample":          "FresnelFullExample.txt",
    "ReflectivityTransmissivity":  "ReflectivityTransmissivity.txt",
    "BrewsterTIR":                 "BrewsterTIR.txt",
    "MalusLaw":                    "MalusLaw.txt",
    # Week 3
    "Week3TitleCard":              "Week3TitleCard.txt",
    "GeometricOpticsIntro":        "GeometricOpticsIntro.txt",
    "SignConventions":             "SignConventions.txt",
    "SphericalSurface":            "SphericalSurface.txt",
    "ThinLensScene":               "ThinLensScene.txt",
    "MirrorScene":                 "MirrorScene.txt",
    "LensCombinations":            "LensCombinations.txt",
    "OpticalInstruments":          "OpticalInstruments.txt",
    # Week 4
    "Week4TitleCard":              "Week4TitleCard.txt",
    "MatrixOpticsIntro":           "MatrixOpticsIntro.txt",
    "MatrixEquations":             "MatrixEquations.txt",
    "SystemMatrixCardinalPoints":  "SystemMatrixCardinalPoints.txt",
    "MatrixExample":               "MatrixExample.txt",
    # Week 5
    "Week5TitleCard":              "Week5TitleCard.txt",
    "PolarisationStatesScene":     "PolarisationStatesScene.txt",
    "BirefringenceWavePlates":     "BirefringenceWavePlates.txt",
    "JonesFormalism":              "JonesFormalism.txt",
    "JonesMatrices":               "JonesMatrices.txt",
    # Week 6
    "Week6TitleCard":              "Week6TitleCard.txt",
    "InterferenceIntroScene":      "InterferenceIntroScene.txt",
    "TwoBeamInterference":         "TwoBeamInterference.txt",
    "YoungDoubleSlit":             "YoungDoubleSlit.txt",
    "ThinFilmInterference":        "ThinFilmInterference.txt",
    "FringeVisibility":            "FringeVisibility.txt",
    "MichelsonScene":              "MichelsonScene.txt",
    # Week 7
    "Week7TitleCard":              "Week7TitleCard.txt",
    "HuygensPrinciple":            "HuygensPrinciple.txt",
    "SingleSlitDiffraction":       "SingleSlitDiffraction.txt",
    "CircularApertureRayleigh":    "CircularApertureRayleigh.txt",
    "DiffractionGrating":          "DiffractionGrating.txt",
    # Week 8
    "Week8TitleCard":              "Week8TitleCard.txt",
    "MultiBeamIntro":              "MultiBeamIntro.txt",
    "AiryFunction":                "AiryFunction.txt",
    "FinesseResolving":            "FinesseResolving.txt",
    "FabryPerotExample":           "FabryPerotExample.txt",
    "CoherenceLength":             "CoherenceLength.txt",
    "Week8Summary":                "Week8Summary.txt",
    # Exam prep
    "FormulaSheetTitleCard":       "FormulaSheetTitleCard.txt",
    "MidtermPrepScene":            "MidtermPrepScene.txt",
    "FinalExamPrepScene":          "FinalExamPrepScene.txt",
}

# ── Video path helper ─────────────────────────────────────────────────────────
def video_path(py_file: str, scene: str, quality: str = QUALITY) -> Path:
    stem = Path(py_file).stem
    return Path(f"media/videos/{stem}/{quality}/{scene}.mp4")


# ── Audio generation ──────────────────────────────────────────────────────────
async def generate_one(scene: str, txt_file: str, overwrite: bool = False) -> bool:
    try:
        import edge_tts
    except ImportError:
        print("ERROR: run  pip install edge-tts  first")
        sys.exit(1)

    txt_path   = NARRATION_DIR / txt_file
    audio_path = AUDIO_DIR / f"{scene}.mp3"

    if not txt_path.exists():
        print(f"  SKIP   {scene:<38} — no .txt narration file")
        return False
    if audio_path.exists() and not overwrite:
        print(f"  EXISTS {scene:<38} — {audio_path}")
        return True

    text = txt_path.read_text(encoding="utf-8").strip()
    if not text:
        print(f"  SKIP   {scene:<38} — empty txt file")
        return False

    print(f"  GEN    {scene:<38} ...", end="", flush=True)
    try:
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await communicate.save(str(audio_path))
        kb = audio_path.stat().st_size // 1024
        print(f" done ({kb} KB)")
        return True
    except Exception as e:
        print(f" FAILED: {e}")
        return False


async def generate_all(overwrite=False, only=None):
    scenes = SCENES if not only else {only: SCENES[only]} if only in SCENES else {}
    if only and not scenes:
        print(f"Scene '{only}' not in narration map."); sys.exit(1)

    print(f"\n31OPT Narration Generator | Voice: {VOICE}\n")
    ok = skip = fail = 0
    for scene, txt in scenes.items():
        r = await generate_one(scene, txt, overwrite)
        if r:    ok   += 1
        elif r is False: skip += 1
        else:    fail  += 1
    print(f"\nDone: {ok} generated, {skip} skipped, {fail} failed")
    print(f"Files in: {AUDIO_DIR.resolve()}")


# ── Video + Audio merge ───────────────────────────────────────────────────────
def merge_all():
    """Merge each rendered scene video with its narration audio."""
    # Import render order from main.py
    import importlib.util
    spec = importlib.util.spec_from_file_location("main_mod", "main.py")
    m    = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    render_order = m.RENDER_ORDER

    print(f"\n31OPT — Merging video + audio into {OUTPUT_DIR}/\n")
    merged = failed = skipped = 0

    for py_file, scene in render_order:
        vid = video_path(py_file, scene, QUALITY)
        aud = AUDIO_DIR / f"{scene}.mp3"
        out = OUTPUT_DIR / f"{scene}.mp4"

        if not vid.exists():
            print(f"  SKIP  {scene:<38} — video not rendered yet")
            skipped += 1
            continue

        if not aud.exists():
            # No audio — just copy the video as-is
            subprocess.run(
                ["ffmpeg", "-y", "-i", str(vid), "-c", "copy", str(out)],
                capture_output=True)
            print(f"  COPY  {scene:<38} — no audio, copied video only")
            skipped += 1
            continue

        print(f"  MERGE {scene:<38} ...", end="", flush=True)
        result = subprocess.run([
            "ffmpeg", "-y",
            "-i",  str(vid),
            "-i",  str(aud),
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",         # stop when the shorter stream ends
            "-movflags", "+faststart",  # web-optimised
            str(out)
        ], capture_output=True, text=True)

        if result.returncode == 0:
            mb = out.stat().st_size // (1024*1024)
            print(f" done ({mb} MB)")
            merged += 1
        else:
            print(f" FAILED")
            print(result.stderr[-200:])
            failed += 1

    print(f"\nMerge complete: {merged} merged, {skipped} skipped, {failed} failed")
    print(f"Output folder: {OUTPUT_DIR.resolve()}")


def concat_final():
    """Concatenate all output_narrated/*.mp4 into one final video."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("main_mod", "main.py")
    m    = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    render_order = m.RENDER_ORDER

    filelist = Path("filelist_narrated.txt")
    with filelist.open("w") as f:
        for _, scene in render_order:
            p = OUTPUT_DIR / f"{scene}.mp4"
            if p.exists():
                f.write(f"file '{p.resolve()}'\n")
            else:
                print(f"  WARNING: {p} not found — skipping from concat")

    out = Path("optics_full_video_narrated.mp4")
    print(f"\nConcatenating into {out} ...")
    result = subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(filelist), "-c", "copy", str(out)
    ], capture_output=True, text=True)

    if result.returncode == 0:
        mb = out.stat().st_size // (1024*1024)
        print(f"Done! Final video: {out.resolve()} ({mb} MB)")
    else:
        print("FAILED:")
        print(result.stderr)


def list_scenes():
    import importlib.util
    spec = importlib.util.spec_from_file_location("main_mod", "main.py")
    m    = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    print(f"\n{'Scene':<38} {'Narr.txt':<10} {'Audio':<10} {'Video'}")
    print("-"*80)
    for py_file, scene in m.RENDER_ORDER:
        has_txt   = "YES" if scene in SCENES and (NARRATION_DIR / SCENES[scene]).exists() else "no"
        has_audio = "YES" if (AUDIO_DIR / f"{scene}.mp3").exists() else "no"
        has_video = "YES" if video_path(py_file, scene).exists() else "no"
        print(f"{scene:<38} {has_txt:<10} {has_audio:<10} {has_video}")


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    p = argparse.ArgumentParser(description="31OPT narration generator and video merger")
    p.add_argument("--all",    action="store_true", help="Regenerate all audio files")
    p.add_argument("--list",   action="store_true", help="Show status of all scenes")
    p.add_argument("--scene",  type=str,            help="Generate audio for one scene")
    p.add_argument("--merge",  action="store_true", help="Merge video+audio for all scenes")
    p.add_argument("--concat", action="store_true", help="Concatenate all narrated videos")
    args = p.parse_args()

    if args.list:
        list_scenes()
    elif args.merge:
        merge_all()
    elif args.concat:
        concat_final()
    else:
        asyncio.run(generate_all(overwrite=args.all, only=args.scene))

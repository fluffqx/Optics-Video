"""
generate_audio.py — Generate narration MP3s + exact word-boundary timing JSON files
====================================================================================

Usage:
    python generate_audio.py              # generate all missing MP3s + timing JSONs
    python generate_audio.py --all        # regenerate everything
    python generate_audio.py --list       # show status of all scenes
    python generate_audio.py --scene NAME # one scene only
    python generate_audio.py --merge      # merge video + audio
    python generate_audio.py --concat     # concatenate final video

Timing JSONs are saved to narration/timing/<SceneName>.json
Each JSON contains:
  {
    "total_duration": 51.3,
    "paragraphs": [
      {"index": 0, "start": 0.0, "end": 4.2, "duration": 4.2, "text": "Before writing..."},
      {"index": 1, "start": 4.2, "end": 23.1, "duration": 18.9, "text": "The divergence..."},
      ...
    ]
  }

Use sync_timing.py to apply these timings to self.wait() calls in scene files.
"""

import asyncio, os, sys, argparse, subprocess, json
from pathlib import Path

VOICE       = "en-GB-RyanNeural"
RATE        = "+0%"
PITCH       = "+0Hz"
QUALITY     = "1080p60"

NARRATION_DIR = Path("narration")
AUDIO_DIR     = Path("narration/audio")
TIMING_DIR    = Path("narration/timing")
OUTPUT_DIR    = Path("output_narrated")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
TIMING_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SCENES = {
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
    "Week3TitleCard":              "Week3TitleCard.txt",
    "GeometricOpticsIntro":        "GeometricOpticsIntro.txt",
    "SignConventions":             "SignConventions.txt",
    "SphericalSurface":            "SphericalSurface.txt",
    "ThinLensScene":               "ThinLensScene.txt",
    "MirrorScene":                 "MirrorScene.txt",
    "LensCombinations":            "LensCombinations.txt",
    "OpticalInstruments":          "OpticalInstruments.txt",
    "Week4TitleCard":              "Week4TitleCard.txt",
    "MatrixOpticsIntro":           "MatrixOpticsIntro.txt",
    "MatrixEquations":             "MatrixEquations.txt",
    "SystemMatrixCardinalPoints":  "SystemMatrixCardinalPoints.txt",
    "MatrixExample":               "MatrixExample.txt",
    "Week5TitleCard":              "Week5TitleCard.txt",
    "PolarisationStatesScene":     "PolarisationStatesScene.txt",
    "BirefringenceWavePlates":     "BirefringenceWavePlates.txt",
    "JonesFormalism":              "JonesFormalism.txt",
    "JonesMatrices":               "JonesMatrices.txt",
    "Week6TitleCard":              "Week6TitleCard.txt",
    "InterferenceIntroScene":      "InterferenceIntroScene.txt",
    "TwoBeamInterference":         "TwoBeamInterference.txt",
    "YoungDoubleSlit":             "YoungDoubleSlit.txt",
    "ThinFilmInterference":        "ThinFilmInterference.txt",
    "FringeVisibility":            "FringeVisibility.txt",
    "MichelsonScene":              "MichelsonScene.txt",
    "Week7TitleCard":              "Week7TitleCard.txt",
    "HuygensPrinciple":            "HuygensPrinciple.txt",
    "SingleSlitDiffraction":       "SingleSlitDiffraction.txt",
    "CircularApertureRayleigh":    "CircularApertureRayleigh.txt",
    "DiffractionGrating":          "DiffractionGrating.txt",
    "Week8TitleCard":              "Week8TitleCard.txt",
    "MultiBeamIntro":              "MultiBeamIntro.txt",
    "AiryFunction":                "AiryFunction.txt",
    "FinesseResolving":            "FinesseResolving.txt",
    "FabryPerotExample":           "FabryPerotExample.txt",
    "CoherenceLength":             "CoherenceLength.txt",
    "Week8Summary":                "Week8Summary.txt",
    "FormulaSheetTitleCard":       "FormulaSheetTitleCard.txt",
    "MidtermPrepScene":            "MidtermPrepScene.txt",
    "FinalExamPrepScene":          "FinalExamPrepScene.txt",
}


def video_path(py_file: str, scene: str, quality: str = QUALITY) -> Path:
    stem = Path(py_file).stem
    return Path(f"media/videos/{stem}/{quality}/{scene}.mp4")


# ── Core: generate MP3 + timing JSON using word boundary events ──────────────

async def generate_one(scene: str, txt_file: str, overwrite: bool = False) -> bool:
    try:
        import edge_tts
    except ImportError:
        print("ERROR: run  pip install edge-tts  first")
        sys.exit(1)

    txt_path    = NARRATION_DIR / txt_file
    audio_path  = AUDIO_DIR / f"{scene}.mp3"
    timing_path = TIMING_DIR / f"{scene}.json"

    if not txt_path.exists():
        print(f"  SKIP   {scene:<40} — no .txt file")
        return False

    if audio_path.exists() and timing_path.exists() and not overwrite:
        print(f"  EXISTS {scene:<40}")
        return True

    full_text = txt_path.read_text(encoding="utf-8").strip()
    if not full_text:
        return False

    # Split into paragraphs
    paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]

    print(f"  GEN    {scene:<40} ({len(paragraphs)} paras)...", end="", flush=True)

    # Generate audio with word boundary events
    communicate = edge_tts.Communicate(full_text, VOICE, rate=RATE, pitch=PITCH)

    audio_chunks = []
    word_events  = []   # {"word": str, "start": float, "end": float}

    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_chunks.append(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            start = chunk["offset"] / 10_000_000      # 100-nanosecond units → seconds
            dur   = chunk["duration"] / 10_000_000
            word_events.append({
                "word":  chunk["text"],
                "start": round(start, 4),
                "end":   round(start + dur, 4),
            })

    # Write MP3
    audio_path.write_bytes(b"".join(audio_chunks))

    # Calculate paragraph timestamps using word events
    # Strategy: assign words to paragraphs proportionally, then use
    # the actual word event timestamps for precise start/end times
    total_duration = word_events[-1]["end"] if word_events else 0
    total_words    = sum(len(p.split()) for p in paragraphs)

    para_timings = []
    word_idx = 0

    for p_idx, para in enumerate(paragraphs):
        para_word_count = len(para.split())
        # start = timestamp of first word assigned to this paragraph
        para_start = word_events[word_idx]["start"] if word_idx < len(word_events) else total_duration
        # advance word_idx by the number of words in this paragraph
        end_idx = min(word_idx + para_word_count - 1, len(word_events) - 1)
        end_idx = min(end_idx, len(word_events) - 1)
        para_end = word_events[end_idx]["end"] if word_events else total_duration
        word_idx = min(word_idx + para_word_count, len(word_events))

        para_timings.append({
            "index":    p_idx,
            "start":    round(para_start, 3),
            "end":      round(para_end, 3),
            "duration": round(para_end - para_start, 3),
            "text":     para[:80],
        })

    # Save timing JSON
    timing_data = {
        "scene":          scene,
        "total_duration": round(total_duration, 3),
        "paragraphs":     para_timings,
    }
    timing_path.write_text(json.dumps(timing_data, indent=2), encoding="utf-8")

    kb = audio_path.stat().st_size // 1024
    print(f" done ({kb}KB, {total_duration:.1f}s)")
    return True


async def generate_all(overwrite=False, only=None):
    scenes = SCENES if not only else {only: SCENES[only]} if only in SCENES else {}
    if only and not scenes:
        print(f"Scene '{only}' not found.")
        sys.exit(1)
    print(f"\n31OPT Narration Generator | Voice: {VOICE}\n")
    ok = skip = fail = 0
    for scene, txt in scenes.items():
        r = await generate_one(scene, txt, overwrite)
        if r:    ok   += 1
        elif r is None: fail += 1
        else:    skip += 1
    print(f"\nDone: {ok} generated, {skip} skipped, {fail} failed")
    print(f"Timing JSONs saved to: {TIMING_DIR.resolve()}")


# ── Merge video + audio ───────────────────────────────────────────────────────

def merge_all():
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
            print(f"  SKIP  {scene:<40} — video not rendered")
            skipped += 1
            continue

        if out.exists():
            print(f"  SKIP  {scene:<40} — already merged")
            merged += 1
            continue

        if not aud.exists():
            subprocess.run(["ffmpeg", "-y", "-i", str(vid), "-c", "copy", str(out)],
                           capture_output=True)
            print(f"  COPY  {scene:<40} — no audio")
            skipped += 1
            continue

        print(f"  MERGE {scene:<40} ...", end="", flush=True)
        result = subprocess.run([
            "ffmpeg", "-y",
            "-i",  str(vid),
            "-i",  str(aud),
            "-filter_complex", "[0:v]tpad=stop_mode=clone:stop_duration=120[v]",
            "-map", "[v]", "-map", "1:a",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "aac", "-b:a", "192k",
            "-shortest", "-movflags", "+faststart",
            str(out)
        ], capture_output=True, text=True)

        if result.returncode == 0:
            mb = out.stat().st_size // (1024*1024)
            print(f" done ({mb}MB)")
            merged += 1
        else:
            print(f" FAILED")
            failed += 1

    print(f"\nMerge: {merged} done, {skipped} skipped, {failed} failed")


def concat_final():
    import importlib.util
    spec = importlib.util.spec_from_file_location("main_mod", "main.py")
    m    = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    filelist = Path("filelist_narrated.txt")
    with filelist.open("w") as f:
        for _, scene in m.RENDER_ORDER:
            p = OUTPUT_DIR / f"{scene}.mp4"
            if p.exists():
                f.write(f"file '{p.resolve()}'\n")

    out = Path("optics_full_video_narrated.mp4")
    print(f"\nConcatenating into {out} ...")
    result = subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(filelist), "-c", "copy", str(out)
    ], capture_output=True, text=True)

    if result.returncode == 0:
        mb = out.stat().st_size // (1024*1024)
        print(f"Done! {out} ({mb}MB)")
    else:
        print("FAILED:", result.stderr[-300:])


def list_scenes():
    import importlib.util
    spec = importlib.util.spec_from_file_location("main_mod", "main.py")
    m    = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    print(f"\n{'Scene':<40} {'Txt':<6} {'MP3':<6} {'JSON':<6} {'Video'}")
    print("-" * 72)
    for py_file, scene in m.RENDER_ORDER:
        has_txt    = "YES" if scene in SCENES and (NARRATION_DIR / SCENES[scene]).exists()   else "no"
        has_audio  = "YES" if (AUDIO_DIR  / f"{scene}.mp3").exists()  else "no"
        has_timing = "YES" if (TIMING_DIR / f"{scene}.json").exists() else "no"
        has_video  = "YES" if video_path(py_file, scene).exists()     else "no"
        print(f"{scene:<40} {has_txt:<6} {has_audio:<6} {has_timing:<6} {has_video}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--all",    action="store_true")
    p.add_argument("--list",   action="store_true")
    p.add_argument("--scene",  type=str)
    p.add_argument("--merge",  action="store_true")
    p.add_argument("--concat", action="store_true")
    args = p.parse_args()

    if args.list:
        list_scenes()
    elif args.merge:
        merge_all()
    elif args.concat:
        concat_final()
    else:
        asyncio.run(generate_all(overwrite=args.all, only=args.scene))

"""
main.py — 31OPT Optics Manim Video Series
==========================================
Render order for the complete optics exam prep video.
Run individual scenes with:
    manim -pql <file>.py <SceneClass>

Render all scenes at high quality:
    manim -qh <file>.py

Concatenate with ffmpeg after rendering all scenes:
    ffmpeg -f concat -safe 0 -i filelist.txt -c copy optics_full_video.mp4

All rendered .mp4 files are output to:
    media/videos/<file>/1080p60/<SceneClass>.mp4

Generate filelist.txt by listing all output paths in the order below.
"""

RENDER_ORDER = [
    # ── WEEK 1: WAVES ─────────────────────────────────────────────────────────
    ("week1_waves.py",            "Week1TitleCard"),
    ("week1_waves.py",            "WaveIntroduction"),
    ("week1_waves.py",            "WaveEquation1D"),
    ("week1_waves.py",            "HarmonicWave"),
    ("week1_waves.py",            "PhaseGroupVelocity"),
    ("week1_waves.py",            "ComplexRepresentation"),
    ("week1_waves.py",            "Week1WavesSummary"),

    # ── WEEK 1: MAXWELL ───────────────────────────────────────────────────────
    ("week1_maxwell.py",          "MaxwellIntro"),
    ("week1_maxwell.py",          "MaxwellEquations"),
    ("week1_maxwell.py",          "EMWaveEquations"),
    ("week1_maxwell.py",          "PoyntingIrradiance"),
    ("week1_maxwell.py",          "DispersionScene"),

    # ── WEEK 1: EXERCISES ─────────────────────────────────────────────────────
    ("exercises_week1.py",        "SC_Week1_Problem1"),
    ("exercises_week1.py",        "SC_Week1_Problem2"),
    ("exercises_week1.py",        "SC_Week1_Problem3"),
    ("exercises_week1.py",        "SC_Week1_Problem4"),
    ("exercises_week1.py",        "SC_Week1_Problem5"),

    # ── WEEK 1: SLT ───────────────────────────────────────────────────────────
    ("slt_week1.py",              "SLT_Week1_Problem1"),
    ("slt_week1.py",              "SLT_Week1_Problem2"),

    # ── WEEK 2: FRESNEL ───────────────────────────────────────────────────────
    ("week2_fresnel.py",          "Week2TitleCard"),
    ("week2_fresnel.py",          "Week2Intro"),
    ("week2_fresnel.py",          "ReflectionRefraction"),
    ("week2_fresnel.py",          "FresnelEquations"),
    ("week2_fresnel.py",          "ReflectivityBrewsterTIR"),

    # ── WEEK 2: EXERCISES ─────────────────────────────────────────────────────
    ("exercises_week2.py",        "SC_Week2_Problem1"),
    ("exercises_week2.py",        "SC_Week2_Problem2"),
    ("exercises_week2.py",        "SC_Week2_Problem6"),
    ("exercises_week2.py",        "SC_Week2_Problem7"),

    # ── WEEK 2: SLT ───────────────────────────────────────────────────────────
    ("slt_week2.py",              "SLT_Week2_Problem1"),
    ("slt_week2.py",              "SLT_Week2_Problem2"),

    # ── WEEK 3: GEOMETRIC OPTICS ──────────────────────────────────────────────
    ("week3_geometric.py",        "Week3TitleCard"),
    ("week3_geometric.py",        "GeometricOpticsIntro"),
    ("week3_geometric.py",        "SignConventions"),
    ("week3_geometric.py",        "SphericalSurface"),
    ("week3_geometric.py",        "ThinLensScene"),
    ("week3_geometric.py",        "MirrorScene"),
    ("week3_geometric.py",        "LensCombinations"),

    # ── WEEK 3: EXERCISES ─────────────────────────────────────────────────────
    ("exercises_week3.py",        "SC_Week3_Problem1"),
    ("exercises_week3.py",        "SC_Week3_Problem3"),

    # ── WEEK 3: SLT ───────────────────────────────────────────────────────────
    ("slt_week3.py",              "SLT_Week3_Problem1"),

    # ── WEEK 4: MATRIX OPTICS ─────────────────────────────────────────────────
    ("week4_matrix_polarisation.py", "Week4TitleCard"),
    ("week4_matrix_polarisation.py", "MatrixOpticsIntro"),
    ("week4_matrix_polarisation.py", "MatrixEquations"),

    # ── WEEK 4: EXERCISES ─────────────────────────────────────────────────────
    ("exercises_week4.py",        "SC_Week4_Problem1"),
    ("exercises_week4.py",        "SC_Week4_Problem3"),

    # ── WEEK 5: JONES & POLARISATION ──────────────────────────────────────────
    ("week5_jones.py",            "Week5TitleCard"),
    ("week5_jones.py",            "PolarisationStatesScene"),
    ("week5_jones.py",            "BirefringenceWavePlates"),
    ("week5_jones.py",            "JonesFormalism"),
    ("week5_jones.py",            "JonesMatrices"),

    # ── WEEK 5: EXERCISES ─────────────────────────────────────────────────────
    ("exercises_week5.py",        "SC_Week5_Problem3"),
    ("exercises_week5.py",        "SC_Week5_Problem7"),
    ("exercises_week5.py",        "SC_Week5_Problem4"),

    # ── WEEK 5: SLT ───────────────────────────────────────────────────────────
    ("slt_week5.py",              "SLT_Week5_Problem1"),

    # ── WEEKS 5-6: INTERFERENCE ───────────────────────────────────────────────
    ("week6_interference.py",     "Week6TitleCard"),
    ("week6_interference.py",     "InterferenceIntroScene"),
    ("week6_interference.py",     "TwoBeamInterference"),
    ("week6_interference.py",     "YoungDoubleSlit"),
    ("week6_interference.py",     "ThinFilmInterference"),
    ("week6_interference.py",     "MichelsonScene"),

    # ── WEEK 6: EXERCISES ─────────────────────────────────────────────────────
    ("exercises_week6.py",        "SC_Week6_Problem1"),
    ("exercises_week6.py",        "SC_Week6_Problem3"),
    ("exercises_week6.py",        "SC_Week6_Problem4"),

    # ── WEEK 6: SLT ───────────────────────────────────────────────────────────
    ("slt_week6.py",              "SLT_Week6_Problem1"),
    ("slt_week6.py",              "SLT_Week6_Problem2"),
    ("slt_week6.py",              "SLT_Week6_Problem3"),

    # ── WEEK 7: DIFFRACTION ───────────────────────────────────────────────────
    ("week7_diffraction.py",      "Week7TitleCard"),
    ("week7_diffraction.py",      "DiffractionIntroScene"),
    ("week7_diffraction.py",      "SingleSlitScene"),
    ("week7_diffraction.py",      "RectangularApertureScene"),
    ("week7_diffraction.py",      "CircularApertureResolution"),
    ("week7_diffraction.py",      "DiffractionGratingScene"),

    # ── WEEK 7: EXERCISES ─────────────────────────────────────────────────────
    ("exercises_week7.py",        "SC_Week7_Problem1"),
    ("exercises_week7.py",        "SC_Week7_Problem5"),
    ("exercises_week7.py",        "SC_Week7_Problem10"),

    # ── WEEK 7: SLT ───────────────────────────────────────────────────────────
    ("slt_week7.py",              "SLT_Week7_Problem1"),
    ("slt_week7.py",              "SLT_Week7_Problem2"),

    # ── WEEK 8: FABRY-PEROT ───────────────────────────────────────────────────
    ("week8_fabry_perot.py",      "Week8TitleCard"),
    ("week8_fabry_perot.py",      "FabryPerotScene"),
    ("week8_fabry_perot.py",      "CoherenceScene"),

    # ── WEEK 8: EXERCISES ─────────────────────────────────────────────────────
    ("exercises_week8.py",        "SC_Week8_Problem9"),
    ("exercises_week8.py",        "SC_Week8_Problem10"),
    ("exercises_week8.py",        "SC_Week8_Problem3"),

    # ── WEEK 8-9: SLT ─────────────────────────────────────────────────────────
    ("slt_week8.py",              "SLT_Week8_Problem1"),
    ("slt_week8.py",              "SLT_Week8_Problem2"),
    ("slt_week9.py",              "SLT_Week9_Problem1"),
    ("slt_week9.py",              "SLT_Week9_Problem2"),
    ("slt_week9.py",              "SLT_Week9_Problem4"),
]


def print_render_commands(quality: str = "ql") -> None:
    """Print all manim render commands in order."""
    for filepath, scene in RENDER_ORDER:
        print(f"python -m manim -{quality} {filepath} {scene}")


def generate_filelist(media_root: str = "media/videos", quality: str = "1080p60") -> str:
    """Generate ffmpeg filelist.txt content."""
    lines = []
    for filepath, scene in RENDER_ORDER:
        stem = filepath.replace(".py", "")
        path = f"{media_root}/{stem}/{quality}/{scene}.mp4"
        lines.append(f"file '{path}'")
    return "\n".join(lines)


if __name__ == "__main__":
    import sys
    if "--list" in sys.argv:
        print_render_commands("qh")
    elif "--filelist" in sys.argv:
        print(generate_filelist())
    else:
        print("Usage:")
        print("  python main.py --list       # print all render commands (high quality)")
        print("  python main.py --filelist   # print ffmpeg filelist.txt content")
        print()
        print(f"Total scenes: {len(RENDER_ORDER)}")
        print()
        print("Quick render (low quality preview):")
        print_render_commands("ql")

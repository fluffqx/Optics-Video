"""
main.py  —  31OPT Optics Manim Video Series
============================================
Usage:
    python main.py --list       # print all render commands (python -m manim -qh ...)
    python main.py --filelist   # print ffmpeg concat file list
    python main.py --scenes     # print all scene names grouped by file
"""
import argparse
from pathlib import Path

# ── Complete scene list in playback order ─────────────────────────────────────
# Format: (python_file, SceneClass)
RENDER_ORDER = [
    # ── WEEK 1: Waves ────────────────────────────────────────────────────────
    ("week1_waves.py",             "Week1TitleCard"),
    ("week1_waves.py",             "WaveIntroduction"),
    ("week1_waves.py",             "WaveEquation1D"),
    ("week1_waves.py",             "WaveEquationProof"),
    ("week1_waves.py",             "HarmonicWave"),
    ("week1_waves.py",             "HarmonicWaveExample"),
    ("week1_waves.py",             "SuperpositionPrinciple"),
    ("week1_waves.py",             "PhaseGroupVelocity"),
    ("week1_waves.py",             "ComplexRepresentation"),
    ("week1_waves.py",             "ThreeDWaves"),
    ("week1_waves.py",             "Week1WavesSummary"),

    # ── WEEK 1: Maxwell ──────────────────────────────────────────────────────
    ("week1_maxwell.py",           "MaxwellIntro"),
    ("week1_maxwell.py",           "VectorCalculusNotation"),
    ("week1_maxwell.py",           "MaxwellEquations"),
    ("week1_maxwell.py",           "MaxwellVacuum"),
    ("week1_maxwell.py",           "EMWaveDerivation"),
    ("week1_maxwell.py",           "EMWaveProperties"),
    ("week1_maxwell.py",           "EMWaveExample"),
    ("week1_maxwell.py",           "PoyntingIrradiance"),
    ("week1_maxwell.py",           "RadiationPressure"),
    ("week1_maxwell.py",           "DispersionScene"),

    # ── WEEK 2: Fresnel ──────────────────────────────────────────────────────
    ("week2_fresnel.py",           "Week2TitleCard"),
    ("week2_fresnel.py",           "Week2Intro"),
    ("week2_fresnel.py",           "FermatPrinciple"),
    ("week2_fresnel.py",           "ReflectionRefraction"),
    ("week2_fresnel.py",           "FresnelEquationsDerivation"),
    ("week2_fresnel.py",           "FresnelEquations"),
    ("week2_fresnel.py",           "FresnelFullExample"),
    ("week2_fresnel.py",           "ReflectivityTransmissivity"),
    ("week2_fresnel.py",           "BrewsterTIR"),
    ("week2_fresnel.py",           "MalusLaw"),

    # ── WEEK 3: Geometric Optics ─────────────────────────────────────────────
    ("week3_geometric.py",         "Week3TitleCard"),
    ("week3_geometric.py",         "GeometricOpticsIntro"),
    ("week3_geometric.py",         "SignConventions"),
    ("week3_geometric.py",         "SphericalSurface"),
    ("week3_geometric.py",         "ThinLensScene"),
    ("week3_geometric.py",         "MirrorScene"),
    ("week3_geometric.py",         "LensCombinations"),
    ("week3_geometric.py",         "OpticalInstruments"),

    # ── WEEK 4: Matrix Optics ────────────────────────────────────────────────
    ("week4_matrix_polarisation.py", "Week4TitleCard"),
    ("week4_matrix_polarisation.py", "MatrixOpticsIntro"),
    ("week4_matrix_polarisation.py", "MatrixEquations"),
    ("week4_matrix_polarisation.py", "SystemMatrixCardinalPoints"),
    ("week4_matrix_polarisation.py", "MatrixExample"),

    # ── WEEK 5: Jones / Polarisation ─────────────────────────────────────────
    ("week5_jones.py",             "Week5TitleCard"),
    ("week5_jones.py",             "PolarisationStatesScene"),
    ("week5_jones.py",             "BirefringenceWavePlates"),
    ("week5_jones.py",             "JonesFormalism"),
    ("week5_jones.py",             "JonesMatrices"),

    # ── WEEK 6: Interference ────────────────────────────────────────────────
    ("week6_interference.py",      "Week6TitleCard"),
    ("week6_interference.py",      "InterferenceIntroScene"),
    ("week6_interference.py",      "TwoBeamInterference"),
    ("week6_interference.py",      "YoungDoubleSlit"),
    ("week6_interference.py",      "ThinFilmInterference"),
    ("week6_interference.py",      "FringeVisibility"),
    ("week6_interference.py",      "MichelsonScene"),

    # ── WEEK 7: Diffraction ──────────────────────────────────────────────────
    ("week7_diffraction.py",       "Week7TitleCard"),
    ("week7_diffraction.py",       "HuygensPrinciple"),
    ("week7_diffraction.py",       "SingleSlitDiffraction"),
    ("week7_diffraction.py",       "CircularApertureRayleigh"),
    ("week7_diffraction.py",       "DiffractionGrating"),

    # ── WEEK 8: Fabry-Pérot ──────────────────────────────────────────────────
    ("week8_fabry_perot.py",       "Week8TitleCard"),
    ("week8_fabry_perot.py",       "MultiBeamIntro"),
    ("week8_fabry_perot.py",       "AiryFunction"),
    ("week8_fabry_perot.py",       "FinesseResolving"),
    ("week8_fabry_perot.py",       "FabryPerotExample"),
    ("week8_fabry_perot.py",       "CoherenceLength"),
    ("week8_fabry_perot.py",       "Week8Summary"),

    # ── FORMULA SHEET & EXAM PREP ────────────────────────────────────────────
    ("formula_sheet_recap.py",     "FormulaSheetTitleCard"),
    ("formula_sheet_recap.py",     "FormulasWavesMaxwell"),
    ("formula_sheet_recap.py",     "FormulasOptics"),
    ("formula_sheet_recap.py",     "FormulasInterferenceDiffraction"),
    ("formula_sheet_recap.py",     "MidtermPrepScene"),
    ("formula_sheet_recap.py",     "FinalExamPrepScene"),

    # ── EXERCISES ────────────────────────────────────────────────────────────
    ("exercises_week1.py",         "ExWeek1TitleCard"),
    ("exercises_week1.py",         "ExWeek1Problem1"),
    ("exercises_week1.py",         "ExWeek1Problem2"),
    ("exercises_week1.py",         "ExWeek1Problem3"),
    ("exercises_week2.py",         "ExWeek2TitleCard"),
    ("exercises_week2.py",         "ExWeek2Problem1"),
    ("exercises_week2.py",         "ExWeek2Problem2"),
    ("exercises_week3.py",         "ExWeek3TitleCard"),
    ("exercises_week3.py",         "ExWeek3Problem1"),
    ("exercises_week3.py",         "ExWeek3Problem2"),
    ("exercises_week6.py",         "ExWeek6TitleCard"),
    ("exercises_week6.py",         "ExWeek6Problem1"),
    ("exercises_week7.py",         "ExWeek7TitleCard"),
    ("exercises_week7.py",         "ExWeek7Problem1"),
    ("exercises_week8.py",         "ExWeek8TitleCard"),
    ("exercises_week8.py",         "ExWeek8Problem1"),

    # ── SLTs ─────────────────────────────────────────────────────────────────
    ("slt_week1.py",               "SLTWeek1"),
    ("slt_week2.py",               "SLTWeek2"),
    ("slt_week3.py",               "SLTWeek3"),
    ("slt_week5.py",               "SLTWeek5"),
    ("slt_week6.py",               "SLTWeek6"),
    ("slt_week7.py",               "SLTWeek7"),
    ("slt_week8.py",               "SLTWeek8"),
    ("slt_week9.py",               "SLTWeek9"),
]

QUALITY_FLAG = "qh"   # qh = 1080p60 | ql = 480p15 (low for testing) | qm = 720p


def print_render_commands(quality: str = QUALITY_FLAG) -> None:
    """Print all manim render commands in order."""
    print(f"# 31OPT Optics — {len(RENDER_ORDER)} scenes to render")
    print(f"# Quality: -{quality}   Change QUALITY_FLAG in main.py to 'ql' for fast preview")
    print()
    for filepath, scene in RENDER_ORDER:
        if Path(filepath).exists():
            print(f"python -m manim -{quality} {filepath} {scene}")
        else:
            print(f"# MISSING FILE: {filepath}  (scene: {scene})")


def print_filelist(quality: str = QUALITY_FLAG) -> None:
    """Print ffmpeg concat filelist for all rendered scenes."""
    res = "1080p60" if quality == "qh" else ("480p15" if quality == "ql" else "720p30")
    for filepath, scene in RENDER_ORDER:
        stem = Path(filepath).stem
        mp4  = Path(f"media/videos/{stem}/{res}/{scene}.mp4")
        if mp4.exists():
            print(f"file '{mp4}'")
        else:
            print(f"# NOT YET RENDERED: {mp4}")


def print_scenes() -> None:
    """Print all scene names grouped by file."""
    current_file = None
    for filepath, scene in RENDER_ORDER:
        if filepath != current_file:
            current_file = filepath
            print(f"\n── {filepath} ──")
        print(f"    {scene}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="31OPT Optics Manim render helper")
    parser.add_argument("--list",      action="store_true", help="Print all render commands")
    parser.add_argument("--filelist",  action="store_true", help="Print ffmpeg concat filelist")
    parser.add_argument("--scenes",    action="store_true", help="List all scene names")
    parser.add_argument("--quality",   default=QUALITY_FLAG, help="Manim quality flag (qh/qm/ql)")
    args = parser.parse_args()

    if args.filelist:
        print_filelist(args.quality)
    elif args.scenes:
        print_scenes()
    else:
        print_render_commands(args.quality)

# slt_week9.py
# 31OPT Optics — SLT Week 9 (Set 9): Fabry-Perot Advanced
from manim import *
from utils import *


class SLT_Week9_Problem1(Scene):
    """Missing orders in grating: derive condition."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 9 — Problem 1: Missing Orders", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Missing orders in a grating occur when an interference maximum", font_size=26, color=WHITE),
            Text("coincides with a zero of the single-slit sinc^2 envelope.", font_size=26, color=WHITE),
            Text("Show that missing orders occur when d/b is an integer,", font_size=26, color=WHITE),
            Text("and that this integer equals the order of the first missing maximum.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(120)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))


class SLT_Week9_Problem2(Scene):
    """Grating at 30 slits/mm, 1 cm wide: diffraction pattern with missing 5th order."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 9 — Problem 2: Grating Pattern", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Monochromatic lambda_0=450 nm, grating: 30 slits/mm, total width 1 cm.", font_size=26, color=WHITE),
            Text("5th-order interference peaks are missing.", font_size=26, color=WHITE),
            Text("(a) Find slit spacing d and number of slits N.", font_size=26, color=WHITE),
            Text("(b) Find slit width b.", font_size=26, color=WHITE),
            Text("(c) Find irradiance ratio I(3rd order)/I(0th order).", font_size=26, color=WHITE),
            Text("(d) At which angles do secondary maxima appear between 0th and 1st orders?", font_size=26, color=WHITE),
            Text("(e) Draw the diffraction spectrum quantitatively (I vs position on screen).", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        prob.next_to(slt_title, DOWN, buff=0.3)
        self.play(FadeIn(prob)); self.wait(120)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(120)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))


class SLT_Week9_Problem4(Scene):
    """Fabry-Perot: transmission maxima, finesse, FSR, ring pattern."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 9 — Problem 4: Fabry-Perot Analysis", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("FP interferometer in vacuum: two mirrors with reflectance R=0.9.", font_size=26, color=WHITE),
            Text("lambda_0=1 micron, f=0.1 m (lens focal length).", font_size=26, color=WHITE),
            Text("(a) At which distances d does transmitted irradiance show maxima?", font_size=26, color=WHITE),
            Text("    Derive the general transmitted irradiance formula.", font_size=26, color=WHITE),
            Text("(b) Find the finesse F of the FP.", font_size=26, color=WHITE),
            Text("(c) Find minimum d to resolve Delta_lambda=1 nm.", font_size=26, color=WHITE),
            Text("(d) Find the maximum resolvable wavelength difference (FSR).", font_size=26, color=WHITE),
            Text("(e) Plot I vs d for lambda_0 and lambda_0+1nm. Demonstrate resolution.", font_size=26, color=WHITE),
            Text("(f) Explain why non-normal incidence gives rings on the CCD.", font_size=26, color=WHITE),
            Text("    Show first bright ring is at r_1 = f*sqrt(lambda_0/d) on CCD.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        prob.next_to(slt_title, DOWN, buff=0.3)
        self.play(FadeIn(prob)); self.wait(120)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(120)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))

# slt_week7.py
# 31OPT Optics — SLT Week 7 (Set 7): Diffraction
from manim import *
from utils import *


class SLT_Week7_Problem1(Scene):
    """Single slit and double slit intensity profiles."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 7 — Problem 1: Single and Double Slit", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Laser at distance L from a single slit of width b. Screen behind slit.", font_size=26, color=WHITE),
            Text("(a) Describe the intensity pattern on the screen.", font_size=26, color=WHITE),
            Text("A second slit is cut with same width b, slit centre separation d=4b.", font_size=26, color=WHITE),
            Text("(b) Calculate the intensity profile I(x) for the two-slit setup.", font_size=26, color=WHITE),
            Text("(c) Sketch the resulting two-slit pattern on the screen.", font_size=26, color=WHITE),
            Text("Number of slits is doubled to 4, same spacing d=4b.", font_size=26, color=WHITE),
            Text("(d) Calculate I(x) for 4 slits.", font_size=26, color=WHITE),
            Text("(e) Sketch the four-slit pattern.", font_size=26, color=WHITE),
            Text("Now use 10 slits, all d=4b and width b.", font_size=26, color=WHITE),
            Text("(f) Calculate I(x) for 10 slits.", font_size=26, color=WHITE),
            Text("(g) Sketch the ten-slit pattern.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        prob.next_to(slt_title, DOWN, buff=0.3)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))


class SLT_Week7_Problem2(Scene):
    """Fresnel vs Fraunhofer conditions discussion + EHT resolving power."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 7 — Problem 2: Discussion & EHT", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("(a) Describe conditions needed for Fresnel and Fraunhofer diffraction.", font_size=26, color=WHITE),
            Text("    Discuss how each regime affects the pattern seen on the screen.", font_size=26, color=WHITE),
            Text("(b) The Event Horizon Telescope (EHT) has 8 telescopes around the Earth.", font_size=26, color=WHITE),
            Text("    EHT wavelength ~ 1.3 mm, Earth diameter ~ 12742 km.", font_size=26, color=WHITE),
            Text("    Discuss how a global telescope network achieves tremendous resolving power.", font_size=26, color=WHITE),
            Text("    Calculate the resolving power of the EHT.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))

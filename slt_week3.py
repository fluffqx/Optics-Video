# slt_week3.py
# 31OPT Optics — SLT Week 3 (Set 3): Fresnel Laws in a Prism
from manim import *
from utils import *


class SLT_Week3_Problem1(Scene):
    """Fresnel laws applied to a triangular prism."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 3 — Problem 1: Fresnel Laws in a Prism", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Triangular prism: n_glass=3/2, angles A=B=40 deg, C=100 deg.", font_size=26, color=WHITE),
            Text("Side AB covered by a perfectly reflecting mirror.", font_size=26, color=WHITE),
            Text("Laser enters perpendicular to one face, polarised in plane of table.", font_size=26, color=WHITE),
            Text("Laser power P_0. Always hits and totally reflects off side AB.", font_size=26, color=WHITE),
            Text("(a) After how many internal reflections does all power leave? (In practice?)", font_size=26, color=WHITE),
            Text("(b) Calculate laser power leaving from each side (stop after 2nd reflection).", font_size=26, color=WHITE),
            Text("(c) At Brewster incidence: calculate power from both sides.", font_size=26, color=WHITE),
            Text("(d) Find prism n for which outgoing beam is parallel to incoming beam.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        prob.next_to(slt_title, DOWN, buff=0.3)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))

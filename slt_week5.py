# slt_week5.py
# 31OPT Optics — SLT Week 5 (Set 5): Telescope and Microscope
from manim import *
from utils import *


class SLT_Week5_Problem1(Scene):
    """Telescope vs microscope, magnification, design choices."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 5 — Problem 1: Telescope", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("A telescope: f_ob=180 mm, f_e=60 mm. Objective focuses parallel rays.", font_size=26, color=WHITE),
            Text("Object placed at 2*f_ob from objective. Near point NP=25.4 cm.", font_size=26, color=WHITE),
            Text("(a) Sketch ray diagram of telescope used as microscope on close object.", font_size=26, color=WHITE),
            Text("(b) Explain difference in image formation: microscope vs telescope.", font_size=26, color=WHITE),
            Text("(c) Show the new lens separation should be 420 mm.", font_size=26, color=WHITE),
            Text("(d) Show the 'microscope' magnifying power is MP_m approx -4.2.", font_size=26, color=WHITE),
            Text("(e) Show original telescope magnification MP_t = -3.", font_size=26, color=WHITE),
            Text("(f) Discuss design choices to increase MP_t.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        prob.next_to(slt_title, DOWN, buff=0.3)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))

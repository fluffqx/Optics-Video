# slt_week2.py
# 31OPT Optics — SLT Week 2 (Set 2): Fresnel and Refraction
from manim import *
from utils import *


class SLT_Week2_Problem1(Scene):
    """Fermat's principle derivation of Snell's law."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 2 — Problem 1: Fermat's Principle", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Light travels from point Q (in medium n1) to P (in medium n2 > n1).", font_size=26, color=WHITE),
            Text("Point O is where the ray crosses the interface at position x.", font_size=26, color=WHITE),
            Text("(a) Show time from Q to O: t_QO = n1*sqrt(x^2+a^2)/c.", font_size=26, color=WHITE),
            Text("(b) Show time from O to P: t_OP = n2*sqrt((l-x)^2+b^2)/c.", font_size=26, color=WHITE),
            Text("(c) Minimise total time to re-derive Snell's law: n1*sin(theta1)=n2*sin(theta2).", font_size=26, color=WHITE),
            Text("(d) Discuss which angle is greater when n1<n2, n2<n1, and n1=n2.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))


class SLT_Week2_Problem2(Scene):
    """Radiation pressure discussion questions."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 2 — Problem 2: Radiation Pressure Discussion", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("A plane wave with I_0 reflects diffusely off a flat surface.", font_size=26, color=WHITE),
            Text("100% of light with I_0 hits the surface perpendicularly.", font_size=26, color=WHITE),
            Text("(a) Which is correct radiation pressure? I_0/c, 2I_0/c, or between/beyond?", font_size=26, color=WHITE),
            Text("(b) Explain how the photoelectric effect implies light is a particle.", font_size=26, color=WHITE),
            Text("(c) E-field of sunlight ~ 1 kV/m. Why doesn't standing in sunlight feel", font_size=26, color=WHITE),
            Text("    like continuous electrocution? (Hint: think about potentials.)", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))

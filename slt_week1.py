# slt_week1.py
# 31OPT Optics — SLT Week 1: Homework Problems (No Solutions)
from manim import *
from utils import *


class SLT_Week1_Problem1(Scene):
    """Matrix multiplication and ray tracing."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 1 — Problem 1: Matrix Multiplication", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("A light ray is described by vector v = [y, theta]^T.", font_size=26, color=WHITE),
            Text("Matrix A with elements a,b,c,d acts as: v1 = A * v0.", font_size=26, color=WHITE),
            Text("(a) Express y1 and theta1 in terms of a,b,c,d,y0,theta0.", font_size=26, color=WHITE),
            Text("(b) Apply matrix A twice to v0; express result in terms of a,b,c,d,y0,theta0.", font_size=26, color=WHITE),
            Text("Given M_T = [[1,d],[0,1]] and M_L = [[1,0],[-1/f,1]]:", font_size=26, color=WHITE),
            Text("(c) Find the vector after: travel d, pass through lens f, travel D.", font_size=26, color=WHITE),
            Text("(d) Discuss why this matrix method is used in simulations.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))


class SLT_Week1_Problem2(Scene):
    """Waves and equations: determine travelling wave, show wave equation solution."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 1 — Problem 2: Waves and Equations", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob_a = VGroup(
            Text("(a) Determine whether the following is a travelling wave:", font_size=26, color=WHITE),
        )
        prob_eq = MathTex(
            r"\Psi(y,t) = \sqrt{100\cos^2(4y^2 + 4ayt + a^2t^2)},\quad a > 0",
            font_size=34, color=E_COLOR)
        prob_a2 = Text("If so, find amplitude, speed, and propagation direction.", font_size=26, color=WHITE)

        prob_b = Text(
            "(b) Use the wave equation to show Psi = (x +/- vt)^n is a solution.",
            font_size=26, color=WHITE)

        prob = VGroup(prob_a, prob_eq, prob_a2, prob_b).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))

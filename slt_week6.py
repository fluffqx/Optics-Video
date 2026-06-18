# slt_week6.py
# 31OPT Optics — SLT Week 6 (Set 6): OPL, Dispersion, Polarisation
from manim import *
from utils import *


class SLT_Week6_Problem1(Scene):
    """Optical path length and interference of two paths."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 6 — Problem 1: Optical Path Length", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Two light paths A and B through slabs of glass (n_g) and water (n_w).", font_size=26, color=WHITE),
            Text("Path A: through air only (length l).", font_size=26, color=WHITE),
            Text("Path B: through 2 glass slabs (each thickness d_g) and water (thickness d_w).", font_size=26, color=WHITE),
            Text("Given: l=5 cm, d_g=0.5 cm, d_w=1 cm, n_g=1.5, n_w=1.33, lambda=500 nm.", font_size=26, color=WHITE),
            Text("Calculate OPD = OPL(B) - OPL(A) and determine if the beams are in phase.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))


class SLT_Week6_Problem2(Scene):
    """Group velocity derivation for dispersive medium."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 6 — Problem 2: Group Velocity", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("For a dispersive medium with n = n(lambda):", font_size=26, color=WHITE),
        )
        prob_eq = MathTex(
            r"v_g = v_p\left[1 + \frac{\lambda}{n}\frac{dn}{d\lambda}\right]",
            font_size=36, color=WAVE_COLOR)
        prob2 = VGroup(
            Text("Starting from v_g = d(omega)/dk and omega = v_p(k)*k = c*k/n(k),", font_size=26, color=WHITE),
            Text("derive the expression above. Show all steps clearly.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)

        full_prob = VGroup(prob, prob_eq, prob2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        full_prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(full_prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, full_prob, prompt)))


class SLT_Week6_Problem3(Scene):
    """Three polarisers at 0, 35, 55 degrees: find transmitted fraction."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 6 — Problem 3: Three Polarisers", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Natural light passes through three ideal linear polarisers.", font_size=26, color=WHITE),
            Text("Transmission axes: theta_1=0 deg, theta_2=35 deg, theta_3=55 deg.", font_size=26, color=WHITE),
            Text("Find the fraction of light passed by this combination.", font_size=26, color=WHITE),
            Text("Hint: natural light through first polariser transmits I_0/2.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(3)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(4)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))

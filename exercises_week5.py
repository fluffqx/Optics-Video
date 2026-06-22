# exercises_week5.py
# 31OPT Optics — Week 5: Polarisation & Jones Exercises (SC5)
from manim import *
from utils import *


class SC_Week5_Problem3(Scene):
    """Malus's law: partially polarised light through polariser at angle."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 5 — Problem 3 (Malus's Law)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Partially polarised light, I_0 = 400 W/m^2, passes through", font_size=26, color=WHITE),
            Text("a polariser with transmission axis at theta = 40 deg", font_size=26, color=WHITE),
            Text("to the polarisation direction. Find the transmitted irradiance.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(r"I = I_0 \cos^2\theta", font_size=40, color=INTENSITY_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"I = 400 \times \cos^2(40^{\circ})"
            r" = 400 \times (0.766)^2 = 400 \times 0.587 = 234.8 \text{ W/m}^2",
            font_size=32, color=GOLD)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp))
        self.play(Create(gold_box(s2))); self.wait(120)
        self.play(FadeOut(*self.mobjects))


class SC_Week5_Problem7(Scene):
    """QWP thickness calculation for red light in quartz."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 5 — Problem 7 (QWP Thickness)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Quartz: n_e=1.5534 (slow), n_o=1.5443 (fast), lambda_0=650 nm.", font_size=26, color=WHITE),
            Text("Find minimum thickness for a quarter-wave plate.", font_size=26, color=WHITE),
            Text("Which other QWP thicknesses also work?", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\Delta n = n_e - n_o = 1.5534 - 1.5443 = 0.0091",
            font_size=34, color=N_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"d_{\min} = \frac{\lambda_0}{4\Delta n}"
            r" = \frac{650\text{ nm}}{4\times0.0091}"
            r" = \frac{650}{0.0364} = 17.9\;\mu\text{m}",
            font_size=32, color=N_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(120)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"d_m = \frac{(4m+1)\lambda_0}{4\Delta n} = d_{\min} + m\frac{\lambda_0}{\Delta n},"
            r"\quad m = 0, 1, 2, \ldots",
            font_size=30, color=WHITE)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp))
        self.play(Create(gold_box(s2))); self.wait(120)
        self.play(FadeOut(*self.mobjects))


class SC_Week5_Problem4(Scene):
    """Nine polarisers each at 10 deg: total transmitted intensity."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 5 — Problem 4 (Nine Polarisers)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Nine ideal linear polarisers, each rotated 10 deg from the previous.", font_size=26, color=WHITE),
            Text("Light enters with I_0 and polarised along first polariser.", font_size=26, color=WHITE),
            Text("Find the fraction of I_0 transmitted.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\text{Each polariser transmits } \cos^2(10^{\circ})",
            font_size=34)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"\frac{I_{\text{out}}}{I_0} = \left[\cos^2(10^{\circ})\right]^9"
            r" = \left(0.9848\right)^9 = (0.9698)^9",
            font_size=32)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"\frac{I_{\text{out}}}{I_0} = 0.760 = 76.0\%",
            font_size=36, color=GOLD)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp))
        self.play(Create(gold_box(s3))); self.wait(120)
        self.play(FadeOut(*self.mobjects))

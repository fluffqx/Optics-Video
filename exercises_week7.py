# exercises_week7.py
# 31OPT Optics — Week 7: Diffraction Exercises (SC7 & SC8)
from manim import *
from utils import *


class SC_Week7_Problem1(Scene):
    """Single slit: intensity at given angle, width from minima."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 7 — Problem 1 (Single Slit)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Single slit, b=0.200 mm, lambda=550 nm, screen at L=2.00 m.", font_size=26, color=WHITE),
            Text("(a) Find the angular position of the first minimum.", font_size=26, color=WHITE),
            Text("(b) Find the width of the central maximum on the screen.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\sin\theta_1 = \frac{\lambda}{b} = \frac{550\times10^{-9}}{0.200\times10^{-3}}"
            r" = 2.75\times10^{-3}",
            font_size=32)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"\theta_1 = \arcsin(2.75\times10^{-3}) = 0.158^{\circ} = 2.75 \text{ mrad}",
            font_size=32, color=ANGLE_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"y_1 = L\tan\theta_1 \approx L\theta_1 = 2.00 \times 2.75\times10^{-3}"
            r" = 5.50 \text{ mm}",
            font_size=32)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"\text{Width of central max} = 2y_1 = 2\times5.50 = 11.0 \text{ mm}",
            font_size=32, color=GOLD)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp))
        self.play(Create(gold_box(VGroup(s2, s4)))); self.wait(120)
        self.play(FadeOut(*self.mobjects))


class SC_Week7_Problem5(Scene):
    """Grating resolving power vs Fabry-Perot comparison."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 7 — Problem 5 (Grating vs FP)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Grating: 256 mm wide, 300 slits/mm. lambda=500 nm.", font_size=26, color=WHITE),
            Text("R = 10^6. Find free spectral range.", font_size=26, color=WHITE),
            Text("FP: d=1 mm gap, finesse F=25. Compare R and FSR.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution — Grating:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"N = 300 \text{ slits/mm} \times 256 \text{ mm} = 76800 \text{ slits}",
            font_size=32)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"m = \frac{\mathcal{R}}{N} = \frac{10^6}{76800} \approx 13",
            font_size=32)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"\Delta\lambda_{\text{FSR}} = \frac{\lambda_{\min}}{m}"
            r" = \frac{500}{13} = 38.5 \text{ nm}",
            font_size=32, color=WAVE_COLOR)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(120)

        self.play(FadeOut(VGroup(sol_title, s1_grp, s2_grp, s3_grp)))
        fp_title = Text("Fabry-Perot Comparison:", font_size=30, color=GOLD)
        fp_title.next_to(prob_title, DOWN, buff=0.5)
        self.play(Write(fp_title))

        f1_lbl = step_label(4)
        f1 = MathTex(
            r"m_{\text{FP}} = \frac{2nd}{\lambda} = \frac{2\times1.0\times10^{-3}}{500\times10^{-9}}"
            r" = 4000",
            font_size=30)
        f1_grp = VGroup(f1_lbl, f1).arrange(RIGHT, buff=0.3)
        f1_grp.next_to(fp_title, DOWN, buff=0.3)
        self.play(Write(f1_grp)); self.wait(0.8)

        f2_lbl = step_label(5)
        f2 = MathTex(
            r"\mathcal{R}_{\text{FP}} = m_{\text{FP}} \times \mathcal{F}"
            r" = 4000 \times 25 = 100000 = 10^5",
            font_size=30, color=INTENSITY_COLOR)
        f2_grp = VGroup(f2_lbl, f2).arrange(RIGHT, buff=0.3)
        f2_grp.next_to(f1_grp, DOWN, buff=0.3)
        self.play(Write(f2_grp)); self.wait(0.8)

        f3_lbl = step_label(6)
        f3 = MathTex(
            r"\Delta\lambda_{\text{FSR,FP}} = \frac{\lambda^2}{2nd}"
            r" = \frac{(500)^2}{2\times10^6\text{ nm}} = 0.125 \text{ nm}",
            font_size=30, color=WAVE_COLOR)
        f3_grp = VGroup(f3_lbl, f3).arrange(RIGHT, buff=0.3)
        f3_grp.next_to(f2_grp, DOWN, buff=0.3)
        self.play(Write(f3_grp))

        compare = Text("Grating: R=10^6 (10x better), FSR=38.5 nm (much wider).",
                       font_size=26, color=GOLD)
        compare.next_to(f3_grp, DOWN, buff=0.3)
        self.play(FadeIn(compare))
        self.play(Create(gold_box(compare))); self.wait(120)
        self.play(FadeOut(*self.mobjects))


class SC_Week7_Problem10(Scene):
    """Laser beam spot on the Moon."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 7 — Problem 10 (Laser on Moon)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Laser: lambda=632.84 nm, beam diameter D=2 mm.", font_size=26, color=WHITE),
            Text("Distance to Moon: L = 3.76e8 m.", font_size=26, color=WHITE),
            Text("Find the light spot diameter on the Moon's surface.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\text{Angular divergence (Rayleigh): } \Delta\theta = 1.22\frac{\lambda}{D}",
            font_size=32)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"\Delta\theta = \frac{1.22 \times 632.84\times10^{-9}}{2\times10^{-3}}"
            r" = 3.86\times10^{-4} \text{ rad}",
            font_size=30, color=ANGLE_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"d_{\text{spot}} = \Delta\theta \times L"
            r" = 3.86\times10^{-4} \times 3.76\times10^8"
            r" = 1.45\times10^5 \text{ m} = 145 \text{ km}",
            font_size=30, color=GOLD)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp))
        self.play(Create(gold_box(s3))); self.wait(120)
        self.play(FadeOut(*self.mobjects))

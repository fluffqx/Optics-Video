# exercises_week8.py
# 31OPT Optics — Week 8: Fabry-Perot & Grating Exercises (SC8)
from manim import *
from utils import *


class SC_Week8_Problem9(Scene):
    """HeNe laser FP cavity: FSR and spectral width."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 8 — Problem 9 (HeNe Laser Cavity)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("633 nm HeNe laser, R=0.99, mirror spacing d=10.0 cm.", font_size=26, color=WHITE),
            Text("Find the free spectral range, finesse, and spectral width.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\Delta\nu_{\text{FSR}} = \frac{c}{2nd}"
            r" = \frac{3\times10^8}{2\times1.0\times0.10} = 1.50 \text{ GHz}",
            font_size=30, color=WAVE_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(120)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"\mathcal{F} = \frac{\pi\sqrt{R}}{1-R}"
            r" = \frac{\pi\sqrt{0.99}}{0.01} = \frac{\pi\times0.995}{0.01} = 312.6",
            font_size=30, color=N_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(120)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"\Delta\nu_{\text{FWHM}} = \frac{\Delta\nu_{\text{FSR}}}{\mathcal{F}}"
            r" = \frac{1.50\text{ GHz}}{312.6} = 4.80 \text{ MHz}",
            font_size=30, color=INTENSITY_COLOR)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(120)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"\Delta\lambda = \frac{\lambda^2\,\Delta\nu}{c}"
            r" = \frac{(633\times10^{-9})^2 \times 4.80\times10^6}{3\times10^8}"
            r" = 6.41\times10^{-15} \text{ m} = 6.41 \text{ fm}",
            font_size=28, color=GOLD)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp))
        self.play(Create(gold_box(VGroup(s2, s3)))); self.wait(120)
        self.play(FadeOut(*self.mobjects))


class SC_Week8_Problem10(Scene):
    """H/D isotope separation: FP suitability check."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 8 — Problem 10 (H/D Isotope FP)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("H: lambda=656.28 nm, D: lambda=656.10 nm (Delta=0.18 nm).", font_size=26, color=WHITE),
            Text("FP: R=0.95, FSR = 0.5 nm. Check if we can resolve the two lines.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\mathcal{F} = \frac{\pi\sqrt{R}}{1-R}"
            r" = \frac{\pi\sqrt{0.95}}{0.05} = 61.3",
            font_size=32, color=N_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"d = \frac{\lambda^2}{2n\,\Delta\lambda_{\text{FSR}}}"
            r" = \frac{(656.28)^2}{2\times0.5\times10^6\text{ nm}^2}"
            r"\approx 0.43 \text{ mm}",
            font_size=28)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"m = \frac{2nd}{\lambda} = \frac{2\times0.43\times10^{-3}}{656.28\times10^{-9}}"
            r" = 1310",
            font_size=28)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"\mathcal{R} = m\mathcal{F} = 1310\times61.3 = 80300",
            font_size=32, color=INTENSITY_COLOR)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp)); self.wait(0.8)

        s5_lbl = step_label(5)
        s5 = MathTex(
            r"(\Delta\lambda)_{\min} = \frac{\lambda}{\mathcal{R}}"
            r" = \frac{656.28}{80300} = 0.0082 \text{ nm} \ll 0.18 \text{ nm} \quad\checkmark",
            font_size=28, color=GOLD)
        s5_grp = VGroup(s5_lbl, s5).arrange(RIGHT, buff=0.3)
        s5_grp.next_to(s4_grp, DOWN, buff=0.3)
        self.play(Write(s5_grp))

        conclusion = Text("YES — the FP can easily resolve the H and D lines!", font_size=28, color=GOLD)
        conclusion.next_to(s5_grp, DOWN, buff=0.3)
        self.play(FadeIn(conclusion))
        self.play(Create(gold_box(conclusion))); self.wait(120)
        self.play(FadeOut(*self.mobjects))


class SC_Week8_Problem3(Scene):
    """Grating resolving power derivation and calculation."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 8 — Problem 3 (Grating Resolution)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("N=1000 slits, lambda_0=500 nm, m=2.", font_size=26, color=WHITE),
            Text("Derive the resolving power equation from scratch,", font_size=26, color=WHITE),
            Text("then find min resolvable wavelength difference Delta_lambda.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\text{Principal max at } \gamma = m\pi \;\Rightarrow\; d\sin\theta_m = m\lambda",
            font_size=32)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"\text{First minimum next to max: } N\gamma = (Nm+1)\pi"
            r"\;\Rightarrow\; d\sin\theta_{\min} = m\lambda + \frac{\lambda}{N}",
            font_size=28)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"\text{Rayleigh: min of }\lambda\text{ coincides with max of }\lambda+\Delta\lambda:"
            r"\quad m(\lambda+\Delta\lambda) = m\lambda + \frac{\lambda}{N}",
            font_size=26)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"\Delta\lambda = \frac{\lambda}{mN}"
            r"\;\Rightarrow\;\mathcal{R} = \frac{\lambda}{\Delta\lambda} = mN \quad\checkmark",
            font_size=32, color=GOLD)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp)); self.wait(0.8)

        s5_lbl = step_label(5)
        s5 = MathTex(
            r"\mathcal{R} = mN = 2\times1000 = 2000,"
            r"\quad \Delta\lambda_{\min} = \frac{500}{2000} = 0.25 \text{ nm}",
            font_size=30, color=INTENSITY_COLOR)
        s5_grp = VGroup(s5_lbl, s5).arrange(RIGHT, buff=0.3)
        s5_grp.next_to(s4_grp, DOWN, buff=0.3)
        self.play(Write(s5_grp))
        self.play(Create(gold_box(s5))); self.wait(120)
        self.play(FadeOut(*self.mobjects))

# exercises_week6.py
# 31OPT Optics — Week 6: Interference Exercises (SC6)
from manim import *
from utils import *


class SC_Week6_Problem1(Scene):
    """Young's double slit in water: fringe position."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 6 — Problem 1 (Young's in Water)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Young's double slit experiment performed in water (n_w=1.33).", font_size=26, color=WHITE),
            Text("Slit separation d, screen distance L, vacuum wavelength lambda_0.", font_size=26, color=WHITE),
            Text("Find the fringe spacing on the screen.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\text{Wavelength in water: } \lambda_w = \frac{\lambda_0}{n_w}",
            font_size=34, color=WAVE_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"\Delta y = \frac{\lambda_w L}{d} = \frac{\lambda_0 L}{n_w d}",
            font_size=38, color=GOLD)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp))

        note = Text("Fringe spacing is smaller by factor n_w compared to experiment in air.",
                    font_size=26, color=WHITE)
        note.next_to(s2_grp, DOWN, buff=0.3)
        self.play(FadeIn(note))
        self.play(Create(gold_box(s2))); self.wait(120)
        self.play(FadeOut(*self.mobjects))


class SC_Week6_Problem3(Scene):
    """Oil film on water: minimum thickness for constructive interference."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 6 — Problem 3 (Oil Film on Water)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Oil (n_oil=1.46) on water (n_w=1.33), lambda_0=550 nm.", font_size=26, color=WHITE),
            Text("(a) Find minimum nonzero thickness for constructive interference (normal incidence).", font_size=26, color=WHITE),
            Text("(b) Find minimum thickness for destructive interference.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\text{Air} \to \text{oil: } n_{\text{air}} < n_{\text{oil}}"
            r"\;\Rightarrow\; +\pi \text{ phase shift}",
            font_size=30, color=B_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"\text{Oil} \to \text{water: } n_{\text{oil}} > n_w"
            r"\;\Rightarrow\; 0 \text{ phase shift}",
            font_size=30, color=N_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"\text{Net reflection phase: } \pi"
            r"\;\Rightarrow\;\text{constructive: } 2n_{\text{oil}}t = \left(m+\tfrac{1}{2}\right)\lambda_0",
            font_size=28)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"t_{\min} = \frac{\lambda_0}{4n_{\text{oil}}}"
            r" = \frac{550}{4\times1.46} = 94.2 \text{ nm}",
            font_size=34, color=GOLD)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp))
        self.play(Create(gold_box(s4))); self.wait(1.5)

        self.play(FadeOut(VGroup(s3_grp, s4_grp)))
        s5_lbl = step_label(5)
        s5 = MathTex(
            r"\text{Destructive: }2n_{\text{oil}}t = m\lambda_0"
            r"\;\Rightarrow\; t_{\min}^{\text{dest}} = \frac{\lambda_0}{2n_{\text{oil}}}"
            r" = \frac{550}{2\times1.46} = 188.4 \text{ nm}",
            font_size=28, color=B_COLOR)
        s5_grp = VGroup(s5_lbl, s5).arrange(RIGHT, buff=0.3)
        s5_grp.next_to(s2_grp, DOWN, buff=0.4)
        self.play(Write(s5_grp))
        self.play(Create(gold_box(s5))); self.wait(120)
        self.play(FadeOut(*self.mobjects))


class SC_Week6_Problem4(Scene):
    """MgF2 anti-reflection coating on glass at 45 deg incidence."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 6 — Problem 4 (MgF2 AR Coating)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("MgF2 (n=1.38) coating on glass (n=1.52), lambda_0=550 nm.", font_size=26, color=WHITE),
            Text("(a) Find min thickness for destructive reflection at normal incidence.", font_size=26, color=WHITE),
            Text("(b) Find min thickness for incidence angle theta_i=45 deg.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\text{Both surfaces: air}\to\text{MgF}_2 \text{ and MgF}_2\to\text{glass}"
            r"\;\Rightarrow\;\text{both +}\pi\;\Rightarrow\;\Delta\varphi_{\text{refl}}=0",
            font_size=26)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"\text{Destructive reflection: } 2n_{\text{MgF}_2}t = \frac{\lambda_0}{2}"
            r"\;\Rightarrow\; t = \frac{\lambda_0}{4n_{\text{MgF}_2}}"
            r" = \frac{550}{4\times1.38} = 99.6 \text{ nm}",
            font_size=28, color=GOLD)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp))
        self.play(Create(gold_box(s2))); self.wait(1.5)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"\text{At }45^{\circ}: \sin\theta_t = \frac{n_{\text{air}}}{n_{\text{MgF}_2}}\sin45^{\circ}"
            r" = \frac{\sin45^{\circ}}{1.38} = 0.513"
            r"\;\Rightarrow\;\cos\theta_t = 0.858",
            font_size=26)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.4)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"t_{45} = \frac{\lambda_0}{4n_{\text{MgF}_2}\cos\theta_t}"
            r" = \frac{550}{4\times1.38\times0.858} = 116.1 \text{ nm}",
            font_size=28, color=GOLD)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp))
        self.play(Create(gold_box(s4))); self.wait(120)
        self.play(FadeOut(*self.mobjects))

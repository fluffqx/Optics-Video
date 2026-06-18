# exercises_week3.py
# 31OPT Optics — Week 3: Geometric Optics Exercises (SC3)
from manim import *
from utils import *


class SC_Week3_Problem1(Scene):
    """Refraction at spherical surface: fish apparent depth."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 3 — Problem 1 (SC3 P1)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("A fish is at depth d under water (n_w=1.33, n_a=1.00).", font_size=26, color=WHITE),
            Text("(a) Show the apparent depth for a ray at angle alpha_a is:", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        prob_eq = MathTex(
            r"d^* = \frac{d\cos\alpha_a}{\sqrt{(n_w/n_a)^2 - \sin^2\alpha_a}}",
            font_size=36, color=N_COLOR)
        prob_eq.next_to(prob, DOWN, buff=0.3)
        prob2 = Text("(b) What is the apparent depth looking straight down (alpha_a = 0)?",
                     font_size=26, color=WHITE)
        prob2.next_to(prob_eq, DOWN, buff=0.3)
        self.play(FadeIn(prob), FadeIn(prob_eq), FadeIn(prob2)); self.wait(2)
        self.play(FadeOut(VGroup(prob, prob_eq, prob2)))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(r"\text{Snell's law at surface: } n_a\sin\alpha_a = n_w\sin\alpha_w",
                     font_size=32)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"r = R\sin\alpha_w = x\sin\alpha_a \;\Rightarrow\; \frac{r}{R} = \frac{\sin\alpha_w}{\sin\alpha_a} = \frac{n_a}{n_w}",
            font_size=30)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"d^* = \frac{r\cos\alpha_a}{r/R} = \frac{d\cos\alpha_a}{\sqrt{(n_w/n_a)^2-\sin^2\alpha_a}} \quad\checkmark",
            font_size=30, color=N_COLOR)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(1)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"\text{Part (b): }\alpha_a = 0 \;\Rightarrow\;"
            r"d^* = \frac{d}{\sqrt{(n_w/n_a)^2}} = \frac{d\,n_a}{n_w} = \frac{d}{1.33} = 0.75d",
            font_size=30, color=GOLD)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp))
        self.play(Create(gold_box(s4))); self.wait(2)
        self.play(FadeOut(*self.mobjects))


class SC_Week3_Problem3(Scene):
    """Thin lens: image distance and magnification."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 3 — Problem 3 (Thin Lens)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("A converging lens, f=25 mm, with object at s_o=30 mm.", font_size=26, color=WHITE),
            Text("Find image distance s_i and magnification m.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(2); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(r"\frac{1}{s_i} = \frac{1}{f} - \frac{1}{s_o}"
                     r" = \frac{1}{25} - \frac{1}{30} = \frac{6-5}{150} = \frac{1}{150}",
                     font_size=34)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(1)

        s2_lbl = step_label(2)
        s2 = MathTex(r"s_i = 150 \text{ mm (real image, on far side)}",
                     font_size=36, color=GOLD)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(1)

        s3_lbl = step_label(3)
        s3 = MathTex(r"m = -\frac{s_i}{s_o} = -\frac{150}{30} = -5"
                     r"\text{ (inverted, 5x magnified)}",
                     font_size=34, color=WHITE)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp))
        self.play(Create(gold_box(VGroup(s2, s3)))); self.wait(2)
        self.play(FadeOut(*self.mobjects))

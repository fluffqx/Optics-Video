# exercises_week4.py
# 31OPT Optics — Week 4: Matrix Optics Exercises (SC4)
from manim import *
from utils import *


class SC_Week4_Problem1(Scene):
    """Beam expander system matrix derivation."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 4 — Problem 1 (Beam Expander)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("A beam expander has two lenses f1 and f2 separated by d = f1+f2.", font_size=26, color=WHITE),
            Text("Show the system matrix is:", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        prob_eq = MathTex(
            r"M_S^{\text{bexb}} = \begin{pmatrix} -f_2/f_1 & f_1+f_2 \\ 0 & -f_1/f_2 \end{pmatrix}",
            font_size=36, color=N_COLOR)
        prob_eq.next_to(prob, DOWN, buff=0.3)
        self.play(FadeIn(prob), FadeIn(prob_eq)); self.wait(2)
        self.play(FadeOut(VGroup(prob, prob_eq)))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1a = MathTex(r"M_{L1}=\begin{pmatrix}1&0\\-1/f_1&1\end{pmatrix}", font_size=24)
        s1b = MathTex(r"M_D=\begin{pmatrix}1&f_1{+}f_2\\0&1\end{pmatrix}", font_size=24)
        s1c = MathTex(r"M_{L2}=\begin{pmatrix}1&0\\-1/f_2&1\end{pmatrix}", font_size=24)
        s1 = VGroup(s1a, s1b, s1c).arrange(RIGHT, buff=0.3)
        safe_scale(s1, max_width=12.5)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(1)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"M_S = M_{L2} \cdot M_D \cdot M_{L1}"
            r" \quad\text{(right-to-left)}",
            font_size=30)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"\text{First: }M_D M_{L1}="
            r"\begin{pmatrix}1&f_1+f_2\\0&1\end{pmatrix}"
            r"\begin{pmatrix}1&0\\-1/f_1&1\end{pmatrix}"
            r"=\begin{pmatrix}1-(f_1+f_2)/f_1 & f_1+f_2\\-1/f_1&1\end{pmatrix}",
            font_size=24)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(1)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"= \begin{pmatrix}-f_2/f_1 & f_1+f_2\\-1/f_1&1\end{pmatrix}",
            font_size=30, color=N_COLOR)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp)); self.wait(0.8)

        s5_lbl = step_label(5)
        s5 = MathTex(
            r"M_S = \begin{pmatrix}1&0\\-1/f_2&1\end{pmatrix}"
            r"\begin{pmatrix}-f_2/f_1&f_1+f_2\\-1/f_1&1\end{pmatrix}"
            r"= \begin{pmatrix}-f_2/f_1&f_1+f_2\\0&-f_1/f_2\end{pmatrix}\quad\checkmark",
            font_size=24, color=GOLD)
        s5_grp = VGroup(s5_lbl, s5).arrange(RIGHT, buff=0.3)
        s5_grp.next_to(s4_grp, DOWN, buff=0.3)
        self.play(Write(s5_grp))
        self.play(Create(gold_box(s5))); self.wait(2)
        self.play(FadeOut(*self.mobjects))


class SC_Week4_Problem3(Scene):
    """Microscope design with two lenses f=25mm."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        prob_title = Text("SC Week 4 — Problem 3 (Microscope)", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("Two biconvex lenses, both f=25.0 mm. Object 27.0 mm in front of objective.", font_size=26, color=WHITE),
            Text("(a) How far apart should the lenses be?", font_size=26, color=WHITE),
            Text("(b) What magnification do we expect?", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(2); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"\text{Objective: } \frac{1}{s_{i1}} = \frac{1}{f} - \frac{1}{s_{o1}}"
            r" = \frac{1}{25} - \frac{1}{27} = \frac{27-25}{675} = \frac{2}{675}",
            font_size=30)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(1)

        s2_lbl = step_label(2)
        s2 = MathTex(r"s_{i1} = 337.5 \text{ mm}", font_size=34, color=N_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"\text{For relaxed eye: image from eyepiece at infinity}"
            r"\;\Rightarrow\; s_{o2} = f_e = 25 \text{ mm}",
            font_size=28)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4 = MathTex(
            r"d = s_{i1} + s_{o2} = 337.5 + 25 = 362.5 \text{ mm}",
            font_size=34, color=GOLD)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp)); self.wait(0.8)

        s5_lbl = step_label(5)
        s5 = MathTex(
            r"m_{\text{obj}} = -\frac{s_{i1}}{s_{o1}} = -\frac{337.5}{27} = -12.5",
            font_size=32)
        s5_grp = VGroup(s5_lbl, s5).arrange(RIGHT, buff=0.3)
        s5_grp.next_to(s4_grp, DOWN, buff=0.3)
        self.play(Write(s5_grp))

        note = MathTex(
            r"\text{Total magnification: } M \approx m_{\text{obj}} \times \frac{25\text{cm}}{f_e}"
            r" = -12.5 \times 10 = -125",
            font_size=30, color=GOLD)
        note.next_to(s5_grp, DOWN, buff=0.3)
        self.play(Write(note))
        self.play(Create(gold_box(VGroup(s4, note)))); self.wait(2)
        self.play(FadeOut(*self.mobjects))

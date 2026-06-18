# week4_matrix_polarisation.py
# 31OPT Optics — Week 4: Matrix Optics & Polarisation Basics
from manim import *
from utils import *


class Week4TitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "WEEK 4",
            "Matrix Optics, Superposition & Polarisation Basics",
            "Bennett Ch. 5.5, 7.1-7.3.1, 6.1-6.2"
        )
        self.play(FadeIn(card)); self.wait(2); self.play(FadeOut(card))


class MatrixOpticsIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Matrix Methods in Paraxial Optics", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        intro = section_intro([
            "Any paraxial optical system can be described by a 2x2 ray transfer matrix.",
            "A ray is described by its height y and angle theta from the optical axis.",
            "Three elementary matrices: translation, refraction, reflection.",
            "Multiply them in order (right to left) to get the system matrix.",
            "From the system matrix elements A,B,C,D we extract all cardinal points."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.wait(1); self.play(FadeOut(VGroup(title, intro)))


class MatrixEquations(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Ray Transfer Matrices", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        # Ray vector
        ray_vec = MathTex(
            r"\text{Ray vector: } \begin{pmatrix} y \\ \theta \end{pmatrix}",
            font_size=38, color=WHITE
        )
        ray_vec_label = Text(
            "y = height from optical axis,   theta = angle from axis (paraxial: small angle)",
            font_size=26, color=WHITE
        )
        ray_group = VGroup(ray_vec, ray_vec_label).arrange(DOWN, buff=0.2)
        self.play(Write(ray_group)); self.wait(1.2); self.play(FadeOut(ray_group))

        # Translation
        t_title = Text("1. Translation (free propagation, distance d):", font_size=30, color=GOLD)
        t_title.next_to(title, DOWN, buff=0.4)
        M_T = MathTex(
            r"M_T = \begin{pmatrix} 1 & d \\ 0 & 1 \end{pmatrix}",
            font_size=44, color=E_COLOR
        )
        M_T_meaning = Text(
            "Ray travels distance d: height increases by d*theta, angle unchanged.",
            font_size=26, color=WHITE
        )
        t_group = VGroup(t_title, M_T, M_T_meaning).arrange(DOWN, buff=0.25)
        self.play(Write(t_group)); self.wait(1.5); self.play(FadeOut(t_group))

        # Refraction
        r_title = Text("2. Refraction at spherical surface (n1 to n2, radius R):",
                       font_size=30, color=GOLD)
        r_title.next_to(title, DOWN, buff=0.4)
        M_R = MathTex(
            r"M_R = \begin{pmatrix} 1 & 0 \\"
            r" -\dfrac{n_2 - n_1}{n_2 R} & \dfrac{n_1}{n_2} \end{pmatrix}",
            font_size=42, color=N_COLOR
        )
        r_group = VGroup(r_title, M_R).arrange(DOWN, buff=0.3)
        self.play(Write(r_group)); self.wait(1.5); self.play(FadeOut(r_group))

        # Thin lens
        l_title = Text("3. Thin lens (focal length f):", font_size=30, color=GOLD)
        l_title.next_to(title, DOWN, buff=0.4)
        M_L = MathTex(
            r"M_{\text{lens}} = \begin{pmatrix} 1 & 0 \\ -1/f & 1 \end{pmatrix}",
            font_size=44, color=N_COLOR
        )
        l_note = Text("Derived from two refraction matrices with d→0 in between.",
                      font_size=26, color=WHITE)
        l_group = VGroup(l_title, M_L, l_note).arrange(DOWN, buff=0.25)
        self.play(Write(l_group)); self.wait(1.5); self.play(FadeOut(l_group))

        # Mirror
        m_title = Text("4. Reflection at spherical mirror (radius R):", font_size=30, color=GOLD)
        m_title.next_to(title, DOWN, buff=0.4)
        M_M = MathTex(
            r"M_{\text{mirror}} = \begin{pmatrix} 1 & 0 \\ -2/R & 1 \end{pmatrix}",
            font_size=44, color=B_COLOR
        )
        m_group = VGroup(m_title, M_M).arrange(DOWN, buff=0.3)
        self.play(Write(m_group)); self.wait(1.5); self.play(FadeOut(m_group))

        # System matrix
        sys_title = Text("System (Ray Transfer) Matrix:", font_size=32, color=GOLD)
        sys_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(sys_title))

        M_sys = MathTex(
            r"M_{\text{sys}} = M_N \cdots M_2 \cdot M_1 \quad \text{(right-to-left order)}",
            font_size=36, color=GOLD
        )
        transform = MathTex(
            r"\begin{pmatrix} y_2 \\ \theta_2 \end{pmatrix}"
            r"= M_{\text{sys}} \begin{pmatrix} y_1 \\ \theta_1 \end{pmatrix}",
            font_size=42
        )
        M_elements = MathTex(
            r"M_{\text{sys}} = \begin{pmatrix} A & B \\ C & D \end{pmatrix}",
            font_size=40
        )
        sys_group = VGroup(M_sys, transform, M_elements).arrange(DOWN, buff=0.4)
        sys_group.next_to(sys_title, DOWN, buff=0.3)
        for item in sys_group:
            self.play(Write(item)); self.wait(0.8)

        # Cardinal points
        self.play(FadeOut(VGroup(sys_title, sys_group)))
        cardinal_title = Text("Cardinal Points from System Matrix M = [A B; C D]:",
                              font_size=28, color=GOLD)
        cardinal_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(cardinal_title))

        cardinals = VGroup(
            MathTex(r"f_{\text{eff}} = -\frac{1}{C} \quad \text{(effective focal length)}",
                    font_size=34, color=N_COLOR),
            MathTex(r"f_{\text{front}} = -\frac{A}{C} \quad \text{(front focal point)}",
                    font_size=34),
            MathTex(r"f_{\text{back}} = \frac{1-A}{C} \quad \text{(back focal point)}",
                    font_size=34),
            MathTex(r"h_f = \frac{1-A}{C} \quad \text{(front principal plane)}",
                    font_size=34),
            MathTex(r"h_b = \frac{D-1}{C} \quad \text{(back principal plane)}",
                    font_size=34),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        cardinals.next_to(cardinal_title, DOWN, buff=0.3)
        for c in cardinals:
            self.play(FadeIn(c)); self.wait(0.6)

        # Worked example: two lenses
        self.play(FadeOut(VGroup(cardinal_title, cardinals)))
        ex_title = Text(
            "Example: lens f1=20cm then free space d=10cm then lens f2=15cm. Find M_sys.",
            font_size=22, color=GOLD
        )
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        s1 = MathTex(
            r"M_{\text{sys}} = M_{L2} \cdot M_T \cdot M_{L1}",
            font_size=34)
        s2 = MathTex(
            r"= \begin{pmatrix}1&0\\-1/15&1\end{pmatrix}"
            r"\begin{pmatrix}1&10\\0&1\end{pmatrix}"
            r"\begin{pmatrix}1&0\\-1/20&1\end{pmatrix}",
            font_size=30)
        s3 = MathTex(
            r"\text{First: }M_T\cdot M_{L1}"
            r"=\begin{pmatrix}1&10\\0&1\end{pmatrix}\begin{pmatrix}1&0\\-1/20&1\end{pmatrix}"
            r"=\begin{pmatrix}1-10/20 & 10\\ -1/20 & 1\end{pmatrix}"
            r"=\begin{pmatrix}0.5 & 10\\ -0.05 & 1\end{pmatrix}",
            font_size=26)
        s4 = MathTex(
            r"M_{\text{sys}}=\begin{pmatrix}1&0\\-1/15&1\end{pmatrix}"
            r"\begin{pmatrix}0.5&10\\-0.05&1\end{pmatrix}"
            r"=\begin{pmatrix}0.5&10\\-0.0833&-0.333\end{pmatrix}",
            font_size=26)
        s5 = MathTex(
            r"f_{\text{eff}} = -\frac{1}{C} = -\frac{1}{-0.0833} = 12\text{ cm}",
            font_size=30, color=GOLD)
        steps = VGroup(s1, s2, s3, s4, s5).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        steps.next_to(ex_title, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s), run_time=1.0); self.wait(0.6)
        self.play(Create(gold_box(s5)))
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, steps)))

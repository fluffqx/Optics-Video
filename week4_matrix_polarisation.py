# week4_matrix_polarisation.py  —  Week 4: Matrix Optics  (v2)
# Source: Bennett Ch. 5.5, 7.1-7.3.1, 6.1-6.2
from manim import *
from utils import *


class Week4TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEK 4",
            "Matrix Optics, Superposition & Polarisation Basics",
            "Bennett Ch. 5.5, 7.1–7.3.1, 6.1–6.2"
        )
        self.play(FadeIn(card)); self.wait(157.5); self.play(FadeOut(card))


class MatrixOpticsIntro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Why Matrix Methods?  (Bennett Section 5.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Any sequence of optical elements can be represented by a SINGLE 2×2 matrix.",
            "This is the ray transfer matrix method — immensely powerful for optical design.",
            "",
            "A ray near the optical axis is described by two numbers:",
            "  y = height from the optical axis  [m]",
            "  θ = angle the ray makes with the axis  [rad] (paraxial: θ small)",
            "",
            "We write this as a column vector:  [y, θ]ᵀ",
            "",
            "Each optical element maps [y_in, θ_in] to [y_out, θ_out]  via a 2×2 matrix.",
            "For a sequence of N elements: M_sys = M_N · ... · M_2 · M_1  (right-to-left!)",
            "The LAST element on the right corresponds to the FIRST element encountered.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(21.5)
        self.wait(38.1); self.play(FadeOut(VGroup(title, intro)))


class MatrixEquations(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("The Elementary Ray Transfer Matrices", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        matrices = [
            ("1. Free Propagation (Translation) — distance d  (Bennett Eq. 5.59):",
             r"M_T = \begin{pmatrix}1 & d \\ 0 & 1\end{pmatrix}",
             ["A ray travels distance d in free space.",
              "Height increases: y_out = y_in + d·θ_in",
              "Angle unchanged: θ_out = θ_in  (no bending in free space)"],
             E_COLOR),
            ("2. Thin Lens — focal length f  (Bennett Eq. 5.64):",
             r"M_L = \begin{pmatrix}1 & 0 \\ -1/f & 1\end{pmatrix}",
             ["A thin lens changes the ray angle without changing its height.",
              "Height unchanged: y_out = y_in  (thin lens → zero thickness)",
              "Angle changes: θ_out = θ_in − y_in/f  (focusing/defocusing)"],
             N_COLOR),
            ("3. Refraction at Spherical Surface — n₁→n₂, radius R  (Bennett Eq. 5.62):",
             r"M_R = \begin{pmatrix}1 & 0 \\ -\frac{n_2-n_1}{n_2 R} & \frac{n_1}{n_2}\end{pmatrix}",
             ["Height unchanged at the surface.",
              "Angle changes according to paraxial Snell's law.",
              "This matrix is derived directly from Snell's law in the paraxial limit."],
             N_COLOR),
            ("4. Reflection at Spherical Mirror — radius R  (Bennett Eq. 5.66):",
             r"M_M = \begin{pmatrix}1 & 0 \\ -2/R & 1\end{pmatrix}",
             ["Same form as the thin lens matrix.",
              "Equivalent to a thin lens with f_m = R/2 (as expected from mirror equation).",
              "Valid for paraxial rays near the mirror axis."],
             B_COLOR),
        ]

        for m_name, latex, desc_lines, color in matrices:
            m_title = Text(m_name, font_size=24, color=GOLD)
            m_title.next_to(title, DOWN, buff=0.5)
            safe_scale(m_title, max_width=13.5)
            self.play(Write(m_title))

            eq = MathTex(latex, font_size=44, color=color)
            eq.next_to(m_title, DOWN, buff=0.3)
            self.play(Write(eq)); self.wait(3.9)

            desc = section_intro(desc_lines, font_size=26)
            desc.next_to(eq, DOWN, buff=0.35)
            for l in desc: self.play(FadeIn(l)); self.wait(17.7)
            self.wait(44.2); self.play(FadeOut(VGroup(m_title, eq, desc)))


class SystemMatrixCardinalPoints(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("System Matrix & Cardinal Points  (Bennett Section 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Multiply all element matrices (right-to-left) to get the SYSTEM matrix:",
            "M_sys = M_N · ... · M_2 · M_1",
            "The system matrix has the form:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(10.5)
        self.wait(23.2)

        M_sys = MathTex(
            r"M_{\text{sys}} = \begin{pmatrix}A & B \\ C & D\end{pmatrix}",
            font_size=50, color=GOLD)
        M_sys.next_to(intro, DOWN, buff=0.35)
        self.play(Write(M_sys)); self.wait(16.0)

        # Cardinal points
        cardinal_title = Text("Cardinal Points from M_sys = [A B; C D]  (Bennett Eq. 5.77-5.80):", font_size=26, color=GOLD)
        cardinal_title.next_to(title, DOWN, buff=0.5)
        safe_scale(cardinal_title, max_width=13.5)
        self.play(Write(cardinal_title))

        cardinals = eq_table([
            (r"f_{\text{eff}} = -\frac{1}{C}",   "effective focal length of the entire system", N_COLOR),
            (r"f_{\text{front}} = -\frac{A}{C}",  "front focal distance (from first element to front focus)", WHITE),
            (r"f_{\text{back}} = \frac{D-1}{C}",  "back focal distance (from last element to rear focus)", WHITE),
            (r"h_f = \frac{1-A}{C}",               "position of front principal plane", WHITE),
            (r"h_b = \frac{D-1}{C}",               "position of rear principal plane", WHITE),
            (r"\det(M) = AD - BC = 1",             "determinant is always 1 (energy conservation)", GOLD),
        ], eq_fs=32, lbl_fs=22, buff=0.25)
        cardinals.next_to(cardinal_title, DOWN, buff=0.3)
        for row in cardinals: self.play(FadeIn(row)); self.wait(12.1)
        self.wait(2.0); self.play(FadeOut(VGroup(title, cardinal_title, cardinals)))


class MatrixExample(Scene):
    """Full example: beam expander — Bennett Example"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Matrix Example: Beam Expander", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        prob = section_intro([
            "A beam expander uses two lenses f₁ and f₂ separated by d = f₁+f₂.",
            "Find the system matrix M_sys = M_L2 · M_T · M_L1.",
            "Show it expands the beam by factor f₂/f₁ without focusing.",
        ], font_size=27)
        prob.next_to(title, DOWN, buff=0.4)
        for l in prob: self.play(FadeIn(l)); self.wait(13.2)
        self.wait(47.4)

        solver = StepSolver(self, prob, start_buff=0.4)
        solver.add_step(1,
            r"M_{L1} = \begin{pmatrix}1&0\\-1/f_1&1\end{pmatrix},\;"
            r"M_T = \begin{pmatrix}1&f_1+f_2\\0&1\end{pmatrix},\;"
            r"M_{L2} = \begin{pmatrix}1&0\\-1/f_2&1\end{pmatrix}",
            "write down the three element matrices")
        solver.add_step(2,
            r"M_T M_{L1} = \begin{pmatrix}1&f_1+f_2\\0&1\end{pmatrix}"
            r"\begin{pmatrix}1&0\\-1/f_1&1\end{pmatrix}"
            r"= \begin{pmatrix}1-\frac{f_1+f_2}{f_1}&f_1+f_2\\-1/f_1&1\end{pmatrix}"
            r"= \begin{pmatrix}-f_2/f_1&f_1+f_2\\-1/f_1&1\end{pmatrix}",
            "multiply T × L1 first (standard matrix multiplication)")
        solver.add_step(3,
            r"M_{\text{sys}} = M_{L2}(M_T M_{L1}) = \begin{pmatrix}-f_2/f_1&f_1+f_2\\0&-f_1/f_2\end{pmatrix}",
            "multiply L2 × (result): C=0 means no net focusing — parallel in, parallel out!", GOLD)
        solver.add_step(4,
            r"f_{\text{eff}} = -1/C \to \infty \quad\text{(afocal system)}",
            "C=0 → infinite effective focal length → beam expander works perfectly")
        solver.add_step(5,
            r"\text{Beam magnification} = A = -f_2/f_1 \quad\text{(ratio of beam diameters)}",
            "A element tells us the transverse magnification of the beam", GOLD)
        solver.finalize()

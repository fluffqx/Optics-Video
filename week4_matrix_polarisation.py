# week4_matrix_polarisation.py — Week 4: Matrix Optics + Wave Superposition + Polarization Basics
# Source: Bennett Ch. 5.5, 7.1-7.3.1, 6.1-6.2
from manim import *
from utils import *


def pg(scene, title, lines, wait, fs=27):
    texts = [Text(l, font_size=fs, color=WHITE) for l in lines if l.strip()]
    if not texts: return
    block = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    safe_scale(block, max_width=13.0, max_height=4.0)
    block.next_to(title, DOWN, buff=0.5)
    scene.play(FadeIn(block, run_time=0.4))
    scene.wait(wait)
    scene.play(FadeOut(block, run_time=0.4))


class Week4TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/Week4TitleCard.mp3", time_offset=0)
        card = make_title_card(
            "WEEK 4",
            "Matrix Optics, Wave Superposition & Polarisation",
            "Bennett Ch. 5.5, 7.1–7.3.1, 6.1–6.2  |  Lecture 4.1"
        )
        self.play(FadeIn(card))
        self.wait(136.8)
        self.play(FadeOut(card))


class MatrixOpticsIntro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/MatrixOpticsIntro.mp3", time_offset=0)
        title = Text("Why Matrix Methods? (Bennett Section 5.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "Any sequence of optical elements can be represented by a SINGLE 2x2 matrix.",
            "This is the ray transfer matrix method — immensely powerful for optical design.",
            "Computers use exactly this method to design camera lenses with 20+ elements.",
        ], wait=18.3)

        pg(self, title, [
            "A ray near the optical axis is described by two numbers:",
            "  y = height from the optical axis  [m]",
            "  theta = angle the ray makes with the axis  [rad]",
            "Written as a column vector: [y, theta]^T",
        ], wait=19.7)

        pg(self, title, [
            "Each optical element maps [y_in, theta_in] to [y_out, theta_out] via a 2x2 matrix.",
            "For a sequence of N elements: M_sys = M_N x ... x M_2 x M_1  (right-to-left!)",
            "The FIRST element encountered goes on the RIGHT of the product.",
            "This is the standard convention — multiplying LEFT-TO-RIGHT gives wrong result.",
        ], wait=12.8)

        self.play(FadeOut(title))


class MatrixEquations(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/MatrixEquations.mp3", time_offset=0)
        title = Text("The Elementary Ray Transfer Matrices", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        matrices = [
            ("Free Propagation — distance d  (Bennett Eq. 5.59)",
             r"M_T = \begin{pmatrix}1 & d \\ 0 & 1\end{pmatrix}",
             ["y_out = y_in + d * theta_in  (height increases as ray travels)",
              "theta_out = theta_in  (angle unchanged in free space — no optical element)"],
             E_COLOR),
            ("Thin Lens — focal length f  (Bennett Eq. 5.64)",
             r"M_L = \begin{pmatrix}1 & 0 \\ -1/f & 1\end{pmatrix}",
             ["y_out = y_in  (lens has zero thickness — height unchanged)",
              "theta_out = theta_in - y_in/f  (lens bends the ray)"],
             N_COLOR),
            ("Refraction at Spherical Surface — n1 to n2, radius R  (Bennett Eq. 5.62)",
             r"M_R = \begin{pmatrix}1 & 0 \\ -\frac{n_2-n_1}{n_2 R} & \frac{n_1}{n_2}\end{pmatrix}",
             ["Height unchanged at the surface.",
              "Angle changes by paraxial Snell's law — derived directly from it."],
             N_COLOR),
            ("Spherical Mirror — radius R  (Bennett Eq. 5.66)",
             r"M_M = \begin{pmatrix}1 & 0 \\ -2/R & 1\end{pmatrix}",
             ["Same form as thin lens matrix with f_m = R/2.",
              "Consistent with the mirror equation derived in Week 3."],
             B_COLOR),
        ]

        for m_name, latex, desc_lines, color in matrices:
            m_title = Text(m_name, font_size=24, color=GOLD)
            m_title.next_to(title, DOWN, buff=0.45)
            safe_scale(m_title, max_width=13.5)
            eq = MathTex(latex, font_size=44, color=color)
            eq.next_to(m_title, DOWN, buff=0.25)
            safe_scale(eq, max_width=11.0)
            desc = VGroup(*[Text(l, font_size=25, color=WHITE) for l in desc_lines])
            desc.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            desc.next_to(eq, DOWN, buff=0.3)
            safe_scale(desc, max_width=13.0)
            block = VGroup(m_title, eq, desc)
            self.play(FadeIn(block, run_time=0.4))
            self.wait(57.1)
            self.play(FadeOut(block, run_time=0.4))

        self.play(FadeOut(title))


class SystemMatrixCardinalPoints(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/SystemMatrixCardinalPoints.mp3", time_offset=0)
        title = Text("System Matrix & Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "Multiply all element matrices right-to-left to get the SYSTEM matrix.",
            "The system matrix has the general form [A B; C D].",
        ], wait=8.7)

        M_sys = MathTex(r"M_{\text{sys}} = \begin{pmatrix}A & B \\ C & D\end{pmatrix}",
                        font_size=52, color=GOLD)
        M_sys.next_to(title, DOWN, buff=0.5)
        self.play(Write(M_sys))
        self.wait(19.8)
        self.play(FadeOut(M_sys))

        cardinal_title = Text("Cardinal Points from [A B; C D]:", font_size=28, color=GOLD)
        cardinal_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(cardinal_title))

        cardinals = eq_table([
            (r"f_{\text{eff}} = -\frac{1}{C}", "effective focal length of entire system", N_COLOR),
            (r"f_{\text{front}} = -\frac{A}{C}", "front focal distance", WHITE),
            (r"f_{\text{back}} = \frac{D-1}{C}", "back focal distance", WHITE),
            (r"\det(M) = AD-BC = 1", "determinant always = 1  (energy conservation)", GOLD),
        ], eq_fs=32, lbl_fs=22, buff=0.28)
        cardinals.next_to(cardinal_title, DOWN, buff=0.3)
        safe_scale(cardinals, max_height=3.5)
        self.play(FadeIn(cardinals))
        self.wait(53.8)
        self.play(FadeOut(VGroup(title, cardinal_title, cardinals)))


class MatrixExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/MatrixExample.mp3", time_offset=0)
        title = Text("Matrix Example: Beam Expander", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "A beam expander uses two lenses f1 and f2 separated by d = f1+f2.",
            "Goal: expand beam diameter by ratio f2/f1 with no net focusing (afocal).",
            "Find: system matrix M = M_L2 x M_T x M_L1",
        ], wait=11.1)

        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1,
            r"M_{L1}=\begin{pmatrix}1&0\\-1/f_1&1\end{pmatrix},\;"
            r"M_T=\begin{pmatrix}1&f_1+f_2\\0&1\end{pmatrix},\;"
            r"M_{L2}=\begin{pmatrix}1&0\\-1/f_2&1\end{pmatrix}",
            "write down the three element matrices")
        solver.add_step(2,
            r"M_T M_{L1}=\begin{pmatrix}-f_2/f_1&f_1+f_2\\-1/f_1&1\end{pmatrix}",
            "multiply T x L1 first")
        solver.add_step(3,
            r"M_{\text{sys}}=\begin{pmatrix}-f_2/f_1&f_1+f_2\\0&-f_1/f_2\end{pmatrix}",
            "C=0: no net focusing — parallel beam in, parallel beam out!", GOLD)
        solver.add_step(4,
            r"f_{\text{eff}}=-1/C\to\infty,\quad\text{beam magnification}=|A|=f_2/f_1",
            "infinite focal length = afocal. Beam expands by factor f2/f1.", GOLD)
        solver.finalize()
        self.wait(52.8)
        self.play(FadeOut(VGroup(title, *solver.steps)))


# ─── LECTURE 4.1: WAVE SUPERPOSITION ────────────────────────────────────────

class StandingWaves(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/StandingWaves.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"A\sin(kx-\omega t)+A\sin(kx+\omega t)=2A\underbrace{\sin(kx)}_{\text{space}}\underbrace{\cos(\omega t)}_{\text{time}}", font_size=36)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(eq, run_time=0.1))
        b = txt_block([
            "Nodes (zero amplitude always): x = m * lambda/2.  Spacing = lambda/2.",
            "Antinodes (maximum amplitude): x = (m + 1/2) * lambda/2.",
            "The pattern oscillates in place — no net energy transport.",
            "Laser cavities only support wavelengths where L = m*lambda/2.",
        ])
        safe_scale(b, max_width=13.0, max_height=3.0)
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(80.0)

class Beating(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/Beating.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"A\cos(\omega_1 t)+A\cos(\omega_2 t)="
                     r"2A\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right)"
                     r"\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right)",
                     font_size=34)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.4)
        f_beat = MathTex(r"f_{\text{beat}} = |f_1 - f_2|", font_size=44, color=GOLD)
        f_beat.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, f_beat), run_time=0.1))
        b = txt_block([
            "Fast oscillation at average frequency, amplitude-modulated by slow envelope.",
            "Two guitar strings at 440 Hz and 443 Hz: 3 beats per second — audible wah-wah.",
            "Tuning: adjust until beats disappear (f1 = f2).",
            "In optics: beating between laser modes used in heterodyne detection.",
        ])
        safe_scale(b, max_width=13.0, max_height=2.8)
        b.next_to(f_beat, DOWN, buff=0.3)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(70.0)

class PolarizationBasics(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/PolarizationBasics.mp3", time_offset=0)
        title = Text("Polarization of Light  (Bennett Section 6.1-6.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        states = VGroup(
            labeled_eq(r"\Delta\phi=0\text{ or }\pi", "LINEAR: E oscillates along fixed line", WHITE, 36, 24),
            labeled_eq(r"|E_x|=|E_y|,\;\Delta\phi=\pm\pi/2", "CIRCULAR: E-tip traces a circle", WAVE_COLOR, 36, 24),
            labeled_eq(r"\text{general }\Delta\phi,\text{ any amplitudes}", "ELLIPTICAL: E-tip traces ellipse", B_COLOR, 36, 24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(states, max_width=13.0, max_height=4.5)
        states.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(states, run_time=0.1))
        b = txt_block([
            "RCP: Delta_phi = -pi/2  (E rotates counterclockwise viewed from receiver).",
            "LCP: Delta_phi = +pi/2.",
            "Natural light = random mixture of all polarisation states (unpolarised).",
        ], 25)
        safe_scale(b, max_width=13.0)
        b.next_to(states, DOWN, buff=0.3)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(90.0)

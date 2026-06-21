# week4_matrix_polarisation.py
from manim import *
from utils import *

class Week4TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Week 4: three topics — matrix optics, superposition, polarisation", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Matrix optics: any optical system as a 2x2 matrix  (Bennett 5.5)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Superposition: standing waves and beating  (Bennett 7.1-7.2)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Polarisation introduction  (Bennett 6.1-6.4)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p5.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Matrix methods used in Jones calculus — Week 5", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Matrix methods in paraxial optics  (Bennett Section 5.5)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\begin{pmatrix}y_2\\\theta_2\end{pmatrix}=\mathbf{M}\begin{pmatrix}y_1\\\theta_1\end{pmatrix}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Ray column vector: height y and angle theta", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Each element is a 2x2 matrix — multiply to cascade elements", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p4.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\det(\mathbf{M})=AD-BC=1", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("System matrix determinant always equals 1 — use as check", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MatrixEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p1.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathbf{M}_T=\begin{pmatrix}1&d\\0&1\end{pmatrix}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Translation matrix: height changes by d*theta  (Bennett Eq. 5.35)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MatrixEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p2.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathbf{M}_L=\begin{pmatrix}1&0\\-1/f&1\end{pmatrix}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Thin lens matrix  (Bennett Eq. 5.36)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MatrixEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p3.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathbf{M}_M=\begin{pmatrix}1&0\\-2/R&1\end{pmatrix}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Mirror matrix — identical to lens with f = R/2", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MatrixEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p4.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathbf{M}_\mathrm{sys}=\mathbf{M}_N\cdots\mathbf{M}_2\mathbf{M}_1", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("System matrix: first element on RIGHT  (Bennett Eq. 5.38)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MatrixEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p5.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Order matters — matrix multiplication is not commutative", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p1.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"f_\mathrm{eff}=-1/C", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Effective focal length from system matrix element C", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p2.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathrm{BFD}=(D-1)/C\quad\mathrm{FFD}=-A/C", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Back and front focal distances", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p3.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("C = 0: afocal system (telescope/beam expander) — parallel in, parallel out", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p4.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"AD-BC=1\;\checkmark", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Verify determinant = 1 after every matrix multiplication", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p5.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("All imaging properties encoded in just 3 quantities: 2 principal planes + f", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p1.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"d=f_1+f_2\;\Rightarrow\;C=0", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Beam expander: separation = sum of focal lengths — afocal", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MatrixExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p2.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"A=-f_2/f_1", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("A element gives beam magnification factor", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MatrixExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p3.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Input: height y, zero angle — output: -f2/f1 * y, zero angle", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p4.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Beam expanded by f2/f1, sign flip = beam is inverted", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p5.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Galilean: diverging f1, converging f2 — no intermediate focus", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p1.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\Psi_1+\Psi_2=2A\sin(kx)\cos(\omega t)", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Standing wave = two oppositely travelling waves  (Bennett 7.1)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class StandingWaves_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p2.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"k x_\mathrm{node}=m\pi\;\Rightarrow\;x=m\lambda/2", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("NODES: always zero, spaced lambda/2 apart", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class StandingWaves_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p3.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"k x_\mathrm{antinode}=(m+\tfrac{1}{2})\pi", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("ANTINODES: maximum amplitude 2A", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class StandingWaves_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p4.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"2L=N\lambda\;\Rightarrow\;\lambda_N=2L/N", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Laser cavity: only N half-wavelengths allowed between mirrors", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class StandingWaves_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p5.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\Delta f=c/2L", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Mode spacing — 500 MHz for 30 cm cavity", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class StandingWaves_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p6.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Guitar string: nodes at both fixed ends — same condition", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p7.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Guitar string: nodes at both fixed ends — same condition", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p1.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"A\cos\omega_1 t+A\cos\omega_2 t=2A\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right)\cos\!\left(\frac{\omega_1+\omega_2}{2}t\right)", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Beating: sum-to-product identity  (Bennett Section 7.2)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class Beating_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p2.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"f_\mathrm{beat}=|f_1-f_2|", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Beat frequency = absolute difference of two frequencies", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class Beating_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p3.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Fast carrier at average frequency, slow envelope at beat frequency", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p4.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Tuning: adjust until beats disappear — frequencies now equal", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p5.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Optical heterodyne: beat signal at radio frequency — easily processed", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p6.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("LIDAR, coherent comms and spectroscopy all use optical beating", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p7.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("LIDAR, coherent comms and spectroscopy all use optical beating", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p1.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathbf{E}(z,t)=E_x\hat{x}+E_y e^{i\Delta\phi}\hat{y}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("E field has x and y components with relative phase Delta-phi", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class PolarizationBasics_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p2.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\Delta\phi=0\;\text{or}\;\pi", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("LINEAR: E oscillates along fixed line", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class PolarizationBasics_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p3.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"|E_x|=|E_y|,\;\Delta\phi=\pm\pi/2", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("CIRCULAR: E-tip traces a circle", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class PolarizationBasics_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p4.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("ELLIPTICAL: general case — any amplitudes and any phase difference", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p5.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Natural light: polarisation randomises every ~10 ns — unpolarised", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)


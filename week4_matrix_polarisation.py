# week4_matrix_polarisation.py
from manim import *
from utils import *

class Week4TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.add(card)
        sub_text = Text("Week 4: three topics — matrix optics, superposition, polarisation", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week4TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.add(card)
        sub_text = Text("Matrix optics: any optical system as a 2x2 matrix  (Bennett 5.5)", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week4TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.add(card)
        sub_text = Text("Superposition: standing waves and beating  (Bennett 7.1-7.2)", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week4TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.add(card)
        sub_text = Text("Polarisation introduction  (Bennett 6.1-6.4)", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week4TitleCard_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p5.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.add(card)
        sub_text = Text("Matrix methods used in Jones calculus — Week 5", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class MatrixOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Matrix methods in paraxial optics  (Bennett Section 5.5)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class MatrixOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\begin{pmatrix}y_2\\\\\\theta_2\\end{pmatrix}=\\mathbf{M}\\begin{pmatrix}y_1\\\\\\theta_1\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Ray column vector: height y and angle theta", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MatrixOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Each element is a 2x2 matrix — multiply to cascade elements", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class MatrixOpticsIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p4.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\det(\\mathbf{M})=AD-BC=1", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("System matrix determinant always equals 1 — use as check", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MatrixEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p1.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}_T=\\begin{pmatrix}1&d\\\\0&1\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Translation matrix: height changes by d*theta  (Bennett Eq. 5.35)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MatrixEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p2.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}_L=\\begin{pmatrix}1&0\\\\-1/f&1\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Thin lens matrix  (Bennett Eq. 5.36)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MatrixEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p3.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}_M=\\begin{pmatrix}1&0\\\\-2/R&1\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Mirror matrix — identical to lens with f = R/2", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MatrixEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p4.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}_\\mathrm{sys}=\\mathbf{M}_N\\cdots\\mathbf{M}_2\\mathbf{M}_1", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("System matrix: first element on RIGHT  (Bennett Eq. 5.38)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MatrixEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p5.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Order matters — matrix multiplication is not commutative", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SystemMatrixCardinalPoints_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p1.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"f_\\mathrm{eff}=-1/C", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Effective focal length from system matrix element C", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SystemMatrixCardinalPoints_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p2.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathrm{BFD}=(D-1)/C\\quad\\mathrm{FFD}=-A/C", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Back and front focal distances", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SystemMatrixCardinalPoints_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p3.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("C = 0: afocal system (telescope/beam expander) — parallel in, parallel out", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SystemMatrixCardinalPoints_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p4.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"AD-BC=1\\;\\checkmark", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Verify determinant = 1 after every matrix multiplication", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SystemMatrixCardinalPoints_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p5.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("All imaging properties encoded in just 3 quantities: 2 principal planes + f", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class MatrixExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p1.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett 5.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"d=f_1+f_2\\;\\Rightarrow\\;C=0", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Beam expander: separation = sum of focal lengths — afocal", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MatrixExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p2.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett 5.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"A=-f_2/f_1", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("A element gives beam magnification factor", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MatrixExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p3.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett 5.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Input: height y, zero angle — output: -f2/f1 * y, zero angle", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class MatrixExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p4.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett 5.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Beam expanded by f2/f1, sign flip = beam is inverted", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class MatrixExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p5.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett 5.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Galilean: diverging f1, converging f2 — no intermediate focus", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class StandingWaves_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p1.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett 7.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Psi_1+\\Psi_2=2A\\sin(kx)\\cos(\\omega t)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Standing wave = two oppositely travelling waves  (Bennett 7.1)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class StandingWaves_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p2.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett 7.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"k x_\\mathrm{node}=m\\pi\\;\\Rightarrow\\;x=m\\lambda/2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("NODES: always zero, spaced lambda/2 apart", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class StandingWaves_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p3.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett 7.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"k x_\\mathrm{antinode}=(m+\\tfrac{1}{2})\\pi", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("ANTINODES: maximum amplitude 2A", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class StandingWaves_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p4.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett 7.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"2L=N\\lambda\\;\\Rightarrow\\;\\lambda_N=2L/N", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Laser cavity: only N half-wavelengths allowed between mirrors", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class StandingWaves_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p5.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett 7.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Delta f=c/2L", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Mode spacing — 500 MHz for 30 cm cavity", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class StandingWaves_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p6.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett 7.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Guitar string: nodes at both fixed ends — same condition", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class StandingWaves_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p7.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett 7.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Guitar string: nodes at both fixed ends — same condition", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class Beating_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p1.mp3", time_offset=0)
        title = Text("Beating  (Bennett 7.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"A\\cos\\omega_1 t+A\\cos\\omega_2 t=2A\\cos\\!\\left(\\frac{\\omega_1-\\omega_2}{2}t\\right)\\cos\\!\\left(\\frac{\\omega_1+\\omega_2}{2}t\\right)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Beating: sum-to-product identity  (Bennett Section 7.2)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class Beating_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p2.mp3", time_offset=0)
        title = Text("Beating  (Bennett 7.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"f_\\mathrm{beat}=|f_1-f_2|", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Beat frequency = absolute difference of two frequencies", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class Beating_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p3.mp3", time_offset=0)
        title = Text("Beating  (Bennett 7.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Fast carrier at average frequency, slow envelope at beat frequency", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class Beating_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p4.mp3", time_offset=0)
        title = Text("Beating  (Bennett 7.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Tuning: adjust until beats disappear — frequencies now equal", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class Beating_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p5.mp3", time_offset=0)
        title = Text("Beating  (Bennett 7.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Optical heterodyne: beat signal at radio frequency — easily processed", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class Beating_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p6.mp3", time_offset=0)
        title = Text("Beating  (Bennett 7.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("LIDAR, coherent comms and spectroscopy all use optical beating", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class Beating_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p7.mp3", time_offset=0)
        title = Text("Beating  (Bennett 7.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("LIDAR, coherent comms and spectroscopy all use optical beating", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class PolarizationBasics_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p1.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{E}(z,t)=E_x\\hat{x}+E_y e^{i\\Delta\\phi}\\hat{y}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("E field has x and y components with relative phase Delta-phi", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PolarizationBasics_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p2.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Delta\\phi=0\\;\\text{or}\\;\\pi", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("LINEAR: E oscillates along fixed line", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PolarizationBasics_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p3.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"|E_x|=|E_y|,\\;\\Delta\\phi=\\pm\\pi/2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("CIRCULAR: E-tip traces a circle", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PolarizationBasics_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p4.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("ELLIPTICAL: general case — any amplitudes and any phase difference", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class PolarizationBasics_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p5.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Natural light: polarisation randomises every ~10 ns — unpolarised", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)


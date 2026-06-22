# week5_jones.py
from manim import *
from utils import *

class Week5TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.add(card)
        sub_t = Text("Week 5: Jones vector and Jones matrix formalism", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week5TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.add(card)
        sub_t = Text("Complete framework for polarisation calculations", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week5TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.add(card)
        sub_t = Text("Jones vector: 2-component complex column vector  (Bennett Ch. 6)", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week5TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.add(card)
        sub_t = Text("Jones matrix: 2x2 complex — for any polarisation element", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class PolarisationStatesScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p1.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\tilde{E}=\begin{pmatrix}E_{0x}\\E_{0y}e^{i\Delta\phi}\end{pmatrix}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("General Jones vector  (Bennett Eq. 6.13)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class PolarisationStatesScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p2.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Delta-phi=0: linear | pi/2: circular | else: elliptical", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class PolarisationStatesScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p3.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("LCP: field rotates counterclockwise from receiver", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class PolarisationStatesScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p4.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("RCP: field rotates clockwise", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class PolarisationStatesScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p5.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=|E_{0x}|^2+|E_{0y}|^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Intensity = sum of squared components", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class PolarisationStatesScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p6.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("LCP and RCP form an alternative complete basis", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class BirefringenceWavePlates_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p1.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Birefringent crystal: different n for different polarisation", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class BirefringenceWavePlates_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p2.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n_e=1.4849,\;n_o=1.6584\;(\text{calcite 589\,nm})', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Calcite indices  (Bennett 6.3)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class BirefringenceWavePlates_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p3.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\Delta\phi=\frac{2\pi d}{\lambda_0}|n_o-n_e|', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Phase retardation  (Bennett Eq. 6.8)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class BirefringenceWavePlates_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p4.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'd_\text{QWP}=\frac{\lambda_0}{4|n_e-n_o|}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Quarter-wave plate: Delta-phi=pi/2", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class BirefringenceWavePlates_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p5.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'd_\text{HWP}=\frac{\lambda_0}{2|n_e-n_o|}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Half-wave plate: Delta-phi=pi", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class BirefringenceWavePlates_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p6.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("QWP converts +/-45 linear to circular", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class BirefringenceWavePlates_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p7.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("HWP rotates linear polarisation by 2*alpha", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class JonesFormalism_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p1.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Jones formalism — R.C. Jones 1941  (Bennett 6.5)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class JonesFormalism_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p2.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\tilde{E}=\begin{pmatrix}E_{0x}\\E_{0y}\end{pmatrix}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Jones vector", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesFormalism_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p3.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\begin{pmatrix}1\\0\end{pmatrix}\;\begin{pmatrix}0\\1\end{pmatrix}\;\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}\;\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("H, V, +45, -45 Jones vectors", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesFormalism_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p4.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}\;\text{LCP}\quad\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}\;\text{RCP}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Circular Jones vectors", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesFormalism_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p5.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=|E_{0x}|^2+|E_{0y}|^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Intensity from Jones vector", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesFormalism_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p6.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Factor i: 90-degree phase — determines rotation direction", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class JonesFormalism_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p7.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("LCP+RCP: alternative basis — equally valid to H,V", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class JonesFormalism_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p8.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Jones vector completely specifies coherent beam polarisation", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class JonesMatrices_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p1.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\tilde{E}_\text{out}=\mathbf{M}\tilde{E}_\text{in}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Jones matrix  (Bennett Eq. 6.22)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesMatrices_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p2.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{M}_\text{total}=\mathbf{M}_N\cdots\mathbf{M}_2\mathbf{M}_1', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Cascade: first element on RIGHT  (Bennett Eq. 6.23)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesMatrices_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p3.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{M}_H=\begin{pmatrix}1&0\\0&0\end{pmatrix}\quad\mathbf{M}_V=\begin{pmatrix}0&0\\0&1\end{pmatrix}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("H and V polarisers  (Bennett Table 6.1)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesMatrices_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p4.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{M}_\text{QWP-H}=\begin{pmatrix}1&0\\0&i\end{pmatrix}\quad\mathbf{M}_\text{HWP-H}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("QWP and HWP  (Table 6.1)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesMatrices_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p5.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{R}(\alpha)=\begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Rotation matrix  (Bennett Example 6.5)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesMatrices_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p6.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\begin{pmatrix}0&0\\0&1\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}=\frac{1}{\sqrt{2}}\begin{pmatrix}0\\1\end{pmatrix}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example 6.6a: +45 through V-pol -> V, half I", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesMatrices_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p7.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\begin{pmatrix}1&0\\0&i\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example 6.6b: +45 through QWP-H -> LCP", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesMatrices_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p8.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{M}_\text{rot}=\mathbf{R}(\alpha)\mathbf{M}\mathbf{R}(-\alpha)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Rotated element  (Bennett Eq. 6.24)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class JonesMatrices_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p9.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Order matters — not commutative", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class JonesMatrices_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p10.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Output modulus-squared = transmitted intensity fraction", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class JonesMatrices_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p11.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Example 6.7: HWP + QWP + polariser — multiply 3 matrices", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

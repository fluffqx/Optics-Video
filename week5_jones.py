# week5_jones.py
from manim import *
from utils import *

class Week5TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.add(card)
        sub_text = Text("Week 5: Jones vector and Jones matrix calculus  (Bennett Ch. 6)", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week5TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.add(card)
        sub_text = Text("Jones vector: 2-component complex column vector for any polarisation", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week5TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.add(card)
        sub_text = Text("Jones matrix: 2x2 complex matrix for any polarisation element", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week5TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.add(card)
        sub_text = Text("Bennett Table 6.1 — memorise all matrices", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class PolarisationStatesScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p1.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\mathbf{E}}=\\begin{pmatrix}E_{0x}\\\\E_{0y}e^{i\\Delta\\phi}\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("General polarisation state  (Bennett Eq. 6.13)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PolarisationStatesScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p2.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Delta\\phi=0:\\;\\text{linear}\\quad\\Delta\\phi=\\pi/2:\\;\\text{circular}\\quad\\text{else: elliptical}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Phase difference determines polarisation state", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PolarisationStatesScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p3.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("LCP: Delta-phi = +pi/2, field rotates counterclockwise from receiver", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class PolarisationStatesScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p4.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("RCP: Delta-phi = -pi/2", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class PolarisationStatesScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p5.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"I=\\varepsilon_0 v|E_{0x}|^2/2+\\varepsilon_0 v|E_{0y}|^2/2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Irradiance = sum of x and y contributions  (Bennett Eq. 6.16)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PolarisationStatesScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p6.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett 6.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Unpolarised through polariser: I0/2 — average of all cos²theta", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class BirefringenceWavePlates_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p1.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Birefringent crystal: different n for different polarisation directions", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class BirefringenceWavePlates_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p2.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"n_e(\\mathrm{calcite})=1.4849\\quad n_o(\\mathrm{calcite})=1.6584", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Calcite at 589 nm — extraordinary vs ordinary index  (Bennett 6.3)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class BirefringenceWavePlates_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p3.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Delta\\phi=\\frac{2\\pi d}{\\lambda_0}|n_o-n_e|", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Phase shift from wave plate of thickness d  (Bennett Eq. 6.8)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class BirefringenceWavePlates_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p4.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"d_\\mathrm{QWP}=\\frac{\\lambda_0}{4|n_e-n_o|}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Quarter-wave plate — Delta-phi = pi/2  (Bennett Eq. 6.10)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class BirefringenceWavePlates_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p5.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"d_\\mathrm{HWP}=\\frac{\\lambda_0}{2|n_e-n_o|}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Half-wave plate — Delta-phi = pi  (Bennett Eq. 6.11)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class BirefringenceWavePlates_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p6.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("QWP converts +/-45 deg linear to circular — and back", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class BirefringenceWavePlates_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p7.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("HWP rotates linear polarisation by 2*alpha  (alpha = fast-axis angle)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class JonesFormalism_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p1.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Jones vectors introduced by R. Clark Jones, 1941  (Bennett 6.5)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class JonesFormalism_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p2.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{E}=\\begin{pmatrix}E_{0x}\\\\E_{0y}\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Jones vector — complex amplitude column vector", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesFormalism_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p3.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Common factor exp(i(kz-omega t)) is implicit — not written", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class JonesFormalism_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p4.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\begin{pmatrix}1\\\\0\\end{pmatrix}\\;\\begin{pmatrix}0\\\\1\\end{pmatrix}\\;\\frac{1}{\\sqrt{2}}\\begin{pmatrix}1\\\\1\\end{pmatrix}\\;\\frac{1}{\\sqrt{2}}\\begin{pmatrix}1\\\\-1\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("H-linear, V-linear, +45, -45 degree Jones vectors", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesFormalism_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p5.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{1}{\\sqrt{2}}\\begin{pmatrix}1\\\\i\\end{pmatrix}\\;\\text{LCP}\\qquad\\frac{1}{\\sqrt{2}}\\begin{pmatrix}1\\\\-i\\end{pmatrix}\\;\\text{RCP}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Left and right circular Jones vectors  (Bennett Table 6.1)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesFormalism_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p6.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"I=|\\tilde{E}|^2=|E_{0x}|^2+|E_{0y}|^2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Intensity from Jones vector: modulus squared", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesFormalism_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p7.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("LCP and RCP form an alternative basis — equally valid to H,V", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class JonesFormalism_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p8.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett 6.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Specifying Jones vector = fully specifying polarisation state", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class JonesMatrices_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p1.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{E}_t=\\mathbf{M}\\tilde{E}_i", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Jones matrix M transforms input to output  (Bennett Eq. 6.22)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p2.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}_\\mathrm{total}=\\mathbf{M}_N\\cdots\\mathbf{M}_2\\mathbf{M}_1", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Cascade: first element on RIGHT  (Bennett Eq. 6.23)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p3.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}_{H-pol}=\\begin{pmatrix}1&0\\\\0&0\\end{pmatrix}\\quad\\mathbf{M}_{V-pol}=\\begin{pmatrix}0&0\\\\0&1\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Horizontal and vertical polarisers  (Bennett Table 6.1)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p4.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}_\\mathrm{QWP-H}=\\begin{pmatrix}1&0\\\\0&i\\end{pmatrix}\\quad\\mathbf{M}_\\mathrm{QWP-V}=\\begin{pmatrix}1&0\\\\0&-i\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("QWP with fast axis horizontal and vertical  (Bennett Table 6.1)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p5.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}_\\mathrm{HWP-H}=\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("HWP with fast axis horizontal", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p6.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{R}(\\alpha)=\\begin{pmatrix}\\cos\\alpha&-\\sin\\alpha\\\\\\sin\\alpha&\\cos\\alpha\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Rotation matrix  (Bennett Example 6.5)  — rotated matrix: R M R^{-1}", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p7.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\begin{pmatrix}0&0\\\\0&1\\end{pmatrix}\\frac{1}{\\sqrt{2}}\\begin{pmatrix}1\\\\1\\end{pmatrix}=\\frac{1}{\\sqrt{2}}\\begin{pmatrix}0\\\\1\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Bennett Example 6.6a: +45 through V-polariser -> V-linear, I/2", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p8.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\begin{pmatrix}1&0\\\\0&i\\end{pmatrix}\\frac{1}{\\sqrt{2}}\\begin{pmatrix}1\\\\1\\end{pmatrix}=\\frac{1}{\\sqrt{2}}\\begin{pmatrix}1\\\\i\\end{pmatrix}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Bennett Example 6.6b: +45 through QWP-H -> LCP, no intensity loss", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p9.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{M}^\\prime=\\mathbf{R}(\\alpha)\\mathbf{M}\\mathbf{R}(-\\alpha)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Rotated element matrix  (Bennett Eq. 6.24)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class JonesMatrices_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p10.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Example 6.7: HWP + QWP + polariser — multiply 3 matrices", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class JonesMatrices_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p11.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett 6.5.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Example 6.7: HWP + QWP + polariser — multiply 3 matrices", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)


# week1_waves.py
from manim import *
from utils import *

class Week1TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation and Complex Representation", "Bennett Ch. 1")
        self.add(card)
        sub_text = Text("31OPT Optics — complete exam preparation series", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week1TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation and Complex Representation", "Bennett Ch. 1")
        self.add(card)
        sub_text = Text("Weeks 1-8 covered in full from Bennett 2nd edition", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week1TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation and Complex Representation", "Bennett Ch. 1")
        self.add(card)
        sub_text = Text("Theory: derivations, examples and physical intuition", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week1TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation and Complex Representation", "Bennett Ch. 1")
        self.add(card)
        sub_text = Text("Start with the most fundamental question: what is a wave?", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class WaveIntroduction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p1.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett 1.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("A wave propagates energy without transporting matter", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveIntroduction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p2.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett 1.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Ocean: water stays put, disturbance moves — same principle", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveIntroduction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p3.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett 1.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Sound: air molecules oscillate, compression wave propagates", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveIntroduction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p4.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett 1.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("EM waves: E and B fields oscillate — no medium needed", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveIntroduction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p5.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett 1.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("1D wave equation captures all essential wave physics", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveIntroduction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p6.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett 1.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Wave function psi(x,t): physical quantity at position x, time t", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveEquation1D_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p1.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett 1.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{\\partial^2\\Psi}{\\partial x^2}=\\frac{1}{v^2}\\frac{\\partial^2\\Psi}{\\partial t^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("The 1D wave equation  (Bennett Eq. 1.1)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class WaveEquation1D_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p2.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett 1.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{\\partial^2\\Psi}{\\partial x^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("LEFT SIDE — spatial curvature of the wave profile", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class WaveEquation1D_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p3.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett 1.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{1}{v^2}\\frac{\\partial^2\\Psi}{\\partial t^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("RIGHT SIDE — temporal acceleration / v²", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class WaveEquation1D_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p4.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett 1.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Curvature in space proportional to acceleration in time", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveEquation1D_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p5.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett 1.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Linear equation — superposition principle holds exactly", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveEquation1D_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p6.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett 1.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Psi = f(x-vt)\\;\\text{or}\\;g(x+vt)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("General solution: any shape, speed v, either direction", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class WaveEquation1D_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p7.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett 1.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("f(x-vt) moves right rigidly at speed v", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveEquation1D_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p8.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett 1.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Shape preservation holds only in non-dispersive media", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class WaveEquationProof_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p1.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Psi=(x-vt)^2\\quad\\text{— test this in the wave equation}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Choose the quadratic as a concrete test function", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class WaveEquationProof_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p2.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{\\partial^2\\Psi}{\\partial x^2}=2 \\qquad \\frac{\\partial^2\\Psi}{\\partial t^2}=2v^2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Both second derivatives computed explicitly", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class WaveEquationProof_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p3.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{2}{v^2\\cdot 2}=\\frac{1}{v^2}\\;\\checkmark", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Ratio gives 1/v² — wave equation satisfied", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class WaveEquationProof_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p4.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{\\partial^2 f}{\\partial x^2}=f^{\\prime\\prime}\\qquad\\frac{\\partial^2 f}{\\partial t^2}=v^2 f^{\\prime\\prime}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("General proof for any f(x-vt) via chain rule", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class WaveEquationProof_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p5.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Any twice-differentiable function is a valid wave solution", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWave_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p1.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Harmonic wave: single-frequency sinusoidal oscillation", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWave_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p2.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Psi(x,t)=A\\sin(kx-\\omega t+\\phi)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("The harmonic traveling wave  (Bennett Eq. 1.14)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p3.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Every symbol in this equation recurs throughout the course", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWave_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p4.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"A", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("AMPLITUDE — maximum value  [V/m for E-field]  |  I ∝ A²", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p5.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"k=\\frac{2\\pi}{\\lambda}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("WAVE NUMBER — spatial frequency  [rad/m]", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p6.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\omega=2\\pi f=\\frac{2\\pi}{T}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("ANGULAR FREQUENCY  [rad/s]", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p7.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\lambda", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("WAVELENGTH — distance between adjacent crests  [m]", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p8.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"f=\\frac{1}{T}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("FREQUENCY — cycles per second  [Hz]", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p9.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v=\\frac{\\omega}{k}=f\\lambda", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("PHASE SPEED — speed of crests  [m/s]", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p10.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\phi", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("INITIAL PHASE — shifts wave in time  [rad]", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p11.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v=f\\lambda \\quad k=\\frac{2\\pi}{\\lambda} \\quad \\omega=2\\pi f \\quad T=\\frac{1}{f}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("FIVE KEY RELATIONS — memorise all of them", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p12(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p12.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Worked example: lambda = 500 nm visible light in vacuum", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWave_p13(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p13.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"k=1.257\\times10^7\\,\\mathrm{rad/m} \\qquad f=5.996\\times10^{14}\\,\\mathrm{Hz}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Wave number and frequency for 500 nm", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p14(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p14.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\omega=3.768\\times10^{15}\\,\\mathrm{rad/s} \\qquad T=1.668\\,\\mathrm{fs}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Period = 1.668 femtoseconds", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p15(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p15.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("T = 1.668 fs: a million times shorter than a nanosecond", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWave_p16(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p16.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Psi=E_0\\sin(1.257\\times10^7 x-3.768\\times10^{15}t+\\phi)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Complete wave function for 500 nm E-field", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWave_p17(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p17.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett 1.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Any wave decomposes into harmonic components — Fourier", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p1.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\lambda=632.8\\,\\mathrm{nm} \\quad v=c=2.998\\times10^8\\,\\mathrm{m/s}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("He-Ne laser — given quantities", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p2.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"k=9.926\\times10^6\\,\\mathrm{rad/m} \\quad f=4.738\\times10^{14}\\,\\mathrm{Hz}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Wave number and frequency", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p3.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\omega=2.977\\times10^{15}\\,\\mathrm{rad/s} \\quad T=2.11\\,\\mathrm{fs}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Angular frequency and period", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p4.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"E_x=E_0\\sin(9.926\\times10^6\\,z-2.977\\times10^{15}\\,t)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Complete E-field wave function", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p5.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("2.11 fs period: one million times shorter than a nanosecond", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p6.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("632.8 nm is about 1/100 the diameter of a human hair", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p7.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"I=\\tfrac{1}{2}\\varepsilon_0 c E_0^2=1327\\,\\mathrm{W/m^2}\\;\\text{for }E_0=1000\\,\\mathrm{V/m}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Irradiance from amplitude  (Bennett Eq. 2.33)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p8.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("I proportional to A squared — doubling field quadruples intensity", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p9.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Optical period too short for any electronic detection", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class HarmonicWaveExample_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p10.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("All optical detectors measure intensity, not field phase", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SuperpositionPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p1.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett 1.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Superposition principle  (Bennett Section 1.5)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SuperpositionPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p2.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett 1.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{\\partial^2(\\Psi_1+\\Psi_2)}{\\partial x^2}=\\frac{1}{v^2}\\frac{\\partial^2(\\Psi_1+\\Psi_2)}{\\partial t^2}\\;\\checkmark", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Proof: sum of solutions satisfies wave equation", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SuperpositionPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p3.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett 1.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Any linear combination a psi-1 + b psi-2 is also a solution", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SuperpositionPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p4.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett 1.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Two laser beams cross in space without affecting each other", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SuperpositionPrinciple_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p5.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett 1.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Foundation of ALL interference and diffraction  (Weeks 6-7)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SuperpositionPrinciple_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p6.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett 1.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Fails at high intensity in nonlinear media — frequency doubling", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class PhaseGroupVelocity_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p1.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett 7.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Two distinct velocities associated with any dispersive wave", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class PhaseGroupVelocity_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p2.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett 7.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v_p=\\frac{\\omega}{k}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("PHASE VELOCITY — speed of individual crests", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PhaseGroupVelocity_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p3.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett 7.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v_g=\\frac{d\\omega}{dk}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("GROUP VELOCITY — speed of energy and information", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PhaseGroupVelocity_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p4.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett 7.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Vacuum: omega = ck, so vp = vg = c — no dispersion", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class PhaseGroupVelocity_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p5.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett 7.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v_g=\\frac{c}{n+\\omega\\,dn/d\\omega}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Group velocity in dispersive medium  (Bennett 7.7)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class PhaseGroupVelocity_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p6.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett 7.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Normal dispersion: dn/d-omega > 0 so vg < c/n — energy slower than crests", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class PhaseGroupVelocity_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p7.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett 7.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\omega=ak^2 \\;\\Rightarrow\\; v_p=ak,\\quad v_g=2ak=2v_p", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Dispersive example: group speed = 2 x phase speed", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p1.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Complex notation replaces trig with exponentials  (Bennett 1.6)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p2.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"e^{i\\theta}=\\cos\\theta+i\\sin\\theta", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Euler's formula — foundation of complex wave notation", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p3.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\cos\\theta=\\mathrm{Re}[e^{i\\theta}] \\qquad \\sin\\theta=\\mathrm{Im}[e^{i\\theta}]", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Cosine = real part, sine = imaginary part", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p4.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\Psi}=Ae^{i(kx-\\omega t)} \\quad \\Psi_\\mathrm{phys}=\\mathrm{Re}[\\tilde{\\Psi}]", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Complex wave — physical wave is real part", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p5.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"|\\tilde{\\Psi}|^2=\\tilde{\\Psi}\\cdot\\tilde{\\Psi}^*=A^2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Intensity proportional to modulus squared = A squared", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p6.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"|\\tilde{\\Psi}_1+\\tilde{\\Psi}_2|^2=A_1^2+A_2^2+2\\mathrm{Re}[\\tilde{\\Psi}_1\\tilde{\\Psi}_2^*]", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Cross term = interference term", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p7.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\Psi}_{3D}=Ae^{i(\\mathbf{k}\\cdot\\mathbf{r}-\\omega t)}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("3D plane wave — wavefronts perpendicular to k", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p8.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\Psi}_\\mathrm{sph}=\\frac{A}{r}e^{i(kr-\\omega t)}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Spherical wave — amplitude 1/r, intensity 1/r squared", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ComplexRepresentation_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p9.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett 1.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Inverse square law follows from energy conservation", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class ThreeDWaves_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p1.mp3", time_offset=0)
        title = Text("3D Waves  (Bennett 1.7)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla^2\\Psi=\\frac{1}{v^2}\\frac{\\partial^2\\Psi}{\\partial t^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("3D wave equation  (Bennett Section 1.7)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThreeDWaves_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p2.mp3", time_offset=0)
        title = Text("3D Waves  (Bennett 1.7)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\Psi}=Ae^{i(\\mathbf{k}\\cdot\\mathbf{r}-\\omega t)} \\quad |\\mathbf{k}|=\\frac{2\\pi}{\\lambda}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("3D plane wave — k-vector in propagation direction", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThreeDWaves_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p3.mp3", time_offset=0)
        title = Text("3D Waves  (Bennett 1.7)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\Psi}=\\frac{A}{r}e^{i(kr-\\omega t)} \\quad I\\propto\\frac{1}{r^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Spherical wave — inverse square law", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThreeDWaves_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p4.mp3", time_offset=0)
        title = Text("3D Waves  (Bennett 1.7)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{k}=k_x\\hat{x}+k_y\\hat{y}+k_z\\hat{z}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Wave vector components in 3D", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class Week1WavesSummary_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p1.mp3", time_offset=0)
        title = Text("Week 1a Summary", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Week 1a complete — collect key results", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class Week1WavesSummary_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p2.mp3", time_offset=0)
        title = Text("Week 1a Summary", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{\\partial^2\\Psi}{\\partial x^2}=\\frac{1}{v^2}\\frac{\\partial^2\\Psi}{\\partial t^2} \\quad \\Psi=f(x\\pm vt)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Wave equation and general solution", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class Week1WavesSummary_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p3.mp3", time_offset=0)
        title = Text("Week 1a Summary", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v=f\\lambda=\\frac{\\omega}{k} \\quad k=\\frac{2\\pi}{\\lambda} \\quad \\omega=2\\pi f \\quad T=\\frac{1}{f}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Five harmonic wave relations", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class Week1WavesSummary_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p4.mp3", time_offset=0)
        title = Text("Week 1a Summary", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\Psi}=Ae^{i(kx-\\omega t)} \\quad I\\propto|\\tilde{\\Psi}|^2=A^2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Complex representation and intensity", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class Week1WavesSummary_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p5.mp3", time_offset=0)
        title = Text("Week 1a Summary", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v_p=\\frac{\\omega}{k} \\quad v_g=\\frac{d\\omega}{dk}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Phase velocity vs group velocity", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class Week1WavesSummary_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p6.mp3", time_offset=0)
        title = Text("Week 1a Summary", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\Psi}_{3D}=Ae^{i(\\mathbf{k}\\cdot\\mathbf{r}-\\omega t)}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("3D plane wave — general form", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class Week1WavesSummary_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p7.mp3", time_offset=0)
        title = Text("Week 1a Summary", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{\\Psi}_{3D}=Ae^{i(\\mathbf{k}\\cdot\\mathbf{r}-\\omega t)}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("3D plane wave — general form", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)


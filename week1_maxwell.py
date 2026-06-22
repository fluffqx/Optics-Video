# week1_maxwell.py
from manim import *
from utils import *

class MaxwellIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellIntro_p1.mp3", time_offset=0)
        title = Text("Maxwell Equations Introduction  (Bennett Ch. 2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Maxwell's equations — four laws of classical EM  (Bennett Ch. 2)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class MaxwellIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellIntro_p2.mp3", time_offset=0)
        title = Text("Maxwell Equations Introduction  (Bennett Ch. 2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Unified electricity, magnetism and optics in 1865", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class MaxwellIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellIntro_p3.mp3", time_offset=0)
        title = Text("Maxwell Equations Introduction  (Bennett Ch. 2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("All optics topics derive from these four equations", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class MaxwellIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellIntro_p4.mp3", time_offset=0)
        title = Text("Maxwell Equations Introduction  (Bennett Ch. 2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Differential form used throughout this course", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class VectorCalculusNotation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p1.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\phi=\\left(\\frac{\\partial\\phi}{\\partial x},\\frac{\\partial\\phi}{\\partial y},\\frac{\\partial\\phi}{\\partial z}\\right)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("GRADIENT — direction and rate of steepest increase", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class VectorCalculusNotation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p2.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\cdot\\mathbf{F}=\\frac{\\partial F_x}{\\partial x}+\\frac{\\partial F_y}{\\partial y}+\\frac{\\partial F_z}{\\partial z}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("DIVERGENCE — sources (+) and sinks (−) of field", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class VectorCalculusNotation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p3.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\times\\mathbf{F}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("CURL — rotation of field around a point", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class VectorCalculusNotation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p4.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla^2\\phi=\\frac{\\partial^2\\phi}{\\partial x^2}+\\frac{\\partial^2\\phi}{\\partial y^2}+\\frac{\\partial^2\\phi}{\\partial z^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("LAPLACIAN — curvature / deviation from neighbourhood average", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class VectorCalculusNotation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p5.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("These operators appear in every Maxwell equation", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class MaxwellEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p1.mp3", time_offset=0)
        title = Text("Maxwell's Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\cdot\\mathbf{E}=\\rho_\\mathrm{free}/\\varepsilon", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Gauss's Law — charges are sources of E field", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p2.mp3", time_offset=0)
        title = Text("Maxwell's Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\cdot\\mathbf{B}=0", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("No magnetic monopoles — B field lines always closed loops", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p3.mp3", time_offset=0)
        title = Text("Maxwell's Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\times\\mathbf{E}=-\\partial\\mathbf{B}/\\partial t", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Faraday's Law — changing B creates curling E", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p4.mp3", time_offset=0)
        title = Text("Maxwell's Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\times\\mathbf{B}=\\mu(\\mathbf{J}+\\varepsilon\\,\\partial\\mathbf{E}/\\partial t)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Ampere-Maxwell Law — currents AND changing E create B", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p5.mp3", time_offset=0)
        title = Text("Maxwell's Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Displacement current term (epsilon dE/dt) was Maxwell's key insight", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class MaxwellEquations_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p6.mp3", time_offset=0)
        title = Text("Maxwell's Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\cdot\\mathbf{E}=0\\quad\\nabla\\cdot\\mathbf{B}=0\\quad\\text{(vacuum, no sources)}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("In vacuum with no charges/currents — both divergences zero", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellEquations_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p7.mp3", time_offset=0)
        title = Text("Maxwell's Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla^2\\mathbf{E}=\\mu_0\\varepsilon_0\\,\\partial^2\\mathbf{E}/\\partial t^2 \\quad v=1/\\sqrt{\\mu_0\\varepsilon_0}=c", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Wave equation for E — speed = c", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellVacuum_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellVacuum_p1.mp3", time_offset=0)
        title = Text("Maxwell in Vacuum  (Bennett 2.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\cdot\\mathbf{E}=0\\quad\\nabla\\cdot\\mathbf{B}=0", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("In vacuum: no sources, no divergence", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellVacuum_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellVacuum_p2.mp3", time_offset=0)
        title = Text("Maxwell in Vacuum  (Bennett 2.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\times\\mathbf{E}=-\\frac{\\partial\\mathbf{B}}{\\partial t}\\qquad\\nabla\\times\\mathbf{B}=\\mu_0\\varepsilon_0\\frac{\\partial\\mathbf{E}}{\\partial t}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Coupled curl equations — fields sustain each other", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellVacuum_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellVacuum_p3.mp3", time_offset=0)
        title = Text("Maxwell in Vacuum  (Bennett 2.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla^2\\mathbf{E}=\\mu_0\\varepsilon_0\\frac{\\partial^2\\mathbf{E}}{\\partial t^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("EM wave equation for E in vacuum", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MaxwellVacuum_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellVacuum_p4.mp3", time_offset=0)
        title = Text("Maxwell in Vacuum  (Bennett 2.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("E determines B and vice versa — fields are coupled", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class EMWaveDerivation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p1.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation  (Bennett App. B)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Derivation of EM wave equation from Maxwell's equations", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class EMWaveDerivation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p2.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation  (Bennett App. B)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla\\times(\\nabla\\times\\mathbf{E})=-\\frac{\\partial}{\\partial t}(\\nabla\\times\\mathbf{B})=-\\mu_0\\varepsilon_0\\frac{\\partial^2\\mathbf{E}}{\\partial t^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Take curl of Faraday, substitute Ampere-Maxwell", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveDerivation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p3.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation  (Bennett App. B)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\nabla^2\\mathbf{E}=\\mu_0\\varepsilon_0\\frac{\\partial^2\\mathbf{E}}{\\partial t^2} \\quad c=\\frac{1}{\\sqrt{\\mu_0\\varepsilon_0}}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("EM wave equation — wave speed = c", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveDerivation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p4.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation  (Bennett App. B)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"c=\\frac{1}{\\sqrt{4\\pi\\times10^{-7}\\times8.854\\times10^{-12}}}=2.998\\times10^8\\,\\mathrm{m/s}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Maxwell computed c from EM measurements alone", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveDerivation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p5.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation  (Bennett App. B)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Agreement with measured speed of light identified light as EM wave", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class EMWaveProperties_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p1.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{k}\\perp\\mathbf{E}\\perp\\mathbf{B}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("E, B and k all mutually perpendicular — transverse wave", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveProperties_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p2.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{B}=\\frac{\\hat{k}\\times\\mathbf{E}}{v}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("B determined by E and propagation direction", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveProperties_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p3.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"E=cB\\quad\\text{in vacuum}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Magnitudes related by E = cB", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveProperties_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p4.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("E and B oscillate in phase — both peak simultaneously", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class EMWaveProperties_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p5.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v=c/n\\quad\\lambda_\\mathrm{medium}=\\lambda_0/n", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("In medium n: speed c/n, wavelength lambda/n, frequency unchanged", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveProperties_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p6.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Frequency unchanged at interface — only wavelength changes", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class EMWaveExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p1.mp3", time_offset=0)
        title = Text("Example: Finding B from E  (Bennett 2.3.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{E}=E_0\\hat{x}\\,e^{i(kz-\\omega t)}\\quad\\text{— find }\\mathbf{B}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Given E in x-direction, propagating in z — find B", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p2.mp3", time_offset=0)
        title = Text("Example: Finding B from E  (Bennett 2.3.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{B}=\\frac{\\hat{z}\\times\\hat{x}}{c}E_0\\,e^{i(kz-\\omega t)}=\\frac{E_0}{c}\\hat{y}\\,e^{i(kz-\\omega t)}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("B in y-direction  (z-hat cross x-hat = y-hat)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p3.mp3", time_offset=0)
        title = Text("Example: Finding B from E  (Bennett 2.3.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{E}\\perp\\mathbf{B}\\perp\\hat{k}\\quad\\hat{x}\\perp\\hat{y}\\perp\\hat{z}\\;\\checkmark", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("All perpendicularity conditions verified", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p4.mp3", time_offset=0)
        title = Text("Example: Finding B from E  (Bennett 2.3.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"I=\\tfrac{1}{2}\\varepsilon_0 c E_0^2=1327\\,\\mathrm{W/m^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Irradiance for E0 = 1000 V/m  (Bennett Eq. 2.33)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class EMWaveExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p5.mp3", time_offset=0)
        title = Text("Example: Finding B from E  (Bennett 2.3.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Full verification: transverse, orthogonal, E=cB, in-phase", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class EMWaveExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p6.mp3", time_offset=0)
        title = Text("Example: Finding B from E  (Bennett 2.3.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Practice this calculation until it takes under 2 minutes", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p1.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathbf{S}=\\frac{1}{\\mu_0}\\mathbf{E}\\times\\mathbf{B}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Poynting vector — energy flux  [W/m²]  (Bennett 2.3.1)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p2.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"I=\\langle|\\mathbf{S}|\\rangle=\\frac{1}{2}\\varepsilon_0 c n E_0^2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Irradiance = time-averaged Poynting magnitude  (Bennett Eq. 2.33)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p3.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Factor of 1/2 from time-averaging cos²(omega t) over one period", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p4.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Irradiance proportional to E0 squared — doubling field quadruples I", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p5.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"I=5\\times10^{-3}/(\\pi\\times10^{-6})=1592\\,\\mathrm{W/m^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example: 5 mW laser focused to 1 mm radius spot", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p6.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"E_0=\\sqrt{2I/(\\varepsilon_0 c)}=1095\\,\\mathrm{V/m}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Peak E-field in the beam", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p7.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"B_0=E_0/c=3.65\\,\\mu\\mathrm{T}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Peak B-field — 14x weaker than Earth's field", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p8.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Yet oscillating at 500 THz — no electronic circuit can follow", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p9.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"P_\\mathrm{rad}=I/c\\;(\\text{absorber})\\quad 2I/c\\;(\\text{mirror})", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Radiation pressure on absorber vs perfect mirror", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class PoyntingIrradiance_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p10.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance  (Bennett 2.3.1)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Solar irradiance 1361 W/m² gives 9 microPascals on a mirror", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class RadiationPressure_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p1.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Light carries momentum — Maxwell predicted, Lebedev measured 1900", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class RadiationPressure_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p2.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"P_\\mathrm{rad}=I/c\\;(\\text{absorber})", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Radiation pressure on perfect absorber", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class RadiationPressure_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p3.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"P_\\mathrm{rad}=2I/c\\;(\\text{mirror})", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Radiation pressure on perfect mirror — momentum reverses", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class RadiationPressure_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p4.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"P_\\mathrm{rad}=\\frac{I(1+R)}{c}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("General: reflectivity R between 0 and 1", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class RadiationPressure_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p5.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Solar sail: 1 mN thrust from 14 x 14 m sail — IKAROS 2010", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class RadiationPressure_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p6.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Optical tweezers: trap cells with focused laser gradient force", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class RadiationPressure_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p7.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Nobel Prize 2018: Arthur Ashkin — optical tweezers", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class RadiationPressure_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p8.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("LIGO: 100 kW intracavity power — radiation pressure must be managed", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class DispersionScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p1.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Dispersion: refractive index depends on frequency  (Bennett 3.9)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class DispersionScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p2.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"n=c/v_p\\quad\\text{— depends on frequency in dispersive media}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Index n = c/vp — varies with omega in glass", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class DispersionScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p3.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Normal dispersion: n increases with frequency — violet refracts more", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class DispersionScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p4.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Lorentz model: electrons as bound oscillators driven by light field", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class DispersionScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p5.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"v_g=\\frac{c}{n+\\omega\\,dn/d\\omega}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Group velocity — energy travels at vg, not vp", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class DispersionScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p6.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Anomalous dispersion near resonance: dn/domega < 0", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class DispersionScene_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p7.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Pulse broadening in optical fibres: 17 ps/nm/km at 1550 nm", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class DispersionScene_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p8.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Dispersion-compensating fibres reverse broadening for higher data rates", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)


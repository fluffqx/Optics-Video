# week1_maxwell.py
from manim import *
from utils import *

class MaxwellIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellIntro_p1.mp3", time_offset=0)
        title = Text("Maxwell Equations Introduction", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Four equations that unify electricity, magnetism and optics", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MaxwellIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellIntro_p2.mp3", time_offset=0)
        title = Text("Maxwell Equations Introduction", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Maxwell 1865: predicted EM waves at speed of light from EM data", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MaxwellIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellIntro_p3.mp3", time_offset=0)
        title = Text("Maxwell Equations Introduction", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("All optics in this course derives from these equations", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MaxwellIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellIntro_p4.mp3", time_offset=0)
        title = Text("Maxwell Equations Introduction", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Before Maxwell: electricity, magnetism, optics seemed unrelated", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class VectorCalculusNotation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p1.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\phi', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("GRADIENT — direction and rate of steepest increase", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class VectorCalculusNotation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p2.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\cdot\mathbf{F}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("DIVERGENCE — sources and sinks of field", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class VectorCalculusNotation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p3.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\times\mathbf{F}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("CURL — rotation of field around a point", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class VectorCalculusNotation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p4.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla^2\phi', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("LAPLACIAN — curvature relative to neighbourhood", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class VectorCalculusNotation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/VectorCalculusNotation_p5.mp3", time_offset=0)
        title = Text("Vector Calculus Notation  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("These operators appear in every Maxwell equation", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MaxwellEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p1.mp3", time_offset=0)
        title = Text("Maxwell Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\cdot\mathbf{E}=\rho/\varepsilon', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Gauss Law — charges are sources of E", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MaxwellEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p2.mp3", time_offset=0)
        title = Text("Maxwell Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\cdot\mathbf{B}=0', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("No magnetic monopoles — B lines always closed", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MaxwellEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p3.mp3", time_offset=0)
        title = Text("Maxwell Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Faraday Law — changing B creates curling E", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MaxwellEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p4.mp3", time_offset=0)
        title = Text("Maxwell Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\times\mathbf{B}=\mu(\mathbf{J}+\varepsilon\,\partial\mathbf{E}/\partial t)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Ampere-Maxwell — currents AND changing E create B", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MaxwellEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p5.mp3", time_offset=0)
        title = Text("Maxwell Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Displacement current was Maxwell's key insight", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MaxwellEquations_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p6.mp3", time_offset=0)
        title = Text("Maxwell Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla^2\mathbf{E}=\mu_0\varepsilon_0\,\partial^2\mathbf{E}/\partial t^2\quad c=1/\sqrt{\mu_0\varepsilon_0}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Wave equation — speed = c", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MaxwellEquations_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellEquations_p7.mp3", time_offset=0)
        title = Text("Maxwell Equations  (Bennett 2.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Maxwell computed c from EM measurements — identified light as EM wave", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MaxwellVacuum_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellVacuum_p1.mp3", time_offset=0)
        title = Text("Maxwell in Vacuum  (Bennett 2.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\cdot\mathbf{E}=0\qquad\nabla\cdot\mathbf{B}=0', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("No sources in vacuum", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MaxwellVacuum_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellVacuum_p2.mp3", time_offset=0)
        title = Text("Maxwell in Vacuum  (Bennett 2.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\times\mathbf{E}=-\partial\mathbf{B}/\partial t\qquad\nabla\times\mathbf{B}=\mu_0\varepsilon_0\,\partial\mathbf{E}/\partial t', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Coupled curl equations", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MaxwellVacuum_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellVacuum_p3.mp3", time_offset=0)
        title = Text("Maxwell in Vacuum  (Bennett 2.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla^2\mathbf{E}=\mu_0\varepsilon_0\,\partial^2\mathbf{E}/\partial t^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("EM wave equation", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MaxwellVacuum_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MaxwellVacuum_p4.mp3", time_offset=0)
        title = Text("Maxwell in Vacuum  (Bennett 2.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Fields sustain each other — no medium needed", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class EMWaveDerivation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p1.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Take curl of Faraday, substitute Ampere-Maxwell", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class EMWaveDerivation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p2.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla\times(\nabla\times\mathbf{E})=-\mu_0\varepsilon_0\,\partial^2\mathbf{E}/\partial t^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("After substitution and vector identity", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveDerivation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p3.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\nabla^2\mathbf{E}=\mu_0\varepsilon_0\,\partial^2\mathbf{E}/\partial t^2\quad c=1/\sqrt{\mu_0\varepsilon_0}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Wave equation — speed = c", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveDerivation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p4.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'c=1/\sqrt{4\pi\times10^{-7}\times8.854\times10^{-12}}=2.998\times10^8\,\text{m/s}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Computed from EM measurements alone", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveDerivation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveDerivation_p5.mp3", time_offset=0)
        title = Text("EM Wave Equation Derivation", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Greatest physics calculation of the 19th century", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class EMWaveProperties_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p1.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{k}\perp\mathbf{E}\quad\mathbf{k}\perp\mathbf{B}\quad\mathbf{E}\perp\mathbf{B}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Transverse: E, B and k mutually perpendicular", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveProperties_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p2.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{B}=\hat{k}\times\mathbf{E}/v', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("B from E and propagation direction", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveProperties_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p3.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'E=cB\quad\text{in vacuum}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Magnitudes: E = cB", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveProperties_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p4.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("E and B oscillate in phase", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class EMWaveProperties_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p5.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'v=c/n\qquad\lambda_\text{med}=\lambda_0/n', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("In medium: c/n, wavelength shrinks, frequency fixed", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveProperties_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveProperties_p6.mp3", time_offset=0)
        title = Text("Properties of EM Waves  (Bennett 2.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Frequency unchanged at interface", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class EMWaveExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p1.mp3", time_offset=0)
        title = Text("Example: Finding B from E", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{E}=E_0\hat{x}\,e^{i(kz-\omega t)}\quad\text{find}\;\mathbf{B}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Given: E in x, propagating in z", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p2.mp3", time_offset=0)
        title = Text("Example: Finding B from E", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\hat{z}\times\hat{x}=\hat{y}\;\Rightarrow\;\mathbf{B}=E_0 c^{-1}\hat{y}\,e^{i(kz-\omega t)}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Cross product gives B direction", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p3.mp3", time_offset=0)
        title = Text("Example: Finding B from E", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{E}\perp\mathbf{B}\perp\hat{k}\;\checkmark\quad E=cB\;\checkmark', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("All properties verified", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p4.mp3", time_offset=0)
        title = Text("Example: Finding B from E", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=\tfrac{1}{2}\varepsilon_0 c E_0^2=1327\,\text{W/m}^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Irradiance  (Bennett Eq. 2.33)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class EMWaveExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p5.mp3", time_offset=0)
        title = Text("Example: Finding B from E", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Practice until this takes under 2 minutes", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class EMWaveExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/EMWaveExample_p6.mp3", time_offset=0)
        title = Text("Example: Finding B from E", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Exam calculation type — appears regularly", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p1.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathbf{S}=\frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Poynting vector — instantaneous energy flux", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p2.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=\langle|\mathbf{S}|\rangle=\frac{1}{2}\varepsilon_0 cn E_0^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Irradiance = time-averaged Poynting  (Bennett Eq. 2.33)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p3.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Factor 1/2 from time-averaging cos-squared", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p4.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("I proportional to E0 squared", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p5.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=5\,\text{mW}/(\pi\times1\,\text{mm}^2)=1592\,\text{W/m}^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("5mW laser, 1mm radius", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p6.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'E_0=\sqrt{2I/(\varepsilon_0 c)}=1095\,\text{V/m}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Peak E-field", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p7.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'B_0=E_0/c=3.65\,\mu\text{T}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Peak B — 14x weaker than Earth's", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p8.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'P_\text{rad}=I/c\;(\text{absorber})\quad 2I/c\;(\text{mirror})', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Radiation pressure", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p9.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Solar irradiance 1361 W/m^2 -> ~9 micropascals on mirror", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class PoyntingIrradiance_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PoyntingIrradiance_p10.mp3", time_offset=0)
        title = Text("Poynting Vector and Irradiance", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("LIGO: 100kW intracavity — radiation pressure managed", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class RadiationPressure_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p1.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Light carries momentum — Maxwell 1865, Lebedev 1900", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class RadiationPressure_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p2.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'P_\text{rad}=I/c\;(\text{absorbing})\quad 2I/c\;(\text{reflecting})', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Radiation pressure formulas", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class RadiationPressure_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p3.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'P_\text{rad}=I(1+R)/c', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("General formula", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class RadiationPressure_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p4.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("IKAROS solar sail 2010: 1mN from 14x14m sail", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class RadiationPressure_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p5.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Optical tweezers: Nobel 2018 Arthur Ashkin", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class RadiationPressure_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p6.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("LIGO: 100kW beams — pressure must be managed", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class RadiationPressure_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p7.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Tiny but continuous — measurable over days", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class RadiationPressure_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/RadiationPressure_p8.mp3", time_offset=0)
        title = Text("Radiation Pressure  (Bennett 2.3.2)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Solar radiation pressure perturbs satellite orbits over years", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class DispersionScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p1.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Dispersion: refractive index n depends on frequency", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class DispersionScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p2.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n(\omega)=c/v_p(\omega)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("n varies with omega", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class DispersionScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p3.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Normal dispersion: n increases with frequency", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class DispersionScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p4.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Lorentz model: electrons as driven oscillators", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class DispersionScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p5.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'v_g=c/(n+\omega\,dn/d\omega)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Group velocity", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class DispersionScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p6.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Anomalous dispersion near resonance", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class DispersionScene_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p7.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Optical fibre: 17 ps/nm/km at 1550 nm", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class DispersionScene_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DispersionScene_p8.mp3", time_offset=0)
        title = Text("Dispersion and Refractive Index  (Bennett 3.9)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Dispersion-compensating fibres counteract broadening", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

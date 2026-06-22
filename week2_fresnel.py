# week2_fresnel.py
from manim import *
from utils import *

class Week2Intro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p1.mp3", time_offset=0)
        title = Text("Week 2 Introduction", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Bridge from Maxwell to geometric optics", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class Week2Intro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p2.mp3", time_offset=0)
        title = Text("Week 2 Introduction", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("The central tool: boundary conditions at interfaces", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class Week2Intro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p3.mp3", time_offset=0)
        title = Text("Week 2 Introduction", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Agenda: Snell law, Fresnel equations, Brewster, TIR", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class Week2TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.add(card)
        sub_t = Text("Week 2: light at an interface — directions and amplitudes", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week2TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.add(card)
        sub_t = Text("Snell law for direction — Fresnel equations for amplitude", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week2TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.add(card)
        sub_t = Text("Every lens surface, mirror coating and fibre depends on this", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week2TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.add(card)
        sub_t = Text("Bennett Chapter 3 — master the Fresnel calculation procedure", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class FermatPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p1.mp3", time_offset=0)
        title = Text("Fermat Principle  (Bennett 3.2.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Light takes the path of stationary travel time  (Fermat 1662)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FermatPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p2.mp3", time_offset=0)
        title = Text("Fermat Principle  (Bennett 3.2.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Reflection: minimise path length — gives angle-in = angle-out", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FermatPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p3.mp3", time_offset=0)
        title = Text("Fermat Principle  (Bennett 3.2.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n_i\sin\theta_i=n_t\sin\theta_t', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Minimise travel time — gives Snell law", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FermatPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p4.mp3", time_offset=0)
        title = Text("Fermat Principle  (Bennett 3.2.1)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Connects to Hamilton principle and Feynman path integral", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ReflectionRefraction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p1.mp3", time_offset=0)
        title = Text("Reflection and Snell Law", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\theta_i=\theta_r', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Law of reflection", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ReflectionRefraction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p2.mp3", time_offset=0)
        title = Text("Reflection and Snell Law", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n_i\sin\theta_i=n_t\sin\theta_t', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Snell Law  (Bennett Eq. 3.2)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ReflectionRefraction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p3.mp3", time_offset=0)
        title = Text("Reflection and Snell Law", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("n increases: bends toward normal", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ReflectionRefraction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p4.mp3", time_offset=0)
        title = Text("Reflection and Snell Law", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Frequency unchanged at interface", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ReflectionRefraction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p5.mp3", time_offset=0)
        title = Text("Reflection and Snell Law", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n_i=1.5,\;\theta_i=30°\;\Rightarrow\;\theta_t=48.6°', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Glass to air at 30 degrees", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ReflectionRefraction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p6.mp3", time_offset=0)
        title = Text("Reflection and Snell Law", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n_i=1.5,\;\theta_i=41.8°\;\Rightarrow\;\sin\theta_t=1.00', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Critical angle: TIR begins", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ReflectionRefraction_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p7.mp3", time_offset=0)
        title = Text("Reflection and Snell Law", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Above critical angle: no transmitted beam, R=1 exactly", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquationsDerivation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p1.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett 3.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("From Maxwell boundary conditions: tangential E and H continuous", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquationsDerivation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p2.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett 3.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("S-pol: E perpendicular to plane of incidence  (TE)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquationsDerivation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p3.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett 3.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'E_i+E_r=E_t\quad n_i\cos\theta_i(E_i-E_r)=n_t\cos\theta_t E_t', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Two boundary equations for s-pol", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelEquationsDerivation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p4.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett 3.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("P-pol: extra cosine factors — different coefficients", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquationsDerivation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p5.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett 3.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("S and P reflect independently", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquationsDerivation_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p6.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett 3.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Reflected light is partially polarised because of this", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p1.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Fresnel amplitude reflection and transmission coefficients", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p2.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'r_s=\frac{n_i\cos\theta_i-n_t\cos\theta_t}{n_i\cos\theta_i+n_t\cos\theta_t}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("s-pol reflection  (Bennett Eq. 3.11a)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p3.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r't_s=\frac{2n_i\cos\theta_i}{n_i\cos\theta_i+n_t\cos\theta_t}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("s-pol transmission  (Bennett Eq. 3.12a)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p4.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'r_p=\frac{n_t\cos\theta_i-n_i\cos\theta_t}{n_t\cos\theta_i+n_i\cos\theta_t}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("p-pol reflection  (Bennett Eq. 3.11b)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p5.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r't_p=\frac{2n_i\cos\theta_i}{n_t\cos\theta_i+n_i\cos\theta_t}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("p-pol transmission  (Bennett Eq. 3.12b)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelEquations_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p6.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'r=\frac{n_i-n_t}{n_i+n_t}\quad t=\frac{2n_i}{n_i+n_t}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Normal incidence — MEMORISE", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelEquations_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p7.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'r_\text{air-glass}=-0.2\quad R=0.04', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Air to glass: 4% reflected, pi phase shift", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelEquations_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p8.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Negative r: n increases — phase shift of pi", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquations_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p9.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Positive r: n decreases — no phase shift", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelEquations_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p10.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett 3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Phase signs critical for thin film interference in Week 6", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelFullExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p1.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 deg", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n_i=1.00,\;n_t=1.50,\;\theta_i=40°', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Given: air to glass at 40 degrees", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelFullExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p2.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 deg", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\sin\theta_t=(1.00/1.50)\sin40°\;\Rightarrow\;\theta_t=25.4°', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 1: Snell law FIRST", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelFullExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p3.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 deg", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("cos(40)=0.766, cos(25.4)=0.904", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FresnelFullExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p4.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 deg", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'r_s=-0.278\;\Rightarrow\;R_s=0.0772', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 3: s-pol — 7.7% reflected", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelFullExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p5.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 deg", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'r_p=+0.119\;\Rightarrow\;R_p=0.0142', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 4: p-pol — 1.4% reflected", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FresnelFullExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p6.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 deg", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'R_s+T_s=1.000\;\checkmark\quad R_p+T_p=1.000\;\checkmark', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 5: energy conservation verified", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ReflectivityTransmissivity_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p1.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'R=|r|^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Reflectivity = modulus squared of r", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ReflectivityTransmissivity_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p2.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'T=\frac{n_t\cos\theta_t}{n_i\cos\theta_i}|t|^2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Transmissivity — NOT simply t-squared", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ReflectivityTransmissivity_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p3.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'R+T=1', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Energy conservation — ALWAYS verify", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ReflectivityTransmissivity_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p4.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("T=t-squared is a common fatal error", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ReflectivityTransmissivity_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p5.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Camera lens 10 surfaces, no AR: only 67% transmitted", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class BrewsterTIR_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p1.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\tan\theta_B=n_t/n_i', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Brewster angle — r_p=0 exactly", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class BrewsterTIR_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p2.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\theta_B=\arctan(1.5)=56.3°', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Brewster for n=1.5", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class BrewsterTIR_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p3.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\sin\theta_c=n_t/n_i\quad(n_i>n_t)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Critical angle for TIR", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class BrewsterTIR_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p4.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\theta_c=\arcsin(1/1.5)=41.8°', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Critical angle for n=1.5 to air", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class BrewsterTIR_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p5.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("At Brewster: reflected and refracted perpendicular", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class BrewsterTIR_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p6.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Laser Brewster windows: p-pol passes with zero loss", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class BrewsterTIR_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p7.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("TIR: R=1.000 — used in fibres and prisms", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class BrewsterTIR_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p8.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5)", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Diamond: theta_c=24.4 degrees — makes it sparkle", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MalusLaw_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p1.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett 6.2.1)", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=I_0\cos^2\theta', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Malus Law  (Bennett Eq. 6.6)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MalusLaw_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p2.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett 6.2.1)", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("theta=0: full | theta=90: zero | theta=45: half", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MalusLaw_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p3.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett 6.2.1)", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Three polarisers: H at 0, at 45, V at 90", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MalusLaw_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p4.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett 6.2.1)", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I_0\xrightarrow{H}I_0/2\xrightarrow{45°}I_0/4\xrightarrow{V}I_0/8', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Result: I0/8", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MalusLaw_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p5.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett 6.2.1)", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Without middle: zero output — crossed polarisers block all", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MalusLaw_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p6.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett 6.2.1)", font_size=38, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Unpolarised through polariser: I0/2", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

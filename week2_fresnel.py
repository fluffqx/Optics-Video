# week2_fresnel.py
from manim import *
from utils import *

class Week2TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Week 2: what happens when light hits an interface", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Snell's law for direction — Fresnel equations for amplitude", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Every lens, mirror coating and optical fibre depends on this", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Bennett Chapter 3 — Reflection and Refraction", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p1.mp3", time_offset=0)
        title = Text("What Happens at an Interface?  (Bennett 3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Even transparent glass reflects ~4% from each surface", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p2.mp3", time_offset=0)
        title = Text("What Happens at an Interface?  (Bennett 3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Derived from Maxwell's boundary conditions at the interface", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p3.mp3", time_offset=0)
        title = Text("What Happens at an Interface?  (Bennett 3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\text{s-pol: }\mathbf{E}\perp\text{plane of incidence}\quad\text{p-pol: }\mathbf{E}\parallel\text{plane}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("S and P polarisations interact differently with interface", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FermatPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p1.mp3", time_offset=0)
        title = Text("Fermat's Principle  (Bennett Section 3.2.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Fermat's principle: light takes the path of stationary travel time", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p2.mp3", time_offset=0)
        title = Text("Fermat's Principle  (Bennett Section 3.2.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Reflection: minimise total path length — gives angle in = angle out", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p3.mp3", time_offset=0)
        title = Text("Fermat's Principle  (Bennett Section 3.2.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"n_i\sin\theta_i=n_t\sin\theta_t", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Refraction: minimise time with different speeds — gives Snell's law", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FermatPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p4.mp3", time_offset=0)
        title = Text("Fermat's Principle  (Bennett Section 3.2.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Fermat connects optics to variational mechanics (Hamilton, Feynman)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p1.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\theta_i=\theta_r", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Law of reflection — angle in equals angle out", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p2.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"n_i\sin\theta_i=n_t\sin\theta_t", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Snell's Law  (Bennett Eq. 3.2)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p3.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("n increases: refracted beam bends toward normal", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p4.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("n decreases: refracted beam bends away from normal", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p5.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Frequency fixed — wavelength = lambda0/n in medium", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p6.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\text{Example: }n_i=1.5,\;\theta_i=30°\;\Rightarrow\;\theta_t=48.6°", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Glass to air — beam bends away from normal", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p7.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\text{At }\theta_i=41.8°:\;\sin\theta_t=1.000\;\Rightarrow\;\text{TIR}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Critical angle reached — total internal reflection", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p1.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Fresnel equations from Maxwell boundary conditions  (Bennett 3.3)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p2.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Tangential E and tangential H continuous across interface", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p3.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("S-polarisation: E already tangential, simple boundary condition", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p4.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"E_i+E_r=E_t\quad n_i\cos\theta_i(E_i-E_r)=n_t\cos\theta_t\,E_t", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Two equations for s-pol give r-s and t-s", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p5.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("P-polarisation: extra cosine factors from geometry", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p6.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("S and P components reflect independently with different coefficients", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p1.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Fresnel equations: amplitude reflection and transmission coefficients", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p2.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"r_\perp=\frac{n_i\cos\theta_i-n_t\cos\theta_t}{n_i\cos\theta_i+n_t\cos\theta_t}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("s-polarisation reflection coefficient  (Bennett Eq. 3.11a)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p3.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"t_\perp=\frac{2n_i\cos\theta_i}{n_i\cos\theta_i+n_t\cos\theta_t}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("s-polarisation transmission coefficient  (Bennett Eq. 3.12a)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p4.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"r_\parallel=\frac{n_t\cos\theta_i-n_i\cos\theta_t}{n_t\cos\theta_i+n_i\cos\theta_t}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("p-polarisation reflection coefficient  (Bennett Eq. 3.11b)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p5.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"t_\parallel=\frac{2n_i\cos\theta_i}{n_t\cos\theta_i+n_i\cos\theta_t}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("p-polarisation transmission coefficient  (Bennett Eq. 3.12b)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelEquations_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p6.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"r=\frac{n_i-n_t}{n_i+n_t}\quad t=\frac{2n_i}{n_i+n_t}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Normal incidence — MEMORISE  (theta-i = 0)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelEquations_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p7.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"r_\text{air\to glass}=\frac{1-1.5}{1+1.5}=-0.2\quad R=0.04", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Air to glass n=1.5: 4% reflected — negative sign = pi phase shift", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelEquations_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p8.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Negative r means pi phase shift on reflection (n increases)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p9.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("No phase shift when going from denser to rarer medium", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p10.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Phase shifts critical for thin film interference — Week 6", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p1.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"n_i=1.0,\;n_t=1.5,\;\theta_i=40°", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Given: air to glass, angle 40 degrees", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelFullExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p2.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\sin\theta_t=\frac{1.0}{1.5}\sin40°=0.4285\;\Rightarrow\;\theta_t=25.37°", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Snell's law — refracted angle", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelFullExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p3.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"r_\perp=\frac{0.766-1.5\times0.904}{0.766+1.5\times0.904}=-0.278\;\Rightarrow\;R_s=0.0772", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("s-pol: 7.7% reflected", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelFullExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p4.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"r_\parallel=\frac{1.5\times0.766-0.904}{1.5\times0.766+0.904}=+0.119\;\Rightarrow\;R_p=0.0143", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("p-pol: 1.4% reflected", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelFullExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p5.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"T_s=1-0.077=0.923\quad T_p=1-0.014=0.986\quad R+T=1\;\checkmark", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Energy conservation verified for both polarisations", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FresnelFullExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p6.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("p-pol near Brewster's angle: much less reflection than s-pol", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p1.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"R=|r|^2", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Reflectivity = modulus squared of amplitude coefficient", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p2.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"T=\frac{n_t\cos\theta_t}{n_i\cos\theta_i}|t|^2", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Transmissivity — NOT simply |t|^2, includes beam geometry", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p3.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"R+T=1", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Energy conservation — ALWAYS verify this in exam", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p4.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("T = |t|² is a common and fatal exam error — include the ratio", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p5.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Normal incidence air/glass: R=0.04, T=0.96, sum=1.00 — check", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p1.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\tan\theta_B=n_t/n_i", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Brewster's angle — r-p = 0, reflected beam purely s-polarised", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class BrewsterTIR_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p2.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\sin\theta_c=n_t/n_i\quad(n_i>n_t)", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Critical angle for total internal reflection", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class BrewsterTIR_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p3.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\theta_B(\text{air/glass})=\arctan(1.5)=56.3°", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Brewster angle for n=1.5 glass", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class BrewsterTIR_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p4.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\theta_c(\text{glass/air})=\arcsin(1/1.5)=41.8°", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Critical angle for n=1.5 glass to air", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class BrewsterTIR_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p5.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("At Brewster: reflected + refracted beams perpendicular", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p6.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Laser Brewster windows: p-pol passes with zero reflection loss", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p7.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("TIR: R = 1.000 exactly — used in optical fibres and prisms", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p8.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Diamond: theta-c = 24.4 degrees — total reflection makes it sparkle", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p1.mp3", time_offset=0)
        title = Text("Malus's Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I=I_0\cos^2\theta", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Malus's Law  (Bennett Eq. 6.6)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MalusLaw_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p2.mp3", time_offset=0)
        title = Text("Malus's Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("theta = 0: full transmission | theta = 90: complete extinction", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p3.mp3", time_offset=0)
        title = Text("Malus's Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("theta = 45: exactly half the intensity transmitted", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p4.mp3", time_offset=0)
        title = Text("Malus's Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Three crossed polarisers: 0, 45, 90 degrees", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p5.mp3", time_offset=0)
        title = Text("Malus's Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I_1=I_0/2\quad I_2=I_0/4\quad I_3=I_0/8", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Three polariser sequence — inserting middle one allows some light through", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MalusLaw_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p6.mp3", time_offset=0)
        title = Text("Malus's Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Without middle polariser: zero output (0 and 90 are crossed)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)


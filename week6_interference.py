# week6_interference.py
from manim import *
from utils import *

class Week6TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Week 6: interference — the wave nature of light made visible", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Superposition: fields add, intensity can be 4x or 0", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Bennett Chapter 7 Sections 7.3 through 7.8 and 7.12", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Applications: AR coatings, LIGO, OCT, spectroscopy", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p1.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Interference: superposition of coherent waves gives non-trivial intensity", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p2.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I=I_1+I_2+2\sqrt{I_1 I_2}\cos\delta", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("General two-beam interference formula  (Bennett Eq. 7.14)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p3.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Constructive: delta = 2m*pi -> I_max = (sqrt(I1)+sqrt(I2))^2", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p4.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Destructive: delta = (2m+1)*pi -> I_min = (sqrt(I1)-sqrt(I2))^2", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p5.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Equal beams I1=I2=I0: I ranges from 0 to 4*I0", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p1.mp3", time_offset=0)
        title = Text("Two-Beam Interference Formula  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\tilde{E}_\mathrm{tot}=E_1 e^{i\phi_1}+E_2 e^{i\phi_2}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Total field = sum of two complex amplitudes", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p2.mp3", time_offset=0)
        title = Text("Two-Beam Interference Formula  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I=|\tilde{E}_\mathrm{tot}|^2=I_1+I_2+2\sqrt{I_1 I_2}\cos\delta\quad\delta=\phi_2-\phi_1", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Expand modulus squared — interference term appears", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p3.mp3", time_offset=0)
        title = Text("Two-Beam Interference Formula  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\delta=\frac{2\pi}{\lambda}\cdot\text{OPD}+\Delta\phi_\mathrm{refl}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Phase difference from optical path difference + reflection shifts", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p4.mp3", time_offset=0)
        title = Text("Two-Beam Interference Formula  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Two sources of phase difference: geometry and reflection", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p5.mp3", time_offset=0)
        title = Text("Two-Beam Interference Formula  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Reflection shift: +pi when n increases, 0 when n decreases", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p1.mp3", time_offset=0)
        title = Text("Young's Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"d\sin\theta_m=m\lambda\;\Rightarrow\;\text{bright fringes}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Young's bright fringe condition  (Bennett Eq. 7.18)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p2.mp3", time_offset=0)
        title = Text("Young's Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\Delta y=\frac{\lambda L}{d}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Fringe spacing on screen at distance L  (Bennett Eq. 7.19)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p3.mp3", time_offset=0)
        title = Text("Young's Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I=4I_0\cos^2\!\left(\frac{\pi d y}{\lambda L}\right)", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Intensity pattern — cosine squared", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p4.mp3", time_offset=0)
        title = Text("Young's Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Example: d=0.1mm, L=1.5m, lambda=589nm -> Delta-y = 8.84mm", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p5.mp3", time_offset=0)
        title = Text("Young's Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\text{5th bright fringe: }y_5=5\times8.84=44.2\,\text{mm}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Fifth fringe position above centre", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p6.mp3", time_offset=0)
        title = Text("Young's Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Young 1801: first conclusive proof light is a wave", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p7.mp3", time_offset=0)
        title = Text("Young's Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Envelope modulated by single-slit diffraction function — Week 7", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p1.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\delta=\frac{4\pi n_f t\cos\theta_t}{\lambda_0}+\Delta\phi_\mathrm{refl}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Phase difference for thin film  (Bennett Eq. 7.26)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p2.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Step 1: for each reflection, does n increase? Yes -> +pi shift", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p3.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Step 2: net phase shift = beam2 shifts minus beam1 shifts", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p4.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\delta=2m\pi\;\text{constructive}\quad\delta=(2m+1)\pi\;\text{destructive}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Constructive and destructive reflection conditions", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p5.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("AR coating: MgF2 (n=1.38) on glass (n=1.52)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p6.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Both reflections: n increases each time -> both +pi -> net shift = 0", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p7.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"2n_f t=\lambda/2\;\Rightarrow\;t=\frac{\lambda_0}{4n_f}=99.6\,\text{nm}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("AR condition: destructive -> t = lambda0/(4*n_f)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p8.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Soap bubble colours: varying thickness gives different resonant lambda", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p9.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("White light: all wavelengths present, different colours cancel at each t", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p10.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Exam: always track both reflection phase shifts carefully", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p1.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"V=\frac{I_\mathrm{max}-I_\mathrm{min}}{I_\mathrm{max}+I_\mathrm{min}}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Fringe visibility  (Bennett Eq. 7.30)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FringeVisibility_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p2.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"V=\frac{2\sqrt{I_1 I_2}}{I_1+I_2}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Visibility maximised when I1 = I2 -> V = 1", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FringeVisibility_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p3.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"l_c=\frac{\lambda^2}{\Delta\lambda}=\frac{c}{\Delta\nu}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Coherence length — OPD must be less than l_c for fringes", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FringeVisibility_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p4.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("White light: l_c ~ 1 micron — only nearest-order fringes visible", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p5.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Sodium lamp Delta-lambda~0.001nm: l_c ~ 0.35 m", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p1.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathrm{OPD}=2\Delta L\;\Rightarrow\;\delta=\frac{4\pi\Delta L}{\lambda}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Michelson: mirror displacement Delta-L gives OPD = 2*Delta-L", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MichelsonScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p2.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"N=\frac{2\Delta L}{\lambda}\;\Rightarrow\;\lambda=\frac{2\Delta L}{N}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Count N fringes as mirror moves Delta-L -> measure wavelength", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MichelsonScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p3.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathrm{RP}=\frac{2L}{\lambda}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Resolving power = 2L/lambda — longer path, sharper resolution", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MichelsonScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p4.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Michelson 1881: searched for aether — null result led to relativity", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p5.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("LIGO: 4 km arms, FP cavities give 1600 km effective path", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)


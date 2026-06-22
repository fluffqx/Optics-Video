# week6_interference.py
from manim import *
from utils import *

class Week6TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.add(card)
        sub_t = Text("Week 6: interference — wave nature of light made visible", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week6TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.add(card)
        sub_t = Text("Two coherent beams: intensity 0 to 4*I0 depending on phase", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week6TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.add(card)
        sub_t = Text("Bennett Chapter 7 Sections 7.3-7.8, 7.12", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week6TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.add(card)
        sub_t = Text("Applications: AR coatings, LIGO, spectroscopy, holography", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class InterferenceIntroScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p1.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=I_1+I_2+2\sqrt{I_1 I_2}\cos\delta', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Two-beam interference  (Bennett Eq. 7.14)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class InterferenceIntroScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p2.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Constructive: delta=2m*pi", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class InterferenceIntroScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p3.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Destructive: delta=(2m+1)*pi", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class InterferenceIntroScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p4.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Equal beams: 0 to 4*I0", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class InterferenceIntroScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p5.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Energy conserved — redistributed, not created", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class TwoBeamInterference_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p1.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=I_1+I_2+2\sqrt{I_1 I_2}\cos\delta\quad\delta=\phi_2-\phi_1', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Interference from modulus squared", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class TwoBeamInterference_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p2.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\delta=\frac{2\pi}{\lambda}\cdot\text{OPD}+\Delta\phi_\text{refl}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Phase: geometric path + reflection shifts", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class TwoBeamInterference_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p3.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Reflection shift: +pi when n increases, 0 otherwise", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class TwoBeamInterference_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p4.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Both sources must be included", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class TwoBeamInterference_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p5.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("For equal beams: I=4*I0*cos^2(delta/2)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class YoungDoubleSlit_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p1.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'd\sin\theta_m=m\lambda', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Bright fringe condition  (Bennett Eq. 7.18)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class YoungDoubleSlit_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p2.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\Delta y=\frac{\lambda L}{d}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Fringe spacing  (Bennett Eq. 7.19) — KEY FORMULA", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class YoungDoubleSlit_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p3.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=4I_0\cos^2\!\left(\frac{\pi dy}{\lambda L}\right)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Intensity pattern", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class YoungDoubleSlit_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p4.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("d=0.1mm, L=1.5m, lambda=589nm: delta-y=8.84mm", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class YoungDoubleSlit_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p5.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'y_5=44.2\,\text{mm}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Fifth fringe above centre", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class YoungDoubleSlit_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p6.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Young 1801: first conclusive proof light is a wave", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class YoungDoubleSlit_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p7.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Envelope from single-slit diffraction — Week 7", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p1.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\delta=\frac{4\pi n_f t\cos\theta_t}{\lambda_0}+\Delta\phi_\text{refl}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Total phase for thin film  (Bennett Eq. 7.26)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p2.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Step 1: does n increase at each reflection? Yes -> +pi", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p3.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Step 2: net shift = beam2 shifts minus beam1 shifts", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p4.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'2n_f t=\lambda/2\;\Rightarrow\;t=\lambda_0/(4n_f)=99.6\,\text{nm}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("AR coating: MgF2 on glass", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p5.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Soap bubble colours: different t, different resonant lambda", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p6.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Never skip reflection phase analysis", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p7.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Both surfaces must be tracked", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p8.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Normal incidence: cos(theta_t)=1", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p9.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("AR coatings are quarter-wavelength thick", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinFilmInterference_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p10.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Camera lens 10 surfaces, all AR coated", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FringeVisibility_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p1.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'V=\frac{I_\text{max}-I_\text{min}}{I_\text{max}+I_\text{min}}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Fringe visibility  (Bennett Eq. 7.30)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FringeVisibility_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p2.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'V=\frac{2\sqrt{I_1 I_2}}{I_1+I_2}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Maximised when I1=I2", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FringeVisibility_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p3.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'l_c=\lambda^2/\Delta\lambda=c/\Delta\nu', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Coherence length", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FringeVisibility_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p4.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("White light: 1um | Na lamp: 0.35m | He-Ne: 300m", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FringeVisibility_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p5.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Stellar interferometry: visibility vs baseline -> star diameter", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MichelsonScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p1.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'N=2\Delta L/\lambda', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Count N fringes as mirror moves delta-L", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MichelsonScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p2.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\text{RP}=2L/\lambda', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Resolving power", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MichelsonScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p3.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Michelson-Morley 1881: null result, no aether", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MichelsonScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p4.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("LIGO: 4km arms, FP cavities -> 1600km effective path", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MichelsonScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p5.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\Delta L_\text{LIGO}=10^{-18}\,\text{m}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("LIGO sensitivity — first detection 2015", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

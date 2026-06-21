# formula_sheet_recap.py
from manim import *
from utils import *

class FormulaSheetTitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p1.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Complete formula reference for 31OPT Optics", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FormulaSheetTitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p2.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Know when to use each formula — not just the algebra", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FormulaSheetTitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p3.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Approach: formula -> substitute with units -> check reasonableness", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p1.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Midterm covers Weeks 1-3: waves, Maxwell, Fresnel, geometric optics", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p2.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\frac{\partial^2\Psi}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2}\quad v=f\lambda=\frac{\omega}{k}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Week 1: wave equation and harmonic wave relations", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p3.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"n_i\sin\theta_i=n_t\sin\theta_t\quad r_\perp,r_\parallel,R+T=1", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Week 2: Snell's law, Fresnel coefficients, energy conservation", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p4.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\frac{1}{s_o}+\frac{1}{s_i}=\frac{1}{f}\quad m=-s_i/s_o", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Week 3: thin lens equation and magnification", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p5.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Most common errors: sign conventions, T not simply |t|^2, R+T check", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p1.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Final exam: all 8 weeks — systematic formula review", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p2.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I=4I_0\cos^2(\pi d y/\lambda L)\quad\Delta y=\lambda L/d", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Week 6: Young's fringes — intensity pattern and spacing", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p3.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I=I_0(\sin\beta/\beta)^2\quad\theta_\mathrm{min}=1.22\lambda/D\quad Nm", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Week 7: single slit, Rayleigh, grating resolving power", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p4.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I_t=I_0/(1+F\sin^2\delta/2)\quad\mathrm{RP}=N\mathcal{F}\quad\Delta\nu=c/2nd", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Week 8: Airy function, resolving power, FSR", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p5.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Week 5: Jones matrices — multiply RIGHT to LEFT in order of encounter", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)


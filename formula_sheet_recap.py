# formula_sheet_recap.py
from manim import *
from utils import *

class FormulaSheetTitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p1.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Complete formula reference for all 8 weeks", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FormulaSheetTitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p2.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Know WHEN to use each formula", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FormulaSheetTitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p3.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Write formula, substitute, check dimensions", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MidtermPrepScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p1.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Midterm: Weeks 1-3", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MidtermPrepScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p2.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\partial^2\Psi/\partial x^2=(1/v^2)\partial^2\Psi/\partial t^2\quad v=\omega/k=f\lambda', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Week 1: wave equation and relations", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MidtermPrepScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p3.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n_i\sin\theta_i=n_t\sin\theta_t\quad r_s,r_p,\;R+T=1', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Week 2: Snell, Fresnel, conservation", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MidtermPrepScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p4.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'1/s_o+1/s_i=1/f\quad m=-s_i/s_o', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Week 3: thin lens equation", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MidtermPrepScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p5.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Errors: sign conventions, T=t^2, not checking R+T=1", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FinalExamPrepScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p1.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Final exam: all 8 weeks", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FinalExamPrepScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p2.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=4I_0\cos^2(\pi dy/\lambda L)\quad\Delta y=\lambda L/d', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Week 6: Young fringes", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FinalExamPrepScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p3.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I=I_0(\sin\beta/\beta)^2\quad\theta_\text{min}=1.22\lambda/D\quad\text{RP}=Nm', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Week 7: diffraction", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FinalExamPrepScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p4.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I_t=I_0/(1+F\sin^2(\delta/2))\quad\text{RP}=N\mathcal{F}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Week 8: Fabry-Perot", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FinalExamPrepScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p5.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Jones: multiply RIGHT to LEFT | Matrix: det=1 always", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

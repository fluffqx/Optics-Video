# formula_sheet_recap.py — paragraph-per-scene
from manim import *
from utils import *

class FormulaSheetTitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p1.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This section animates the complete official 31OPT formula",
            "sheet — every equation you are given in the exam, explained",
            "in context.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FormulaSheetTitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p2.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The formula sheet is provided during the exam, so the goal",
            "is not to memorise it blindly. The goal is to understand",
            "every symbol deeply enough that you can use any formula",
            "correctly under time pressure.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FormulaSheetTitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FormulaSheetTitleCard_p3.mp3", time_offset=0)
        title = Text("Formula Sheet and Exam Preparation", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "We'll go through the sheet section by section, the same way",
            "it appears in the exam.",
        ])
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
        b = txt_block([
            "The midterm covers everything from weeks 1 through 3 —",
            "electromagnetic waves, Fresnel equations, and geometric",
            "optics.",
        ])
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
        b = txt_block([
            "It's a one-hour written exam. No AI tools, no phones — just",
            "pen, paper, ruler, calculator, and the formula sheet.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p3.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The most important advice: the formula sheet gives you the",
            "equations, but it does not tell you when to use which one,",
            "or how to handle sign conventions. That's what you need to",
            "practise.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p4.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Go through the SLT problems from weeks 1 to 3. They are at",
            "exactly the right level of difficulty. If you can solve",
            "those independently, you are ready for the midterm.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p5.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A few specific things to watch for. First: Fresnel equations",
            "— always identify which polarisation you're dealing with",
            "before you start. Second: thin lenses and mirrors — draw the",
            "ray diagram first, always. It prevents sign errors. Third:",
            "radiation pressure — remember the factor of 2 for a",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MidtermPrepScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MidtermPrepScene_p6.mp3", time_offset=0)
        title = Text("Midterm Preparation  (Weeks 1-3)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Good luck.",
        ])
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
        b = txt_block([
            "The final exam covers all eight weeks. It's three hours, and",
            "it counts for 85 percent of your grade.",
        ])
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
        b = txt_block([
            "The grading formula is: FINAL equals 0.85 times your exam",
            "score, plus 0.15 times your midterm score, plus your SLT",
            "bonus. To pass, you need a FINAL of at least 6 AND an exam",
            "score of at least 5. Both conditions must be met.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p3.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The SLT bonus can add up to a full point to your grade if",
            "you earned at least 100 SLT points across the semester.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p4.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The topics that appear most often in exam questions are:",
            "Fresnel calculations, thin film interference, Young's double",
            "slit, single slit diffraction, grating equation with",
            "resolving power, Fabry-Pérot with finesse and free spectral",
            "range, Jones matrices for polarisation, and the Rayleigh",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p5.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For each of these, you should be able to: set up the problem",
            "from scratch, identify all the relevant variables, apply the",
            "correct formula with correct sign conventions, and compute a",
            "numerical answer.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p6.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The best preparation is still the SLT problem sets. They are",
            "designed to be at exam level, and many are directly taken",
            "from past exams. If you can solve all nine SLT sets",
            "independently, you are fully prepared.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinalExamPrepScene_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinalExamPrepScene_p7.mp3", time_offset=0)
        title = Text("Final Exam Preparation  (All 8 Weeks)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "You can do this. Good luck.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

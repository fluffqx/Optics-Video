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
        b = txt_block([
            "This section provides a complete formula reference for 31OPT",
            "Optics at TU/e, covering all eight weeks of the course. Each",
            "formula is stated with its Bennett equation number and the",
            "conditions under which it applies.",
        ])
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
        b = txt_block([
            "The formulas are organised by week and topic. For each",
            "formula: know the symbol definitions, the units, and at",
            "least one worked numerical example. In the exam, you will",
            "have access to a formula sheet — but formula sheet access is",
            "only useful if you know when and how to apply each formula.",
        ])
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
        b = txt_block([
            "Approach the exam by reading the problem carefully,",
            "identifying which week's material it draws on, writing down",
            "the relevant formula with all symbols defined, substituting",
            "numerical values with units, and checking the answer for",
            "dimensional consistency and physical reasonableness. If an",
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
            "The midterm examination at TU/e covers Weeks 1 through 3:",
            "waves, Maxwell's equations, Fresnel equations, and geometric",
            "optics. Here is a systematic preparation guide based on the",
            "types of problems that appear.",
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
            "Wave equation problems: you may be asked to verify that a",
            "given function satisfies the wave equation, identify the",
            "wave speed from the equation, or write down a wave function",
            "given wavelength and frequency. Practice differentiating",
            "expressions like A e to the i kx minus omega t twice with",
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
            "Fresnel equation problems: given n-i, n-t, and theta-i, you",
            "must find theta-t from Snell's law, then compute r-s, r-p,",
            "R-s, R-p, T-s, T-p, and verify R plus T equals 1. The",
            "calculation for r-p is the one students most often get wrong",
            "— double-check the sign convention. Brewster's angle and",
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
            "Geometric optics problems: thin lens equation problems",
            "almost always involve finding the image location and",
            "magnification for an object at a given distance. Remember",
            "the sign convention: real images have positive s-i, virtual",
            "images have negative s-i, real objects have positive s-o.",
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
            "Exam technique: always write down the formula, substitute",
            "values with units, and state the answer with units and a",
            "physical interpretation. If R plus T does not sum to one,",
            "you have made an error — go back and find it before moving",
            "on.",
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
            "The final examination covers all eight weeks. The most",
            "important thing to bring is fluency with formulas — you",
            "should not need to derive them under time pressure. Here is",
            "a rapid review of the key formulas by week.",
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
            "Week 1: wave equation, harmonic wave relations v equals f",
            "lambda, complex representation, superposition principle.",
            "Week 2: Snell's law, Fresnel equations for r-s and r-p, R",
            "equals r-squared, R plus T equals 1, Brewster's angle",
            "tangent theta-B equals n-t over n-i, critical angle sine",
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
            "Week 4: translation matrix, thin lens matrix, system matrix",
            "and how to extract cardinal points. Week 5: Jones vectors",
            "for six standard states, Jones matrices from Bennett Table",
            "6.1, multiplication order M-N times ... times M-1, intensity",
            "from modulus-squared. Week 6: interference formula I equals",
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
            "Week 7: single-slit zeros at b sine theta equals m lambda,",
            "Airy disk radius sine theta-one equals 1.22 lambda over D,",
            "Rayleigh criterion, grating equation d sine theta-m equals m",
            "lambda, resolving power R equals N m. Week 8: Airy function",
            "I-t equals I-naught over 1 plus F sine squared delta over 2,",
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
            "The most common mistakes: confusing F with script-F in the",
            "Fabry-Pérot; forgetting the cosine theta factor in thin-film",
            "interference for oblique incidence; using the wrong sign in",
            "Brewster vs critical angle formula; not using the correct",
            "factor for T (it is not simply t-squared). Review the worked",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

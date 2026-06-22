# slt_week8.py
# 31OPT Optics — SLT Week 8 (Set 8): Michelson & Diffraction
from manim import *
from utils import *


class SLT_Week8_Problem1(Scene):
    """Variable-reflectivity mirror in Michelson interferometer."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 8 — Problem 1: Variable Michelson", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Michelson interferometer: silver mirror R_s=1, variable mirror R_v=0.25.", font_size=26, color=WHITE),
            Text("Laser: lambda_0=640 nm. Silver mirror at L+(n+1/4)*lambda_0 from beamsplitter.", font_size=26, color=WHITE),
            Text("(a) Explain why no position on the output screen is fully dark.", font_size=26, color=WHITE),
            Text("(b) Does it matter which mirror is moved? Argue quantitatively.", font_size=26, color=WHITE),
            Text("(c) Sketch/describe the radial intensity profile for R_v=0.25 and R_v=1.", font_size=26, color=WHITE),
            Text("(d) Derive an expression for central fringe intensity vs R_v (constructive and destructive).", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        prob.next_to(slt_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(120)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(120)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))


class SLT_Week8_Problem2(Scene):
    """Multi-slit diffraction: intensity profiles for 1, 2, 4, 10 slits."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        slt_title = Text("SLT Week 8 — Problem 2: Slits Diffraction", font_size=34, color=GOLD)
        slt_title.to_edge(UP)
        self.play(Write(slt_title))

        prob = VGroup(
            Text("Laser at distance L from a single slit (width b). Screen behind slit.", font_size=26, color=WHITE),
            Text("(a) Describe the intensity pattern.", font_size=26, color=WHITE),
            Text("Second slit added: d=4b, same width b.", font_size=26, color=WHITE),
            Text("(b) Calculate I(x) for two slits. (c) Sketch the pattern.", font_size=26, color=WHITE),
            Text("Doubled again to 4 slits, d=4b.", font_size=26, color=WHITE),
            Text("(d) Calculate I(x) for 4 slits. (e) Sketch the pattern.", font_size=26, color=WHITE),
            Text("Now 10 slits, d=4b.", font_size=26, color=WHITE),
            Text("(f) Calculate I(x) for 10 slits. (g) Sketch the pattern.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        prob.next_to(slt_title, DOWN, buff=0.3)
        self.play(FadeIn(prob)); self.wait(120)

        prompt = Text("Pause and solve this yourself before continuing!", font_size=30, color=GOLD)
        prompt.to_edge(DOWN)
        self.play(FadeIn(prompt)); self.wait(120)
        self.play(FadeOut(VGroup(slt_title, prob, prompt)))

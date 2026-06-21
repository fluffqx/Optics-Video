# week4_matrix_polarisation.py — Week 4 (paragraph-per-scene)
from manim import *
from utils import *

class Week4TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p1.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Week 4 introduces a powerful systematic method for tracing",
            "rays through any optical system — matrix optics, also called",
            "the ray transfer matrix method.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p2.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The idea is elegant. We represent a ray by a two-component",
            "column vector: its height y above the optical axis, and its",
            "angle theta with respect to the axis. Then every optical",
            "element — lens, mirror, free space — is represented by a",
            "two-by-two matrix. To trace a ray through the whole system, we",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p3.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is why computers are so good at optical design. Matrix",
            "multiplication is fast and exact, and the same formalism works",
            "for any sequence of elements.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p4.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "There are four fundamental matrices. The translation matrix",
            "for free propagation over distance d has ones on the diagonal",
            "and d in the top right — the height increases by d times",
            "theta, while the angle is unchanged.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p5.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The thin lens matrix has a minus one over f in the lower left",
            "— the lens changes the ray angle but not its height at the",
            "lens.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p6.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The refraction matrix at a spherical surface accounts for both",
            "the change in angle due to the surface curvature and the ratio",
            "of refractive indices.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p7.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The mirror matrix looks like the lens matrix with minus two",
            "over R in the lower left.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p8.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "To find the system matrix for a complete optical system,",
            "multiply the individual matrices from right to left — the",
            "first element the ray encounters goes on the rightmost",
            "position.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p9.mp3", time_offset=0)
        title = Text("Matrix Optics, Superposition and Polarisation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "From the system matrix elements A, B, C, D, you can extract",
            "all cardinal points of the system: the effective focal length",
            "is minus one over C, and the principal planes can be located",
            "from A and D.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Matrix Optics Introduction", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Matrix optics represents any optical system as a single 2 by 2",
            "matrix. A ray is described by its height y above the optical",
            "axis and its angle theta with respect to the axis, written as",
            "a column vector.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Matrix Optics Introduction", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Each optical element maps the input ray vector to the output",
            "ray vector via matrix multiplication. For a sequence of N",
            "elements, we multiply the matrices from right to left — the",
            "first element the ray encounters goes on the rightmost",
            "position.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Matrix Optics Introduction", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This method is exact within the paraxial approximation and",
            "trivially handles arbitrarily complex systems. Computer-aided",
            "optical design tools use this formalism to trace millions of",
            "rays simultaneously.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p1.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "There are four elementary ray transfer matrices.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p2.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The translation matrix for free propagation over distance d",
            "has ones on the diagonal and d in the upper right. The height",
            "increases by d times theta while the angle is unchanged.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p3.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The thin lens matrix has minus one over f in the lower left.",
            "The lens changes the angle but not the height of a ray passing",
            "through it.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p4.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The refraction matrix at a spherical surface accounts for the",
            "angle change from Snell's law and the ratio of refractive",
            "indices.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p5.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The mirror matrix looks identical to the thin lens matrix with",
            "minus two over R in the lower left — equivalent to a thin lens",
            "with focal length R over 2.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p1.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Multiply all element matrices from right to left to get the",
            "system matrix with elements A, B, C, D.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p2.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The effective focal length is minus one over C. The front and",
            "back focal distances can be read off from A, C, and D. The",
            "determinant of the system matrix is always exactly 1 — this is",
            "a consequence of energy conservation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p3.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "If C equals zero, the effective focal length is infinite — the",
            "system is afocal. Parallel rays enter and parallel rays leave,",
            "just magnified. This is a beam expander.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p4.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The principal planes can also be located from the matrix",
            "elements, giving a complete paraxial description of any",
            "optical system however complex.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p1.mp3", time_offset=0)
        title = Text("Beam Expander — Matrix Example", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The beam expander is a classic matrix optics example. Two",
            "lenses with focal lengths f_1 and f_2, separated by d equals",
            "f_1 plus f_2.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p2.mp3", time_offset=0)
        title = Text("Beam Expander — Matrix Example", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "We multiply three matrices: the second lens, the free-space",
            "propagation, and the first lens — in that order from left to",
            "right.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p3.mp3", time_offset=0)
        title = Text("Beam Expander — Matrix Example", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resulting system matrix has zeros in the off-diagonal",
            "positions of the C element, confirming it is afocal. The beam",
            "magnification is the ratio f_2 over f_1. A parallel input beam",
            "emerges as a parallel output beam, expanded by this factor.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p4.mp3", time_offset=0)
        title = Text("Beam Expander — Matrix Example", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is used in laser beam expanders, Galilean telescopes, and",
            "spatial light modulators where a collimated beam of a specific",
            "diameter is required.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p1.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When two identical waves travel in opposite directions through",
            "the same medium, they create a remarkable pattern called a",
            "standing wave. Unlike a travelling wave, the pattern does not",
            "move — it oscillates in place.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p2.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The mathematical derivation uses the sum-to-product",
            "trigonometric identity. Adding A sine of kx minus omega t,",
            "plus A sine of kx plus omega t, gives two A sine of kx times",
            "cosine of omega t.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p3.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The spatial part, sine of kx, determines where the amplitude",
            "is large or small. The temporal part, cosine of omega t, makes",
            "the whole pattern oscillate in time.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p4.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Nodes are positions where the amplitude is permanently zero —",
            "the waves always cancel there. They occur wherever kx equals m",
            "pi, which means at positions x equals m times lambda over two.",
            "The spacing between nodes is exactly half a wavelength.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p5.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Antinodes are positions of maximum oscillation — the waves",
            "always add constructively there. They sit exactly halfway",
            "between adjacent nodes.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p6.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Standing waves are fundamental to understanding lasers,",
            "optical cavities, and musical instruments. In a laser cavity,",
            "only wavelengths that fit exactly into the cavity length can",
            "form standing waves — these are the laser modes.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p1.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Beating occurs when two waves of slightly different",
            "frequencies overlap. The result is a wave whose amplitude",
            "varies slowly in time — producing a periodic rise and fall in",
            "intensity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p2.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Mathematically, we add A cosine of omega-one times t plus A",
            "cosine of omega-two times t. Using the sum-to-product",
            "identity, this equals two A times cosine of the",
            "half-difference in frequencies times t, multiplied by cosine",
            "of the average frequency times t.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p3.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The fast oscillation has the average frequency — this is what",
            "you actually see or hear. The slow modulation of the amplitude",
            "has the beat frequency, which equals the absolute difference",
            "between the two frequencies.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p4.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "If f-one equals 440 hertz and f-two equals 443 hertz, the beat",
            "frequency is 3 hertz — you hear three amplitude pulses per",
            "second. Musicians use this to tune instruments — they adjust",
            "until the beats disappear, meaning the frequencies are equal.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p5.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In optics, beating between two laser frequencies produces an",
            "interference signal at the difference frequency. This is the",
            "basis of heterodyne detection, used in interferometry and",
            "optical communications.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p1.mp3", time_offset=0)
        title = Text("Polarization of Light", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Polarization is one of the most important properties of light,",
            "and one that our eyes cannot detect directly. For a plane wave",
            "travelling in the z-direction, the electric field lies in the",
            "x-y plane. The direction in which E oscillates defines the",
            "polarization state.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p2.mp3", time_offset=0)
        title = Text("Polarization of Light", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Linear polarization means the electric field always oscillates",
            "along a fixed straight line in the x-y plane. Horizontal,",
            "vertical, and diagonal are all forms of linear polarization. A",
            "polarizing filter transmits only one direction and blocks the",
            "perpendicular direction.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p3.mp3", time_offset=0)
        title = Text("Polarization of Light", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Circular polarization occurs when the x and y components have",
            "equal amplitudes but a ninety-degree phase difference. As the",
            "wave propagates, the tip of the E-vector traces a circle.",
            "Right circular polarization rotates clockwise when viewed",
            "face-on from the direction the wave is approaching. Left",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p4.mp3", time_offset=0)
        title = Text("Polarization of Light", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Elliptical polarization is the general case. When the",
            "amplitudes are unequal, or the phase difference is not zero,",
            "ninety, or one hundred eighty degrees, the E-vector traces an",
            "ellipse. Linear and circular are both special cases of",
            "elliptical polarization.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p5.mp3", time_offset=0)
        title = Text("Polarization of Light", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Natural light — from the sun, a light bulb, a flame — is",
            "unpolarized. It consists of a rapid random mixture of all",
            "polarization directions with no preferred orientation. When",
            "natural light reflects at Brewster's angle or passes through a",
            "polarizer, it becomes polarized.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

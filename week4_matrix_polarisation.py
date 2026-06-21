# week4_matrix_polarisation.py — paragraph-per-scene
from manim import *
from utils import *

class Week4TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5 and 7.1")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 4 combines three distinct topics: matrix optics for",
            "systematic ray tracing, superposition phenomena including",
            "standing waves and beating, and the basics of polarisation.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5 and 7.1")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Matrix optics provides a systematic, computer-friendly",
            "method for tracing rays through arbitrarily complex optical",
            "systems. Any sequence of lenses, mirrors, and free-space",
            "propagation steps can be represented as a single two-by-two",
            "matrix. This method is used professionally in laser design,",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5 and 7.1")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Standing waves and beating are superposition phenomena that",
            "arise from adding waves in particular configurations.",
            "Standing waves arise from two counter-propagating waves and",
            "are fundamental to laser resonators. Beating arises from two",
            "waves of slightly different frequencies and is the basis of",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5 and 7.1")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Polarisation describes the direction in which the electric",
            "field oscillates. Week 4 introduces the basic states:",
            "linear, circular, and elliptical polarisation. Week 5 will",
            "develop the Jones vector formalism for calculating",
            "polarisation transformations quantitatively.",
        ])
        b.move_to(ORIGIN)
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
            "Matrix optics represents any paraxial optical system as a",
            "single two-by-two matrix. A ray is described by a",
            "two-component column vector containing its height y above",
            "the optical axis and its angle theta to the axis. Each",
            "optical element maps the input ray vector to the output ray",
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
            "The power of this method comes from the fact that",
            "multiplying matrices corresponds to cascading optical",
            "elements. A system of ten lenses, five free-space",
            "propagation sections, and three mirrors — which would",
            "require solving fifteen separate geometric equations —",
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
            "The key constraint is that all matrices in this framework",
            "have a determinant of exactly one. This is a consequence of",
            "conservation of the optical path and is a useful check on",
            "matrix algebra.",
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
            "The translation matrix for free propagation through distance",
            "d has ones on the diagonal and d in the upper right: the",
            "height changes by d times the angle, while the angle remains",
            "unchanged. This is just the geometry of a straight ray.",
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
            "The thin lens matrix has a minus one over f in the lower",
            "left and ones elsewhere: the height is unchanged at a thin",
            "lens, but the angle is changed by minus y over f. This is",
            "the paraxial focusing condition.",
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
            "The refraction matrix at a spherical surface with radius R",
            "separating media with indices n-one and n-two accounts for",
            "both the Snell's law angle change and the unchanged height.",
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
            "The mirror matrix looks identical to the thin lens matrix",
            "with minus two over R in the lower left. This makes sense: a",
            "concave mirror with radius R has a focal length of R over",
            "two.",
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
            "To find the system matrix, multiply the individual element",
            "matrices from right to left — the first element encountered",
            "by the light goes on the right. The order matters because",
            "matrix multiplication is not commutative.",
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
            "Once we have the system matrix M with elements A, B, C, D,",
            "we can extract all the cardinal points of the optical system",
            "without knowing the internal structure.",
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
            "The effective focal length is minus one over C. If C equals",
            "zero, the system is afocal — parallel rays in give parallel",
            "rays out, which is the definition of a telescope or beam",
            "expander.",
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
            "The back focal distance — from the last physical element to",
            "the rear focal point — is given by D minus one, all over C.",
            "The front focal distance from the front focal point to the",
            "first element is minus A over C.",
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
            "The principal planes can be located from these quantities.",
            "All the focusing properties of the system are captured by",
            "specifying the two principal planes and the effective focal",
            "length.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p5.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The determinant of the system matrix must always equal one:",
            "AD minus BC equals one. This is a powerful check — if your",
            "computed matrix does not satisfy this, you have made an",
            "error.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p1.mp3", time_offset=0)
        title = Text("Beam Expander: Matrix Example", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The beam expander is a classic and important example. Two",
            "lenses with focal lengths f-one and f-two are separated by d",
            "equals f-one plus f-two. We calculate the system matrix.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p2.mp3", time_offset=0)
        title = Text("Beam Expander: Matrix Example", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Write the three matrices from right to left: thin lens",
            "f-one, free propagation f-one plus f-two, thin lens f-two.",
            "Multiply them out step by step.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p3.mp3", time_offset=0)
        title = Text("Beam Expander: Matrix Example", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The result has a C element equal to zero, confirming that",
            "the system is afocal. The A element equals minus f-two over",
            "f-one, which is the beam magnification. A beam entering with",
            "height y and zero angle exits with height minus f-two over",
            "f-one times y and zero angle — the beam has been expanded by",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p4.mp3", time_offset=0)
        title = Text("Beam Expander: Matrix Example", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is the operating principle of a telescope used in",
            "reverse, a Galilean beam expander, and a spatial light",
            "modulator relay system. The same matrix result applies to",
            "all of them.",
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
            "When two identical waves travel in opposite directions",
            "through the same medium, they superpose to create a standing",
            "wave — a pattern that oscillates in place without",
            "propagating.",
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
            "Using the trigonometric identity for the sum of cosines: A",
            "sine of kx minus omega t plus A sine of kx plus omega t",
            "equals 2A sine kx times cosine omega t. The spatial and",
            "temporal parts have separated completely. The amplitude 2A",
            "sine kx is purely spatial, and the cosine omega t factor is",
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
            "This means the wave pattern does not move. At a node — a",
            "position where sine kx equals zero — the amplitude is",
            "permanently zero, regardless of time. At an antinode — where",
            "sine kx equals plus or minus one — the amplitude oscillates",
            "between plus 2A and minus 2A.",
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
            "Nodes occur at kx equals m pi, meaning x equals m lambda",
            "over two. The spacing between adjacent nodes is lambda over",
            "two. Antinodes occur halfway between nodes.",
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
            "Standing waves are fundamental to lasers. The optical cavity",
            "formed by two mirrors supports standing waves only at",
            "frequencies where an integer number of half-wavelengths fit",
            "between the mirrors. This quantisation of allowed",
            "frequencies gives each laser its discrete set of",
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
            "Standing waves also explain why we can hear notes from a",
            "guitar string. The string can only vibrate in modes where",
            "nodes exist at both fixed ends. The allowed wavelengths are",
            "2L, L, 2L over 3, and so on — these give the fundamental",
            "frequency and its harmonics.",
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
            "frequencies are superimposed. The result is a wave that",
            "oscillates at the average of the two frequencies but whose",
            "amplitude varies slowly at the difference frequency.",
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
            "Mathematically: A cosine omega-one t plus A cosine omega-two",
            "t equals 2A cosine of omega-one minus omega-two over 2 times",
            "t, times cosine of omega-one plus omega-two over 2 times t.",
            "The first factor is the slowly varying envelope and the",
            "second is the fast oscillation at the average frequency.",
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
            "The beat frequency is the absolute value of f-one minus",
            "f-two. The amplitude modulation oscillates at half this",
            "rate, but since intensity goes as amplitude squared, the",
            "perceived intensity fluctuation occurs at the full beat",
            "frequency.",
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
            "If f-one equals 440 hertz and f-two equals 443 hertz, the",
            "beat frequency is 3 hertz — you hear the volume pulsate",
            "three times per second. Musicians use this to tune",
            "instruments: adjust the pitch until the beats become slower",
            "and finally disappear, at which point the frequencies are",
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
            "In optical interferometry, beating between two laser",
            "frequencies is called optical heterodyne detection. A signal",
            "beam at frequency omega-s is mixed with a local oscillator",
            "at frequency omega-lo. The detector output contains a",
            "component at the beat frequency omega-s minus omega-lo,",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p1.mp3", time_offset=0)
        title = Text("Polarization of Light  (Bennett 6.1-6.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Polarisation describes the direction in which the electric",
            "field oscillates as a wave propagates. For a plane wave",
            "travelling in the z-direction, the electric field lies in",
            "the xy-plane. The polarisation state specifies exactly how",
            "the field vector moves in this plane as time progresses.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p2.mp3", time_offset=0)
        title = Text("Polarization of Light  (Bennett 6.1-6.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Linear polarisation means the field always oscillates along",
            "a fixed line in the xy-plane. The field may point in the",
            "x-direction, the y-direction, at 45 degrees, or any other",
            "fixed angle. The angle of linear polarisation can take any",
            "value between zero and 180 degrees. Linear polarisation",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p3.mp3", time_offset=0)
        title = Text("Polarization of Light  (Bennett 6.1-6.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Circular polarisation occurs when the x and y components",
            "have equal amplitudes but differ in phase by pi over 2. The",
            "field vector then traces a circle in the xy-plane as time",
            "progresses. Right circular polarisation — by the physics",
            "convention — has the phase of y leading x by pi over 2,",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p4.mp3", time_offset=0)
        title = Text("Polarization of Light  (Bennett 6.1-6.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Elliptical polarisation is the general case. When the",
            "amplitudes are unequal, or the phase difference is neither",
            "zero, pi over 2, nor pi, the field tip traces an ellipse.",
            "The ellipse has a major axis, a minor axis, and an",
            "orientation angle. Linear and circular polarisation are",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p5.mp3", time_offset=0)
        title = Text("Polarization of Light  (Bennett 6.1-6.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Natural light from the sun, incandescent bulbs, or flames is",
            "unpolarised. The polarisation direction changes randomly on",
            "a timescale of femtoseconds — much faster than any detector",
            "can follow. Our eyes cannot distinguish polarised from",
            "unpolarised light, but polarising filters, wave plates, and",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

# week4_matrix_polarisation.py
from manim import *
from utils import *

class Week4TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 4 combines three topics that are grouped together in",
            "the TU/e course structure: matrix methods in geometric",
            "optics, superposition phenomena, and the introduction to",
            "polarisation.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The matrix optics section follows Bennett Chapter 5,",
            "Sections 5.5 and 5.5.5. We represent any paraxial optical",
            "system — any number of lenses, mirrors, and free-space",
            "propagation sections — as a single two-by-two matrix. The",
            "imaging properties of the whole system are read directly",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The superposition section follows Bennett Chapter 7,",
            "Sections 7.1 and 7.2. Standing waves arise when two",
            "identical waves travel in opposite directions; they are",
            "fundamental to laser resonators and to understanding which",
            "wavelengths a cavity supports. Beating arises when two",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The polarisation introduction follows Bennett Chapter 6,",
            "Sections 6.1 through 6.4. We describe linear, circular, and",
            "elliptical polarisation states geometrically and introduce",
            "the phase-difference parameter Delta-phi that distinguishes",
            "them. Week 5 will develop the Jones vector formalism for",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week4TitleCard_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week4TitleCard_p5.mp3", time_offset=0)
        card = make_title_card("WEEK 4", "Matrix Optics, Superposition and Polarisation", "Bennett Ch. 5, 7.1-7.2, 6.1-6.4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The combination of these three topics in one week reflects",
            "the structure of the TU/e course. The matrix optics and",
            "polarisation topics are closely related through their use of",
            "two-by-two matrix calculus: the ray transfer matrices of",
            "Section 5.5 and the Jones matrices of Section 6.5 are both",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett introduces matrix methods in Section 5.5, titled",
            "Introduction to Matrix Methods in Paraxial Geometrical",
            "Optics. The method allows images formed by any optical",
            "system to be located by tracing rays as they refract or",
            "reflect at interfaces, restricted to paraxial rays.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A ray is defined by two parameters: y, the perpendicular",
            "distance from the optical axis to the intersection of the",
            "ray with a reference plane; and theta, the angle the ray",
            "makes with the optical axis. These two numbers completely",
            "specify a paraxial ray at any point in the optical system.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Each optical element transforms the input ray vector to an",
            "output ray vector by matrix multiplication. For a system of",
            "N elements numbered 1 to N where element 1 is first",
            "encountered by the light, the total system matrix is M-N",
            "times ... times M-2 times M-1 — the first element goes on",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixOpticsIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixOpticsIntro_p4.mp3", time_offset=0)
        title = Text("Matrix Methods in Paraxial Optics  (Bennett 5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "All matrices in this paraxial ray-optics framework have a",
            "determinant of exactly one: AD minus BC equals one. This",
            "constraint follows from conservation of the optical",
            "invariant and serves as a useful check on matrix",
            "calculations. If your computed matrix violates this, you",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p1.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett derives the translation matrix in Section 5.5.1",
            "using the geometry of Figure 5.10. A ray at height y-one and",
            "angle theta-one propagates through a medium over horizontal",
            "distance d. In the paraxial approximation, tan theta is",
            "replaced by theta. The height changes to y-two equals y-one",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p2.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The refraction matrix is derived in Bennett Section 5.5.2",
            "from Snell's law at a spherical surface of radius R. The key",
            "geometry from Bennett Figure 5.11: the angle phi subtended",
            "at the centre of curvature satisfies phi approximately",
            "equals y over R in the paraxial limit. Applying paraxial",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p3.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The thin lens matrix follows by combining two refractions",
            "and letting the thickness go to zero. The result has 1 and 0",
            "on the diagonal, minus 1 over f in the lower left, and 1 in",
            "the lower right, where f is the focal length given by the",
            "lensmaker's equation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p4.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The mirror matrix is derived in Bennett Section 5.5.3. For a",
            "spherical mirror with radius R, the ray is reflected and",
            "continues propagating. The matrix has 1 and 0 in the top row",
            "and minus 2 over R in the lower left and 1 in the lower",
            "right — formally identical to the thin lens matrix with f",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixEquations_p5.mp3", time_offset=0)
        title = Text("Ray Transfer Matrices  (Bennett 5.5.1-5.5.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett gives a worked example in Example 5.5: two",
            "consecutive translations of distances T-one and T-two.",
            "Multiplying the two translation matrices gives a single",
            "matrix with 1, T-one plus T-two in the top row and 0, 1 in",
            "the bottom. The total translation is just the sum, and this",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p1.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Once the individual element matrices are known, Bennett",
            "Section 5.5.5 shows how to extract the cardinal points of",
            "the complete system from the system matrix M with elements",
            "A, B, C, D satisfying AD minus BC equals one.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p2.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The effective focal length of the system is f-effective",
            "equals minus 1 over C, from the principal-plane analysis in",
            "Bennett Section 5.5.5. If C equals zero, the focal length is",
            "infinite — the system is afocal, meaning parallel rays in",
            "give parallel rays out. This is the definition of a",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p3.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The back focal distance — from the last element to the rear",
            "focal point — is given by BFD equals D minus 1 over C. The",
            "front focal distance from the first element to the front",
            "focal point is FFD equals minus A over C. These distances",
            "are measured from the last and first physical elements",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p4.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The principal planes themselves can be located by computing",
            "their distances from the first and last elements using the",
            "matrix elements. The effective focal length measured from",
            "either principal plane is the same quantity f-effective.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SystemMatrixCardinalPoints_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SystemMatrixCardinalPoints_p5.mp3", time_offset=0)
        title = Text("System Matrix and Cardinal Points  (Bennett 5.5.5)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett emphasises in Section 5.5.5 that for any paraxial",
            "optical system, no matter how complex, all imaging",
            "properties are summarised by just three quantities: the two",
            "principal plane locations and the effective focal length.",
            "This is a powerful result — you do not need to know the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p1.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett works through the beam expander in Example 5.6. Two",
            "thin lenses with focal lengths f-one and f-two are separated",
            "by distance d equals f-one plus f-two. We compute M-system",
            "equals M-L2 times M-T times M-L1.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p2.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Write M-L1 for the first lens: top row 1, 0; bottom row",
            "minus 1 over f-one, 1. Write M-T for the free propagation of",
            "distance f-one plus f-two: top row 1, f-one plus f-two;",
            "bottom row 0, 1. Write M-L2 for the second lens: top row 1,",
            "0; bottom row minus 1 over f-two, 1.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p3.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Multiplying M-T times M-L1 first: top row 1 minus (f-one",
            "plus f-two) over f-one, f-one plus f-two; bottom row minus 1",
            "over f-one, 1. The top left becomes minus f-two over f-one.",
            "Then multiplying M-L2 times this intermediate result, the C",
            "element becomes minus 1 over f-one minus 1 over f-two plus",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p4.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The system matrix for the beam expander has C equals zero,",
            "so the effective focal length is infinite — the system is",
            "afocal. The A element equals minus f-two over f-one. An",
            "input beam with height y and zero angle (parallel to the",
            "axis) exits with height minus f-two over f-one times y and",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MatrixExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MatrixExample_p5.mp3", time_offset=0)
        title = Text("Beam Expander Matrix Example  (Bennett Example 5.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This result has important practical applications. A Galilean",
            "telescope uses a converging objective and a diverging",
            "eyepiece to produce an afocal beam expander with no image",
            "inversion. Laser beam expanders are used to reduce the",
            "divergence of laser beams for long-range propagation.",
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
            "A standing wave is the superposition of two identical",
            "harmonic waves travelling in opposite directions. Bennett",
            "Section 7.1 derives the result.",
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
            "Two waves with the same amplitude A, frequency omega, and",
            "wave number k, travelling in opposite directions: psi-one",
            "equals A sine of kx minus omega t and psi-two equals A sine",
            "of kx plus omega t. Their sum, using the sum-to-product",
            "identity, is psi equals 2A sine kx times cosine omega t.",
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
            "The spatial and temporal dependences have completely",
            "separated. The profile 2A sine kx is stationary — it does",
            "not move. The factor cosine omega t makes the entire profile",
            "oscillate in time between plus 2A sine kx and minus 2A sine",
            "kx.",
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
            "Nodes are positions where sine kx equals zero, meaning kx",
            "equals m pi for integer m, giving x equals m lambda over 2.",
            "At nodes, the wave function is zero at all times — the",
            "medium never moves at these points. The spacing between",
            "adjacent nodes is lambda over 2.",
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
            "Antinodes are positions where the absolute value of sine kx",
            "equals one, giving maximum amplitude of 2A. They occur",
            "halfway between nodes at x equals m plus one half times",
            "lambda over 2.",
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
            "Standing waves in a laser cavity are fundamental to laser",
            "physics. The cavity is bounded by two mirrors. The boundary",
            "condition requires that the electric field is zero at both",
            "mirror surfaces — or equivalently that the wave function has",
            "nodes at the mirror positions. For a cavity of length L, the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class StandingWaves_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/StandingWaves_p7.mp3", time_offset=0)
        title = Text("Standing Waves  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The frequency spacing between adjacent modes is delta-f",
            "equals c over 2L. For a laser cavity of length 30",
            "centimetres: delta-f equals 3 times ten to the 8 divided by",
            "0.6 equals 500 megahertz. The laser output is a frequency",
            "comb with modes spaced 500 megahertz apart.",
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
            "Beating occurs when two harmonic waves of slightly different",
            "angular frequencies omega-one and omega-two are",
            "superimposed. Bennett Section 7.2 derives the result using",
            "the sum-to-product trigonometric identity.",
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
            "Consider two waves of equal amplitude A: psi equals A cosine",
            "omega-one t plus A cosine omega-two t. Using the identity",
            "cosine u plus cosine v equals 2 cosine of u plus v over 2",
            "times cosine of u minus v over 2, the superposition becomes:",
            "2A cosine of omega-one plus omega-two over 2 times t, times",
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
            "The first factor, cosine of the average frequency omega-bar",
            "equals omega-one plus omega-two over 2, is the fast carrier",
            "oscillation. The second factor, cosine of half the",
            "difference frequency, is the slow envelope modulation. The",
            "envelope amplitude oscillates between 2A and minus 2A at the",
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
            "This is Bennett's result. The beat frequency equals the",
            "absolute difference of the two component frequencies.",
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
            "In acoustics: two guitar strings at 440 and 443 hertz",
            "produce 3 beats per second. Musicians use beating to tune —",
            "they listen for the beats to slow down and disappear as the",
            "second string approaches the correct pitch.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p6.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In optics: heterodyne detection uses beating between a",
            "signal beam at frequency omega-s and a strong local",
            "oscillator at frequency omega-lo. The detector produces an",
            "output at the beat frequency omega-s minus omega-lo, which",
            "can be in the radio frequency or microwave range and is",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Beating_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/Beating_p7.mp3", time_offset=0)
        title = Text("Beating  (Bennett Section 7.2)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The coherence requirement: beating is only observable if the",
            "two wave trains overlap in time. The observation time must",
            "be shorter than the coherence time of each source. For two",
            "laser beams with linewidths of 1 megahertz, the coherence",
            "time is one microsecond, and beats can be observed for path",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarizationBasics_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        # self.add_sound("narration/audio/paragraphs/PolarizationBasics_p1.mp3", time_offset=0)
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
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
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
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
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
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
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
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
        title = Text("Polarization States  (Bennett 6.1-6.4)", font_size=36, color=GOLD)
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

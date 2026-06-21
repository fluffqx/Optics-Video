# week5_jones.py — paragraph-per-scene
from manim import *
from utils import *

class Week5TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 5 develops the Jones vector formalism — the systematic",
            "mathematical framework for describing and manipulating",
            "polarisation states.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The key insight is that any polarisation state of a plane",
            "wave can be represented as a two-component complex column",
            "vector — the Jones vector. Any optical element that",
            "transforms the polarisation can be represented as a",
            "two-by-two complex matrix — the Jones matrix. To trace",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 5", "Polarisation, Birefringence and Jones Formalism", "Bennett Ch. 6")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "This formalism is exact within the paraxial approximation",
            "for fully coherent light. It handles linear polarisers, wave",
            "plates, rotators, beam splitters, and any combination of",
            "these.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p1.mp3", time_offset=0)
        title = Text("Polarisation States  (Bennett Section 6.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Jones vector for a plane wave propagating in the",
            "z-direction is a two-component vector containing the x and y",
            "complex amplitudes of the electric field. The common factor",
            "e to the i kz minus omega t is always implicit.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p2.mp3", time_offset=0)
        title = Text("Polarisation States  (Bennett Section 6.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Horizontal linear polarisation has field only in the",
            "x-direction: Jones vector one, zero. Vertical has zero, one.",
            "Linear polarisation at angle alpha from horizontal has",
            "components cosine alpha and sine alpha. The normalisation",
            "convention sets the total intensity to one: the magnitude",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p3.mp3", time_offset=0)
        title = Text("Polarisation States  (Bennett Section 6.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Circular polarisation requires equal amplitudes in x and y",
            "with a phase difference of pi over two. Right circular",
            "polarisation is one over root two times one, minus i — the y",
            "component lags the x component by pi over two. Left circular",
            "polarisation is one over root two times one, plus i.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p4.mp3", time_offset=0)
        title = Text("Polarisation States  (Bennett Section 6.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The intensity of a polarisation state is the dot product of",
            "the Jones vector with its complex conjugate — the modulus",
            "squared of each component, summed. This always gives a real,",
            "non-negative result.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p1.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Birefringent crystals have two different refractive indices",
            "for two orthogonal linear polarisations — the ordinary index",
            "n-o and the extraordinary index n-e. A wave with",
            "polarisation along the fast axis travels faster than one",
            "along the slow axis.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p2.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A slab of birefringent material with thickness d introduces",
            "a relative phase difference delta phi between the two",
            "orthogonal components. Delta phi equals 2 pi over",
            "lambda-naught times the quantity n-e minus n-o times d. This",
            "phase difference determines the polarisation transformation",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p3.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A quarter-wave plate has delta phi equals pi over two — a",
            "quarter of a full cycle. The minimum thickness is",
            "lambda-naught divided by four times the absolute value of",
            "n-e minus n-o. A quarter-wave plate converts 45-degree",
            "linear polarisation to circular, and circular to linear. It",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p4.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A half-wave plate has delta phi equals pi. It rotates the",
            "plane of linear polarisation by twice the angle between the",
            "input polarisation and the fast axis. A half-wave plate with",
            "fast axis at 22.5 degrees rotates any linear polarisation by",
            "45 degrees. A half-wave plate at 45 degrees converts",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p1.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A Jones vector is a two-component complex column vector that",
            "completely describes the polarisation state of a fully",
            "coherent plane wave. The first component is the complex",
            "amplitude of the x-component of the electric field, and the",
            "second is the complex amplitude of the y-component. Both",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p2.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Horizontal linear polarisation is represented by the Jones",
            "vector 1, 0 — field entirely in x, zero in y. Vertical is 0,",
            "1. Linear at plus 45 degrees is 1, 1 divided by root 2 —",
            "equal components in phase. Linear at minus 45 degrees is 1,",
            "minus 1 over root 2.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p3.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Right circular polarisation is 1, minus i divided by root 2",
            "— the y component lags x by 90 degrees. Left circular is 1,",
            "plus i divided by root 2. The i factor encodes the",
            "quarter-wavelength phase difference between components.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p4.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The intensity is the modulus squared of the Jones vector: I",
            "equals the absolute value of E-x squared plus the absolute",
            "value of E-y squared. For a normalised Jones vector, this",
            "equals one, and the actual intensity is separately specified",
            "by a prefactor.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p1.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Each optical element is represented by a two-by-two Jones",
            "matrix J. The output polarisation state is J times the input",
            "Jones vector. For a sequence of N elements, the output is",
            "J-N times J N-minus-1 times dot dot dot times J-1 times the",
            "input, with the first element encountered on the right.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p2.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A horizontal linear polariser passes only the x-component:",
            "its Jones matrix has 1, 0, 0, 0. A vertical polariser has 0,",
            "0, 0, 1.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p3.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A quarter-wave plate with fast axis horizontal introduces",
            "minus i to the y-component: its Jones matrix has 1, 0 in the",
            "top row and 0, minus i in the bottom. The x-component",
            "acquires no additional phase; the y-component acquires a",
            "phase of minus pi over two.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p4.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A half-wave plate with fast axis horizontal flips the sign",
            "of the y-component: 1, 0 top row and 0, minus 1 bottom row.",
            "This corresponds to a phase shift of minus pi on the",
            "y-component.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p5.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "To find the output for a specific input and sequence of",
            "elements: write down the Jones matrices, multiply from right",
            "to left (first element on right), then multiply by the input",
            "Jones vector. The result is the output Jones vector, from",
            "which you can read off the polarisation state and intensity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p6.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Example: horizontal linear polariser, then quarter-wave",
            "plate with fast axis at 45 degrees. Input: vertically",
            "polarised light, Jones vector 0, 1. After horizontal",
            "polariser: Jones vector 0, 0 — all blocked. No light reaches",
            "the quarter-wave plate. This confirms that a polariser",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p7.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Different example: plus 45-degree linear input through a",
            "quarter-wave plate with horizontal fast axis. Input: 1, 1",
            "over root 2. QWP matrix times input: 1, 0, 0, minus i times",
            "1, 1 over root 2 equals 1, minus i over root 2. This is",
            "right circular polarisation. The quarter-wave plate has",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

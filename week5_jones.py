# week5_jones.py — Week 5 (paragraph-per-scene)
from manim import *
from utils import *

class Week5TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p1.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Week 5 is all about polarisation — one of the most important",
            "properties of light, and one that's easy to miss because our",
            "eyes can't detect it directly.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p2.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Polarisation describes the direction in which the electric",
            "field oscillates as the wave propagates. For a plane wave",
            "travelling in the z direction, the electric field can point",
            "anywhere in the x-y plane.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p3.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "If the field always points in the same direction, we have",
            "linear polarisation. If the tip of the electric field vector",
            "traces a circle as time progresses, we have circular",
            "polarisation. The general case is elliptical polarisation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p4.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Birefringent crystals have two different refractive indices",
            "for two perpendicular polarisation directions — the ordinary",
            "and extraordinary axes. Light polarised along the slow axis",
            "travels more slowly than light along the fast axis. This",
            "accumulates a phase difference between the two components.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p5.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A wave plate exploits this: it introduces a controlled phase",
            "difference delta phi equal to 2 pi over lambda naught times",
            "n_e minus n_o times d, where d is the plate thickness.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p6.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A quarter-wave plate introduces a phase difference of pi over",
            "2 — a quarter of a full cycle. This converts linearly",
            "polarised light at 45 degrees into circularly polarised light,",
            "and vice versa.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p7.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A half-wave plate introduces pi — half a cycle — and rotates",
            "the plane of linear polarisation by twice the angle between",
            "the input polarisation and the fast axis.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p8.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Jones formalism handles all of this mathematically. A",
            "Jones vector is a two-component complex column vector giving",
            "the x and y components of the electric field amplitude. A",
            "Jones matrix is a two-by-two complex matrix representing an",
            "optical element.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p9.mp3", time_offset=0)
        title = Text("Polarisation, Birefringence and Jones Formalism", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "To trace polarisation through a sequence of elements, multiply",
            "the Jones matrices from right to left, then apply the result",
            "to the input Jones vector. The output intensity is the",
            "magnitude squared of the output vector.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p1.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Polarisation describes the direction in which the electric",
            "field oscillates as a wave propagates. For a wave travelling",
            "in the z-direction, E can point anywhere in the x-y plane.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p2.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Linear polarisation means E always oscillates along a fixed",
            "direction. Circular polarisation means the tip of E traces a",
            "circle — this requires equal amplitudes in x and y, with a",
            "90-degree phase difference between them. The general case is",
            "elliptical polarisation, where E traces an ellipse.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p3.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Our eyes cannot detect polarisation directly. But polarising",
            "filters, wave plates, and birefringent materials interact",
            "strongly with it, making polarisation one of the most",
            "practically exploited properties of light.",
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
            "for two perpendicular polarisation directions — the slow axis",
            "and the fast axis.",
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
            "A slab of birefringent material of thickness d introduces a",
            "phase difference delta phi between the two polarisation",
            "components, given by 2 pi over lambda naught times n_e minus",
            "n_o times d.",
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
            "A quarter-wave plate introduces a phase difference of pi over",
            "2. Linear polarisation at 45 degrees to the fast axis is",
            "converted into circular polarisation. Going back through a",
            "second quarter-wave plate converts it back. This is used in",
            "optical isolators and CD players.",
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
            "A half-wave plate introduces a phase difference of pi. It",
            "rotates the plane of linear polarisation by twice the angle",
            "between the input polarisation and the fast axis. Used in",
            "continuously variable power control of laser beams.",
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
            "The Jones vector is a 2-component complex column vector that",
            "completely describes the polarisation state of a monochromatic",
            "wave. The two components give the x and y electric field",
            "amplitudes including their relative phase.",
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
            "Horizontal linear polarisation is represented by the vector 1,",
            "0. Vertical is 0, 1. Plus 45 degrees is 1 over root 2 times 1,",
            "1. Right circular polarisation is 1 over root 2 times 1, minus",
            "i. Left circular is 1 over root 2 times 1, plus i.",
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
            "The intensity is the magnitude squared of the Jones vector —",
            "which is always real and positive.",
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
            "Each optical element is represented by a 2 by 2 Jones matrix.",
            "To find the output polarisation state, multiply the Jones",
            "matrix by the input Jones vector.",
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
            "A horizontal polariser passes only the x-component: it has 1",
            "zero zero zero. A vertical polariser has zero zero zero one.",
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
            "A quarter-wave plate with fast axis horizontal introduces a",
            "minus i phase to the y-component: the matrix is 1 zero zero",
            "minus i.",
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
            "A half-wave plate with fast axis horizontal flips the sign of",
            "the y-component: 1 zero zero minus 1.",
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
            "For a sequence of elements, multiply the Jones matrices from",
            "right to left — first element on the right — then apply the",
            "result to the input vector.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

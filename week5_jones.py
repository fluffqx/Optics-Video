# week5_jones.py — Week 5: Polarisation and Jones Formalism (paragraph-per-scene)
from manim import *
from utils import *

class Week5TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 5",
            "Polarisation, Birefringence and Jones Formalism",
            "Bennett Ch. 6")
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
        card = make_title_card("WEEK 5",
            "Polarisation, Birefringence and Jones Formalism",
            "Bennett Ch. 6")
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
        card = make_title_card("WEEK 5",
            "Polarisation, Birefringence and Jones Formalism",
            "Bennett Ch. 6")
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
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Polarisation is one of the most important properties of",
            "light, and one that our eyes cannot detect directly. Bennett",
            "opens Chapter 6 by continuing the discussion from Chapter 2,",
            "where it was shown that linearly polarised transverse",
            "electromagnetic waves are solutions to Maxwell's equations.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p2.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "An electromagnetic wave with an electric field vector that",
            "oscillates back and forth along a fixed direction is",
            "linearly polarised, as described in Bennett Section 6.2. The",
            "electric field oscillates within the plane of polarisation.",
            "The plane of polarisation for a wave travelling in the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p3.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Equation 6.3 gives the general form for a wave where",
            "the y-component has a phase shift Delta-phi relative to the",
            "x-component. The polarisation state depends on both the",
            "ratio of amplitudes E-naught-x to E-naught-y and the value",
            "of Delta-phi.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p4.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When Delta-phi equals zero or pi, the fields oscillate in",
            "phase or perfectly out of phase, giving linear polarisation.",
            "The field vector traces a straight line. When E-naught-x",
            "equals E-naught-y and Delta-phi equals plus or minus pi over",
            "2, the field vector traces a circle — circular polarisation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p5.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For all other combinations of amplitude ratio and phase",
            "difference, the field traces an ellipse — this is elliptical",
            "polarisation. Bennett Figure 6.14 shows the full range of",
            "polarisation states as Delta-phi varies from minus pi to",
            "plus pi, for both equal and unequal amplitudes. Linear and",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PolarisationStatesScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PolarisationStatesScene_p6.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Natural light from thermal sources — the sun, incandescent",
            "bulbs, flames — is unpolarised. The polarisation direction",
            "changes randomly on a timescale of about ten to the minus 8",
            "seconds, much faster than any detector. This rapid",
            "randomisation is why an unpolarised beam of irradiance",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p1.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett Section 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Section 6.3 discusses birefringence — also known as",
            "double refraction — in crystalline materials. A birefringent",
            "crystal has an ordered atomic structure that makes the index",
            "of refraction anisotropic: it depends on both the",
            "propagation direction and the polarisation direction.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p2.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett Section 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Calcite (CaCO3) is the classic example, with a hexagonal",
            "crystal structure and one optic axis. An unpolarised beam",
            "incident normally on a cleavage plane refracts into two",
            "beams: the ordinary ray, which obeys Snell's law with index",
            "n-o equals 1.6584 at 589 nanometres, and the extraordinary",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p3.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett Section 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A wave plate, also called a retarder, is a slab of",
            "birefringent material cut so that the optic axis is parallel",
            "to the face of the slab, as shown in Bennett Figure 6.10(c).",
            "A beam normally incident on such a slab resolves into two",
            "components: one polarised along the optic axis (travelling",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p4.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett Section 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The relative phase shift is derived in Bennett Equation 6.8.",
            "The n-e component travels optical distance n-e times d, and",
            "the n-o component travels n-o times d. The phase of a wave",
            "changes by k times distance, where k equals 2 pi over",
            "lambda-naught. The relative phase shift is therefore",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p5.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett Section 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A quarter-wave plate is designed so that d times the",
            "absolute value of n-e minus n-o equals lambda-naught over 4,",
            "as given in Bennett Equation 6.10. The relative phase shift",
            "is then pi over 2. The minimum thickness for quartz at 589",
            "nanometres is, from Bennett Example 6.3: d equals",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p6.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett Section 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A half-wave plate satisfies d times the absolute value of",
            "n-e minus n-o equals lambda-naught over 2, from Bennett",
            "Equation 6.11. The phase shift is pi. A half-wave plate with",
            "fast axis horizontal negates the y-component of the electric",
            "field. If the incident polarisation is at angle theta from",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BirefringenceWavePlates_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BirefringenceWavePlates_p7.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett Section 6.3-6.4)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Example 6.4 shows what happens when left-circularly",
            "polarised light passes through a quarter-wave plate with",
            "horizontal fast axis. The incident beam has Jones vector 1,",
            "i. The QWP matrix adds an additional i to the y-component:",
            "the output is 1, i times i equals 1, minus 1. This is linear",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p1.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Jones vector formalism was introduced by R. Clark Jones",
            "in 1941 as a compact and systematic way to represent and",
            "compute polarisation transformations. Bennett introduces it",
            "in Section 6.5 as a tool that makes calculations involving",
            "multiple polarisers and wave plates much easier than working",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p2.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The starting point is the electric field of a plane wave",
            "propagating in the positive z-direction, from Bennett",
            "Equation 6.1. The wave is described by E-vector equals",
            "E-naught times e to the i times kz minus omega t plus phi,",
            "where E-naught equals E-naught-x times x-hat plus E-naught-y",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p3.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        # Show the 6 fundamental Jones vectors
        hdr = Text("Fundamental Jones Vectors  (Bennett Table 6.1)", font_size=24, color=GOLD)
        hdr.next_to(title, DOWN, buff=0.3)
        rows = VGroup(
            VGroup(MathTex(r"\begin{pmatrix}1\\0\end{pmatrix}", font_size=36, color=E_COLOR),
                   Text("  Horizontal linear", font_size=22, color=WHITE)).arrange(RIGHT, buff=0.3),
            VGroup(MathTex(r"\begin{pmatrix}0\\1\end{pmatrix}", font_size=36, color=E_COLOR),
                   Text("  Vertical linear", font_size=22, color=WHITE)).arrange(RIGHT, buff=0.3),
            VGroup(MathTex(r"\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}", font_size=36, color=WAVE_COLOR),
                   Text("  Linear +45 deg", font_size=22, color=WHITE)).arrange(RIGHT, buff=0.3),
            VGroup(MathTex(r"\frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}", font_size=36, color=B_COLOR),
                   Text("  Left circular (Delta phi = +pi/2)", font_size=22, color=WHITE)).arrange(RIGHT, buff=0.3),
            VGroup(MathTex(r"\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}", font_size=36, color=B_COLOR),
                   Text("  Right circular (Delta phi = -pi/2)", font_size=22, color=WHITE)).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        safe_scale(rows, max_width=13.0, max_height=5.0)
        rows.next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(VGroup(hdr, rows), run_time=0.1))
        self.wait(1)

class JonesFormalism_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p4.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For elliptically polarised light as in Bennett Equation",
            "6.13, the y-component acquires a relative phase shift",
            "Delta-phi. The Jones vector is E-naught-x, E-naught-y times",
            "e to the i Delta-phi. The magnitude of e to the i Delta-phi",
            "is always one, so the phase shift does not change the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p5.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Jones vectors are normalised so that the sum of the",
            "modulus-squared of each component equals one. From Bennett",
            "Section 6.5: a normalised Jones vector represents one unit",
            "of irradiance. The irradiance of the wave equals epsilon",
            "times v divided by 2 times E-naught squared, from Bennett",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p6.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The six fundamental normalised Jones vectors to memorise:",
            "horizontal linear polarisation is 1, 0; vertical linear",
            "polarisation is 0, 1; linear at plus 45 degrees is 1, 1",
            "divided by root 2; linear at minus 45 degrees is 1, minus 1",
            "divided by root 2; left circular polarisation is 1, i",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p7.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The factor i equals e to the i pi over 2 in the left",
            "circular vector encodes the 90-degree phase lead of the",
            "y-component over the x-component. When you take the real",
            "part of the full wave, the y-component leads x by a quarter",
            "wavelength, causing the electric field vector to rotate",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesFormalism_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesFormalism_p8.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett shows in Section 6.5 that the unit vectors for left",
            "and right circular polarisation, e-hat-l and e-hat-r, can be",
            "used to represent any state of linear polarisation.",
            "Specifically, e-hat-h equals e-hat-l plus e-hat-r divided by",
            "root 2, and e-hat-v equals e-hat-l minus e-hat-r divided by",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p1.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "From Bennett Section 6.5.1: each optical element such as a",
            "linear polariser or wave plate is represented in the Jones",
            "notation by a two-by-two matrix M. If E-tilde-i is the",
            "incident Jones vector, the transmitted Jones vector is",
            "E-tilde-t equals M times E-tilde-i. This is Bennett Equation",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p2.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        hdr = Text("Jones Matrices — Bennett Table 6.1", font_size=24, color=GOLD)
        hdr.next_to(title, DOWN, buff=0.3)
        mats = VGroup(
            VGroup(Text("H-polariser:", font_size=20, color=WHITE),
                   MathTex(r"\begin{pmatrix}1&0\\0&0\end{pmatrix}", font_size=34, color=E_COLOR)).arrange(RIGHT, buff=0.3),
            VGroup(Text("V-polariser:", font_size=20, color=WHITE),
                   MathTex(r"\begin{pmatrix}0&0\\0&1\end{pmatrix}", font_size=34, color=E_COLOR)).arrange(RIGHT, buff=0.3),
            VGroup(Text("QWP fast-H:", font_size=20, color=WHITE),
                   MathTex(r"\begin{pmatrix}1&0\\0&i\end{pmatrix}", font_size=34, color=B_COLOR)).arrange(RIGHT, buff=0.3),
            VGroup(Text("QWP fast-V:", font_size=20, color=WHITE),
                   MathTex(r"\begin{pmatrix}1&0\\0&-i\end{pmatrix}", font_size=34, color=B_COLOR)).arrange(RIGHT, buff=0.3),
            VGroup(Text("HWP fast-H:", font_size=20, color=WHITE),
                   MathTex(r"\begin{pmatrix}1&0\\0&-1\end{pmatrix}", font_size=34, color=WAVE_COLOR)).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        safe_scale(mats, max_width=13.0, max_height=5.0)
        mats.next_to(hdr, DOWN, buff=0.25)
        self.play(FadeIn(VGroup(hdr, mats), run_time=0.1))
        self.wait(1)

class JonesMatrices_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p3.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        hdr = Text("Bennett Example 6.6(a): +45 deg linear through V-polariser", font_size=24, color=GOLD)
        hdr.next_to(title, DOWN, buff=0.3)
        calc = VGroup(
            MathTex(r"\tilde{E}_t = \begin{pmatrix}0&0\\0&1\end{pmatrix} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}0\\1\end{pmatrix}", font_size=36),
            Text("Vertical polarisation, half the incident intensity transmitted.", font_size=24, color=WAVE_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(calc, max_width=13.0)
        calc.next_to(hdr, DOWN, buff=0.35)
        b = txt_block([
            "Bennett's Table 6.1 gives the Jones matrices for all",
            "standard optical elements. The horizontal linear polariser",
            "has 1, 0 in the top row and 0, 0 in the bottom. The vertical",
            "polariser has 0, 0 top and 0, 1 bottom. The transmission",
            "axis at plus 45 degrees gives one-half times the matrix 1,",
        ])
        b.next_to(calc, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(hdr, calc, b), run_time=0.1))
        self.wait(1)

class JonesMatrices_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p4.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        hdr = Text("Bennett Example 6.6(b): +45 deg linear through QWP (fast-H)", font_size=22, color=GOLD)
        hdr.next_to(title, DOWN, buff=0.3)
        calc = VGroup(
            MathTex(r"\tilde{E}_t = \begin{pmatrix}1&0\\0&i\end{pmatrix} \cdot \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}", font_size=36),
            Text("Left circular polarisation — all intensity transmitted, no loss.", font_size=24, color=B_COLOR),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(calc, max_width=13.0)
        calc.next_to(hdr, DOWN, buff=0.35)
        b = txt_block([
            "The quarter-wave plate with fast axis horizontal has matrix",
            "1, 0, 0, i. Why i? The fast axis is horizontal, so the",
            "x-component travels faster — it accumulates less phase delay",
            "through the plate. The y-component travels more slowly along",
            "the slow axis and picks up an additional phase of pi over 2,",
        ])
        b.next_to(calc, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(hdr, calc, b), run_time=0.1))
        self.wait(1)

class JonesMatrices_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p5.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        hdr = Text("Rotation Matrix  (Bennett Example 6.5)", font_size=26, color=GOLD)
        hdr.next_to(title, DOWN, buff=0.3)
        rot = MathTex(r"R(\alpha) = \begin{pmatrix}\cos\alpha & -\sin\alpha \\ \sin\alpha & \cos\alpha\end{pmatrix}", font_size=42, color=WAVE_COLOR)
        rot.next_to(hdr, DOWN, buff=0.3)
        note = Text("Rotated Jones matrix: M' = R(alpha) M R(-alpha)  (Bennett Eq. 6.24)", font_size=22, color=WHITE)
        safe_scale(note, max_width=13.0)
        note.next_to(rot, DOWN, buff=0.25)
        b = txt_block([
            "The quarter-wave plate with fast axis vertical has matrix 1,",
            "0, 0, minus i. The x-component is now on the slow axis and",
            "picks up the extra phase. The y-component is on the fast",
            "axis and acquires no additional phase relative to x.",
        ])
        b.next_to(note, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(hdr, rot, note, b), run_time=0.1))
        self.wait(1)

class JonesMatrices_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p6.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The rotation matrix rotates a Jones vector through angle",
            "alpha: cosine alpha, minus sine alpha in the top row and",
            "sine alpha, cosine alpha in the bottom. Bennett derives this",
            "in Example 6.5 by requiring the matrix to map cosine theta,",
            "sine theta to cosine of theta plus alpha, sine of theta plus",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p7.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through Bennett's Example 6.6 in full. Light",
            "polarised at 45 degrees — Jones vector 1, 1 divided by root",
            "2 — is incident on a vertical linear polariser. The result",
            "is 0, 0; 0, 1 times 1, 1 over root 2, which equals 0, 1 over",
            "root 2. This is the normalised Jones vector for vertical",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p8.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Now the same 45-degree incident beam through a quarter-wave",
            "plate with horizontal fast axis. The matrix 1, 0, 0, i times",
            "1, 1 over root 2 equals 1, i over root 2. This is left",
            "circular polarisation. The quarter-wave plate converts",
            "45-degree linear to left circular — none of the intensity is",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p9.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Now Bennett's Example 6.7, which is the most involved:",
            "45-degree linear light through a half-wave plate with",
            "horizontal fast axis, then a quarter-wave plate with",
            "vertical fast axis, then a linear polariser at minus 45",
            "degrees. There is no half-wave plate in Table 6.1, but a",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p10.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Working from right to left: two QWPs with horizontal fast",
            "axis give the half-wave plate matrix 1, 0, 0, minus 1.",
            "Multiplying by the QWP with vertical fast axis 1, 0, 0,",
            "minus i gives the effective combination matrix 1, 0, 0, i —",
            "a QWP with horizontal fast axis. This means a half-wave",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class JonesMatrices_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/JonesMatrices_p11.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The rotation of a Jones matrix is given by M-prime equals R",
            "of alpha times M times R of minus alpha. This is Bennett",
            "Equation 6.24. Using this, you can derive the Jones matrix",
            "for a linear polariser at any angle from the horizontal or",
            "vertical matrix in the table, without memorising additional",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week5TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week5TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 5",
            "Polarisation, Birefringence and Jones Formalism",
            "Bennett Ch. 6")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "You must be able to write down the Jones vector for any",
            "standard polarisation state from memory, multiply Jones",
            "matrices in the correct order, compute the output",
            "polarisation state and intensity from a given input and",
            "sequence of elements, and verify your results by checking",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

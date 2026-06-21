# week1_waves.py
from manim import *
from utils import *

class Week1TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation and Complex Representation", "Bennett Ch. 1")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Welcome to the 31OPT Optics exam preparation series. This",
            "video covers all eight weeks of the course in full detail,",
            "working directly from Bennett's Principles of Physical",
            "Optics, Second Edition, and the TU/e lecture material. Every",
            "derivation, every worked example, and every exam technique",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation and Complex Representation", "Bennett Ch. 1")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 1 covers the mathematical foundations that all",
            "subsequent weeks build upon. The first half follows Bennett",
            "Chapter 1: the one-dimensional wave equation, its general",
            "solutions, harmonic traveling waves and all their",
            "parameters, the superposition principle, and the complex",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation and Complex Representation", "Bennett Ch. 1")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "If you can work through the problems at the end of Bennett",
            "Chapters 1 and 2 with confidence, you are well prepared for",
            "the Week 1 material in the exam. The most important skill to",
            "develop this week is facility with the harmonic wave",
            "relations: v equals f lambda, v equals omega over k, k",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation and Complex Representation", "Bennett Ch. 1")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Let's begin.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p1.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett Section 1.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett opens Chapter 1 with the statement from Heisenberg:",
            "the mental pictures of particles and waves are both",
            "incomplete and have only the validity of analogies that are",
            "accurate only in limiting cases. This captures the central",
            "theme of optics: light has both wave properties and particle",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p2.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett Section 1.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A wave is a propagating disturbance that transports energy",
            "and momentum from one location to another without",
            "transporting matter. Bennett Section 1.1 gives the example",
            "of transverse waves on a stretched string — the string",
            "elements move up and down but the wave itself propagates",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p3.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett Section 1.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For electromagnetic waves — light — there is no medium at",
            "all. The oscillating quantities are the electric and",
            "magnetic fields themselves. Maxwell showed in 1865 that",
            "these fields could sustain self-propagating oscillations in",
            "vacuum at a speed he computed to be 3.107 times ten to the 8",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p4.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett Section 1.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Before working with electromagnetic waves, we need to",
            "understand the mathematics of waves in general. The simplest",
            "case is a wave that propagates in a single direction — the",
            "x-axis. This one-dimensional description captures all the",
            "essential physics and extends naturally to three dimensions.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p5.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett Section 1.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The wave function psi of x and t is any physical quantity",
            "that depends on both position and time and propagates as a",
            "wave. It could be the transverse displacement of a string,",
            "the pressure fluctuation in a sound wave, or the electric",
            "field amplitude in a light wave. The wave equation tells us",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p6.mp3", time_offset=0)
        title = Text("What Is a Wave?  (Bennett Section 1.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Appendix A derives the wave equation for a stretched",
            "string by applying Newton's second law to a small segment.",
            "The result is the same equation that governs all classical",
            "waves: the second spatial derivative of psi equals one over",
            "v-squared times the second time derivative. This",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p1.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett Section 1.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Section 1.2 derives and analyses the one-dimensional",
            "wave equation. The equation is: partial squared psi over",
            "partial x squared equals one over v-squared times partial",
            "squared psi over partial t squared, given as Bennett",
            "Equation 1.1.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p2.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett Section 1.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The left side, partial squared psi over partial x squared,",
            "is the spatial curvature of the wave — how quickly the wave",
            "shape bends in space. A large positive value means the",
            "profile is concave upward; negative means concave downward.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p3.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett Section 1.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The right side, one over v-squared times partial squared psi",
            "over partial t squared, is the temporal acceleration of the",
            "field at a fixed location, scaled by one over v-squared.",
            "This tells us how rapidly the field value is changing in",
            "time.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p4.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett Section 1.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The equation says: curvature in space is proportional to",
            "acceleration in time. In physical terms: if a region of the",
            "wave is curved — higher than its neighbours — it will",
            "experience a restoring force or restoring mechanism that",
            "accelerates it back toward equilibrium. This acceleration",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p5.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett Section 1.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The wave equation is linear: psi appears only to the first",
            "power. There is no psi squared, no psi times partial psi",
            "over partial x. This linearity is what makes the",
            "superposition principle possible: the sum of any two",
            "solutions is also a solution. Superposition is the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p6.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett Section 1.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Section 1.3 gives the general solutions. Any",
            "function of the form f of x minus vt satisfies the wave",
            "equation, as does any function of g of x plus vt. This can",
            "be verified by substitution: computing partial squared f",
            "over partial x squared gives f-double-prime of x minus vt;",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p7.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett Section 1.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The function f of x minus vt represents a profile moving in",
            "the positive x direction at speed v. As time increases by",
            "delta-t, the argument x minus vt is unchanged if x increases",
            "by v times delta-t. So the entire profile shifts rigidly to",
            "the right at speed v, preserving its shape exactly.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p8.mp3", time_offset=0)
        title = Text("The 1D Wave Equation  (Bennett Section 1.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The remarkable thing is that f can be any",
            "twice-differentiable function — a Gaussian pulse, a square",
            "wave, a single peak — and it propagates without distortion.",
            "This shape-preserving property holds only in a",
            "non-dispersive medium where v is the same for all",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquationProof_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p1.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's verify concretely that a specific function of the form",
            "f of x minus vt satisfies the wave equation. We choose psi",
            "equals x minus vt, all squared, following Bennett's approach",
            "in Section 1.2.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquationProof_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p2.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step one: the spatial derivative. We compute partial psi",
            "over partial x equals 2 times x minus vt. Differentiating",
            "again: partial squared psi over partial x squared equals 2.",
            "This is constant — the spatial curvature is 2 everywhere.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquationProof_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p3.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step two: the temporal derivative. We compute partial psi",
            "over partial t. Using the chain rule: partial of the",
            "quantity x minus vt squared over partial t equals 2 times x",
            "minus vt times minus v equals minus 2v times x minus vt.",
            "Differentiating again: partial squared psi over partial t",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquationProof_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p4.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step three: substitute into the wave equation. The left side",
            "is 2. The right side is one over v-squared times 2v-squared",
            "equals 2. Both sides equal 2 for all x and t, so the wave",
            "equation is satisfied.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquationProof_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p5.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This works for any function of x minus vt, not just the",
            "quadratic. The chain rule always brings down the same",
            "factors regardless of the functional form. For f of x minus",
            "vt: partial f over partial x equals f-prime times 1, and",
            "partial f over partial t equals f-prime times minus v, where",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p1.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The most important special case of a travelling wave is the",
            "harmonic wave — a pure sinusoidal oscillation. Bennett",
            "Section 1.4 introduces it as the building block from which",
            "any wave can be constructed through Fourier superposition.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p2.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The harmonic wave is written psi of x and t equals A sine of",
            "kx minus omega t plus phi. Every symbol in this expression",
            "appears throughout the entire course and must be known",
            "immediately and precisely.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p3.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A is the amplitude — the maximum value of the wave function.",
            "For an electric field wave, it has units of volts per metre.",
            "The irradiance of the wave is proportional to A squared, not",
            "A: doubling the amplitude quadruples the intensity. This",
            "factor of two in the exponent is fundamental and we will use",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p4.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "k is the wave number in radians per metre. It is the spatial",
            "frequency of the wave — how many radians of phase the wave",
            "accumulates per metre. The relationship to wavelength is k",
            "equals 2 pi over lambda. Large k means short wavelength: the",
            "wave oscillates rapidly in space.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p5.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "omega is the angular frequency in radians per second. It is",
            "the temporal frequency — how many radians of phase the wave",
            "accumulates per second. The relationship to ordinary",
            "frequency f is omega equals 2 pi f. The relationship to",
            "period T is omega equals 2 pi over T.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p6.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "lambda is the wavelength in metres — the spatial distance",
            "between adjacent crests or between any two points that are",
            "one full cycle apart. It is related to wave number by lambda",
            "equals 2 pi over k.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p7.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "f is the ordinary frequency in hertz — the number of",
            "complete oscillation cycles per second. f equals one over T",
            "equals omega over 2 pi.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p8.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "T is the period in seconds — the time for one complete cycle",
            "at a fixed point in space. T equals one over f equals 2 pi",
            "over omega.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p9.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "v is the phase velocity in metres per second — the speed at",
            "which the crests of the wave propagate. From the structure",
            "of the argument kx minus omega t: holding the argument",
            "constant and differentiating gives dx over dt equals omega",
            "over k. So v equals omega over k equals f times lambda. This",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p10.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "phi is the initial phase in radians. It shifts the wave",
            "pattern left or right in time and is determined by the",
            "initial conditions.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p11.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The five key relations you must know without hesitation: v",
            "equals f lambda, v equals omega over k, k equals 2 pi over",
            "lambda, omega equals 2 pi f, and T equals one over f. These",
            "are not independent — any one follows from the others — but",
            "you need all five for rapid calculation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p12(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p12.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Now a complete example from Bennett. A visible light wave",
            "has wavelength lambda equals 500 nanometres and speed v",
            "equals c equals 2.998 times ten to the 8 metres per second.",
            "Find k, f, omega, and T.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p13(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p13.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "k equals 2 pi over lambda equals 2 pi over 500 times ten to",
            "the minus 9 equals 1.257 times ten to the 7 radians per",
            "metre.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p14(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p14.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "f equals v over lambda equals 2.998 times ten to the 8 over",
            "500 times ten to the minus 9 equals 5.996 times ten to the",
            "14 hertz, approximately 600 terahertz.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p15(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p15.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "omega equals 2 pi f equals 3.768 times ten to the 15 radians",
            "per second.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p16(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p16.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "T equals one over f equals 1.668 times ten to the minus 15",
            "seconds equals 1.668 femtoseconds.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p17(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p17.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves  (Bennett Section 1.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Write the complete wave function with amplitude A equals",
            "E-naught: psi equals E-naught sine of 1.257 times ten to the",
            "7 times x minus 3.768 times ten to the 15 times t plus phi.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p1.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through the specific case of a He-Ne laser at",
            "632.8 nanometres, one of the most common laser wavelengths",
            "used in optics laboratories worldwide.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p2.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Given: wavelength lambda equals 632.8 nanometres equals",
            "632.8 times ten to the minus 9 metres, propagating in air",
            "where v approximately equals c equals 2.998 times ten to the",
            "8 metres per second.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p3.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Wave number: k equals 2 pi over lambda equals 2 pi over",
            "632.8 times ten to the minus 9 equals 9.926 times ten to the",
            "6 radians per metre.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p4.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Frequency: f equals v over lambda equals 2.998 times ten to",
            "the 8 over 632.8 times ten to the minus 9 equals 4.738 times",
            "ten to the 14 hertz, which is 473.8 terahertz.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p5.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Angular frequency: omega equals 2 pi f equals 2 pi times",
            "4.738 times ten to the 14 equals 2.977 times ten to the 15",
            "radians per second.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p6.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Period: T equals one over f equals 1 over 4.738 times ten to",
            "the 14 equals 2.110 times ten to the minus 15 seconds, or",
            "2.11 femtoseconds.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p7.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Write the complete wave function for an electric field in",
            "the x-direction propagating in z, with amplitude E-naught:",
            "E-x equals E-naught sine of 9.926 times ten to the 6 times z",
            "minus 2.977 times ten to the 15 times t.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p8.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "To put the time scale in perspective: 2.11 femtoseconds is",
            "2.11 millionths of a nanosecond, or 2.11 billionths of a",
            "microsecond. The fastest electronic circuits operate at",
            "picosecond timescales — a thousand times slower than one",
            "optical period. This is why we cannot directly detect the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p9.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The wavelength of 632.8 nanometres is about one hundredth",
            "the diameter of a human hair (roughly 60 micrometres). The",
            "spatial oscillation period is so small that you would need",
            "to fit about 1580 wave cycles across the width of one human",
            "hair.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p10.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "If the amplitude is E-naught equals 1000 volts per metre,",
            "the irradiance from Bennett Equation 2.33 is I equals one",
            "half times epsilon-naught times c times E-naught squared",
            "equals one half times 8.854 times ten to the minus 12 times",
            "2.998 times ten to the 8 times ten to the 6 equals 1327",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p1.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett Section 1.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The superposition principle is stated in Bennett Section",
            "1.5: if psi-one and psi-two are both solutions of the wave",
            "equation, then the sum psi-one plus psi-two is also a",
            "solution.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p2.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett Section 1.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The proof is direct and follows from linearity. Substitute",
            "psi-one plus psi-two into the wave equation. The second",
            "partial derivative of a sum is the sum of the second partial",
            "derivatives — this is basic calculus. So partial squared of",
            "psi-one plus psi-two over partial x squared equals partial",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p3.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett Section 1.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This extends to any linear combination: a times psi-one plus",
            "b times psi-two is also a solution, for any constants a and",
            "b. And to sums of any number of solutions. And to integrals",
            "of solutions weighted by any function — which is the Fourier",
            "integral.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p4.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett Section 1.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Section 1.5.2 discusses linear independence. Two",
            "waves are linearly independent if neither can be written as",
            "a scalar multiple of the other. Any arbitrary wave in a",
            "linear medium can be written as a superposition of the",
            "normal modes of that medium. For a uniform one-dimensional",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p5.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett Section 1.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The physical consequences are profound. Two laser beams",
            "cross in space without interaction — each continues exactly",
            "as if the other were not there. At every point where they",
            "overlap, the total field is the vector sum of the two",
            "individual fields. Neither beam is scattered, absorbed, or",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p6.mp3", time_offset=0)
        title = Text("Superposition Principle  (Bennett Section 1.5)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Superposition fails in nonlinear media at high intensities.",
            "A Nd:YAG laser focused into a crystal of potassium titanyl",
            "phosphate converts some of its 1064 nanometre infrared",
            "photons to 532 nanometre green photons through",
            "second-harmonic generation — this requires the nonlinear",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p1.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett Section 7.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Section 7.6 analyses wave packets and introduces",
            "group velocity. A wave packet is a localised disturbance",
            "formed by superimposing many harmonic waves with a range of",
            "frequencies centred around a central frequency omega-naught.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p2.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett Section 7.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The phase velocity is the speed of a single-frequency",
            "component: v-p equals omega over k. For light in vacuum,",
            "omega equals ck and v-p equals c for all frequencies. There",
            "is no dispersion.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p3.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett Section 7.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a wave packet containing frequencies around",
            "omega-naught, the envelope of the packet moves at a",
            "different velocity called the group velocity. Bennett",
            "derives this in Section 7.6 by expanding omega as a function",
            "of k around k-naught using a Taylor series: omega of k",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p4.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett Section 7.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In vacuum, omega equals ck so d omega d k equals c. Phase",
            "and group velocities are both c. There is no dispersion.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p5.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett Section 7.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In a dispersive medium with refractive index n of omega, the",
            "dispersion relation is omega equals c k over n of omega.",
            "Differentiating: v-g equals d omega d k equals c over n plus",
            "omega times d n d omega. The term omega times d n d omega is",
            "the dispersion correction.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p6.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett Section 7.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For normal dispersion where n increases with omega — which",
            "is the case for most optical glasses in the visible spectrum",
            "— d n d omega is positive, so v-g is less than c over n,",
            "which is already less than c. Energy travels more slowly",
            "than the phase crests.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p7.mp3", time_offset=0)
        title = Text("Phase and Group Velocity  (Bennett Section 7.6)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett gives a specific example in Section 7.6: a",
            "dispersion relation omega equals a k squared, representing a",
            "dispersive medium. The phase velocity is v-p equals omega",
            "over k equals ak. The group velocity is v-g equals d omega d",
            "k equals 2ak equals 2 v-p. The energy envelope travels at",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p1.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett introduces complex notation in Section 1.6 and",
            "explains exactly why it is so much more convenient than real",
            "notation for wave calculations.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p2.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Euler's formula is e to the i theta equals cosine theta plus",
            "i times sine theta. Bennett derives this in Section 1.6.1",
            "from the Taylor series for the exponential function: e to",
            "the ix equals the sum from n of ix to the n over n",
            "factorial. Grouping even and odd powers and recognising the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p3.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "From Euler's formula: cosine theta equals the real part of e",
            "to the i theta, and sine theta equals the imaginary part. So",
            "any real harmonic wave can be written as the real part of a",
            "complex exponential: A cosine kx minus omega t equals the",
            "real part of A e to the i kx minus omega t.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p4.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Section 1.6.2 defines the complex representation.",
            "The complex wave is psi-tilde equals A e to the i kx minus",
            "omega t, and the physical wave is the real part. The tilde",
            "denotes the complex representation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p5.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Multiplying two complex exponentials adds their exponents: e",
            "to the ia times e to the ib equals e to the i a plus b. This",
            "makes addition and multiplication of waves trivial. To add",
            "two waves, just add their complex amplitudes. The real and",
            "imaginary parts of the sum give the combined cosine and sine",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p6.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The intensity from Bennett Section 2.3.3: I is proportional",
            "to the modulus squared of the complex field, which equals",
            "psi-tilde times psi-tilde-star equals the magnitude of A",
            "squared. For a pure harmonic wave this is just A squared — a",
            "constant, as expected. The complex conjugate removes the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p7.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For the sum of two waves: the intensity of psi-one-tilde",
            "plus psi-two-tilde equals the modulus squared of the sum,",
            "which expands to give modulus-squared psi-one plus",
            "modulus-squared psi-two plus 2 times the real part of",
            "psi-one-tilde times psi-two-tilde-star. That last cross term",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p8.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A three-dimensional plane wave propagating in the direction",
            "of wave vector k-vector is psi-tilde of r-vector and t",
            "equals A e to the i k-vector dot r-vector minus omega t. The",
            "dot product k-vector dot r-vector selects the component of",
            "position along the propagation direction. Surfaces of",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p9.mp3", time_offset=0)
        title = Text("Complex Representation  (Bennett Section 1.6)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A spherical wave from a point source at the origin has the",
            "form A over r times e to the i kr minus omega t. The",
            "amplitude decreases as one over r, so the intensity falls as",
            "one over r-squared. This is the inverse-square law, and it",
            "follows directly from energy conservation: the total power",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThreeDWaves_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p1.mp3", time_offset=0)
        title = Text("3D Waves  (Bennett Section 1.7)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Section 1.7 generalises the wave equation to three",
            "spatial dimensions. The three-dimensional wave equation is",
            "del-squared psi equals one over v-squared times partial",
            "squared psi over partial t squared, where del-squared is the",
            "Laplacian operator. The equation has the same structure as",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThreeDWaves_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p2.mp3", time_offset=0)
        title = Text("3D Waves  (Bennett Section 1.7)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A three-dimensional plane wave propagating in the direction",
            "of the wave vector k-vector is given by Bennett Equation",
            "1.43: psi-tilde of r-vector and t equals A e to the i times",
            "k-vector dot r-vector minus omega t. The dot product",
            "k-vector dot r-vector selects the component of position",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThreeDWaves_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p3.mp3", time_offset=0)
        title = Text("3D Waves  (Bennett Section 1.7)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A spherical wave from a point source at the origin has the",
            "form A over r times e to the i times kr minus omega t, where",
            "r is the distance from the source. The amplitude decreases",
            "as one over r. Since irradiance is proportional to amplitude",
            "squared, the irradiance falls as one over r-squared — the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThreeDWaves_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p4.mp3", time_offset=0)
        title = Text("3D Waves  (Bennett Section 1.7)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The wave vector k-vector for a three-dimensional plane wave",
            "has components k-x, k-y, k-z and magnitude k equals omega",
            "over v. The direction of k-vector is the propagation",
            "direction. Writing k-vector equals k-x x-hat plus k-y y-hat",
            "plus k-z z-hat, the phase at position r-vector equals x",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p1.mp3", time_offset=0)
        title = Text("Week 1a Summary: Key Wave Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Here is a concise summary of all the key results from the",
            "first half of Week 1.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p2.mp3", time_offset=0)
        title = Text("Week 1a Summary: Key Wave Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The one-dimensional wave equation from Bennett Section 1.2:",
            "partial squared psi over partial x squared equals one over",
            "v-squared times partial squared psi over partial t squared.",
            "General solutions have the form f of x minus vt moving right",
            "or g of x plus vt moving left, for any twice-differentiable",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p3.mp3", time_offset=0)
        title = Text("Week 1a Summary: Key Wave Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The harmonic wave from Bennett Section 1.4: psi of x and t",
            "equals A sine of kx minus omega t plus phi. Five key",
            "relations: v equals f lambda, v equals omega over k, k",
            "equals 2 pi over lambda, omega equals 2 pi f, T equals one",
            "over f. Know these without hesitation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p4.mp3", time_offset=0)
        title = Text("Week 1a Summary: Key Wave Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The superposition principle from Bennett Section 1.5: any",
            "linear combination of solutions is a solution, because the",
            "wave equation is linear. This is the foundation of all",
            "interference and diffraction phenomena.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p5.mp3", time_offset=0)
        title = Text("Week 1a Summary: Key Wave Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The complex representation from Bennett Section 1.6: the",
            "complex wave psi-tilde equals A e to the i kx minus omega t.",
            "Physical wave equals the real part. Intensity proportional",
            "to the modulus squared equals A squared. The cross term in",
            "modulus squared of a sum gives the interference term.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p6.mp3", time_offset=0)
        title = Text("Week 1a Summary: Key Wave Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Phase velocity v-p equals omega over k: the speed of wave",
            "crests. Group velocity v-g equals d omega d k: the speed of",
            "energy and information. Equal in vacuum; differ in",
            "dispersive media.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p7.mp3", time_offset=0)
        title = Text("Week 1a Summary: Key Wave Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The three-dimensional plane wave from Bennett Section 1.7:",
            "psi-tilde equals A e to the i k-vector dot r-vector minus",
            "omega t. Spherical wave: amplitude proportional to one over",
            "r, giving inverse-square law for intensity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

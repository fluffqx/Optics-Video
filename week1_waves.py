# week1_waves.py — Week 1 Waves (paragraph-per-scene, clean visuals)
from manim import *
from utils import *

class Week1TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 1",
            "Waves, Wave Equation and Complex Representation",
            "Bennett Ch. 1 and 2.1-2.3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Welcome to the 31OPT Optics exam preparation series for TU",
            "Eindhoven Applied Physics. This is a complete course",
            "covering all eight weeks, from the wave equation through to",
            "the Fabry-Pérot interferometer.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 1",
            "Waves, Wave Equation and Complex Representation",
            "Bennett Ch. 1 and 2.1-2.3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 1 lays the mathematical foundation that every other",
            "week builds on. We cover two main topics: the physics of",
            "waves in the first half, and Maxwell's equations and",
            "electromagnetic waves in the second half.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 1",
            "Waves, Wave Equation and Complex Representation",
            "Bennett Ch. 1 and 2.1-2.3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "By the end of Week 1, you will be able to write down the",
            "wave equation and explain what each term means physically.",
            "You will know the harmonic wave relations by heart. You will",
            "be comfortable with complex representation of waves. And you",
            "will understand where the speed of light comes from — not as",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 1",
            "Waves, Wave Equation and Complex Representation",
            "Bennett Ch. 1 and 2.1-2.3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Let's begin with the most fundamental question: what exactly",
            "is a wave?",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p1.mp3", time_offset=0)
        title = Text("What Is a Wave?", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "So what exactly is a wave? This is not a trivial question.",
            "The answer shapes everything that follows in this course.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p2.mp3", time_offset=0)
        title = Text("What Is a Wave?", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A wave is a disturbance that propagates through space and",
            "time, transporting energy and momentum from one location to",
            "another — without transporting matter itself. Think about a",
            "wave on the ocean. The water molecules move up and down, but",
            "they do not travel with the wave. The disturbance — the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p3.mp3", time_offset=0)
        title = Text("What Is a Wave?", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The same principle applies to sound waves in air. The air",
            "molecules oscillate back and forth around their equilibrium",
            "positions. They do not travel from your mouth to someone",
            "else's ear. Instead, regions of compression and rarefaction",
            "propagate through the air, carrying the sound energy. The",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p4.mp3", time_offset=0)
        title = Text("What Is a Wave?", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Now, electromagnetic waves — light — are fundamentally",
            "different from mechanical waves in one crucial way. They do",
            "not require a medium at all. Light propagates through the",
            "vacuum of space. The oscillating quantities are not the",
            "positions of matter but the electric and magnetic fields",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p5.mp3", time_offset=0)
        title = Text("What Is a Wave?", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For now, we need to build up the mathematical description of",
            "a wave. We start with the simplest possible case: a wave",
            "moving in one spatial dimension, along the x-axis.",
            "Everything we learn in one dimension extends naturally to",
            "three dimensions, and the essential physics is all already",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveIntroduction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveIntroduction_p6.mp3", time_offset=0)
        title = Text("What Is a Wave?", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The fundamental object is the wave function psi of x and t.",
            "This is some physical quantity — displacement, pressure,",
            "electric field strength — that depends on both position and",
            "time. The wave equation is the differential equation that",
            "tells us exactly how psi can vary. It is the most important",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p1.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\frac{\partial^2\Psi}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2}", font_size=52)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.5)
        box = SurroundingRectangle(eq, color=GOLD, buff=0.18, stroke_width=2)
        b = txt_block([
            "Here is the one-dimensional wave equation. It relates the",
            "second derivative of psi with respect to position x, to the",
            "second derivative of psi with respect to time t.",
        ])
        b.next_to(eq, DOWN, buff=0.45)
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(box))
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p2.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        lhs = MathTex(r"\partial^2\Psi/\partial x^2", font_size=60, color=E_COLOR)
        lhs.next_to(title, DOWN, buff=0.5)
        lbl = Text("SPATIAL CURVATURE", font_size=32, color=E_COLOR, weight=BOLD)
        lbl.next_to(lhs, DOWN, buff=0.25)
        b = txt_block([
            "On the left side, we have the second partial derivative of",
            "psi with respect to x. This is the spatial curvature of the",
            "wave profile — how rapidly the shape bends in space. A large",
            "positive value means the profile is concave upward; a large",
            "negative value means it curves downward.",
        ])
        b.next_to(lbl, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(lhs, lbl, b), run_time=0.1))
        self.wait(1)

class WaveEquation1D_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p3.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        rhs = MathTex(r"rac{1}{v^2}rac{\partial^2\Psi}{\partial t^2}", font_size=60, color=B_COLOR)
        rhs.next_to(title, DOWN, buff=0.5)
        lbl = Text("TEMPORAL ACCELERATION / v squared", font_size=28, color=B_COLOR, weight=BOLD)
        safe_scale(lbl, max_width=13.0)
        lbl.next_to(rhs, DOWN, buff=0.25)
        b = txt_block([
            "On the right side, we have one over v-squared, times the",
            "second partial derivative of psi with respect to t. This is",
            "the temporal acceleration of the field — how rapidly the",
            "value at a fixed point in space is changing in time. The",
            "factor one over v-squared scales this acceleration.",
        ])
        b.next_to(lbl, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(rhs, lbl, b), run_time=0.1))
        self.wait(1)

class WaveEquation1D_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p4.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The wave equation is saying: the spatial curvature at any",
            "point equals the temporal acceleration at that point,",
            "divided by v-squared. Intuitively, a region that is curved",
            "in space will also be accelerating in time — and the rate at",
            "which this happens determines how fast the disturbance",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p5.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The critical observation is that the wave equation is",
            "linear. Psi appears only to the first power, and there are",
            "no products of psi with its derivatives. This linearity is",
            "what makes the superposition principle possible — and",
            "superposition is the foundation of all interference and",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p6.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The general solution to the wave equation is any function of",
            "the form f of x minus vt, or g of x plus vt. The first",
            "represents a profile moving in the positive x direction at",
            "speed v. The second moves in the negative x direction. Any",
            "combination of these is also a solution.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p7.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The remarkable thing is that the shape of f or g can be",
            "completely arbitrary — a Gaussian pulse, a square wave, a",
            "single crest, anything at all. Whatever shape the wave has",
            "at time zero, it will retain exactly that shape as it",
            "propagates. This shape-preserving property follows directly",
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
            "Let's verify with a concrete example that f of x minus vt",
            "satisfies the wave equation. We choose the simplest",
            "non-trivial case: psi equals the quantity x minus vt, all",
            "squared.",
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
            "We compute the left side first. The first spatial derivative",
            "is 2 times open bracket x minus vt close bracket.",
            "Differentiating again with respect to x gives 2. So the left",
            "side of the wave equation is simply 2.",
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
            "Now the right side. The first time derivative of psi is",
            "minus 2v times open bracket x minus vt close bracket,",
            "because the chain rule brings down a factor of minus v.",
            "Differentiating again with respect to t gives 2v-squared.",
            "Multiplying by one over v-squared gives 2. Both sides equal",
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
            "This confirms that any function of the form f of x minus vt",
            "is a valid travelling wave solution. The specific example we",
            "chose, x minus vt squared, is a parabolic profile that moves",
            "rigidly to the right at speed v without changing shape. The",
            "same argument works for any twice-differentiable function of",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p1.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The most important special case of a travelling wave is the",
            "harmonic wave — a pure sinusoidal oscillation. This is the",
            "wave produced by a laser, by a single tuning fork, by any",
            "source that oscillates at a single well-defined frequency.",
            "It is the building block of all wave phenomena: by Fourier's",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p2.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\Psi(x,t) = A\sin(kx - \omega t + \phi)", font_size=52, color=E_COLOR)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.5)
        box = SurroundingRectangle(eq, color=GOLD, buff=0.18, stroke_width=2)
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(box))
        self.wait(1)

class HarmonicWave_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p3.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's go through every symbol carefully, because these",
            "appear throughout this entire course and you need to know",
            "them instantly.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p4.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"A", font_size=54, color=INTENSITY_COLOR)
        safe_scale(sym, max_width=9.0)
        sym.next_to(title, DOWN, buff=0.4)
        nm = Text("AMPLITUDE  —  max value of the wave [V/m for E-field]", font_size=26, color=INTENSITY_COLOR)
        safe_scale(nm, max_width=13.0)
        nm.next_to(sym, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "A is the amplitude — the maximum value of the wave function.",
            "For an electric field wave, it has units of volts per metre.",
            "For a pressure wave, it would be in pascals. The amplitude",
            "determines the intensity: irradiance is proportional to A",
            "squared, not A. This factor of two in the exponent is",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(sym, nm, sep, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p5.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"k = \frac{2\pi}{\lambda}", font_size=54, color=WAVE_COLOR)
        safe_scale(sym, max_width=9.0)
        sym.next_to(title, DOWN, buff=0.4)
        nm = Text("WAVE NUMBER  —  spatial frequency  [rad/m]", font_size=26, color=WAVE_COLOR)
        safe_scale(nm, max_width=13.0)
        nm.next_to(sym, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "k is the wave number, in units of radians per metre. It",
            "measures the spatial frequency — how many complete",
            "oscillation cycles fit into one metre. The relationship",
            "between k and the wavelength lambda is k equals 2 pi divided",
            "by lambda. Large k means short wavelength, meaning the wave",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(sym, nm, sep, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p6.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"\omega = 2\pi f = 2\pi/T", font_size=54, color=WAVE_COLOR)
        safe_scale(sym, max_width=9.0)
        sym.next_to(title, DOWN, buff=0.4)
        nm = Text("ANGULAR FREQUENCY  —  [rad/s]", font_size=26, color=WAVE_COLOR)
        safe_scale(nm, max_width=13.0)
        nm.next_to(sym, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "Omega is the angular frequency, in radians per second. It",
            "measures the temporal frequency — how many radians of phase",
            "the wave completes each second. The relationship to ordinary",
            "frequency f in hertz is omega equals 2 pi f. The",
            "relationship to period T is omega equals 2 pi divided by T.",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(sym, nm, sep, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p7.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"\lambda", font_size=54, color=WAVE_COLOR)
        safe_scale(sym, max_width=9.0)
        sym.next_to(title, DOWN, buff=0.4)
        nm = Text("WAVELENGTH  —  distance between crests [m]", font_size=26, color=WAVE_COLOR)
        safe_scale(nm, max_width=13.0)
        nm.next_to(sym, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "Lambda is the wavelength in metres — the spatial distance",
            "between two consecutive crests, or two consecutive troughs,",
            "or any two points that are one full cycle apart.",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(sym, nm, sep, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p8.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"f = 1/T", font_size=54, color=WAVE_COLOR)
        safe_scale(sym, max_width=9.0)
        sym.next_to(title, DOWN, buff=0.4)
        nm = Text("FREQUENCY  —  cycles per second [Hz]", font_size=26, color=WAVE_COLOR)
        safe_scale(nm, max_width=13.0)
        nm.next_to(sym, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "f is the ordinary frequency in hertz — the number of",
            "complete cycles per second. It is the inverse of the period:",
            "f equals one over T.",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(sym, nm, sep, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p9.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"v = \omega/k = f\lambda", font_size=54, color=WAVE_COLOR)
        safe_scale(sym, max_width=9.0)
        sym.next_to(title, DOWN, buff=0.4)
        nm = Text("PHASE SPEED  —  speed of crests [m/s]", font_size=26, color=WAVE_COLOR)
        safe_scale(nm, max_width=13.0)
        nm.next_to(sym, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "v is the phase velocity — the speed at which the wave crests",
            "move through space. It is given by omega divided by k, or",
            "equivalently by f times lambda. This is the key relation",
            "connecting spatial and temporal oscillation rates. For light",
            "in vacuum, v equals c, the speed of light.",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(sym, nm, sep, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p10.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"\phi", font_size=54, color=WHITE)
        safe_scale(sym, max_width=9.0)
        sym.next_to(title, DOWN, buff=0.4)
        nm = Text("INITIAL PHASE  —  sets position of wave at t=0 [rad]", font_size=26, color=WHITE)
        safe_scale(nm, max_width=13.0)
        nm.next_to(sym, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "phi is the initial phase — a constant in radians that shifts",
            "the wave pattern left or right in time. It is determined by",
            "initial conditions and tells you the phase of the wave at x",
            "equals zero and t equals zero.",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(sym, nm, sep, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p11.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        hdr = Text("KEY RELATIONS — memorise all five", font_size=28, color=GOLD)
        hdr.next_to(title, DOWN, buff=0.35)
        rels = VGroup(
            MathTex(r"v = f\lambda = \omega/k", font_size=38, color=WAVE_COLOR),
            MathTex(r"k = 2\pi/\lambda", font_size=38, color=WAVE_COLOR),
            MathTex(r"\omega = 2\pi f", font_size=38, color=WAVE_COLOR),
            MathTex(r"T = 1/f = 2\pi/\omega", font_size=38, color=WAVE_COLOR),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        safe_scale(rels, max_width=12.0, max_height=3.8)
        rels.next_to(hdr, DOWN, buff=0.3)
        b = txt_block([
            "All these symbols are connected by a web of relations that",
            "you must be able to derive in your sleep. The most important",
            "ones: v equals f lambda, v equals omega over k, k equals 2",
            "pi over lambda, omega equals 2 pi f, and T equals one over",
            "f.",
        ])
        b.next_to(rels, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(hdr, rels, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p12(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p12.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's do a complete worked example. A green laser pointer",
            "emits light at a wavelength of 532 nanometres in air. The",
            "speed of light in air is essentially c equals 2.998 times",
            "ten to the eighth metres per second. Find k, f, omega, and",
            "T.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p13(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p13.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "k equals 2 pi divided by 532 times ten to the minus nine,",
            "giving 1.181 times ten to the seventh radians per metre. f",
            "equals c divided by lambda, which is 2.998 times ten to the",
            "eighth divided by 532 times ten to the minus nine, giving",
            "5.64 times ten to the fourteenth hertz — that is 564",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p14(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p14.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Omega equals 2 pi times f, giving 3.54 times ten to the",
            "fifteenth radians per second. The period T equals one",
            "divided by f, giving 1.77 times ten to the minus fifteen",
            "seconds — one point seven seven femtoseconds. To put this in",
            "perspective, this is shorter than the fastest electronic",
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
        given = txt_block([
            "Given: lambda = 632.8 nm,  v = c = 2.998 x 10^8 m/s",
            "Find: k, f, omega, T",
        ], 30)
        given.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(given, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p2.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        steps = VGroup(
            labeled_eq(r"k=2\pi/(632.8\times10^{-9})=9.926\times10^6\,\text{rad/m}", "wave number", WAVE_COLOR, 32, 22),
            labeled_eq(r"f=c/\lambda=4.738\times10^{14}\,\text{Hz}", "frequency (473.8 THz)", WAVE_COLOR, 32, 22),
            labeled_eq(r"\omega=2\pi f=2.977\times10^{15}\,\text{rad/s}", "angular frequency", WAVE_COLOR, 32, 22),
            labeled_eq(r"T=1/f=2.11\times10^{-15}\,\text{s}=2.11\,\text{fs}", "period (femtoseconds!)", GOLD, 32, 22),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        safe_scale(steps, max_width=13.0, max_height=5.0)
        steps.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(steps, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p3.mp3", time_offset=0)
        title = Text("Worked Example: He-Ne Laser at 632.8 nm", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Wave number: k equals 2 pi divided by 632.8 times ten to the",
            "minus nine, giving 9.926 times ten to the sixth radians per",
            "metre.",
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
            "Frequency: f equals c divided by lambda equals 4.738 times",
            "ten to the fourteenth hertz, which is 473.8 terahertz.",
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
            "Angular frequency: omega equals 2 pi times f equals 2.977",
            "times ten to the fifteenth radians per second.",
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
            "Period: T equals one over f equals 2.110 times ten to the",
            "minus fifteen seconds, or 2.11 femtoseconds.",
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
            "Write the full wave function for an electric field pointing",
            "in the x-direction with amplitude E naught equals 1000 volts",
            "per metre, propagating in the z-direction: E equals 1000",
            "times sine of the quantity 9.926 times ten to the sixth",
            "times z, minus 2.977 times ten to the fifteenth times t, in",
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
            "This specific combination of numbers represents a real,",
            "physical laser beam that you can buy for a few euros. The",
            "wave oscillates 474 trillion times every second, yet the",
            "waveform maintains perfect sinusoidal shape and propagates",
            "without distortion at the speed of light.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p1.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The superposition principle is the mathematical foundation",
            "of all interference and diffraction phenomena. It follows",
            "directly from the linearity of the wave equation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p2.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        proof = MathTex(
            r"\frac{\partial^2(\Psi_1+\Psi_2)}{\partial x^2}"
            r"=\frac{\partial^2\Psi_1}{\partial x^2}+\frac{\partial^2\Psi_2}{\partial x^2}"
            r"=\frac{1}{v^2}\frac{\partial^2(\Psi_1+\Psi_2)}{\partial t^2}\;\checkmark",
            font_size=30)
        safe_scale(proof, max_width=13.0)
        proof.next_to(title, DOWN, buff=0.45)
        b = txt_block([
            "A linear equation is one where the unknown function and all",
            "its derivatives appear only to the first power — no squares,",
            "no products, no functions like sine of psi. The wave",
            "equation is linear because psi appears at most to the first",
            "power everywhere. There is no psi squared term, no psi times",
        ])
        b.next_to(proof, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(proof, b), run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p3.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Because of this linearity, if psi-one satisfies the wave",
            "equation and psi-two also satisfies it, then any linear",
            "combination a times psi-one plus b times psi-two — where a",
            "and b are arbitrary constants — also satisfies the wave",
            "equation. The proof is one line: substitute the linear",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p4.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This means two laser beams can cross in space and pass",
            "through each other completely unaffected. At every point",
            "where they overlap, the total electric field is simply the",
            "vector sum of the two individual fields. Neither beam is",
            "absorbed, scattered, or modified by the other. They interact",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p5.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The consequences are profound. When two waves with slightly",
            "different frequencies overlap, they produce beats. When two",
            "waves from slits in a screen overlap, they produce the",
            "interference fringes of Young's experiment. When a wavefront",
            "passes through an aperture and the secondary wavelets",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p6.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Superposition breaks down in nonlinear media — crystals used",
            "for frequency doubling in green laser pointers, for example,",
            "or the interior of a laser medium at high intensities.",
            "Nonlinear optics is a rich research field precisely because",
            "the physics is much richer when superposition fails. But for",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p1.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "There are two different speeds associated with any wave, and",
            "confusing them is one of the most common conceptual errors",
            "in wave physics. Understanding the distinction is essential",
            "for optics and for exam questions on dispersion.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p2.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        vp = MathTex(r"v_p = \omega/k", font_size=60, color=WAVE_COLOR)
        vp.next_to(title, DOWN, buff=0.45)
        lbl = Text("PHASE VELOCITY  —  speed of wave crests  [m/s]", font_size=26, color=WAVE_COLOR)
        safe_scale(lbl, max_width=13.0)
        lbl.next_to(vp, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(lbl, DOWN, buff=0.2)
        b = txt_block([
            "The phase velocity is the speed at which the crests of a",
            "single frequency component move through space. It is defined",
            "as omega divided by k. For a pure sinusoidal wave in a",
            "non-dispersive medium like vacuum, all frequencies have the",
            "same phase velocity, and a wave packet moves without",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(vp, lbl, sep, b), run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p3.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        vg = MathTex(r"v_g = d\omega/dk", font_size=60, color=B_COLOR)
        vg.next_to(title, DOWN, buff=0.45)
        lbl = Text("GROUP VELOCITY  —  speed of energy and information  [m/s]", font_size=24, color=B_COLOR)
        safe_scale(lbl, max_width=13.0)
        lbl.next_to(vg, DOWN, buff=0.2)
        sep = Line(LEFT*6, RIGHT*6, stroke_width=1, color=GRAY).next_to(lbl, DOWN, buff=0.2)
        b = txt_block([
            "The group velocity is fundamentally different. It is the",
            "speed at which the envelope of a wave packet moves — the",
            "speed of the overall amplitude modulation. It is defined as",
            "the derivative d omega d k, evaluated at the central",
            "frequency of the packet. The group velocity is also the",
        ])
        b.next_to(sep, DOWN, buff=0.2)
        self.play(FadeIn(VGroup(vg, lbl, sep, b), run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p4.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In vacuum, omega equals ck, so d omega d k equals c for all",
            "frequencies. Phase velocity and group velocity are both c.",
            "There is no dispersion — all frequencies travel at the same",
            "speed, and a pulse propagates without changing shape.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p5.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In a dispersive medium like glass, omega is not a linear",
            "function of k. Different frequencies have different phase",
            "velocities, and the group velocity differs from the phase",
            "velocity. This is why a prism separates white light: red and",
            "violet have different phase velocities in glass, so they",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p6.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The group velocity in a dispersive medium is c divided by",
            "the quantity n plus omega times dn d omega. The term omega",
            "dn d omega is the correction for dispersion. When dn d omega",
            "is positive — meaning n increases with frequency, which is",
            "called normal dispersion — the group velocity is less than c",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p7.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Consider a concrete example: suppose the dispersion relation",
            "is omega equals a k squared, where a is a constant. The",
            "phase velocity is omega over k, which equals ak — it depends",
            "on k, so this is a dispersive medium. The group velocity is",
            "d omega d k, which equals 2ak — twice the phase velocity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p8.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In anomalous dispersion, near an absorption resonance, dn d",
            "omega can be negative and the group velocity can apparently",
            "exceed c. This does not violate relativity because the group",
            "velocity is not the signal velocity in these regimes — the",
            "pulse shape distorts dramatically and information cannot",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p1.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Working directly with sines and cosines becomes extremely",
            "cumbersome as soon as you start adding multiple waves or",
            "computing intensities. The complex representation replaces",
            "these trigonometric functions with exponentials, making the",
            "algebra vastly simpler. This is not a mathematical trick —",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p2.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        euler = MathTex(r"e^{i\theta} = \cos\theta + i\sin\theta", font_size=64, color=GOLD)
        safe_scale(euler)
        euler.next_to(title, DOWN, buff=0.45)
        box = SurroundingRectangle(euler, color=GOLD, buff=0.2, stroke_width=2)
        b = txt_block([
            "The foundation is Euler's formula: e to the power i theta",
            "equals cosine theta plus i times sine theta. This identity",
            "connects the exponential function to the trigonometric",
            "functions through the imaginary unit i. It can be proved",
            "from the Taylor series: expand e to the ix, group the real",
        ])
        b.next_to(euler, DOWN, buff=0.4)
        self.play(FadeIn(euler, run_time=0.1))
        self.play(Create(box))
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p3.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "From Euler's formula, cosine theta is the real part of e to",
            "the i theta, and sine theta is the imaginary part. This",
            "means we can write a wave psi equals A cosine of kx minus",
            "omega t as the real part of A times e to the i times kx",
            "minus omega t. We define the complex wave psi-tilde as A",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p4.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Why is this better? Because multiplication of complex",
            "exponentials is trivial: e to the ia times e to the ib just",
            "equals e to the i times a plus b. Adding complex numbers is",
            "just adding their real and imaginary parts separately —",
            "there are no product-to-sum identities needed, no half-angle",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p5.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The intensity is proportional to the modulus squared: I is",
            "proportional to the absolute value of psi-tilde squared,",
            "which equals psi-tilde times its complex conjugate",
            "psi-tilde-star. For our plane wave, this gives A squared — a",
            "constant, as expected for a pure sinusoidal wave. The phase",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p6.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is also why interference is so interesting: when two",
            "waves add, the intensity of the sum is not simply the sum of",
            "the intensities. The cross terms produce the interference",
            "pattern. In complex notation: the intensity of psi-one plus",
            "psi-two equals the modulus squared of psi-one-tilde plus",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p7.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Extending to three dimensions, a plane wave propagating in",
            "the direction of the wave vector k-vector is written as A",
            "times e to the i times k-vector dot r-vector minus omega t.",
            "The dot product k-vector dot r-vector extracts the component",
            "of position along the propagation direction. Surfaces of",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p8.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A spherical wave spreading out from a point source at the",
            "origin has the form A divided by r, times e to the i times",
            "kr minus omega t. The amplitude decreases as one over r,",
            "which ensures that the intensity — proportional to amplitude",
            "squared — falls as one over r squared. This is the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThreeDWaves_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p1.mp3", time_offset=0)
        title = Text("3D Plane Waves and Spherical Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Extending from one dimension to three dimensions, a plane",
            "wave is written as A times e to the power of i times",
            "k-vector dot r-vector minus omega t. The wave vector",
            "k-vector points in the direction of propagation, and its",
            "magnitude is the wave number k.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThreeDWaves_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p2.mp3", time_offset=0)
        title = Text("3D Plane Waves and Spherical Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The wavefronts — surfaces of constant phase — are flat",
            "planes perpendicular to k-vector. Hence the name plane wave.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThreeDWaves_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p3.mp3", time_offset=0)
        title = Text("3D Plane Waves and Spherical Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A spherical wave from a point source has the form A over r",
            "times e to the i kr minus omega t. The amplitude falls off",
            "as 1 over r, which is required by energy conservation: as",
            "the wavefront expands over a larger sphere, the intensity",
            "must decrease as 1 over r squared.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p1.mp3", time_offset=0)
        title = Text("Week 1 Summary", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's collect the essential results from the first half of",
            "Week 1 before moving to Maxwell's equations.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p2.mp3", time_offset=0)
        title = Text("Week 1 Summary", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The wave equation, psi-xx equals one over v-squared times",
            "psi-tt, is the fundamental equation governing all wave",
            "phenomena. Its general solution is any function of x minus",
            "vt or x plus vt. The shape propagates without distortion at",
            "speed v in a non-dispersive medium.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p3.mp3", time_offset=0)
        title = Text("Week 1 Summary", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The harmonic wave relations connect all the wave parameters.",
            "v equals f lambda equals omega over k. The wave number k is",
            "2 pi over lambda. The angular frequency omega is 2 pi f. The",
            "period T is one over f. These five relations are not",
            "independent — any one follows from the others — but knowing",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p4.mp3", time_offset=0)
        title = Text("Week 1 Summary", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The complex representation, psi-tilde equals A e to the i kx",
            "minus omega t, simplifies all wave calculations. The",
            "physical wave is the real part. The intensity is",
            "proportional to the modulus squared, which equals A squared.",
            "The convenience of complex notation becomes most apparent",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p5.mp3", time_offset=0)
        title = Text("Week 1 Summary", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The superposition principle states that linear combinations",
            "of solutions are solutions. This follows from the linearity",
            "of the wave equation and is the foundation of all",
            "interference phenomena. It holds for electromagnetic waves",
            "in linear media, which covers all of classical optics.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p6.mp3", time_offset=0)
        title = Text("Week 1 Summary", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Phase velocity v-p equals omega over k gives the speed of",
            "crests. Group velocity v-g equals d omega d k gives the",
            "speed of energy and information. In a non-dispersive medium",
            "they are equal. In a dispersive medium like glass they",
            "differ, giving rise to pulse spreading and the separation of",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

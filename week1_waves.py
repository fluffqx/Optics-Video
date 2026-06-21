# week1_waves.py — Week 1: Waves (paragraph-per-scene, zero overlap)
from manim import *
from utils import *

class Week1TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation & Complex Representation",
                               "Bennett Ch. 1 & 2.1-2.3")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([
            "Welcome to the complete exam preparation series for 31OPT Optics",
            "at TU Eindhoven.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation & Complex Representation",
                               "Bennett Ch. 1 & 2.1-2.3")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([
            "Week 1 covers the foundation of everything in this course —",
            "waves, the wave equation, and how we represent waves",
            "mathematically using complex numbers.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation & Complex Representation",
                               "Bennett Ch. 1 & 2.1-2.3")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([
            "By the end of this week, you will understand what a wave",
            "actually is, how to write and interpret the wave equation, and",
            "why physicists prefer complex exponentials over sines and",
            "cosines.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation & Complex Representation",
                               "Bennett Ch. 1 & 2.1-2.3")
        self.play(FadeIn(card, run_time=0.3))
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
        title = Text("What Is a Wave?", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "So what exactly is a wave?",
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
            "A wave is a disturbance that transports energy from one place to",
            "another — without transporting matter along with it. Think of",
            "ripples on a pond. The water itself doesn't travel across the",
            "pond. The disturbance does.",
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
            "In optics, the disturbance is the electromagnetic field — the",
            "electric and magnetic fields oscillating together as they travel",
            "through space.",
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
            "We start with the simplest possible case: a wave moving in just",
            "one spatial dimension. One direction. This is the foundation.",
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
            "The wave equation is the mathematical statement that tells us",
            "exactly how such a disturbance evolves in both space and time",
            "simultaneously. Master this equation, and you have the key to",
            "understanding everything else in this course — interference,",
            "diffraction, polarisation, all of it follows from here.",
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
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(gold_box(eq)))
        b = txt_block([
            "Here is the one-dimensional wave equation. Take a moment to look",
            "at its structure.",
        ])
        b.next_to(eq, DOWN, buff=0.4)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class WaveEquation1D_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquation1D_p2.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        lhs = MathTex(r"rac{\partial^2\Psi}{\partial x^2}", font_size=56, color=E_COLOR)
        lhs.next_to(title, DOWN, buff=0.45)
        lbl = Text("LEFT SIDE: spatial curvature of the wave", font_size=28, color=E_COLOR, weight=BOLD)
        safe_scale(lbl, max_width=13.0)
        lbl.next_to(lhs, DOWN, buff=0.3)
        b = txt_block([
            "On the left side, we have the second derivative of psi with",
            "respect to position x. This is the curvature of the wave in",
            "space — how sharply the wave bends at each point.",
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
        rhs = MathTex(r"rac{1}{v^2}rac{\partial^2\Psi}{\partial t^2}", font_size=56, color=B_COLOR)
        rhs.next_to(title, DOWN, buff=0.45)
        lbl = Text("RIGHT SIDE: temporal acceleration / v squared", font_size=28, color=B_COLOR, weight=BOLD)
        safe_scale(lbl, max_width=13.0)
        lbl.next_to(rhs, DOWN, buff=0.3)
        b = txt_block([
            "On the right side, we have one over v squared, times the second",
            "derivative of psi with respect to time. This is the acceleration",
            "of the wave in time — how quickly the wave is changing at each",
            "moment.",
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
            "The equation is saying: the spatial curvature equals the",
            "temporal acceleration, scaled by the wave speed v. Space and",
            "time are linked by a single number — the speed of the wave.",
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
            "Now, what are the solutions to this equation? Any function of",
            "the form f of x minus vt is a solution — this represents a wave",
            "travelling in the positive x direction at speed v. And any",
            "function of the form g of x plus vt travels in the negative x",
            "direction.",
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
            "Notice the key insight: the shape of the wave — whatever shape",
            "it has — travels without distortion. The wave just moves.",
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
            "Let's prove that the function psi equals x minus vt, all",
            "squared, actually satisfies the wave equation. This is Bennett",
            "Example 1.1.",
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
        s1 = labeled_eq(r"\partial^2\Psi/\partial x^2 = 2", "second x-derivative = 2", E_COLOR, 40, 24)
        s2 = labeled_eq(r"\partial^2\Psi/\partial t^2 = 2v^2", "second t-derivative = 2v squared", B_COLOR, 40, 24)
        s3 = labeled_eq(r"\frac{1}{v^2}\cdot 2v^2 = 2 = \partial^2\Psi/\partial x^2\;\checkmark",
                        "LHS = RHS — wave equation satisfied!", GOLD, 36, 24)
        steps = VGroup(s1, s2, s3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(steps, max_width=13.0, max_height=4.5)
        steps.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(steps, run_time=0.1))
        self.wait(1)

class WaveEquationProof_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/WaveEquationProof_p3.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This confirms that any function of the form x minus vt is a",
            "valid travelling wave.",
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
            "harmonic wave — a pure sine or cosine oscillation.",
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
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(gold_box(eq)))
        self.wait(1)

class HarmonicWave_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p3.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"A", font_size=56, color=INTENSITY_COLOR)
        safe_scale(sym, max_width=13.0)
        sym.next_to(title, DOWN, buff=0.45)
        nm = Text("AMPLITUDE", font_size=30, color=INTENSITY_COLOR, weight=BOLD)
        nm.next_to(sym, DOWN, buff=0.2)
        dd = Text("max displacement  [V/m for E-field]", font_size=26, color=WHITE)
        safe_scale(dd, max_width=13.0)
        dd.next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "Let's go through every symbol carefully, because these appear",
            "constantly throughout the course.",
        ])
        b.next_to(dd, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(sym, nm, dd, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p4.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"k = 2\pi/\lambda", font_size=56, color=WAVE_COLOR)
        safe_scale(sym, max_width=13.0)
        sym.next_to(title, DOWN, buff=0.45)
        nm = Text("WAVE NUMBER", font_size=30, color=WAVE_COLOR, weight=BOLD)
        nm.next_to(sym, DOWN, buff=0.2)
        dd = Text("spatial frequency  [rad/m]", font_size=26, color=WHITE)
        safe_scale(dd, max_width=13.0)
        dd.next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "A is the amplitude — the maximum value of the wave. For an",
            "electric field, it's in volts per metre. For a pressure wave, it",
            "would be in Pascals.",
        ])
        b.next_to(dd, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(sym, nm, dd, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p5.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"\omega = 2\pi f = 2\pi/T", font_size=56, color=WAVE_COLOR)
        safe_scale(sym, max_width=13.0)
        sym.next_to(title, DOWN, buff=0.45)
        nm = Text("ANGULAR FREQUENCY", font_size=30, color=WAVE_COLOR, weight=BOLD)
        nm.next_to(sym, DOWN, buff=0.2)
        dd = Text("[rad/s]", font_size=26, color=WHITE)
        safe_scale(dd, max_width=13.0)
        dd.next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "k is the wave number, equal to 2 pi divided by the wavelength",
            "lambda. It tells you how many radians of oscillation fit into",
            "one metre of space. Its units are radians per metre.",
        ])
        b.next_to(dd, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(sym, nm, dd, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p6.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"\lambda", font_size=56, color=WAVE_COLOR)
        safe_scale(sym, max_width=13.0)
        sym.next_to(title, DOWN, buff=0.45)
        nm = Text("WAVELENGTH", font_size=30, color=WAVE_COLOR, weight=BOLD)
        nm.next_to(sym, DOWN, buff=0.2)
        dd = Text("distance between crests  [m]", font_size=26, color=WHITE)
        safe_scale(dd, max_width=13.0)
        dd.next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "Omega is the angular frequency, equal to 2 pi times the",
            "frequency f. It tells you how many radians of oscillation happen",
            "per second.",
        ])
        b.next_to(dd, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(sym, nm, dd, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p7.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"f = 1/T", font_size=56, color=WAVE_COLOR)
        safe_scale(sym, max_width=13.0)
        sym.next_to(title, DOWN, buff=0.45)
        nm = Text("FREQUENCY", font_size=30, color=WAVE_COLOR, weight=BOLD)
        nm.next_to(sym, DOWN, buff=0.2)
        dd = Text("cycles per second  [Hz]", font_size=26, color=WHITE)
        safe_scale(dd, max_width=13.0)
        dd.next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "Lambda is the wavelength — the distance between two consecutive",
            "crests.",
        ])
        b.next_to(dd, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(sym, nm, dd, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p8.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"v = \omega/k = f\lambda", font_size=56, color=WAVE_COLOR)
        safe_scale(sym, max_width=13.0)
        sym.next_to(title, DOWN, buff=0.45)
        nm = Text("PHASE SPEED", font_size=30, color=WAVE_COLOR, weight=BOLD)
        nm.next_to(sym, DOWN, buff=0.2)
        dd = Text("speed of crests  [m/s]", font_size=26, color=WHITE)
        safe_scale(dd, max_width=13.0)
        dd.next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "f is the ordinary frequency in hertz — how many full cycles per",
            "second. Related to the period T by f equals one over T.",
        ])
        b.next_to(dd, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(sym, nm, dd, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p9.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"\phi", font_size=56, color=WHITE)
        safe_scale(sym, max_width=13.0)
        sym.next_to(title, DOWN, buff=0.45)
        nm = Text("INITIAL PHASE", font_size=30, color=WHITE, weight=BOLD)
        nm.next_to(sym, DOWN, buff=0.2)
        dd = Text("shifts wave in time  [rad]", font_size=26, color=WHITE)
        safe_scale(dd, max_width=13.0)
        dd.next_to(nm, DOWN, buff=0.2)
        b = txt_block([
            "v is the phase speed — how fast the wave crests move. It equals",
            "omega divided by k, which also equals f times lambda.",
        ])
        b.next_to(dd, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(sym, nm, dd, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p10.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        hdr = Text("Key Relations — MEMORISE", font_size=28, color=GOLD)
        hdr.next_to(title, DOWN, buff=0.4)
        rels = MathTex(r"v = f\lambda = rac{\omega}{k}\qquad k=rac{2\pi}{\lambda}\qquad \omega=2\pi f\qquad T=rac{1}{f}", font_size=38)
        safe_scale(rels, max_width=13.0)
        rels.next_to(hdr, DOWN, buff=0.3)
        b = txt_block([
            "And phi is the initial phase offset — it shifts the wave left or",
            "right in time.",
        ])
        b.next_to(rels, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(hdr, rels, b), run_time=0.1))
        self.wait(1)

class HarmonicWave_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p11.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's do a quick example. Given lambda equals 500 nanometres and",
            "v equals 3 times 10 to the 8 metres per second — visible green",
            "light — we can find all the other quantities.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWave_p12(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWave_p12.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "k equals 2 pi divided by 500 times 10 to the minus 9, which",
            "gives us 1.257 times 10 to the 7 radians per metre.",
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
            "Multiplying by v gives omega equal to 3.77 times 10 to the 15",
            "radians per second.",
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
            "And the period T equals 2 pi divided by omega, giving 1.67 times",
            "10 to the minus 15 seconds — about 1.7 femtoseconds. Light",
            "oscillates extraordinarily fast.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p1.mp3", time_offset=0)
        title = Text("Example: Green Laser (lambda = 532 nm)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through a complete numerical example using a green",
            "laser pointer at 532 nanometres.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p2.mp3", time_offset=0)
        title = Text("Example: Green Laser (lambda = 532 nm)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        steps = VGroup(
            labeled_eq(r"k=2\pi/(532	imes10^{-9})=1.18	imes10^7\,\text{rad/m}", "wave number", WAVE_COLOR, 34, 22),
            labeled_eq(r"f=c/\lambda=5.64	imes10^{14}\,\text{Hz}", "frequency (564 THz)", WAVE_COLOR, 34, 22),
            labeled_eq(r"\omega=2\pi f=3.54	imes10^{15}\,\text{rad/s}", "angular frequency", WAVE_COLOR, 34, 22),
            labeled_eq(r"T=1/f=1.77\times10^{-15}\,\text{s}=1.77\,\text{fs}", "period (femtoseconds!)", GOLD, 34, 22),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(steps, max_width=13.0, max_height=4.8)
        steps.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(steps, run_time=0.1))
        self.wait(1)

class HarmonicWaveExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HarmonicWaveExample_p3.mp3", time_offset=0)
        title = Text("Example: Green Laser (lambda = 532 nm)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "These numbers give you a feel for how incredibly fast optical",
            "oscillations are — nearly a quadrillion cycles per second.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p1.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The superposition principle is the mathematical foundation of",
            "all interference and diffraction phenomena.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p2.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        proof = MathTex(
            r"\frac{\partial^2(\Psi_1+\Psi_2)}{\partial x^2}"
            r"=\frac{\partial^2\Psi_1}{\partial x^2}+\frac{\partial^2\Psi_2}{\partial x^2}"
            r"=\frac{1}{v^2}\frac{\partial^2(\Psi_1+\Psi_2)}{\partial t^2}\;\checkmark",
            font_size=32)
        safe_scale(proof, max_width=13.0)
        proof.next_to(title, DOWN, buff=0.45)
        b = txt_block([
            "Because the wave equation is linear, any sum of solutions is",
            "also a solution. If wave 1 and wave 2 each satisfy the wave",
            "equation independently, then wave 1 plus wave 2 is automatically",
            "also a valid wave. The proof simply adds the two equations",
            "together.",
        ])
        b.next_to(proof, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(proof, b), run_time=0.1))
        self.wait(1)

class SuperpositionPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SuperpositionPrinciple_p3.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This means two laser beams can cross in space and their electric",
            "fields simply add — they don't interact, scatter, or change each",
            "other. This is what makes optical computing and holography",
            "possible.",
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
            "There are actually two different speeds associated with a wave,",
            "and confusing them is a classic mistake.",
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
        eq = labeled_eq(r"v_p = \omega/k", "PHASE VELOCITY — speed of wave crests  [m/s]", WAVE_COLOR, 52, 28)
        eq.next_to(title, DOWN, buff=0.5)
        b = txt_block([
            "The phase velocity is the speed at which the crests of the wave",
            "move. It's simply omega divided by k. This is the speed of a",
            "single frequency component.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p3.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = labeled_eq(r"v_g = d\omega/dk", "GROUP VELOCITY — speed of energy and information  [m/s]", WAVE_COLOR, 52, 28)
        eq.next_to(title, DOWN, buff=0.5)
        b = txt_block([
            "The group velocity is the speed at which the envelope of a wave",
            "packet moves — this is the speed at which energy and information",
            "actually travel. It's defined as d omega d k — the derivative of",
            "angular frequency with respect to wave number.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p4.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In vacuum, and in any non-dispersive medium, these two speeds",
            "are identical. Every frequency travels at the same speed, so the",
            "wave packet holds its shape.",
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
            "But in a dispersive medium like glass, different frequencies",
            "travel at different speeds — that's exactly what dispersion",
            "means. The phase velocity varies with frequency. And this causes",
            "the group velocity to differ from the phase velocity.",
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
            "This is why a prism separates white light into a rainbow. Red",
            "light and violet light have different phase velocities in glass,",
            "so they refract at different angles.",
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
            "Let's look at a concrete example. Suppose the dispersion",
            "relation is omega equals a times k squared — a hypothetical",
            "case.",
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
            "The phase velocity is omega over k, which equals a k. It depends",
            "on k, so this medium is dispersive.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p9.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The group velocity is d omega d k, which equals 2 a k. That's",
            "twice the phase velocity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class PhaseGroupVelocity_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/PhaseGroupVelocity_p10.mp3", time_offset=0)
        title = Text("Phase Velocity and Group Velocity", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "So in this medium, the envelope of a wave packet travels twice",
            "as fast as the individual crests inside it. Fascinating",
            "behaviour, and directly measurable in real dispersive media.",
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
            "Working with sines and cosines directly becomes very cumbersome",
            "as soon as you try to add waves or compute intensities. There's",
            "a much better way — complex exponentials.",
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
        eq = MathTex(r"e^{i\theta} = \cos\theta + i\sin\theta", font_size=60, color=GOLD)
        safe_scale(eq)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(gold_box(eq)))
        b = txt_block([
            "The key is Euler's formula: e to the power of i theta equals",
            "cosine theta plus i times sine theta. This connects the",
            "exponential function to trigonometry in a beautiful and",
            "extremely useful way.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p3.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"\cos\theta = \mathrm{Re}[e^{i\theta}]", "cosine = real part", WHITE, 40, 24),
            labeled_eq(r"\sin\theta = \mathrm{Im}[e^{i\theta}]", "sine = imaginary part", WHITE, 40, 24),
        ).arrange(DOWN, buff=0.4)
        eqs.next_to(title, DOWN, buff=0.5)
        b = txt_block([
            "From this, cosine theta equals the real part of e to the i",
            "theta, and sine theta is the imaginary part.",
        ])
        b.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p4.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        cw = MathTex(r"\tilde{\Psi} = A\,e^{i(kx-\omega t+\phi)}", font_size=50, color=E_COLOR)
        safe_scale(cw)
        cw.next_to(title, DOWN, buff=0.45)
        rule = MathTex(r"\Psi_{\rm phys} = \mathrm{Re}[\tilde{\Psi}] = A\cos(kx-\omega t+\phi)", font_size=34)
        safe_scale(rule, max_width=13.0)
        rule.next_to(cw, DOWN, buff=0.25)
        b = txt_block([
            "So instead of writing A cosine of kx minus omega t plus phi, we",
            "write A times e to the power of i times kx minus omega t plus",
            "phi. The physical wave is always understood to be the real part",
            "of this complex expression.",
        ])
        b.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(cw, rule, b), run_time=0.1))
        self.wait(1)

class ComplexRepresentation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ComplexRepresentation_p5.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Why is this better? Because multiplying complex exponentials is",
            "trivial — you just add the exponents. Adding waves becomes just",
            "adding complex numbers. And computing intensities becomes taking",
            "the magnitude squared, which is always real and always positive.",
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
            "The intensity is proportional to the magnitude squared of psi —",
            "psi times its complex conjugate — which simply gives A squared.",
            "No oscillating terms to average over.",
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
            "Now we can extend this to three dimensions. A plane wave in 3D",
            "is written as A times e to the i times k-vector dot r-vector",
            "minus omega t. The k-vector points in the direction of",
            "propagation, and k-vector dot r-vector is the projection of the",
            "position onto that direction.",
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
            "A spherical wave spreading out from a point source has amplitude",
            "that falls off as one over r — this ensures energy is conserved",
            "as the wavefront expands over a larger and larger sphere.",
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
        pw = MathTex(r"\tilde{\Psi}(\mathbf{r},t)=A\,e^{i(\mathbf{k}\cdot\mathbf{r}-\omega t)}", font_size=50, color=E_COLOR)
        safe_scale(pw)
        pw.next_to(title, DOWN, buff=0.45)
        sym = eq_table([
            (r"\mathbf{k}", "wave vector — points in propagation direction", WAVE_COLOR),
            (r"|\mathbf{k}|=k=2\pi/\lambda", "magnitude = wave number", WAVE_COLOR),
        ], eq_fs=30, lbl_fs=22, buff=0.22)
        sym.next_to(pw, DOWN, buff=0.35)
        b = txt_block([
            "Extending from one dimension to three dimensions, a plane wave",
            "is written as A times e to the power of i times k-vector dot",
            "r-vector minus omega t. The wave vector k-vector points in the",
            "direction of propagation, and its magnitude is the wave number",
            "k.",
        ])
        b.next_to(sym, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(pw, sym, b), run_time=0.1))
        self.wait(1)

class ThreeDWaves_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThreeDWaves_p2.mp3", time_offset=0)
        title = Text("3D Plane Waves and Spherical Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The wavefronts — surfaces of constant phase — are flat planes",
            "perpendicular to k-vector. Hence the name plane wave.",
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
        sw = labeled_eq(r"\tilde{\Psi}(r,t)=\frac{A}{r}e^{i(kr-\omega t)}",
                        "amplitude = A/r  →  intensity falls as 1/r squared", B_COLOR, 46, 25)
        sw.next_to(title, DOWN, buff=0.5)
        b = txt_block([
            "A spherical wave from a point source has the form A over r times",
            "e to the i kr minus omega t. The amplitude falls off as 1 over",
            "r, which is required by energy conservation: as the wavefront",
            "expands over a larger sphere, the intensity must decrease as 1",
            "over r squared.",
        ])
        b.next_to(sw, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(sw, b), run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p1.mp3", time_offset=0)
        title = Text("Week 1 Summary — Key Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's recap the three essential equations from Week 1.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p2.mp3", time_offset=0)
        title = Text("Week 1 Summary — Key Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = labeled_eq(r"\partial^2\Psi/\partial x^2=(1/v^2)\partial^2\Psi/\partial t^2", "wave equation", GOLD, 34, 24)
        eq.next_to(title, DOWN, buff=0.5)
        b = txt_block([
            "First: the wave equation itself — the second spatial derivative",
            "equals one over v squared times the second time derivative. This",
            "governs all classical wave phenomena.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p3.mp3", time_offset=0)
        title = Text("Week 1 Summary — Key Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = labeled_eq(r"v=f\lambda=\omega/k,\;k=2\pi/\lambda,\;\omega=2\pi f", "harmonic wave relations", WAVE_COLOR, 34, 24)
        eq.next_to(title, DOWN, buff=0.5)
        b = txt_block([
            "Second: the harmonic wave relations — v equals f lambda equals",
            "omega over k, with k equals 2 pi over lambda and omega equals 2",
            "pi f. Know these relationships cold.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)

class Week1WavesSummary_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week1WavesSummary_p4.mp3", time_offset=0)
        title = Text("Week 1 Summary — Key Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = labeled_eq(r"\tilde\Psi=Ae^{i(kx-\omega t)},\;|\tilde\Psi|^2=A^2", "complex representation", E_COLOR, 34, 24)
        eq.next_to(title, DOWN, buff=0.5)
        b = txt_block([
            "Third: the complex representation — psi tilde equals A e to the",
            "i times kx minus omega t. The physical wave is the real part.",
            "The intensity is the magnitude squared, which equals A squared.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)

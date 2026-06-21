# week8_fabry_perot.py — Week 8 (paragraph-per-scene)
from manim import *
from utils import *

class Week8TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p1.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Week 8 brings us to the Fabry-Pérot interferometer — the most",
            "powerful spectroscopic instrument based on interference.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p2.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Unlike the two-beam Michelson, the Fabry-Pérot uses multiple",
            "reflections between two highly reflective parallel mirrors.",
            "Light bounces back and forth many times, and all the",
            "transmitted beams interfere together. This is multi-beam",
            "interference.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p3.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The result is the Airy function: transmitted intensity equals",
            "I naught divided by one plus F times sine squared of delta",
            "over 2, where F is the coefficient of finesse equal to 4R over",
            "one minus R squared, and delta is the round-trip phase.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p4.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When delta is a multiple of 2 pi, the sine term is zero and",
            "the transmission is maximum — equal to I naught. This is",
            "resonance. All the multiply-reflected beams are in phase and",
            "add up constructively.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p5.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When delta is an odd multiple of pi, the transmission drops to",
            "its minimum. For high reflectivity, this minimum is extremely",
            "close to zero. The contrast between maximum and minimum is",
            "enormous.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p6.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The sharpness of the transmission peaks is characterised by",
            "the finesse, script F, equal to pi times square root of R over",
            "one minus R. For mirror reflectivity R equals 0.99, the",
            "finesse is about 310. The peaks are 310 times narrower than",
            "the spacing between them.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p7.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The free spectral range is the spacing between successive",
            "resonances: delta lambda equals lambda squared over 2nd in",
            "wavelength, or delta nu equals c over 2nd in frequency.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p8.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power R equals m times finesse — where m is the",
            "resonance order. For a 10 centimetre cavity and 633 nanometre",
            "light, m is about 300,000, giving a resolving power of nearly",
            "20 million. This is extraordinary compared to a grating.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p9.mp3", time_offset=0)
        title = Text("Fabry-Perot Interferometer", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Coherence determines whether interference fringes are visible",
            "at all. The temporal coherence length equals lambda squared",
            "over delta lambda. A laser with a narrow linewidth has a long",
            "coherence length — metres or more. A thermal source has a",
            "coherence length of micrometres.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MultiBeamIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p1.mp3", time_offset=0)
        title = Text("From Two Beams to Multiple Beams  (Bennett 7.10)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In the Michelson interferometer and Young's double slit,",
            "exactly two beams interfere. The Fabry-Pérot takes this much",
            "further by using an infinite series of beams — all the",
            "multiply-reflected beams between two parallel mirrors.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MultiBeamIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p2.mp3", time_offset=0)
        title = Text("From Two Beams to Multiple Beams  (Bennett 7.10)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The setup is two flat, partially-reflecting parallel mirrors",
            "separated by distance d. Light enters through the first mirror",
            "and bounces back and forth. At each bounce, a fraction T of",
            "the power transmits out. So there's a first transmitted beam,",
            "then a second weaker one after two reflections, then a third",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MultiBeamIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p3.mp3", time_offset=0)
        title = Text("From Two Beams to Multiple Beams  (Bennett 7.10)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett sums this infinite geometric series in Section 7.10.",
            "The key mathematical identity is that the sum of x to the n",
            "equals 1 over 1 minus x, for x less than 1.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MultiBeamIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p4.mp3", time_offset=0)
        title = Text("From Two Beams to Multiple Beams  (Bennett 7.10)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The result depends critically on the phase relationship",
            "between successive beams. If all beams are in phase —",
            "constructive interference — the transmitted field is",
            "enormously amplified. If they are out of phase, they cancel.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MultiBeamIntro_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p5.mp3", time_offset=0)
        title = Text("From Two Beams to Multiple Beams  (Bennett 7.10)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is fundamentally different from two-beam interference.",
            "With two beams, you get a smooth cosine pattern. With",
            "infinitely many beams, you get very sharp transmission spikes",
            "at resonance and nearly zero transmission everywhere else. The",
            "more reflective the mirrors, the sharper the spikes.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class AiryFunction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p1.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Airy function is the central result of Fabry-Pérot theory.",
            "Bennett derives it in Section 7.10 by summing the infinite",
            "geometric series of multiply-reflected transmitted beams.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class AiryFunction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p2.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The result is: transmitted intensity equals I-naught divided",
            "by one plus F times sine squared of delta over two, where F is",
            "the coefficient of finesse and delta is the round-trip phase.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class AiryFunction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p3.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When delta is a multiple of 2 pi — the resonance condition —",
            "the sine term is zero and the transmission is I-naught,",
            "meaning 100 percent. This is the remarkable property of the",
            "Fabry-Pérot: even with highly reflective mirrors that",
            "individually transmit only a few percent, the transmission at",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class AiryFunction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p4.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The physical explanation is that at resonance, all the",
            "multiply-reflected beams are in phase and add constructively.",
            "The field builds up inside the cavity to a very large",
            "amplitude, and the increased build-up exactly compensates for",
            "the low transmission of each mirror.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class AiryFunction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p5.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Between resonances, the sine term is large, and the",
            "transmission drops to nearly zero for high-finesse cavities.",
            "The pattern looks like a series of very sharp transmission",
            "spikes separated by broad dark regions.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class AiryFunction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p6.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The coefficient of finesse F equals 4R over one minus R",
            "squared. For a mirror reflectivity of 99 percent, F equals",
            "39,600 — giving extremely sharp peaks.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinesseResolving_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p1.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Three quantities characterise the performance of a Fabry-Pérot",
            "interferometer: the finesse, the resolving power, and the free",
            "spectral range.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinesseResolving_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p2.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The finesse — written as a script F — is the ratio of the free",
            "spectral range to the full width at half maximum of a",
            "transmission peak. It equals pi times square root of R,",
            "divided by one minus R. For R equals 99 percent, the finesse",
            "is about 312. This means the transmission peaks are 312 times",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinesseResolving_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p3.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Physically, the finesse equals the average number of times a",
            "photon bounces back and forth before leaking out through a",
            "mirror. Higher reflectivity means more bounces, narrower",
            "peaks, higher finesse.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinesseResolving_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p4.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The order number N equals 2nd divided by lambda — the number",
            "of half-wavelengths that fit in the cavity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinesseResolving_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p5.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power equals N times the finesse. This can be",
            "enormous — a cavity of 10 centimetres at 633 nanometres has N",
            "equal to about 316,000. Multiplied by a finesse of 312, the",
            "resolving power exceeds 98 million.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinesseResolving_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p6.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The free spectral range in wavelength is lambda squared over",
            "2nd. It tells you the range of wavelengths you can measure",
            "unambiguously — adjacent resonance orders must not overlap",
            "your spectrum.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FinesseResolving_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p7.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Note carefully: the coefficient of finesse F and the finesse",
            "script-F are different quantities. The coefficient is 4R over",
            "one minus R squared. The finesse is pi root R over one minus",
            "R. Don't confuse them — it's a standard notation trap.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p1.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through Bennett's Example 7.11 — measuring the",
            "splitting between the hydrogen and deuterium H-alpha spectral",
            "lines using a Fabry-Pérot interferometer.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p2.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Hydrogen H-alpha is at 656.28 nanometres. Deuterium H-alpha is",
            "at 656.10 nanometres. The splitting is 0.18 nanometres. We",
            "want to resolve this with mirrors of 90 percent reflectivity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p3.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "First, the coefficient of finesse: F equals 4 times 0.90",
            "divided by 0.10 squared, giving 360. The finesse is pi times",
            "square root of 360 divided by 2, giving 29.8.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p4.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "We choose a free spectral range of 0.5 nanometres to",
            "comfortably bracket the 0.18 nanometre splitting. This",
            "requires a mirror spacing of d equals lambda squared over 2",
            "times delta-lambda-FSR, which gives 0.431 millimetres. Tight!",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p5.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The order number at this spacing is N equals 1313. The",
            "resolving power is N times finesse equals 1313 times 29.8,",
            "giving about 39,000.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p6.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The minimum resolvable wavelength difference is lambda over",
            "resolving power, which is 656.2 divided by 39,000, giving",
            "0.017 nanometres. This is more than ten times smaller than the",
            "actual splitting of 0.18 nanometres — the lines are clearly",
            "resolved.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p7.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For comparison, the best diffraction grating we looked at had",
            "a resolving power of 30,000. The Fabry-Pérot beats it in a",
            "much more compact device.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CoherenceLength_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p1.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Fabry-Pérot interferometer only works if the light source",
            "has sufficient temporal coherence — the ability to interfere",
            "with a delayed copy of itself.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CoherenceLength_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p2.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Coherence length is related to spectral purity. A perfectly",
            "monochromatic wave — which doesn't exist in reality — would",
            "have infinite coherence length. Real sources have a spread of",
            "frequencies delta-nu, and their coherence length is",
            "approximately c divided by delta-nu, or equivalently lambda",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CoherenceLength_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p3.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For the Fabry-Pérot to show fringes, the cavity round trip",
            "must be shorter than the coherence length. Otherwise, the",
            "beams from different round trips are no longer coherent with",
            "each other, and the interference averages out.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CoherenceLength_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p4.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The coherence length varies enormously between different light",
            "sources. White light from a thermal source has a coherence",
            "length of about 1 micrometre — too short for almost any",
            "interferometer. A sodium lamp filtered to one line has about",
            "half a millimetre. A stabilised helium-neon laser has hundreds",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CoherenceLength_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p5.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is why gravitational wave detectors like LIGO use",
            "ultra-stable lasers — the 4-kilometre arms require the laser",
            "to be coherent over an 8-kilometre round trip.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p1.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's collect all the Fabry-Pérot formulas in one place.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p2.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Airy function: I-t equals I-naught divided by one plus F",
            "sine squared of delta over 2. This is the transmitted",
            "intensity as a function of round-trip phase.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p3.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The coefficient of finesse F equals 4R over one minus R",
            "squared.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p4.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The finesse script-F equals pi root R over one minus R.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p5.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The round-trip phase delta equals 4 pi n d cosine theta over",
            "lambda-naught.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p6.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The order number N equals 2nd over lambda-naught.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p7.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power equals N times the finesse.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p8.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The free spectral range in wavelength equals lambda-naught",
            "squared over 2nd.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p9.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The free spectral range in frequency equals c over 2nd — this",
            "is the cavity mode spacing.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p10.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "And the coherence length of the light source must exceed 2nd",
            "for fringes to be visible.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p11.mp3", time_offset=0)
        title = Text("Week 8 Summary — All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "These formulas describe the most powerful spectroscopic",
            "instrument based on interference. Study them carefully — the",
            "Fabry-Pérot almost always appears on the final exam.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

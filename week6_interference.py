# week6_interference.py — Week 6 (paragraph-per-scene)
from manim import *
from utils import *

class Week6TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p1.mp3", time_offset=0)
        title = Text("Interference and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Interference is perhaps the most dramatic demonstration that",
            "light is a wave. When two coherent waves overlap, they don't",
            "just add their intensities — they can add constructively to",
            "give bright fringes, or cancel destructively to give darkness.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p2.mp3", time_offset=0)
        title = Text("Interference and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key quantity is the phase difference delta between the two",
            "beams. If delta is a multiple of 2 pi, the waves are in phase",
            "and interfere constructively. If delta is an odd multiple of",
            "pi, they're out of phase and interfere destructively.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p3.mp3", time_offset=0)
        title = Text("Interference and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The phase difference comes from two sources: the optical path",
            "difference — how much farther one beam has to travel — and any",
            "phase shifts that occur upon reflection.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p4.mp3", time_offset=0)
        title = Text("Interference and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The optical path difference is n times the geometric path",
            "length. Converting to phase: delta equals 2 pi over lambda",
            "naught times the OPD.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p5.mp3", time_offset=0)
        title = Text("Interference and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Crucially: whenever light reflects off a surface where it's",
            "going from a lower to a higher refractive index, it picks up a",
            "phase shift of pi. This is equivalent to adding half a",
            "wavelength to the path. If the other reflection doesn't have",
            "this shift, the two beams start with a pi phase difference",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p6.mp3", time_offset=0)
        title = Text("Interference and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Young's double slit experiment proved the wave nature of light",
            "in 1801. Two slits separated by d produce an interference",
            "pattern on a screen at distance L. The fringe spacing is",
            "simply lambda times L over d. Bigger wavelength, bigger",
            "fringes. Closer slits, bigger fringes.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p7.mp3", time_offset=0)
        title = Text("Interference and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Thin film interference explains the colours of soap bubbles",
            "and oil slicks. The film has two surfaces, and the two",
            "reflected beams interfere. The total phase difference depends",
            "on the film thickness, the refractive index, and whether",
            "reflection phase shifts are present.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p8.mp3", time_offset=0)
        title = Text("Interference and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Michelson interferometer splits a beam in two, sends each",
            "part down a separate arm, reflects them, and recombines them.",
            "Moving one mirror by half a wavelength shifts the OPD by one",
            "full wavelength, producing one complete fringe cycle. This",
            "instrument can measure distances to nanometre precision.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p1.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett Ch. 7)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Interference is what happens when two or more coherent waves",
            "overlap. Their electric fields add by superposition, and the",
            "resulting intensity can be larger or smaller than the sum of",
            "the individual intensities.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p2.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett Ch. 7)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When two waves are in phase — their crests align — the",
            "amplitude doubles and the intensity quadruples. This is",
            "constructive interference. When they are exactly out of phase",
            "— crests align with troughs — they cancel completely. This is",
            "destructive interference.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p3.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett Ch. 7)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key requirement is coherence: the two waves must have a",
            "stable, well-defined phase relationship. A single laser split",
            "into two beams is coherent. Two separate lamps are not — their",
            "phases fluctuate randomly on timescales of nanoseconds,",
            "washing out any interference pattern.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p1.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett Section 7.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Two-beam interference is the foundation of all interferometry.",
            "When two coherent beams overlap, the total intensity is not",
            "simply the sum of the individual intensities — there is an",
            "extra interference term.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p2.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett Section 7.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The general formula is I equals I-one plus I-two plus two",
            "times the square root of I-one times I-two, times cosine",
            "delta. That extra cosine delta term is the new physics of wave",
            "optics. It can add up to four times I-naught when delta is",
            "zero, or cancel completely when delta is pi.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p3.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett Section 7.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The phase difference delta comes from two sources: the optical",
            "path difference — how much farther one beam travels — and any",
            "phase shifts that occur upon reflection. A reflection at a",
            "surface where the refractive index increases gives a pi phase",
            "shift, equivalent to half a wavelength of extra path.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p4.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett Section 7.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When both beams have equal intensity I-naught, the pattern",
            "simplifies to four I-naught cosine squared of delta over two.",
            "The maximum is four times the single-beam intensity — this is",
            "where the energy redistribution comes from. Dark fringes have",
            "zero intensity, compensated by the brighter maxima.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p1.mp3", time_offset=0)
        title = Text("Young's Double-Slit Experiment  (Bennett 7.3.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In Young's double-slit experiment, two narrow slits separated",
            "by a distance d are illuminated by a coherent source. Each",
            "slit acts as a secondary wave source, and the two waves",
            "overlap on a distant screen.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p2.mp3", time_offset=0)
        title = Text("Young's Double-Slit Experiment  (Bennett 7.3.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The path difference from the two slits to a point at angle",
            "theta on the screen is d sine theta. When this path difference",
            "equals a whole number of wavelengths, we get constructive",
            "interference — a bright fringe. When it's a half-integer",
            "number of wavelengths, we get destructive interference — a",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p3.mp3", time_offset=0)
        title = Text("Young's Double-Slit Experiment  (Bennett 7.3.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The phase difference between the two beams is delta equals 2",
            "pi over lambda times d sine theta.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p4.mp3", time_offset=0)
        title = Text("Young's Double-Slit Experiment  (Bennett 7.3.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The intensity pattern is I equals 4 I naught times cosine",
            "squared of delta over 2. The maximum intensity is 4 I naught —",
            "four times the intensity from a single slit — because the",
            "amplitudes add, and squaring doubles the factor.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p5.mp3", time_offset=0)
        title = Text("Young's Double-Slit Experiment  (Bennett 7.3.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The fringe spacing on a screen at distance L is delta y equals",
            "lambda L over d. This is the most important formula for",
            "Young's experiment. Notice: longer wavelength gives wider",
            "fringes, closer slits give wider fringes.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p6.mp3", time_offset=0)
        title = Text("Young's Double-Slit Experiment  (Bennett 7.3.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's calculate. With d equals 0.1 millimetres, L equals 1.5",
            "metres, and lambda equals 500 nanometres, the fringe spacing",
            "is 500 times 10 to the minus 9 times 1.5 over 10 to the minus",
            "4, which equals 7.5 millimetres. Easily visible with the naked",
            "eye.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p1.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett Section 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Thin film interference explains some of the most beautiful",
            "optical phenomena — the rainbow colours of soap bubbles, oil",
            "slicks on water, and the reflective coatings on camera lenses.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p2.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett Section 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key is that a thin transparent film reflects light at both",
            "its top and bottom surfaces. These two reflected beams travel",
            "different path lengths and may have different reflection phase",
            "shifts. Their interference determines whether the film looks",
            "bright or dark at each wavelength.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p3.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett Section 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The total phase difference has two contributions. First, the",
            "path difference from the extra round trip inside the film,",
            "which gives a phase of four pi n-film times thickness times",
            "cosine theta-t, all divided by the vacuum wavelength. Second,",
            "any reflection phase shifts — remember that each reflection",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p4.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett Section 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Counting the reflection phase shifts carefully is the most",
            "common source of errors. Work through each surface",
            "systematically: does n increase or decrease? If it increases,",
            "add pi. If it decreases, add nothing.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p5.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett Section 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Anti-reflection coatings use this deliberately — a",
            "quarter-wavelength layer of the right index cancels the",
            "reflection completely at the design wavelength.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p1.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Fringe visibility — also called fringe contrast — quantifies",
            "how sharp the interference fringes are.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p2.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The visibility V is defined as I_max minus I_min, divided by",
            "I_max plus I_min. Perfect fringes give V equals 1. No fringes",
            "at all give V equals 0.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p3.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For two beams of equal intensity from a perfectly coherent",
            "source, V equals 1. If the intensities are unequal, V is less",
            "than 1 even with perfect coherence — the dark fringes are not",
            "completely dark.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p4.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Visibility can also degrade due to spatial or temporal",
            "incoherence. Measuring visibility as a function of path",
            "difference is how we characterise the coherence length of a",
            "source.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p1.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett Section 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Michelson interferometer is one of the most important",
            "instruments in the history of physics. Albert Michelson built",
            "the first version in 1881, specifically to detect the",
            "luminiferous aether — the hypothetical medium through which",
            "light was thought to travel.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p2.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett Section 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The experiment failed to detect the aether, and this null",
            "result was a crucial step toward special relativity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p3.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett Section 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The setup is simple: a beamsplitter divides the input beam",
            "into two arms. Each arm reflects off a mirror and returns. The",
            "two beams recombine and interfere. Moving one mirror by a",
            "distance delta-L changes the optical path difference by two",
            "times delta-L — factor of two because the beam travels the arm",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p4.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett Section 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Each time the mirror moves by half a wavelength, the fringes",
            "go through one complete cycle. So counting fringes gives an",
            "extraordinarily precise measurement of mirror displacement.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p5.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett Section 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power equals two L over lambda, where L is the",
            "total mirror travel. For a laser with a long coherence length,",
            "L can be metres, giving resolving powers in the millions. This",
            "is why Michelson interferometers are used to detect",
            "gravitational waves — the LIGO detectors are essentially",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

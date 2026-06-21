# week8_fabry_perot.py — paragraph-per-scene
from manim import *
from utils import *

class Week8TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett Sections 7.10-7.12")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 8 brings us to the Fabry-Pérot interferometer — the",
            "most powerful spectroscopic instrument based on classical",
            "interference, and the foundation of modern laser cavities.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett Sections 7.10-7.12")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Unlike the two-beam Michelson interferometer, the",
            "Fabry-Pérot uses multiple reflections between two parallel",
            "mirrors. A beam bounces back and forth many times, and all",
            "the multiply-reflected beams interfere simultaneously. The",
            "result is the Airy function — narrow transmission peaks",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett Sections 7.10-7.12")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The key performance parameters are: the finesse, which",
            "determines the sharpness of the peaks; the free spectral",
            "range, which determines the unambiguous wavelength interval;",
            "and the resolving power, which determines the minimum",
            "wavelength difference that can be resolved. We will also",
        ])
        b.move_to(ORIGIN)
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
            "In the Michelson interferometer, exactly two beams interfere",
            "— the two reflections from the two arms. The interference is",
            "sinusoidal: the intensity varies as cosine squared of the",
            "path difference, producing a broad, smooth fringe pattern.",
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
            "In the Fabry-Pérot cavity, formed by two parallel",
            "partially-reflecting mirrors of reflectivity R, a beam",
            "bounces back and forth many times. Each round trip produces",
            "both a transmitted beam and a reflected beam. After N round",
            "trips, the transmitted amplitude from that pass is t squared",
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
            "The total transmitted field is a geometric series: t squared",
            "times one plus r-squared e to the i delta plus r-fourth e to",
            "the 2i delta plus dot dot dot, where delta equals 4 pi n d",
            "cosine theta over lambda is the round-trip phase. Summing",
            "the series: T-tilde equals t-squared over one minus",
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
            "The transmitted intensity is the modulus squared of T-tilde",
            "divided by the input intensity: I-t over I-naught equals",
            "t-squared squared over the modulus squared of one minus",
            "r-squared e to the i delta. Expanding the denominator and",
            "using energy conservation gives the Airy function.",
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
            "The Airy function is the central result of Fabry-Pérot",
            "theory. Transmitted intensity equals I-naught divided by one",
            "plus F times sine-squared of delta over two, where F is the",
            "coefficient of finesse, F equals 4R over one minus R",
            "squared.",
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
            "At resonance — when delta equals 2N pi for integer N — the",
            "sine term is zero and I-t equals I-naught. Complete",
            "transmission, regardless of R. Even if each mirror has 99",
            "percent reflectivity, the cavity transmits 100 percent at",
            "resonance. The physical explanation: at resonance, all the",
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
            "Off resonance — when delta is between resonances — the sine",
            "term is of order one, and I-t drops to I-naught divided by",
            "one plus F. For R equals 0.9, F equals 360, so the",
            "off-resonance transmission is I-naught over 361, less than",
            "0.3 percent. The cavity is essentially opaque off resonance.",
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
            "The coefficient of finesse F equals 4R divided by one minus",
            "R squared should not be confused with the finesse script-F.",
            "F appears in the Airy formula. Script-F equals pi root R",
            "over one minus R is the ratio of the free spectral range to",
            "the full-width-at-half-maximum of each transmission peak.",
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
            "As R increases toward one, F increases as one over one minus",
            "R squared, and the peaks become progressively sharper. For R",
            "equals 0.99: F equals 4 times 0.99 over 0.0001 equals",
            "39,600, and script-F equals pi times 0.995 over 0.01 equals",
            "312. The peaks are extremely sharp.",
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
            "Three key parameters describe the performance of a",
            "Fabry-Pérot interferometer: the finesse, the free spectral",
            "range, and the resolving power.",
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
            "The finesse script-F equals pi root R over one minus R",
            "equals pi root F over 2, where F is the coefficient of",
            "finesse. It equals the ratio of the free spectral range to",
            "the FWHM of each transmission peak. Physically, it counts",
            "approximately how many times a photon bounces back and forth",
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
            "The order number N equals 2nd cosine theta over lambda at",
            "normal incidence equals 2nd over lambda. It is the number of",
            "optical wavelengths in one round trip. Resonance occurs at",
            "wavelengths satisfying 2nd equals N lambda, where N is a",
            "large integer. Successive resonances correspond to N, N-one,",
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
            "The resolving power RP equals lambda over delta-lambda-min",
            "equals N times script-F. For a cavity with N equals 1000 and",
            "script-F equals 30: RP equals 30,000. For N equals 10,000",
            "and script-F equals 100: RP equals 1,000,000. Fabry-Pérot",
            "interferometers can achieve resolving powers of tens of",
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
            "The free spectral range in wavelength is delta-lambda-FSR",
            "equals lambda-naught squared over 2nd. It is the separation",
            "between adjacent transmission peaks. The free spectral range",
            "in frequency is delta-nu-FSR equals c over 2nd — this is the",
            "cavity mode spacing, fundamental to laser physics.",
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
            "Do not confuse F with script-F. F equals 4R over one minus R",
            "squared appears in the Airy formula. Script-F equals pi root",
            "R over one minus R appears in resolving power. The ratio",
            "script-F equals pi root F over 2. For R equals 0.9: F equals",
            "360, script-F equals pi times square root 360 over 2 equals",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p1.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through Bennett's Example 7.11 — resolving the",
            "hydrogen and deuterium H-alpha lines.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p2.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The H-alpha line of hydrogen is at 656.28 nanometres. The",
            "H-alpha line of deuterium is at 656.10 nanometres. The",
            "wavelength difference is 0.18 nanometres. We want to design",
            "a Fabry-Pérot with mirror reflectivity R equals 0.90 that",
            "can resolve these two lines.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p3.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step one: coefficient of finesse. F equals 4 times 0.90 over",
            "1 minus 0.90 squared equals 3.60 over 0.01 equals 360.",
            "Finesse: script-F equals pi root 360 over 2 equals pi times",
            "18.97 over 2 equals 29.8.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p4.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step two: choose free spectral range. The FSR must",
            "comfortably exceed the line separation of 0.18 nanometres.",
            "Choose FSR equals 0.50 nanometres, which is nearly three",
            "times the separation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p5.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step three: find the required mirror spacing.",
            "Delta-lambda-FSR equals lambda-naught squared over 2nd. For",
            "a cavity filled with air, n equals 1. Spacing d equals",
            "lambda-naught squared over 2 times delta-lambda-FSR equals",
            "656.2 squared times ten to the minus 18 divided by 2 times",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p6.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step four: compute order number and resolving power. N",
            "equals 2d over lambda-naught equals 2 times 0.431 times ten",
            "to the minus 3 over 656.2 times ten to the minus 9 equals",
            "1313. Resolving power equals N times script-F equals 1313",
            "times 29.8 equals 39,100.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p7.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step five: verify resolution. Minimum resolvable wavelength",
            "difference equals lambda over RP equals 656.2 over 39,100",
            "equals 0.0168 nanometres. This is much smaller than the 0.18",
            "nanometre separation of the H-alpha lines, so yes, they are",
            "clearly resolved with this cavity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FabryPerotExample_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p8.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For comparison: the best diffraction grating we discussed,",
            "with 30,000 slits in first order, has RP equals 30,000. Our",
            "compact 0.43-millimetre Fabry-Pérot with RP equals 39,100",
            "outperforms it, and could do much better with",
            "higher-reflectivity mirrors.",
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
            "A Fabry-Pérot interferometer only functions if the light",
            "source has sufficient temporal coherence. The cavity",
            "round-trip path length 2nd must be shorter than the",
            "coherence length of the light, otherwise the interfering",
            "beams are derived from different parts of the wave train and",
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
            "The coherence length is related to the spectral purity of",
            "the source: l-c equals lambda squared over delta-lambda",
            "equals c over delta-nu, where delta-lambda is the linewidth",
            "and delta-nu is the frequency width of the source.",
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
            "The coherence time is tau-c equals l-c over c equals one",
            "over delta-nu — the lifetime of the coherent wave train.",
            "Sources with narrow linewidth have long coherence time and",
            "long coherence length.",
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
            "White light from an incandescent bulb has a broad spectrum",
            "spanning about 300 nanometres, giving l-c approximately 550",
            "squared over 300 nanometres, approximately 1 micrometre.",
            "White light fringes are only visible for path differences of",
            "a few microns — impractical for most interferometry. But",
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
            "A filtered sodium lamp emitting the yellow D lines with",
            "linewidth of about 0.001 nanometres has l-c approximately",
            "589 squared over 0.001 equals 0.35 metres. Fringes visible",
            "for path differences up to 35 centimetres.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CoherenceLength_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p6.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A free-running He-Ne laser has typical linewidth of a few",
            "megahertz, giving l-c approximately c over delta-nu equals 3",
            "times 10 to the 8 over 10 to the 6 equals 300 metres. Ideal",
            "for laboratory interferometry.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CoherenceLength_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p7.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "An ultra-stabilised laser for gravitational wave detection —",
            "like those used in LIGO — can have linewidths of millihertz,",
            "giving coherence lengths of hundreds of thousands of",
            "kilometres. This extraordinary coherence is what makes LIGO",
            "possible.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p1.mp3", time_offset=0)
        title = Text("Week 8 Summary: All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's collect all the Fabry-Pérot formulas in one place for",
            "quick reference.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p2.mp3", time_offset=0)
        title = Text("Week 8 Summary: All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Airy function: I-t equals I-naught divided by one plus F",
            "sine squared delta over 2. This is the transmitted intensity",
            "as a function of round-trip phase. F is the coefficient of",
            "finesse, F equals 4R over one minus R squared. Delta is the",
            "round-trip phase, delta equals 4 pi n d cosine theta over",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p3.mp3", time_offset=0)
        title = Text("Week 8 Summary: All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The finesse script-F equals pi root R over one minus R. This",
            "equals the FSR divided by the FWHM of each transmission",
            "peak, and approximately equals the average number of round",
            "trips before leakage.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p4.mp3", time_offset=0)
        title = Text("Week 8 Summary: All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The order number N equals 2nd cosine theta over",
            "lambda-naught at normal incidence equals 2nd over",
            "lambda-naught.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p5.mp3", time_offset=0)
        title = Text("Week 8 Summary: All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power equals N times script-F. This is the",
            "ratio lambda over delta-lambda-min.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p6.mp3", time_offset=0)
        title = Text("Week 8 Summary: All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The free spectral range in wavelength is delta-lambda-FSR",
            "equals lambda-naught over N equals lambda-naught squared",
            "over 2nd. The free spectral range in frequency is",
            "delta-nu-FSR equals c over 2nd — this is the cavity mode",
            "spacing and determines the longitudinal mode spectrum of a",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p7.mp3", time_offset=0)
        title = Text("Week 8 Summary: All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The coherence length of the source must exceed 2nd for",
            "fringes to be visible.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week8Summary_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p8.mp3", time_offset=0)
        title = Text("Week 8 Summary: All Fabry-Perot Formulas", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Common mistakes: using F instead of script-F in the",
            "resolving power formula; forgetting the cosine theta factor",
            "for oblique incidence; confusing the order number N with the",
            "number of slits; and using lambda in air instead of",
            "lambda-naught in vacuum when computing the round-trip phase.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

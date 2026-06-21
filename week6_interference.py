# week6_interference.py
from manim import *
from utils import *

class Week6TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 6 is interference — the most visually striking",
            "consequence of the wave nature of light. This follows",
            "Bennett Chapter 7, Sections 7.3 through 7.8 and 7.12.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Interference occurs because the superposition principle",
            "allows wave amplitudes to add, and intensity is proportional",
            "to amplitude squared. When two coherent beams overlap and",
            "add constructively, the intensity can be four times that of",
            "a single beam. When they add destructively, the intensity",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The key topics are: the general two-beam interference",
            "formula with the interference term; Young's double-slit",
            "experiment and the fringe spacing formula delta-y equals",
            "lambda L over d; thin film interference with careful",
            "attention to reflection phase shifts; fringe visibility as a",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week6TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week6TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 6", "Interference and Coherence", "Bennett Ch. 7")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Modern applications of interference include: anti-reflection",
            "coatings on every camera lens; laser Fabry-Pérot cavities",
            "and their longitudinal modes; optical coherence tomography",
            "for medical imaging; gravitational wave detection in LIGO;",
            "and wavelength measurement in spectroscopy. Every one of",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p1.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Interference is the result of the superposition principle",
            "applied to two or more coherent waves occupying the same",
            "region of space. The fields add pointwise, and the intensity",
            "— which goes as field squared — is therefore not simply the",
            "sum of the individual intensities.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p2.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When two waves arrive at a point with the same phase — their",
            "crests and troughs aligned — they interfere constructively.",
            "The total field amplitude is the sum of the individual",
            "amplitudes. For two equal beams each with amplitude",
            "E-naught, the total amplitude is 2E-naught and the intensity",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p3.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When two waves arrive with phases differing by pi — crest",
            "aligned with trough — they interfere destructively. The",
            "fields cancel and the intensity is zero. This zero-intensity",
            "condition is exact for equal-amplitude beams, not",
            "approximate.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p4.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The requirement for interference to be observable is",
            "coherence. The two beams must maintain a stable,",
            "well-defined phase relationship for a time long enough for",
            "the detector to average over. If the phase relationship",
            "fluctuates randomly on a timescale shorter than the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class InterferenceIntroScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/InterferenceIntroScene_p5.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Coherence comes in two forms. Temporal coherence requires",
            "the source to emit at a well-defined frequency — a narrow",
            "spectral linewidth. Spatial coherence requires the source to",
            "be small enough that the wavefront at the point of",
            "observation has a well-defined phase across the aperture.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p1.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The general formula for two-beam interference starts from",
            "the superposition of the two complex fields. Let field one",
            "have amplitude E-one and phase phi-one, and field two have",
            "amplitude E-two and phase phi-two. The total field is E-one",
            "e to the i phi-one plus E-two e to the i phi-two.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p2.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The intensity is proportional to the modulus squared of the",
            "total field. Expanding: I equals E-one squared plus E-two",
            "squared plus two E-one E-two cosine of phi-two minus",
            "phi-one. Writing this in terms of the individual intensities",
            "I-one and I-two and the phase difference delta equals",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p3.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The third term — 2 root I-one I-two cosine delta — is the",
            "interference term. It oscillates between plus 2 root I-one",
            "I-two and minus 2 root I-one I-two as the phase difference",
            "delta varies. For equal intensities I-one equals I-two",
            "equals I-naught: I equals 4 I-naught cosine squared of delta",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p4.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The phase difference delta comes from two sources. First,",
            "the optical path difference — any geometric difference in",
            "the distances the two beams travel contributes 2 pi over",
            "lambda times the optical path difference to the phase",
            "difference. Second, reflection phase shifts — any reflection",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class TwoBeamInterference_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/TwoBeamInterference_p5.mp3", time_offset=0)
        title = Text("Two-Beam Interference  (Bennett 7.3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The fringe spacing — how quickly the pattern alternates",
            "between bright and dark — depends on the geometry of the",
            "setup and the wavelength. Shorter wavelength gives finer",
            "fringes for the same geometry. Larger angle between the",
            "beams gives finer fringes. This is the basis of",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p1.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Young's double-slit experiment, performed in 1801, provided",
            "the first conclusive demonstration that light is a wave. Two",
            "narrow slits separated by distance d are illuminated by a",
            "coherent source. The two slits act as two coherent point",
            "sources and their fields interfere on a distant screen.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p2.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key is the path difference. A point on the screen at",
            "angle theta from the axis receives waves that have travelled",
            "slightly different distances from the two slits. The path",
            "difference is delta equals d sine theta, approximately equal",
            "to dy over L for small angles, where y is the height on the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p3.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Constructive interference — bright fringes — occurs when the",
            "path difference is an integer number of wavelengths: d sine",
            "theta equals m lambda, for m equals zero, plus or minus one,",
            "plus or minus two, and so on. The central maximum at m",
            "equals zero is at theta equals zero, directly ahead of the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p4.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Destructive interference — dark fringes — occurs when the",
            "path difference is a half-integer number of wavelengths: d",
            "sine theta equals m plus one-half times lambda.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p5.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The fringe spacing on a screen at distance L is delta-y",
            "equals lambda L over d. This is the most useful formula for",
            "Young's experiment and you must know it. Larger slit",
            "separation gives finer fringes. Longer wavelength gives",
            "coarser fringes. Larger screen distance gives coarser",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p6.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Complete numerical example: d equals 0.1 millimetres, L",
            "equals 1.5 metres, lambda equals 589 nanometres sodium",
            "yellow light. Fringe spacing equals 589 times ten to the",
            "minus 9 times 1.5 over 0.1 times ten to the minus 3 equals",
            "8.84 millimetres. The fringes are about a centimetre apart —",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class YoungDoubleSlit_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/YoungDoubleSlit_p7.mp3", time_offset=0)
        title = Text("Young Double-Slit  (Bennett 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The intensity pattern is I equals 4 I-naught cosine squared",
            "of pi d y over lambda L. This is a cosine-squared pattern",
            "with the fringes spacing lambda L over d. The envelope of",
            "the pattern is modulated by the single-slit diffraction",
            "function — we will return to this in Week 7.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p1.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Thin film interference produces some of the most beautiful",
            "optical phenomena — the iridescent colours of soap bubbles,",
            "oil slicks on wet pavement, the wings of some butterflies,",
            "and anti-reflection coatings on camera lenses.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p2.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The physics: a thin transparent film reflects light from",
            "both its top and bottom surfaces. These two reflected beams",
            "come from the same original beam, so they are coherent. They",
            "interfere, and whether the interference is constructive or",
            "destructive depends on the film thickness and the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p3.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The optical path difference between the two reflected beams",
            "has two contributions. First, the geometric path difference:",
            "beam 2 travels through the film twice, a distance 2t, but in",
            "a medium with index n-f. The optical path difference is 2",
            "n-f t cosine theta-t, where theta-t is the refraction angle",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p4.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Second, reflection phase shifts must be counted carefully.",
            "When a beam reflects at an interface where the refractive",
            "index increases — going from lower to higher n — the",
            "reflected beam acquires a phase shift of pi. This is",
            "equivalent to an extra optical path of lambda over 2. When",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p5.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Here is the systematic approach. List each reflection. For",
            "each one, ask: does n increase? If yes, add a pi phase shift",
            "to that beam. Compute the net phase difference between the",
            "two reflected beams: subtract the total phase shifts for",
            "beam 1 from those for beam 2. Add the geometric contribution",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p6.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through an anti-reflection coating. A glass",
            "substrate with n equals 1.52 is coated with magnesium",
            "fluoride MgF-two with n equals 1.38. Surrounding medium is",
            "air with n equals 1.00.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p7.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Beam 1 reflects at the air-MgF-two interface. n increases",
            "from 1.00 to 1.38, so beam 1 acquires a pi phase shift.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p8.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Beam 2 passes through MgF-two and reflects at the",
            "MgF-two-glass interface. n increases from 1.38 to 1.52, so",
            "beam 2 acquires a pi phase shift.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p9.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Both beams have the same reflection phase shift, so the net",
            "phase shift from reflections is zero. The total phase",
            "difference is purely from the geometric path: delta equals 4",
            "pi n-f t cosine theta-t over lambda-naught. For destructive",
            "interference of the reflected light — anti-reflection",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinFilmInterference_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinFilmInterference_p10.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett 7.3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For lambda-naught equals 550 nanometres, the design",
            "wavelength: t equals 550 divided by 4 times 1.38 equals 99.6",
            "nanometres. Anti-reflection coatings are about 100",
            "nanometres thick — one hundred billionths of a metre.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p1.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Fringe visibility, also called fringe contrast, quantifies",
            "how sharp and clear the interference fringes are. It is",
            "defined as V equals I-max minus I-min, divided by I-max plus",
            "I-min.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p2.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Perfect visibility V equals one means I-min equals zero —",
            "the dark fringes are completely dark. This requires the two",
            "interfering beams to have equal intensities and to be",
            "perfectly coherent. V equals zero means no fringes — I-max",
            "equals I-min — the pattern is uniformly illuminated with no",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p3.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For two beams with intensities I-one and I-two from a",
            "coherent source: V equals 2 root I-one I-two over I-one plus",
            "I-two. This is maximised when I-one equals I-two, giving V",
            "equals one. For unequal intensities, say I-one equals 9",
            "I-two: V equals 2 times 3 I-two over 9 I-two plus I-two",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p4.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Visibility also depends on coherence. Temporal coherence",
            "determines whether fringes are visible when the path length",
            "difference is large. If the two beams differ in path length",
            "by more than the coherence length l-c equals lambda squared",
            "over delta-lambda, the fringes wash out. Spatial coherence",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FringeVisibility_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FringeVisibility_p5.mp3", time_offset=0)
        title = Text("Fringe Visibility and Coherence  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Measuring visibility as a function of path length difference",
            "gives the coherence length of the source. This is how",
            "astronomers measure the diameter of distant stars using",
            "stellar interferometry — the fringe visibility as a function",
            "of telescope separation tells you the angular size of the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p1.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Michelson interferometer is one of the most important",
            "instruments in the history of physics. Albert Michelson",
            "built it in 1881, and the null result of the",
            "Michelson-Morley experiment — which showed no aether drag —",
            "was a crucial step toward special relativity.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p2.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The setup: a beam splitter divides the input beam into two",
            "arms. Each arm has a mirror at the end. The reflected beams",
            "recombine at the beam splitter and interfere. The path",
            "length difference between the two arms determines the phase",
            "difference and hence the intensity at the detector.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p3.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When one mirror is moved by a distance delta-L, the optical",
            "path in that arm changes by 2 delta-L — because the beam",
            "travels to the mirror and back. The phase difference changes",
            "by 4 pi delta-L over lambda. Each time delta-L increases by",
            "lambda over 2, the intensity goes through one complete",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p4.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The modern application: LIGO — the Laser Interferometer",
            "Gravitational-Wave Observatory. Two perpendicular arms, each",
            "4 kilometres long, with Fabry-Pérot cavities increasing the",
            "effective path length to 1600 kilometres. A gravitational",
            "wave from a merging black hole system changes the arm",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MichelsonScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MichelsonScene_p5.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett 7.8)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power of a Michelson interferometer — its",
            "ability to distinguish two close wavelengths — equals 2L",
            "over lambda, where L is the total path length explored. For",
            "a small desktop instrument with L equals one centimetre:",
            "resolving power equals 2 times 0.01 divided by 500 times 10",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

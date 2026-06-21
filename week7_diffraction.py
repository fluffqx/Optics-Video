# week7_diffraction.py
from manim import *
from utils import *

class Week7TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 7", "Fraunhofer Diffraction", "Bennett Ch. 8")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 7 is diffraction — the bending and spreading of light",
            "as it passes through apertures or around obstacles. This",
            "follows Bennett Chapter 8, Sections 8.2 through 8.3.8.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 7", "Fraunhofer Diffraction", "Bennett Ch. 8")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Diffraction is what happens when the aperture size becomes",
            "comparable to the wavelength, so that geometric optics",
            "fails. Bennett opens Chapter 8 with a precise statement: in",
            "a sense, diffraction is interference done correctly. In",
            "Young's experiment we had two discrete point sources. In",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 7", "Fraunhofer Diffraction", "Bennett Ch. 8")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The Fraunhofer approximation — valid when the screen is in",
            "the far field — reduces the diffraction integral to a",
            "Fourier transform. The single-slit pattern is the",
            "sinc-squared function. The circular aperture gives the Airy",
            "disk with its 1.22 lambda over D angular radius. The",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 7", "Fraunhofer Diffraction", "Bennett Ch. 8")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "These results determine the resolution of every optical",
            "instrument — telescope, microscope, camera, spectrograph.",
            "Understanding why a larger aperture gives better resolution,",
            "and by exactly how much, is the central practical lesson of",
            "this week.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p1.mp3", time_offset=0)
        title = Text("Huygens Principle  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Huygens proposed in 1678 that every point on a wavefront",
            "acts as the source of a secondary spherical wavelet. The new",
            "wavefront at a later time is the envelope of all these",
            "secondary wavelets. This principle correctly predicts",
            "reflection, refraction, and diffraction, though it was not",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p2.mp3", time_offset=0)
        title = Text("Huygens Principle  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In Young's double-slit experiment, we had two discrete",
            "Huygens sources — the two slits. The interference pattern",
            "was the superposition of two spherical waves. In single-slit",
            "diffraction, we have an infinite number of Huygens sources",
            "distributed continuously across the slit aperture. The",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p3.mp3", time_offset=0)
        title = Text("Huygens Principle  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Fraunhofer approximation — also called the far-field",
            "approximation — applies when the screen is far enough from",
            "the aperture that the wavefronts arriving at the screen can",
            "be treated as plane waves. The condition is L much greater",
            "than a squared over lambda, where a is the aperture size and",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p4.mp3", time_offset=0)
        title = Text("Huygens Principle  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In the Fraunhofer regime, the diffraction integral",
            "simplifies to a Fourier transform. The electric field",
            "pattern at angle theta is proportional to the Fourier",
            "transform of the aperture function, evaluated at spatial",
            "frequency u equals sine theta over lambda. This Fourier",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p1.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a single slit of width b, the Fraunhofer diffraction",
            "integral gives the famous sinc-squared pattern. Define beta",
            "equals pi b sine theta over lambda. The intensity is I",
            "equals I-naught times sine-squared beta over beta-squared.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p2.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The function sine beta over beta is the sinc function — it",
            "equals one at beta equals zero, decreasing oscillatorily",
            "toward zero as beta increases. Squaring it gives I-naught at",
            "the centre and decreasing secondary maxima.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p3.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The central maximum is the dominant feature: it spans from",
            "the first zero on the left to the first zero on the right.",
            "The zeros of the sinc-squared function occur where sine beta",
            "equals zero with beta nonzero, meaning beta equals m pi for",
            "non-zero integer m. This gives the condition for dark",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p4.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The central maximum has double the angular width of each",
            "secondary maximum. The first secondary maximum has an",
            "intensity of about 4.7 percent of the central maximum. The",
            "second has about 1.7 percent. The energy is concentrated in",
            "the central maximum.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p5.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Physical intuition: the slit can be divided into pairs of",
            "segments, one from each half of the slit. At the first dark",
            "minimum, each pair contributes a path difference of exactly",
            "lambda, so they cancel. The central bright maximum occurs",
            "because all contributions have nearly the same path length",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p6.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A key result: the half-angular width of the central maximum",
            "is theta-half equals arcsin of lambda over b, approximately",
            "lambda over b in radians for small angles. A narrower slit",
            "gives a wider diffraction pattern. Wider slit gives narrower",
            "pattern. This inverse relationship — width in aperture space",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p7.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For our complete example: b equals 0.200 millimetres, lambda",
            "equals 632.8 nanometres, screen at L equals 2.00 metres.",
            "First dark minimum: sine theta-one equals lambda over b",
            "equals 3.164 times ten to the minus 3. Position on screen:",
            "y-one equals L theta-one approximately L sine theta-one",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p1.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3-8.3.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Most optical systems — the human eye, camera lenses,",
            "telescope objectives, microscope objectives — have circular",
            "apertures, not rectangular slits. The Fraunhofer diffraction",
            "pattern of a circular aperture of diameter D is the Airy",
            "disk: a bright central disk surrounded by concentric bright",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p2.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3-8.3.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The mathematics replaces the one-dimensional sinc function",
            "with a Bessel function. The radial intensity distribution is",
            "I equals I-naught times 2 J-one of x over x, squared, where",
            "x equals pi D r over lambda z, with r the distance from the",
            "axis on the screen and z the distance to the screen.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p3.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3-8.3.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "J-one is the first-order Bessel function of the first kind.",
            "Its first zero occurs at x equals 3.832, not at x equals pi",
            "as for the sinc function. This gives the radius of the first",
            "dark ring: sin theta-one equals 1.22 lambda over D. The",
            "factor 1.22 is not approximate — it comes from the exact",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p4.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3-8.3.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Rayleigh criterion defines the resolution limit of a",
            "diffraction-limited optical system: two point sources are",
            "just resolved when the central maximum of one coincides with",
            "the first dark ring of the other. The minimum resolvable",
            "angular separation is theta-min equals 1.22 lambda over D.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p5.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3-8.3.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Human eye: D approximately 3 millimetres at normal viewing,",
            "lambda approximately 550 nanometres. Theta-min equals 1.22",
            "times 550 times ten to the minus 9 over 3 times ten to the",
            "minus 3 equals 2.24 times ten to the minus 4 radians equals",
            "about 46 arcseconds, approximately one arcminute. This",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p6.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3-8.3.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Hubble Space Telescope: D equals 2.4 metres. Theta-min",
            "equals 1.22 times 550 times ten to the minus 9 over 2.4",
            "equals 2.8 times ten to the minus 7 radians equals 0.058",
            "arcseconds. Hubble is about 800 times sharper than the",
            "unaided eye, and its resolution is limited by diffraction —",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p7.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3-8.3.4)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "To improve resolution: either decrease lambda or increase D.",
            "X-ray telescopes like Chandra use shorter wavelengths. Radio",
            "telescopes compensate their longer wavelengths with huge",
            "dishes — the Very Large Array has baselines of 36",
            "kilometres. VLBI — very long baseline interferometry — uses",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p1.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A diffraction grating takes the principle of interference to",
            "its logical extreme. Instead of two slits, it has N slits",
            "with spacing d, where N can be thousands or tens of",
            "thousands per millimetre.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p2.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The grating equation is d times sine theta-m equals m",
            "lambda, for normal incidence, where m is the order number.",
            "This is the condition for constructive interference from all",
            "N slits simultaneously. Light of wavelength lambda is",
            "diffracted into a series of sharp maxima at angles theta-m,",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p3.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The sharpness of these maxima is what makes gratings so",
            "powerful for spectroscopy. With N slits, each maximum has an",
            "angular width proportional to one over N. The more slits,",
            "the sharper the peaks. And sharper peaks mean closer",
            "wavelengths can be resolved.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p4.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power is R equals lambda over delta-lambda",
            "equals N times m. N is the total number of illuminated",
            "slits; m is the diffraction order. For a grating with 600",
            "grooves per millimetre, length 5 centimetres: N equals 600",
            "times 50 equals 30,000 slits. In first order, R equals",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p5.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The sodium D lines are the classic test: lambda-one equals",
            "589.0 nanometres and lambda-two equals 589.6 nanometres,",
            "separation 0.6 nanometres. Required resolving power equals",
            "589 over 0.6 equals 982. Our 30,000-groove grating easily",
            "resolves them in first order.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p6.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The free spectral range tells you the unambiguous wavelength",
            "range in each order. In order m, wavelength lambda and",
            "wavelength lambda plus delta-lambda-FSR produce maxima at",
            "the same angle if d sine theta equals m lambda equals m plus",
            "one times lambda plus delta-lambda-FSR. Solving:",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p7.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For the general grating equation including oblique",
            "incidence: d times sine theta-m minus sine theta-i equals m",
            "lambda. Here theta-i is the angle of incidence and theta-m",
            "is the diffraction angle, both measured from the grating",
            "normal.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

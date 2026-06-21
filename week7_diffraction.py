# week7_diffraction.py — Week 7 (paragraph-per-scene)
from manim import *
from utils import *

class Week7TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p1.mp3", time_offset=0)
        title = Text("Fraunhofer Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Diffraction is what happens when a wave encounters an obstacle",
            "or aperture whose size is comparable to the wavelength.",
            "Instead of casting a sharp shadow, the wave bends around the",
            "edges and spreads into the geometric shadow region.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p2.mp3", time_offset=0)
        title = Text("Fraunhofer Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Huygens' principle gives us the physical picture: every point",
            "on a wavefront acts as a new point source of secondary",
            "wavelets. The diffraction pattern is the interference pattern",
            "of all these secondary sources.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p3.mp3", time_offset=0)
        title = Text("Fraunhofer Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In the far field — the Fraunhofer regime — the intensity",
            "pattern of a single slit of width b is the famous sinc-squared",
            "function: I equals I naught times sine beta over beta squared,",
            "where beta equals pi b sine theta over lambda.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p4.mp3", time_offset=0)
        title = Text("Fraunhofer Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The central maximum is at theta equals zero and has twice the",
            "angular width of the secondary maxima. The dark fringes occur",
            "wherever b sine theta equals m lambda, for integer m.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p5.mp3", time_offset=0)
        title = Text("Fraunhofer Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a circular aperture of diameter D, the pattern is the Airy",
            "disk. The first dark ring occurs at sine theta equals 1.22",
            "lambda over D. This sets the fundamental resolution limit of",
            "any optical instrument with a circular aperture.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p6.mp3", time_offset=0)
        title = Text("Fraunhofer Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Rayleigh criterion states that two point sources are just",
            "resolved when the central maximum of one falls on the first",
            "dark ring of the other. The minimum resolvable angle is 1.22",
            "lambda over D.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p7.mp3", time_offset=0)
        title = Text("Fraunhofer Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A diffraction grating has N slits with spacing d. The N-slit",
            "interference pattern has extremely sharp principal maxima",
            "wherever d sine theta equals m lambda — the grating equation.",
            "At oblique incidence, this becomes d times sine theta_m minus",
            "sine theta_i equals m lambda.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p8.mp3", time_offset=0)
        title = Text("Fraunhofer Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power of a grating is R equals N times m — the",
            "number of slits times the diffraction order. The free spectral",
            "range is lambda over m. Higher order, higher resolution, but",
            "smaller unambiguous wavelength range.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p1.mp3", time_offset=0)
        title = Text("Huygens' Principle and Diffraction  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett opens Chapter 8 on diffraction with a profound",
            "statement: in a sense, diffraction is interference done",
            "correctly.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p2.mp3", time_offset=0)
        title = Text("Huygens' Principle and Diffraction  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In Young's double-slit experiment, we had two discrete point",
            "sources interfering. Huygens' principle generalises this:",
            "every point on a wavefront acts as a source of secondary",
            "spherical wavelets. The diffraction pattern is the",
            "interference sum of all these secondary sources across the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p3.mp3", time_offset=0)
        title = Text("Huygens' Principle and Diffraction  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When a wavefront encounters an aperture, only the wavelets",
            "from the open area contribute. Their superposition — with",
            "different path lengths to each observation point — produces",
            "the diffraction pattern.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p4.mp3", time_offset=0)
        title = Text("Huygens' Principle and Diffraction  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Fraunhofer approximation applies when both the source and",
            "the observation point are effectively at infinity — meaning",
            "the illumination and diffracted waves are both plane waves. In",
            "practice, this is achieved with lenses. The Fraunhofer",
            "condition requires the distance r to satisfy r much greater",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p5.mp3", time_offset=0)
        title = Text("Huygens' Principle and Diffraction  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a slit of width 0.1 millimetres illuminated at 500",
            "nanometres and observed at 1 metre, the minimum Fraunhofer",
            "distance is only 1 centimetre — so 1 metre is well into the",
            "Fraunhofer regime.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p1.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett Section 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The single-slit diffraction pattern is the starting point for",
            "understanding all diffraction phenomena. Bennett derives it",
            "carefully in Section 8.3.1 using the Fraunhofer diffraction",
            "integral — integrating the Huygens contributions from every",
            "point across the slit width.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p2.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett Section 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The result is the sinc-squared function: intensity equals",
            "I-naught times sine beta over beta, squared. The parameter",
            "beta equals pi b sine theta over lambda, where b is the slit",
            "width and theta is the diffraction angle.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p3.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett Section 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The central maximum is at theta equals zero, where sine beta",
            "over beta approaches one by L'Hopital's rule. It is the",
            "tallest and widest feature in the pattern.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p4.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett Section 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Dark minima occur wherever beta equals m pi — that is,",
            "wherever b sine theta equals m lambda for integer m not equal",
            "to zero. This has a beautiful physical interpretation: at",
            "these angles, the contributions from the top and bottom halves",
            "of the slit cancel exactly.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p5.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett Section 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key physical insight is the narrower the slit, the wider",
            "the diffraction pattern. This is the uncertainty principle in",
            "action — confining the wave in space forces it to spread out",
            "in angle.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p1.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Most optical systems — telescopes, microscopes, cameras, the",
            "human eye — have circular apertures. The diffraction pattern",
            "of a circular aperture is the Airy disk, named after George",
            "Biddell Airy who calculated it in 1835.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p2.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The pattern is described by the first-order Bessel function",
            "J-one, and the first dark ring occurs where the argument",
            "equals 3.832. This gives sine theta-one equals 1.22 lambda",
            "over D, where D is the aperture diameter.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p3.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The factor 1.22 — compared to 1.00 for a slit — comes entirely",
            "from the circular geometry and the Bessel function",
            "mathematics.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p4.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Rayleigh criterion defines the resolution limit: two point",
            "sources are just resolved when the central maximum of one",
            "falls exactly on the first dark ring of the other. The minimum",
            "resolvable angle is theta-min equals 1.22 lambda over D.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p5.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is a fundamental limit of wave optics — not an",
            "engineering limitation. To resolve finer details, you must",
            "either use a shorter wavelength or a larger aperture. There is",
            "no other way.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p6.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For the human eye with a 3 millimetre pupil, this gives about",
            "1 arcminute — which matches our measured visual acuity",
            "remarkably well. For the Hubble telescope with a 2.4 metre",
            "mirror, the limit is about 0.06 arcseconds — 800 times sharper",
            "than the eye.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p1.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett Sections 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A diffraction grating takes the principle of interference to",
            "its logical extreme — instead of two slits, it uses thousands.",
            "The result is an instrument of extraordinary spectral",
            "resolution.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p2.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett Sections 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The N-slit intensity pattern is a product of two terms: the",
            "single-slit diffraction envelope, which shapes the overall",
            "intensity, and the N-slit interference term, which creates",
            "sharp principal maxima wherever d sine theta equals m lambda.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p3.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett Sections 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The grating equation is the central formula: d times the",
            "quantity sine theta-m minus sine theta-i equals m lambda. Here",
            "d is the grating period, theta-i is the angle of the incoming",
            "beam, theta-m is the angle of the m-th order diffracted beam,",
            "and m is the diffraction order — zero, plus or minus one, plus",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p4.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett Sections 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "At normal incidence theta-i equals zero, and the equation",
            "simplifies to d sine theta-m equals m lambda.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p5.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett Sections 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The resolving power equals N times m — the number of slits",
            "times the diffraction order. This is why large gratings used",
            "in high orders can resolve wavelengths differing by less than",
            "a hundredth of a nanometre.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p6.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett Sections 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The free spectral range is lambda-minimum divided by m. It",
            "tells you the wavelength range you can measure unambiguously",
            "in order m before the next order overlaps.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

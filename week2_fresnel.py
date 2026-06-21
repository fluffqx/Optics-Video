# week2_fresnel.py
from manim import *
from utils import *

class Week2TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 2 covers what happens when a light wave reaches an",
            "interface between two different optical media. This is",
            "Bennett Chapter 3, and it is one of the most practically",
            "important topics in all of optics. Every lens surface, every",
            "mirror coating, every optical fibre, and every",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The central results are Snell's law and the Fresnel",
            "equations. Snell's law tells you the direction of the",
            "reflected and transmitted beams. The Fresnel equations tell",
            "you the amplitudes — how much electric field is reflected",
            "and how much is transmitted — and these depend on the angle",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "We also cover Brewster's angle, where the p-polarised",
            "component is completely transmitted with zero reflection,",
            "and total internal reflection, where all the light is",
            "reflected when the angle exceeds the critical angle. These",
            "phenomena are exploited in polarising beam splitters,",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "By the end of this week you must be able to: apply Snell's",
            "law to find refraction angles; compute Fresnel coefficients",
            "r-s, r-p, t-s, t-p for given angles and indices; compute",
            "reflectivity R and transmissivity T and verify R plus T",
            "equals 1; find Brewster's angle and the critical angle; and",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p1.mp3", time_offset=0)
        title = Text("What Happens at an Interface?  (Bennett 3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When a light wave reaches the boundary between two different",
            "media — glass and air, water and glass, any interface where",
            "the refractive index changes — some of the light is",
            "reflected and some is transmitted. This is true even for a",
            "boundary between two perfectly transparent materials. A",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p2.mp3", time_offset=0)
        title = Text("What Happens at an Interface?  (Bennett 3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The physics is determined entirely by Maxwell's boundary",
            "conditions at the interface. The electric field tangential",
            "to the surface must be continuous, and the magnetic field",
            "tangential to the surface must also be continuous, subject",
            "to the material properties. Applying these conditions to a",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p3.mp3", time_offset=0)
        title = Text("What Happens at an Interface?  (Bennett 3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "We separate the incident electric field into two independent",
            "polarisation components, because these interact differently",
            "with the interface. The s-polarisation has the electric",
            "field perpendicular to the plane of incidence. The",
            "p-polarisation has the electric field parallel to the plane",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p1.mp3", time_offset=0)
        title = Text("Fermat Principle  (Bennett Section 3.2.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Before deriving the Fresnel equations, let's understand",
            "Snell's law at a deeper level through Fermat's principle.",
            "Fermat's principle states that light travels between two",
            "points along the path that requires the least time — or more",
            "precisely, along the path where the travel time is",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p2.mp3", time_offset=0)
        title = Text("Fermat Principle  (Bennett Section 3.2.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For reflection from a flat surface, Fermat's principle",
            "immediately gives the law of reflection: the angle of",
            "incidence equals the angle of reflection. Any other path",
            "from source to surface to detector would take longer. The",
            "proof is a simple calculus problem: minimise the total path",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p3.mp3", time_offset=0)
        title = Text("Fermat Principle  (Bennett Section 3.2.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For refraction, the same principle applies but now the light",
            "travels at different speeds in the two media. The optimal",
            "path — the one that minimises travel time — bends at the",
            "interface. The bending angle is determined by the ratio of",
            "the speeds in the two media, which equals the ratio of the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p4.mp3", time_offset=0)
        title = Text("Fermat Principle  (Bennett Section 3.2.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Fermat's principle is more than a clever trick for deriving",
            "Snell's law. It is a profound variational principle that",
            "reveals a deep connection between optics and mechanics.",
            "Hamilton showed that classical mechanics can be formulated",
            "in an analogous way — particles follow paths that minimise",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p1.mp3", time_offset=0)
        title = Text("Reflection and Snell Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The law of reflection is simple: the angle of incidence",
            "equals the angle of reflection. Both angles are measured",
            "from the surface normal — the line perpendicular to the",
            "surface at the point of contact. The incident ray, the",
            "reflected ray, and the surface normal all lie in the same",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p2.mp3", time_offset=0)
        title = Text("Reflection and Snell Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Snell's law governs refraction — the bending of a",
            "transmitted beam at an interface. If n-i is the refractive",
            "index of the incident medium and n-t is the index of the",
            "transmitted medium, with theta-i and theta-t the angles from",
            "the normal, then n-i times sine theta-i equals n-t times",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p3.mp3", time_offset=0)
        title = Text("Reflection and Snell Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When light goes from a lower-index medium to a higher-index",
            "medium — like from air into glass — theta-t is smaller than",
            "theta-i. The refracted beam bends toward the normal. When",
            "light goes from higher to lower index, the refracted beam",
            "bends away from the normal and theta-t is larger than",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p4.mp3", time_offset=0)
        title = Text("Reflection and Snell Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "One important conceptual point: the frequency of light does",
            "not change when it crosses an interface. The wavelength",
            "changes — it equals lambda-vacuum divided by n in the medium",
            "— but the frequency is fixed by the source. This is required",
            "by the boundary conditions: the electromagnetic fields on",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p5.mp3", time_offset=0)
        title = Text("Reflection and Snell Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through a complete example. Light in glass with",
            "n-i equals 1.5, hitting a glass-to-air interface, with",
            "theta-i equals 30 degrees. Snell's law gives 1.5 times sine",
            "30 equals 1.0 times sine theta-t. One point five times zero",
            "point five equals 0.75. So sine theta-t equals 0.75, and",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p6.mp3", time_offset=0)
        title = Text("Reflection and Snell Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Now increase the incident angle to 40 degrees: 1.5 times",
            "sine 40 equals 1.5 times 0.6428 equals 0.9642. So sine",
            "theta-t equals 0.9642, and theta-t equals 74.6 degrees. The",
            "refracted beam is nearly grazing the surface.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p7.mp3", time_offset=0)
        title = Text("Reflection and Snell Law  (Bennett 3.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "And at 41.8 degrees: 1.5 times sine 41.8 equals 1.5 times",
            "0.6667 equals 1.000. But sine theta-t cannot exceed one.",
            "There is no real solution — total internal reflection",
            "occurs. The critical angle for glass to air is arcsin of 1",
            "over 1.5, which is 41.8 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p1.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett derives the Fresnel equations in Section 3.3 by",
            "applying Maxwell's boundary conditions at a planar interface",
            "between two dielectric media with refractive indices n-i and",
            "n-t.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p2.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The starting point is Maxwell's equations at an interface,",
            "derived in Section 3.3.1. The boundary conditions require",
            "that the tangential components of both E and H must be",
            "continuous across the interface. There are no free currents",
            "or surface charges at a dielectric interface, so these",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p3.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "We separate the analysis into two polarisation cases. The",
            "s-polarisation, also called TE, has the electric field",
            "perpendicular to the plane of incidence. The p-polarisation,",
            "also called TM, has the electric field parallel to the plane",
            "of incidence. Bennett works through s-polarisation in",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p4.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For s-polarisation: the tangential E is the full field",
            "(since E is already tangential). Continuity of tangential E",
            "gives E-i plus E-r equals E-t. Continuity of tangential H —",
            "using H equals n E over mu-naught c and the geometry — gives",
            "n-i times cosine theta-i times E-i minus E-r equals n-t",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p5.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For p-polarisation: only the component of E tangential to",
            "the surface is continuous. The geometry introduces extra",
            "cosine factors. Continuity of tangential E gives E-i minus",
            "E-r times cosine theta-i equals E-t times cosine theta-t.",
            "Continuity of tangential H gives n-i times E-i plus E-r",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p6.mp3", time_offset=0)
        title = Text("Fresnel Derivation  (Bennett Section 3.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The derivation confirms a key physical point: the s and p",
            "components interact differently with the interface because",
            "their electric field orientations relative to the surface",
            "normal are different.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p1.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Snell's law tells us directions. The Fresnel equations tell",
            "us amplitudes — how much of the incident electric field is",
            "reflected and how much is transmitted at an interface.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p2.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key insight is that polarisation matters at an",
            "interface. We split the incident electric field into two",
            "independent components. S-polarisation, also called TE or",
            "transverse electric, has the electric field perpendicular to",
            "the plane of incidence. P-polarisation, also called TM or",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p3.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For s-polarisation, the reflection amplitude coefficient is",
            "r-perp equals n-i cosine theta-i minus n-t cosine theta-t,",
            "all divided by n-i cosine theta-i plus n-t cosine theta-t.",
            "The transmission amplitude coefficient is t-perp equals 2",
            "n-i cosine theta-i, divided by n-i cosine theta-i plus n-t",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p4.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For p-polarisation, the reflection amplitude coefficient is",
            "r-parallel equals n-t cosine theta-i minus n-i cosine",
            "theta-t, divided by n-t cosine theta-i plus n-i cosine",
            "theta-t. The transmission amplitude coefficient is",
            "t-parallel equals 2 n-i cosine theta-i, divided by n-t",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p5.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "At normal incidence, theta-i and theta-t are both zero, and",
            "both polarisations give the same result: r equals n-i minus",
            "n-t, divided by n-i plus n-t. This is the most important",
            "special case and you must know it immediately. For air to",
            "glass with n-t equals 1.5: r equals 1 minus 1.5 divided by 1",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p6.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The energy reflectivity R is the square of the amplitude",
            "coefficient: R equals r squared. For our air-to-glass",
            "example at normal incidence: R equals 0.04, meaning four",
            "percent of the incident energy is reflected. The energy",
            "transmissivity T satisfies R plus T equals one, so T equals",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p7.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through the full calculation for air to glass",
            "with n-i equals 1.0, n-t equals 1.5, at theta-i equals 40",
            "degrees. Snell's law first: sine theta-t equals 1.0 over 1.5",
            "times sine 40 equals 0.4285, so theta-t equals 25.37",
            "degrees. Now the cosines: cosine 40 equals 0.766, cosine",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p8.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "S-polarisation: r-perp equals 0.766 minus 1.5 times 0.9036",
            "over 0.766 plus 1.5 times 0.9036 equals 0.766 minus 1.355",
            "over 0.766 plus 1.355 equals minus 0.589 over 2.121 equals",
            "minus 0.278. R-perp equals 0.277 squared equals 0.0771,",
            "about 7.7 percent reflected.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p9.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "P-polarisation: r-parallel equals 1.5 times 0.766 minus 1.0",
            "times 0.9036 over 1.5 times 0.766 plus 1.0 times 0.9036",
            "equals 1.149 minus 0.904 over 1.149 plus 0.904 equals 0.245",
            "over 2.053 equals plus 0.119. R-parallel equals 0.119",
            "squared equals 0.0142, about 1.4 percent reflected.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p10.mp3", time_offset=0)
        title = Text("The Fresnel Equations  (Bennett Section 3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The p-polarisation reflects significantly less than",
            "s-polarisation at this angle. This difference increases",
            "until Brewster's angle, where r-parallel equals zero exactly",
            "— we will derive this next.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p1.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through a complete Fresnel calculation following",
            "Bennett Section 3.5.4. Incident medium: air, n-i equals",
            "1.000. Transmitted medium: glass, n-t equals 1.500. Angle of",
            "incidence: theta-i equals 40 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p2.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 1: Snell's law for the refracted angle. Sine theta-t",
            "equals n-i over n-t times sine theta-i equals 1.000 over",
            "1.500 times sine 40 degrees equals 0.4285. Therefore theta-t",
            "equals 25.37 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p3.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 2: Compute cosines. Cosine theta-i equals cosine 40",
            "degrees equals 0.7660. Cosine theta-t equals cosine 25.37",
            "degrees equals 0.9036.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p4.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 3: s-polarisation Fresnel coefficient. r-s equals n-i",
            "cosine theta-i minus n-t cosine theta-t, over n-i cosine",
            "theta-i plus n-t cosine theta-t, equals 0.7660 minus 1.5",
            "times 0.9036, over 0.7660 plus 1.5 times 0.9036, equals",
            "0.7660 minus 1.3554 over 0.7660 plus 1.3554, equals minus",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p5.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 4: p-polarisation Fresnel coefficient. r-p equals n-t",
            "cosine theta-i minus n-i cosine theta-t, over n-t cosine",
            "theta-i plus n-i cosine theta-t, equals 1.5 times 0.7660",
            "minus 1.0 times 0.9036, over 1.5 times 0.7660 plus 1.0 times",
            "0.9036, equals 1.1490 minus 0.9036 over 1.1490 plus 0.9036,",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p6.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 5: check with R plus T equals 1. T-s equals 1 minus",
            "0.0772 equals 0.9228. T-p equals 1 minus 0.0143 equals",
            "0.9857. Both satisfy energy conservation. The p-polarisation",
            "reflects much less than s at this angle — it is approaching",
            "Brewster's angle.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p1.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Fresnel amplitude coefficients r and t give the ratio of",
            "electric field amplitudes. To find the fraction of energy",
            "that is reflected and transmitted, we need the energy",
            "coefficients.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p2.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The reflectivity R is simply the square of the amplitude",
            "reflection coefficient: R equals r squared. This follows",
            "because irradiance is proportional to the square of the",
            "electric field amplitude, and the beam geometry is unchanged",
            "on reflection.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p3.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The transmissivity T is not simply t squared. When a beam",
            "refracts at an interface, its cross-section changes and the",
            "wave speed changes, and we must account for both. The",
            "correct expression is T equals n-t cosine theta-t over n-i",
            "cosine theta-i, times t squared. The factor n-t cosine",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p4.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Energy conservation requires R plus T equals one. This is an",
            "excellent sanity check for any Fresnel calculation — if your",
            "R and T do not add to one, you have made an error somewhere.",
            "Verify this for normal incidence with n-i equals one and n-t",
            "equals 1.5: r equals minus one-fifth, so R equals one",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p5.mp3", time_offset=0)
        title = Text("Reflectivity and Transmissivity  (Bennett 3.6)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a multilayer optical system like a camera lens with six",
            "or eight glass-air interfaces, the reflectivity at each",
            "surface compounds: if each surface reflects four percent,",
            "then after ten surfaces the transmitted fraction is 0.96 to",
            "the power ten, which is approximately 0.665 — only 66.5",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p1.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Brewster's angle is the angle of incidence at which the",
            "p-polarised component has zero reflectivity — it is",
            "completely transmitted. At this special angle, the reflected",
            "beam consists entirely of s-polarised light.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p2.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The formula is simple: tangent theta-B equals n-t over n-i.",
            "For air to glass with n-t equals 1.5: theta-B equals arctan",
            "of 1.5, which gives 56.31 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p3.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The physical explanation is elegant. At Brewster's angle,",
            "the reflected ray and the refracted ray are exactly",
            "perpendicular to each other: theta-B plus theta-t equals 90",
            "degrees. The p-polarised electric field oscillates in the",
            "plane of incidence, which means it oscillates in the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p4.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Applications: laser Brewster windows. Lasers with Brewster",
            "windows have their gain medium bounded by glass plates",
            "tilted at Brewster's angle. P-polarised light passes through",
            "without any reflection loss, so the laser naturally selects",
            "p-polarisation and lases with essentially zero cavity loss",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p5.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Total internal reflection occurs when light tries to",
            "propagate from a denser medium into a rarer one, at an angle",
            "of incidence exceeding the critical angle theta-c. The",
            "critical angle is given by sine theta-c equals n-t over n-i,",
            "where n-i is greater than n-t.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p6.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "At exactly the critical angle, the refracted beam travels",
            "parallel to the interface. Beyond the critical angle,",
            "Snell's law gives a sine of theta-t greater than one, for",
            "which there is no real solution. The refracted beam does not",
            "exist — all the energy is reflected. The reflectivity jumps",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p7.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For glass with n equals 1.5 to air: sine theta-c equals 1",
            "over 1.5, so theta-c equals 41.81 degrees. For diamond with",
            "n equals 2.42: theta-c equals 24.41 degrees — even steeper,",
            "which is why diamond sparkles so brilliantly. Light entering",
            "the diamond undergoes total internal reflection many times",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p8.mp3", time_offset=0)
        title = Text("Brewster Angle and TIR  (Bennett 3.5.2-3.5.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Optical fibres use total internal reflection to guide light.",
            "The core has index n-core and the cladding has index n-clad,",
            "where n-core is greater than n-clad. Light propagating at a",
            "sufficiently shallow angle to the fibre axis hits the",
            "core-cladding boundary beyond the critical angle and is",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p1.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Malus's law describes what happens to the intensity of",
            "linearly polarised light when it passes through a linear",
            "polariser. It is one of the most fundamental results",
            "involving polarised light and is widely used in optical",
            "instruments.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p2.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The setup: a beam of linearly polarised light with intensity",
            "I-naught and polarisation direction making angle theta with",
            "the transmission axis of the polariser. The transmitted",
            "intensity is I-naught times cosine squared theta. This is",
            "Malus's law.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p3.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The physical origin is simple. The polariser transmits only",
            "the component of the electric field along its transmission",
            "axis. If the field amplitude is E-naught and the angle",
            "between the field and the transmission axis is theta, then",
            "the transmitted field amplitude is E-naught cosine theta.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p4.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "At theta equals zero — polarisations aligned — cosine",
            "squared is one and full intensity is transmitted. At theta",
            "equals 90 degrees — polarisations crossed — cosine squared",
            "is zero and no light passes. At theta equals 45 degrees,",
            "cosine squared is one half and half the intensity is",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p5.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "An important exam question type: three polarisers in",
            "sequence. Unpolarised light with intensity I-naught enters a",
            "horizontal polariser, then a polariser at 45 degrees, then a",
            "vertical polariser. What intensity exits?",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p6.mp3", time_offset=0)
        title = Text("Malus Law  (Bennett Section 6.2.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "After the first polariser: I-naught over 2 (unpolarised",
            "light through any polariser gives half the intensity). After",
            "the second polariser at 45 degrees to the first: I-naught",
            "over 2 times cosine squared 45 equals I-naught over 4. After",
            "the third polariser at 90 degrees to the second: I-naught",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

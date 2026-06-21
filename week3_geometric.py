# week3_geometric.py
from manim import *
from utils import *

class Week3TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 3 is geometric optics — the ray approximation to wave",
            "propagation that applies when all apertures are much larger",
            "than the wavelength. This follows Bennett Chapter 4 closely.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week3TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Geometric optics is not an approximation to be embarrassed",
            "about. It correctly describes every camera lens, every",
            "telescope, every microscope objective, every pair of",
            "eyeglasses, and the optics of the human eye. The thin lens",
            "equation, the mirror equation, and the lensmaker's formula",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week3TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The most critical skill in this week is sign conventions.",
            "Every student who makes a significant error in a geometric",
            "optics exam problem makes a sign error. We establish the",
            "conventions carefully and apply them consistently to every",
            "example.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week3TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "By the end of this week you must be able to: apply the thin",
            "lens equation to find image position and magnification; use",
            "the lensmaker's equation to relate focal length to lens",
            "geometry; draw ray diagrams with three principal rays; solve",
            "two-lens combination problems step by step; compute the",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett Section 4.1-4.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Geometric optics, also called ray optics, applies when the",
            "wavelength of light is much smaller than all the apertures,",
            "obstacles, and optical elements in the system. Under this",
            "condition, we can treat light as travelling in straight",
            "lines called rays. The ray is always perpendicular to the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett Section 4.1-4.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Bennett Section 4.1 notes that the paraxial approximation",
            "further simplifies the analysis. We restrict attention to",
            "rays that make small angles with the optical axis — the",
            "central axis of the system. For small angles theta in",
            "radians, we replace sin theta by theta and cos theta by one.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett Section 4.1-4.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The paraxial approximation is not just a mathematical",
            "convenience — it corresponds to the regime where real",
            "optical instruments are designed to operate. Camera lenses,",
            "microscope objectives, and telescope primaries are all",
            "optimised for paraxial rays. The aberrations that degrade",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p4.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett Section 4.1-4.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Geometric optics fails when the aperture becomes comparable",
            "to the wavelength — then diffraction effects become",
            "important, and we need the full wave theory of Week 7. But",
            "for apertures larger than a few wavelengths, geometric",
            "optics is an excellent and exact approximation within its",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p5.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett Section 4.1-4.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key concept of the optical path length from Bennett",
            "Section 4.2: the optical path length equals n times the",
            "geometric distance travelled. This quantity determines phase",
            "and is what enters Fermat's principle and the interference",
            "and diffraction calculations of Weeks 6 and 7.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p1.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett Section 4.3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Sign conventions are the most important technical details in",
            "geometric optics. Getting a sign wrong gives a completely",
            "wrong answer — the magnitude might be right but the physical",
            "interpretation is opposite. These conventions are not",
            "arbitrary: they follow a consistent logic that makes the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p2.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett Section 4.3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "All distances are measured from the optical element — the",
            "lens, mirror, or refracting surface. Positive distances are",
            "in the direction of light propagation; negative distances",
            "are against it.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p3.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett Section 4.3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The object distance s-o is positive for a real object,",
            "located on the incoming side of the element. It is negative",
            "for a virtual object, which occurs when a converging beam is",
            "intercepted before reaching its focus. Real objects always",
            "have positive s-o in the standard single-element geometry.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p4.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett Section 4.3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The image distance s-i is positive for a real image, formed",
            "on the far side of the element where light actually",
            "converges. It is negative for a virtual image, formed on the",
            "same side as the incoming light. You cannot project a",
            "virtual image onto a screen — it exists only as diverging",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p5.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett Section 4.3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The radius of curvature R is positive if the centre of",
            "curvature is to the right of the surface — in the direction",
            "of light propagation. A convex lens surface curving toward",
            "the light source has R positive on the first surface and R",
            "negative on the second surface. For a biconvex lens: R-one",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p6.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett Section 4.3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For mirrors, the sign convention reverses: positive is now",
            "toward the incoming light, because after reflection light",
            "travels back the way it came. A concave mirror — which",
            "converges light — has a positive focal length. A convex",
            "mirror — which diverges light — has negative focal length.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p7.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett Section 4.3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The magnification m equals minus s-i over s-o. A negative",
            "magnification means the image is inverted relative to the",
            "object. A magnification with absolute value greater than one",
            "means the image is larger than the object. A real image",
            "always has negative magnification if the object is real —",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p8.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett Section 4.3.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Always draw a ray diagram first. Use three principal rays:",
            "one parallel to the axis (passes through far focal point",
            "after refraction), one through the near focal point (emerges",
            "parallel to axis after refraction), and one through the",
            "optical centre (passes straight through). Where these three",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SphericalSurface_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p1.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A single curved interface between two transparent media is",
            "the fundamental building block of lens design. Bennett",
            "derives the spherical surface equation in Section 4.3.3.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SphericalSurface_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p2.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Consider a spherical surface of radius R centred at point C,",
            "separating medium with index n-i on the left from medium",
            "with index n-t on the right. Positive R means the centre of",
            "curvature is to the right — on the transmitted side — which",
            "corresponds to a convex surface for a lens element.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SphericalSurface_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p3.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The refraction equation for a single spherical surface is:",
            "n-i over s-o plus n-t over s-i equals n-t minus n-i, all",
            "divided by R. Here s-o is the object distance and s-i is the",
            "image distance, both measured from the vertex of the",
            "surface.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SphericalSurface_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p4.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "At normal incidence, a flat surface has R going to infinity",
            "and the equation becomes n-i over s-o plus n-t over s-i",
            "equals zero. This gives s-i equals minus n-t over n-i times",
            "s-o. For an object at depth s-o in water with n-i equals",
            "1.33, viewed from air with n-t equals 1.00: s-i equals minus",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SphericalSurface_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p5.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a convex glass surface with R equals 10 centimetres, n-i",
            "equals 1.00 air, n-t equals 1.50 glass, and an object 30",
            "centimetres in front: 1.00 over 30 plus 1.50 over s-i equals",
            "0.50 over 10 equals 0.050. Solving: 1.50 over s-i equals",
            "0.050 minus 0.0333 equals 0.0167. s-i equals 90 centimetres",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p1.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The thin lens equation is the central formula of geometric",
            "optics: one over s-o plus one over s-i equals one over f.",
            "Here s-o is the object distance, s-i is the image distance,",
            "and f is the focal length of the lens.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p2.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The focal length f is determined by the lens geometry and",
            "material through the lensmaker's equation: one over f equals",
            "the quantity n-l minus n-m, times the quantity one over",
            "R-one minus one over R-two. Here n-l is the refractive index",
            "of the lens glass, n-m is the index of the surrounding",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p3.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In air with n-m equals one, the lensmaker's equation",
            "simplifies to one over f equals n-l minus one, times one",
            "over R-one minus one over R-two. For a biconvex lens with",
            "R-one equals R equals positive R and R-two equals negative",
            "R: one over R-one minus one over R-two equals one over R",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p4.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The dioptric power P equals one over f in dioptres.",
            "Ophthalmologists prescribe glasses in dioptres. A person",
            "needing one over 0.5 equals plus 2 dioptres to read means",
            "they need a converging lens of focal length 50 centimetres.",
            "Distance glasses for myopia have negative power — diverging",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p5.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For lenses in contact, powers add: P-total equals P-one plus",
            "P-two. This is why you can combine eyeglass prescriptions",
            "additively.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p6.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Now a complete worked example. Biconvex lens: R-one equals",
            "plus 20 centimetres, R-two equals minus 20 centimetres, n-l",
            "equals 1.50, in air. Object at s-o equals 60 centimetres.",
            "Find s-i and m.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p7.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step one: lensmaker's equation. One over f equals 1.50 minus",
            "1.00 times one over 0.20 minus one over minus 0.20, equals",
            "0.50 times 5 plus 5 equals 0.50 times 10 equals 5. So f",
            "equals 0.20 metres equals 20 centimetres.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p8.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step two: thin lens equation. One over s-i equals one over f",
            "minus one over s-o equals one over 20 minus one over 60",
            "equals 3 over 60 minus 1 over 60 equals 2 over 60. So s-i",
            "equals 30 centimetres. Positive — real image on the far side",
            "of the lens.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p9.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step three: magnification. m equals minus s-i over s-o",
            "equals minus 30 over 60 equals minus 0.5. Inverted (negative",
            "sign) and half the size (absolute value one-half). This is",
            "the geometry of a simple projector or camera.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p10.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Now vary the object distance. Put the object at s-o equals",
            "30 centimetres, which equals 1.5 f: one over s-i equals one",
            "over 20 minus one over 30 equals 3 over 60 minus 2 over 60",
            "equals 1 over 60. s-i equals 60 centimetres. m equals minus",
            "60 over 30 equals minus 2. Real, inverted, twice the size.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p11.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Now put the object at s-o equals 10 centimetres, inside the",
            "focal length: one over s-i equals one over 20 minus one over",
            "10 equals 1 over 20 minus 2 over 20 equals minus 1 over 20.",
            "s-i equals minus 20 centimetres. Virtual image on the same",
            "side as the object. m equals minus minus 20 over 10 equals",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p1.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Spherical mirrors obey an equation that is structurally",
            "identical to the thin lens equation. Bennett derives the",
            "mirror equation in Section 4.3.2 starting from the geometry",
            "of reflection at a spherical surface.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p2.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The mirror equation is one over s-o plus one over s-i equals",
            "two over R equals one over f-m. Here f-m equals R over two",
            "is the focal length of the mirror. The sign convention: for",
            "mirrors, positive distances are measured toward the incoming",
            "light, which reverses the usual convention used for lenses.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p3.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A concave mirror converges light and has a positive focal",
            "length. The centre of curvature is on the same side as the",
            "incoming light, giving positive R by the mirror convention.",
            "A convex mirror diverges light and has a negative focal",
            "length.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p4.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Worked example: concave mirror with R equals 40 centimetres,",
            "so f-m equals 20 centimetres. Object at s-o equals 60",
            "centimetres. One over s-i equals one over 20 minus one over",
            "60 equals 3 over 60 minus 1 over 60 equals 2 over 60.",
            "Therefore s-i equals 30 centimetres — real image in front of",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p5.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "If the object is at s-o equals 10 centimetres, inside the",
            "focal length: one over s-i equals one over 20 minus one over",
            "10 equals minus 1 over 20. s-i equals minus 20 centimetres —",
            "behind the mirror. Virtual, upright, magnified by factor 2.",
            "This is the operating principle of a shaving or makeup",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p6.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Concave mirrors are used as primary mirrors in reflecting",
            "telescopes because they avoid chromatic aberration — mirrors",
            "reflect all wavelengths identically, unlike lenses. Convex",
            "mirrors are used as rear-view mirrors and security mirrors",
            "for their wide field of view.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p1.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For two thin lenses separated by distance d, Bennett Section",
            "4.4 gives the procedure: apply the thin lens equation to the",
            "first lens to find its image, then use that image as the",
            "object for the second lens.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p2.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "If the first lens has focal length f-one and the object is",
            "at distance s-o-one, then s-i-one satisfies one over s-o-one",
            "plus one over s-i-one equals one over f-one. The object",
            "distance for the second lens is s-o-two equals d minus",
            "s-i-one. If s-i-one is greater than d — the first image",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p3.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Apply the thin lens equation to the second lens: one over",
            "s-o-two plus one over s-i-two equals one over f-two. The",
            "total magnification is m-total equals m-one times m-two",
            "equals minus s-i-one over s-o-one times minus s-i-two over",
            "s-o-two.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p4.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For lenses in contact with d equals zero, the effective",
            "focal length satisfies one over f-eff equals one over f-one",
            "plus one over f-two, which is equivalent to P-eff equals",
            "P-one plus P-two. The powers add directly. This is why",
            "optometrists write prescriptions in dioptres — combining",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p5.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For two lenses separated by distance d, Bennett gives the",
            "general formula: one over f-eff equals one over f-one plus",
            "one over f-two minus d over f-one f-two. The last term is",
            "the correction for separation. For two identical converging",
            "lenses each of focal length f separated by d equals f, we",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class OpticalInstruments_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p1.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "All optical instruments reduce to combinations of lenses and",
            "mirrors. Understanding the operating principle of each one",
            "clarifies the optical design choices.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class OpticalInstruments_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p2.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A magnifying glass uses a single converging lens to create a",
            "virtual, upright, magnified image of an object placed just",
            "inside the focal length. The angular magnification is 25",
            "centimetres divided by f, where 25 centimetres is the",
            "conventional near-point distance. A 5-centimetre focal",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class OpticalInstruments_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p3.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A compound microscope uses two lenses: a short-focal-length",
            "objective and a longer-focal-length eyepiece. The objective",
            "forms a real, inverted, highly magnified intermediate image.",
            "The eyepiece then acts as a simple magnifier for that",
            "intermediate image. The total angular magnification is M",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class OpticalInstruments_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p4.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "An astronomical refracting telescope has a long-focal-length",
            "objective and a short-focal-length eyepiece, separated by",
            "f-objective plus f-eyepiece. Parallel light from a distant",
            "star enters and the objective forms a real image at its back",
            "focal point. The eyepiece magnifies this image. The angular",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class OpticalInstruments_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p5.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The human eye has a total focal length of about 22",
            "millimetres in air and can focus objects from 25 centimetres",
            "to infinity by changing the shape of its crystalline lens.",
            "The retina is a curved photosensitive surface 22 millimetres",
            "from the optical system. Nearsightedness (myopia) means the",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

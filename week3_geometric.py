# week3_geometric.py — paragraph-per-scene
from manim import *
from utils import *

class Week3TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "Week 3 is geometric optics — the regime where the wavelength",
            "of light is so small compared to the optical elements that",
            "we can treat light as rays travelling in straight lines.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week3TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "This approximation is remarkably powerful. It describes",
            "lenses, mirrors, microscopes, telescopes, cameras, and the",
            "human eye with great accuracy. The thin lens equation and",
            "the mirror equation are the workhorses of optical",
            "engineering.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week3TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = txt_block([
            "The most important lesson of this week is sign conventions.",
            "They seem tedious, but getting a sign wrong in a geometric",
            "optics problem means getting the completely wrong answer. We",
            "will establish them carefully and check them on every",
            "example.",
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Geometric Optics and the Paraxial Approximation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Geometric optics applies when the wavelength of light is",
            "much smaller than all the apertures, lenses, and optical",
            "elements in the system. Under this condition, diffraction",
            "effects are negligible and we can treat light as travelling",
            "in straight lines called rays. The ray is perpendicular to",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Geometric Optics and the Paraxial Approximation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The paraxial approximation further simplifies the analysis.",
            "We consider only rays that travel at small angles to the",
            "optical axis — the main axis of the optical system. For",
            "small angles theta in radians, sine theta approximately",
            "equals theta and cosine theta approximately equals one. This",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Geometric Optics and the Paraxial Approximation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The domain of geometric optics covers most of everyday",
            "optics: eyeglasses, camera lenses, binoculars, telescopes,",
            "microscopes, projectors. It breaks down when apertures",
            "become comparable to the wavelength — which brings us to",
            "diffraction in Week 7 — and when coherence effects matter —",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SignConventions_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p1.mp3", time_offset=0)
        title = Text("Sign Conventions — CRITICAL", font_size=36, color=GOLD)
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
        title = Text("Sign Conventions — CRITICAL", font_size=36, color=GOLD)
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
        title = Text("Sign Conventions — CRITICAL", font_size=36, color=GOLD)
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
        title = Text("Sign Conventions — CRITICAL", font_size=36, color=GOLD)
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
        title = Text("Sign Conventions — CRITICAL", font_size=36, color=GOLD)
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
        title = Text("Sign Conventions — CRITICAL", font_size=36, color=GOLD)
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
        title = Text("Sign Conventions — CRITICAL", font_size=36, color=GOLD)
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
        title = Text("Sign Conventions — CRITICAL", font_size=36, color=GOLD)
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
        title = Text("Refraction at a Spherical Surface", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A single curved interface between two media refracts light",
            "according to the spherical surface equation: n-i over s-o",
            "plus n-t over s-i equals n-t minus n-i, all divided by R.",
            "Here R is the radius of curvature of the surface, positive",
            "if the centre is on the transmitted side.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SphericalSurface_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p2.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This equation is derived by applying Snell's law in the",
            "paraxial approximation to a ray hitting the surface at a",
            "small angle. The paraxial approximation replaces sine theta",
            "with theta and cosine theta with one, which linearises",
            "everything.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SphericalSurface_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p3.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a flat surface with R going to infinity, the equation",
            "reduces to n-i over s-o plus n-t over s-i equals zero, or",
            "s-i equals minus n-t over n-i times s-o. The image of an",
            "object in water viewed from air appears at a different depth",
            "from the actual object — this is why a pool appears",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ThinLensScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p1.mp3", time_offset=0)
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
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
        title = Text("Spherical Mirrors", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Spherical mirrors obey the mirror equation: one over s-o",
            "plus one over s-i equals two over R equals one over f-m,",
            "where f-m equals R over two is the focal length of the",
            "mirror.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p2.mp3", time_offset=0)
        title = Text("Spherical Mirrors", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is identical in form to the thin lens equation. The",
            "sign convention for mirrors: positive distances are on the",
            "same side as the incoming light. A concave mirror curves",
            "toward the light and has R positive, giving a positive focal",
            "length — it is converging. A convex mirror curves away from",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p3.mp3", time_offset=0)
        title = Text("Spherical Mirrors", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a concave mirror with f-m equals 20 centimetres and",
            "object at s-o equals 60 centimetres: one over s-i equals one",
            "over 20 minus one over 60 equals 2 over 60, so s-i equals 30",
            "centimetres. Real image in front of the mirror.",
            "Magnification m equals minus 30 over 60 equals minus",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MirrorScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p4.mp3", time_offset=0)
        title = Text("Spherical Mirrors", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Concave mirrors are used in reflecting telescopes — the",
            "primary mirror focuses starlight to form a real image. They",
            "are also used in car headlights in reverse: a light source",
            "at the focal point produces a parallel reflected beam.",
            "Convex mirrors are used as rear-view mirrors and security",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p1.mp3", time_offset=0)
        title = Text("Lens Combinations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When two lenses are used in sequence, the image formed by",
            "the first lens serves as the object for the second lens. You",
            "apply the thin lens equation twice.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p2.mp3", time_offset=0)
        title = Text("Lens Combinations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For two thin lenses separated by distance d, the first image",
            "is at distance s-i-one from the first lens. The second",
            "object distance is s-o-two equals d minus s-i-one — the",
            "separation minus the first image distance. If s-i-one is",
            "greater than d, the first image falls beyond the second",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p3.mp3", time_offset=0)
        title = Text("Lens Combinations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The effective focal length of the two-lens system satisfies:",
            "one over f-effective equals one over f-one plus one over",
            "f-two minus d over f-one f-two. In the contact limit where d",
            "goes to zero, this simplifies to one over f-effective equals",
            "one over f-one plus one over f-two, or equivalently",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class LensCombinations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p4.mp3", time_offset=0)
        title = Text("Lens Combinations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The total magnification of a two-lens system is the product",
            "of the individual magnifications: m-total equals m-one times",
            "m-two. This multiplicative property is what makes compound",
            "microscopes so powerful — two lenses each providing large",
            "magnification multiply their effects.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class OpticalInstruments_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p1.mp3", time_offset=0)
        title = Text("Optical Instruments", font_size=40, color=GOLD)
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
        title = Text("Optical Instruments", font_size=40, color=GOLD)
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
        title = Text("Optical Instruments", font_size=40, color=GOLD)
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
        title = Text("Optical Instruments", font_size=40, color=GOLD)
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
        title = Text("Optical Instruments", font_size=40, color=GOLD)
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

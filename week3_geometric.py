# week3_geometric.py — Week 3: Geometric Optics (paragraph-per-scene)
from manim import *
from utils import *

class Week3TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([            "Week 3 takes us into geometric optics — the regime where the",
            "wavelength of light is much smaller than the optical elements",
            "we're dealing with. In this limit, we can treat light as rays",
            "travelling in straight lines, and ignore diffraction entirely.",])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week3TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([            "This approximation works beautifully for lenses, mirrors,",
            "telescopes, and microscopes. It breaks down when apertures",
            "become comparable to the wavelength — which is when",
            "diffraction becomes important, and we'll return to that in",
            "week 7.",])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week3TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([            "The key mathematical tool is the paraxial approximation: for",
            "small angles, sine theta is approximately equal to tangent",
            "theta, which is approximately equal to theta in radians. This",
            "linearises all the equations and makes them analytically",
            "tractable.",])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week3TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([            "Sign conventions are absolutely critical in geometric optics.",
            "Getting a sign wrong means getting the wrong answer. Always",
            "measure distances from the optical element. Object distance is",
            "positive for real objects on the incoming side. Image distance",
            "is positive for real images on the outgoing side. Radius of",])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Geometric Optics and Paraxial Approximation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Geometric optics applies when the wavelength of light is much",
            "smaller than the optical elements it encounters. In this",
            "limit, we can ignore diffraction entirely and treat light as",
            "rays — straight lines that carry energy in a specific",
            "direction.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Geometric Optics and Paraxial Approximation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The paraxial approximation further simplifies things: for rays",
            "that stay close to and nearly parallel to the optical axis,",
            "sine theta is approximately equal to theta in radians. This",
            "linearises all the equations, making analytic solutions",
            "possible.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class GeometricOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Geometric Optics and Paraxial Approximation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Geometric optics describes lenses, mirrors, telescopes,",
            "microscopes, cameras, the human eye, and optical fibres — an",
            "enormous range of practical applications built on remarkably",
            "simple equations.",
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
            "Sign conventions are the most common source of errors in",
            "geometric optics problems. Getting a sign wrong means getting",
            "the wrong answer for the entire problem. Study these",
            "carefully.",
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
            "lens, mirror, or refracting surface. The object distance s_o",
            "is positive when the object is on the side where light is",
            "coming from. This is called a real object and is the normal",
            "case.",
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
            "The image distance s_i is positive when the image forms on the",
            "far side of the lens — on the side where light is going to.",
            "This is a real image that can be projected onto a screen.",
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
            "The radius of curvature R is positive if the centre of",
            "curvature is to the right of the surface — which means a",
            "convex surface for light coming from the left. It is negative",
            "for a concave surface.",
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
            "For mirrors, the sign convention flips: a concave mirror has R",
            "positive, a convex mirror has R negative.",
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
            "The magnification m equals minus s_i over s_o. A negative",
            "magnification means the image is inverted. A magnitude greater",
            "than one means the image is larger than the object.",
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
            "Always draw a diagram first. Label the signs explicitly. Then",
            "substitute into the equation.",
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
            "according to the spherical surface equation: n_m over s_o plus",
            "n_i over s_i equals n_i minus n_m over R.",
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
            "This is derived by applying Snell's law in the paraxial",
            "approximation to a ray hitting a spherical surface. It is the",
            "building block from which the thin lens equations are derived",
            "by applying this formula twice — once for each surface of the",
            "lens.",
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
            "The radius R is positive if the centre of curvature is to the",
            "right of the surface, and negative if it is to the left.",
            "Getting this sign right is essential.",
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
            "The thin lens equation is one of the most used equations in",
            "all of optics. One over s_o plus one over s_i equals one over",
            "f.",
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
            "s_o is the object distance, s_i is the image distance, and f",
            "is the focal length of the lens.",
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
        eqs = VGroup(
            labeled_eq(r"\frac{1}{s_o}+\frac{1}{s_i}=\frac{1}{f}", "thin lens equation", GOLD, 44, 26),
            labeled_eq(r"m=-s_i/s_o", "magnification (negative = inverted)", WHITE, 44, 26),
            labeled_eq(r"P=1/f\;[\text{D}]", "power in dioptres", WAVE_COLOR, 44, 26),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=4.5)
        eqs.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "The lensmaker's equation tells us how f depends on the lens",
            "geometry: one over f equals n_l minus n_m over n_m, times one",
            "over R_1 minus one over R_2.",])
        b.next_to(eqs, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class ThinLensScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p4.mp3", time_offset=0)
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\frac{1}{f}=(n_l-n_m)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)", font_size=44, color=E_COLOR)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "Here n_l is the refractive index of the lens material, n_m is",
            "the index of the surrounding medium, and R_1 and R_2 are the",
            "radii of curvature of the two surfaces.",])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)

class ThinLensScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p5.mp3", time_offset=0)
        title = Text("The Thin Lens Equation", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "In air, this simplifies to one over f equals n_l minus one,",
            "times one over R_1 minus one over R_2.",
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
            "The magnification m equals minus s_i over s_o. A negative",
            "magnification means the image is inverted. A magnitude greater",
            "than one means the image is larger than the object.",
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
            "The dioptric power P equals one over f in units of dioptres —",
            "inverse metres. This is what your optician prescribes for",
            "glasses. Powers of lenses in contact simply add.",
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
            "Let's work through a complete example. A biconvex lens with",
            "R_1 equals positive 20 centimetres, R_2 equals negative 20",
            "centimetres, and n_l equals 1.5. Object at s_o equals 60",
            "centimetres.",
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
            "First: one over f equals 0.5 times 1 over 20 minus 1 over",
            "minus 20 equals 0.5 times 10 equals 5 dioptres. So f equals 20",
            "centimetres.",
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
            "Then: one over s_i equals one over 20 minus one over 60 equals",
            "3 minus 1 over 60 equals 2 over 60. So s_i equals 30",
            "centimetres. Real image.",
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
            "Magnification: minus 30 over 60 equals minus 0.5. Inverted,",
            "half the size of the object.",
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
        eqs = VGroup(
            labeled_eq(r"\frac{1}{s_o}+\frac{1}{s_i}=\frac{2}{R}=\frac{1}{f_m}", "mirror equation (same form as thin lens!)", GOLD, 40, 24),
            labeled_eq(r"f_m=R/2", "focal length = half the radius", WHITE, 40, 24),
            labeled_eq(r"m=-s_i/s_o", "magnification", WHITE, 40, 24),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=4.0)
        eqs.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "Spherical mirrors obey the mirror equation: one over s_o plus",
            "one over s_i equals two over R, which also equals one over the",
            "focal length f_m.",])
        b.next_to(eqs, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class MirrorScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p2.mp3", time_offset=0)
        title = Text("Spherical Mirrors", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The focal length of a mirror is half the radius of curvature:",
            "f_m equals R over 2. For a concave mirror with R positive, the",
            "focal length is positive and parallel rays converge to a real",
            "focus in front of the mirror.",
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
            "The magnification is minus s_i over s_o — same formula as for",
            "lenses. A concave mirror with an object beyond the focal point",
            "gives an inverted, real image. An object inside the focal",
            "point gives an upright, virtual, magnified image — exactly as",
            "in a shaving mirror.",
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
            "When two lenses are used in sequence, the image formed by the",
            "first lens becomes the object for the second lens. Apply the",
            "thin lens equation sequentially.",
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
        eqs = VGroup(
            labeled_eq(r"\frac{1}{f_{\rm eff}}=\frac{1}{f_1}+\frac{1}{f_2}-\frac{d}{f_1 f_2}", "two lenses separated by d", GOLD, 40, 24),
            labeled_eq(r"P_{\rm eff}=P_1+P_2", "contact lenses (d=0): powers add", WHITE, 40, 24),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=3.5)
        eqs.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "For two thin lenses separated by distance d, the effective",
            "focal length satisfies: one over f_eff equals one over f_1",
            "plus one over f_2 minus d over f_1 f_2.",])
        b.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class LensCombinations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p3.mp3", time_offset=0)
        title = Text("Lens Combinations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When the lenses are in contact — d approaches zero — this",
            "simplifies to: the powers add. P_eff equals P_1 plus P_2. This",
            "is why opticians measure lens power in dioptres and simply add",
            "them.",
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
            "All optical instruments are combinations of lenses and",
            "mirrors.",
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
        insts = eq_table([
            (r"M=25\,\text{cm}/f", "Magnifying glass (near point = 25 cm)", GOLD),
            (r"M=(-L/f_{ob})(25/f_e)", "Compound microscope", WAVE_COLOR),
            (r"M=-f_{ob}/f_e", "Astronomical telescope", E_COLOR),
        ], eq_fs=32, lbl_fs=22, buff=0.3)
        safe_scale(insts, max_width=13.0, max_height=4.0)
        insts.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "A magnifying glass places an object just inside its focal",
            "length, producing a virtual, upright, magnified image. The",
            "angular magnification is 25 centimetres divided by f, where 25",
            "cm is the standard near-point distance of the human eye.",])
        b.next_to(insts, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(insts, b), run_time=0.1))
        self.wait(1)

class OpticalInstruments_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p3.mp3", time_offset=0)
        title = Text("Optical Instruments", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "A compound microscope uses an objective with very short focal",
            "length to form a magnified real image, then an eyepiece to",
            "magnify that image further. The total magnification is the",
            "product of the two magnifications.",
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
            "A telescope works in reverse: the objective forms a real image",
            "of a distant object at its focal plane, and the eyepiece",
            "magnifies it. The angular magnification is minus f_objective",
            "over f_eyepiece. The minus sign means the image is inverted —",
            "hence telescopes for astronomy often don't bother with an",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

# week3_geometric.py — Week 3: Geometric Optics (v3 — complete, narration-ready)
# Source: Bennett Ch. 4.3-4.5, 5.2, 5.5.1-5.5.4
from manim import *
from utils import *


def pg(scene, title, lines, wait, fs=27, color=WHITE):
    texts = [Text(l, font_size=fs, color=color) for l in lines if l.strip()]
    if not texts: return
    block = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    safe_scale(block, max_width=13.0, max_height=4.0)
    block.next_to(title, DOWN, buff=0.5)
    scene.play(FadeIn(block, run_time=0.4))
    scene.wait(wait)
    scene.play(FadeOut(block, run_time=0.4))


class Week3TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEK 3",
            "Geometric Optics: Lenses, Mirrors & Instruments",
            "Bennett Ch. 4.3–4.5, 5.2, 5.5"
        )
        self.play(FadeIn(card))
        self.wait(83.5)
        self.play(FadeOut(card))


class GeometricOpticsIntro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("What is Geometric (Ray) Optics?", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "When the wavelength of light is MUCH smaller than the aperture,",
            "diffraction effects are negligible and light travels in straight RAYS.",
            "This is the regime of geometric optics.",
        ], wait=18.8)

        pg(self, title, [
            "Geometric optics describes: lenses, mirrors, telescopes,",
            "microscopes, the human eye, cameras, and optical fibres.",
            "It breaks down when apertures are comparable to the wavelength.",
        ], wait=17.3)

        pg(self, title, [
            "Key simplification: the PARAXIAL APPROXIMATION (Bennett 4.3.1).",
            "For small angles (rays close to and nearly parallel to the optical axis):",
            "sin(theta) ≈ tan(theta) ≈ theta  [theta in radians]",
            "This linearises all equations and makes analytic solutions possible.",
        ], wait=12.1)

        self.play(FadeOut(title))


class SignConventions(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Sign Conventions — CRITICAL (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        warning = Text(
            "Getting signs wrong is the #1 source of errors in geometric optics.",
            font_size=27, color=B_COLOR)
        safe_scale(warning, max_width=13.0)
        warning.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(warning))
        self.wait(13.5)

        rules = [
            ("Distances",       "measured FROM the optical element (lens/mirror/surface)"),
            ("Object dist s_o", "POSITIVE for real object (on the incoming light side)"),
            ("Image dist s_i",  "POSITIVE for real image (on the outgoing light side)"),
            ("Radius R",        "POSITIVE if centre of curvature is to the RIGHT of surface"),
            ("Concave mirror",  "R > 0  (centre of curvature in FRONT of mirror)"),
            ("Convex mirror",   "R < 0  (centre of curvature BEHIND mirror)"),
            ("Converging lens", "f > 0  (positive/convex lens)"),
            ("Diverging lens",  "f < 0  (negative/concave lens)"),
            ("Magnification m", "= -s_i/s_o.  NEGATIVE m means inverted image.  |m|>1 means magnified"),
        ]

        rule_group = VGroup()
        for key, val in rules:
            k = Text(key + ":", font_size=24, color=GOLD, weight=BOLD)
            v = Text(val, font_size=24, color=WHITE)
            row = VGroup(k, v).arrange(RIGHT, buff=0.3, aligned_edge=UP)
            safe_scale(row, max_width=13.0)
            rule_group.add(row)
        rule_group.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        rule_group.next_to(warning, DOWN, buff=0.3)
        safe_scale(rule_group, max_height=4.5)
        self.play(FadeIn(rule_group))
        self.wait(84.3)
        self.play(FadeOut(VGroup(title, warning, rule_group)))


class SphericalSurface(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Refraction at a Spherical Surface (Bennett Eq. 4.10)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "Before thin lenses, Bennett treats a SINGLE curved interface.",
            "Apply the paraxial approximation to Snell's law at the curved surface.",
        ], wait=13.0)

        eq = MathTex(r"\frac{n_m}{s_o} + \frac{n_i}{s_i} = \frac{n_i - n_m}{R}",
                     font_size=56, color=N_COLOR)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(eq))
        self.wait(20.7)

        sym = eq_table([
            (r"n_m", "index of incident medium (object side)", N_COLOR),
            (r"n_i", "index of refracting medium (glass side)", N_COLOR),
            (r"s_o", "object distance from surface  [m]", WHITE),
            (r"s_i", "image distance from surface  [m]", WHITE),
            (r"R",   "radius of curvature (signed: + if centre is right of surface)", WHITE),
        ], eq_fs=30, lbl_fs=23, buff=0.22)
        sym.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(sym))
        self.wait(14.5)
        self.play(FadeOut(sym))

        pg(self, title, [
            "Example: air (n=1.0) to glass (n=1.5), R=+10 cm, object at 30 cm.",
            "1.0/30 + 1.5/s_i = (1.5-1.0)/10 = 0.05",
            "1.5/s_i = 0.05 - 0.033 = 0.017  =>  s_i = 90 cm  (real image in glass)",
        ], wait=2.0)

        self.play(FadeOut(VGroup(title, eq)))


class ThinLensScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Thin Lenses (Bennett Section 4.3.3)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "A thin lens has two spherical surfaces so close we treat them as one.",
            "Apply the spherical surface equation TWICE to derive the thin lens equation.",
        ], wait=12.1)

        lme = MathTex(r"\frac{1}{f} = (n_l-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)",
                      font_size=44, color=N_COLOR)
        lme_lbl = Text("Lensmaker's equation  (Bennett Eq. 4.15)  [in air]", font_size=24, color=COMMENT_COLOR)
        lme_block = VGroup(lme, lme_lbl).arrange(DOWN, buff=0.2)
        lme_block.next_to(title, DOWN, buff=0.5)
        self.play(Write(lme_block))
        self.wait(8.7)
        self.play(FadeOut(lme_block))

        tl = MathTex(r"\frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f}", font_size=62, color=GOLD)
        tl.next_to(title, DOWN, buff=0.5)
        self.play(Write(tl))
        self.play(Create(gold_box(tl)))
        self.wait(13.5)

        extras = VGroup(
            labeled_eq(r"m = -\frac{s_i}{s_o}", "lateral magnification", WHITE, 44, 24),
            labeled_eq(r"P = \frac{1}{f}\text{ [dioptres D = m}^{-1}\text{]}", "dioptric power", INTENSITY_COLOR, 36, 24),
        ).arrange(RIGHT, buff=1.5)
        extras.next_to(tl, DOWN, buff=0.4)
        self.play(FadeIn(extras))
        self.wait(14.5)
        self.play(FadeOut(extras))

        pg(self, title, [
            "Example: biconvex lens R1=+20cm, R2=-20cm, n_l=1.5, object at 60cm.",
            "Step 1: 1/f = (0.5)(1/20 - 1/-20) = 0.5 x 2/20 = 1/20  =>  f = 20 cm",
            "Step 2: 1/s_i = 1/20 - 1/60 = 2/60  =>  s_i = 30 cm  (real image)",
            "Step 3: m = -30/60 = -0.5  (inverted, half size)",
        ], wait=83.6)

        self.play(FadeOut(VGroup(title, tl)))


class MirrorScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Spherical Mirrors (Bennett Section 4.3.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "Spherical mirrors follow the same paraxial structure as thin lenses.",
            "Focal length of a mirror: f_m = R/2  (centre of curvature is at 2f).",
            "Concave mirrors (R>0) converge rays — like converging lenses.",
            "Convex mirrors (R<0) diverge rays — like diverging lenses.",
        ], wait=12.1)

        mirror_eq = MathTex(r"\frac{1}{s_o}+\frac{1}{s_i}=\frac{2}{R}=\frac{1}{f_m}",
                            font_size=58, color=GOLD)
        mirror_eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(mirror_eq))
        self.play(Create(gold_box(mirror_eq)))
        self.wait(19.8)

        pg(self, title, [
            "Example: concave mirror R=+40cm, object at s_o=30cm.",
            "f_m = 40/2 = 20 cm",
            "1/s_i = 1/20 - 1/30 = 1/60  =>  s_i = 60 cm  (real, in front)",
            "m = -60/30 = -2  (inverted, twice the size)",
        ], wait=22.2)

        self.play(FadeOut(VGroup(title, mirror_eq)))


class LensCombinations(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Lens Combinations (Bennett Section 4.4)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "Two lenses in sequence: image of lens 1 is the object of lens 2.",
            "Apply the thin lens equation sequentially.",
        ], wait=12.6)

        eqs = VGroup(
            labeled_eq(
                r"\frac{1}{f_{\text{eff}}} = \frac{1}{f_1}+\frac{1}{f_2}-\frac{d}{f_1 f_2}",
                "two lenses separated by distance d", N_COLOR, 38, 24),
            labeled_eq(
                r"P_{\text{eff}} = P_1 + P_2 \quad (d=0)",
                "lenses in CONTACT: powers simply add", N_COLOR, 40, 24),
        ).arrange(DOWN, buff=0.5)
        eqs.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(eqs))
        self.wait(13.5)
        self.play(FadeOut(eqs))

        pg(self, title, [
            "Example: f1=30cm, f2=20cm, d=10cm.",
            "1/f_eff = 1/30 + 1/20 - 10/(30x20) = 0.033+0.05-0.017 = 0.067",
            "f_eff = 15 cm",
            "Contact case (d=0): 1/f = 1/30+1/20 = 5/60  =>  f=12 cm",
        ], wait=16.4)

        self.play(FadeOut(title))


class OpticalInstruments(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Optical Instruments (Bennett Section 4.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        instruments = [
            ("Magnifying Glass",
             [
                 "Object just inside focal point => virtual, magnified, upright image.",
                 "Angular magnification: M = 25 cm / f",
                 "(near point distance = 25 cm = standard for human eye)",
             ], 15),
            ("Compound Microscope",
             [
                 "Objective (short f_ob) forms real magnified intermediate image.",
                 "Eyepiece acts as magnifying glass for that intermediate image.",
                 "Total magnification: M = m_ob x M_eye = (-L/f_ob) x (25/f_e)",
                 "L = tube length = distance from rear focal point to eyepiece.",
             ], 20),
            ("Astronomical Telescope",
             [
                 "Objective collects light, forms real image at its focal plane.",
                 "Eyepiece magnifies the intermediate image.",
                 "Angular magnification (afocal): M = -f_ob / f_e",
                 "Negative sign: inverts image (Galilean telescope uses diverging eyepiece).",
             ], 20),
            ("Camera",
             [
                 "A single converging lens forms a real, inverted image on the sensor.",
                 "Focusing: adjust lens-sensor distance s_i for different object distances.",
                 "f-number = f/D where D = aperture diameter.",
                 "Lower f-number = more light = shallower depth of field.",
             ], 18),
        ]

        for inst_name, desc_lines, wait in instruments:
            inst_title = Text(inst_name + ":", font_size=30, color=GOLD)
            inst_title.next_to(title, DOWN, buff=0.5)
            self.play(Write(inst_title))
            desc = VGroup(*[Text(l, font_size=25, color=WHITE) for l in desc_lines])
            desc.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            safe_scale(desc, max_width=13.0, max_height=3.5)
            desc.next_to(inst_title, DOWN, buff=0.3)
            self.play(FadeIn(desc))
            self.wait(wait)
            self.play(FadeOut(VGroup(inst_title, desc)))

        self.play(FadeOut(title))

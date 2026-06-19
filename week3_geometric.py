# week3_geometric.py  —  Week 3: Geometric Optics  (v2)
# Source: Bennett Ch. 4.3-4.5, 5.2, 5.5
from manim import *
from utils import *


class Week3TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEK 3",
            "Geometric Optics: Lenses, Mirrors & Optical Instruments",
            "Bennett Ch. 4.3–4.5, 5.2, 5.5"
        )
        self.play(FadeIn(card)); self.wait(97.69999999999999); self.play(FadeOut(card))


class GeometricOpticsIntro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("What is Geometric (Ray) Optics?", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        show_pages(self, title, [
            (["When the wavelength of light λ is much smaller than the aperture or", "obstacle it encounters, diffraction effects are negligible.", "In this limit, light travels in straight RAYS — like tiny arrows."], 19.0),
            (["This is the realm of geometric optics (also called ray optics).", "It describes lenses, mirrors, telescopes, microscopes, the human eye,", "cameras, and optical fibres — with elegant, simple equations."], 19.0),
            (["The key simplification is the PARAXIAL APPROXIMATION  (Bennett Section 4.3.1):", "For small angles (rays close to and nearly parallel to the optical axis):", "sin(θ) ≈ tan(θ) ≈ θ  [θ in radians]", "This linearises all the equations and makes analytic solutions possible."], 19.0),
        ], font_size=28)
        self.camera.background_color = BG_COLOR
        title = Text("Sign Conventions  (Bennett Section 4.3.4) — CRITICAL", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        warning = Text(
            "Getting signs wrong is the #1 source of errors in geometric optics. Read carefully.",
            font_size=27, color=B_COLOR
        )
        warning.next_to(title, DOWN, buff=0.4)
        safe_scale(warning, max_width=13.5)
        self.play(FadeIn(warning)); self.wait(11.6)

        rules = [
            ("All distances", "measured from the optical element (lens/mirror/surface)."),
            ("Object distance s_o", "POSITIVE for real object (object on incoming-light side)."),
            ("Image distance s_i", "POSITIVE for real image (image on outgoing-light side)."),
            ("Radius R", "POSITIVE if centre of curvature is to the RIGHT of the surface."),
            ("Mirrors concave", "R > 0  (centre of curvature in FRONT of mirror)."),
            ("Mirrors convex",  "R < 0  (centre of curvature BEHIND mirror)."),
            ("Lenses converging", "f > 0  (positive/convex lens)."),
            ("Lenses diverging",  "f < 0  (negative/concave lens)."),
            ("Magnification m",   "= −s_i/s_o.  NEGATIVE m → inverted image.  |m|>1 → magnified."),
        ]

        rule_group = VGroup()
        for key, val in rules:
            k = Text(key + ":", font_size=25, color=GOLD, weight=BOLD)
            v = Text(val, font_size=25, color=WHITE)
            row = VGroup(k, v).arrange(RIGHT, buff=0.25, aligned_edge=UP)
            rule_group.add(row)
        rule_group.arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        rule_group.next_to(warning, DOWN, buff=0.3)
        safe_scale(rule_group, max_height=5.0)

        for row in rule_group:
            self.play(FadeIn(row), run_time=0.4); self.wait(23.2)
        self.wait(36.4); self.play(FadeOut(VGroup(title, warning, rule_group)))


class SphericalSurface(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Refraction at a Spherical Surface  (Bennett Eq. 4.10)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Before thin lenses, Bennett treats a SINGLE curved interface between two media.",
            "This is the building block from which all lens equations are derived.",
            "Apply the paraxial approximation to Snell's law at the curved surface:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(15.5)
        self.wait(24.3); self.play(FadeOut(intro))

        eq = MathTex(
            r"\frac{n_m}{s_o} + \frac{n_i}{s_i} = \frac{n_i - n_m}{R}",
            font_size=56, color=N_COLOR)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(eq)); self.wait(17.1)

        sym = eq_table([
            (r"n_m", "index of the medium containing the object (incoming medium)", N_COLOR),
            (r"n_i", "index of the refracting medium (the glass/lens material)", N_COLOR),
            (r"s_o", "object distance from the surface [m]", WHITE),
            (r"s_i", "image distance from the surface [m]", WHITE),
            (r"R",   "radius of curvature of the surface (signed!)", WHITE),
        ], eq_fs=30, lbl_fs=23, buff=0.24)
        sym.next_to(eq, DOWN, buff=0.4)
        for row in sym: self.play(FadeIn(row)); self.wait(2.0)
        self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5); self.play(FadeOut(sym))

        # Worked example
        ex_title = Text("Example: air (n=1.0) → glass (n=1.5), R=+10 cm, s_o=30 cm", font_size=26, color=GOLD)
        ex_title.next_to(eq, DOWN, buff=0.4)
        safe_scale(ex_title, max_width=13.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.35)
        solver.add_step(1,
            r"\frac{1.0}{30} + \frac{1.5}{s_i} = \frac{1.5-1.0}{10} = 0.05",
            "substitute n_m=1.0, n_i=1.5, R=+10, s_o=30 (all in cm)")
        solver.add_step(2,
            r"\frac{1.5}{s_i} = 0.05 - \frac{1.0}{30} = 0.05 - 0.0333 = 0.0167",
            "isolate the 1.5/s_i term")
        solver.add_step(3,
            r"s_i = \frac{1.5}{0.0167} = 90\text{ cm} \quad\text{(real image, positive)}",
            "image forms 90 cm to the RIGHT of the surface, in the glass", GOLD)
        solver.finalize()


class ThinLensScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Thin Lenses  (Bennett Section 4.3.3)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "A thin lens is formed by two spherical refracting surfaces so close together",
            "that we treat them as having zero separation between them.",
            "Apply the spherical surface equation TWICE — the image of surface 1 is the",
            "object of surface 2 — and combine the results.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(14.4)
        self.wait(10.5); self.play(FadeOut(intro))

        # Lensmaker's equation
        lme_title = Text("Lensmaker's Equation  (Bennett Eq. 4.15):", font_size=28, color=GOLD)
        lme_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(lme_title))

        lme = MathTex(
            r"\frac{1}{f} = \frac{n_l - n_m}{n_m}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)",
            font_size=44, color=N_COLOR)
        lme.next_to(lme_title, DOWN, buff=0.3)
        self.play(Write(lme)); self.wait(16.0)

        lme_air = MathTex(
            r"\text{In air } (n_m=1):\quad \frac{1}{f} = (n_l-1)\left(\frac{1}{R_1}-\frac{1}{R_2}\right)",
            font_size=38, color=N_COLOR)
        lme_air.next_to(lme, DOWN, buff=0.3)
        safe_scale(lme_air, max_width=13.0)
        self.play(Write(lme_air)); self.wait(17.1)
        self.play(FadeOut(VGroup(lme_title, lme, lme_air)))

        # Thin lens equation
        tl_title = Text("Thin Lens Equation  (Bennett Eq. 4.17):", font_size=28, color=GOLD)
        tl_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(tl_title))

        tl = MathTex(r"\frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f}", font_size=60, color=GOLD)
        tl.next_to(tl_title, DOWN, buff=0.35)
        self.play(Write(tl)); self.wait(11.0)
        self.play(Create(gold_box(tl))); self.wait(16.0)

        mag = MathTex(r"m = -\frac{s_i}{s_o}", font_size=50, color=WHITE)
        power = MathTex(r"P = \frac{1}{f} \quad [\text{dioptres D} = \text{m}^{-1}]", font_size=40, color=INTENSITY_COLOR)
        extras = VGroup(mag, power).arrange(RIGHT, buff=1.5)
        extras.next_to(tl, DOWN, buff=0.4)
        self.play(Write(extras)); self.wait(72.4)
        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.play(FadeOut(VGroup(tl_title, tl, extras)))

        # Full worked example
        ex_title = Text(
            "Example: biconvex lens R₁=+20cm, R₂=−20cm, n_l=1.5, s_o=60cm",
            font_size=26, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        safe_scale(ex_title, max_width=13.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"\frac{1}{f} = (n_l-1)\!\left(\frac{1}{R_1}-\frac{1}{R_2}\right)"
            r"= (0.5)\!\left(\frac{1}{20}-\frac{1}{-20}\right) = 0.5\times\frac{2}{20} = \frac{1}{20}",
            "lensmaker's equation: f = 20 cm", N_COLOR)
        solver.add_step(2,
            r"\frac{1}{s_i} = \frac{1}{f} - \frac{1}{s_o} = \frac{1}{20} - \frac{1}{60}"
            r"= \frac{3-1}{60} = \frac{2}{60}",
            "thin lens equation: solve for s_i")
        solver.add_step(3,
            r"s_i = \frac{60}{2} = 30\text{ cm} \quad\text{(positive \to \text{ real image} on far side)}",
            "image forms 30 cm beyond the lens", GOLD)
        solver.add_step(4,
            r"m = -\frac{s_i}{s_o} = -\frac{30}{60} = -0.5",
            "magnification = −0.5: inverted, half the size of the object", WHITE)
        solver.add_step(5,
            r"P = \frac{1}{f} = \frac{1}{0.20\text{ m}} = +5.0\text{ D} \quad\text{(converging lens)}",
            "dioptric power in dioptres (m⁻¹)", INTENSITY_COLOR)
        solver.finalize()


class MirrorScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Spherical Mirrors  (Bennett Section 4.3.2)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        show_pages(self, title, [
            (["Spherical mirrors obey the same paraxial equation structure as lenses.", "The focal length of a mirror: f_m = R/2  (centre of curvature is at 2f).", "Concave mirrors (R > 0) converge rays → behave like converging lenses.", "Convex mirrors  (R < 0) diverge  rays → behave like diverging lenses."], 18.8),
            (["Sign convention for mirrors: distances measured from the mirror surface;", "real images are in FRONT of the mirror (positive s_i for concave mirrors)."], 18.8),
        ], font_size=28)
        mirror_eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(mirror_eq)); self.wait(25.9)
        self.play(Create(gold_box(mirror_eq))); self.wait(2.0)

        mag_eq = MathTex(r"m = -\frac{s_i}{s_o} \quad\text{(same as for lenses)}", font_size=40, color=WHITE)
        mag_eq.next_to(mirror_eq, DOWN, buff=0.35)
        self.play(Write(mag_eq)); self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5); self.play(FadeOut(mag_eq))

        # Worked example
        ex_title = Text("Example: concave mirror R=+40 cm, object at s_o=30 cm", font_size=28, color=GOLD)
        ex_title.next_to(mirror_eq, DOWN, buff=0.4)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"f_m = \frac{R}{2} = \frac{40}{2} = 20\text{ cm}",
            "focal length of concave mirror")
        solver.add_step(2,
            r"\frac{1}{s_i} = \frac{1}{f_m} - \frac{1}{s_o} = \frac{1}{20} - \frac{1}{30}"
            r"= \frac{3-2}{60} = \frac{1}{60}",
            "mirror equation: solve for s_i")
        solver.add_step(3,
            r"s_i = 60\text{ cm} \quad\text{(positive \to \text{ real image} in front of mirror)}",
            "real image, 60 cm in front of the mirror", GOLD)
        solver.add_step(4,
            r"m = -\frac{s_i}{s_o} = -\frac{60}{30} = -2.0",
            "magnification = −2: image is inverted and TWICE the size of object", WHITE)
        solver.finalize()


class LensCombinations(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Lens Combinations  (Bennett Section 4.4)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Two or more lenses in sequence: the IMAGE of the first lens becomes",
            "the OBJECT of the second lens — apply the thin lens equation sequentially.",
            "",
            "For two thin lenses separated by distance d:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(14.9)
        self.wait(16.0); self.play(FadeOut(intro))

        separated = labeled_eq(
            r"\frac{1}{f_{\text{eff}}} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2}",
            "two lenses separated by distance d — effective focal length", N_COLOR, 44, 25)
        separated.next_to(title, DOWN, buff=0.5)
        self.play(Write(separated)); self.wait(19.3)

        contact = labeled_eq(
            r"P_{\text{eff}} = P_1 + P_2 = \frac{1}{f_1} + \frac{1}{f_2} \quad (d\to 0)",
            "lenses in CONTACT: powers ADD — used in spectacle design", N_COLOR, 40, 25)
        contact.next_to(separated, DOWN, buff=0.4)
        self.play(Write(contact)); self.wait(2.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.play(FadeOut(VGroup(separated, contact)))

        # Example
        ex_title = Text("Example: f₁=30cm, f₂=20cm, d=10cm", font_size=30, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"\frac{1}{f_{\text{eff}}} = \frac{1}{30} + \frac{1}{20} - \frac{10}{30\times20}",
            "substitute values into combination formula")
        solver.add_step(2,
            r"= 0.0333 + 0.0500 - 0.0167 = 0.0667",
            "arithmetic: add the three terms")
        solver.add_step(3,
            r"f_{\text{eff}} = \frac{1}{0.0667} = 15.0\text{ cm}",
            "effective focal length of the combination", GOLD)
        solver.add_step(4,
            r"\text{For contact }(d=0): \frac{1}{f_{\text{eff}}} = \frac{1}{30}+\frac{1}{20} = \frac{5}{60}"
            r"\;\Rightarrow\; f_{\text{eff}} = 12.0\text{ cm}",
            "comparison: contact combination is stronger (shorter f)")
        solver.finalize()


class OpticalInstruments(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Optical Instruments  (Bennett Section 4.5)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "All optical instruments are combinations of lenses and/or mirrors.",
            "The key parameters are: magnification, field of view, and resolution.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(5.0)
        self.wait(21.0); self.play(FadeOut(intro))

        instruments = [
            ("Magnifying Glass", [
                "Object just inside focal point → virtual, magnified, upright image.",
                "Angular magnification: M = 25cm / f  (near point = 25 cm).",
                "Maximum useful magnification limited by eye's resolution ~0.2 mm.",
            ], N_COLOR),
            ("Compound Microscope", [
                "Objective lens (short f_ob) forms a real, magnified intermediate image.",
                "Eyepiece acts as a magnifying glass for that intermediate image.",
                "Total magnification: M ≈ m_ob × M_eye = (−L/f_ob)×(25cm/f_e)",
                "L = tube length = distance from rear focal point of objective to eyepiece.",
            ], E_COLOR),
            ("Astronomical Telescope", [
                "Objective collects light and forms real image at its focal plane.",
                "Eyepiece magnifies this intermediate image.",
                "Angular magnification (afocal): M = −f_ob / f_e",
                "Negative sign: telescope inverts image (hence the Galilean telescope uses",
                "a diverging eyepiece to produce an upright image).",
            ], B_COLOR),
        ]

        for inst_name, desc_lines, color in instruments:
            inst_title = Text(inst_name + "  (Bennett Section 4.5):", font_size=30, color=GOLD)
            inst_title.next_to(title, DOWN, buff=0.5)
            self.play(Write(inst_title))

            desc = section_intro(desc_lines, font_size=26)
            desc.next_to(inst_title, DOWN, buff=0.35)
            self.play(FadeIn(desc))
            self.wait(19.3)
            self.wait(28.7); self.play(FadeOut(VGroup(inst_title, desc)))

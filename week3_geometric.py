# week3_geometric.py
# 31OPT Optics — Week 3: Geometric Optics: Lenses, Mirrors & Instruments
from manim import *
from utils import *


class Week3TitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "WEEK 3",
            "Geometric Optics: Lenses, Mirrors & Instruments",
            "Bennett Ch. 4.3-4.5, 5.2"
        )
        self.play(FadeIn(card)); self.wait(2); self.play(FadeOut(card))


class GeometricOpticsIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Geometric Optics", font_size=44, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        intro = section_intro([
            "When wavelength << aperture size, light travels in straight rays.",
            "Geometric optics ignores diffraction and treats lenses/mirrors with simple equations.",
            "The paraxial approximation assumes small angles: sin(theta) approx tan(theta) approx theta.",
            "We derive equations for image distance, magnification, focal length.",
            "Sign convention is critical — get it right or everything is wrong."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.1)
        self.wait(1); self.play(FadeOut(VGroup(title, intro)))


class SignConventions(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Sign Conventions — MEMORISE THESE", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        rules = [
            "All distances measured from the optical element (lens/mirror/surface).",
            "Object distance s_o > 0 for real object (on incoming side).",
            "Image distance  s_i > 0 for real image  (on outgoing side).",
            "Radius R > 0 if centre of curvature is to the RIGHT of the surface.",
            "For mirrors:  concave R > 0,  convex R < 0.",
            "For lenses:   converging f > 0,  diverging f < 0.",
            "Magnification m = -s_i / s_o:  negative = inverted image.",
        ]
        rule_texts = VGroup(*[Text(r, font_size=26, color=WHITE) for r in rules])
        rule_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        rule_texts.next_to(title, DOWN, buff=0.3)
        for r in rule_texts:
            self.play(FadeIn(r), run_time=0.5); self.wait(0.5)
        self.wait(2); self.play(FadeOut(VGroup(title, rule_texts)))


class SphericalSurface(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Refraction at a Single Spherical Surface", font_size=36, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Before thin lenses, we treat a single curved interface between two media.",
            "The paraxial refraction equation relates object distance, image distance,",
            "and radius of curvature, accounting for both indices of refraction.",
            "Thin lenses are just two such surfaces applied in sequence."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        eq = MathTex(
            r"\frac{n_m}{s_o} + \frac{n_i}{s_i} = \frac{n_i - n_m}{R}",
            font_size=52, color=N_COLOR
        )
        self.play(Write(eq)); self.wait(1)

        symbols = VGroup(
            MathTex(r"n_m = \text{index of incoming (object) medium}", font_size=28, color=N_COLOR),
            MathTex(r"n_i = \text{index of refracting medium}",         font_size=28, color=N_COLOR),
            MathTex(r"s_o = \text{object distance}",                    font_size=28, color=WHITE),
            MathTex(r"s_i = \text{image distance}",                     font_size=28, color=WHITE),
            MathTex(r"R   = \text{radius of curvature (+/- by sign convention)}", font_size=28, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        symbols.next_to(eq, DOWN, buff=0.4)
        self.play(FadeIn(symbols)); self.wait(1.5)

        self.play(FadeOut(symbols))
        ex_title = Text(
            "Example: air (n=1.0) to glass (n=1.5), R=+10 cm, s_o=30 cm",
            font_size=26, color=GOLD
        )
        ex_title.next_to(eq, DOWN, buff=0.4)
        self.play(Write(ex_title))

        s1 = MathTex(r"\frac{1.0}{30} + \frac{1.5}{s_i} = \frac{1.5-1.0}{10} = 0.05",
                     font_size=36)
        s2 = MathTex(r"\frac{1.5}{s_i} = 0.05 - \frac{1.0}{30} = 0.05 - 0.0333 = 0.0167",
                     font_size=36)
        s3 = MathTex(r"s_i = \frac{1.5}{0.0167} = 90 \text{ cm (real image)}",
                     font_size=36, color=GOLD)
        steps = VGroup(s1, s2, s3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(ex_title, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s)); self.wait(0.8)
        self.play(Create(gold_box(s3)))
        self.wait(2); self.play(FadeOut(VGroup(title, eq, ex_title, steps)))


class ThinLensScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Thin Lens — Lensmaker's Equation", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "A thin lens is approximated as having negligible thickness.",
            "Its focal length f depends on the lens material and surface curvatures.",
            "The lensmaker's equation gives f from the geometry.",
            "Dioptric power P = 1/f is additive for lenses in contact."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        lme = MathTex(
            r"\frac{1}{f} = \frac{n_l - n_m}{n_m}"
            r" \left(\frac{1}{R_1} - \frac{1}{R_2}\right)",
            font_size=42, color=N_COLOR
        )
        lme_air = MathTex(
            r"\text{In air } (n_m=1): \quad"
            r"\frac{1}{f} = (n_l - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)",
            font_size=36, color=N_COLOR
        )
        self.play(Write(lme)); self.wait(1)
        self.play(Write(lme_air)); self.wait(1.5)

        tl    = MathTex(r"\frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f}",
                         font_size=52, color=GOLD)
        mag   = MathTex(r"m = -\frac{s_i}{s_o}", font_size=44, color=WHITE)
        power = MathTex(r"P = \frac{1}{f} \quad [\text{dioptres, D} = \text{m}^{-1}]",
                         font_size=36, color=INTENSITY_COLOR)
        combined = VGroup(tl, mag, power).arrange(DOWN, buff=0.4)
        combined.next_to(lme_air, DOWN, buff=0.4)
        for item in combined:
            self.play(Write(item)); self.wait(0.8)
        self.play(Create(gold_box(tl)))

        # Full example
        self.play(FadeOut(VGroup(lme, lme_air, combined)))
        ex_title = Text(
            "Example: biconvex lens R1=+20cm, R2=-20cm, n_l=1.5. Object at s_o=60cm.",
            font_size=23, color=GOLD
        )
        ex_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(ex_title))

        s1 = MathTex(
            r"\frac{1}{f} = (1.5-1)\left(\frac{1}{0.20}-\frac{1}{-0.20}\right)"
            r" = 0.5 \times 10 = 5 \text{ m}^{-1}",
            font_size=30)
        s2 = MathTex(r"f = 0.20 \text{ m} = 20 \text{ cm}", font_size=30, color=N_COLOR)
        s3 = MathTex(
            r"\frac{1}{s_i} = \frac{1}{f} - \frac{1}{s_o}"
            r" = \frac{1}{20} - \frac{1}{60} = \frac{3-1}{60} = \frac{2}{60}",
            font_size=30)
        s4 = MathTex(r"s_i = 30 \text{ cm (real image)}", font_size=30, color=GOLD)
        s5 = MathTex(
            r"m = -\frac{s_i}{s_o} = -\frac{30}{60} = -0.5 \text{ (inverted, half-size)}",
            font_size=30, color=WHITE)
        steps = VGroup(s1, s2, s3, s4, s5).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        steps.next_to(ex_title, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s), run_time=1.0); self.wait(0.6)
        self.play(Create(gold_box(VGroup(s4, s5))))
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, steps)))


class MirrorScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Mirror Equation", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Curved mirrors follow the same thin-lens structure but R sign is flipped.",
            "Concave mirrors converge light (R > 0) — like a converging lens.",
            "Convex mirrors diverge light (R < 0) — like a diverging lens.",
            "Focal length of a mirror: f_m = R/2."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        mirror_eq = MathTex(
            r"\frac{1}{s_o} + \frac{1}{s_i} = \frac{2}{R} = \frac{1}{f_m}",
            font_size=52, color=GOLD
        )
        self.play(Write(mirror_eq)); self.wait(1)

        mag_eq = MathTex(r"m = -\frac{s_i}{s_o}", font_size=44, color=WHITE)
        signs = VGroup(
            Text("Concave mirror: R > 0  (centre of curvature in front of mirror)", font_size=26),
            Text("Convex mirror:  R < 0  (centre of curvature behind mirror)",      font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        below = VGroup(mag_eq, signs).arrange(DOWN, buff=0.3)
        below.next_to(mirror_eq, DOWN, buff=0.4)
        self.play(Write(below)); self.wait(1.5)

        self.play(FadeOut(below))
        ex = MathTex(
            r"\text{Concave mirror } R=40\text{ cm},\; s_o=30\text{ cm. Find }s_i, m.",
            font_size=28, color=GOLD
        )
        ex.next_to(mirror_eq, DOWN, buff=0.4)
        self.play(Write(ex))

        s1 = MathTex(
            r"\frac{1}{s_i} = \frac{2}{R} - \frac{1}{s_o}"
            r" = \frac{2}{40} - \frac{1}{30} = \frac{1}{20} - \frac{1}{30} = \frac{1}{60}",
            font_size=32)
        s2 = MathTex(r"s_i = 60 \text{ cm (real image)}", font_size=32, color=GOLD)
        s3 = MathTex(r"m = -\frac{60}{30} = -2 \text{ (inverted, magnified x2)}", font_size=32)
        steps = VGroup(s1, s2, s3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(ex, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s)); self.wait(0.7)
        self.play(Create(gold_box(VGroup(s2, s3))))
        self.wait(2); self.play(FadeOut(VGroup(title, mirror_eq, ex, steps)))


class LensCombinations(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Thin Lens Combinations", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Two or more lenses in sequence: treat image of first lens as object of second.",
            "For two lenses separated by distance d, an effective focal length formula exists.",
            "Lenses in contact (d=0): powers simply add."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        separated = MathTex(
            r"\frac{1}{f_{\text{eff}}} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2}",
            font_size=46, color=N_COLOR
        )
        contact = MathTex(
            r"\text{In contact } (d\to 0):"
            r"\quad P_{\text{eff}} = P_1 + P_2 = \frac{1}{f_1} + \frac{1}{f_2}",
            font_size=36, color=N_COLOR
        )
        eqs = VGroup(separated, contact).arrange(DOWN, buff=0.5)
        self.play(Write(eqs)); self.wait(1.5)

        self.play(FadeOut(eqs))
        ex = MathTex(
            r"f_1=30\text{ cm},\; f_2=20\text{ cm},\; d=10\text{ cm}",
            font_size=30, color=GOLD
        )
        ex.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex))

        s1 = MathTex(
            r"\frac{1}{f_{\text{eff}}} = \frac{1}{30} + \frac{1}{20} - \frac{10}{600}"
            r" = 0.0333 + 0.05 - 0.0167 = 0.0667",
            font_size=30)
        s2 = MathTex(r"f_{\text{eff}} = 15 \text{ cm}", font_size=36, color=GOLD)
        steps = VGroup(s1, s2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(ex, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s)); self.wait(0.8)
        self.play(Create(gold_box(s2)))
        self.wait(2); self.play(FadeOut(VGroup(title, ex, steps)))

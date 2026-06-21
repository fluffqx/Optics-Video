# week2_fresnel.py — Week 2: Fresnel Equations (paragraph-per-scene)
from manim import *
from utils import *

class Week2TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([            "Week 2 brings us to one of the most practically important",
            "topics in optics: what happens when light strikes a boundary",
            "between two different materials.",])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([            "Every time light passes through a lens, reflects off a mirror,",
            "or travels through a window, it's encountering an interface.",
            "The behaviour at that interface determines how optical",
            "instruments work.",])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([            "We need to answer two questions. First: in which directions",
            "does the reflected and transmitted light travel? That's",
            "answered by the law of reflection and Snell's law. Second: how",
            "much light is reflected and how much is transmitted? That's",
            "answered by the Fresnel equations.",])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 2", "Fresnel Equations, Reflection and Refraction", "Bennett Ch. 3")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([            "These are not just theoretical tools — they're used every day",
            "to design camera lenses, optical fibres, laser cavities, and",
            "anti-reflection coatings.",])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p1.mp3", time_offset=0)
        title = Text("What Happens at an Interface?", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Week 2 focuses on what happens when light crosses a boundary",
            "between two different optical media.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p2.mp3", time_offset=0)
        title = Text("What Happens at an Interface?", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Every time light passes through a lens, bounces off a mirror,",
            "or travels through a window, it encounters an interface. The",
            "physics at that interface determines everything — how much",
            "light is reflected, how much is transmitted, and in which",
            "direction.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week2Intro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week2Intro_p3.mp3", time_offset=0)
        title = Text("What Happens at an Interface?", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "We need to answer two questions. First, which direction? That",
            "is answered by the law of reflection and Snell's law. Second,",
            "how much? That is answered by the Fresnel equations — one of",
            "the most important sets of equations in all of optics.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p1.mp3", time_offset=0)
        title = Text("Fermat's Principle", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Fermat's principle states that light travels between two",
            "points along the path that takes the least time. This was",
            "proposed in 1657, well before Maxwell's equations existed.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p2.mp3", time_offset=0)
        title = Text("Fermat's Principle", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For reflection, minimising the travel time with respect to the",
            "reflection point automatically gives the law of reflection —",
            "angle in equals angle out.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p3.mp3", time_offset=0)
        title = Text("Fermat's Principle", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For refraction, the same minimisation with two different wave",
            "speeds in the two media gives Snell's law — n_i sin theta_i",
            "equals n_t sin theta_t.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FermatPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FermatPrinciple_p4.mp3", time_offset=0)
        title = Text("Fermat's Principle", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "This is a beautiful example of a variational principle —",
            "nature finding the optimal path. It also appears in quantum",
            "mechanics as Feynman's path integral formulation.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p1.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The law of reflection is simple: the angle of incidence equals",
            "the angle of reflection. Both angles are measured from the",
            "surface normal — the line perpendicular to the surface at the",
            "point of incidence. This holds for any wavelength and any",
            "material.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p2.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Snell's law governs refraction — the bending of light as it",
            "crosses the interface. n_i times sine of theta_i equals n_t",
            "times sine of theta_t.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p3.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Here n_i is the refractive index of the medium the light is",
            "coming from, theta_i is the angle of incidence, n_t is the",
            "index of the medium the light is entering, and theta_t is the",
            "angle of refraction.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p4.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "When light goes from a low-index medium to a high-index medium",
            "— like air into glass — it bends toward the normal. The angle",
            "gets smaller. When it goes from high to low index, it bends",
            "away from the normal.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p5.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"n_i\sin\theta_i = n_t\sin\theta_t", font_size=42, color=E_COLOR)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(eq, run_time=0.1))
        b = txt_block([
            "Let's work through an example. Glass with n equals 1.5 to air,",
            "with theta_i equals 30 degrees.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p6.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"n_i\sin\theta_i = n_t\sin\theta_t", font_size=42, color=E_COLOR)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(eq, run_time=0.1))
        b = txt_block([
            "Snell's law gives 1.5 times sine 30 equals 1.0 times sine",
            "theta_t.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p7.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"n_i\sin\theta_i = n_t\sin\theta_t", font_size=42, color=E_COLOR)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(eq, run_time=0.1))
        b = txt_block([
            "1.5 times 0.5 equals 0.75, so sine theta_t equals 0.75.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectionRefraction_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectionRefraction_p8.mp3", time_offset=0)
        title = Text("Reflection and Snell's Law", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"n_i\sin\theta_i = n_t\sin\theta_t", font_size=42, color=E_COLOR)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(eq, run_time=0.1))
        b = txt_block([
            "Taking the inverse sine gives theta_t equals 48.6 degrees. The",
            "light bends away from the normal as expected, since it's going",
            "from a denser medium to air.",
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p1.mp3", time_offset=0)
        title = Text("Where the Fresnel Equations Come From", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Fresnel equations come from applying Maxwell's boundary",
            "conditions at the interface.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p2.mp3", time_offset=0)
        title = Text("Where the Fresnel Equations Come From", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key conditions are: the tangential component of E must be",
            "continuous across the boundary, and the tangential component",
            "of B must also be continuous. These follow directly from",
            "Faraday's law and Ampere's law applied to a thin rectangle",
            "straddling the interface.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquationsDerivation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquationsDerivation_p3.mp3", time_offset=0)
        title = Text("Where the Fresnel Equations Come From", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "We split the incident electric field into two independent",
            "polarisation components — s-polarisation with E perpendicular",
            "to the plane of incidence, and p-polarisation with E parallel",
            "to the plane of incidence. Applying the boundary conditions to",
            "each gives four Fresnel equations — two reflection",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p1.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Snell's law tells us directions. The Fresnel equations tell us",
            "amplitudes — how much of the electric field is reflected and",
            "how much is transmitted.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p2.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The key insight is that polarisation matters at an interface.",
            "We split the electric field into two independent components.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p3.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "S-polarisation — sometimes called TE or transverse electric —",
            "has the electric field perpendicular to the plane of",
            "incidence. If you imagine the ray diagram drawn on paper, the",
            "s-polarised field points out of the paper toward you.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p4.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "P-polarisation — sometimes called TM or transverse magnetic —",
            "has the electric field lying in the plane of incidence,",
            "parallel to the page.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p5.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "These two polarisations reflect and transmit differently, and",
            "the Fresnel equations give us the amplitude reflection",
            "coefficient r and amplitude transmission coefficient t for",
            "each.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p6.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"r_\perp=\frac{n_i\cos\theta_i-n_t\cos\theta_t}{n_i\cos\theta_i+n_t\cos\theta_t}", "s-pol reflection coefficient", E_COLOR, 34, 22),
            labeled_eq(r"t_\perp=\frac{2n_i\cos\theta_i}{n_i\cos\theta_i+n_t\cos\theta_t}", "s-pol transmission coefficient", E_COLOR, 34, 22),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=3.5)
        eqs.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "For s-polarisation: r_perp equals n_i cosine theta_i minus n_t",
            "cosine theta_t, all divided by n_i cosine theta_i plus n_t",
            "cosine theta_t.",])
        b.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class FresnelEquations_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p7.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"r_\parallel=\frac{n_t\cos\theta_i-n_i\cos\theta_t}{n_t\cos\theta_i+n_i\cos\theta_t}", "p-pol reflection coefficient", B_COLOR, 34, 22),
            labeled_eq(r"t_\parallel=\frac{2n_i\cos\theta_i}{n_t\cos\theta_i+n_i\cos\theta_t}", "p-pol transmission coefficient", B_COLOR, 34, 22),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=3.5)
        eqs.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "For p-polarisation: r_parallel equals n_t cosine theta_i minus",
            "n_i cosine theta_t, all divided by n_t cosine theta_i plus n_i",
            "cosine theta_t.",])
        b.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class FresnelEquations_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p8.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"r=\frac{n_i-n_t}{n_i+n_t}", "normal incidence — MEMORISE", GOLD, 46, 26),
            labeled_eq(r"t=\frac{2n_i}{n_i+n_t}", "normal incidence transmission", GOLD, 46, 26),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=3.5)
        eqs.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "At normal incidence — when the light hits straight on — both",
            "polarisations give the same result: r equals n_i minus n_t",
            "over n_i plus n_t. This is a very useful formula to remember.",])
        b.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class FresnelEquations_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p9.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's work through a full example. Air to glass, n_i equals",
            "1.0, n_t equals 1.5, theta_i equals 40 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p10.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 1: Snell's law gives sine theta_t equals 1.0 over 1.5",
            "times sine 40 degrees equals 0.4285, so theta_t equals 25.37",
            "degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p11.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 2: compute the cosines. Cosine 40 is 0.766, cosine 25.37",
            "is 0.9036.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p12(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p12.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 3: plug into the Fresnel equations. r_perp comes out to",
            "minus 0.278. The negative sign means a phase flip on",
            "reflection. r_parallel comes out to plus 0.119 — a smaller",
            "reflection with no phase flip.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelEquations_p13(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelEquations_p13.mp3", time_offset=0)
        title = Text("The Fresnel Equations", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The p-polarisation reflects less. This will become important",
            "when we discuss Brewster's angle.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p1.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass at 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Let's go through a complete Fresnel calculation for air to",
            "glass at 40 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p2.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass at 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 1: use Snell's law to find the refraction angle. Sin of",
            "theta_t equals 1.0 over 1.5 times sin 40, giving theta_t",
            "equals 25.37 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p3.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass at 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 2: compute the cosines. Cosine 40 is 0.766, cosine 25.37",
            "is 0.9036.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p4.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass at 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Step 3: plug into the Fresnel equations for r_perp and",
            "r_parallel. We get minus 0.278 for s-polarisation and plus",
            "0.119 for p-polarisation. The negative sign on r_perp means a",
            "phase flip upon reflection.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class FresnelFullExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FresnelFullExample_p5.mp3", time_offset=0)
        title = Text("Full Fresnel Example: Air to Glass at 40 degrees", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The p-polarisation reflects significantly less than s at this",
            "angle — this difference grows with angle and reaches zero at",
            "Brewster's angle.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p1.mp3", time_offset=0)
        title = Text("Reflectivity, Transmissivity and Energy Conservation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The Fresnel coefficients r and t give amplitude ratios. To",
            "find the fraction of energy, we need the reflectivity R and",
            "transmissivity T.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p2.mp3", time_offset=0)
        title = Text("Reflectivity, Transmissivity and Energy Conservation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"R=|r|^2", "reflectivity (energy)", INTENSITY_COLOR, 44, 26),
            labeled_eq(r"T=\frac{n_t\cos\theta_t}{n_i\cos\theta_i}|t|^2", "transmissivity (energy, NOT |t|^2)", INTENSITY_COLOR, 44, 26),
            labeled_eq(r"R+T=1", "energy conservation — always check!", GOLD, 44, 26),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=4.5)
        eqs.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "Reflectivity is simply the square of the amplitude reflection",
            "coefficient: R equals r squared. At normal incidence from air",
            "to glass with n equals 1.5, R equals 4 percent. This is why",
            "glass surfaces look slightly shiny.",])
        b.next_to(eqs, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p3.mp3", time_offset=0)
        title = Text("Reflectivity, Transmissivity and Energy Conservation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Transmissivity T is not simply t squared — we also need to",
            "account for the change in beam cross-section and refractive",
            "index: T equals n_t cos theta_t over n_i cos theta_i, times t",
            "squared.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class ReflectivityTransmissivity_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ReflectivityTransmissivity_p4.mp3", time_offset=0)
        title = Text("Reflectivity, Transmissivity and Energy Conservation", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Energy conservation demands R plus T equals one. This is a",
            "useful sanity check: if your answer doesn't satisfy it, you",
            "made an error.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p1.mp3", time_offset=0)
        title = Text("Brewster's Angle and Total Internal Reflection", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Brewster's angle is the special angle at which p-polarised",
            "light has exactly zero reflectivity. The reflected beam is",
            "then purely s-polarised.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p2.mp3", time_offset=0)
        title = Text("Brewster's Angle and Total Internal Reflection", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The formula is simple: tangent of theta_B equals n_t over n_i.",
            "For air to glass with n equals 1.5, theta_B is 56.3 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class BrewsterTIR_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p3.mp3", time_offset=0)
        title = Text("Brewster's Angle and Total Internal Reflection", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        brew = labeled_eq(r"\tan\theta_B = n_t/n_i", "Brewster's angle  (r_p = 0)", E_COLOR, 48, 26)
        tir  = labeled_eq(r"\sin\theta_c = n_t/n_i\quad(n_i>n_t)", "critical angle for TIR", B_COLOR, 48, 26)
        eqs = VGroup(brew, tir).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        eqs.next_to(title, DOWN, buff=0.45)
        b = txt_block([            "At Brewster's angle, the reflected and refracted rays are",
            "exactly perpendicular to each other. This is the physical",
            "reason for zero p-reflectivity: the oscillating dipoles in the",
            "medium cannot radiate in the direction of the reflected beam.",])
        b.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)

class BrewsterTIR_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/BrewsterTIR_p4.mp3", time_offset=0)
        title = Text("Brewster's Angle and Total Internal Reflection", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Total internal reflection occurs when light tries to go from a",
            "denser medium to a less dense one, and the angle exceeds the",
            "critical angle. Above theta_c, ALL light is reflected — R",
            "equals exactly 1. The critical angle satisfies sine theta_c",
            "equals n_t over n_i. For glass to air, this is 41.8 degrees.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p1.mp3", time_offset=0)
        title = Text("Malus's Law", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Malus's law describes what happens when linearly polarised",
            "light passes through a polariser.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p2.mp3", time_offset=0)
        title = Text("Malus's Law", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I = I_0\cos^2\theta", font_size=60, color=INTENSITY_COLOR)
        safe_scale(eq)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(gold_box(eq)))
        b = txt_block([            "The transmitted intensity is I naught times cosine squared",
            "theta, where theta is the angle between the incoming",
            "polarisation direction and the polariser's transmission axis.",])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p3.mp3", time_offset=0)
        title = Text("Malus's Law", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "The physical reason: only the component of E along the",
            "transmission axis passes through. That component has amplitude",
            "E_0 cosine theta. Squaring to get intensity gives the cosine",
            "squared factor.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class MalusLaw_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MalusLaw_p4.mp3", time_offset=0)
        title = Text("Malus's Law", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "At theta equals zero, full transmission. At 45 degrees, half",
            "the intensity. At 90 degrees — crossed polarisers — zero",
            "transmission. This is why two crossed polarising filters block",
            "all light completely.",
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

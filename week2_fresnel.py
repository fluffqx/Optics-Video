# week2_fresnel.py  —  Week 2: Reflection, Refraction & Fresnel Equations  (v2)
# Source: Bennett Ch. 3.2-3.6, 4.1-4.2
from manim import *
from utils import *


class Week2TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEK 2",
            "Reflection, Refraction & Fresnel Equations",
            "Bennett Ch. 3.2–3.6, 4.1–4.2"
        )
        self.play(FadeIn(card, shift=UP)); self.wait(66.8); self.play(FadeOut(card))


class Week2Intro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("What Happens When Light Hits an Interface?", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Reflection and refraction occur whenever light enters a new medium",
            "where the refractive index n changes value  (Bennett Section 3.2).",
            "",
            "There are two fundamental questions we must answer:",
            "1. IN WHICH DIRECTION does the reflected/transmitted light travel?",
            "   → Answered by the Law of Reflection and Snell's Law.",
            "2. HOW MUCH light is reflected and how much transmitted?",
            "   → Answered by the Fresnel Equations.",
            "",
            "Snell's law was discovered experimentally in the 1600s.",
            "The Fresnel equations were derived from Maxwell in the 1800s.",
            "Together they completely describe electromagnetic wave behaviour at interfaces.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(8.8)
        self.wait(46.3); self.play(FadeOut(VGroup(title, intro)))


class FermatPrinciple(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Fermat's Principle of Least Time", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Before Maxwell, Fermat (1657) derived both the law of reflection AND Snell's",
            "law from a single elegant variational principle  (Bennett Section 3.2.1):",
            "",
            "\"Light travels between two points along the path that takes the LEAST TIME.\"",
            "",
            "Since time = distance / speed, and speed = c/n varies between media,",
            "the minimum-time path bends at the interface — this IS Snell's law.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(14.9)
        self.wait(41.4); self.play(FadeOut(intro))

        # Fermat → Snell derivation outline
        deriv_title = Text("Fermat → Snell's Law  (Bennett Example 3.2.1):", font_size=30, color=GOLD)
        deriv_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(deriv_title))

        solver = StepSolver(self, deriv_title, start_buff=0.4)
        solver.add_step(1,
            r"t_{\text{total}} = \frac{\sqrt{s^2+x^2}}{v_i} + \frac{\sqrt{d^2+(\rho-x)^2}}{v_t}",
            "total travel time from S (medium 1) to D (medium 2) via crossing point x")
        solver.add_step(2,
            r"\frac{dt}{dx} = \frac{1}{v_i}\frac{x}{\sqrt{s^2+x^2}} - \frac{1}{v_t}\frac{\rho-x}{\sqrt{d^2+(\rho-x)^2}} = 0",
            "minimise time: set derivative to zero; identify sin(θ_i) and sin(θ_t)")
        solver.add_step(3,
            r"\frac{\sin\theta_i}{v_i} = \frac{\sin\theta_t}{v_t} \quad\Rightarrow\quad n_i\sin\theta_i = n_t\sin\theta_t",
            "using v = c/n: Snell's law emerges from Fermat's principle! ✓", GOLD)
        solver.finalize())


class ReflectionRefraction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Law of Reflection & Snell's Law", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # Setup definitions
        setup = section_intro([
            "All angles are measured from the SURFACE NORMAL (perpendicular to surface),",
            "NOT from the surface itself. This is a common source of errors.",
            "The incident, reflected, and refracted rays all lie in one plane: the PLANE OF INCIDENCE.",
        ])
        setup.next_to(title, DOWN, buff=0.4)
        for l in setup: self.play(FadeIn(l)); self.wait(23.7)
        self.wait(13.8); self.play(FadeOut(setup))

        # Law of reflection
        refl_title = Text("Law of Reflection  (Bennett Eq. 3.3):", font_size=30, color=GOLD)
        refl_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(refl_title))

        refl = MathTex(r"\theta_i = \theta_r", font_size=64, color=ANGLE_COLOR)
        refl.next_to(refl_title, DOWN, buff=0.3)
        self.play(Write(refl)); self.wait(21.0)

        refl_desc = section_intro([
            "The angle of incidence = angle of reflection.  Always, for any wavelength, any material.",
            "Both angles measured from the surface normal.",
            "This holds for both specular (smooth surface) and can be derived from Maxwell.",
        ], font_size=26)
        refl_desc.next_to(refl, DOWN, buff=0.35)
        for l in refl_desc: self.play(FadeIn(l)); self.wait(22.1)
        self.wait(9.4); self.play(FadeOut(VGroup(refl_title, refl, refl_desc)))

        # Snell's Law
        snell_title = Text("Snell's Law of Refraction  (Bennett Eq. 3.4):", font_size=30, color=GOLD)
        snell_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(snell_title))

        snell = MathTex(r"n_i\sin\theta_i = n_t\sin\theta_t", font_size=60, color=N_COLOR)
        snell.next_to(snell_title, DOWN, buff=0.3)
        self.play(Write(snell)); self.wait(6.6)

        snell_sym = eq_table([
            (r"n_i", "refractive index of incident medium (where light comes FROM)", N_COLOR),
            (r"n_t", "refractive index of transmitted medium (where light goes TO)", N_COLOR),
            (r"\theta_i", "angle of incidence — measured from the normal", ANGLE_COLOR),
            (r"\theta_t", "angle of refraction (transmission angle) — measured from the normal", ANGLE_COLOR),
        ], eq_fs=30, lbl_fs=24, buff=0.25)
        snell_sym.next_to(snell, DOWN, buff=0.35)
        for row in snell_sym: self.play(FadeIn(row)); self.wait(5.5)
        self.wait(14.9); self.play(FadeOut(VGroup(snell_title, snell, snell_sym)))

        # Physical intuition
        intuition = section_intro([
            "Physical intuition: when n_t > n_i (going INTO denser medium),",
            "the light SLOWS DOWN and bends TOWARD the normal (θ_t < θ_i).",
            "When n_t < n_i (going INTO less dense medium),",
            "the light SPEEDS UP and bends AWAY from the normal (θ_t > θ_i).",
            "This is directly analogous to how a car slows down on gravel —",
            "if the front wheels hit the gravel first, the car turns toward the gravel.",
        ], font_size=26)
        intuition.next_to(title, DOWN, buff=0.45)
        for l in intuition: self.play(FadeIn(l)); self.wait(2.0)
        self.wait(2.0); self.play(FadeOut(intuition))

        # Worked example
        ex_title = Text("Example: air (n=1.0) → glass (n=1.5), θ_i = 40°", font_size=30, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"n_i\sin\theta_i = n_t\sin\theta_t \quad\Rightarrow\quad \sin\theta_t = \frac{n_i}{n_t}\sin\theta_i",
            "rearrange Snell's law to solve for θ_t")
        solver.add_step(2,
            r"\sin\theta_t = \frac{1.0}{1.5}\sin 40^{\circ} = \frac{1.0}{1.5}\times0.6428 = 0.4285",
            "substitute values: n_i=1.0, n_t=1.5, sin(40°)=0.6428")
        solver.add_step(3,
            r"\theta_t = \arcsin(0.4285) = 25.4^{\circ}",
            "angle of refraction — light bends TOWARD the normal as expected (25.4° < 40°)", ANGLE_COLOR)
        solver.add_step(4,
            r"\text{Check: } n_i\sin\theta_i = 1.0\times0.643 = 0.643, \quad n_t\sin\theta_t = 1.5\times0.429 = 0.643\;\checkmark",
            "always verify with a back-substitution", GOLD)
        solver.finalize())


class FresnelEquationsDerivation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Where the Fresnel Equations Come From", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Bennett Section 3.3 derives the Fresnel equations from Maxwell's equations",
            "using boundary conditions at the interface.",
            "",
            "The boundary conditions are:",
            "→ Tangential component of E must be CONTINUOUS across the interface",
            "→ Tangential component of B must be CONTINUOUS across the interface",
            "",
            "We split the incident electric field into two independent polarisation components:",
            "s-polarisation (⊥, TE): E-field PERPENDICULAR to the plane of incidence",
            "p-polarisation (∥, TM): E-field PARALLEL to the plane of incidence",
            "",
            "These two components experience DIFFERENT boundary conditions,",
            "so they reflect and transmit with different amplitude ratios.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(6.6)
        self.wait(50.2); self.play(FadeOut(VGroup(title, intro)))


class FresnelEquations(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("The Fresnel Equations", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # s-polarisation
        s_header = Text("s-POLARISATION  (E perpendicular to plane of incidence)  Bennett Eq. 3.17–3.18:", font_size=24, color=E_COLOR)
        s_header.next_to(title, DOWN, buff=0.5)
        safe_scale(s_header, max_width=13.5)
        self.play(Write(s_header))

        r_s = labeled_eq(
            r"r_\perp = \frac{n_i\cos\theta_i - n_t\cos\theta_t}{n_i\cos\theta_i + n_t\cos\theta_t}",
            "amplitude REFLECTION coefficient for s-polarisation  (dimensionless, can be negative)", E_COLOR, 38, 23)
        t_s = labeled_eq(
            r"t_\perp = \frac{2n_i\cos\theta_i}{n_i\cos\theta_i + n_t\cos\theta_t}",
            "amplitude TRANSMISSION coefficient for s-polarisation  (dimensionless, always positive)", E_COLOR, 38, 23)
        s_eqs = VGroup(r_s, t_s).arrange(DOWN, buff=0.38)
        s_eqs.next_to(s_header, DOWN, buff=0.3)
        safe_scale(s_eqs, max_height=3.0)
        self.play(Write(r_s)); self.wait(13.8)
        self.play(Write(t_s)); self.wait(10.5)
        self.play(FadeOut(VGroup(s_header, s_eqs)))

        # p-polarisation
        p_header = Text("p-POLARISATION  (E parallel to plane of incidence)  Bennett Eq. 3.22–3.23:", font_size=24, color=B_COLOR)
        p_header.next_to(title, DOWN, buff=0.5)
        safe_scale(p_header, max_width=13.5)
        self.play(Write(p_header))

        r_p = labeled_eq(
            r"r_\parallel = \frac{n_t\cos\theta_i - n_i\cos\theta_t}{n_t\cos\theta_i + n_i\cos\theta_t}",
            "amplitude REFLECTION coefficient for p-polarisation — note the SWAPPED n's in numerator!", B_COLOR, 38, 23)
        t_p = labeled_eq(
            r"t_\parallel = \frac{2n_i\cos\theta_i}{n_t\cos\theta_i + n_i\cos\theta_t}",
            "amplitude TRANSMISSION coefficient for p-polarisation", B_COLOR, 38, 23)
        p_eqs = VGroup(r_p, t_p).arrange(DOWN, buff=0.38)
        p_eqs.next_to(p_header, DOWN, buff=0.3)
        safe_scale(p_eqs, max_height=3.0)
        self.play(Write(r_p)); self.wait(21.0)
        self.play(Write(t_p)); self.wait(12.7))

        # Normal incidence — simplification
        norm_title = Text("Special Case: Normal Incidence  (θ_i = θ_t = 0°):", font_size=30, color=GOLD)
        norm_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(norm_title))

        r_norm = labeled_eq(
            r"r = \frac{n_i - n_t}{n_i + n_t}",
            "both polarisations give the SAME result at normal incidence — memorise this!", GOLD, 52, 26)
        t_norm = labeled_eq(
            r"t = \frac{2n_i}{n_i + n_t}",
            "transmission amplitude at normal incidence", GOLD, 52, 26)
        norm_eqs = VGroup(r_norm, t_norm).arrange(DOWN, buff=0.4)
        norm_eqs.next_to(norm_title, DOWN, buff=0.35)
        safe_scale(norm_eqs, max_height=3.5)
        self.play(Write(r_norm)); self.wait(13.8)
        self.play(Write(t_norm)); self.wait(11.6)
        self.play(Create(gold_box(r_norm)))
        self.wait(87.3); self.play(FadeOut(VGroup(title, norm_title, norm_eqs)))


class FresnelFullExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Fresnel Full Example: air→glass, θ_i=40°", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        given = section_intro([
            "Given:  n_i = 1.000 (air),  n_t = 1.500 (glass),  θ_i = 40.0°",
            "Find:   r_⊥, t_⊥, r_∥, t_∥  for both polarisations",
        ], font_size=28)
        given.next_to(title, DOWN, buff=0.4)
        for l in given: self.play(FadeIn(l)); self.wait(7.7)
        self.wait(51.3)

        solver = StepSolver(self, given, start_buff=0.4)
        solver.add_step(1,
            r"\sin\theta_t = \frac{n_i}{n_t}\sin\theta_i = \frac{1.0}{1.5}\sin40^{\circ} = 0.4285"
            r"\quad\Rightarrow\quad\theta_t = 25.37^{\circ}",
            "Step 1: Snell's law to find θ_t first", ANGLE_COLOR)
        solver.add_step(2,
            r"\cos\theta_i = \cos40^{\circ} = 0.7660, \quad \cos\theta_t = \cos25.37^{\circ} = 0.9036",
            "Step 2: compute the cosines needed for Fresnel equations")
        solver.add_step(3,
            r"r_\perp = \frac{1.0\times0.7660 - 1.5\times0.9036}{1.0\times0.7660 + 1.5\times0.9036}"
            r"= \frac{0.766-1.355}{0.766+1.355} = \frac{-0.589}{2.121} = -0.278",
            "r_⊥ = −0.278: negative sign means π phase shift upon reflection", E_COLOR)
        solver.add_step(4,
            r"t_\perp = \frac{2\times1.0\times0.7660}{2.121} = \frac{1.532}{2.121} = 0.722",
            "t_⊥ = +0.722: always positive for s-polarisation", E_COLOR)
        solver.add_step(5,
            r"r_\parallel = \frac{1.5\times0.7660 - 1.0\times0.9036}{1.5\times0.7660 + 1.0\times0.9036}"
            r"= \frac{1.149-0.904}{1.149+0.904} = \frac{0.245}{2.053} = +0.119",
            "r_∥ = +0.119: positive, no phase shift — less reflection than s-pol", B_COLOR)
        solver.add_step(6,
            r"t_\parallel = \frac{2\times1.0\times0.7660}{1.5\times0.7660+1.0\times0.9036}"
            r"= \frac{1.532}{2.053} = 0.746",
            "t_∥ = +0.746: transmission amplitude for p-polarisation", B_COLOR)
        solver.finalize())


class ReflectivityTransmissivity(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Reflectivity and Transmissivity", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "The Fresnel coefficients r and t give AMPLITUDE ratios.",
            "For energy (power, irradiance), we need the INTENSITY ratios:",
            "Reflectivity R and Transmissivity T  (Bennett Section 3.6).",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(12.7)
        self.wait(20.4); self.play(FadeOut(intro))

        eqs = eq_table([
            (r"R = |r|^2 = r\cdot r^*",
             "Reflectivity: fraction of INTENSITY reflected  [dimensionless, 0 to 1]", INTENSITY_COLOR),
            (r"T = \frac{n_t\cos\theta_t}{n_i\cos\theta_i}|t|^2",
             "Transmissivity: fraction of INTENSITY transmitted  [dimensionless, 0 to 1]", INTENSITY_COLOR),
            (r"R + T = 1",
             "Energy conservation: reflected + transmitted = incident  (assuming no absorption)", GOLD),
            (r"R_{\text{normal}} = \left(\frac{n_i-n_t}{n_i+n_t}\right)^2, \quad T_{\text{normal}} = \frac{4n_in_t}{(n_i+n_t)^2}",
             "normal-incidence formulas — often used for quick estimates", INTENSITY_COLOR),
        ], eq_fs=32, lbl_fs=23, buff=0.32)
        eqs.next_to(title, DOWN, buff=0.5)
        for row in eqs: self.play(FadeIn(row)); self.wait(18.8)
        self.wait(13.2); self.play(FadeOut(eqs))

        # Why T ≠ |t|²
        why_title = Text("Why T ≠ |t|²?  (Bennett Section 3.6 — important!)", font_size=30, color=GOLD)
        why_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(why_title))

        why = section_intro([
            "The transmitted beam travels in a different medium (different n) at a different",
            "angle — so the beam cross-section changes at the interface.",
            "The factor n_t cos(θ_t) / n_i cos(θ_i) corrects for this geometric effect.",
            "When this factor > 1: more energy per unit area is transmitted than you'd expect.",
            "Check: R + T = 1 — if your answer doesn't satisfy this, you made an error.",
        ], font_size=26)
        why.next_to(why_title, DOWN, buff=0.35)
        for l in why: self.play(FadeIn(l)); self.wait(2.0)
        self.wait(2.0); self.play(FadeOut(VGroup(why_title, why)))

        # Worked example
        ex_title = Text("Example: air→glass n=1.5, normal incidence", font_size=30, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"r = \frac{n_i-n_t}{n_i+n_t} = \frac{1.0-1.5}{1.0+1.5} = \frac{-0.5}{2.5} = -0.200",
            "amplitude reflection coefficient at normal incidence")
        solver.add_step(2,
            r"R = r^2 = (-0.200)^2 = 0.040 = 4.0\%",
            "4% of light is reflected — this is why windows look slightly glassy!", INTENSITY_COLOR)
        solver.add_step(3,
            r"T = 1 - R = 1 - 0.040 = 0.960 = 96.0\%",
            "96% is transmitted — consistent with energy conservation", INTENSITY_COLOR)
        solver.add_step(4,
            r"\text{A window (2 surfaces): }T_{\text{total}} = 0.96^2 = 0.922 = 92.2\%",
            "two glass-air interfaces means about 8% total reflection loss", GOLD)
        solver.finalize())


class BrewsterTIR(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Brewster's Angle & Total Internal Reflection", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # Brewster's angle
        brew_title = Text("Brewster's Angle  (Bennett Section 3.5.2):", font_size=30, color=GOLD)
        brew_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(brew_title))

        brew_intro = section_intro([
            "At one specific angle of incidence — Brewster's angle θ_B — the p-polarisation",
            "has ZERO reflectivity: R_∥ = 0.  The reflected beam is then purely s-polarised.",
            "",
            "Physical reason: at Brewster's angle, the reflected ray and refracted ray are",
            "exactly PERPENDICULAR to each other: θ_i + θ_t = 90^{\circ}.",
            "The oscillating dipoles in the material cannot radiate in their oscillation",
            "direction — so p-polarisation (which oscillates along the reflected ray direction)",
            "produces zero reflection.",
        ], font_size=25)
        brew_intro.next_to(brew_title, DOWN, buff=0.3)
        for l in brew_intro: self.play(FadeIn(l)); self.wait(11.6)
        self.wait(12.7); self.play(FadeOut(VGroup(brew_title, brew_intro)))

        brew_eq_title = Text("Brewster's Angle Formula  (Bennett Eq. 3.31):", font_size=30, color=GOLD)
        brew_eq_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(brew_eq_title))

        brew = MathTex(r"\tan\theta_B = \frac{n_t}{n_i}", font_size=60, color=ANGLE_COLOR)
        brew.next_to(brew_eq_title, DOWN, buff=0.3)
        self.play(Write(brew)); self.wait(20.4)

        brew_ex = section_intro([
            "Example: air (n=1.0) → glass (n=1.5):",
            "θ_B = arctan(1.5/1.0) = arctan(1.5) = 56.3°",
            "",
            "Applications: polarising beamsplitters, laser Brewster windows,",
            "anti-glare sunglasses (polarised lenses block the s-polarised glare",
            "from horizontal surfaces which reflects near Brewster's angle).",
        ], font_size=26)
        brew_ex.next_to(brew, DOWN, buff=0.35)
        for l in brew_ex: self.play(FadeIn(l)); self.wait(33.7)
        self.play(Create(gold_box(brew)))
        self.wait(2.0); self.play(FadeOut(VGroup(brew_eq_title, brew, brew_ex)))

        # TIR
        tir_title = Text("Total Internal Reflection (TIR)  (Bennett Section 3.5.3):", font_size=28, color=GOLD)
        tir_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(tir_title))

        tir_intro = section_intro([
            "TIR occurs when light tries to go from a DENSER to a LESS DENSE medium (n_i > n_t),",
            "AND the angle of incidence exceeds the critical angle θ_c.",
            "Above θ_c: R = 1.000 exactly — ALL light is reflected, ZERO is transmitted.",
            "This is not an approximation — it follows exactly from Maxwell's equations.",
        ], font_size=26)
        tir_intro.next_to(tir_title, DOWN, buff=0.3)
        for l in tir_intro: self.play(FadeIn(l)); self.wait(2.0)
        self.wait(2.0); self.play(FadeOut(tir_intro))

        tir_eq_title = Text("Critical Angle Formula  (Bennett Eq. 3.35):", font_size=28, color=GOLD)
        tir_eq_title.next_to(tir_title, DOWN, buff=0.4)
        self.play(Write(tir_eq_title))

        tir_eq = MathTex(
            r"\sin\theta_c = \frac{n_t}{n_i} \quad (n_i > n_t \text{ required})",
            font_size=50, color=ANGLE_COLOR)
        tir_cond = MathTex(
            r"\theta_i \geq \theta_c \;\Rightarrow\; R = 1,\; T = 0",
            font_size=44, color=GOLD)
        tir_eqs = VGroup(tir_eq, tir_cond).arrange(DOWN, buff=0.4)
        tir_eqs.next_to(tir_eq_title, DOWN, buff=0.3)
        safe_scale(tir_eqs, max_height=2.5)
        self.play(Write(tir_eqs)); self.wait(2.0)

        tir_examples = section_intro([
            "glass (n=1.5) → air (n=1.0):  sin(θ_c) = 1.0/1.5 = 0.667  →  θ_c = 41.8°",
            "water (n=1.33) → air:  sin(θ_c) = 1/1.33 = 0.752  →  θ_c = 48.8°",
            "",
            "Applications of TIR: optical fibres, periscope prisms, diamond brilliance",
            "(diamond has n=2.42, θ_c=24.4° — almost everything gets TIR'd back out).",
        ], font_size=25)
        tir_examples.next_to(tir_eqs, DOWN, buff=0.35)
        for l in tir_examples: self.play(FadeIn(l)); self.wait(2.0)
        self.wait(2.0); self.play(FadeOut(VGroup(title, tir_title, tir_eq_title, tir_eqs, tir_examples)))


class MalusLaw(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Malus's Law", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "When polarised light passes through a linear polariser,",
            "only the component of E along the polariser's transmission axis passes through.",
            "If the incident polarisation makes angle θ with the transmission axis:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(7.2)
        self.wait(13.8); self.play(FadeOut(intro))

        malus = MathTex(r"I = I_0\cos^2\theta", font_size=64, color=INTENSITY_COLOR)
        malus.next_to(title, DOWN, buff=0.5)
        self.play(Write(malus)); self.wait(16.6)
        self.play(Create(gold_box(malus))); self.wait(17.7)

        sym = eq_table([
            (r"I_0", "incident intensity [W/m²]", INTENSITY_COLOR),
            (r"\theta", "angle between incident E-field direction and polariser transmission axis", ANGLE_COLOR),
            (r"I", "transmitted intensity [W/m²]", INTENSITY_COLOR),
        ], eq_fs=32, lbl_fs=24, buff=0.25)
        sym.next_to(malus, DOWN, buff=0.45)
        for row in sym: self.play(FadeIn(row)); self.wait(2.0)
        self.wait(2.0); self.play(FadeOut(sym))

        # Derivation idea
        why = section_intro([
            "Why cos²θ?  The transmitted E-field amplitude is E₀cos(θ).",
            "Since intensity ∝ E² ∝ |E|² = (E₀cosθ)² = E₀²cos²θ = I₀cos²θ.",
        ], font_size=26)
        why.next_to(malus, DOWN, buff=0.45)
        for l in why: self.play(FadeIn(l)); self.wait(2.0)
        self.wait(2.0); self.play(FadeOut(why))

        # Worked examples
        ex_title = Text("Worked Examples:", font_size=30, color=GOLD)
        ex_title.next_to(malus, DOWN, buff=0.45)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.35)
        solver.add_step(1,
            r"I_0=400\text{ W/m}^2,\;\theta=30^{\circ}:\quad I = 400\cos^2 30^{\circ} = 400\times0.75 = 300\text{ W/m}^2",
            "75% transmitted at 30^{\circ} — still most of the light")
        solver.add_step(2,
            r"I_0=400\text{ W/m}^2,\;\theta=45^{\circ}:\quad I = 400\cos^2 45^{\circ} = 400\times0.5 = 200\text{ W/m}^2",
            "50% transmitted at 45^{\circ} — half the intensity")
        solver.add_step(3,
            r"I_0=400\text{ W/m}^2,\;\theta=90^{\circ}:\quad I = 400\cos^2 90^{\circ} = 400\times0 = 0\text{ W/m}^2",
            "0% transmitted at 90^{\circ} — CROSSED polarisers block all light", GOLD)
        solver.add_step(4,
            r"N\text{ polarisers each at }\Delta\theta:\quad I_N = I_0\cos^{2N}(\Delta\theta)",
            "chain of polarisers: multiply cos² factors — used to rotate polarisation gradually")
        solver.finalize())

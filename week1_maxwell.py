# week1_maxwell.py  —  Week 1 (continued): Maxwell's Equations & EM Waves  (v2)
# Source: Bennett Ch. 2.1-2.5, 3.1-3.2, 3.9
from manim import *
from utils import *


class MaxwellIntro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Maxwell's Equations", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(0.5)

        intro = section_intro([
            "Maxwell's equations are the four fundamental laws of classical electromagnetism.",
            "Written down by James Clerk Maxwell in the 1860s, they unified electricity,",
            "magnetism, and optics into a single coherent theoretical framework.",
            "",
            "From these four equations alone, Maxwell predicted electromagnetic waves",
            "and computed their speed — getting exactly c = 2.998 × 10⁸ m/s.",
            "This immediately identified light as an electromagnetic wave.",
            "",
            "Bennett (Chapter 2) builds up these equations from physical principles.",
            "Understanding WHY each equation has its form is as important as knowing it.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(61.2); self.play(FadeOut(VGroup(title, intro)))


class VectorCalculusNotation(Scene):
    """Brief explanation of ∇· and ∇× before Maxwell equations"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Vector Calculus Notation — Essential Prerequisites", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Maxwell's equations use three differential operators. You must recognise them",
            "instantly and understand their physical meaning.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(0.3); self.play(FadeOut(intro))

        ops = [
            (r"\nabla\cdot\vec{F} = \frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}+\frac{\partial F_z}{\partial z}",
             "DIVERGENCE of F: measures how much F spreads outward from a point.\n"
             "Positive divergence → field lines radiate outward (source).\n"
             "Negative divergence → field lines converge inward (sink).",
             E_COLOR),
            (r"\nabla\times\vec{F} = \left(\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}\right)\hat{x}+\cdots",
             "CURL of F: measures how much F rotates around a point.\n"
             "Think of it as the 'rotation density' of the field.\n"
             "A paddle wheel placed in the field would spin if curl ≠ 0.",
             B_COLOR),
            (r"\nabla^2 F = \frac{\partial^2 F}{\partial x^2}+\frac{\partial^2 F}{\partial y^2}+\frac{\partial^2 F}{\partial z^2}",
             "LAPLACIAN of F: the 3D generalisation of the second derivative.\n"
             "Appears in both the wave equation AND Maxwell's derivation.",
             WAVE_COLOR),
        ]

        for latex, desc, color in ops:
            op_eq   = MathTex(latex, font_size=34, color=color)
            op_eq.next_to(title, DOWN, buff=0.5)
            safe_scale(op_eq, max_width=13.0)
            op_desc = section_intro(desc.split('\n'), font_size=26)
            op_desc.next_to(op_eq, DOWN, buff=0.4)
            self.play(Write(op_eq)); self.wait(0.5)
            for l in op_desc: self.play(FadeIn(l)); self.wait(0.8)
            self.wait(48.7)
            self.play(FadeOut(VGroup(op_eq, op_desc)))

        self.play(FadeOut(title))


class MaxwellEquations(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Maxwell's Equations in Matter", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        laws = [
            (
                r"\nabla\cdot\vec{E} = \frac{\rho_{\text{free}}}{\varepsilon}",
                "GAUSS'S LAW FOR E  (Bennett Eq. 2.5)",
                [
                    "Electric field lines DIVERGE from positive free charges.",
                    "The divergence of E equals the free charge density / permittivity.",
                    "Where there are no charges: ∇·E = 0  (field lines don't start/stop).",
                    "Physical picture: E field lines begin on + charges, end on − charges.",
                ],
                E_COLOR
            ),
            (
                r"\nabla\cdot\vec{B} = 0",
                "GAUSS'S LAW FOR B  (Bennett Eq. 2.6)",
                [
                    "The divergence of B is ALWAYS zero — no exceptions, ever.",
                    "This means magnetic monopoles do NOT exist.",
                    "All magnetic field lines form closed loops — no sources or sinks.",
                    "Every field line entering a closed surface must also leave it.",
                ],
                B_COLOR
            ),
            (
                r"\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t}",
                "FARADAY'S LAW  (Bennett Eq. 2.21)",
                [
                    "A time-changing magnetic field INDUCES a curling electric field.",
                    "The minus sign (Lenz's law): induced E opposes the change in B.",
                    "This is the principle behind electric generators and transformers.",
                    "No changing B → no induced E → curl E = 0.",
                ],
                E_COLOR
            ),
            (
                r"\nabla\times\vec{B} = \mu\vec{J}_{\text{free}} + \mu\varepsilon\frac{\partial\vec{E}}{\partial t}",
                "AMPERE-MAXWELL LAW  (Bennett Eq. 2.22)",
                [
                    "Both electric CURRENTS and time-changing E fields create curling B.",
                    "The second term μ₀ε₀ ∂E/∂t was Maxwell's crucial addition.",
                    "Without it, the equations would be inconsistent for EM waves.",
                    "This displacement current term allows light to propagate in vacuum.",
                ],
                B_COLOR
            ),
        ]

        for latex, law_name, desc_lines, color in laws:
            law_title = Text(law_name, font_size=26, color=GOLD)
            law_title.next_to(title, DOWN, buff=0.5)
            self.play(Write(law_title))

            eq = MathTex(latex, font_size=48, color=color)
            eq.next_to(law_title, DOWN, buff=0.3)
            safe_scale(eq, max_width=11.0)
            self.play(Write(eq)); self.wait(0.8)

            desc = section_intro(desc_lines, font_size=26)
            desc.next_to(eq, DOWN, buff=0.35)
            for l in desc: self.play(FadeIn(l)); self.wait(0.9)
            self.wait(129.8)
            self.play(FadeOut(VGroup(law_title, eq, desc)))

        self.play(FadeOut(title))


class MaxwellVacuum(Scene):
    """Maxwell equations in vacuum — the form used for EM waves"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Maxwell's Equations in Vacuum  (ρ=0, J=0)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "In empty space (no charges, no currents), the equations simplify.",
            "This is the form we use to derive electromagnetic wave propagation.",
            "Setting ρ=0 and J=0 in the general equations gives:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(0.3); self.play(FadeOut(intro))

        vac_eqs = VGroup(
            MathTex(r"\nabla\cdot\vec{E} = 0", font_size=46, color=E_COLOR),
            MathTex(r"\nabla\cdot\vec{B} = 0", font_size=46, color=B_COLOR),
            MathTex(r"\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t}", font_size=46, color=E_COLOR),
            MathTex(r"\nabla\times\vec{B} = \mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t}", font_size=46, color=B_COLOR),
        )
        vac_eqs.arrange(DOWN, buff=0.38)
        vac_eqs.next_to(title, DOWN, buff=0.5)
        safe_scale(vac_eqs, max_height=5.5)

        for eq in vac_eqs:
            self.play(Write(eq), run_time=0.9); self.wait(0.6)
        self.wait(1)

        constants = VGroup(
            MathTex(r"\varepsilon_0 = 8.854\times10^{-12} \text{ F/m}", font_size=28, color=N_COLOR),
            MathTex(r"\mu_0 = 1.257\times10^{-6} \text{ H/m}", font_size=28, color=N_COLOR),
            MathTex(r"c = \frac{1}{\sqrt{\varepsilon_0\mu_0}} = 2.998\times10^8 \text{ m/s}", font_size=30, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        constants.to_edge(RIGHT, buff=0.5)
        constants.shift(DOWN * 0.5)
        self.play(FadeIn(constants)); self.wait(51.0)
        self.play(FadeOut(VGroup(title, vac_eqs, constants)))


class EMWaveDerivation(Scene):
    """Derive the EM wave equation from Maxwell — step by step"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Deriving the EM Wave Equation from Maxwell", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Bennett Appendix B derives this explicitly. Here are the key steps.",
            "Start with Faraday's law: ∇×E = −∂B/∂t",
            "Take the curl of BOTH sides — this is the key trick:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(77.5); self.play(FadeOut(intro))

        solver = StepSolver(self, title, start_buff=0.55)

        solver.add_step(1,
            r"\nabla\times(\nabla\times\vec{E}) = \nabla\times\!\left(-\frac{\partial\vec{B}}{\partial t}\right) = -\frac{\partial}{\partial t}(\nabla\times\vec{B})",
            "take curl of Faraday; swap curl and time derivative (they commute)")

        solver.add_step(2,
            r"\nabla\times\vec{B} = \mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t} \quad\Rightarrow\quad "
            r"-\frac{\partial}{\partial t}(\nabla\times\vec{B}) = -\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}",
            "substitute Ampere-Maxwell law into right-hand side")

        solver.add_step(3,
            r"\nabla\times(\nabla\times\vec{E}) = \nabla(\nabla\cdot\vec{E}) - \nabla^2\vec{E} = -\nabla^2\vec{E}",
            "vector identity: curl-curl = grad(div) − Laplacian; use ∇·E=0 in vacuum")

        solver.add_step(4,
            r"\nabla^2\vec{E} = \mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2} \quad\Rightarrow\quad c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}",
            "EM wave equation! Compare with general form: c = 1/√(μ₀ε₀)", GOLD)

        solver.finalize()
        self.play(FadeOut(VGroup(title, *solver.steps)))


class EMWaveProperties(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Properties of Electromagnetic Waves", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "The plane wave solutions to Maxwell's equations (Bennett Eq. 2.28-2.30)",
            "have remarkable properties — all provable directly from Maxwell's equations.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.play(FadeOut(intro))

        properties = [
            ("Transverse", r"\vec{E}\perp\vec{k} \quad\text{and}\quad \vec{B}\perp\vec{k}",
             "Both E and B are perpendicular to the propagation direction k⃗.\n"
             "Proof: ∇·E=0 gives ik⃗·E⃗=0, so k⃗⊥E⃗.  Same for B⃗.", E_COLOR),
            ("Mutually perpendicular", r"\vec{E}\perp\vec{B} \quad\text{and}\quad \vec{E}\times\vec{B}\parallel\vec{k}",
             "E and B are perpendicular to each other.\n"
             "The cross product E⃗×B⃗ points in the direction of energy flow (= k⃗ direction).\n"
             "E⃗, B⃗, k⃗ form a right-handed coordinate system.", B_COLOR),
            ("Amplitude ratio", r"E = vB \quad (E = cB \text{ in vacuum})\quad\Leftarrow\quad \vec{k}\times\vec{E}=\omega\vec{B}",
             "The magnitudes of E and B are always in ratio v (or c in vacuum).\n"
             "Derived from Faraday's law applied to the plane wave solution.", GOLD),
            ("In phase", r"E\text{ and }B\text{ are IN PHASE — they reach maxima simultaneously}",
             "Both fields oscillate with the same kx−ωt dependence.\n"
             "There is no phase lag between E and B.", WHITE),
            ("Refractive index", r"n = \sqrt{K_E} \quad (K_E = \varepsilon/\varepsilon_0) \quad v = \frac{c}{n}",
             "In a material with relative permittivity K_E (and μ_r≈1).\n"
             "The wave slows down by factor n compared to vacuum.", N_COLOR),
        ]

        for prop_name, latex, desc, color in properties:
            prop_title = Text(prop_name + ":", font_size=30, color=GOLD)
            prop_title.next_to(title, DOWN, buff=0.5)
            self.play(Write(prop_title))

            eq = MathTex(latex, font_size=38, color=color)
            eq.next_to(prop_title, DOWN, buff=0.3)
            safe_scale(eq, max_width=13.0)
            self.play(Write(eq)); self.wait(0.7)

            desc_mob = section_intro(desc.split('\n'), font_size=26)
            desc_mob.next_to(eq, DOWN, buff=0.35)
            for l in desc_mob: self.play(FadeIn(l)); self.wait(0.8)
            self.wait(52.1); self.play(FadeOut(VGroup(prop_title, eq, desc_mob)))

        self.play(FadeOut(title))


class EMWaveExample(Scene):
    """Full example: find B from given E — Bennett Example 2.3"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Example: Finding B from E  (Bennett Ex. 2.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        prob = section_intro([
            "A plane EM wave in vacuum is described by:",
        ])
        prob.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(prob[0]))

        E_field = MathTex(
            r"\vec{E}(x,y,z,t) = E_0\,\hat{x}\,e^{i(kz-\omega t)}",
            font_size=44, color=E_COLOR)
        E_field.next_to(prob, DOWN, buff=0.3)
        self.play(Write(E_field)); self.wait(1)

        find = Text("Find: the magnetic field B⃗(x,y,z,t)", font_size=30, color=WHITE)
        find.next_to(E_field, DOWN, buff=0.3)
        self.play(FadeIn(find)); self.wait(46.8)

        solver = StepSolver(self, find, start_buff=0.4)

        solver.add_step(1,
            r"\hat{k} = \hat{z} \quad\text{(propagation in the +z direction)}",
            "read propagation direction from the exponent ikz")

        solver.add_step(2,
            r"\vec{k}\times\vec{E} = \omega\vec{B} \quad\Rightarrow\quad \vec{B} = \frac{\vec{k}\times\vec{E}}{\omega}",
            "from Faraday's law applied to plane waves (Bennett Eq. 2.31)")

        solver.add_step(3,
            r"\vec{k}\times\vec{E} = k\hat{z}\times E_0\hat{x}\,e^{i(kz-\omega t)} = kE_0(\hat{z}\times\hat{x})\,e^{i(kz-\omega t)}",
            "k⃗ = kẑ, E⃗ = E₀x̂ e^(...); perform the cross product")

        solver.add_step(4,
            r"\hat{z}\times\hat{x} = \hat{y} \quad\Rightarrow\quad \vec{B} = \frac{kE_0}{\omega}\hat{y}\,e^{i(kz-\omega t)} = \frac{E_0}{c}\hat{y}\,e^{i(kz-\omega t)}",
            "using k/ω = 1/v = 1/c in vacuum;  B is in the y-direction", B_COLOR)

        solver.add_step(5,
            r"\vec{E}\perp\vec{B}\perp\vec{k}: \quad \hat{x}\perp\hat{y}\perp\hat{z}\quad\checkmark",
            "confirms the mutually perpendicular property of EM waves", GOLD)

        solver.finalize()
        self.play(FadeOut(VGroup(title, prob, E_field, find, *solver.steps)))


class PoyntingIrradiance(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Poynting Vector & Irradiance", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Electromagnetic waves carry energy. The Poynting vector describes",
            "HOW MUCH energy flows, and IN WHICH DIRECTION (Bennett Section 2.3.2).",
            "",
            "The Poynting vector S⃗ gives the power per unit area [W/m²],",
            "flowing in the direction of E⃗ × B⃗ = direction of k⃗.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.5); self.play(FadeOut(intro))

        # Poynting vector definition
        S_title = Text("The Poynting Vector  (Bennett Eq. 2.35):", font_size=30, color=GOLD)
        S_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(S_title))

        S_eq = MathTex(
            r"\vec{S} = \frac{1}{\mu_0}\vec{E}\times\vec{B} \quad [\text{W/m}^2]",
            font_size=52, color=INTENSITY_COLOR)
        S_eq.next_to(S_title, DOWN, buff=0.3)
        self.play(Write(S_eq)); self.wait(1.2)

        S_desc = section_intro([
            "S⃗ points in the direction of energy flow (same as k⃗).",
            "Its magnitude |S| is the power per unit area (intensity).",
            "S⃗ oscillates in time — we need the TIME AVERAGE for practical use.",
        ], font_size=26)
        S_desc.next_to(S_eq, DOWN, buff=0.35)
        for l in S_desc: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(1); self.play(FadeOut(VGroup(S_title, S_eq, S_desc)))

        # Irradiance
        I_title = Text("Irradiance I = Time-averaged Poynting Magnitude  (Bennett Eq. 2.38):", font_size=28, color=GOLD)
        I_title.next_to(title, DOWN, buff=0.5)
        safe_scale(I_title, max_width=13.0)
        self.play(Write(I_title))

        I_eq = MathTex(
            r"I \equiv \langle|\vec{S}|\rangle_T = \frac{n\varepsilon_0 c}{2}E_0^2",
            font_size=52, color=INTENSITY_COLOR)
        I_eq.next_to(I_title, DOWN, buff=0.35)
        self.play(Write(I_eq)); self.wait(1)

        half_note = section_intro([
            "Where does the factor of ½ come from?",
            "Time average of cos²(ωt) over one full period = ½.",
            "⟨cos²(ωt)⟩_T = (1/T)∫₀ᵀ cos²(ωt) dt = ½",
            "This is a very frequently-needed result — commit it to memory.",
        ], font_size=26)
        half_note.next_to(I_eq, DOWN, buff=0.35)
        for l in half_note: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(129.6); self.play(FadeOut(VGroup(I_title, I_eq, half_note)))

        # Worked example
        ex_title = Text("Example: Green Laser, Power=5.0 mW, beam radius=1.0 mm", font_size=28, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        safe_scale(ex_title, max_width=13.0)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"A = \pi r^2 = \pi(10^{-3})^2 = 3.14\times10^{-6} \text{ m}^2",
            "cross-sectional area of the beam")
        solver.add_step(2,
            r"I = \frac{P}{A} = \frac{5.0\times10^{-3}}{3.14\times10^{-6}} = 1592 \text{ W/m}^2",
            "irradiance = power / area", INTENSITY_COLOR)
        solver.add_step(3,
            r"E_0 = \sqrt{\frac{2I}{n\varepsilon_0 c}} = \sqrt{\frac{2\times1592}{1\times8.85\times10^{-12}\times3\times10^8}} = 1094 \text{ V/m}",
            "peak electric field amplitude (n=1 for air)", E_COLOR)
        solver.add_step(4,
            r"B_0 = \frac{E_0}{c} = \frac{1094}{3\times10^8} = 3.65\times10^{-6} \text{ T} = 3.65\;\mu\text{T}",
            "peak magnetic field amplitude", B_COLOR)
        solver.finalize()
        self.play(FadeOut(VGroup(title, ex_title, *solver.steps)))


class RadiationPressure(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Radiation Pressure — Light Carries Momentum", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Light carries MOMENTUM as well as energy. This leads to radiation pressure.",
            "Bennett Section 2.3.2 derives this from electromagnetic energy density.",
            "The momentum density of an EM wave: g = S/c²  [kg/(m²·s)]",
            "",
            "When light hits a surface, it transfers momentum — exerting a force.",
            "For an ABSORBING surface (all light absorbed): radiation pressure = I/c",
            "For a REFLECTING surface (all light reflected): pressure = 2I/c",
            "   (factor of 2 because momentum REVERSES — like a ball bouncing off a wall)",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(0.5); self.play(FadeOut(intro))

        # Equations
        P_title = Text("Radiation Pressure Formulas  (Bennett Eq. 2.43):", font_size=30, color=GOLD)
        P_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(P_title))

        pabs  = labeled_eq(r"P_{\text{abs}} = \frac{I}{c}", "absorbed surface  [Pa = N/m²]", INTENSITY_COLOR, 50, 26)
        prefl = labeled_eq(r"P_{\text{refl}} = \frac{2I}{c}", "perfectly reflecting surface — 2\times  because momentum reverses", INTENSITY_COLOR, 50, 26)
        peqs  = VGroup(pabs, prefl).arrange(DOWN, buff=0.5)
        peqs.next_to(P_title, DOWN, buff=0.3)
        self.play(Write(pabs)); self.wait(1)
        self.play(Write(prefl)); self.wait(49.9)
        self.play(FadeOut(VGroup(P_title, peqs)))

        # Example 1: solar sail
        ex1_title = Text("Example 1: Solar Sail", font_size=30, color=GOLD)
        ex1_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex1_title))

        solver1 = StepSolver(self, ex1_title, start_buff=0.4)
        solver1.add_step(1,
            r"I_{\text{sun}} \approx 1361 \text{ W/m}^2 \quad\text{(solar constant at Earth orbit)}",
            "given: solar irradiance near Earth")
        solver1.add_step(2,
            r"P_{\text{refl}} = \frac{2I}{c} = \frac{2\times1361}{3\times10^8} = 9.07\times10^{-6} \text{ Pa}",
            "radiation pressure on a perfect mirror — about 9 micropascals", INTENSITY_COLOR)
        solver1.add_step(3,
            r"F = P\cdot A \quad\Rightarrow\quad A=10^4\text{ m}^2:\; F = 9.07\times10^{-6}\times10^4 = 0.091 \text{ N}",
            "a 100m×100m sail gets ~90 mN of thrust — enough for deep space travel!", GOLD)
        solver1.finalize()
        self.play(FadeOut(VGroup(ex1_title, *solver1.steps)))

        # Example 2: astronaut propulsion
        ex2_title = Text("Example 2: Astronaut with a Flashlight", font_size=30, color=GOLD)
        ex2_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex2_title))

        solver2 = StepSolver(self, ex2_title, start_buff=0.4)
        solver2.add_step(1,
            r"F = \frac{P}{c} = \frac{10\text{ W}}{3\times10^8\text{ m/s}} = 3.33\times10^{-8}\text{ N}",
            "force from a 10 W flashlight — in free space, all momentum goes to astronaut")
        solver2.add_step(2,
            r"a = \frac{F}{m} = \frac{3.33\times10^{-8}}{100} = 3.33\times10^{-10}\text{ m/s}^2",
            "acceleration of 100 kg astronaut — tiny but non-zero!")
        solver2.add_step(3,
            r"t = \frac{v}{a} = \frac{10}{3.33\times10^{-10}} \approx 3\times10^{10}\text{ s} \approx 950\text{ years}",
            "to reach 10 m/s — radiation pressure is real but extremely small", GOLD)
        solver2.finalize()
        self.play(FadeOut(VGroup(title, ex2_title, *solver2.steps)))


class DispersionScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Dispersion & Index of Refraction", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Dispersion: the refractive index n depends on the frequency of light.",
            "Different colours travel at different speeds in a material.",
            "This is why a prism splits white light into a rainbow.",
            "",
            "Bennett Section 3.9 uses the Lorentz oscillator model to explain this.",
            "Electrons in atoms behave like harmonic oscillators with natural frequencies ω_j.",
            "When light at frequency ω drives these oscillators, the phase response",
            "depends on how close ω is to the resonance frequency ω_j.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(0.5); self.play(FadeOut(intro))

        # n = sqrt(K_E)
        n_eq = labeled_eq(
            r"n = \frac{c}{v} = \sqrt{K_E} \quad (K_E = \varepsilon/\varepsilon_0)",
            "refractive index = sqrt(relative permittivity)  [dimensionless]",
            N_COLOR, 46, 26)
        n_eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(n_eq)); self.wait(1.5)

        # Lorentz model
        lorentz_title = Text("Lorentz Oscillator Model  (Bennett Eq. 3.113):", font_size=28, color=GOLD)
        lorentz_title.next_to(n_eq, DOWN, buff=0.45)
        self.play(Write(lorentz_title))

        lorentz = MathTex(
            r"n^2(\omega) \approx 1 + \frac{Nq^2}{m\varepsilon_0}\sum_j\frac{f_j}{\omega_j^2-\omega^2}",
            font_size=36, color=N_COLOR)
        lorentz.next_to(lorentz_title, DOWN, buff=0.3)
        safe_scale(lorentz, max_width=12.5)
        self.play(Write(lorentz)); self.wait(1.2)

        sym_rows = eq_table([
            (r"N", "number density of oscillators (atoms/m³)", WHITE),
            (r"q, m", "electron charge and mass", WHITE),
            (r"\omega_j", "natural (resonance) frequencies of each type of electron", N_COLOR),
            (r"f_j", "oscillator strengths — dimensionless weights summing to total electrons", N_COLOR),
        ], eq_fs=28, lbl_fs=22, buff=0.22)
        sym_rows.next_to(lorentz, DOWN, buff=0.3)
        for row in sym_rows: self.play(FadeIn(row)); self.wait(0.6)
        self.wait(1.5); self.play(FadeOut(VGroup(lorentz_title, lorentz, sym_rows)))

        # Normal vs anomalous dispersion
        disp_title = Text("Normal vs Anomalous Dispersion:", font_size=30, color=GOLD)
        disp_title.next_to(n_eq, DOWN, buff=0.45)
        self.play(Write(disp_title))

        disp_rows = eq_table([
            (r"\frac{dn}{d\lambda} < 0 \;\Leftrightarrow\; \frac{dn}{d\omega} > 0",
             "NORMAL dispersion — n increases with frequency (most glasses in visible range)", N_COLOR),
            (r"\frac{dn}{d\lambda} > 0 \;\Leftrightarrow\; \frac{dn}{d\omega} < 0",
             "ANOMALOUS dispersion — occurs near absorption resonances", B_COLOR),
            (r"v_g = \frac{c}{n + \omega\frac{dn}{d\omega}}",
             "group velocity in dispersive medium — differs from phase velocity v_p = c/n", WAVE_COLOR),
        ], eq_fs=30, lbl_fs=22, buff=0.3)
        disp_rows.next_to(disp_title, DOWN, buff=0.3)
        for row in disp_rows: self.play(FadeIn(row)); self.wait(0.8)

        prism_note = section_intro([
            "Prism example: violet light (λ≈400nm) bends MORE than red (λ≈700nm)",
            "because n_violet > n_red in glass (normal dispersion).",
            "This is Newton's famous prism experiment — explained by the Lorentz model.",
        ], font_size=25)
        prism_note.next_to(disp_rows, DOWN, buff=0.3)
        for l in prism_note: self.play(FadeIn(l)); self.wait(0.7)
        self.wait(101.8); self.play(FadeOut(VGroup(title, n_eq, disp_title, disp_rows, prism_note)))

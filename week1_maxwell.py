# week1_maxwell.py — Week 1: Maxwell's Equations & EM Waves (v3 — narration-synced)
# EVERY page on screen corresponds to EXACTLY ONE paragraph in the narration file.
from manim import *
from utils import *


def txt(s, fs=28):
    t = Text(s, font_size=fs, color=WHITE)
    safe_scale(t, max_width=13.0)
    return t


def page(scene, title, lines, wait, fs=28):
    """Show one page of text below title, wait, then fade out."""
    texts = [txt(l, fs) for l in lines if l.strip()]
    if not texts:
        return
    block = VGroup(*texts)
    block.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
    safe_scale(block, max_width=13.0, max_height=4.0)
    block.next_to(title, DOWN, buff=0.5)
    scene.play(FadeIn(block))
    scene.wait(wait)
    scene.play(FadeOut(block))


class MaxwellIntro(Scene):
    """3 narration paragraphs — 3 pages"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Maxwell's Equations", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        # Para 1 (15s): "Maxwell's equations are the four fundamental laws..."
        page(self, title, [
            "Maxwell's equations are the four fundamental laws of electromagnetism.",
            "Written down by James Clerk Maxwell in the 1860s, they unified",
            "electricity, magnetism, and light into a single coherent theory.",
        ], wait=15)

        # Para 2 (16s): "Everything we do in optics ultimately derives..."
        page(self, title, [
            "Everything we do in optics ultimately derives from these four equations.",
            "They relate the electric field E and the magnetic field B",
            "to their sources — electric charges and currents.",
        ], wait=16)

        # Para 3 (35s): "Before we write them down, let's fix the notation..."
        page(self, title, [
            "Before writing them down, we must fix notation:",
            "nabla dot E  =  divergence of E  (how much E spreads from a point)",
            "nabla cross E  =  curl of E  (how much E rotates around a point)",
            "nabla squared E  =  Laplacian  (3D second spatial derivative)",
        ], wait=35)

        self.play(FadeOut(title))


class VectorCalculusNotation(Scene):
    """4 narration paragraphs — 4 pages"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Vector Calculus Notation", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        # Para 1 (5s): "Before writing Maxwell's equations, we need three operators"
        page(self, title, [
            "Before writing Maxwell's equations, we need three differential operators.",
        ], wait=5)

        # Para 2 (21s): "The divergence..."
        div_eq = MathTex(
            r"\nabla\cdot\vec{F} = \frac{\partial F_x}{\partial x}+\frac{\partial F_y}{\partial y}+\frac{\partial F_z}{\partial z}",
            font_size=40, color=E_COLOR)
        div_desc = Text("DIVERGENCE — measures how much F spreads outward from a point.", font_size=26, color=WHITE)
        div_extra = Text("Positive divergence = source.  Negative = sink.  Zero = no sources.", font_size=26, color=WHITE)
        safe_scale(div_eq, max_width=13.0)
        safe_scale(div_desc, max_width=13.0)
        safe_scale(div_extra, max_width=13.0)
        p2 = VGroup(div_eq, div_desc, div_extra).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        p2.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(p2)); self.wait(21); self.play(FadeOut(p2))

        # Para 3 (18s): "The curl..."
        curl_eq = MathTex(
            r"\nabla\times\vec{F} = \left(\frac{\partial F_z}{\partial y}-\frac{\partial F_y}{\partial z}\right)\hat{x}+\cdots",
            font_size=36, color=B_COLOR)
        curl_desc = Text("CURL — measures how much F rotates around a point.", font_size=26, color=WHITE)
        curl_extra = Text("Think: a paddle wheel in the field spins if curl is nonzero.", font_size=26, color=WHITE)
        safe_scale(curl_eq, max_width=13.0)
        p3 = VGroup(curl_eq, curl_desc, curl_extra).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        p3.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(p3)); self.wait(18); self.play(FadeOut(p3))

        # Para 4 (12s): "The Laplacian..."
        lap_eq = MathTex(
            r"\nabla^2 F = \frac{\partial^2 F}{\partial x^2}+\frac{\partial^2 F}{\partial y^2}+\frac{\partial^2 F}{\partial z^2}",
            font_size=40, color=WAVE_COLOR)
        lap_desc = Text("LAPLACIAN — the 3D generalisation of the second derivative.", font_size=26, color=WHITE)
        lap_extra = Text("Appears in the EM wave equation in 3 dimensions.", font_size=26, color=WHITE)
        safe_scale(lap_eq, max_width=13.0)
        p4 = VGroup(lap_eq, lap_desc, lap_extra).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        p4.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(p4)); self.wait(12); self.play(FadeOut(VGroup(title, p4)))


class MaxwellEquations(Scene):
    """7 narration paragraphs — show each law when narrator describes it"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Maxwell's Equations in Matter", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        # Para 1 (4s): "Here are Maxwell's four equations in matter."
        page(self, title, ["Here are Maxwell's four equations in matter."], wait=4)

        laws = [
            # (equation_latex, law_name, description_lines, wait_seconds)
            (r"\nabla\cdot\vec{E} = \frac{\rho_{\text{free}}}{\varepsilon}",
             "Gauss's Law for E",
             ["Electric field lines DIVERGE from positive free charges.",
              "Where there are no charges: divergence of E = 0.",
              "Field lines begin on + charges, end on - charges."],
             E_COLOR, 20),

            (r"\nabla\cdot\vec{B} = 0",
             "Gauss's Law for B",
             ["The divergence of B is ALWAYS zero — no magnetic monopoles.",
              "All magnetic field lines form closed loops.",
              "Every line entering a surface must also leave it."],
             B_COLOR, 21),

            (r"\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t}",
             "Faraday's Law",
             ["A time-changing magnetic field induces a curling electric field.",
              "The minus sign (Lenz's law): induced E opposes the change in B.",
              "Principle behind electric generators and transformers."],
             E_COLOR, 18),

            (r"\nabla\times\vec{B} = \mu\vec{J}_{\text{free}} + \mu\varepsilon\frac{\partial\vec{E}}{\partial t}",
             "Ampere-Maxwell Law",
             ["Both electric CURRENTS and changing E fields create curling B.",
              "The second term (displacement current) was Maxwell's crucial addition.",
              "Without it, EM waves could not exist."],
             B_COLOR, 32),
        ]

        for latex, name, desc_lines, color, wait in laws:
            law_title = Text(name, font_size=28, color=GOLD)
            law_title.next_to(title, DOWN, buff=0.4)
            eq = MathTex(latex, font_size=44, color=color)
            eq.next_to(law_title, DOWN, buff=0.25)
            safe_scale(eq, max_width=11.0)
            texts = [Text(l, font_size=25, color=WHITE) for l in desc_lines]
            for t in texts: safe_scale(t, max_width=13.0)
            desc = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            desc.next_to(eq, DOWN, buff=0.3)
            safe_scale(desc, max_width=13.0, max_height=2.5)
            block = VGroup(law_title, eq, desc)
            self.play(FadeIn(block)); self.wait(wait); self.play(FadeOut(block))

        # Para 6 (20s): "In vacuum..."
        page(self, title, [
            "In vacuum (no charges, no currents), the equations simplify:",
            "divergence of E = 0      divergence of B = 0",
            "curl of E = -dB/dt       curl of B = mu_0 eps_0 dE/dt",
            "The curl equations now couple E and B through time derivatives.",
        ], wait=20)

        # Para 7 (26s): "The fundamental constants..."
        c_eq = MathTex(r"c = \frac{1}{\sqrt{\varepsilon_0\mu_0}} = 2.998\times10^8\text{ m/s}", font_size=44, color=GOLD)
        c_eq.next_to(title, DOWN, buff=0.5)
        c_desc = Text("Maxwell derived this from his own equations — not assumed!", font_size=28, color=WHITE)
        c_desc.next_to(c_eq, DOWN, buff=0.3)
        safe_scale(c_eq); safe_scale(c_desc, max_width=13.0)
        c_note = Text("This identified light as an electromagnetic wave.", font_size=28, color=E_COLOR)
        c_note.next_to(c_desc, DOWN, buff=0.3)
        safe_scale(c_note, max_width=13.0)
        block = VGroup(c_eq, c_desc, c_note)
        self.play(FadeIn(block)); self.wait(26); self.play(FadeOut(VGroup(title, block)))


class MaxwellVacuum(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Maxwell's Equations in Vacuum", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        page(self, title, [
            "In empty space with no charges and no currents:",
            "These are the equations we use to derive EM wave propagation.",
        ], wait=8)

        vac_eqs = VGroup(
            MathTex(r"\nabla\cdot\vec{E} = 0", font_size=44, color=E_COLOR),
            MathTex(r"\nabla\cdot\vec{B} = 0", font_size=44, color=B_COLOR),
            MathTex(r"\nabla\times\vec{E} = -\frac{\partial\vec{B}}{\partial t}", font_size=44, color=E_COLOR),
            MathTex(r"\nabla\times\vec{B} = \mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t}", font_size=44, color=B_COLOR),
        )
        vac_eqs.arrange(DOWN, buff=0.35)
        vac_eqs.next_to(title, DOWN, buff=0.5)
        safe_scale(vac_eqs, max_height=5.0)
        self.play(FadeIn(vac_eqs)); self.wait(30)
        self.play(FadeOut(VGroup(title, vac_eqs)))


class EMWaveDerivation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Deriving the EM Wave Equation", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        page(self, title, [
            "Take the curl of Faraday's law and substitute Ampere-Maxwell.",
            "After applying the vector identity curl(curl F) = grad(div F) - laplacian F:",
        ], wait=10)

        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1,
            r"\nabla\times(\nabla\times\vec{E}) = -\frac{\partial}{\partial t}(\nabla\times\vec{B})",
            "take curl of Faraday's law")
        solver.add_step(2,
            r"-\frac{\partial}{\partial t}(\nabla\times\vec{B}) = -\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}",
            "substitute Ampere-Maxwell law")
        solver.add_step(3,
            r"\nabla(\nabla\cdot\vec{E}) - \nabla^2\vec{E} = -\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}",
            "vector identity: curl(curl) = grad(div) - laplacian")
        solver.add_step(4,
            r"\nabla^2\vec{E} = \mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2} \quad\Rightarrow\quad c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}",
            "use div E = 0 in vacuum. EM wave equation with speed c!", GOLD)
        solver.finalize()
        self.wait(5)
        self.play(FadeOut(VGroup(title, *solver.steps)))


class EMWaveProperties(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Properties of EM Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        properties = [
            ("Transverse",
             r"\vec{E}\perp\vec{k} \quad\text{and}\quad \vec{B}\perp\vec{k}",
             "Both E and B are perpendicular to the propagation direction.",
             E_COLOR, 15),
            ("Mutually perpendicular",
             r"\vec{E}\perp\vec{B},\quad \vec{E}\times\vec{B}\parallel\vec{k}",
             "E, B, and k form a right-handed coordinate system.",
             B_COLOR, 15),
            ("Amplitude ratio",
             r"E = cB \quad\text{(in vacuum)}",
             "The magnitudes of E and B are always in ratio c.",
             GOLD, 15),
            ("In phase",
             r"E\text{ and }B\text{ reach maxima simultaneously}",
             "Both fields have the same kx - omega*t dependence.",
             WHITE, 12),
            ("Refractive index",
             r"n = \sqrt{K_E},\quad v = \frac{c}{n}",
             "In a material: wave slows down by factor n.",
             N_COLOR, 15),
        ]

        for name, latex, desc, color, wait in properties:
            prop_title = Text(name + ":", font_size=30, color=GOLD)
            prop_title.next_to(title, DOWN, buff=0.5)
            eq = MathTex(latex, font_size=42, color=color)
            eq.next_to(prop_title, DOWN, buff=0.3)
            safe_scale(eq, max_width=13.0)
            desc_mob = Text(desc, font_size=26, color=WHITE)
            desc_mob.next_to(eq, DOWN, buff=0.3)
            safe_scale(desc_mob, max_width=13.0)
            block = VGroup(prop_title, eq, desc_mob)
            self.play(FadeIn(block)); self.wait(wait); self.play(FadeOut(block))

        self.play(FadeOut(title))


class EMWaveExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Example: Finding B from E", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        E_field = MathTex(r"\vec{E} = E_0\hat{x}\,e^{i(kz-\omega t)}", font_size=46, color=E_COLOR)
        E_field.next_to(title, DOWN, buff=0.4)
        find = Text("Find the magnetic field B(x,y,z,t)", font_size=28, color=WHITE)
        find.next_to(E_field, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(E_field, find))); self.wait(5)

        solver = StepSolver(self, find, start_buff=0.4)
        solver.add_step(1, r"\hat{k} = \hat{z}", "propagation in the +z direction", ANGLE_COLOR)
        solver.add_step(2, r"\vec{B} = \frac{\vec{k}\times\vec{E}}{\omega}", "from Faraday's law for plane waves", B_COLOR)
        solver.add_step(3, r"\hat{z}\times\hat{x} = \hat{y}", "cross product of unit vectors")
        solver.add_step(4, r"\vec{B} = \frac{E_0}{c}\hat{y}\,e^{i(kz-\omega t)}", "B points in y-direction, magnitude E_0/c", B_COLOR)
        solver.add_step(5, r"\vec{E}\perp\vec{B}\perp\vec{k}:\quad\hat{x}\perp\hat{y}\perp\hat{z}\;\checkmark", "confirms transverse, right-handed system", GOLD)
        solver.finalize()
        self.wait(5)
        self.play(FadeOut(VGroup(title, E_field, find, *solver.steps)))


class PoyntingIrradiance(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Poynting Vector & Irradiance", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        # Poynting vector
        page(self, title, [
            "The Poynting vector describes the flow of electromagnetic energy.",
            "It points in the direction of energy flow (same as k).",
            "Its magnitude gives the power per unit area [W/m squared].",
        ], wait=15)

        S_eq = MathTex(r"\vec{S} = \frac{1}{\mu_0}\vec{E}\times\vec{B} \quad[\text{W/m}^2]", font_size=50, color=INTENSITY_COLOR)
        S_eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(S_eq)); self.wait(15); self.play(FadeOut(S_eq))

        # Irradiance
        page(self, title, [
            "Irradiance I is the time-averaged magnitude of S.",
            "The factor of 1/2 comes from time-averaging cos squared omega t = 1/2.",
            "This is a very frequently needed result — remember it.",
        ], wait=18)

        I_eq = MathTex(r"I = \frac{n\varepsilon_0 c}{2}E_0^2", font_size=56, color=INTENSITY_COLOR)
        I_eq.next_to(title, DOWN, buff=0.5)
        self.play(Create(gold_box(I_eq.copy())), Write(I_eq)); self.wait(20)

        # Example
        page(self, title, [
            "Example: green laser, power 5 mW, beam radius 1 mm.",
            "Area = pi r squared = 3.14 x 10^-6 m squared.",
            "I = P/A = 5x10^-3 / 3.14x10^-6 = 1592 W/m squared.",
            "E_0 = sqrt(2I / n eps_0 c) = 1094 V/m.",
        ], wait=25)

        self.play(FadeOut(VGroup(title, I_eq)))


class RadiationPressure(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Radiation Pressure", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        page(self, title, [
            "Light carries momentum — it exerts a pressure on surfaces it strikes.",
            "For an absorbing surface: P = I/c",
            "For a reflecting surface: P = 2I/c  (momentum reverses — factor of 2)",
        ], wait=20)

        eqs = VGroup(
            labeled_eq(r"P_{\text{abs}} = \frac{I}{c}", "absorbing surface  [Pa]", INTENSITY_COLOR, 46, 26),
            labeled_eq(r"P_{\text{refl}} = \frac{2I}{c}", "reflecting surface — 2x because momentum reverses", INTENSITY_COLOR, 46, 26),
        ).arrange(DOWN, buff=0.5)
        eqs.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(eqs)); self.wait(20)

        page(self, title, [
            "Solar sail example: solar irradiance = 1361 W/m squared.",
            "Pressure on mirror = 2 x 1361 / 3x10^8 = 9 micropascals.",
            "A 100m x 100m sail gets about 90 mN of thrust.",
            "Tiny — but real. Solar sails use exactly this effect.",
        ], wait=25)

        self.play(FadeOut(VGroup(title, eqs)))


class DispersionScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Dispersion & Index of Refraction", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(1)

        page(self, title, [
            "Dispersion: the refractive index n depends on frequency.",
            "Different colours travel at different speeds in a material.",
            "This is why a prism splits white light into a rainbow.",
        ], wait=15)

        n_eq = MathTex(r"n = \frac{c}{v} = \sqrt{K_E}", font_size=52, color=N_COLOR)
        n_eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(n_eq)); self.wait(10)

        page(self, title, [
            "The Lorentz oscillator model explains WHY dispersion occurs:",
            "Electrons behave like oscillators with resonant frequencies omega_j.",
            "Light at frequency omega drives these oscillators.",
            "The phase response depends on how close omega is to omega_j.",
        ], wait=20)

        page(self, title, [
            "Normal dispersion: n increases with frequency (most glasses).",
            "Violet light bends MORE than red light in a prism.",
            "Group velocity in dispersive medium: v_g = c / (n + omega dn/domega).",
            "When dn/domega > 0: group velocity < phase velocity.",
        ], wait=22)

        self.play(FadeOut(VGroup(title, n_eq)))

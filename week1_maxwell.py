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
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Maxwell's Equations", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # p1: 14s — "Maxwell's equations are the four fundamental laws..."
        t1a = Text("Maxwell's equations are the four fundamental laws of electromagnetism.", font_size=27, color=WHITE)
        t1b = Text("Written down by James Clerk Maxwell in the 1860s, they unified", font_size=27, color=WHITE)
        t1c = Text("electricity, magnetism, and light into a single coherent theory.", font_size=27, color=WHITE)
        for t in [t1a, t1b, t1c]: safe_scale(t, max_width=13.0)
        p1 = VGroup(t1a, t1b, t1c).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        p1.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(p1, run_time=0.5))
        self.wait(13)
        self.play(FadeOut(p1, run_time=0.5))

        # p2: 14s — "Everything we do in optics..."
        t2a = Text("Everything we do in optics ultimately derives from these four equations.", font_size=27, color=WHITE)
        t2b = Text("They relate the electric field E and the magnetic field B", font_size=27, color=WHITE)
        t2c = Text("to their sources — electric charges and currents.", font_size=27, color=WHITE)
        for t in [t2a, t2b, t2c]: safe_scale(t, max_width=13.0)
        p2 = VGroup(t2a, t2b, t2c).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        p2.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(p2, run_time=0.5))
        self.wait(13)
        self.play(FadeOut(p2, run_time=0.5))

        # p3: 32s — "Before we write them down, let's fix the notation..."
        t3 = Text("Before writing them down, we must fix notation:", font_size=27, color=WHITE)
        safe_scale(t3, max_width=13.0)
        r1 = MathTex(r"\nabla\cdot\vec{E}", font_size=36, color=E_COLOR)
        r2 = MathTex(r"\nabla\times\vec{E}", font_size=36, color=E_COLOR)
        r3 = MathTex(r"\nabla^2\vec{E}", font_size=36, color=WAVE_COLOR)
        l1 = Text("= divergence of E  (how much E spreads from a point)", font_size=24, color=WHITE)
        l2 = Text("= curl of E  (how much E rotates around a point)", font_size=24, color=WHITE)
        l3 = Text("= Laplacian  (3D second spatial derivative)", font_size=24, color=WHITE)
        for m in [r1,r2,r3,l1,l2,l3]: safe_scale(m, max_width=6.0)
        rows = VGroup(r1, r2, r3).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        lbls = VGroup(l1, l2, l3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        eq_row = VGroup(rows, lbls).arrange(RIGHT, buff=0.5, aligned_edge=UP)
        p3 = VGroup(t3, eq_row).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(p3, max_width=13.0, max_height=4.2)
        p3.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(p3, run_time=0.5))
        self.wait(31)
        self.play(FadeOut(VGroup(title, p3), run_time=0.5))


class VectorCalculusNotation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Vector Calculus Notation", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # p1: 4s — "Before writing Maxwell's equations..."
        intro = Text(
            "Before writing Maxwell's equations, we need three differential operators.",
            font_size=27, color=WHITE)
        safe_scale(intro, max_width=13.0)
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro, run_time=0.5))
        self.wait(3)
        self.play(FadeOut(intro, run_time=0.5))

        def op_block(sym_latex, name, d1_str, d2_str, color):
            sym  = MathTex(sym_latex, font_size=52, color=color)
            name_mob = Text(name, font_size=30, color=color, weight=BOLD)
            d1   = Text(d1_str, font_size=26, color=WHITE)
            d2   = Text(d2_str, font_size=26, color=COMMENT_COLOR)
            safe_scale(sym, max_width=13.0)
            safe_scale(d1, max_width=13.0)
            safe_scale(d2, max_width=13.0)
            blk = VGroup(sym, name_mob, d1, d2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
            safe_scale(blk, max_width=13.0, max_height=4.2)
            blk.next_to(title, DOWN, buff=0.45)
            return blk

        # p2: 19s — "The divergence of a vector field F..."
        p2 = op_block(r"\nabla\cdot\vec{F}", "DIVERGENCE",
                      "Measures how much the field spreads outward from a point.",
                      "Positive = field lines radiate out (source).  Zero = no sources.",
                      E_COLOR)
        self.play(FadeIn(p2, run_time=0.5))
        self.wait(18)
        self.play(FadeOut(p2, run_time=0.5))

        # p3: 17s — "The curl of F..."
        p3 = op_block(r"\nabla\times\vec{F}", "CURL",
                      "Measures how much the field rotates around a point.",
                      "A paddle wheel in the field spins if curl is nonzero.",
                      B_COLOR)
        self.play(FadeIn(p3, run_time=0.5))
        self.wait(16)
        self.play(FadeOut(p3, run_time=0.5))

        # p4: 11s — "The Laplacian..."
        p4 = op_block(r"\nabla^2 F", "LAPLACIAN",
                      "The 3D generalisation of the second derivative.",
                      "Appears in the EM wave equation in three dimensions.",
                      WAVE_COLOR)
        self.play(FadeIn(p4, run_time=0.5))
        self.wait(10)
        self.play(FadeOut(VGroup(title, p4), run_time=0.5))

class MaxwellEquations(Scene):
    """7 narration paragraphs — show each law when narrator describes it"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Maxwell's Equations in Matter", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

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
        vac_intro = Text("In vacuum, the equations simplify to:", font_size=28, color=WHITE)
        safe_scale(vac_intro, max_width=13.0)
        vac_eqs_simple = VGroup(
            MathTex(r"\nabla\cdot\vec{E}=0", font_size=32, color=E_COLOR),
            MathTex(r"\nabla\cdot\vec{B}=0", font_size=32, color=B_COLOR),
            MathTex(r"\nabla\times\vec{E}=-\partial\vec{B}/\partial t", font_size=32, color=E_COLOR),
            MathTex(r"\nabla\times\vec{B}=\mu_0\varepsilon_0\partial\vec{E}/\partial t", font_size=32, color=B_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        vac_block = VGroup(vac_intro, vac_eqs_simple).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(vac_block, max_width=13.0, max_height=4.0)
        vac_block.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(vac_block)); self.wait(20); self.play(FadeOut(vac_block))  # para6

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
        self.play(Write(title))

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
        self.play(FadeIn(vac_eqs)); self.wait(28)  # para2
        # para3 (22s): "These four equations couple E and B..."
        coupling = Text("The curl equations couple E and B — this enables EM waves.", font_size=28, color=WHITE)
        safe_scale(coupling, max_width=13.0)
        coupling.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(coupling)); self.wait(22)
        self.play(FadeOut(VGroup(title, vac_eqs, coupling)))


class EMWaveDerivation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Deriving the EM Wave Equation", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        page(self, title, [
            "Take the curl of Faraday's law and substitute Ampere-Maxwell.",
            "After applying the vector identity curl(curl F) = grad(div F) - laplacian F:",
        ], wait=11)  # para1

        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1,
            r"\nabla\times(\nabla\times\vec{E}) = -\frac{\partial}{\partial t}(\nabla\times\vec{B})",
            "take curl of Faraday's law"); self.wait(26 - 1)
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
             E_COLOR, 11),
            ("Mutually perpendicular",
             r"\vec{E}\perp\vec{B},\quad \vec{E}\times\vec{B}\parallel\vec{k}",
             "E, B, and k form a right-handed coordinate system.",
             B_COLOR, 11),
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
        self.play(Write(title)); self.wait(12)

        E_field = MathTex(r"\vec{E} = E_0\hat{x}\,e^{i(kz-\omega t)}", font_size=46, color=E_COLOR)
        E_field.next_to(title, DOWN, buff=0.4)
        find = Text("Find the magnetic field B(x,y,z,t)", font_size=28, color=WHITE)
        find.next_to(E_field, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(E_field, find))); self.wait(25)

        solver = StepSolver(self, find, start_buff=0.4)
        solver.add_step(1, r"\hat{k} = \hat{z}", "propagation in the +z direction", ANGLE_COLOR)
        solver.add_step(2, r"\vec{B} = \frac{\vec{k}\times\vec{E}}{\omega}", "from Faraday's law for plane waves", B_COLOR)
        solver.add_step(3, r"\hat{z}\times\hat{x} = \hat{y}", "cross product of unit vectors")
        solver.add_step(4, r"\vec{B} = \frac{E_0}{c}\hat{y}\,e^{i(kz-\omega t)}", "B points in y-direction, magnitude E_0/c", B_COLOR)
        solver.add_step(5, r"\vec{E}\perp\vec{B}\perp\vec{k}:\quad\hat{x}\perp\hat{y}\perp\hat{z}\;\checkmark", "confirms transverse, right-handed system", GOLD)
        solver.finalize()
        self.wait(15)
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
        ], wait=6)

        S_eq = MathTex(r"\vec{S} = \frac{1}{\mu_0}\vec{E}\times\vec{B} \quad[\text{W/m}^2]", font_size=50, color=INTENSITY_COLOR)
        S_eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(S_eq)); self.wait(18); self.play(FadeOut(S_eq))

        # Irradiance
        page(self, title, [
            "Irradiance I is the time-averaged magnitude of S.",
            "The factor of 1/2 comes from time-averaging cos squared omega t = 1/2.",
            "This is a very frequently needed result — remember it.",
        ], wait=20)

        I_eq = MathTex(r"I = \frac{n\varepsilon_0 c}{2}E_0^2", font_size=56, color=INTENSITY_COLOR)
        I_eq.next_to(title, DOWN, buff=0.5)
        self.play(Create(gold_box(I_eq.copy())), Write(I_eq)); self.wait(16)

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
        self.play(Write(title))

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
        self.play(Write(title))

        page(self, title, [
            "Dispersion: the refractive index n depends on frequency.",
            "Different colours travel at different speeds in a material.",
            "This is why a prism splits white light into a rainbow.",
        ], wait=12)

        n_eq = MathTex(r"n = \frac{c}{v} = \sqrt{K_E}", font_size=52, color=N_COLOR)
        n_eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(n_eq)); self.wait(20)

        page(self, title, [
            "The Lorentz oscillator model explains WHY dispersion occurs:",
            "Electrons behave like oscillators with resonant frequencies omega_j.",
            "Light at frequency omega drives these oscillators.",
            "The phase response depends on how close omega is to omega_j.",
        ], wait=26)

        page(self, title, [
            "Normal dispersion: n increases with frequency (most glasses).",
            "Violet light bends MORE than red light in a prism.",
        ], wait=12)

        page(self, title, [
            "Normal dispersion: d(n)/d(lambda) < 0  (violet bends more than red).",
            "Group velocity: v_g = c / (n + omega dn/domega).",
            "When dn/domega > 0: group velocity < phase velocity.",
        ], wait=21)

        page(self, title, [
            "Anomalous dispersion occurs near absorption resonances.",
            "Group velocity can exceed c near resonances — but no information",
            "travels faster than light (signal velocity is still < c).",
        ], wait=31)

        self.play(FadeOut(VGroup(title, n_eq)))

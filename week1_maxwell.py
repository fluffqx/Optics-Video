# week1_maxwell.py — Week 1: Maxwell's Equations (v4 — add_sound + zero overlap)
# add_sound() embeds narration IN the scene — millisecond-precise sync
from manim import *
from utils import *

AUDIO = "narration/audio"


def show(scene, mob, wait, fade_time=0.1):
    """Show mob, wait exactly 'wait' seconds, fade out. Zero overlap guaranteed."""
    scene.play(FadeIn(mob, run_time=fade_time))
    scene.wait(wait)
    scene.play(FadeOut(mob, run_time=fade_time))


def txt_block(lines, fs=27):
    texts = [Text(l, font_size=fs, color=WHITE) for l in lines if l.strip()]
    b = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    safe_scale(b, max_width=13.0, max_height=4.0)
    return b


class MaxwellIntro(Scene):
    # Narration: p1=13.5s p2=14.0s p3=31.3s  total=60s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/MaxwellIntro.mp3", time_offset=0)
        title = Text("Maxwell's Equations", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 13.5s
        b = txt_block([
            "Maxwell's equations are the four fundamental laws of electromagnetism.",
            "Written down by James Clerk Maxwell in the 1860s, they unified",
            "electricity, magnetism, and light into a single coherent theory.",
        ])
        b.next_to(title, DOWN, buff=0.45)
        show(self, b, 13.5)

        # p2 18.0s (was 14.0 + 4s gap observed in render)
        b2 = txt_block([
            "Everything we do in optics ultimately derives from these four equations.",
            "They relate the electric field E and the magnetic field B",
            "to their sources — electric charges and currents.",
        ])
        b2.next_to(title, DOWN, buff=0.45)
        show(self, b2, 18.0)

        # p3 27.3s (31.3 - 4s transferred to p2) — notation preview
        t3 = Text("Before writing them down, we must fix notation:", font_size=27, color=WHITE)
        safe_scale(t3, max_width=13.0)
        r1 = MathTex(r"\nabla\cdot\vec{E}", font_size=38, color=E_COLOR)
        r2 = MathTex(r"\nabla\times\vec{E}", font_size=38, color=E_COLOR)
        r3 = MathTex(r"\nabla^2\vec{E}", font_size=38, color=WAVE_COLOR)
        l1 = Text("= divergence of E", font_size=24, color=WHITE)
        l2 = Text("= curl of E", font_size=24, color=WHITE)
        l3 = Text("= Laplacian", font_size=24, color=WHITE)
        for x in [r1,r2,r3,l1,l2,l3]: safe_scale(x, max_width=6.0)
        rows = VGroup(r1,r2,r3).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        lbls = VGroup(l1,l2,l3).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        eq_row = VGroup(rows, lbls).arrange(RIGHT, buff=0.5, aligned_edge=UP)
        p3 = VGroup(t3, eq_row).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(p3, max_width=13.0, max_height=4.2)
        p3.next_to(title, DOWN, buff=0.45)
        show(self, p3, 27.3)
        self.play(FadeOut(title))


class VectorCalculusNotation(Scene):
    # p1=3.9s p2=18.8s p3=16.4s p4=10.6s  total=51.4s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/VectorCalculusNotation.mp3", time_offset=0)
        title = Text("Vector Calculus Notation", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 3.9s
        intro = Text("Before writing Maxwell's equations, we need three differential operators.",
                     font_size=27, color=WHITE)
        safe_scale(intro, max_width=13.0)
        intro.next_to(title, DOWN, buff=0.4)
        show(self, intro, 3.9)

        def op(sym_latex, name, d1, d2, color):
            sym  = MathTex(sym_latex, font_size=52, color=color)
            nm   = Text(name, font_size=30, color=color, weight=BOLD)
            dd1  = Text(d1, font_size=26, color=WHITE)
            dd2  = Text(d2, font_size=26, color=COMMENT_COLOR)
            for x in [sym,nm,dd1,dd2]: safe_scale(x, max_width=13.0)
            blk = VGroup(sym,nm,dd1,dd2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
            safe_scale(blk, max_width=13.0, max_height=4.2)
            blk.next_to(title, DOWN, buff=0.45)
            return blk

        # p2 18.8s
        show(self, op(r"\nabla\cdot\vec{F}", "DIVERGENCE",
            "Measures how much the field spreads outward from a point.",
            "Positive = source (field lines radiate out). Zero = no sources.", E_COLOR), 18.8)

        # p3 16.4s
        show(self, op(r"\nabla\times\vec{F}", "CURL",
            "Measures how much the field rotates around a point.",
            "A paddle wheel in the field spins if curl is nonzero.", B_COLOR), 16.4)

        # p4 10.6s
        show(self, op(r"\nabla^2 F", "LAPLACIAN",
            "The 3D generalisation of the second derivative.",
            "Appears in the EM wave equation in three dimensions.", WAVE_COLOR), 10.6)

        self.play(FadeOut(title))


class MaxwellEquations(Scene):
    # p1=3.0s p2=17.4s p3=18.8s p4=16.4s p5=28.4s p6=17.8s p7=23.6s  total=128.2s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/MaxwellEquations.mp3", time_offset=0)
        title = Text("Maxwell's Equations in Matter", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 3.0s
        b = txt_block(["Here are Maxwell's four equations in matter."])
        b.next_to(title, DOWN, buff=0.5)
        show(self, b, 3.0)

        def law(latex, name, desc_lines, color, wait):
            law_title = Text(name, font_size=26, color=GOLD)
            law_title.next_to(title, DOWN, buff=0.4)
            eq = MathTex(latex, font_size=44, color=color)
            eq.next_to(law_title, DOWN, buff=0.25)
            safe_scale(eq, max_width=11.0)
            texts = [Text(l, font_size=24, color=WHITE) for l in desc_lines]
            for t in texts: safe_scale(t, max_width=13.0)
            desc = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            desc.next_to(eq, DOWN, buff=0.28)
            safe_scale(desc, max_width=13.0, max_height=2.5)
            block = VGroup(law_title, eq, desc)
            show(self, block, wait)

        # p2-p5: four laws
        law(r"\nabla\cdot\vec{E}=\frac{\rho}{\varepsilon}",
            "GAUSS'S LAW FOR E  (Bennett Eq. 2.5)",
            ["Electric field lines diverge from positive free charges.",
             "Where there are no charges, divergence of E equals zero."], E_COLOR, 17.4)

        law(r"\nabla\cdot\vec{B}=0",
            "GAUSS'S LAW FOR B  (Bennett Eq. 2.6)",
            ["The divergence of B is always zero — no magnetic monopoles.",
             "All magnetic field lines form closed loops."], B_COLOR, 18.8)

        law(r"\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t}",
            "FARADAY'S LAW  (Bennett Eq. 2.21)",
            ["A time-changing magnetic field induces a curling electric field.",
             "The minus sign (Lenz's law): induced E opposes the change in B."], E_COLOR, 16.4)

        law(r"\nabla\times\vec{B}=\mu\vec{J}+\mu\varepsilon\frac{\partial\vec{E}}{\partial t}",
            "AMPERE-MAXWELL LAW  (Bennett Eq. 2.22)",
            ["Both electric currents AND changing E fields create curling B.",
             "Maxwell's displacement current term enables electromagnetic waves."], B_COLOR, 28.4)

        # p6 17.8s — vacuum form
        vac = VGroup(
            Text("In vacuum (no charges, no currents):", font_size=26, color=WHITE),
            MathTex(r"\nabla\cdot\vec{E}=0,\quad\nabla\cdot\vec{B}=0", font_size=32, color=E_COLOR),
            MathTex(r"\nabla\times\vec{E}=-\partial\vec{B}/\partial t,\quad\nabla\times\vec{B}=\mu_0\varepsilon_0\partial\vec{E}/\partial t", font_size=28, color=B_COLOR),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        safe_scale(vac, max_width=13.0, max_height=4.0)
        vac.next_to(title, DOWN, buff=0.5)
        show(self, vac, 17.8)

        # p7 23.6s — speed of light
        c_eq = MathTex(r"c=\frac{1}{\sqrt{\varepsilon_0\mu_0}}=2.998\times10^8\text{ m/s}", font_size=46, color=GOLD)
        c_note = Text("Maxwell derived this — not assumed. Light IS an electromagnetic wave.", font_size=26, color=WHITE)
        safe_scale(c_eq); safe_scale(c_note, max_width=13.0)
        c_block = VGroup(c_eq, c_note).arrange(DOWN, buff=0.35)
        c_block.next_to(title, DOWN, buff=0.5)
        show(self, c_block, 23.6)
        self.play(FadeOut(title))


class MaxwellVacuum(Scene):
    # p1=7.3s p2=25.0s p3=19.8s  total=53.3s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/MaxwellVacuum.mp3", time_offset=0)
        title = Text("Maxwell's Equations in Vacuum", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 7.3s
        b = txt_block(["In empty space with no charges and no currents, the equations simplify."])
        b.next_to(title, DOWN, buff=0.5)
        show(self, b, 7.3)

        # p2 25.0s
        eqs = VGroup(
            MathTex(r"\nabla\cdot\vec{E}=0", font_size=44, color=E_COLOR),
            MathTex(r"\nabla\cdot\vec{B}=0", font_size=44, color=B_COLOR),
            MathTex(r"\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t}", font_size=44, color=E_COLOR),
            MathTex(r"\nabla\times\vec{B}=\mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t}", font_size=44, color=B_COLOR),
        ).arrange(DOWN, buff=0.35)
        eqs.next_to(title, DOWN, buff=0.5)
        safe_scale(eqs, max_height=5.0)
        show(self, eqs, 25.0)

        # p3 19.8s
        coupling = txt_block([
            "The curl equations couple E and B through time derivatives.",
            "A changing E creates B, which creates E, which creates B...",
            "This self-sustaining oscillation IS the electromagnetic wave.",
        ])
        coupling.next_to(title, DOWN, buff=0.5)
        show(self, coupling, 19.8)
        self.play(FadeOut(title))


class EMWaveDerivation(Scene):
    # p1=9.7s p2=23.6s p3=14.0s p4=26.9s  total=75.8s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/EMWaveDerivation.mp3", time_offset=0)
        title = Text("Deriving the EM Wave Equation", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 9.7s
        b = txt_block([
            "Take the curl of Faraday's law and substitute Ampere-Maxwell.",
            "After the vector identity curl(curl F) = grad(div F) minus Laplacian:",
        ])
        b.next_to(title, DOWN, buff=0.5)
        show(self, b, 9.7)

        # p2 23.6s — step 1+2
        s1 = MathTex(r"\nabla\times(\nabla\times\vec{E})=-\frac{\partial}{\partial t}(\nabla\times\vec{B})", font_size=34)
        s2 = MathTex(r"=-\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}", font_size=34, color=WAVE_COLOR)
        safe_scale(s1, max_width=13.0); safe_scale(s2, max_width=13.0)
        sb1 = VGroup(s1, s2).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        sb1.next_to(title, DOWN, buff=0.5)
        show(self, sb1, 23.6)

        # p3 14.0s — vector identity
        s3 = MathTex(r"\nabla(\nabla\cdot\vec{E})-\nabla^2\vec{E}=-\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}", font_size=34)
        s3_note = Text("Use div E = 0 in vacuum:", font_size=24, color=COMMENT_COLOR)
        safe_scale(s3, max_width=13.0)
        sb2 = VGroup(s3_note, s3).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        sb2.next_to(title, DOWN, buff=0.5)
        show(self, sb2, 14.0)

        # p4 26.9s — result
        result = MathTex(r"\nabla^2\vec{E}=\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}\quad\Rightarrow\quad c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}", font_size=38, color=GOLD)
        safe_scale(result, max_width=13.0)
        result.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(result, run_time=0.4))
        self.play(Create(gold_box(result)))
        self.wait(74.4)
        self.play(FadeOut(VGroup(title, result)))


class EMWaveProperties(Scene):
    # p1=7.8s p2=9.7s p3=9.7s p4=5.8s p5=6.8s p6=13.0s  total=55.2s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/EMWaveProperties.mp3", time_offset=0)
        title = Text("Properties of EM Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [7.8, 9.7, 9.7, 5.8, 6.8, 13.0]
        props = [
            ("Transverse",
             r"\vec{E}\perp\vec{k}\text{ and }\vec{B}\perp\vec{k}",
             "Both E and B are perpendicular to propagation direction.", E_COLOR),
            ("Mutually Perpendicular",
             r"\vec{E}\perp\vec{B},\quad\vec{E}\times\vec{B}\parallel\vec{k}",
             "E, B, k form a right-handed coordinate system.", B_COLOR),
            ("Amplitude Ratio",
             r"E=cB\text{ (in vacuum)}",
             "The magnitudes are always in ratio c.", GOLD),
            ("In Phase",
             r"E\text{ and }B\text{ reach maxima simultaneously}",
             "Both have the same kx minus omega t dependence.", WHITE),
            ("Phase Speed",
             r"v=c/n,\quad n=\sqrt{K_E}",
             "In a material, wave slows by factor n.", N_COLOR),
            ("Refractive Index",
             r"n=\sqrt{\varepsilon/\varepsilon_0}\approx\sqrt{K_E}",
             "For non-magnetic materials with mu_r = 1.", N_COLOR),
        ]

        for i, (name, latex, desc, color) in enumerate(props):
            nm  = Text(name + ":", font_size=28, color=GOLD)
            eq  = MathTex(latex, font_size=40, color=color)
            d   = Text(desc, font_size=25, color=WHITE)
            safe_scale(eq, max_width=13.0); safe_scale(d, max_width=13.0)
            blk = VGroup(nm, eq, d).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            blk.next_to(title, DOWN, buff=0.5)
            show(self, blk, waits[i])

        self.play(FadeOut(title))


class EMWaveExample(Scene):
    # p1=10.2s p2=22.1s p3=13.5s  total=47.0s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/EMWaveExample.mp3", time_offset=0)
        title = Text("Example: Finding B from E", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 10.2s
        E_field = MathTex(r"\vec{E}=E_0\hat{x}\,e^{i(kz-\omega t)}", font_size=46, color=E_COLOR)
        find = Text("Find the magnetic field B(x,y,z,t).", font_size=28, color=WHITE)
        safe_scale(find, max_width=13.0)
        p1_block = VGroup(E_field, find).arrange(DOWN, buff=0.3)
        p1_block.next_to(title, DOWN, buff=0.5)
        show(self, p1_block, 10.2)

        # p2 22.1s — steps 1-4
        steps = VGroup(
            MathTex(r"\hat{k}=\hat{z}\quad\text{(propagation in +z)}", font_size=32),
            MathTex(r"\vec{B}=\frac{\vec{k}\times\vec{E}}{\omega}\quad\text{(Faraday for plane waves)}", font_size=32, color=B_COLOR),
            MathTex(r"\hat{z}\times\hat{x}=\hat{y}\quad\Rightarrow\quad\vec{B}=\frac{E_0}{c}\hat{y}\,e^{i(kz-\omega t)}", font_size=32, color=B_COLOR),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        for s in steps: safe_scale(s, max_width=13.0)
        steps.next_to(title, DOWN, buff=0.5)
        show(self, steps, 22.1)

        # p3 13.5s — verification
        verify = MathTex(r"\vec{E}\perp\vec{B}\perp\vec{k}:\quad\hat{x}\perp\hat{y}\perp\hat{z}\;\checkmark", font_size=38, color=GOLD)
        verify.next_to(title, DOWN, buff=0.5)
        show(self, verify, 13.5)
        self.play(FadeOut(title))


class PoyntingIrradiance(Scene):
    # p1=5.4s p2=16.4s p3=17.8s p4=14.0s p5=7.3s p6=7.8s p7=11.6s p8=24.6s p9=27.9s  total=136.3s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/PoyntingIrradiance.mp3", time_offset=0)
        title = Text("Poynting Vector & Irradiance", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [5.4, 16.4, 17.8, 14.0, 7.3, 7.8, 11.6, 24.6, 27.9]

        # p1 5.4s
        b = txt_block(["The Poynting vector describes electromagnetic energy flow."])
        b.next_to(title, DOWN, buff=0.5)
        show(self, b, waits[0])

        # p2 16.4s — S definition
        S = MathTex(r"\vec{S}=\frac{1}{\mu_0}\vec{E}\times\vec{B}\quad[\text{W/m}^2]", font_size=50, color=INTENSITY_COLOR)
        S_desc = Text("Points in direction of energy flow. Magnitude = power per unit area.", font_size=25, color=WHITE)
        safe_scale(S); safe_scale(S_desc, max_width=13.0)
        S_block = VGroup(S, S_desc).arrange(DOWN, buff=0.3)
        S_block.next_to(title, DOWN, buff=0.5)
        show(self, S_block, waits[1])

        # p3 17.8s — time average
        b3 = txt_block([
            "The Poynting vector oscillates rapidly. We take the time average.",
            "The time average of cos squared omega t over one period is one half.",
            "This factor of one half appears in all irradiance formulas.",
        ])
        b3.next_to(title, DOWN, buff=0.5)
        show(self, b3, waits[2])

        # p4 14.0s — irradiance formula
        I_eq = MathTex(r"I=\frac{n\varepsilon_0 c}{2}E_0^2", font_size=56, color=INTENSITY_COLOR)
        I_lbl = Text("Irradiance = time-averaged intensity  [W/m squared]", font_size=25, color=COMMENT_COLOR)
        safe_scale(I_lbl, max_width=13.0)
        I_block = VGroup(I_eq, I_lbl).arrange(DOWN, buff=0.3)
        I_block.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(I_block, run_time=0.4))
        self.play(Create(gold_box(I_eq)))
        self.wait(waits[3])
        self.play(FadeOut(I_block))

        # p5 7.3s — inverse relationship
        b5 = txt_block(["Irradiance is proportional to E_0 squared.",
                        "Double the field amplitude — quadruple the intensity."])
        b5.next_to(title, DOWN, buff=0.5)
        show(self, b5, waits[4])

        # p6 7.8s — find E from I
        inv = MathTex(r"E_0=\sqrt{\frac{2I}{n\varepsilon_0 c}}", font_size=46, color=E_COLOR)
        inv.next_to(title, DOWN, buff=0.5)
        show(self, inv, waits[5])

        # p7 11.6s — example setup
        b7 = txt_block(["Example: green laser, power 5 mW, beam radius 1 mm."])
        b7.next_to(title, DOWN, buff=0.5)
        show(self, b7, waits[6])

        # p8 24.6s — example calculation
        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1, r"A=\pi r^2=\pi(10^{-3})^2=3.14\times10^{-6}\text{ m}^2", "beam cross-section area")
        solver.add_step(2, r"I=P/A=5\times10^{-3}/3.14\times10^{-6}=1592\text{ W/m}^2", "irradiance", INTENSITY_COLOR)
        solver.add_step(3, r"E_0=\sqrt{2\times1592/(8.85\times10^{-12}\times3\times10^8)}=1094\text{ V/m}", "peak E field", E_COLOR)
        self.wait(waits[7])

        # p9 27.9s — B field and summary
        b9 = txt_block([
            "The peak magnetic field: B_0 = E_0/c = 3.65 micro-Tesla.",
            "This seems tiny — but the field oscillates 600 trillion times per second.",
            "The irradiance formula is one of the most important in optics.",
            "Remember: I is proportional to E_0 squared, not E_0.",
        ])
        b9.next_to(title, DOWN, buff=0.5)
        self.play(FadeOut(VGroup(*solver.steps)))
        show(self, b9, waits[8])
        self.play(FadeOut(title))


class RadiationPressure(Scene):
    # p1=8.7s p2=15.4s p3=21.7s p4=7.3s  total=54.7s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/RadiationPressure.mp3", time_offset=0)
        title = Text("Radiation Pressure", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [8.7, 15.4, 21.7, 7.3]

        # p1 8.7s
        b1 = txt_block(["Light carries momentum. When it hits a surface, it exerts a pressure.",
                        "This is radiation pressure — tiny but real and measurable."])
        b1.next_to(title, DOWN, buff=0.5)
        show(self, b1, waits[0])

        # p2 15.4s
        eqs = VGroup(
            labeled_eq(r"P_{\text{abs}}=I/c", "absorbing surface  [Pa]", INTENSITY_COLOR, 48, 26),
            labeled_eq(r"P_{\text{refl}}=2I/c", "reflecting surface — 2x because momentum reverses", INTENSITY_COLOR, 48, 26),
        ).arrange(DOWN, buff=0.5)
        eqs.next_to(title, DOWN, buff=0.5)
        show(self, eqs, waits[1])

        # p3 21.7s — solar sail example
        b3 = txt_block([
            "Solar sail: solar irradiance = 1361 W/m squared at Earth orbit.",
            "Pressure on a mirror: 2 x 1361 / 3x10^8 = 9 micro-Pascals.",
            "A 100m x 100m sail: force = 9e-6 x 10^4 = 0.09 Newtons.",
            "Small, but enough to slowly accelerate a spacecraft over months.",
        ])
        b3.next_to(title, DOWN, buff=0.5)
        show(self, b3, waits[2])

        # p4 7.3s
        b4 = txt_block(["A laser pointer exerts nanonewtons — real but unmeasurable by hand.",
                        "LIGO mirrors feel radiation pressure from circulating laser power."])
        b4.next_to(title, DOWN, buff=0.5)
        show(self, b4, waits[3])
        self.play(FadeOut(title))


class DispersionScene(Scene):
    # p1=10.6s p2=17.8s p3=23.1s p4=10.6s p5=18.3s p6=27.4s  total=110.4s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{AUDIO}/DispersionScene.mp3", time_offset=0)
        title = Text("Dispersion & Index of Refraction", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [10.6, 17.8, 23.1, 10.6, 18.3, 27.4]

        # p1 10.6s
        b1 = txt_block(["Dispersion: the refractive index n depends on frequency.",
                        "Different colours travel at different speeds in a material.",
                        "This is why a prism splits white light into a rainbow."])
        b1.next_to(title, DOWN, buff=0.5)
        show(self, b1, waits[0])

        # p2 17.8s — n definition
        n_eq = MathTex(r"n=\frac{c}{v}=\sqrt{K_E}\quad(K_E=\varepsilon/\varepsilon_0)", font_size=50, color=N_COLOR)
        n_desc = Text("Refractive index: ratio of speed of light to wave speed in material.", font_size=25, color=WHITE)
        safe_scale(n_eq); safe_scale(n_desc, max_width=13.0)
        n_block = VGroup(n_eq, n_desc).arrange(DOWN, buff=0.3)
        n_block.next_to(title, DOWN, buff=0.5)
        show(self, n_block, waits[1])

        # p3 23.1s — Lorentz model
        b3 = txt_block([
            "The Lorentz oscillator model explains WHY dispersion occurs.",
            "Electrons in atoms behave like harmonic oscillators with natural frequencies.",
            "Light at frequency omega drives these oscillators.",
            "The phase response depends on how close omega is to the resonance.",
            "Far below resonance: n is real and slightly above 1 (normal glass).",
        ])
        b3.next_to(title, DOWN, buff=0.5)
        show(self, b3, waits[2])

        # p4 10.6s — normal dispersion
        b4 = txt_block(["Normal dispersion: n increases with frequency (most glasses in visible).",
                        "Violet light (high f) bends MORE than red (low f) in a prism."])
        b4.next_to(title, DOWN, buff=0.5)
        show(self, b4, waits[3])

        # p5 18.3s — group vs phase
        gv = MathTex(r"v_g=\frac{c}{n+\omega\,dn/d\omega}", font_size=44, color=WAVE_COLOR)
        gv_desc = txt_block(["Group velocity: speed of energy and information.",
                             "In normal dispersion: v_g is less than v_p = c/n.",
                             "Different colours separate as they propagate — chromatic dispersion."])
        safe_scale(gv)
        gv_block = VGroup(gv, gv_desc).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(gv_block, max_width=13.0, max_height=4.2)
        gv_block.next_to(title, DOWN, buff=0.5)
        show(self, gv_block, waits[4])

        # p6 27.4s — anomalous + examples
        b6 = txt_block([
            "Anomalous dispersion: near absorption resonances, n can decrease with frequency.",
            "Group velocity can exceed c near resonances — but no information travels faster.",
            "Glass (n=1.5): violet at 410nm has n=1.53, red at 700nm has n=1.51.",
            "This difference of 0.02 causes the rainbow in a prism.",
            "Optical fibre design must account for dispersion to avoid pulse broadening.",
        ])
        b6.next_to(title, DOWN, buff=0.5)
        show(self, b6, waits[5])
        self.play(FadeOut(title))

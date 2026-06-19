# week1_waves.py — Week 1: Waves (v3 — perfect narration sync)
# Each visual element on screen = exactly one narration paragraph
from manim import *
from utils import *


def pg(scene, title, lines, wait, fs=28):
    """Show one page of plain text lines below title."""
    texts = [Text(l, font_size=fs, color=WHITE) for l in lines if l.strip()]
    if not texts: return
    block = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
    safe_scale(block, max_width=13.0, max_height=4.0)
    block.next_to(title, DOWN, buff=0.5)
    scene.play(FadeIn(block)); scene.wait(wait); scene.play(FadeOut(block))


class Week1TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card("WEEK 1", "Waves, Wave Equation & Complex Representation", "Bennett Ch. 1 & 2.1–2.3")
        self.play(FadeIn(card)); self.wait(38); self.play(FadeOut(card))


class WaveIntroduction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("What Is a Wave?", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # para1 (3s): "So what exactly is a wave?"
        pg(self, title, ["So what exactly is a wave?"], wait=3)

        # para2 (20s): "A wave is a disturbance that transports energy..."
        pg(self, title, [
            "A wave is a disturbance that transports ENERGY",
            "from one place to another — without transporting MATTER.",
            "Think of ripples on a pond: the water stays,",
            "but the disturbance travels across the surface.",
        ], wait=20)

        # para3 (11s): "In optics, the disturbance is the electromagnetic field..."
        pg(self, title, [
            "In optics, the disturbance is the electromagnetic field —",
            "the electric and magnetic fields oscillating as they travel.",
            "Light does not need a medium. It travels in vacuum.",
        ], wait=11)

        # para4 (11s): "We start with the simplest case..."
        pg(self, title, [
            "We start with the simplest case:",
            "a wave moving in just ONE spatial dimension.",
            "This is the foundation of everything in optics.",
        ], wait=11)

        # para5 (25s): "The wave equation is the mathematical statement..."
        pg(self, title, [
            "The wave equation is the mathematical statement that tells us",
            "exactly how a disturbance evolves in both space and time.",
            "Master this equation, and you have the key to everything:",
            "interference, diffraction, polarisation — all follow from here.",
        ], wait=25)

        self.play(FadeOut(title))


class WaveEquation1D(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # Show the equation — para1 (7s): "Here is the 1D wave equation..."
        eq = MathTex(
            r"\frac{\partial^2\Psi}{\partial x^2}", r"=", r"\frac{1}{v^2}",
            r"\frac{\partial^2\Psi}{\partial t^2}", font_size=56)
        eq[2].set_color(WAVE_COLOR)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(eq)); self.wait(7)

        # para2 (18s): "On the left side, the second derivative w.r.t. x..."
        left_brace = Brace(eq[0], DOWN, color=E_COLOR)
        left_txt = left_brace.get_text("Curvature\\\\ in space", font_size=26)
        left_txt.set_color(E_COLOR)
        self.play(GrowFromCenter(left_brace), FadeIn(left_txt))
        self.wait(18)

        # para3 (21s): "On the right side, 1/v squared times the second derivative w.r.t. t..."
        right_brace = Brace(eq[3], DOWN, color=B_COLOR)
        right_txt = right_brace.get_text("Acceleration\\\\ in time", font_size=26)
        right_txt.set_color(B_COLOR)
        self.play(GrowFromCenter(right_brace), FadeIn(right_txt))
        self.wait(21)

        # para4 (17s): "The equation is saying: spatial curvature = temporal acceleration..."
        interp = Text("Spatial curvature = Temporal acceleration / v²", font_size=30, color=GOLD)
        interp.next_to(right_txt, DOWN, buff=0.4)
        safe_scale(interp, max_width=13.0)
        self.play(FadeIn(interp)); self.wait(17)
        self.play(FadeOut(VGroup(left_brace, left_txt, right_brace, right_txt, interp)))

        # para5 (28s): "What are the solutions? f(x-vt) and g(x+vt)..."
        sol_title = Text("General Solutions:", font_size=30, color=GOLD)
        sol_title.next_to(eq, DOWN, buff=0.45)
        sol1 = labeled_eq(r"\Psi(x,t) = f(x-vt)", "travels in +x direction at speed v", E_COLOR, 44, 26)
        sol2 = labeled_eq(r"\Psi(x,t) = g(x+vt)", "travels in -x direction at speed v", B_COLOR, 44, 26)
        sols = VGroup(sol1, sol2).arrange(DOWN, buff=0.4)
        sols.next_to(sol_title, DOWN, buff=0.3)
        safe_scale(sols, max_height=3.0)
        self.play(Write(sol_title), Write(sol1)); self.wait(14)
        self.play(Write(sol2)); self.wait(14)

        # para6 (12s): "Notice the key insight: ANY shape travels without distortion..."
        key = Text("Any shape travels without distortion at speed v.", font_size=30, color=GOLD)
        key.next_to(sols, DOWN, buff=0.4)
        safe_scale(key, max_width=13.0)
        self.play(FadeIn(key)); self.wait(12)
        self.play(FadeOut(VGroup(title, eq, sol_title, sols, key)))


class WaveEquationProof(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "Let Psi(x,t) = (x - vt) squared and verify it solves the wave equation.",
        ], wait=11)

        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1, r"\frac{\partial\Psi}{\partial x} = 2(x-vt)", "chain rule w.r.t. x", E_COLOR)
        solver.add_step(2, r"\frac{\partial^2\Psi}{\partial x^2} = 2", "second derivative w.r.t. x", E_COLOR)
        solver.add_step(3, r"\frac{\partial\Psi}{\partial t} = -2v(x-vt)", "chain rule w.r.t. t", B_COLOR)
        solver.add_step(4, r"\frac{\partial^2\Psi}{\partial t^2} = 2v^2", "second derivative w.r.t. t", B_COLOR)
        solver.add_step(5, r"\frac{1}{v^2}\cdot 2v^2 = 2 = \frac{\partial^2\Psi}{\partial x^2}\;\checkmark", "both sides equal 2 — wave equation satisfied!", GOLD)
        solver.finalize(); self.wait(24 + 8)
        self.play(FadeOut(VGroup(title, *solver.steps)))


class HarmonicWave(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Harmonic Traveling Waves", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # para1 (11s): "The most important special case..."
        pg(self, title, [
            "The most important special case of a traveling wave",
            "is the HARMONIC wave — a pure sinusoidal oscillation.",
        ], wait=11)

        # para2 (8s): "Psi = A sin(kx - omega t + phi)"
        psi = MathTex(r"\Psi(x,t) = A\sin(kx - \omega t + \phi)", font_size=52, color=E_COLOR)
        psi.next_to(title, DOWN, buff=0.5)
        self.play(Write(psi)); self.play(Create(gold_box(psi)))
        self.wait(8)

        # para3 (7s): "Let's go through every symbol..."
        pg(self, title, ["Let's go through every symbol carefully."], wait=5)

        # para4 (15s): "A is the amplitude..."
        A_row = labeled_eq(r"A", "AMPLITUDE — maximum displacement [V/m for E-field]", INTENSITY_COLOR, 48, 26)
        A_row.next_to(psi, DOWN, buff=0.4)
        self.play(FadeIn(A_row)); self.wait(15); self.play(FadeOut(A_row))

        # para5 (18s): "k is the wave number..."
        k_eq = labeled_eq(r"k = \frac{2\pi}{\lambda}", "WAVE NUMBER — spatial frequency [rad/m]", WAVE_COLOR, 48, 26)
        k_eq.next_to(psi, DOWN, buff=0.4)
        self.play(FadeIn(k_eq)); self.wait(18); self.play(FadeOut(k_eq))

        # para6 (13s): "Omega is the angular frequency..."
        w_eq = labeled_eq(r"\omega = 2\pi f = \frac{2\pi}{T}", "ANGULAR FREQUENCY [rad/s]", WAVE_COLOR, 48, 26)
        w_eq.next_to(psi, DOWN, buff=0.4)
        self.play(FadeIn(w_eq)); self.wait(13); self.play(FadeOut(w_eq))

        # para7 (6s): "Lambda is the wavelength..."
        lam_eq = labeled_eq(r"\lambda", "WAVELENGTH — distance between crests [m]", WAVE_COLOR, 52, 26)
        lam_eq.next_to(psi, DOWN, buff=0.4)
        self.play(FadeIn(lam_eq)); self.wait(6); self.play(FadeOut(lam_eq))

        # para8 (13s): "f is the ordinary frequency..."
        f_eq = labeled_eq(r"f = \frac{1}{T}", "FREQUENCY — cycles per second [Hz]", WAVE_COLOR, 48, 26)
        f_eq.next_to(psi, DOWN, buff=0.4)
        self.play(FadeIn(f_eq)); self.wait(13); self.play(FadeOut(f_eq))

        # para9 (13s): "v is the phase speed..."
        v_eq = labeled_eq(r"v = \frac{\omega}{k} = f\lambda", "PHASE SPEED — how fast crests move [m/s]", WAVE_COLOR, 48, 26)
        v_eq.next_to(psi, DOWN, buff=0.4)
        self.play(FadeIn(v_eq)); self.wait(13); self.play(FadeOut(v_eq))

        # para10 (9s): "phi is the phase offset..."
        phi_eq = labeled_eq(r"\phi", "INITIAL PHASE — shifts the wave in time [rad]", WHITE, 52, 26)
        phi_eq.next_to(psi, DOWN, buff=0.4)
        self.play(FadeIn(phi_eq)); self.wait(9); self.play(FadeOut(phi_eq))

        # paras 11-14: worked example
        pg(self, title, [
            "Example: green laser, lambda = 500 nm, v = c = 3x10^8 m/s.",
        ], wait=18)

        solver = StepSolver(self, psi, start_buff=0.45)
        solver.add_step(1, r"k = \frac{2\pi}{500\times10^{-9}} = 1.257\times10^7\text{ rad/m}", "wave number", WAVE_COLOR)
        solver.add_step(2, r"f = \frac{v}{\lambda} = \frac{3\times10^8}{500\times10^{-9}} = 6\times10^{14}\text{ Hz}", "frequency", WAVE_COLOR)  # para13 (8s)
        solver.add_step(3, r"\omega = 2\pi f = 3.77\times10^{15}\text{ rad/s}", "angular frequency", WAVE_COLOR)
        solver.add_step(4, r"T = \frac{1}{f} = 1.67\times10^{-15}\text{ s} = 1.67\text{ fs}", "period — light oscillates 600 trillion times/second!", GOLD)
        solver.finalize(); self.wait(13 + 8 + 14)
        self.play(FadeOut(VGroup(title, psi, *solver.steps)))


class HarmonicWaveExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Example: Green Laser (lambda = 532 nm)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "Given: lambda = 532 nm = 532 x 10^-9 m",
            "       v = c = 3.00 x 10^8 m/s",
            "Find: k, omega, f, T",
        ], wait=8)

        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1, r"k = \frac{2\pi}{532\times10^{-9}} = 1.181\times10^7\text{ rad/m}", "wave number")
        solver.add_step(2, r"f = \frac{c}{\lambda} = \frac{3\times10^8}{532\times10^{-9}} = 5.64\times10^{14}\text{ Hz}", "frequency: 564 THz")
        solver.add_step(3, r"\omega = 2\pi f = 3.54\times10^{15}\text{ rad/s}", "angular frequency")
        solver.add_step(4, r"T = \frac{1}{f} = 1.77\times10^{-15}\text{ s} = 1.77\text{ fs}", "period: 1.77 femtoseconds", GOLD)
        solver.finalize(); self.wait(37 + 11)
        self.play(FadeOut(VGroup(title, *solver.steps)))


class SuperpositionPrinciple(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("The Principle of Superposition", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        pg(self, title, [
            "The wave equation is LINEAR — Psi appears only to the first power.",
            "No products like Psi times dPsi/dx.",
            "For any linear equation, superposition holds:",
        ], wait=7)

        pg(self, title, [
            "If Psi_1 and Psi_2 each satisfy the wave equation,",
            "then Psi_1 + Psi_2 is ALSO a valid solution.",
            "This extends to any number of waves.",
        ], wait=24)

        proof = MathTex(
            r"\frac{\partial^2(\Psi_1+\Psi_2)}{\partial x^2} = \frac{\partial^2\Psi_1}{\partial x^2}+\frac{\partial^2\Psi_2}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2(\Psi_1+\Psi_2)}{\partial t^2}\;\checkmark",
            font_size=30)
        safe_scale(proof, max_width=13.0)
        proof.next_to(title, DOWN, buff=0.5)
        self.play(Write(proof)); self.wait(5)
        self.play(FadeOut(proof))

        pg(self, title, [
            "Why this matters enormously:",
            "It is the mathematical basis for ALL interference and diffraction.",
            "Two laser beams cross — their fields simply ADD.",
            "White light = sum of many harmonic waves at different frequencies.",
        ], wait=17)

        self.play(FadeOut(title))


class PhaseGroupVelocity(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Phase Velocity & Group Velocity", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # para1 (9s): "There are two different speeds..."
        pg(self, title, [
            "There are TWO fundamentally different speeds associated with any wave.",
            "Confusing them is a classic exam mistake.",
        ], wait=9)

        # para2 (15s): "Phase velocity — speed of crests..."
        vp = labeled_eq(r"v_p = \frac{\omega}{k}", "PHASE VELOCITY — speed of wave crests  [m/s]", WAVE_COLOR, 54, 28)
        vp.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(vp)); self.wait(15); self.play(FadeOut(vp))

        # para3 (24s): "Group velocity — speed of envelope..."
        vg = labeled_eq(r"v_g = \frac{d\omega}{dk}", "GROUP VELOCITY — speed of energy/information  [m/s]", WAVE_COLOR, 54, 28)
        vg.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(vg)); self.wait(24); self.play(FadeOut(vg))

        # para4 (14s): "In vacuum, both speeds are equal..."
        pg(self, title, [
            "In vacuum and non-dispersive media: v_g = v_p.",
            "All frequencies travel at the same speed.",
            "The wave packet holds its shape perfectly.",
        ], wait=14)

        # para5 (20s): "In a dispersive medium like glass..."
        pg(self, title, [
            "In a dispersive medium (glass, water): v_g differs from v_p.",
            "Different frequencies travel at different speeds.",
            "The wave packet spreads out as it propagates.",
            "This causes chromatic dispersion in optical fibres.",
        ], wait=20)

        # para6 (15s): "This is why a prism separates white light..."
        pg(self, title, [
            "This is why a prism separates white light into a rainbow.",
            "Red light and violet light have different phase velocities in glass.",
            "They refract at different angles — dispersion!",
        ], wait=15)

        # paras 7-10: example omega = ak^2
        pg(self, title, ["Example: dispersion relation omega = a k squared."], wait=11)

        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1, r"v_p = \frac{\omega}{k} = ak", "phase velocity depends on k — dispersive", WAVE_COLOR)
        solver.add_step(2, r"v_g = \frac{d\omega}{dk} = 2ak", "group velocity", WAVE_COLOR)
        solver.add_step(3, r"v_g = 2v_p", "envelope travels TWICE as fast as the crests!", GOLD)
        solver.finalize(); self.wait(35)
        self.play(FadeOut(VGroup(title, *solver.steps)))


class ComplexRepresentation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Complex Representation of Waves", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # para1 (15s): "Working with sines and cosines is cumbersome..."
        pg(self, title, [
            "Working with sines and cosines becomes cumbersome",
            "when adding multiple waves or computing intensities.",
            "Complex exponentials make everything MUCH easier.",
        ], wait=15)

        # para2 (18s): "Euler's formula: e^(i theta) = cos + i sin..."
        euler = MathTex(r"e^{i\theta} = \cos\theta + i\sin\theta", font_size=60, color=GOLD)
        euler.next_to(title, DOWN, buff=0.5)
        self.play(Write(euler)); self.play(Create(gold_box(euler)))
        self.wait(18); self.play(FadeOut(euler))

        # para3 (11s): "From this, cos = Re[e^(i theta)]..."
        cons = VGroup(
            labeled_eq(r"\cos\theta = \mathrm{Re}[e^{i\theta}]", "cosine = real part", WHITE, 42, 24),
            labeled_eq(r"\sin\theta = \mathrm{Im}[e^{i\theta}]", "sine = imaginary part", WHITE, 42, 24),
        ).arrange(DOWN, buff=0.4)
        cons.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(cons)); self.wait(11); self.play(FadeOut(cons))

        # para4 (24s): "Instead of A cos(kx - omega t + phi), write complex exponential..."
        cwave = MathTex(r"\tilde{\Psi}(x,t) = Ae^{i(kx-\omega t+\phi)}", font_size=50, color=E_COLOR)
        rule  = MathTex(r"\text{Physical wave} = \mathrm{Re}[\tilde{\Psi}] = A\cos(kx-\omega t+\phi)", font_size=34, color=WHITE)
        safe_scale(rule, max_width=13.0)
        block = VGroup(cwave, rule).arrange(DOWN, buff=0.4)
        block.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(block)); self.wait(24); self.play(FadeOut(block))

        # para5 (20s): "Why is this better?"
        pg(self, title, [
            "Why is this better?",
            "Multiplying: e^(ia) x e^(ib) = e^(i(a+b))  — trivial!",
            "Adding waves: just add complex numbers directly.",
            "No more cos squared integrals — vastly simpler algebra.",
        ], wait=20)

        # para6 (15s): "Intensity = |Psi|^2..."
        I_eq = labeled_eq(r"I \propto |\tilde{\Psi}|^2 = \tilde{\Psi}\cdot\tilde{\Psi}^* = A^2",
                           "always real and positive — no oscillating terms", INTENSITY_COLOR, 42, 26)
        I_eq.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(I_eq)); self.wait(15); self.play(FadeOut(I_eq))

        # para7 (26s): "Extend to 3D: plane wave..."
        pw = MathTex(r"\tilde{\Psi}(\vec{r},t) = Ae^{i(\vec{k}\cdot\vec{r}-\omega t)}", font_size=48, color=E_COLOR)
        pw_desc = Text("k-vector points in direction of propagation. k.r = projection onto that direction.", font_size=25, color=WHITE)
        safe_scale(pw_desc, max_width=13.0)
        pw_block = VGroup(pw, pw_desc).arrange(DOWN, buff=0.35)
        pw_block.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(pw_block)); self.wait(26); self.play(FadeOut(pw_block))

        # para8 (18s): "Spherical wave: A/r..."
        sw = labeled_eq(r"\tilde{\Psi}(r,t) = \frac{A}{r}e^{i(kr-\omega t)}",
                         "amplitude falls off as 1/r — energy conservation over sphere 4 pi r squared", B_COLOR, 46, 25)
        sw.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sw)); self.wait(18)
        self.play(FadeOut(VGroup(title, sw)))


class ThreeDWaves(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("3D Plane Waves & Spherical Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        # para1 (24s): "In 3D, a plane wave is..."
        plane = MathTex(r"\tilde{\Psi}(\vec{r},t) = Ae^{i(\vec{k}\cdot\vec{r}-\omega t)}", font_size=50, color=E_COLOR)
        plane.next_to(title, DOWN, buff=0.45)
        self.play(Write(plane)); self.wait(5)
        sym = eq_table([
            (r"\vec{k}", "wave vector — points in direction of propagation", WAVE_COLOR),
            (r"|\vec{k}| = k = 2\pi/\lambda", "magnitude = wave number", WAVE_COLOR),
            (r"\vec{k}\cdot\vec{r} = k_x x+k_y y+k_z z", "dot product = phase along propagation", WHITE),
        ], eq_fs=30, lbl_fs=22, buff=0.25)
        sym.next_to(plane, DOWN, buff=0.35)
        self.play(FadeIn(sym)); self.wait(19); self.play(FadeOut(sym))

        # para2 (10s): "Wavefronts are flat planes perpendicular to k..."
        pg(self, title, [
            "Wavefronts — surfaces of constant phase — are flat planes",
            "perpendicular to k.  Hence the name: PLANE wave.",
        ], wait=10); self.play(FadeOut(plane))

        # para3 (28s): "Spherical wave: amplitude falls off as 1/r..."
        sphere = labeled_eq(r"\tilde{\Psi}(r,t) = \frac{A}{r}e^{i(kr-\omega t)}",
                             "amplitude = A/r  (1/r falloff for energy conservation)", B_COLOR, 48, 25)
        sphere.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(sphere)); self.wait(10)
        pg(self, title, [
            "The 1/r amplitude ensures intensity falls as 1/r squared —",
            "the inverse-square law familiar from photometry.",
            "Far from a point source, the wavefront looks locally flat.",
            "This is why we use plane waves for lasers and starlight.",
        ], wait=18); self.play(FadeOut(VGroup(title, sphere)))


class Week1WavesSummary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = equation_summary_card("Week 1 — Waves: Key Equations", [
            r"\partial^2\Psi/\partial x^2 = (1/v^2)\partial^2\Psi/\partial t^2 \quad\text{(wave eq.)}",
            r"v = f\lambda = \omega/k,\quad k=2\pi/\lambda,\quad \omega=2\pi f",
            r"\tilde{\Psi} = Ae^{i(kx-\omega t)},\quad |\tilde{\Psi}|^2 = A^2",
        ])
        self.play(FadeIn(card)); self.wait(53); self.play(FadeOut(card))

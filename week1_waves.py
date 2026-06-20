# week1_waves.py — Week 1: Waves (v4 — add_sound + zero overlap)
from manim import *
from utils import *

AUDIO = "narration/audio"


def show(scene, mob, wait, ft=0.1):
    scene.play(FadeIn(mob, run_time=0.1))
    scene.wait(wait)
    scene.play(FadeOut(mob, run_time=0.2))


def tb(lines, fs=27):
    texts = [Text(l, font_size=fs, color=WHITE) for l in lines if l.strip()]
    b = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    safe_scale(b, max_width=13.0, max_height=4.0)
    return b


class Week1TitleCard(Scene):
    # p1=5.8s p2=11.1s p3=15.0s p4=0.6s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/Week1TitleCard.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/Week1TitleCard.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation & Complex Representation",
                               "Bennett Ch. 1 & 2.1-2.3")
        self.play(FadeIn(card))
        self.wait(34.1)
        self.play(FadeOut(card))


class WaveIntroduction(Scene):
    # p1=2.5s p2=17.4s p3=9.7s p4=9.7s p5=22.2s  total=63.4s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/WaveIntroduction.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/WaveIntroduction.mp3", time_offset=0)
        title = Text("What Is a Wave?", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [2.5, 17.4, 9.7, 9.7, 22.2]

        blocks = [
            ["So what exactly is a wave?"],
            ["A wave is a disturbance that transports ENERGY from one place to another",
             "without transporting MATTER.",
             "Think of ripples on a pond: the water stays, but the disturbance travels."],
            ["In optics, the disturbance is the electromagnetic field.",
             "The electric and magnetic fields oscillate as they travel.",
             "Light does not need a medium — it travels through vacuum."],
            ["We start with the simplest case: a wave in ONE spatial dimension.",
             "This is the foundation of everything in optics."],
            ["The wave equation is the mathematical statement that governs",
             "how a disturbance evolves in both space and time.",
             "Master this equation, and you have the key to everything:",
             "interference, diffraction, polarisation — all follow from here."],
        ]

        for i, lines in enumerate(blocks):
            b = tb(lines)
            b.next_to(title, DOWN, buff=0.5)
            show(self, b, waits[i])

        self.play(FadeOut(title))


class WaveEquation1D(Scene):
    # p1=6.3s p2=15.9s p3=18.3s p4=15.0s p5=24.5s p6=10.2s  total=92.6s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/WaveEquation1D.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/WaveEquation1D.mp3", time_offset=0)
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 6.3s — show equation
        eq = MathTex(r"\frac{\partial^2\Psi}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2}",
                     font_size=56)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(eq, run_time=1.0))
        self.wait(6.3)

        # p2 15.9s — left side
        lb = Brace(eq[0:2], DOWN, color=E_COLOR)
        lt = lb.get_text("Curvature\\\\ in space", font_size=26)
        lt.set_color(E_COLOR)
        self.play(GrowFromCenter(lb), FadeIn(lt))
        self.wait(15.9)

        # p3 18.3s — right side
        rb = Brace(eq[2:], DOWN, color=B_COLOR)
        rt = rb.get_text("Acceleration\\\\ in time", font_size=26)
        rt.set_color(B_COLOR)
        self.play(GrowFromCenter(rb), FadeIn(rt))
        self.wait(18.3)

        # p4 15.0s — interpretation
        interp = Text("Spatial curvature = Temporal acceleration / v squared", font_size=30, color=GOLD)
        safe_scale(interp, max_width=13.0)
        interp.next_to(rt, DOWN, buff=0.4)
        self.play(FadeIn(interp))
        self.wait(15.0)
        self.play(FadeOut(VGroup(lb, lt, rb, rt, interp)))

        # p5 24.5s — solutions
        sol_title = Text("General Solutions:", font_size=30, color=GOLD)
        sol1 = labeled_eq(r"\Psi(x,t)=f(x-vt)", "travels in +x at speed v", E_COLOR, 44, 26)
        sol2 = labeled_eq(r"\Psi(x,t)=g(x+vt)", "travels in -x at speed v", B_COLOR, 44, 26)
        sols = VGroup(sol_title, sol1, sol2).arrange(DOWN, buff=0.38)
        sols.next_to(eq, DOWN, buff=0.5)
        safe_scale(sols, max_height=3.5)
        self.play(FadeIn(sol_title), Write(sol1))
        self.wait(24.5)
        self.play(Write(sol2))
        self.wait(10.4)

        # p6 10.2s — key insight
        key = Text("Any shape travels without distortion at speed v.", font_size=30, color=GOLD)
        safe_scale(key, max_width=13.0)
        key.next_to(sols, DOWN, buff=0.3)
        self.play(FadeIn(key))
        self.wait(92.6)
        self.play(FadeOut(VGroup(title, eq, sols, key)))


class WaveEquationProof(Scene):
    # p1=10.2s p2=21.7s p3=7.3s  total=40.3s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/WaveEquationProof.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/WaveEquationProof.mp3", time_offset=0)
        title = Text("Proof: f(x-vt) Satisfies the Wave Equation", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 10.2s
        b = tb(["Let Psi(x,t) = (x minus vt) squared and verify it solves the wave equation."])
        b.next_to(title, DOWN, buff=0.5)
        show(self, b, 10.2)

        # p2 21.7s — proof steps
        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1, r"\partial^2\Psi/\partial x^2=2", "second x-derivative = 2", E_COLOR)
        solver.add_step(2, r"\partial^2\Psi/\partial t^2=2v^2", "second t-derivative = 2v squared", B_COLOR)
        solver.add_step(3, r"\frac{1}{v^2}\cdot2v^2=2=\partial^2\Psi/\partial x^2\;\checkmark",
                       "both sides equal 2 — wave equation satisfied!", GOLD)
        solver.finalize()
        self.wait(40.3)

        # p3 7.3s
        b3 = tb(["Any function of the form f(x-vt) satisfies the wave equation.",
                 "This includes sine waves, Gaussians, square pulses — any shape."])
        b3.next_to(title, DOWN, buff=0.5)
        self.play(FadeOut(VGroup(*solver.steps)))
        show(self, b3, 7.3)
        self.play(FadeOut(title))


class HarmonicWave(Scene):
    # 14 paragraphs, 151.2s total
    # waits: [9.2, 7.3, 5.8, 13.5, 15.9, 11.1, 4.9, 11.6, 11.1, 7.8, 15.9, 11.6, 7.3, 12.6]
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/HarmonicWave.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/HarmonicWave.mp3", time_offset=0)
        title = Text("Harmonic Traveling Waves", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [9.2, 7.3, 5.8, 13.5, 15.9, 11.1, 4.9, 11.6, 11.1, 7.8, 15.9, 11.6, 7.3, 12.6]

        # p1 9.2s
        show(self, tb(["The most important special case of a traveling wave is the harmonic wave",
                       "— a pure sinusoidal oscillation. This is what lasers, LEDs, and all",
                       "coherent light sources produce."]), waits[0])

        # p2 7.3s — main equation
        psi = MathTex(r"\Psi(x,t)=A\sin(kx-\omega t+\phi)", font_size=52, color=E_COLOR)
        psi.next_to(title, DOWN, buff=0.5)
        self.play(Write(psi, run_time=0.8))
        self.play(Create(gold_box(psi)))
        self.wait(waits[1])

        # p3-p10: one symbol per paragraph
        symbols = [
            (r"A", "AMPLITUDE — maximum displacement [V/m for E-field]", INTENSITY_COLOR, waits[2]),
            (r"k=\frac{2\pi}{\lambda}", "WAVE NUMBER — spatial frequency [rad/m]", WAVE_COLOR, waits[3]),
            (r"\omega=2\pi f=\frac{2\pi}{T}", "ANGULAR FREQUENCY [rad/s]", WAVE_COLOR, waits[4]),
            (r"\lambda", "WAVELENGTH — distance between crests [m]", WAVE_COLOR, waits[5]),
            (r"f=1/T", "FREQUENCY — cycles per second [Hz]", WAVE_COLOR, waits[6]),
            (r"T", "PERIOD — time for one full cycle [s]", WAVE_COLOR, waits[7]),
            (r"v=\omega/k=f\lambda", "PHASE SPEED — how fast crests move [m/s]", WAVE_COLOR, waits[8]),
            (r"\phi", "INITIAL PHASE — shifts wave in time [rad]", WHITE, waits[9]),
        ]

        for latex, label, color, wait in symbols:
            eq = labeled_eq(latex, label, color, 50, 26)
            eq.next_to(psi, DOWN, buff=0.4)
            show(self, eq, wait)

        # p11 15.9s — key relations
        rels = eq_table([
            (r"v=f\lambda=\omega/k", "wave speed = frequency x wavelength", GOLD),
            (r"k=2\pi/\lambda", "wave number from wavelength", WAVE_COLOR),
            (r"T=1/f=2\pi/\omega", "period from frequency", WAVE_COLOR),
        ], eq_fs=34, lbl_fs=24, buff=0.28)
        rels.next_to(psi, DOWN, buff=0.4)
        show(self, rels, waits[10])

        # p12 11.6s — example setup
        show(self, tb(["Example: green laser, lambda = 500 nm, v = c = 3x10^8 m/s."]), waits[11])

        # p13 7.3s — k and f
        steps1 = VGroup(
            MathTex(r"k=2\pi/500\times10^{-9}=1.257\times10^7\text{ rad/m}", font_size=30, color=WAVE_COLOR),
            MathTex(r"f=c/\lambda=3\times10^8/500\times10^{-9}=6\times10^{14}\text{ Hz}", font_size=30, color=WAVE_COLOR),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        for s in steps1: safe_scale(s, max_width=13.0)
        steps1.next_to(psi, DOWN, buff=0.4)
        show(self, steps1, waits[12])

        # p14 12.6s — omega and T
        steps2 = VGroup(
            MathTex(r"\omega=2\pi f=3.77\times10^{15}\text{ rad/s}", font_size=32, color=WAVE_COLOR),
            MathTex(r"T=1/f=1.67\times10^{-15}\text{ s}=1.67\text{ fs}", font_size=32, color=GOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        for s in steps2: safe_scale(s, max_width=13.0)
        steps2.next_to(psi, DOWN, buff=0.4)
        show(self, steps2, waits[13])

        self.play(FadeOut(VGroup(title, psi)))


class HarmonicWaveExample(Scene):
    # p1=6.8s p2=33.7s p3=9.2s  total=50.9s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/HarmonicWaveExample.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/HarmonicWaveExample.mp3", time_offset=0)
        title = Text("Example: Green Laser (lambda = 532 nm)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 6.8s
        show(self, tb(["Given: lambda = 532 nm,  v = c = 3.00 x 10^8 m/s",
                       "Find: k, f, omega, T"]), 6.8)

        # p2 33.7s
        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1, r"k=2\pi/532\times10^{-9}=1.181\times10^7\text{ rad/m}", "wave number", WAVE_COLOR)
        solver.add_step(2, r"f=c/\lambda=5.64\times10^{14}\text{ Hz}", "frequency: 564 THz", WAVE_COLOR)
        solver.add_step(3, r"\omega=2\pi f=3.54\times10^{15}\text{ rad/s}", "angular frequency", WAVE_COLOR)
        solver.add_step(4, r"T=1/f=1.77\text{ fs}", "period: 1.77 femtoseconds", GOLD)
        solver.finalize()
        self.wait(50.9)

        # p3 9.2s
        self.play(FadeOut(VGroup(*solver.steps)))
        show(self, tb(["These numbers give a feel for how incredibly fast optical oscillations are.",
                       "The period of 1.77 femtoseconds is 1.77 millionths of a nanosecond."]), 9.2)
        self.play(FadeOut(title))


class SuperpositionPrinciple(Scene):
    # p1=5.8s p2=21.7s p3=15.5s  total=44.2s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/SuperpositionPrinciple.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/SuperpositionPrinciple.mp3", time_offset=0)
        title = Text("The Principle of Superposition", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 5.8s
        show(self, tb(["The wave equation is LINEAR.",
                       "Psi appears only to the first power — no Psi squared, no products."]), 5.8)

        # p2 21.7s — statement + proof
        stmt = tb(["If Psi_1 and Psi_2 each satisfy the wave equation,",
                   "then Psi_1 + Psi_2 is ALSO a valid solution."])
        proof = MathTex(
            r"\partial^2(\Psi_1+\Psi_2)/\partial x^2=\partial^2\Psi_1/\partial x^2+\partial^2\Psi_2/\partial x^2=\frac{1}{v^2}\partial^2(\Psi_1+\Psi_2)/\partial t^2\;\checkmark",
            font_size=27)
        safe_scale(proof, max_width=13.0)
        block = VGroup(stmt, proof).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        block.next_to(title, DOWN, buff=0.5)
        show(self, block, 21.7)

        # p3 15.5s
        show(self, tb(["Why this matters enormously:",
                       "It is the mathematical basis for ALL interference and diffraction.",
                       "Two laser beams can cross — their fields simply ADD with no interaction.",
                       "White light = sum of many harmonic waves at different frequencies."]), 15.5)

        self.play(FadeOut(title))


class PhaseGroupVelocity(Scene):
    # 10 paras: [7.8,13.5,21.2,12.1,17.4,13.0,9.7,9.2,8.2,13.5]  total=129.6s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/PhaseGroupVelocity.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/PhaseGroupVelocity.mp3", time_offset=0)
        title = Text("Phase Velocity & Group Velocity", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [7.8, 13.5, 21.2, 12.1, 17.4, 13.0, 9.7, 9.2, 8.2, 13.5]

        # p1 7.8s
        show(self, tb(["There are TWO fundamentally different speeds associated with any wave.",
                       "Confusing them is a classic exam mistake — understand the difference."]), waits[0])

        # p2 13.5s — phase velocity
        vp = labeled_eq(r"v_p=\omega/k", "PHASE VELOCITY — speed of wave crests  [m/s]", WAVE_COLOR, 56, 28)
        vp.next_to(title, DOWN, buff=0.5)
        show(self, vp, waits[1])

        # p3 21.2s — group velocity
        vg = labeled_eq(r"v_g=d\omega/dk", "GROUP VELOCITY — speed of energy/information  [m/s]", WAVE_COLOR, 56, 28)
        vg.next_to(title, DOWN, buff=0.5)
        show(self, vg, waits[2])

        # p4 12.1s
        show(self, tb(["In vacuum and non-dispersive media: v_g = v_p.",
                       "All frequencies travel at the same speed.",
                       "The wave packet holds its shape perfectly."]), waits[3])

        # p5 17.4s
        show(self, tb(["In a dispersive medium (glass, water): v_g differs from v_p.",
                       "Different frequencies travel at different speeds.",
                       "The wave packet spreads out — pulse broadening.",
                       "This causes chromatic dispersion in optical fibres."]), waits[4])

        # p6 13.0s
        show(self, tb(["A prism separates white light because different frequencies",
                       "have different phase velocities in glass.",
                       "They refract at different angles — dispersion!"]), waits[5])

        # p7 9.7s — relation to dispersion relation
        show(self, tb(["The dispersion relation omega(k) determines both speeds.",
                       "For light in vacuum: omega = ck, so v_p = v_g = c."]), waits[6])

        # p8 9.2s — example intro
        show(self, tb(["Example: dispersion relation omega = a k squared."]), waits[7])

        # p9 8.2s — example calculation
        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1, r"v_p=\omega/k=ak", "phase velocity depends on k — dispersive", WAVE_COLOR)
        solver.add_step(2, r"v_g=d\omega/dk=2ak", "group velocity", WAVE_COLOR)
        solver.add_step(3, r"v_g=2v_p", "envelope travels TWICE as fast as the crests!", GOLD)
        solver.finalize()
        self.wait(waits[8])

        # p10 13.5s
        self.play(FadeOut(VGroup(*solver.steps)))
        show(self, tb(["Physical meaning: the energy-carrying envelope moves at 2ak,",
                       "while individual wave crests move at ak.",
                       "This is directly observable in water waves."]), waits[9])

        self.play(FadeOut(title))


class ComplexRepresentation(Scene):
    # 8 paras: [13.0,15.9,9.7,21.2,17.8,13.0,23.6,15.9]  total=133.4s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/ComplexRepresentation.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/ComplexRepresentation.mp3", time_offset=0)
        title = Text("Complex Representation of Waves", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [13.0, 15.9, 9.7, 21.2, 17.8, 13.0, 23.6, 15.9]

        # p1 13.0s
        show(self, tb(["Working with sines and cosines becomes cumbersome when adding",
                       "multiple waves or computing intensities.",
                       "Complex exponentials make everything MUCH easier."]), waits[0])

        # p2 15.9s — Euler's formula
        euler = MathTex(r"e^{i\theta}=\cos\theta+i\sin\theta", font_size=60, color=GOLD)
        euler.next_to(title, DOWN, buff=0.5)
        self.play(Write(euler, run_time=0.8))
        self.play(Create(gold_box(euler)))
        self.wait(waits[1])
        self.play(FadeOut(euler))

        # p3 9.7s
        cons = VGroup(
            labeled_eq(r"\cos\theta=\mathrm{Re}[e^{i\theta}]", "cosine = real part", WHITE, 40, 24),
            labeled_eq(r"\sin\theta=\mathrm{Im}[e^{i\theta}]", "sine = imaginary part", WHITE, 40, 24),
        ).arrange(DOWN, buff=0.4)
        cons.next_to(title, DOWN, buff=0.5)
        show(self, cons, waits[2])

        # p4 21.2s — complex wave
        cwave = MathTex(r"\tilde{\Psi}(x,t)=Ae^{i(kx-\omega t+\phi)}", font_size=50, color=E_COLOR)
        rule = MathTex(r"\text{Physical wave}=\mathrm{Re}[\tilde{\Psi}]=A\cos(kx-\omega t+\phi)",
                       font_size=34, color=WHITE)
        safe_scale(rule, max_width=13.0)
        cblock = VGroup(cwave, rule).arrange(DOWN, buff=0.4)
        cblock.next_to(title, DOWN, buff=0.5)
        show(self, cblock, waits[3])

        # p5 17.8s — why better
        show(self, tb(["Why is this better?",
                       "Multiplying: e^(ia) x e^(ib) = e^(i(a+b)) — trivial!",
                       "Adding waves: just add complex numbers directly.",
                       "No more cos squared integrals — vastly simpler algebra."]), waits[4])

        # p6 13.0s — intensity
        I_eq = labeled_eq(r"I\propto|\tilde{\Psi}|^2=\tilde{\Psi}\cdot\tilde{\Psi}^*=A^2",
                          "always real and positive — no oscillating terms", INTENSITY_COLOR, 40, 26)
        I_eq.next_to(title, DOWN, buff=0.5)
        show(self, I_eq, waits[5])

        # p7 23.6s — 3D plane wave
        pw = MathTex(r"\tilde{\Psi}(\vec{r},t)=Ae^{i(\vec{k}\cdot\vec{r}-\omega t)}", font_size=48, color=E_COLOR)
        pw_sym = eq_table([
            (r"\vec{k}", "wave vector — points in direction of propagation", WAVE_COLOR),
            (r"\vec{k}\cdot\vec{r}=k_xx+k_yy+k_zz", "phase along propagation direction", WHITE),
        ], eq_fs=28, lbl_fs=22, buff=0.22)
        pw_block = VGroup(pw, pw_sym).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(pw_block, max_width=13.0, max_height=4.2)
        pw_block.next_to(title, DOWN, buff=0.5)
        show(self, pw_block, waits[6])

        # p8 15.9s — spherical wave
        sw = labeled_eq(r"\tilde{\Psi}(r,t)=\frac{A}{r}e^{i(kr-\omega t)}",
                        "amplitude = A/r (1/r falloff ensures inverse-square law)", B_COLOR, 46, 25)
        sw.next_to(title, DOWN, buff=0.5)
        show(self, sw, waits[7])
        self.play(FadeOut(title))


class ThreeDWaves(Scene):
    # p1=21.7s p2=8.7s p3=25.0s  total=56.6s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/ThreeDWaves.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/ThreeDWaves.mp3", time_offset=0)
        title = Text("3D Plane Waves & Spherical Waves", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        # p1 21.7s — plane wave
        plane = MathTex(r"\tilde{\Psi}(\vec{r},t)=Ae^{i(\vec{k}\cdot\vec{r}-\omega t)}", font_size=50, color=E_COLOR)
        plane.next_to(title, DOWN, buff=0.45)
        self.play(Write(plane, run_time=0.8))
        sym = eq_table([
            (r"\vec{k}", "wave vector — points in propagation direction", WAVE_COLOR),
            (r"|\vec{k}|=k=2\pi/\lambda", "magnitude = wave number", WAVE_COLOR),
        ], eq_fs=30, lbl_fs=22, buff=0.25)
        sym.next_to(plane, DOWN, buff=0.35)
        self.play(FadeIn(sym))
        self.wait(waits[0] if False else 21.7)
        self.play(FadeOut(sym))

        # p2 8.7s
        wf = tb(["Wavefronts — surfaces of constant phase — are flat planes",
                 "perpendicular to k. Hence the name: PLANE wave."])
        wf.next_to(plane, DOWN, buff=0.35)
        show(self, wf, 8.7)
        self.play(FadeOut(plane))

        # p3 25.0s — spherical wave
        sphere = labeled_eq(r"\tilde{\Psi}(r,t)=\frac{A}{r}e^{i(kr-\omega t)}",
                            "amplitude falls as 1/r — energy conservation over sphere 4 pi r squared",
                            B_COLOR, 46, 25)
        note = tb(["The 1/r amplitude ensures intensity falls as 1/r squared.",
                   "Far from a point source, the wavefront looks locally flat.",
                   "This is why we use plane waves for lasers and starlight."])
        sblock = VGroup(sphere, note).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(sblock, max_width=13.0, max_height=4.2)
        sblock.next_to(title, DOWN, buff=0.5)
        show(self, sblock, 25.0)
        self.play(FadeOut(title))


class Week1WavesSummary(Scene):
    # p1=3.9s p2=12.1s p3=14.5s p4=16.4s  total=48.5s
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/Week1WavesSummary.mp3", time_offset=0)
        self.add_sound(f"{AUDIO}/Week1WavesSummary.mp3", time_offset=0)
        title = Text("Week 1 Summary — Key Equations", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)

        waits = [3.9, 12.1, 14.5, 16.4]

        show(self, tb(["Here are the essential formulas from Week 1."]), waits[0])

        rows = [
            (r"\partial^2\Psi/\partial x^2=(1/v^2)\partial^2\Psi/\partial t^2", "wave equation", GOLD),
            (r"v=f\lambda=\omega/k,\; k=2\pi/\lambda,\; \omega=2\pi f", "harmonic wave relations", WAVE_COLOR),
            (r"\tilde{\Psi}=Ae^{i(kx-\omega t)},\; |\tilde{\Psi}|^2=A^2", "complex representation", E_COLOR),
        ]
        for i, (latex, lbl, color) in enumerate(rows):
            eq = labeled_eq(latex, lbl, color, 32, 24)
            eq.next_to(title, DOWN, buff=0.5)
            show(self, eq, waits[i+1])

        self.play(FadeOut(title))

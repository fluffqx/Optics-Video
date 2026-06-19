# week1_waves.py  —  Week 1: The Physics of Waves  (v2 — detailed)
# Source: Bennett Ch. 1 & 2.1-2.3
from manim import *
from utils import *


class Week1TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEK 1",
            "Waves, Wave Equation & Complex Representation",
            "Bennett Ch. 1 & 2.1–2.3"
        )
        self.play(FadeIn(card, shift=UP)); self.wait(2.5); self.play(FadeOut(card))


class WaveIntroduction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("What Is a Wave?", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(0.5)

        for page in [
            [
                "A wave is a disturbance that transports ENERGY without transporting MATTER.",
                "When a guitar string is plucked, the mechanical energy propagates along the",
                "string as a traveling wave — the string itself does not travel.",
            ],
            [
                "Mechanical waves like sound require an elastic medium for propagation.",
                "Acoustic waves are LONGITUDINAL — molecules oscillate along the direction",
                "of travel, creating alternating regions of high and low pressure.",
                "Waves on a string are TRANSVERSE — displacement is perpendicular to travel.",
            ],
            [
                "Electromagnetic waves (light, radio, X-rays) do NOT require any medium.",
                "They propagate as disturbances in the electromagnetic field itself,",
                "even in a perfect vacuum — there is no 'aether'.",
                "In this course, the wavefunction describes the electric field amplitude.",
                "The wave equation governs how this field evolves in space and time.",
                "Understanding it is the foundation of EVERYTHING in optics.",
            ],
        ]:
            block = section_intro(page, font_size=26)
            block.next_to(title, DOWN, buff=0.4)
            for line in block:
                self.play(FadeIn(line, shift=UP*0.1), run_time=0.5)
                self.wait(0.8)
            self.wait(0.8)
            self.play(FadeOut(block))

        self.play(FadeOut(title))


class WaveEquation1D(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("The 1D Wave Equation", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(0.4)

        # The equation itself
        eq = MathTex(
            r"\frac{\partial^2 \Psi(x,t)}{\partial x^2}",
            r"=",
            r"\frac{1}{v^2}",
            r"\frac{\partial^2 \Psi(x,t)}{\partial t^2}",
            font_size=52
        )
        eq[2].set_color(WAVE_COLOR)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(eq)); self.wait(1.2)

        # Annotation of each side
        left_brace = Brace(eq[0], DOWN, color=E_COLOR)
        left_txt   = left_brace.get_text("Curvature\\\\in space", font_size=26)
        left_txt.set_color(E_COLOR)
        right_brace = Brace(eq[3], DOWN, color=B_COLOR)
        right_txt   = right_brace.get_text("Acceleration\\\\in time", font_size=26)
        right_txt.set_color(B_COLOR)

        self.play(GrowFromCenter(left_brace), FadeIn(left_txt)); self.wait(1)
        self.play(GrowFromCenter(right_brace), FadeIn(right_txt)); self.wait(1.5)

        interp = Text(
            "The spatial curvature equals the temporal acceleration, scaled by 1/v².",
            font_size=28, color=WHITE
        )
        interp.next_to(left_txt, DOWN, buff=0.5)
        safe_scale(interp, max_width=13.0)
        self.play(FadeIn(interp)); self.wait(1.5)

        self.play(FadeOut(VGroup(left_brace, left_txt, right_brace, right_txt, interp)))

        # Variable definition
        v_def = labeled_eq(
            r"v = \text{wave speed, SI unit: m/s}",
            "v links spatial and temporal behaviour — one number characterises the entire wave",
            WAVE_COLOR, 38, 26
        )
        v_def.next_to(eq, DOWN, buff=0.5)
        self.play(FadeIn(v_def)); self.wait(1.5)
        self.play(FadeOut(v_def))

        # General solutions
        sol_title = Text("General Solutions  (Bennett Eq. 1.2 & 1.3)", font_size=32, color=GOLD)
        sol_title.next_to(eq, DOWN, buff=0.5)
        self.play(Write(sol_title))

        sol1 = labeled_eq(
            r"\Psi(x,t) = f(x - vt)",
            "Any differentiable f — wave travels in the +x direction at speed v",
            E_COLOR, 42, 26
        )
        sol2 = labeled_eq(
            r"\Psi(x,t) = g(x + vt)",
            "Any differentiable g — wave travels in the −x direction at speed v",
            B_COLOR, 42, 26
        )
        sols = VGroup(sol1, sol2).arrange(DOWN, buff=0.4)
        sols.next_to(sol_title, DOWN, buff=0.3)
        safe_scale(sols, max_height=3.5)

        self.play(Write(sol1)); self.wait(1.2)
        self.play(Write(sol2)); self.wait(1.2)

        key = Text(
            "Key insight: ANY shape travels without distortion at speed v.",
            font_size=28, color=GOLD
        )
        key.next_to(sols, DOWN, buff=0.4)
        safe_scale(key, max_width=13.0)
        self.play(FadeIn(key)); self.wait(2)
        self.play(FadeOut(VGroup(title, eq, sol_title, sols, key)))


class WaveEquationProof(Scene):
    """Full derivation that f(x-vt) satisfies the wave equation — Bennett Example 1.1"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Proof: f(x−vt) Satisfies the Wave Equation", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(0.5)

        intro = Text(
            "Bennett Example 1.1 — Let Ψ(x,t) = (x − vt)²  and verify it solves Eq. 1.1",
            font_size=28, color=WHITE
        )
        intro.next_to(title, DOWN, buff=0.4)
        safe_scale(intro, max_width=13.0)
        self.play(FadeIn(intro)); self.wait(1.2)

        solver = StepSolver(self, intro)

        solver.add_step(1, r"\frac{\partial \Psi}{\partial x} = 2(x - vt)",
                        "chain rule: derivative of (x−vt)² w.r.t. x", E_COLOR)
        solver.add_step(2, r"\frac{\partial^2 \Psi}{\partial x^2} = 2",
                        "second derivative w.r.t. x — a constant", E_COLOR)
        solver.add_step(3, r"\frac{\partial \Psi}{\partial t} = 2(x-vt)\cdot(-v) = -2v(x-vt)",
                        "chain rule: derivative of (x−vt)² w.r.t. t", B_COLOR)
        solver.add_step(4, r"\frac{\partial^2 \Psi}{\partial t^2} = -2v\cdot(-v) = 2v^2",
                        "second derivative w.r.t. t", B_COLOR)
        solver.add_step(5,
            r"\frac{\partial^2\Psi}{\partial x^2} = 2 \quad \text{and} \quad "
            r"\frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2} = \frac{1}{v^2}\cdot 2v^2 = 2",
            "both sides equal 2 — wave equation is satisfied ✓", GOLD)

        solver.finalize()
        self.play(FadeOut(VGroup(title, intro, *solver.steps)))


class HarmonicWave(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Harmonic Traveling Waves", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title)); self.wait(0.4)

        intro = section_intro([
            "The most important special case of a traveling wave is the HARMONIC wave —",
            "a pure sinusoidal oscillation. Bennett defines it in Eq. 1.15:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.5)

        # Main equation
        psi = MathTex(
            r"\Psi(x,t) = A \sin(kx - \omega t + \phi)",
            font_size=50, color=E_COLOR
        )
        psi.next_to(intro, DOWN, buff=0.4)
        self.play(Write(psi)); self.wait(1.5)

        box = gold_box(psi)
        self.play(Create(box)); self.wait(0.5)
        self.play(FadeOut(VGroup(intro, box)))

        # Symbol definitions — page 1
        sym_title = Text("Every Symbol Defined:", font_size=32, color=GOLD)
        sym_title.next_to(psi, DOWN, buff=0.45)
        self.play(Write(sym_title))

        rows1 = [
            (r"A",  "Amplitude — maximum displacement; units depend on wave type (V/m for light)", INTENSITY_COLOR),
            (r"k = \frac{2\pi}{\lambda}", "Wave number = spatial frequency  [rad/m]",  WAVE_COLOR),
            (r"\lambda",  "Wavelength — distance between consecutive crests  [m]",      WAVE_COLOR),
            (r"\omega = 2\pi f = \frac{2\pi}{T}", "Angular frequency  [rad/s]",        WAVE_COLOR),
        ]
        t1 = eq_table(rows1, eq_fs=32, lbl_fs=23, buff=0.28)
        t1.next_to(sym_title, DOWN, buff=0.3)
        for row in t1: self.play(FadeIn(row)); self.wait(0.8)
        self.wait(1.5); self.play(FadeOut(VGroup(sym_title, t1)))

        # Symbol definitions — page 2
        sym_title2 = Text("More Symbols:", font_size=32, color=GOLD)
        sym_title2.next_to(psi, DOWN, buff=0.45)
        self.play(Write(sym_title2))

        rows2 = [
            (r"f = \frac{1}{T}", "Frequency — cycles per second  [Hz = s⁻¹]",          WAVE_COLOR),
            (r"T",               "Period — time for one full cycle  [s]",                WAVE_COLOR),
            (r"v = \frac{\omega}{k} = f\lambda", "Phase speed — how fast crests move  [m/s]", WAVE_COLOR),
            (r"\phi",            "Initial phase offset — shifts the wave in time  [rad]", WHITE),
        ]
        t2 = eq_table(rows2, eq_fs=32, lbl_fs=23, buff=0.28)
        t2.next_to(sym_title2, DOWN, buff=0.3)
        for row in t2: self.play(FadeIn(row)); self.wait(0.8)
        self.wait(1.5); self.play(FadeOut(VGroup(sym_title2, t2)))

        # Relations between quantities
        rel_title = Text("Key Relations — Memorise These:", font_size=32, color=GOLD)
        rel_title.next_to(psi, DOWN, buff=0.45)
        self.play(Write(rel_title))

        rel_rows = [
            (r"v = f\lambda", "wave speed = frequency × wavelength", GOLD),
            (r"v = \frac{\omega}{k}", "also: angular frequency / wave number", GOLD),
            (r"k = \frac{2\pi}{\lambda}", "wave number from wavelength", WAVE_COLOR),
            (r"\omega = 2\pi f", "angular frequency from frequency", WAVE_COLOR),
            (r"T = \frac{1}{f} = \frac{2\pi}{\omega}", "period from frequency or angular frequency", WAVE_COLOR),
        ]
        t3 = eq_table(rel_rows, eq_fs=34, lbl_fs=23, buff=0.25)
        t3.next_to(rel_title, DOWN, buff=0.3)
        for row in t3: self.play(FadeIn(row)); self.wait(0.7)
        self.wait(2); self.play(FadeOut(VGroup(title, psi, rel_title, t3)))


class HarmonicWaveExample(Scene):
    """Full numerical example — green laser λ=532 nm"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Example: Green Laser Pointer (λ = 532 nm)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        given = section_intro([
            "Given:  λ = 532 nm = 532 × 10⁻⁹ m   (green laser)",
            "        v = c = 3.00 × 10⁸ m/s   (speed of light in vacuum)",
            "Find:   wave number k, angular frequency ω, frequency f, period T",
        ], font_size=28)
        given.next_to(title, DOWN, buff=0.4)
        for l in given: self.play(FadeIn(l)); self.wait(0.7)
        self.wait(0.5)

        solver = StepSolver(self, given, start_buff=0.4)
        solver.add_step(1,
            r"k = \frac{2\pi}{\lambda} = \frac{2\pi}{532\times10^{-9}} = 1.181\times10^7 \text{ rad/m}",
            "wave number: 11.8 million radians per metre", WAVE_COLOR)
        solver.add_step(2,
            r"f = \frac{v}{\lambda} = \frac{3.00\times10^8}{532\times10^{-9}} = 5.64\times10^{14} \text{ Hz}",
            "frequency: 564 terahertz — light oscillates 564 trillion times per second", WAVE_COLOR)
        solver.add_step(3,
            r"\omega = 2\pi f = 2\pi\times5.64\times10^{14} = 3.54\times10^{15} \text{ rad/s}",
            "angular frequency in radians per second", WAVE_COLOR)
        solver.add_step(4,
            r"T = \frac{1}{f} = \frac{1}{5.64\times10^{14}} = 1.77\times10^{-15} \text{ s} = 1.77 \text{ fs}",
            "period: 1.77 femtoseconds — inconceivably fast", WAVE_COLOR)
        solver.add_step(5,
            r"\Psi(x,t) = A\sin\!\left(1.181\times10^7 x - 3.54\times10^{15}\,t\right)",
            "complete wavefunction for this green laser", E_COLOR)
        solver.finalize()
        self.play(FadeOut(VGroup(title, given, *solver.steps)))


class SuperpositionPrinciple(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("The Principle of Superposition", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "The wave equation is LINEAR — it contains Ψ and its derivatives only to",
            "the first power, with no products like Ψ·(∂Ψ/∂x).",
            "",
            "For any linear equation, the principle of superposition holds:",
            "If Ψ₁ and Ψ₂ individually satisfy the wave equation, then Ψ₁ + Ψ₂ is also",
            "a valid solution. This can be extended to any number of waves.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.5); self.play(FadeOut(intro))

        # Mathematical statement
        proof_title = Text("Proof  (Bennett Section 1.5):", font_size=30, color=GOLD)
        proof_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(proof_title))

        s1 = MathTex(
            r"\text{If } \frac{\partial^2\Psi_1}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2\Psi_1}{\partial t^2}"
            r"\quad \text{and} \quad \frac{\partial^2\Psi_2}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2\Psi_2}{\partial t^2}",
            font_size=30, color=WHITE)
        s2 = MathTex(
            r"\text{Then: } \frac{\partial^2(\Psi_1+\Psi_2)}{\partial x^2}"
            r"= \frac{\partial^2\Psi_1}{\partial x^2}+\frac{\partial^2\Psi_2}{\partial x^2}"
            r"= \frac{1}{v^2}\frac{\partial^2(\Psi_1+\Psi_2)}{\partial t^2} \quad\checkmark",
            font_size=30, color=GOLD)
        eqs = VGroup(s1, s2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(eqs)
        eqs.next_to(proof_title, DOWN, buff=0.4)
        self.play(Write(s1)); self.wait(1.2)
        self.play(Write(s2)); self.wait(1.5)

        importance = section_intro([
            "Why does this matter enormously?",
            "→ It is the mathematical basis for ALL of interference and diffraction.",
            "→ Two laser beams can cross and their fields simply ADD — no interaction.",
            "→ A complex wave (e.g. white light) = sum of many harmonic waves.",
        ], font_size=26)
        importance.next_to(eqs, DOWN, buff=0.4)
        for l in importance: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(2); self.play(FadeOut(VGroup(title, proof_title, eqs, importance)))


class PhaseGroupVelocity(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Phase Velocity & Group Velocity", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "There are TWO fundamentally different speeds associated with any wave.",
            "Confusing them is a classic exam mistake — understand the difference deeply.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(1.0)
        self.wait(0.5); self.play(FadeOut(intro))

        # Phase velocity
        vp_title = Text("Phase Velocity  v_p:", font_size=34, color=WAVE_COLOR)
        vp_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(vp_title))

        vp_eq = MathTex(r"v_p = \frac{\omega}{k}", font_size=56, color=WAVE_COLOR)
        vp_eq.next_to(vp_title, DOWN, buff=0.3)
        self.play(Write(vp_eq)); self.wait(0.8)

        vp_desc = section_intro([
            "v_p is the speed at which the PHASE of the wave propagates.",
            "Equivalently: the speed at which a single wave crest (peak) moves.",
            "For a crest: kx − ωt = constant  →  dx/dt = ω/k = v_p.",
            "In vacuum: v_p = c = 3×10⁸ m/s for all frequencies.",
        ], font_size=26)
        vp_desc.next_to(vp_eq, DOWN, buff=0.3)
        for l in vp_desc: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(1); self.play(FadeOut(VGroup(vp_title, vp_eq, vp_desc)))

        # Group velocity
        vg_title = Text("Group Velocity  v_g:", font_size=34, color=WAVE_COLOR)
        vg_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(vg_title))

        vg_eq = MathTex(
            r"v_g = \frac{d\omega}{dk} = \left(\frac{dk}{d\omega}\right)^{-1}",
            font_size=50, color=WAVE_COLOR)
        vg_eq.next_to(vg_title, DOWN, buff=0.3)
        self.play(Write(vg_eq)); self.wait(0.8)

        vg_desc = section_intro([
            "v_g is the speed at which the ENVELOPE of a wave packet propagates.",
            "This is the speed at which ENERGY and INFORMATION travel.",
            "For a wave packet: it is the group of many slightly different frequencies.",
            "In a non-dispersive medium: v_g = v_p (all frequencies travel equally fast).",
            "In a dispersive medium (glass, water): v_g ≠ v_p — different colours travel",
            "at different speeds, causing dispersion.",
        ], font_size=26)
        vg_desc.next_to(vg_eq, DOWN, buff=0.3)
        for l in vg_desc: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(1); self.play(FadeOut(VGroup(vg_title, vg_eq, vg_desc)))

        # Example with concrete dispersion relation
        ex_title = Text("Example: ω = ak²  (hypothetical dispersion relation)", font_size=30, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"v_p = \frac{\omega}{k} = \frac{ak^2}{k} = ak",
            "phase velocity depends on k — medium is dispersive", WAVE_COLOR)
        solver.add_step(2,
            r"v_g = \frac{d\omega}{dk} = \frac{d(ak^2)}{dk} = 2ak",
            "group velocity = 2ak", WAVE_COLOR)
        solver.add_step(3,
            r"v_g = 2v_p",
            "group velocity is TWICE the phase velocity in this medium", GOLD)

        note = section_intro([
            "Physical meaning: the wave crests move at speed ak,",
            "but the energy-carrying envelope moves at speed 2ak.",
            "This is directly observable in water waves!",
        ], font_size=26)
        note.next_to(solver.steps[-1], DOWN, buff=0.4)
        for l in note: self.play(FadeIn(l)); self.wait(0.8)

        solver.finalize()
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, note, *solver.steps)))


class ComplexRepresentation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Complex Representation of Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Working with sin and cos directly becomes very cumbersome when adding",
            "multiple waves or computing intensities. The complex exponential notation",
            "introduced by Bennett in Section 1.6 makes everything MUCH easier.",
            "",
            "The key is Euler's formula — one of the most beautiful results in mathematics:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.5); self.play(FadeOut(intro))

        # Euler's formula with derivation context
        euler_title = Text("Euler's Formula  (Bennett Eq. 1.18):", font_size=30, color=GOLD)
        euler_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(euler_title))

        euler = MathTex(r"e^{i\theta} = \cos\theta + i\sin\theta",
                        font_size=58, color=GOLD)
        euler.next_to(euler_title, DOWN, buff=0.3)
        self.play(Write(euler)); self.wait(1.5)
        self.play(Create(gold_box(euler))); self.wait(1)

        # Consequences
        consequences = [
            (r"\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}", "cosine from complex exponentials", WHITE),
            (r"\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}", "sine from complex exponentials", WHITE),
            (r"|e^{i\theta}| = 1", "magnitude is always 1 — it just rotates in the complex plane", N_COLOR),
        ]
        c_group = eq_table(consequences, eq_fs=34, lbl_fs=24, buff=0.28)
        c_group.next_to(euler, DOWN, buff=0.4)
        for row in c_group: self.play(FadeIn(row)); self.wait(0.8)
        self.wait(1.5); self.play(FadeOut(VGroup(euler_title, euler, c_group)))

        # Complex wave notation
        cwave_title = Text("The Complex Wave  (Bennett Eq. 1.6.2):", font_size=30, color=GOLD)
        cwave_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(cwave_title))

        cwave = MathTex(
            r"\tilde{\Psi}(x,t) = A\,e^{i(kx - \omega t + \phi)}",
            font_size=50, color=E_COLOR)
        cwave.next_to(cwave_title, DOWN, buff=0.35)
        self.play(Write(cwave)); self.wait(1)

        rule = MathTex(
            r"\text{Physical wave} = \mathrm{Re}[\tilde{\Psi}]"
            r"= A\cos(kx - \omega t + \phi)",
            font_size=36, color=WHITE)
        rule.next_to(cwave, DOWN, buff=0.4)
        safe_scale(rule, max_width=13.0)
        self.play(Write(rule)); self.wait(1.5)

        why = section_intro([
            "Why is this better?",
            "→ Multiplying complex exponentials: e^(ia) · e^(ib) = e^(i(a+b))  — trivial!",
            "→ Adding two waves: just add the complex numbers directly.",
            "→ Computing intensity: |Ψ̃|² = Ψ̃·Ψ̃* = A²  — always real, always positive.",
            "→ No more cos² integrals — the algebra is vastly simpler.",
        ], font_size=25)
        why.next_to(rule, DOWN, buff=0.35)
        for l in why: self.play(FadeIn(l)); self.wait(0.7)
        self.wait(1.5); self.play(FadeOut(VGroup(cwave_title, cwave, rule, why)))

        # Intensity from complex notation
        int_title = Text("Intensity from Complex Notation:", font_size=32, color=GOLD)
        int_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(int_title))

        int_rows = [
            (r"|\tilde{\Psi}|^2 = \tilde{\Psi}\cdot\tilde{\Psi}^* = A^2",
             "intensity ∝ amplitude squared — the imaginary parts cancel perfectly", INTENSITY_COLOR),
            (r"\tilde{\Psi}^* = A\,e^{-i(kx-\omega t+\phi)}",
             "complex conjugate: replace i → −i everywhere", WHITE),
            (r"\tilde{\Psi}\cdot\tilde{\Psi}^* = A\,e^{i(\ldots)}\cdot A\,e^{-i(\ldots)} = A^2",
             "exponentials cancel: result is real and positive", INTENSITY_COLOR),
        ]
        int_eqs = eq_table(int_rows, eq_fs=32, lbl_fs=24, buff=0.3)
        int_eqs.next_to(int_title, DOWN, buff=0.35)
        for row in int_eqs: self.play(FadeIn(row)); self.wait(0.9)
        self.wait(2); self.play(FadeOut(VGroup(title, int_title, int_eqs)))


class ThreeDWaves(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("3D Plane Waves & Spherical Waves", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Real light waves propagate in three dimensions. Bennett Section 1.7",
            "extends the 1D description to 3D using the wave vector k⃗.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.5); self.play(FadeOut(intro))

        # 3D plane wave
        pw_title = Text("3D Plane Wave  (Bennett Eq. 1.57):", font_size=30, color=GOLD)
        pw_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(pw_title))

        plane = MathTex(
            r"\tilde{\Psi}(\vec{r},t) = A\,e^{i(\vec{k}\cdot\vec{r} - \omega t)}",
            font_size=48, color=E_COLOR)
        plane.next_to(pw_title, DOWN, buff=0.3)
        self.play(Write(plane)); self.wait(1)

        plane_details = eq_table([
            (r"\vec{k} = k_x\hat{x} + k_y\hat{y} + k_z\hat{z}",
             "wave vector — points in direction of propagation", WAVE_COLOR),
            (r"\vec{k}\cdot\vec{r} = k_x x + k_y y + k_z z",
             "dot product: projection of position onto propagation direction", WAVE_COLOR),
            (r"|\vec{k}| = k = \frac{\omega}{v} = \frac{2\pi}{\lambda}",
             "magnitude of wave vector = wave number", WAVE_COLOR),
            (r"\text{Wavefronts: surfaces where } \vec{k}\cdot\vec{r} = \text{const}",
             "flat planes perpendicular to k⃗ — hence 'plane wave'", WHITE),
        ], eq_fs=30, lbl_fs=23, buff=0.25)
        plane_details.next_to(plane, DOWN, buff=0.35)
        for row in plane_details: self.play(FadeIn(row)); self.wait(0.7)
        self.wait(1.5); self.play(FadeOut(VGroup(pw_title, plane, plane_details)))

        # Spherical wave
        sw_title = Text("Spherical Wave  (Bennett Eq. 1.59):", font_size=30, color=GOLD)
        sw_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(sw_title))

        sphere = MathTex(
            r"\tilde{\Psi}(r,t) = \frac{A}{r}\,e^{i(kr - \omega t)}",
            font_size=52, color=B_COLOR)
        sphere.next_to(sw_title, DOWN, buff=0.3)
        self.play(Write(sphere)); self.wait(1.2)

        sw_details = section_intro([
            "The amplitude falls off as 1/r — this is NOT arbitrary.",
            "It is required by energy conservation: as the wavefront expands",
            "over a sphere of area 4πr², the intensity I ∝ A² ∝ 1/r².",
            "This is the inverse-square law — familiar from photometry.",
            "",
            "Far from a point source, the 1/r curvature of the wavefront becomes",
            "negligible — it looks like a plane wave locally. This is why we",
            "use plane waves to describe laser beams and starlight.",
        ], font_size=26)
        sw_details.next_to(sphere, DOWN, buff=0.35)
        for l in sw_details: self.play(FadeIn(l)); self.wait(0.7)
        self.wait(2); self.play(FadeOut(VGroup(title, sw_title, sphere, sw_details)))


class Week1WavesSummary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = equation_summary_card(
            "Week 1 — Waves: Key Equations",
            [
                r"\frac{\partial^2\Psi}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2} \quad \text{(wave equation)}",
                r"v = f\lambda = \frac{\omega}{k},\quad k=\frac{2\pi}{\lambda},\quad \omega=2\pi f \quad \text{(harmonic wave)}",
                r"\tilde{\Psi} = A\,e^{i(kx-\omega t)},\quad |\tilde{\Psi}|^2 = A^2 \quad \text{(complex notation)}",
            ]
        )
        self.play(FadeIn(card)); self.wait(4); self.play(FadeOut(card))

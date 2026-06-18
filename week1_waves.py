# week1_waves.py
# 31OPT Optics — Week 1: Waves & Wave Equation
from manim import *
from utils import *


class Week1TitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "WEEK 1",
            "Waves, Wave Equation & Complex Representation",
            "Bennett Ch. 1 & 2.1–2.3"
        )
        self.play(FadeIn(card, shift=UP))
        self.wait(2)
        self.play(FadeOut(card))


class WaveIntroduction(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        intro = section_intro([
            "A wave is a disturbance that transports energy without transporting matter.",
            "In optics, the disturbance is the electromagnetic field.",
            "We start with the simplest case: a wave in one spatial dimension.",
            "The wave equation tells us how such a disturbance evolves in space and time.",
            "Understanding this equation is the foundation of everything in this course."
        ])
        self.play(FadeIn(intro[0])); self.wait(1.5)
        for line in intro[1:]:
            self.play(FadeIn(line)); self.wait(1.2)
        self.wait(1)
        self.play(FadeOut(intro))


class WaveEquation1D(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        title = Text("The 1D Wave Equation", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        eq = MathTex(
            r"\frac{\partial^2 \Psi(x,t)}{\partial x^2}",
            r"=",
            r"\frac{1}{v^2}",
            r"\frac{\partial^2 \Psi(x,t)}{\partial t^2}",
            font_size=48
        )
        eq[2].set_color(WAVE_COLOR)
        self.play(Write(eq))
        self.wait(1)

        v_label = MathTex(r"v = \text{wave speed (m/s)}", font_size=34, color=WAVE_COLOR)
        v_label.next_to(eq, DOWN, buff=0.5)
        self.play(FadeIn(v_label))
        self.wait(1)

        meaning = Text(
            "Left side: curvature in space.   Right side: acceleration in time.",
            font_size=28, color=WHITE
        )
        meaning.next_to(v_label, DOWN, buff=0.4)
        self.play(FadeIn(meaning))
        self.wait(2)

        self.play(FadeOut(v_label), FadeOut(meaning))
        sol_title = Text("General Solutions:", font_size=32, color=GOLD)
        sol_title.next_to(eq, DOWN, buff=0.5)
        self.play(Write(sol_title))

        sol1 = MathTex(r"\Psi(x,t) = f(x - vt)", font_size=40, color=E_COLOR)
        sol1_label = Text("  rightward-travelling wave", font_size=26, color=WHITE)
        sol1_group = VGroup(sol1, sol1_label).arrange(RIGHT)

        sol2 = MathTex(r"\Psi(x,t) = g(x + vt)", font_size=40, color=B_COLOR)
        sol2_label = Text("  leftward-travelling wave", font_size=26, color=WHITE)
        sol2_group = VGroup(sol2, sol2_label).arrange(RIGHT)

        solutions = VGroup(sol1_group, sol2_group).arrange(DOWN, buff=0.4)
        solutions.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(solutions))
        self.wait(2)
        self.play(FadeOut(VGroup(title, eq, sol_title, solutions)))


class HarmonicWave(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Harmonic Travelling Wave", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        psi = MathTex(
            r"\Psi(x,t) = A \sin(kx - \omega t + \varphi)",
            font_size=46
        )
        self.play(Write(psi))
        self.wait(1)

        symbols = [
            (r"A",                          "amplitude (units of the wave quantity)",  INTENSITY_COLOR),
            (r"k = \frac{2\pi}{\lambda}",   "wave number  [rad/m]",                   WAVE_COLOR),
            (r"\omega = 2\pi f",            "angular frequency  [rad/s]",              WAVE_COLOR),
            (r"\lambda",                    "wavelength  [m]",                         WAVE_COLOR),
            (r"f = \frac{1}{T}",            "frequency  [Hz]",                         WAVE_COLOR),
            (r"v = \frac{\omega}{k} = f\lambda", "phase speed  [m/s]",                WAVE_COLOR),
            (r"\varphi",                    "initial phase offset  [rad]",             WHITE),
        ]
        table_items = VGroup()
        for sym, desc, col in symbols:
            sym_tex   = MathTex(sym, font_size=32, color=col)
            desc_text = Text(desc, font_size=26, color=WHITE)
            row = VGroup(sym_tex, desc_text).arrange(RIGHT, buff=0.3)
            table_items.add(row)
        table_items.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        table_items.next_to(psi, DOWN, buff=0.4)

        for item in table_items:
            self.play(FadeIn(item), run_time=0.6)
        self.wait(2)

        # ── Worked example ────────────────────────────────────────────
        self.play(FadeOut(table_items))
        ex_title = Text(
            "Example: Find k, omega, T  given  lambda = 500 nm,  v = 3e8 m/s",
            font_size=27, color=GOLD
        )
        ex_title.next_to(psi, DOWN, buff=0.4)
        self.play(Write(ex_title))

        step1 = MathTex(
            r"k = \frac{2\pi}{\lambda} = \frac{2\pi}{500 \times 10^{-9}}",
            r"= 1.257 \times 10^7 \text{ rad/m}",
            font_size=34, color=WAVE_COLOR
        )
        step2 = MathTex(
            r"\omega = k \cdot v = 1.257 \times 10^7 \times 3 \times 10^8",
            r"= 3.77 \times 10^{15} \text{ rad/s}",
            font_size=34, color=WAVE_COLOR
        )
        step3 = MathTex(
            r"T = \frac{2\pi}{\omega} = \frac{2\pi}{3.77 \times 10^{15}}",
            r"= 1.67 \times 10^{-15} \text{ s}",
            font_size=34, color=WAVE_COLOR
        )
        steps = VGroup(step1, step2, step3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(ex_title, DOWN, buff=0.3)

        for step in steps:
            self.play(Write(step), run_time=1.2)
            self.wait(0.8)
        box = gold_box(steps)
        self.play(Create(box))
        self.wait(2)
        self.play(FadeOut(VGroup(title, psi, ex_title, steps, box)))


class PhaseGroupVelocity(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Phase Velocity & Group Velocity", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Phase velocity: the speed at which a single wavefront (crest) moves.",
            "Group velocity: the speed of the wave packet envelope — how energy travels.",
            "In vacuum they are equal. In a dispersive medium (like glass) they differ.",
            "This difference is why a prism separates colours: each frequency has a different v_p."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.2)
        self.play(FadeOut(intro))

        vp = MathTex(r"v_p = \frac{\omega}{k}", font_size=48, color=WAVE_COLOR)
        vp_label = Text("Phase velocity  [m/s]", font_size=30, color=WHITE)
        vp_group = VGroup(vp, vp_label).arrange(RIGHT, buff=0.5)

        vg = MathTex(
            r"v_g = \frac{d\omega}{dk} = \left(\frac{dk}{d\omega}\right)^{-1}",
            font_size=48, color=WAVE_COLOR
        )
        vg_label = Text("Group velocity  [m/s]", font_size=30, color=WHITE)
        vg_group = VGroup(vg, vg_label).arrange(RIGHT, buff=0.5)

        eq_group = VGroup(vp_group, vg_group).arrange(DOWN, buff=0.6)
        self.play(Write(vp_group)); self.wait(1)
        self.play(Write(vg_group)); self.wait(1)

        non_disp = MathTex(
            r"\text{Non-dispersive medium: } v_g = v_p",
            font_size=36, color=N_COLOR
        )
        non_disp.next_to(eq_group, DOWN, buff=0.5)
        self.play(FadeIn(non_disp)); self.wait(1)

        self.play(FadeOut(VGroup(eq_group, non_disp)))
        ex = Text("Example: omega = ak^2  (hypothetical dispersion relation)", font_size=30, color=GOLD)
        ex.next_to(title, DOWN, buff=0.4)
        self.play(Write(ex))

        s1 = MathTex(r"v_p = \frac{\omega}{k} = \frac{ak^2}{k} = ak",
                     font_size=38, color=WAVE_COLOR)
        s2 = MathTex(r"v_g = \frac{d\omega}{dk} = \frac{d(ak^2)}{dk} = 2ak",
                     font_size=38, color=WAVE_COLOR)
        s3 = MathTex(r"\therefore \quad v_g = 2 v_p \quad \text{(group is twice phase speed)}",
                     font_size=36, color=GOLD)
        steps = VGroup(s1, s2, s3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        steps.next_to(ex, DOWN, buff=0.35)

        for s in steps:
            self.play(Write(s), run_time=1.1); self.wait(0.7)
        self.play(Create(gold_box(s3)))
        self.wait(2)
        self.play(FadeOut(VGroup(title, ex, steps)))


class ComplexRepresentation(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Complex Representation of Waves", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Working with sine and cosine is cumbersome for superposition.",
            "We use complex exponentials instead — Euler's formula connects them.",
            "Physical quantities are always the real part of the complex expression.",
            "The complex form makes adding waves and computing intensities much simpler."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.1)
        self.play(FadeOut(intro))

        euler = MathTex(r"e^{i\theta} = \cos\theta + i\sin\theta",
                        font_size=50, color=GOLD)
        self.play(Write(euler)); self.wait(1.5)

        cos_form = MathTex(r"\cos\theta = \frac{e^{i\theta} + e^{-i\theta}}{2}", font_size=40)
        sin_form = MathTex(r"\sin\theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}", font_size=40)
        trig = VGroup(cos_form, sin_form).arrange(RIGHT, buff=1.0)
        trig.next_to(euler, DOWN, buff=0.5)
        self.play(Write(trig)); self.wait(1.5)
        self.play(FadeOut(VGroup(euler, trig)))

        cwave = MathTex(
            r"\Psi(x,t) = A \, e^{i(kx - \omega t + \varphi)}",
            font_size=48, color=E_COLOR
        )
        self.play(Write(cwave)); self.wait(1)

        rule = MathTex(
            r"\text{Physical wave} = \mathrm{Re}[\Psi] = A\cos(kx - \omega t + \varphi)",
            font_size=36, color=WHITE
        )
        rule.next_to(cwave, DOWN, buff=0.5)
        self.play(Write(rule)); self.wait(1.5)

        intensity = MathTex(
            r"|\Psi|^2 = \Psi \cdot \Psi^* = A^2",
            font_size=40, color=INTENSITY_COLOR
        )
        intensity_label = Text(
            "Intensity proportional to |Psi|^2 — always real and positive",
            font_size=26, color=WHITE
        )
        int_group = VGroup(intensity, intensity_label).arrange(DOWN, buff=0.2)
        int_group.next_to(rule, DOWN, buff=0.5)
        self.play(Write(int_group)); self.wait(2)

        # 3D plane wave and spherical wave
        self.play(FadeOut(VGroup(cwave, rule, int_group)))
        pw_title = Text("3D Plane Wave & Spherical Wave", font_size=36, color=GOLD)
        pw_title.to_edge(UP).shift(DOWN * 0.5)
        self.play(Transform(title, pw_title))

        plane = MathTex(
            r"\Psi(\vec{r},t) = A \, e^{i(\vec{k}\cdot\vec{r} - \omega t)}",
            font_size=46, color=E_COLOR
        )
        plane_note = MathTex(
            r"\vec{k}\cdot\vec{r} = k_x x + k_y y + k_z z, \quad |\vec{k}| = k = \frac{\omega}{v}",
            font_size=34, color=WAVE_COLOR
        )
        sphere = MathTex(
            r"\Psi(r,t) = \frac{A}{r} \, e^{i(kr - \omega t)}",
            font_size=46, color=B_COLOR
        )
        sphere_note = Text(
            "Amplitude decays as 1/r — energy conservation over expanding sphere",
            font_size=26, color=WHITE
        )
        all_eqs = VGroup(plane, plane_note, sphere, sphere_note).arrange(DOWN, buff=0.35)
        for eq in all_eqs:
            self.play(Write(eq), run_time=1.0); self.wait(0.7)
        self.wait(2)
        self.play(FadeOut(VGroup(pw_title, all_eqs, title)))


# ── Week 1 Equation Summary ───────────────────────────────────────────────────
class Week1WavesSummary(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = equation_summary_card(
            "Week 1 Key Equations — Waves",
            [
                r"\frac{\partial^2\Psi}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2}",
                r"\Psi(x,t)=A\,e^{i(kx-\omega t)}, \quad v_p=\frac{\omega}{k}, \quad v_g=\frac{d\omega}{dk}",
                r"I \propto |\Psi|^2 = A^2",
            ]
        )
        self.play(FadeIn(card))
        self.wait(3)
        self.play(FadeOut(card))

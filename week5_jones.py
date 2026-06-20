# week5_jones.py  —  Week 5: Polarisation & Jones Formalism  (v2)
# Source: Bennett Ch. 6 (all)
from manim import *
from utils import *


class Week5TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEK 5",
            "Polarisation Optics: Wave Plates & Jones Formalism",
            "Bennett Ch. 6"
        )
        self.play(FadeIn(card)); self.wait(145.4); self.play(FadeOut(card))


class PolarisationStatesScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        make_pages(self, title, [
            "For a plane wave propagating in the z-direction, E⃗ lies in the x-y plane.",
            "The DIRECTION in which E⃗ oscillates defines the polarisation state.",
            "Human eyes cannot distinguish polarisation — we need special detectors.",
            "",
            "There are three fundamental polarisation states:",
            "LINEAR: E⃗ oscillates along a fixed direction in the x-y plane.",
            "CIRCULAR: the tip of E⃗ traces a circle as the wave passes (equal amplitudes, 90° phase shift).",
            "ELLIPTICAL: the general case — tip of E⃗ traces an ellipse (unequal amplitudes or arbitrary phase).",
        ], font_size=28, wait=13.5, lines_per_page=4)
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(22.2)
        self.wait(13.7); self.play(FadeOut(intro))

        # Detailed equations for each state
        states = [
            ("Linear Polarisation  (Bennett Section 6.2):",
             [r"E_x = E_{0x}e^{i(kz-\omega t)},\quad E_y = 0 \quad\text{(horizontal)}",
              r"\Delta\varphi = \varphi_y - \varphi_x = 0 \text{ or }\pi\quad\text{(any amplitude ratio)}",
              r"\text{The E-vector oscillates along a fixed line in the x-y plane.}"],
             E_COLOR,
             ["For horizontal linear:  E points along x-axis only.",
              "For vertical linear:    E points along y-axis only.",
              "For diagonal linear at angle α: E₀x/E₀y = tan(α), Δφ = 0."]),
            ("Circular Polarisation  (Bennett Section 6.4):",
             [r"|E_{0x}| = |E_{0y}| = E_0,\quad \Delta\varphi = \pm\frac{\pi}{2}",
              r"E_x = E_0\cos(kz-\omega t),\quad E_y = \pm E_0\sin(kz-\omega t)",
              r"\text{The E-vector tip traces a CIRCLE — amplitude is constant}"],
             B_COLOR,
             ["Right circular (RCP): Δφ = −π/2, E⃗ rotates clockwise viewed by receiver.",
              "Left  circular (LCP): Δφ = +π/2, E⃗ rotates counter-clockwise.",
              "Used in CD/DVD players, some satellite communications."]),
            ("Elliptical Polarisation  (Bennett Section 6.4):",
             [r"|E_{0x}| \neq |E_{0y}|\text{ or }\Delta\varphi\text{ not }0,\pm\pi/2,\pi",
              r"\text{The E-vector tip traces an ELLIPSE — most general case}",
              r"\text{Linear and circular are special cases of elliptical polarisation}"],
             N_COLOR,
             ["The ellipse's orientation and eccentricity depend on E₀x, E₀y, and Δφ.",
              "Can be completely characterised by the Stokes parameters or Jones vector."]),
        ]

        for state_name, eqs, color, desc_lines in states:
            s_title = Text(state_name, font_size=28, color=GOLD)
            s_title.next_to(title, DOWN, buff=0.5)
            safe_scale(s_title, max_width=13.5)
            self.play(Write(s_title))

            eq_mobs = VGroup()
            for e in eqs:
                em = MathTex(e, font_size=30, color=color)
                safe_scale(em, max_width=13.0)
                eq_mobs.add(em)
            eq_mobs.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
            eq_mobs.next_to(s_title, DOWN, buff=0.3)
            self.play(Write(eq_mobs)); self.wait(1.0)

            desc = section_intro(desc_lines, font_size=25)
            desc.next_to(eq_mobs, DOWN, buff=0.3)
            self.play(FadeIn(desc))
            self.wait(1.0)
            self.wait(1.0); self.play(FadeOut(VGroup(s_title, eq_mobs, desc)))


class BirefringenceWavePlates(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Birefringence & Wave Plates  (Bennett Section 6.3-6.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        make_pages(self, title, [
            "Birefringent crystals (quartz, calcite, LiNbO₃) have TWO different",
            "refractive indices for two perpendicular polarisation directions.",
            "",
            "The SLOW AXIS (high n) and FAST AXIS (low n) are the principal axes.",
            "Light polarised along the slow axis propagates more slowly (higher phase delay).",
            "Light polarised along the fast axis propagates more quickly.",
            "",
            "A slab of birefringent material of thickness d introduces a phase difference",
            "Δφ between the two polarisation components — this is a WAVE PLATE.",
        ], font_size=28, wait=9.2, lines_per_page=4)
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(15.0)
        self.wait(20.7); self.play(FadeOut(intro))

        # Phase retardation formula
        phase_title = Text("Phase Retardation  (Bennett Eq. 6.11):", font_size=28, color=GOLD)
        phase_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(phase_title))

        delta_phi = MathTex(
            r"\Delta\varphi = \frac{2\pi}{\lambda_0}(n_e - n_o)d",
            font_size=52, color=WAVE_COLOR)
        delta_phi.next_to(phase_title, DOWN, buff=0.3)
        self.play(Write(delta_phi)); self.wait(17.5)
        self.play(Create(gold_box(delta_phi))); self.wait(1.0)

        sym = eq_table([
            (r"n_e", "extraordinary (slow) refractive index", N_COLOR),
            (r"n_o", "ordinary (fast) refractive index", N_COLOR),
            (r"d",   "thickness of the wave plate [m]", WHITE),
            (r"\lambda_0", "vacuum wavelength of light [m]", WAVE_COLOR),
        ], eq_fs=30, lbl_fs=23, buff=0.22)
        sym.next_to(delta_phi, DOWN, buff=0.35)
        for row in sym: self.play(FadeIn(row)); self.wait(1.0)
        self.wait(1.0); self.play(FadeOut(VGroup(phase_title, delta_phi, sym)))

        # QWP and HWP
        for plate_name, delta, thickness_eq, effects, color in [
            ("Quarter-Wave Plate (QWP)  Δφ = π/2:",
             r"\Delta\varphi = \frac{\pi}{2},\quad d_{\min} = \frac{\lambda_0}{4|n_e-n_o|}",
             r"d_{\min}(\text{quartz, 589nm}) = \frac{589\text{nm}}{4\times0.0092} = 16.0\;\mu\text{m}",
             ["Effect: converts linear (at 45°) → circular polarisation, and vice versa.",
              "Used in: isolators, Stokes parameter measurements, optical pickups in CD players.",
              "Quarter-wave plates appear at many wavelengths — thickness varies with λ."],
             WAVE_COLOR),
            ("Half-Wave Plate (HWP)  Δφ = π:",
             r"\Delta\varphi = \pi,\quad d_{\min} = \frac{\lambda_0}{2|n_e-n_o|}",
             r"d_{\min}(\text{quartz, 589nm}) = \frac{589\text{nm}}{2\times0.0092} = 32.0\;\mu\text{m}",
             ["Effect: rotates linear polarisation by 2α, where α is the angle between",
              "the input E-field direction and the wave plate's fast axis.",
              "Used in: polarisation rotators, continuous power control of laser beams."],
             WAVE_COLOR),
        ]:
            p_title = Text(plate_name, font_size=28, color=GOLD)
            p_title.next_to(title, DOWN, buff=0.5)
            self.play(Write(p_title))

            eq1 = MathTex(delta, font_size=38, color=color)
            eq1.next_to(p_title, DOWN, buff=0.3)
            safe_scale(eq1, max_width=13.0)
            self.play(Write(eq1)); self.wait(1.0)

            eq2 = MathTex(thickness_eq, font_size=32, color=N_COLOR)
            eq2.next_to(eq1, DOWN, buff=0.3)
            safe_scale(eq2, max_width=13.0)
            self.play(Write(eq2)); self.wait(1.0)

            eff = section_intro(effects, font_size=25)
            eff.next_to(eq2, DOWN, buff=0.3)
            self.play(FadeIn(eff))
            self.wait(1.0)
            self.wait(1.0); self.play(FadeOut(VGroup(p_title, eq1, eq2, eff)))


class JonesFormalism(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        make_pages(self, title, [
            "The Jones vector is a compact 2-component complex vector that fully",
            "specifies the polarisation state of a monochromatic plane wave.",
            "It encodes BOTH the amplitude AND phase of E_x and E_y.",
            "",
            "Convention: the e^{i(kz−ωt)} propagation factor is IMPLICIT — not written.",
            "Normalised Jones vectors have unit magnitude: |E̊|² = 1.",
        ], font_size=28, wait=15.9, lines_per_page=4)
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(22.6)
        self.wait(8.0); self.play(FadeOut(intro))

        gen = MathTex(
            r"\tilde{E} = \begin{pmatrix}E_{0x}e^{i\varphi_x}\\E_{0y}e^{i\varphi_y}\end{pmatrix}",
            font_size=48, color=E_COLOR)
        gen.next_to(title, DOWN, buff=0.5)
        self.play(Write(gen)); self.wait(1.0)

        # Table of all standard Jones vectors
        states_title = Text("Standard Normalised Jones Vectors  (Bennett Table 6.1):", font_size=28, color=GOLD)
        states_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(states_title))

        states = [
            (r"\hat{e}_H = \begin{pmatrix}1\\0\end{pmatrix}",          "Horizontal linear",    E_COLOR),
            (r"\hat{e}_V = \begin{pmatrix}0\\1\end{pmatrix}",          "Vertical linear",      E_COLOR),
            (r"\hat{e}_{+45} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}", "Linear +45°", E_COLOR),
            (r"\hat{e}_{-45} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}", "Linear −45°", E_COLOR),
            (r"\hat{e}_R = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}", "Right circular (RCP)", B_COLOR),
            (r"\hat{e}_L = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\+i\end{pmatrix}", "Left circular (LCP)",  B_COLOR),
        ]
        state_mobs = VGroup()
        for latex, label, color in states:
            eq  = MathTex(latex, font_size=28, color=color)
            lbl = Text(label, font_size=23, color=WHITE)
            row = VGroup(eq, lbl).arrange(RIGHT, buff=0.5)
            state_mobs.add(row)
        state_mobs.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        state_mobs.next_to(states_title, DOWN, buff=0.3)
        safe_scale(state_mobs, max_height=5.0)

        for row in state_mobs:
            self.play(FadeIn(row), run_time=0.5); self.wait(1.0)
        self.wait(1.0); self.play(FadeOut(VGroup(title, states_title, state_mobs)))


class JonesMatrices(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        make_pages(self, title, [
            "Each optical element is represented by a 2×2 Jones matrix J.",
            "Output vector = J × Input vector:  Ẽ_out = J · Ẽ_in",
            "For a sequence of N elements, multiply RIGHT-TO-LEFT:",
            "Ẽ_out = J_N · ... · J_2 · J_1 · Ẽ_in",
            "Transmitted intensity (when input is normalised): I_out = |Ẽ_out|²",
        ], font_size=28, wait=12.6, lines_per_page=4)
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(9.7)
        self.wait(10.6); self.play(FadeOut(intro))

        matrices = [
            (r"J_{\text{pol},H} = \begin{pmatrix}1&0\\0&0\end{pmatrix}",
             "Linear polariser, horizontal transmission axis", E_COLOR),
            (r"J_{\text{pol},V} = \begin{pmatrix}0&0\\0&1\end{pmatrix}",
             "Linear polariser, vertical transmission axis", E_COLOR),
            (r"J_{\text{pol},\theta} = \begin{pmatrix}\cos^2\theta&\sin\theta\cos\theta\\\sin\theta\cos\theta&\sin^2\theta\end{pmatrix}",
             "Linear polariser with transmission axis at angle θ from horizontal", E_COLOR),
            (r"J_{\text{QWP},H} = \begin{pmatrix}1&0\\0&-i\end{pmatrix}",
             "Quarter-wave plate, fast axis horizontal (slow axis vertical)", WAVE_COLOR),
            (r"J_{\text{QWP},V} = \begin{pmatrix}1&0\\0&+i\end{pmatrix}",
             "Quarter-wave plate, fast axis vertical", WAVE_COLOR),
            (r"J_{\text{HWP},H} = \begin{pmatrix}1&0\\0&-1\end{pmatrix}",
             "Half-wave plate, fast axis horizontal", WAVE_COLOR),
            (r"J_{\text{rot}}(\alpha) = \begin{pmatrix}\cos\alpha&\sin\alpha\\-\sin\alpha&\cos\alpha\end{pmatrix}",
             "Coordinate rotation matrix: rotates reference frame by angle α", N_COLOR),
        ]

        for latex, label, color in matrices:
            mat  = MathTex(latex, font_size=36, color=color)
            lbl  = Text(label, font_size=24, color=WHITE)
            block = VGroup(mat, lbl).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
            safe_scale(block, max_width=13.0)
            block.next_to(title, DOWN, buff=0.45)
            self.play(FadeIn(block)); self.wait(8.2); self.play(FadeOut(block))

        # Rotated element formula
        rot_title = Text("Rotating an Element  (Bennett Eq. 6.25):", font_size=28, color=GOLD)
        rot_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(rot_title))

        rot_formula = MathTex(
            r"J_{\text{rotated}} = J_{\text{rot}}(-\alpha)\cdot J_{\text{element}}\cdot J_{\text{rot}}(\alpha)",
            font_size=36, color=N_COLOR)
        rot_formula.next_to(rot_title, DOWN, buff=0.3)
        safe_scale(rot_formula, max_width=13.0)
        self.play(Write(rot_formula)); self.wait(13.2)
        self.play(FadeOut(*self.mobjects), run_time=0.5); self.play(FadeOut(VGroup(rot_title, rot_formula)))

        # Full worked example
        ex_title = Text("Example: 45° input → HWP(fast H) → QWP(fast V) → find output", font_size=26, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        safe_scale(ex_title, max_width=13.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.35)
        solver.add_step(1,
            r"\tilde{E}_{\text{in}} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} \quad \text{(linear +45°)}",
            "starting Jones vector: normalised +45° linear polarisation", E_COLOR)
        solver.add_step(2,
            r"J_{\text{HWP}}\tilde{E}_{\text{in}} = \begin{pmatrix}1&0\\0&-1\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}",
            "after HWP: output is linear −45° (HWP rotated polarisation by 90°)", E_COLOR)
        solver.add_step(3,
            r"J_{\text{QWP},V}\cdot\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix} = \begin{pmatrix}1&0\\0&i\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}",
            "after QWP: output is right circular polarisation!", B_COLOR)
        solver.add_step(4,
            r"\left|\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}\right|^2 = \frac{1}{2}(|1|^2+|-i|^2) = \frac{1}{2}(1+1) = 1",
            "intensity check: |Ẽ_out|² = 1 ✓ — normalised, no loss through wave plates", GOLD)
        solver.finalize()

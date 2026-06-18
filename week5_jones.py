# week5_jones.py
# 31OPT Optics — Week 5: Polarisation Optics & Jones Formalism
from manim import *
from utils import *


class Week5TitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "WEEK 5",
            "Polarisation Optics: Wave Plates & Jones Formalism",
            "Bennett Ch. 6"
        )
        self.play(FadeIn(card)); self.wait(2); self.play(FadeOut(card))


class PolarisationStatesScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("States of Polarisation", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Polarisation describes the direction of the electric field oscillation.",
            "For a plane wave travelling in z, E can point in x, y, or a combination.",
            "Three states: linear, circular, elliptical.",
            "Birefringent materials and wave plates control the polarisation state.",
            "Jones vectors and matrices give a compact mathematical way to handle all this."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        lin_title = Text("Linear Polarisation:", font_size=28, color=E_COLOR)
        lin = MathTex(
            r"E_x = E_{0x} e^{i(kz-\omega t)},\quad E_y = 0 \quad (\text{horizontal})",
            font_size=32, color=E_COLOR)
        lin2 = MathTex(
            r"\Delta\varphi = 0,\quad |E_{0x}|, |E_{0y}| \text{ arbitrary}",
            font_size=28, color=E_COLOR)

        circ_title = Text("Circular Polarisation:", font_size=28, color=B_COLOR)
        circ = MathTex(
            r"|E_{0x}| = |E_{0y}|,\quad \Delta\varphi = \pm\frac{\pi}{2}",
            font_size=32, color=B_COLOR)
        circ2 = MathTex(
            r"E_x = E_0\cos(kz-\omega t),\quad E_y = \pm E_0\sin(kz-\omega t)",
            font_size=28, color=B_COLOR)

        ell_title = Text("Elliptical Polarisation (general):", font_size=28, color=N_COLOR)
        ell = MathTex(
            r"E_{0x} \neq E_{0y},\quad \Delta\varphi \text{ arbitrary} \Rightarrow \text{ellipse}",
            font_size=32, color=N_COLOR)

        all_states = VGroup(
            VGroup(lin_title, lin, lin2).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(circ_title, circ, circ2).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(ell_title, ell).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
        ).arrange(DOWN, buff=0.4)
        for state in all_states:
            self.play(FadeIn(state)); self.wait(1.2)
        self.wait(2); self.play(FadeOut(VGroup(title, all_states)))


class BirefringenceWavePlates(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Birefringence & Wave Plates", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Birefringent crystals have two principal refractive indices: n_e and n_o.",
            "The two polarisation components (fast/slow axis) travel at different speeds.",
            "A wave plate accumulates a phase difference Delta-phi between the two components.",
            "Quarter-wave plate (QWP): Delta-phi = pi/2.   Half-wave plate (HWP): Delta-phi = pi."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        delta_phi = MathTex(
            r"\Delta\varphi = \frac{2\pi}{\lambda_0}(n_e - n_o) d",
            font_size=46, color=WAVE_COLOR
        )
        opd = MathTex(r"\text{OPD} = (n_e - n_o)\, d", font_size=36, color=WAVE_COLOR)
        self.play(Write(delta_phi)); self.wait(1); self.play(Write(opd)); self.wait(1.5)

        # QWP
        self.play(FadeOut(VGroup(delta_phi, opd)))
        qwp_title = Text("Quarter-Wave Plate (QWP):", font_size=32, color=GOLD)
        qwp_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(qwp_title))

        qwp_cond  = MathTex(r"\Delta\varphi = \frac{\pi}{2} + m \cdot 2\pi,\quad m=0,1,2,\ldots",
                            font_size=36, color=WAVE_COLOR)
        qwp_thick = MathTex(r"d_{\min} = \frac{\lambda_0}{4|n_e - n_o|}",
                            font_size=38, color=N_COLOR)
        qwp_effect = Text("Effect: Linear (at 45°) → Circular.   Circular → Linear.",
                          font_size=28, color=WHITE)
        qwp_group = VGroup(qwp_cond, qwp_thick, qwp_effect).arrange(DOWN, buff=0.35)
        qwp_group.next_to(qwp_title, DOWN, buff=0.3)
        for item in qwp_group:
            self.play(Write(item) if isinstance(item, MathTex) else FadeIn(item)); self.wait(0.8)

        qwp_ex  = MathTex(
            r"\text{Quartz: } n_e - n_o = 0.0092,\; \lambda_0=589\text{ nm}:",
            font_size=28, color=GOLD)
        qwp_ex2 = MathTex(
            r"d_{\min} = \frac{589 \times 10^{-9}}{4 \times 0.0092} = 16.0\;\mu\text{m}",
            font_size=34, color=N_COLOR)
        qwp_ex_group = VGroup(qwp_ex, qwp_ex2).arrange(DOWN, buff=0.2)
        qwp_ex_group.next_to(qwp_group, DOWN, buff=0.3)
        self.play(Write(qwp_ex_group)); self.play(Create(gold_box(qwp_ex2))); self.wait(1.5)

        # HWP
        self.play(FadeOut(VGroup(qwp_title, qwp_group, qwp_ex_group)))
        hwp_title = Text("Half-Wave Plate (HWP):", font_size=32, color=GOLD)
        hwp_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(hwp_title))

        hwp_cond  = MathTex(r"\Delta\varphi = \pi + m \cdot 2\pi,\quad m=0,1,2,\ldots",
                            font_size=36, color=WAVE_COLOR)
        hwp_thick = MathTex(r"d_{\min} = \frac{\lambda_0}{2|n_e - n_o|}",
                            font_size=38, color=N_COLOR)
        hwp_effect = Text(
            "Effect: Rotates linear polarisation by 2*alpha  (alpha = angle between E and fast axis).",
            font_size=26, color=WHITE)
        hwp_group = VGroup(hwp_cond, hwp_thick, hwp_effect).arrange(DOWN, buff=0.35)
        hwp_group.next_to(hwp_title, DOWN, buff=0.3)
        for item in hwp_group:
            self.play(Write(item) if isinstance(item, MathTex) else FadeIn(item)); self.wait(0.8)
        self.wait(2); self.play(FadeOut(VGroup(title, hwp_title, hwp_group)))


class JonesFormalism(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Jones Vectors", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "A Jones vector is a 2-component complex vector representing the polarisation state.",
            "It encodes both amplitude and phase of E_x and E_y.",
            "Normalised: the squared magnitude equals 1 (unit irradiance).",
            "The e^(i(kz-wt)) factor is implicit — not written in the Jones vector."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        gen = MathTex(
            r"\tilde{E} = \begin{pmatrix} E_{0x} e^{i\varphi_x} \\ E_{0y} e^{i\varphi_y} \end{pmatrix}",
            font_size=44, color=E_COLOR
        )
        self.play(Write(gen)); self.wait(1.2)

        states_title = Text("Standard normalised Jones vectors:", font_size=30, color=GOLD)
        states_title.next_to(gen, DOWN, buff=0.5)
        self.play(Write(states_title))

        states = [
            (r"\hat{e}_H = \begin{pmatrix} 1 \\ 0 \end{pmatrix}",
             "Horizontal linear"),
            (r"\hat{e}_V = \begin{pmatrix} 0 \\ 1 \end{pmatrix}",
             "Vertical linear"),
            (r"\hat{e}_{+45} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}",
             "Linear +45 deg"),
            (r"\hat{e}_{-45} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}",
             "Linear -45 deg"),
            (r"\hat{e}_R = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix}",
             "Right circular"),
            (r"\hat{e}_L = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ +i \end{pmatrix}",
             "Left circular"),
        ]
        state_rows = VGroup()
        for latex, label in states:
            tex = MathTex(latex, font_size=26, color=E_COLOR)
            lbl = Text(label, font_size=22, color=WHITE)
            state_rows.add(VGroup(tex, lbl).arrange(RIGHT, buff=0.5))
        state_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        state_rows.next_to(states_title, DOWN, buff=0.3)
        for row in state_rows:
            self.play(FadeIn(row), run_time=0.5); self.wait(0.4)
        self.wait(2); self.play(FadeOut(VGroup(title, gen, states_title, state_rows)))


class JonesMatrices(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Jones Matrices", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Each optical element (polariser, wave plate) is a 2x2 Jones matrix J.",
            "The output Jones vector is:  E_out = J * E_in.",
            "For a sequence of elements, multiply matrices right-to-left.",
            "Transmitted intensity fraction = |E_out|^2 when input is normalised."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        conv = MathTex(
            r"\tilde{E}_{\text{out}} = J_N \cdots J_2 \cdot J_1 \cdot \tilde{E}_{\text{in}}",
            font_size=42, color=GOLD
        )
        self.play(Write(conv)); self.wait(1.2); self.play(FadeOut(conv))

        matrices = [
            (r"J_{\text{pol},H} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}",
             "Linear polariser, horizontal transmission axis", E_COLOR),
            (r"J_{\text{pol},V} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}",
             "Linear polariser, vertical transmission axis", E_COLOR),
            (r"J_{\text{pol},\theta} = \begin{pmatrix} \cos^2\theta & \sin\theta\cos\theta \\ \sin\theta\cos\theta & \sin^2\theta \end{pmatrix}",
             "Linear polariser at angle theta", E_COLOR),
            (r"J_{\text{QWP},H} = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}",
             "Quarter-wave plate, fast axis horizontal", WAVE_COLOR),
            (r"J_{\text{QWP},V} = \begin{pmatrix} 1 & 0 \\ 0 & +i \end{pmatrix}",
             "Quarter-wave plate, fast axis vertical", WAVE_COLOR),
            (r"J_{\text{HWP},H} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}",
             "Half-wave plate, fast axis horizontal", WAVE_COLOR),
            (r"J_{\text{rot}}(\alpha) = \begin{pmatrix} \cos\alpha & \sin\alpha \\ -\sin\alpha & \cos\alpha \end{pmatrix}",
             "Rotation matrix (rotate element by angle alpha)", N_COLOR),
        ]

        for latex, label, color in matrices:
            mat  = MathTex(latex, font_size=34, color=color)
            lbl  = Text(label, font_size=24, color=WHITE)
            block = VGroup(mat, lbl).arrange(DOWN, buff=0.15)
            block.next_to(title, DOWN, buff=0.4)
            self.play(FadeIn(block)); self.wait(1.4); self.play(FadeOut(block))

        rot_formula = MathTex(
            r"J_{\text{rotated}} = J_{\text{rot}}(-\alpha) \cdot J_{\text{element}} \cdot J_{\text{rot}}(\alpha)",
            font_size=34, color=N_COLOR
        )
        rot_formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(rot_formula)); self.wait(2)

        # Worked example
        self.play(FadeOut(rot_formula))
        ex_title = Text(
            "Example: 45-deg input → HWP (fast H) → QWP (fast V) → pol at 45 deg",
            font_size=24, color=GOLD
        )
        ex_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(ex_title))

        s1 = MathTex(
            r"\tilde{E}_{\text{in}} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}",
            font_size=32, color=E_COLOR)
        s2 = MathTex(
            r"\text{After HWP: }\begin{pmatrix}1&0\\0&-1\end{pmatrix}"
            r"\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}"
            r"=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}",
            font_size=26, color=E_COLOR)
        s3 = MathTex(
            r"\text{After QWP(V): }\begin{pmatrix}1&0\\0&i\end{pmatrix}"
            r"\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}"
            r"=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}\text{ (right circ.)}",
            font_size=24, color=B_COLOR)
        s4 = MathTex(
            r"|\tilde{E}_{\text{out}}|^2 = \frac{1}{2}(1+1) = 1 \;\Rightarrow\; 100\%"
            r"\text{ intensity into pol at }45°",
            font_size=26, color=GOLD)
        steps = VGroup(s1, s2, s3, s4).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(ex_title, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s), run_time=1.0); self.wait(0.7)
        self.play(Create(gold_box(s4)))
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, steps)))

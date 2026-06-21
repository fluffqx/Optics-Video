# week5_jones.py  —  Week 5: Polarisation & Jones Formalism  (v2)
# Source: Bennett Ch. 6 (all)
from manim import *
from utils import *


class Week5TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/Week5TitleCard.mp3", time_offset=0)
        card = make_title_card(
            "WEEK 5",
            "Polarisation Optics: Wave Plates & Jones Formalism",
            "Bennett Ch. 6"
        )
        self.play(FadeIn(card)); self.wait(148.8); self.play(FadeOut(card))


class PolarisationStatesScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/PolarisationStatesScene.mp3", time_offset=0)
        title = Text("States of Polarisation  (Bennett Section 6.1)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "For a plane wave in z-direction, E lies in the x-y plane.",
            "Linear: Delta_phi = 0 or pi — E oscillates along fixed line.",
            "Circular: |Ex|=|Ey| and Delta_phi = +/-pi/2 — E traces a circle.",
            "Elliptical: general case — E traces an ellipse. Most general state.",
        ])
        safe_scale(b, max_width=13.0, max_height=4.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(50.4)

class BirefringenceWavePlates(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/BirefringenceWavePlates.mp3", time_offset=0)
        title = Text("Birefringence and Wave Plates  (Bennett 6.3-6.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq_dp = MathTex(r"\Delta\phi = \frac{2\pi}{\lambda_0}(n_e - n_o)d",
                        font_size=46, color=WAVE_COLOR)
        safe_scale(eq_dp)
        eq_dp.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(eq_dp, run_time=0.1))
        b = txt_block([
            "Birefringent crystals (quartz, calcite) have two refractive indices: n_e and n_o.",
            "QWP: Delta_phi = pi/2.  Converts +/-45 deg linear to circular (and back).",
            "  Minimum thickness: d = lambda_0 / (4 |n_e - n_o|).",
            "HWP: Delta_phi = pi.  Rotates linear polarisation by 2*alpha.",
            "  Minimum thickness: d = lambda_0 / (2 |n_e - n_o|).",
        ])
        safe_scale(b, max_width=13.0, max_height=3.5)
        b.next_to(eq_dp, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(63.8)

class JonesFormalism(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/JonesFormalism.mp3", time_offset=0)
        title = Text("Jones Vectors  (Bennett Section 6.5)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        table = eq_table([
            (r"\begin{pmatrix}1\\0\end{pmatrix}", "Horizontal linear", WHITE),
            (r"\begin{pmatrix}0\\1\end{pmatrix}", "Vertical linear", WHITE),
            (r"\dfrac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}", "+45 deg linear", E_COLOR),
            (r"\dfrac{1}{\sqrt{2}}\begin{pmatrix}1\\-i\end{pmatrix}", "Right circular (RCP)", B_COLOR),
            (r"\dfrac{1}{\sqrt{2}}\begin{pmatrix}1\\+i\end{pmatrix}", "Left circular (LCP)", B_COLOR),
        ], eq_fs=30, lbl_fs=22, buff=0.22)
        safe_scale(table, max_width=13.0, max_height=4.5)
        table.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(table, run_time=0.1))
        self.wait(47.5)

class JonesMatrices(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/JonesMatrices.mp3", time_offset=0)
        title = Text("Jones Matrices  (Bennett Section 6.5.1)", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        mats = VGroup(
            labeled_eq(r"\begin{pmatrix}1&0\\0&0\end{pmatrix}", "Horizontal polariser", WHITE, 34, 22),
            labeled_eq(r"\begin{pmatrix}0&0\\0&1\end{pmatrix}", "Vertical polariser", WHITE, 34, 22),
            labeled_eq(r"\begin{pmatrix}1&0\\0&-i\end{pmatrix}", "QWP fast axis horizontal", WAVE_COLOR, 34, 22),
            labeled_eq(r"\begin{pmatrix}1&0\\0&-1\end{pmatrix}", "HWP fast axis horizontal", B_COLOR, 34, 22),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        safe_scale(mats, max_width=13.0, max_height=4.5)
        mats.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(mats, run_time=0.1))
        b = txt_block(["Output = J_N x ... x J_1 x J_in  (right-to-left multiplication).",
                       "Intensity: I = |J_out|^2 = J_out . J_out* — always check this."], 24)
        safe_scale(b, max_width=13.0)
        b.next_to(mats, DOWN, buff=0.3)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(56.2)

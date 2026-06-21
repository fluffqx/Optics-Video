# week6_interference.py  —  Weeks 5-6: Interference  (v2)
# Source: Bennett Ch. 7.1-7.3.5, 7.8
from manim import *
from utils import *


class Week6TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/Week6TitleCard.mp3", time_offset=0)
        card = make_title_card(
            "WEEKS 5–6",
            "Interference: Two-Beam, Young's, Thin Films & Michelson",
            "Bennett Ch. 7.1–7.3.5, 7.8"
        )
        self.play(FadeIn(card)); self.wait(157.0); self.play(FadeOut(card))


class InterferenceIntroScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/InterferenceIntroScene.mp3", time_offset=0)
        title = Text("Introduction to Interference  (Bennett Ch. 7)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\delta",
                     font_size=50, color=INTENSITY_COLOR)
        safe_scale(eq)
        eq.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(eq, run_time=0.1))
        b = txt_block([
            "Interference occurs when two coherent waves overlap in the same region.",
            "The third term 2*sqrt(I1*I2)*cos(delta) is the INTERFERENCE TERM.",
            "It can add (constructive) or subtract (destructive) — energy is redistributed.",
            "Energy is CONSERVED: averaged over space the total equals I1 + I2.",
        ])
        safe_scale(b, max_width=13.0, max_height=3.0)
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(56.6)

class TwoBeamInterference(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/TwoBeamInterference.mp3", time_offset=0)
        title = Text("Two-Beam Interference Formula  (Bennett Section 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Consider two monochromatic EM waves overlapping at a point P.",
            "Bennett derives the interference irradiance in Section 7.3.2 (Eq. 7.16):",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(15.0)
        self.wait(25.1); self.play(FadeOut(intro))

        general = MathTex(
            r"I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\delta",
            font_size=56, color=INTENSITY_COLOR)
        general.next_to(title, DOWN, buff=0.5)
        self.play(Write(general)); self.wait(24.1)
        self.play(Create(gold_box(general))); self.wait(21.9)

        sym = eq_table([
            (r"I_1, I_2", "irradiances of the individual beams  [W/m²]", INTENSITY_COLOR),
            (r"\delta",   "phase difference between the two beams at point P  [rad]", WAVE_COLOR),
            (r"2\sqrt{I_1 I_2}\cos\delta", "interference term — the KEY new physics", GOLD),
        ], eq_fs=30, lbl_fs=24, buff=0.25)
        sym.next_to(general, DOWN, buff=0.4)
        for row in sym: self.play(FadeIn(row)); self.wait(1.0)
        self.wait(1.0); self.play(FadeOut(sym))

        # Phase difference definition
        phase_title = Text("Phase Difference δ  (Bennett Eq. 7.17):", font_size=28, color=GOLD)
        phase_title.next_to(general, DOWN, buff=0.45)
        self.play(Write(phase_title))

        delta_def = MathTex(
            r"\delta = \frac{2\pi}{\lambda_0}\times\text{OPD} + \Delta\varphi_{\text{refl}}",
            font_size=42, color=WAVE_COLOR)
        delta_def.next_to(phase_title, DOWN, buff=0.3)
        safe_scale(delta_def, max_width=13.0)
        self.play(Write(delta_def)); self.wait(1.0)

        opd_def = MathTex(
            r"\text{OPD} = n_2 d_2 - n_1 d_1 \quad\text{(optical path = refractive index × geometric path)}",
            font_size=30, color=WHITE)
        opd_def.next_to(delta_def, DOWN, buff=0.3)
        safe_scale(opd_def, max_width=13.0)
        self.play(Write(opd_def)); self.wait(1.0)

        refl_note = MathTex(
            r"\Delta\varphi_{\text{refl}} = \pi \text{ for each reflection where } n_{\text{reflected}} > n_{\text{incident}}",
            font_size=28, color=B_COLOR)
        refl_note.next_to(opd_def, DOWN, buff=0.3)
        safe_scale(refl_note, max_width=13.0)
        self.play(Write(refl_note)); self.wait(1.0)

        # Equal intensities
        eq_int_title = Text("Special Case: Equal Intensities  I₁ = I₂ = I₀:", font_size=28, color=GOLD)
        eq_int_title.next_to(general, DOWN, buff=0.45)
        self.play(Write(eq_int_title))

        equal_I = MathTex(
            r"I = 4I_0\cos^2\!\left(\frac{\delta}{2}\right)",
            font_size=56, color=INTENSITY_COLOR)
        equal_I.next_to(eq_int_title, DOWN, buff=0.3)
        self.play(Write(equal_I)); self.wait(1.0)

        cond_rows = eq_table([
            (r"\delta = 2m\pi \;\Rightarrow\; I = 4I_0",
             "CONSTRUCTIVE (maximum): δ=0, 2π, 4π, ...  intensity is 4× single beam!", E_COLOR),
            (r"\delta = (2m+1)\pi \;\Rightarrow\; I = 0",
             "DESTRUCTIVE (minimum): δ=π, 3π, 5π, ...  complete cancellation!", B_COLOR),
            (r"\text{Average: } \langle I\rangle = 2I_0",
             "averaged over space: energy is conserved — just redistributed", GOLD),
        ], eq_fs=28, lbl_fs=22, buff=0.25)
        cond_rows.next_to(equal_I, DOWN, buff=0.35)
        for row in cond_rows: self.play(FadeIn(row)); self.wait(1.0)
        self.wait(87.4); self.play(FadeOut(VGroup(title, general, eq_int_title, equal_I, cond_rows)))


class YoungDoubleSlit(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/YoungDoubleSlit.mp3", time_offset=0)
        title = Text("Young's Double-Slit Experiment  (Bennett Section 7.3.2.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Young's 1801 experiment was the first PROOF that light is a wave.",
            "Newton's corpuscular theory could not explain the dark fringes.",
            "Two slits separated by d, illuminated by coherent monochromatic light.",
            "A screen at distance L  (L >> d) shows alternating bright and dark fringes.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(16.4)
        self.wait(25.0); self.play(FadeOut(intro))

        # Path difference
        path_title = Text("Path Difference and Phase Difference:", font_size=28, color=GOLD)
        path_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(path_title))

        path = MathTex(
            r"\Delta = r_2 - r_1 \approx d\sin\theta \approx \frac{dy}{L} \quad (L \gg d)",
            font_size=36, color=WAVE_COLOR)
        path.next_to(path_title, DOWN, buff=0.3)
        safe_scale(path, max_width=13.0)
        self.play(Write(path)); self.wait(8.2)

        phase = MathTex(
            r"\delta = \frac{2\pi}{\lambda}d\sin\theta = \frac{2\pi dy}{\lambda L}",
            font_size=44, color=WAVE_COLOR)
        phase.next_to(path, DOWN, buff=0.3)
        self.play(Write(phase)); self.wait(19.8)

        # Fringe conditions
        bright = MathTex(
            r"\text{Bright fringes: } d\sin\theta = m\lambda,\quad m = 0, \pm1, \pm2, \ldots",
            font_size=32, color=E_COLOR)
        dark   = MathTex(
            r"\text{Dark fringes: } d\sin\theta = \left(m+\tfrac{1}{2}\right)\lambda",
            font_size=32, color=B_COLOR)
        fringe_pos = MathTex(
            r"y_m = \frac{m\lambda L}{d} \quad\text{(position of m-th bright fringe on screen)}",
            font_size=34, color=E_COLOR)
        fringe_spacing = MathTex(
            r"\Delta y = \frac{\lambda L}{d} \quad\text{(spacing between adjacent bright fringes)}",
            font_size=40, color=GOLD)

        fringes = VGroup(bright, dark, fringe_pos, fringe_spacing).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        fringes.next_to(phase, DOWN, buff=0.3)
        safe_scale(fringes, max_height=3.5)
        for f in fringes: self.play(Write(f), run_time=0.9); self.wait(17.4)
        self.play(Create(gold_box(fringe_spacing)))
        self.wait(21.4); self.play(FadeOut(VGroup(path_title, path, phase, fringes)))

        # Intensity pattern
        int_title = Text("Intensity Pattern  (Bennett Eq. 7.18):", font_size=28, color=GOLD)
        int_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(int_title))

        int_eq = MathTex(
            r"I(\theta) = 4I_0\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right)",
            font_size=44, color=INTENSITY_COLOR)
        int_eq.next_to(int_title, DOWN, buff=0.3)
        self.play(Write(int_eq)); self.wait(110.4)
        self.play(FadeOut(*self.mobjects), run_time=0.5)
        self.play(FadeOut(VGroup(int_title, int_eq)))

        # Full worked example
        ex_title = Text("Example: d=0.100mm, L=1.50m, λ=589nm (sodium light)", font_size=27, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"\Delta y = \frac{\lambda L}{d} = \frac{589\times10^{-9}\times1.50}{0.100\times10^{-3}}",
            "fringe spacing formula")
        solver.add_step(2,
            r"= \frac{883.5\times10^{-9}}{10^{-4}} = 8.835\times10^{-3}\text{ m} = 8.84\text{ mm}",
            "fringe spacing = 8.84 mm — easily visible with the naked eye!", GOLD)
        solver.add_step(3,
            r"\text{10th bright fringe: } y_{10} = \frac{10\times589\times10^{-9}\times1.50}{10^{-4}} = 88.4\text{ mm}",
            "position of the 10th bright fringe from centre")
        solver.add_step(4,
            r"\delta_{\text{at }y=5\text{mm}} = \frac{2\pi\times5\times10^{-3}\times10^{-4}}{589\times10^{-9}\times1.50} = 3.56\text{ rad}",
            "phase difference at y=5mm — not a maximum or minimum")
        solver.finalize()


class ThinFilmInterference(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/ThinFilmInterference.mp3", time_offset=0)
        title = Text("Thin Film Interference  (Bennett Section 7.3.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\delta = \frac{4\pi n_f t \cos\theta_t}{\lambda_0} + \Delta\phi_{\rm refl}",
                     font_size=44, color=WAVE_COLOR)
        safe_scale(eq)
        eq.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(eq, run_time=0.1))
        b1 = txt_block([
            "Step 1: For each reflection, check if n increases (+pi shift) or decreases (0 shift).",
            "Step 2: Net Delta_phi_refl = (beam2 shift) - (beam1 shift).",
            "Step 3: Constructive: delta = 2m*pi.  Destructive: delta = (2m+1)*pi.",
        ])
        safe_scale(b1, max_width=13.0, max_height=2.5)
        b1.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(b1, run_time=0.1))
        self.wait(30)
        self.play(FadeOut(b1))
        b2 = txt_block([
            "AR coating example: MgF2 (n=1.38) on glass (n=1.52).",
            "Both reflections: n increases each time -> both beams get +pi shift.",
            "Net Delta_phi_refl = 0.  Destructive condition: 2*n_f*t = lambda/2.",
            "Minimum thickness: t = lambda / (4 * n_f) = 550/(4*1.38) = 100 nm.",
        ])
        safe_scale(b2, max_width=13.0, max_height=2.8)
        b2.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(b2, run_time=0.1))
        self.wait(91.7)

class FringeVisibility(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/FringeVisibility.mp3", time_offset=0)
        title = Text("Fringe Visibility  (Bennett Section 7.3.4)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Not all interference patterns have perfect contrast.",
            "The VISIBILITY (or fringe contrast) V quantifies how sharp the fringes are.",
            "V=1 means perfect contrast (maximum dark, maximum bright).",
            "V=0 means no fringes at all — beams are incoherent.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(6.8)
        self.wait(13.1); self.play(FadeOut(intro))

        vis = MathTex(
            r"V = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}} = \frac{2\sqrt{I_1 I_2}}{I_1+I_2}",
            font_size=48, color=INTENSITY_COLOR)
        vis.next_to(title, DOWN, buff=0.5)
        self.play(Write(vis)); self.wait(16.9)
        self.play(Create(gold_box(vis))); self.wait(13.3)

        vis_rows = eq_table([
            (r"V = 1", "PERFECT visibility — I₁=I₂ and fully coherent (only possible for lasers)", GOLD),
            (r"V = \frac{2\sqrt{I_1 I_2}}{I_1+I_2} < 1", "when I₁ ≠ I₂: visibility < 1 even with coherent beams", WHITE),
            (r"V = 0", "no fringes — either completely incoherent or one beam is blocked", B_COLOR),
        ], eq_fs=30, lbl_fs=23, buff=0.28)
        vis_rows.next_to(vis, DOWN, buff=0.4)
        for row in vis_rows: self.play(FadeIn(row)); self.wait(1.0)
        self.wait(51.4); self.play(FadeOut(VGroup(title, vis, vis_rows)))


class MichelsonScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/MichelsonScene.mp3", time_offset=0)
        title = Text("Michelson Interferometer  (Bennett Section 7.8)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"\text{OPD} = 2\Delta L", "optical path difference (factor 2: beam travels twice)", WAVE_COLOR, 42, 24),
            labeled_eq(r"N = 2\Delta L/\lambda", "number of fringes counted as mirror moves by Delta L", GOLD, 42, 24),
            labeled_eq(r"\lambda = 2\Delta L / N", "measure wavelength by counting fringes", INTENSITY_COLOR, 42, 24),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=4.0)
        eqs.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(eqs, run_time=0.1))
        b = txt_block([
            "Michelson (1881): failed to detect the aether, led to special relativity.",
            "Modern use: LIGO uses 4 km arms to detect gravitational waves at 10^-21 m.",
            "Each half-wavelength of mirror travel = one complete fringe cycle.",
        ], 25)
        safe_scale(b, max_width=13.0)
        b.next_to(eqs, DOWN, buff=0.3)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(94.6)

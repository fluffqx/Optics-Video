# week6_interference.py  —  Weeks 5-6: Interference  (v2)
# Source: Bennett Ch. 7.1-7.3.5, 7.8
from manim import *
from utils import *


class Week6TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEKS 5–6",
            "Interference: Two-Beam, Young's, Thin Films & Michelson",
            "Bennett Ch. 7.1–7.3.5, 7.8"
        )
        self.play(FadeIn(card)); self.wait(2.5); self.play(FadeOut(card))


class InterferenceIntroScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Introduction to Interference  (Bennett Section 7.1)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Interference is the key phenomenon that proves light is a WAVE.",
            "It occurs when two or more coherent waves overlap in the same region of space.",
            "",
            "The principle of superposition gives us the total field: Ψ_total = Ψ₁ + Ψ₂",
            "The INTENSITY is what we measure: I ∝ |Ψ_total|²",
            "",
            "Bennett (Section 7.1) illustrates this with Figure 7.1 — two harmonic waves:",
            "When in phase (Δφ=0): amplitudes ADD → constructive interference → bright fringe",
            "When out of phase (Δφ=π): amplitudes CANCEL → destructive interference → dark fringe",
            "",
            "Key requirement: the two waves must be COHERENT —",
            "they must have a stable, well-defined phase relationship.",
            "Two separate light bulbs are incoherent (random phase fluctuations every ~10⁻⁸ s).",
            "Two slits illuminated by the same source are coherent (same source).",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.7)
        self.wait(2); self.play(FadeOut(VGroup(title, intro)))


class TwoBeamInterference(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Two-Beam Interference Formula  (Bennett Section 7.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Consider two monochromatic EM waves overlapping at a point P.",
            "Bennett derives the interference irradiance in Section 7.3.2 (Eq. 7.16):",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.3); self.play(FadeOut(intro))

        general = MathTex(
            r"I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\delta",
            font_size=56, color=INTENSITY_COLOR)
        general.next_to(title, DOWN, buff=0.5)
        self.play(Write(general)); self.wait(1.2)
        self.play(Create(gold_box(general))); self.wait(0.5)

        sym = eq_table([
            (r"I_1, I_2", "irradiances of the individual beams  [W/m²]", INTENSITY_COLOR),
            (r"\delta",   "phase difference between the two beams at point P  [rad]", WAVE_COLOR),
            (r"2\sqrt{I_1 I_2}\cos\delta", "interference term — the KEY new physics", GOLD),
        ], eq_fs=30, lbl_fs=24, buff=0.25)
        sym.next_to(general, DOWN, buff=0.4)
        for row in sym: self.play(FadeIn(row)); self.wait(0.7)
        self.wait(1); self.play(FadeOut(sym))

        # Phase difference definition
        phase_title = Text("Phase Difference δ  (Bennett Eq. 7.17):", font_size=28, color=GOLD)
        phase_title.next_to(general, DOWN, buff=0.45)
        self.play(Write(phase_title))

        delta_def = MathTex(
            r"\delta = \frac{2\pi}{\lambda_0}\times\text{OPD} + \Delta\varphi_{\text{refl}}",
            font_size=42, color=WAVE_COLOR)
        delta_def.next_to(phase_title, DOWN, buff=0.3)
        safe_scale(delta_def, max_width=13.0)
        self.play(Write(delta_def)); self.wait(1)

        opd_def = MathTex(
            r"\text{OPD} = n_2 d_2 - n_1 d_1 \quad\text{(optical path = refractive index × geometric path)}",
            font_size=30, color=WHITE)
        opd_def.next_to(delta_def, DOWN, buff=0.3)
        safe_scale(opd_def, max_width=13.0)
        self.play(Write(opd_def)); self.wait(1)

        refl_note = MathTex(
            r"\Delta\varphi_{\text{refl}} = \pi \text{ for each reflection where } n_{\text{reflected}} > n_{\text{incident}}",
            font_size=28, color=B_COLOR)
        refl_note.next_to(opd_def, DOWN, buff=0.3)
        safe_scale(refl_note, max_width=13.0)
        self.play(Write(refl_note)); self.wait(1.5)
        self.play(FadeOut(VGroup(phase_title, delta_def, opd_def, refl_note)))

        # Equal intensities
        eq_int_title = Text("Special Case: Equal Intensities  I₁ = I₂ = I₀:", font_size=28, color=GOLD)
        eq_int_title.next_to(general, DOWN, buff=0.45)
        self.play(Write(eq_int_title))

        equal_I = MathTex(
            r"I = 4I_0\cos^2\!\left(\frac{\delta}{2}\right)",
            font_size=56, color=INTENSITY_COLOR)
        equal_I.next_to(eq_int_title, DOWN, buff=0.3)
        self.play(Write(equal_I)); self.wait(1)

        cond_rows = eq_table([
            (r"\delta = 2m\pi \;\Rightarrow\; I = 4I_0",
             "CONSTRUCTIVE (maximum): δ=0, 2π, 4π, ...  intensity is 4× single beam!", E_COLOR),
            (r"\delta = (2m+1)\pi \;\Rightarrow\; I = 0",
             "DESTRUCTIVE (minimum): δ=π, 3π, 5π, ...  complete cancellation!", B_COLOR),
            (r"\text{Average: } \langle I\rangle = 2I_0",
             "averaged over space: energy is conserved — just redistributed", GOLD),
        ], eq_fs=28, lbl_fs=22, buff=0.25)
        cond_rows.next_to(equal_I, DOWN, buff=0.35)
        for row in cond_rows: self.play(FadeIn(row)); self.wait(0.8)
        self.wait(2); self.play(FadeOut(VGroup(title, general, eq_int_title, equal_I, cond_rows)))


class YoungDoubleSlit(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
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
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.3); self.play(FadeOut(intro))

        # Path difference
        path_title = Text("Path Difference and Phase Difference:", font_size=28, color=GOLD)
        path_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(path_title))

        path = MathTex(
            r"\Delta = r_2 - r_1 \approx d\sin\theta \approx \frac{dy}{L} \quad (L \gg d)",
            font_size=36, color=WAVE_COLOR)
        path.next_to(path_title, DOWN, buff=0.3)
        safe_scale(path, max_width=13.0)
        self.play(Write(path)); self.wait(0.8)

        phase = MathTex(
            r"\delta = \frac{2\pi}{\lambda}d\sin\theta = \frac{2\pi dy}{\lambda L}",
            font_size=44, color=WAVE_COLOR)
        phase.next_to(path, DOWN, buff=0.3)
        self.play(Write(phase)); self.wait(1)

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
        for f in fringes: self.play(Write(f), run_time=0.9); self.wait(0.6)
        self.play(Create(gold_box(fringe_spacing)))
        self.wait(1.5); self.play(FadeOut(VGroup(path_title, path, phase, fringes)))

        # Intensity pattern
        int_title = Text("Intensity Pattern  (Bennett Eq. 7.18):", font_size=28, color=GOLD)
        int_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(int_title))

        int_eq = MathTex(
            r"I(\theta) = 4I_0\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right)",
            font_size=44, color=INTENSITY_COLOR)
        int_eq.next_to(int_title, DOWN, buff=0.3)
        self.play(Write(int_eq)); self.wait(1.2)
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
        self.play(FadeOut(VGroup(title, ex_title, *solver.steps)))


class ThinFilmInterference(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Thin Film Interference  (Bennett Section 7.3.3)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "A thin transparent film (soap bubble, oil on water, AR coating)",
            "reflects light at BOTH surfaces. The two reflected beams interfere.",
            "",
            "The total phase difference has TWO contributions:",
            "1. PATH DIFFERENCE from the extra distance traveled inside the film.",
            "2. REFLECTION PHASE SHIFTS — π shift at each interface where n increases.",
            "",
            "CRITICAL RULE: +π phase shift (equivalent to +λ/2 extra path) occurs",
            "WHENEVER light reflects off a surface where n_reflected > n_incident.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(0.5); self.play(FadeOut(intro))

        # Main formula
        phi_title = Text("Total Phase Difference  (Bennett Eq. 7.26):", font_size=28, color=GOLD)
        phi_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(phi_title))

        phi_eq = MathTex(
            r"\Delta\varphi_{\text{total}} = \underbrace{\frac{4\pi n_f t\cos\theta_t}{\lambda_0}}_{\text{path difference}} + \underbrace{\Delta\varphi_{\text{refl}}}_{\text{reflection shifts}}",
            font_size=36, color=WAVE_COLOR)
        phi_eq.next_to(phi_title, DOWN, buff=0.3)
        safe_scale(phi_eq, max_width=13.0)
        self.play(Write(phi_eq)); self.wait(1.5)
        self.play(FadeOut(VGroup(phi_title, phi_eq)))

        # Case analysis
        cases = [
            ("Case 1: Film in Air  (n_air < n_film, same on both sides):",
             [("Top surface (air→film):", "+π shift  (n increases)", B_COLOR),
              ("Bottom surface (film→air):", "0 shift  (n decreases)", N_COLOR),
              ("Net Δφ_refl:", "π  →  net path shift of λ₀/2", WHITE)],
             [r"\text{Constructive (bright):} \quad 2n_f t\cos\theta_t = \left(m+\tfrac{1}{2}\right)\lambda_0",
              r"\text{Destructive (dark/AR):} \quad 2n_f t\cos\theta_t = m\lambda_0"],
             "Soap bubbles: bright rainbow colours come from thin film interference!"),
            ("Case 2: Air Gap Between Glass  (n_glass > n_air):",
             [("Top surface (glass→air):", "0 shift  (n decreases)", N_COLOR),
              ("Bottom surface (air→glass):", "+π shift  (n increases)", B_COLOR),
              ("Net Δφ_refl:", "π  →  same as Case 1", WHITE)],
             [r"\text{Constructive:} \quad 2n_{\text{air}}t\cos\theta_t = \left(m+\tfrac{1}{2}\right)\lambda_0",
              r"\text{Dark at t=0 } \Rightarrow \text{ dark spot at centre (Newton's rings!)}"],
             "Newton's rings: dark centre because both reflections give a π shift."),
        ]

        for case_name, reflect_rows, formula_strs, note_str in cases:
            c_title = Text(case_name, font_size=26, color=GOLD)
            c_title.next_to(title, DOWN, buff=0.5)
            safe_scale(c_title, max_width=13.5)
            self.play(Write(c_title))

            r_group = VGroup()
            for label, val, color in reflect_rows:
                l = Text(label, font_size=24, color=COMMENT_COLOR)
                v = Text(val, font_size=24, color=color)
                r_group.add(VGroup(l, v).arrange(RIGHT, buff=0.3))
            r_group.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
            r_group.next_to(c_title, DOWN, buff=0.3)
            for row in r_group: self.play(FadeIn(row)); self.wait(0.6)
            self.wait(0.5)

            f_group = VGroup()
            for fs in formula_strs:
                f_group.add(MathTex(fs, font_size=28, color=E_COLOR if "Constr" in fs else B_COLOR))
            f_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
            f_group.next_to(r_group, DOWN, buff=0.3)
            safe_scale(f_group, max_width=13.0)
            self.play(Write(f_group)); self.wait(1)

            note = Text(note_str, font_size=24, color=GOLD)
            note.next_to(f_group, DOWN, buff=0.25)
            safe_scale(note, max_width=13.5)
            self.play(FadeIn(note)); self.wait(1.5)
            self.play(FadeOut(VGroup(c_title, r_group, f_group, note)))

        # AR coating example
        ar_title = Text("Example: Anti-Reflection Coating  (Bennett Ex. 7.3):", font_size=28, color=GOLD)
        ar_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ar_title))

        ar_desc = section_intro([
            "MgF₂ (n_coat=1.38) on glass (n_glass=1.52), λ₀=550 nm.",
            "Camera lenses use AR coatings to reduce reflection losses from ~4% to ~0.1%.",
        ], font_size=26)
        ar_desc.next_to(ar_title, DOWN, buff=0.3)
        for l in ar_desc: self.play(FadeIn(l)); self.wait(0.8)

        solver = StepSolver(self, ar_desc, start_buff=0.35)
        solver.add_step(1,
            r"\text{Surface 1 (air\to MgF}_2\text{): }+\pi\text{ shift (n increases)}",
            "n_air=1.00 < n_MgF₂=1.38  →  π shift")
        solver.add_step(2,
            r"\text{Surface 2 (MgF}_2\to\text{glass}: }+\pi\text{ shift (n increases)}",
            "n_MgF₂=1.38 < n_glass=1.52  →  π shift")
        solver.add_step(3,
            r"\Delta\varphi_{\text{refl}} = \pi+\pi = 2\pi \equiv 0 \quad\text{(net: no relative shift)}",
            "both reflections shift by π → they CANCEL each other out")
        solver.add_step(4,
            r"\text{For destructive reflection: } 2n_{\text{coat}}t = \frac{\lambda_0}{2}"
            r"\;\Rightarrow\; t = \frac{\lambda_0}{4n_{\text{coat}}} = \frac{550}{4\times1.38} = 99.6\text{ nm}",
            "minimum thickness for AR at λ=550nm: about 100 nm — thinner than a virus!", GOLD)
        solver.finalize()
        self.play(FadeOut(VGroup(title, ar_title, ar_desc, *solver.steps)))


class FringeVisibility(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
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
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.3); self.play(FadeOut(intro))

        vis = MathTex(
            r"V = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}} = \frac{2\sqrt{I_1 I_2}}{I_1+I_2}",
            font_size=48, color=INTENSITY_COLOR)
        vis.next_to(title, DOWN, buff=0.5)
        self.play(Write(vis)); self.wait(1.2)
        self.play(Create(gold_box(vis))); self.wait(0.5)

        vis_rows = eq_table([
            (r"V = 1", "PERFECT visibility — I₁=I₂ and fully coherent (only possible for lasers)", GOLD),
            (r"V = \frac{2\sqrt{I_1 I_2}}{I_1+I_2} < 1", "when I₁ ≠ I₂: visibility < 1 even with coherent beams", WHITE),
            (r"V = 0", "no fringes — either completely incoherent or one beam is blocked", B_COLOR),
        ], eq_fs=30, lbl_fs=23, buff=0.28)
        vis_rows.next_to(vis, DOWN, buff=0.4)
        for row in vis_rows: self.play(FadeIn(row)); self.wait(0.8)
        self.wait(2); self.play(FadeOut(VGroup(title, vis, vis_rows)))


class MichelsonScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Michelson Interferometer  (Bennett Section 7.8)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "The Michelson interferometer (1881) is one of the most important",
            "instruments in the history of physics — it famously FAILED to detect",
            "the luminiferous aether, directly leading to special relativity.",
            "",
            "Setup: a beamsplitter splits the input beam into two arms.",
            "Each arm reflects off a mirror and returns to the beamsplitter.",
            "The two beams recombine and interfere on a screen or detector.",
            "Moving mirror M₂ by ΔL changes the OPD by 2ΔL (beam travels arm twice).",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(0.5); self.play(FadeOut(intro))

        eqs = eq_table([
            (r"\text{OPD} = 2\Delta L", "factor of 2: beam travels mirror arm twice (out and back)", WAVE_COLOR),
            (r"\delta = \frac{4\pi\Delta L}{\lambda}", "phase difference from mirror displacement ΔL", WAVE_COLOR),
            (r"\text{Bright central fringe: } \Delta L = \frac{m\lambda}{2}",
             "one fringe cycle per λ/2 of mirror travel", E_COLOR),
            (r"\text{Fringe count: } N = \frac{2\Delta L}{\lambda}",
             "count fringes to measure mirror displacement — used in precision metrology", GOLD),
            (r"\mathcal{R} = \frac{\lambda}{\Delta\lambda} = \frac{2L}{\lambda}",
             "resolving power: L = total mirror path length — can measure tiny λ differences", INTENSITY_COLOR),
        ], eq_fs=30, lbl_fs=22, buff=0.28)
        eqs.next_to(title, DOWN, buff=0.5)
        for row in eqs: self.play(FadeIn(row)); self.wait(0.8)
        self.wait(1.5); self.play(FadeOut(eqs))

        # Worked example
        ex_title = Text("Example: λ=589nm, mirror moves ΔL=0.500mm. How many fringes?", font_size=26, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        safe_scale(ex_title, max_width=13.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"N = \frac{2\Delta L}{\lambda} = \frac{2\times0.500\times10^{-3}}{589\times10^{-9}}",
            "fringe count formula")
        solver.add_step(2,
            r"= \frac{1.000\times10^{-3}}{589\times10^{-9}} = 1698 \text{ fringes}",
            "1698 fringes in 0.5 mm of mirror travel — very sensitive!", GOLD)
        solver.add_step(3,
            r"\text{If we count to 1 fringe: }\Delta L = \frac{\lambda}{2} = 294.5\text{ nm}",
            "resolution of ~295 nm per fringe — nanometre-scale position measurement!")
        solver.finalize()
        self.play(FadeOut(VGroup(title, ex_title, *solver.steps)))

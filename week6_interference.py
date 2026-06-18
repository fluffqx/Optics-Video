# week6_interference.py
# 31OPT Optics — Weeks 5-6: Interference
from manim import *
from utils import *


class Week6TitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "WEEKS 5-6",
            "Interference: Two-Beam, Thin Films, Young's & Michelson",
            "Bennett Ch. 7.3-7.3.5, 7.8"
        )
        self.play(FadeIn(card)); self.wait(2); self.play(FadeOut(card))


class InterferenceIntroScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Introduction to Interference", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        intro = section_intro([
            "Interference occurs when two (or more) coherent waves overlap.",
            "If the waves are in phase, they add (constructive → bright fringe).",
            "If out of phase by pi, they cancel (destructive → dark fringe).",
            "The key quantity is the PHASE DIFFERENCE delta between the two beams.",
            "Phase difference comes from optical path difference (OPD) and reflection phase shifts.",
            "Two types: wavefront splitting (Young's) and amplitude splitting (thin film, Michelson)."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.wait(1); self.play(FadeOut(VGroup(title, intro)))


class TwoBeamInterference(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Two-Beam Interference Formula", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        general = MathTex(
            r"I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\delta",
            font_size=50, color=INTENSITY_COLOR
        )
        self.play(Write(general)); self.wait(1.2)

        delta_def = MathTex(
            r"\delta = \frac{2\pi}{\lambda_0} \times \text{OPD}",
            font_size=44, color=WAVE_COLOR
        )
        delta_def.next_to(general, DOWN, buff=0.5)
        self.play(Write(delta_def)); self.wait(1.5)

        self.play(FadeOut(delta_def))
        equal_title = Text("For equal intensities  I_1 = I_2 = I_0:", font_size=30, color=WHITE)
        equal_title.next_to(general, DOWN, buff=0.4)
        self.play(Write(equal_title))

        equal_I = MathTex(
            r"I = 4I_0 \cos^2\!\left(\frac{\delta}{2}\right)",
            font_size=50, color=INTENSITY_COLOR
        )
        equal_I.next_to(equal_title, DOWN, buff=0.3)
        self.play(Write(equal_I)); self.wait(1)

        constructive = MathTex(
            r"\text{Constructive: } \delta = 2m\pi \Rightarrow I = 4I_0",
            font_size=32, color=E_COLOR)
        destructive  = MathTex(
            r"\text{Destructive: } \delta = (2m+1)\pi \Rightarrow I = 0",
            font_size=32, color=B_COLOR)
        cond_group = VGroup(constructive, destructive).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        cond_group.next_to(equal_I, DOWN, buff=0.4)
        self.play(Write(constructive)); self.wait(0.8)
        self.play(Write(destructive)); self.wait(1.5)

        self.play(FadeOut(VGroup(equal_title, equal_I, cond_group)))
        opd_title = Text("Optical Path Difference and Phase Difference:", font_size=30, color=GOLD)
        opd_title.next_to(general, DOWN, buff=0.5)
        self.play(Write(opd_title))

        opd          = MathTex(
            r"\text{OPD} = n_2 d_2 - n_1 d_1",
            font_size=34, color=WHITE)
        opd_to_delta = MathTex(
            r"\delta = \frac{2\pi}{\lambda_0} \times \text{OPD}",
            font_size=44, color=WAVE_COLOR)
        phase_shift  = MathTex(
            r"\text{Phase shift on reflection: } +\pi \text{ if going from low-}n\text{ to high-}n",
            font_size=28, color=B_COLOR)
        opd_group = VGroup(opd, opd_to_delta, phase_shift).arrange(DOWN, buff=0.35)
        opd_group.next_to(opd_title, DOWN, buff=0.3)
        for item in opd_group:
            self.play(Write(item) if isinstance(item, MathTex) else FadeIn(item)); self.wait(0.8)
        self.play(Create(gold_box(opd_to_delta)))
        self.wait(2); self.play(FadeOut(VGroup(title, general, opd_title, opd_group)))


class YoungDoubleSlit(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Young's Double-Slit Experiment", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Young's experiment proved that light is a wave.",
            "Two slits separated by d create two coherent sources.",
            "The path difference to a point on the screen determines constructive/destructive.",
            "Screen at distance L (>> d): small angle approximation applies."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        path_diff = MathTex(
            r"\Delta = r_2 - r_1 \approx d\sin\theta \approx \frac{dy}{L} \quad (L \gg d)",
            font_size=36, color=WAVE_COLOR)
        phase = MathTex(
            r"\delta = \frac{2\pi}{\lambda} d\sin\theta",
            font_size=44, color=WAVE_COLOR)
        bright = MathTex(
            r"\text{Bright fringes: } d\sin\theta = m\lambda,\quad m = 0, \pm 1, \pm 2, \ldots",
            font_size=34, color=E_COLOR)
        dark = MathTex(
            r"\text{Dark fringes: } d\sin\theta = \left(m+\tfrac{1}{2}\right)\lambda",
            font_size=34, color=B_COLOR)
        fringe_spacing = MathTex(
            r"\Delta y = \frac{\lambda L}{d} \quad \text{(fringe spacing on screen)}",
            font_size=44, color=GOLD)
        irradiance_pattern = MathTex(
            r"I(\theta) = 4I_0 \cos^2\!\left(\frac{\pi d \sin\theta}{\lambda}\right)",
            font_size=36, color=INTENSITY_COLOR)

        all_eqs = VGroup(path_diff, phase, bright, dark, fringe_spacing, irradiance_pattern)
        all_eqs.arrange(DOWN, aligned_edge=LEFT, buff=0.30)
        for eq in all_eqs:
            self.play(Write(eq), run_time=1.0); self.wait(0.7)
        self.play(Create(gold_box(fringe_spacing)))

        # Worked example
        self.play(FadeOut(all_eqs))
        ex_title = Text("Example: d=0.100 mm, L=1.50 m, lambda=500 nm. Find fringe spacing.",
                        font_size=26, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        s1 = MathTex(
            r"\Delta y = \frac{\lambda L}{d}"
            r" = \frac{500 \times 10^{-9} \times 1.50}{0.100 \times 10^{-3}}",
            font_size=34)
        s2 = MathTex(
            r"= \frac{7.50 \times 10^{-7}}{1.00 \times 10^{-4}}"
            r" = 7.50 \times 10^{-3} \text{ m} = 7.50 \text{ mm}",
            font_size=34, color=GOLD)
        steps = VGroup(s1, s2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(ex_title, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s)); self.wait(0.8)
        self.play(Create(gold_box(s2)))
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, steps)))


class ThinFilmInterference(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Thin Film Interference", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "A thin film (soap bubble, oil slick, coating) partially reflects at each surface.",
            "The two reflected beams interfere — their phase difference depends on film thickness.",
            "Two contributions: path difference AND reflection phase shifts.",
            "A pi shift occurs when reflecting off a denser medium (n_reflected > n_incident)."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        total_phase = MathTex(
            r"\Delta\varphi_{\text{total}} ="
            r" \underbrace{\frac{4\pi n_f t \cos\theta_t}{\lambda_0}}_{\text{path}}"
            r" + \underbrace{\Delta\varphi_{\text{refl}}}_{\text{reflection shifts}}",
            font_size=36, color=WAVE_COLOR)
        self.play(Write(total_phase)); self.wait(1.5)

        self.play(FadeOut(total_phase))
        case_title = Text("Case 1: Film in air (n_air < n_film on both sides):", font_size=28, color=GOLD)
        case_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(case_title))

        c1 = VGroup(
            MathTex(r"\text{Top surface (air to film): } +\pi \text{ shift}",  font_size=28, color=B_COLOR),
            MathTex(r"\text{Bottom surface (film to air): } 0 \text{ shift}", font_size=28, color=N_COLOR),
            MathTex(r"\text{Net reflection phase: } \Delta\varphi_{\text{refl}} = \pi", font_size=28, color=WHITE),
            MathTex(r"\text{Constructive: } 2n_f t\cos\theta_t = \left(m+\tfrac{1}{2}\right)\lambda_0",
                    font_size=28, color=E_COLOR),
            MathTex(r"\text{Destructive (anti-reflection): } 2n_f t\cos\theta_t = m\lambda_0",
                    font_size=28, color=B_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        c1.next_to(case_title, DOWN, buff=0.3)
        for item in c1:
            self.play(FadeIn(item)); self.wait(0.7)
        self.wait(1.5)

        # Newton's rings
        self.play(FadeOut(VGroup(case_title, c1)))
        newton_title = Text("Newton's Rings:", font_size=34, color=GOLD)
        newton_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(newton_title))

        gap          = MathTex(r"t(r) = \frac{r^2}{2R_{\text{lens}}} \quad \text{(air gap at radius }r\text{)}",
                               font_size=34, color=WHITE)
        dark_rings   = MathTex(r"r_m = \sqrt{m\lambda R_{\text{lens}}} \quad \text{(dark rings, reflected)}",
                               font_size=34, color=B_COLOR)
        bright_rings = MathTex(
            r"r_m = \sqrt{\left(m+\tfrac{1}{2}\right)\lambda R_{\text{lens}}} \quad \text{(bright rings)}",
            font_size=34, color=E_COLOR)
        newton_group = VGroup(gap, dark_rings, bright_rings).arrange(DOWN, buff=0.4)
        newton_group.next_to(newton_title, DOWN, buff=0.3)
        for item in newton_group:
            self.play(Write(item)); self.wait(0.8)

        # Anti-reflection coating example
        self.play(FadeOut(VGroup(newton_title, newton_group)))
        ar_title = Text("Example: AR coating. n_coat=1.22, n_glass=1.5, lambda=550 nm.",
                        font_size=24, color=GOLD)
        ar_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ar_title))

        ar1 = MathTex(
            r"\text{Both surfaces give }\pi\text{ shift }\Rightarrow\Delta\varphi_{\text{refl}}=0",
            font_size=28)
        ar2 = MathTex(
            r"\text{Need destructive reflection: } 2 n_{\text{coat}} t = \frac{\lambda_0}{2}",
            font_size=28)
        ar3 = MathTex(
            r"t = \frac{\lambda_0}{4 n_{\text{coat}}} = \frac{550}{4 \times 1.22} = 112.7 \text{ nm}",
            font_size=32, color=GOLD)
        ar_steps = VGroup(ar1, ar2, ar3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ar_steps.next_to(ar_title, DOWN, buff=0.3)
        for s in ar_steps:
            self.play(Write(s)); self.wait(0.8)
        self.play(Create(gold_box(ar3)))

        # Fringe visibility
        self.play(FadeOut(VGroup(ar_title, ar_steps)))
        vis_title = Text("Fringe Visibility:", font_size=32, color=GOLD)
        vis_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(vis_title))

        vis_eq = MathTex(
            r"V = \frac{I_{\max} - I_{\min}}{I_{\max} + I_{\min}}"
            r" = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2}",
            font_size=44, color=INTENSITY_COLOR)
        vis_note = MathTex(
            r"V=1 \text{ (perfect coherence)},\quad V=0 \text{ (incoherent, no fringes)}",
            font_size=28, color=WHITE)
        vis_group = VGroup(vis_eq, vis_note).arrange(DOWN, buff=0.35)
        vis_group.next_to(vis_title, DOWN, buff=0.3)
        self.play(Write(vis_group))
        self.wait(2); self.play(FadeOut(VGroup(title, vis_title, vis_group)))


class MichelsonScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Michelson Interferometer", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "The Michelson interferometer splits a beam into two arms with a beamsplitter.",
            "Each arm reflects off a mirror; the two beams recombine and interfere.",
            "Moving one mirror by DeltaL changes the OPD by 2*DeltaL.",
            "One full fringe cycle (dark to bright to dark) per lambda/2 of mirror travel.",
            "Used to measure wavelengths, distances, and refractive indices to extreme precision."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        opd_m    = MathTex(
            r"\text{OPD} = 2\Delta L \quad \text{(factor 2: beam travels arm twice)}",
            font_size=36, color=WAVE_COLOR)
        phase_m  = MathTex(
            r"\delta = \frac{4\pi \Delta L}{\lambda}",
            font_size=44, color=WAVE_COLOR)
        bright_m = MathTex(
            r"\text{Bright central fringe: } \Delta L = \frac{m\lambda}{2}",
            font_size=34, color=E_COLOR)
        cycle_m  = MathTex(
            r"\text{One fringe cycle per } \frac{\lambda}{2} \text{ of mirror travel}",
            font_size=32, color=WHITE)
        resolving_m = MathTex(
            r"\mathcal{R} = \frac{\lambda}{\Delta\lambda} = \frac{2L}{\lambda}"
            r"\quad \text{(}L\text{ = total mirror travel)}",
            font_size=34, color=INTENSITY_COLOR)
        all_eqs = VGroup(opd_m, phase_m, bright_m, cycle_m, resolving_m).arrange(DOWN, buff=0.38)
        for eq in all_eqs:
            self.play(Write(eq), run_time=1.0); self.wait(0.7)
        self.play(Create(gold_box(resolving_m)))

        # Worked example
        self.play(FadeOut(all_eqs))
        ex_title = Text("Example: lambda=589 nm. Mirror moved 0.5 mm. How many fringes?",
                        font_size=26, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))
        s1 = MathTex(
            r"N = \frac{2\Delta L}{\lambda}"
            r" = \frac{2 \times 0.5 \times 10^{-3}}{589 \times 10^{-9}}"
            r" = \frac{10^{-3}}{5.89\times10^{-7}} = 1698 \text{ fringes}",
            font_size=30, color=GOLD)
        s1.next_to(ex_title, DOWN, buff=0.3)
        self.play(Write(s1)); self.play(Create(gold_box(s1)))
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, s1)))

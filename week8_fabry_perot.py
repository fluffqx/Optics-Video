# week8_fabry_perot.py
# 31OPT Optics — Week 8: Multi-Beam Interference: Fabry-Pérot & Coherence
from manim import *
from utils import *


class Week8TitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "WEEK 8",
            "Multi-Beam Interference: Fabry-Perot & Coherence",
            "Bennett Ch. 7.10, 7.12"
        )
        self.play(FadeIn(card)); self.wait(2); self.play(FadeOut(card))


class FabryPerotScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Fabry-Perot Interferometer", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Two parallel, highly reflective mirrors form a resonant cavity.",
            "Light bounces many times between the mirrors — MULTI-beam interference.",
            "Transmission is sharply peaked at resonance wavelengths.",
            "Used for high-resolution spectroscopy, laser cavities, and filters.",
            "The sharpness of transmission peaks is quantified by the Finesse F-script."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        # Airy transmission function
        trans = MathTex(
            r"I_t = \frac{I_0}{1 + F\sin^2\!\left(\dfrac{\delta}{2}\right)}",
            font_size=52, color=INTENSITY_COLOR)
        self.play(Write(trans)); self.wait(1.2)

        delta_fp = MathTex(
            r"\delta = \frac{4\pi n d \cos\theta}{\lambda_0}"
            r" \quad \text{(round-trip phase, }d\text{ = mirror separation)}",
            font_size=32, color=WAVE_COLOR)
        delta_fp.next_to(trans, DOWN, buff=0.4)
        self.play(Write(delta_fp)); self.wait(1)

        F_eq = MathTex(
            r"F = \frac{4R}{(1-R)^2}"
            r" \quad \text{(coefficient of finesse, }R\text{ = mirror reflectivity)}",
            font_size=34, color=N_COLOR)
        F_eq.next_to(delta_fp, DOWN, buff=0.4)
        self.play(Write(F_eq)); self.wait(1.5)

        # Finesse
        self.play(FadeOut(VGroup(trans, delta_fp, F_eq)))
        finesse_title = Text("Finesse F-script  (different from F!):", font_size=30, color=GOLD)
        finesse_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(finesse_title))

        finesse_eq = MathTex(
            r"\mathcal{F} = \frac{\pi\sqrt{R}}{1-R} = \frac{\pi}{2}\sqrt{F}",
            font_size=44, color=N_COLOR)
        finesse_meaning = Text(
            "F-script = ratio of free spectral range to FWHM of transmission peak.",
            font_size=26, color=WHITE)
        finesse_group = VGroup(finesse_eq, finesse_meaning).arrange(DOWN, buff=0.3)
        finesse_group.next_to(finesse_title, DOWN, buff=0.3)
        self.play(Write(finesse_group)); self.wait(1.5)

        # Resolving power and FSR
        self.play(FadeOut(VGroup(finesse_title, finesse_group)))
        res_title = Text("Resolving Power & Free Spectral Range:", font_size=30, color=GOLD)
        res_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(res_title))

        resolving      = MathTex(
            r"\mathcal{R} = \frac{\lambda}{\Delta\lambda} = m \cdot \mathcal{F}",
            font_size=48, color=INTENSITY_COLOR)
        resolving_note = MathTex(
            r"m = \frac{2nd}{\lambda} \quad \text{(number of half-wavelengths in cavity)}",
            font_size=32, color=WHITE)
        fsr_lambda     = MathTex(
            r"\Delta\lambda_{\text{FSR}} = \frac{\lambda_0^2}{2nd}",
            font_size=40, color=WAVE_COLOR)
        fsr_freq       = MathTex(
            r"\Delta\nu_{\text{FSR}} = \frac{c}{2nd}",
            font_size=40, color=WAVE_COLOR)
        res_group = VGroup(resolving, resolving_note, fsr_lambda, fsr_freq).arrange(DOWN, buff=0.38)
        res_group.next_to(res_title, DOWN, buff=0.3)
        for item in res_group:
            self.play(Write(item), run_time=1.0); self.wait(0.7)
        self.play(Create(gold_box(VGroup(resolving, fsr_lambda, fsr_freq))))

        # Big worked example
        self.play(FadeOut(VGroup(res_title, res_group)))
        ex_title = Text(
            "Full Example: R=0.95, d=10 cm (air), lambda=632.8 nm.",
            font_size=26, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        s1 = MathTex(
            r"F = \frac{4R}{(1-R)^2} = \frac{4\times0.95}{(0.05)^2}"
            r" = \frac{3.8}{0.0025} = 1520",
            font_size=28, color=N_COLOR)
        s2 = MathTex(
            r"\mathcal{F} = \frac{\pi\sqrt{R}}{1-R}"
            r" = \frac{\pi \times 0.9747}{0.05} = 61.3",
            font_size=28, color=N_COLOR)
        s3 = MathTex(
            r"m = \frac{2\times1.0\times0.10}{632.8\times10^{-9}} = 3.16\times10^5",
            font_size=28)
        s4 = MathTex(
            r"\mathcal{R} = m\mathcal{F} = 3.16\times10^5 \times 61.3 = 1.94\times10^7",
            font_size=28, color=INTENSITY_COLOR)
        s5 = MathTex(
            r"\Delta\lambda_{\text{FSR}} = \frac{(632.8)^2}{2\times10^8\text{ nm}}"
            r" = 0.002 \text{ nm}",
            font_size=28, color=WAVE_COLOR)
        steps = VGroup(s1, s2, s3, s4, s5).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        steps.next_to(ex_title, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s), run_time=1.0); self.wait(0.6)
        self.play(Create(gold_box(VGroup(s4, s5))))
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, steps)))


class CoherenceScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Coherence", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Coherence is what determines whether interference fringes are visible.",
            "Temporal coherence: related to the spectral purity (bandwidth) of the source.",
            "Spatial coherence: related to the spatial extent of the source.",
            "Perfect coherence → V=1.   Zero coherence → V=0 (no fringes).",
            "Lasers have high coherence; thermal sources have low coherence."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        temp_title = Text("Temporal Coherence:", font_size=30, color=GOLD)
        temp_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(temp_title))

        coh_time = MathTex(
            r"\tau_c \approx \frac{1}{\Delta\nu} = \frac{\lambda^2}{c\,\Delta\lambda}",
            font_size=40, color=WAVE_COLOR)
        coh_len  = MathTex(
            r"l_c = c\,\tau_c = \frac{\lambda^2}{\Delta\lambda}",
            font_size=40, color=WAVE_COLOR)
        temp_group = VGroup(coh_time, coh_len).arrange(RIGHT, buff=1.0)
        temp_group.next_to(temp_title, DOWN, buff=0.3)
        self.play(Write(temp_group)); self.wait(1.5)

        spat_title = Text("Spatial Coherence:", font_size=30, color=GOLD)
        spat_title.next_to(temp_group, DOWN, buff=0.5)
        self.play(Write(spat_title))

        spat = MathTex(
            r"d \leq l_{\text{spatial}} = \frac{1.22\lambda L}{D_{\text{source}}}",
            font_size=38, color=WAVE_COLOR)
        spat_note = Text(
            "Fringes visible only if slit separation d ≤ spatial coherence length.",
            font_size=26, color=WHITE)
        spat_group = VGroup(spat, spat_note).arrange(DOWN, buff=0.2)
        spat_group.next_to(spat_title, DOWN, buff=0.3)
        self.play(Write(spat_group))

        # Example: coherence length of HeNe laser
        self.play(FadeOut(VGroup(temp_group, spat_group)))
        ex_title = Text(
            "Example: HeNe laser lambda=632.8 nm, linewidth Delta_lambda=0.001 nm.",
            font_size=26, color=GOLD)
        ex_title.next_to(temp_title, DOWN, buff=0.5)
        self.play(Write(ex_title))
        s1 = MathTex(
            r"l_c = \frac{\lambda^2}{\Delta\lambda}"
            r" = \frac{(632.8\times10^{-9})^2}{0.001\times10^{-9}}"
            r" = \frac{4.00\times10^{-13}}{10^{-12}}"
            r" = 0.40 \text{ m}",
            font_size=28, color=GOLD)
        s1.next_to(ex_title, DOWN, buff=0.3)
        self.play(Write(s1)); self.play(Create(gold_box(s1)))
        self.wait(2)
        self.play(FadeOut(VGroup(title, temp_title, spat_title, ex_title, s1)))

# week8_fabry_perot.py  —  Week 8: Fabry-Pérot Interferometer  (v2)
# Source: Bennett Ch. 7.10, 7.11
from manim import *
from utils import *


class Week8TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEK 8",
            "Multiple-Beam Interference & Fabry-Pérot",
            "Bennett Ch. 7.10, 7.11"
        )
        self.play(FadeIn(card)); self.wait(162.3); self.play(FadeOut(card))


class MultiBeamIntro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("From Two Beams to Multiple Beams  (Bennett Section 7.10)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "In Young's experiment and the Michelson interferometer, exactly TWO beams",
            "interfere. The Fabry-Pérot uses an INFINITE SERIES of beams.",
            "",
            "Setup: two parallel, flat, partially-reflecting mirrors with reflectance R.",
            "A beam enters and bounces back and forth between the two mirrors.",
            "At each bounce, a fraction T is transmitted out.",
            "The series of transmitted beams are: Et₁, Et₂=r²Et₁·e^{iδ}, Et₃=r⁴Et₁·e^{i2δ}, ...",
            "",
            "Bennett Section 7.10 sums this infinite geometric series (Eq. 7.85).",
            "The result is the AIRY FUNCTION — one of the most important results in optics.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(100.6); self.play(FadeOut(VGroup(title, intro)))


class AiryFunction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Summing the infinite series of transmitted beams gives the Airy function:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro[0])); self.wait(0.8); self.play(FadeOut(intro))

        airy = MathTex(
            r"I_t = \frac{I_0}{1 + F\sin^2\!\left(\frac{\delta}{2}\right)}",
            font_size=64, color=INTENSITY_COLOR)
        airy.next_to(title, DOWN, buff=0.5)
        self.play(Write(airy)); self.wait(1.5)
        self.play(Create(gold_box(airy))); self.wait(0.5)

        sym = eq_table([
            (r"I_0", "incident irradiance  [W/m²]", INTENSITY_COLOR),
            (r"F = \frac{4R}{(1-R)^2}", "coefficient of finesse — depends only on mirror reflectivity R", GOLD),
            (r"\delta = \frac{4\pi nd\cos\theta}{\lambda_0} + \delta_{\text{refl}}",
             "round-trip phase: 2× the path inside cavity + reflection phase shifts", WAVE_COLOR),
            (r"R", "mirror reflectivity (same for both mirrors)", N_COLOR),
        ], eq_fs=30, lbl_fs=23, buff=0.25)
        sym.next_to(airy, DOWN, buff=0.4)
        for row in sym: self.play(FadeIn(row)); self.wait(0.7)
        self.wait(1.5); self.play(FadeOut(sym))

        # Resonance condition
        res_title = Text("Resonance Condition — Peak Transmission:", font_size=28, color=GOLD)
        res_title.next_to(airy, DOWN, buff=0.4)
        self.play(Write(res_title))

        res = section_intro([
            "When δ/2 = Nπ (i.e. δ = 2Nπ): sin²(δ/2) = 0  →  I_t = I₀",
            "100% transmission even with highly reflective mirrors!",
            "This happens when the round-trip phase is a multiple of 2π.",
            "Physical picture: all the multiply-reflected beams add up constructively.",
            "The field builds up inside the cavity to a very large amplitude.",
        ], font_size=26)
        res.next_to(res_title, DOWN, buff=0.3)
        for l in res: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(95.9); self.play(FadeOut(VGroup(title, airy, res_title, res)))


class FinesseResolving(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Finesse, Resolving Power & Free Spectral Range", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "The finesse (script F) characterises the sharpness of the transmission peaks.",
            "It is defined as the ratio of the free spectral range to the peak FWHM.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.9)
        self.wait(0.3); self.play(FadeOut(intro))

        eqs = eq_table([
            (r"\mathcal{F} = \frac{\pi\sqrt{R}}{1-R} = \frac{\pi\sqrt{F}}{2}",
             "FINESSE: ratio of FSR to FWHM of transmission peak  (Bennett Eq. 7.91)", GOLD),
            (r"F = \frac{4R}{(1-R)^2} = \frac{4\mathcal{F}^2}{\pi^2}",
             "coefficient of finesse F vs. finesse script-F (different quantities!)", N_COLOR),
            (r"N = \frac{2nd\cos\theta}{\lambda/2} = \frac{2nd}{\lambda_0}\cos\theta",
             "order number N = number of half-wavelengths in the cavity", WHITE),
            (r"\text{RP} = \frac{\lambda}{\Delta\lambda} = N\mathcal{F}",
             "RESOLVING POWER: product of order number and finesse  (Bennett Eq. 7.93)", GOLD),
            (r"\Delta\lambda_{\text{FSR}} = \frac{\lambda^2}{2nd} = \frac{\lambda_0}{N}",
             "FREE SPECTRAL RANGE in wavelength  (Bennett Eq. 7.94)", INTENSITY_COLOR),
            (r"\Delta\nu_{\text{FSR}} = \frac{c}{2nd}",
             "FREE SPECTRAL RANGE in frequency — cavity mode spacing", INTENSITY_COLOR),
        ], eq_fs=30, lbl_fs=22, buff=0.28)
        eqs.next_to(title, DOWN, buff=0.5)
        for row in eqs: self.play(FadeIn(row)); self.wait(0.7)
        self.wait(1.5); self.play(FadeOut(eqs))

        # Physical interpretations
        phys_title = Text("Physical Interpretation of Finesse:", font_size=30, color=GOLD)
        phys_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(phys_title))

        phys = section_intro([
            "Script-F is the number of times a photon bounces back and forth before leaking out.",
            "High finesse → very sharp transmission peaks → high spectral resolution.",
            "High finesse also means: large field buildup inside the cavity — important for lasers.",
            "For R=99%: F = 4×0.99/(0.01)² = 39600, finesse = π√39600/2 ≈ 312.",
            "The peaks are 312× narrower than the spacing between them!",
        ], font_size=26)
        phys.next_to(phys_title, DOWN, buff=0.35)
        for l in phys: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(115.1); self.play(FadeOut(VGroup(title, phys_title, phys)))


class FabryPerotExample(Scene):
    """Full Fabry-Perot example — Bennett Example 7.11"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Example: Resolving H and D Hα Lines  (Bennett Ex. 7.11)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        prob = section_intro([
            "Hydrogen Hα: λ₁ = 656.28 nm.  Deuterium Hα: λ₂ = 656.10 nm.",
            "Splitting: Δλ = 0.18 nm.  Fabry-Pérot mirrors: R = 90%.",
            "Find: required mirror spacing, finesse, resolving power, and verify resolution.",
        ], font_size=27)
        prob.next_to(title, DOWN, buff=0.4)
        for l in prob: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(100.6)

        solver = StepSolver(self, prob, start_buff=0.4)
        solver.add_step(1,
            r"F = \frac{4R}{(1-R)^2} = \frac{4\times0.90}{(0.10)^2} = \frac{3.6}{0.01} = 360",
            "coefficient of finesse for R=90%")
        solver.add_step(2,
            r"\mathcal{F} = \frac{\pi\sqrt{F}}{2} = \frac{\pi\sqrt{360}}{2} = \frac{\pi\times18.97}{2} = 29.8",
            "finesse: transmission peaks are 29.8× narrower than the FSR", GOLD)
        solver.add_step(3,
            r"\Delta\lambda_{\text{FSR}} = 0.5\text{ nm} \quad\Rightarrow\quad d = \frac{\lambda^2}{2\Delta\lambda_{\text{FSR}}} = \frac{(656.2)^2}{2\times0.5\times10^6}\text{ nm} = 0.431\text{ mm}",
            "choose FSR=0.5nm to bracket the splitting; find required mirror spacing")
        solver.add_step(4,
            r"N = \frac{2nd}{\lambda} = \frac{2\times1\times0.431\times10^6}{656.2} = 1313",
            "order number (n=1 for air, d=0.431mm)")
        solver.add_step(5,
            r"\text{RP} = N\mathcal{F} = 1313\times29.8 = 39100",
            "resolving power of this configuration", GOLD)
        solver.add_step(6,
            r"\Delta\lambda_{\min} = \frac{\lambda}{\text{RP}} = \frac{656.2}{39100} = 0.0168\text{ nm}",
            "minimum resolvable Δλ = 0.017nm  <<  actual splitting 0.18nm  ✓", GOLD)
        solver.add_step(7,
            r"\text{Compare to grating: RP}=Nm=30000\times1=30000 \quad (\text{same grating as before})",
            "Fabry-Pérot gives higher RP than the 5cm grating — in a much more compact package!")
        solver.finalize())


class CoherenceLength(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Coherence & the Fabry-Pérot  (Bennett Section 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "A Fabry-Pérot interferometer only works if the light source has sufficient",
            "TEMPORAL COHERENCE — the coherence length must exceed the cavity round trip.",
            "",
            "Temporal coherence is related to the spectral purity of the source.",
            "A narrow spectral linewidth Δν corresponds to a long coherence length l_c.",
            "Intuitively: a perfectly monochromatic wave (Δν=0) has infinite coherence length",
            "— it is coherent with a copy of itself no matter how much you delay it.",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        for l in intro: self.play(FadeIn(l)); self.wait(0.8)
        self.wait(0.5); self.play(FadeOut(intro))

        coh_eqs = eq_table([
            (r"l_c = \frac{c}{\Delta\nu} = \frac{\lambda^2}{\Delta\lambda}",
             "coherence length [m]: related to spectral linewidth", WAVE_COLOR),
            (r"\tau_c = \frac{l_c}{c} = \frac{1}{\Delta\nu}",
             "coherence TIME [s]: how long the wave stays predictable", WAVE_COLOR),
            (r"\text{Fabry-Pérot requires: } 2nd < l_c",
             "cavity round trip must be less than coherence length for fringes to appear", GOLD),
        ], eq_fs=34, lbl_fs=24, buff=0.3)
        coh_eqs.next_to(title, DOWN, buff=0.5)
        for row in coh_eqs: self.play(FadeIn(row)); self.wait(0.8)
        self.wait(1.5); self.play(FadeOut(coh_eqs))

        # Source comparison
        sources_title = Text("Coherence Length of Different Sources:", font_size=28, color=GOLD)
        sources_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(sources_title))

        sources = [
            ("Thermal light (white light)", "Δλ≈300nm", r"l_c \approx \frac{(550)^2}{300}\approx 1.0\;\mu\text{m}", "too short for most interferometers"),
            ("Sodium lamp (D lines)", "Δλ≈0.6nm", r"l_c \approx \frac{(589)^2}{0.6}\approx 0.58\;\text{mm}", "a few mm of mirror spacing"),
            ("Filtered spectral lamp", "Δλ≈0.01nm", r"l_c \approx 3.5\;\text{cm}", "useful for compact FP"),
            ("Stabilised He-Ne laser", "Δν≈1MHz", r"l_c = c/\Delta\nu \approx 300\;\text{m}", "long coherence: ideal for FP"),
            ("Ultra-stable ECDL laser", "Δν≈1kHz", r"l_c \approx 3\times10^5\;\text{m} = 300\;\text{km}", "extraordinary — used in gravitational wave detectors"),
        ]

        for src_name, linewidth, lc_calc, note in sources:
            row_mob = VGroup(
                Text(src_name+":", font_size=23, color=GOLD),
                Text(linewidth, font_size=23, color=WHITE),
                MathTex(lc_calc, font_size=26, color=WAVE_COLOR),
                Text("→ "+note, font_size=22, color=COMMENT_COLOR),
            ).arrange(RIGHT, buff=0.3)
            safe_scale(row_mob, max_width=13.5)
            row_mob.next_to(sources_title, DOWN, buff=0.35)
            self.play(FadeIn(row_mob)); self.wait(89.7); self.play(FadeOut(row_mob)))


class Week8Summary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Week 8 — Complete Formula Summary", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        rows = eq_table([
            (r"I_t = \frac{I_0}{1+F\sin^2(\delta/2)}", "Airy function (Fabry-Pérot transmission)", INTENSITY_COLOR),
            (r"F = \frac{4R}{(1-R)^2}", "coefficient of finesse", N_COLOR),
            (r"\mathcal{F} = \frac{\pi\sqrt{R}}{1-R}", "finesse", GOLD),
            (r"\delta = \frac{4\pi nd}{\lambda_0}\cos\theta", "round-trip phase (at oblique angle θ)", WAVE_COLOR),
            (r"N = \frac{2nd}{\lambda_0}", "order number (at normal incidence)", WHITE),
            (r"\text{RP} = N\mathcal{F}", "resolving power", GOLD),
            (r"\Delta\lambda_{\text{FSR}} = \lambda_0/N", "free spectral range (wavelength)", INTENSITY_COLOR),
            (r"\Delta\nu_{\text{FSR}} = c/(2nd)", "free spectral range (frequency)", INTENSITY_COLOR),
            (r"l_c = \lambda^2/\Delta\lambda = c/\Delta\nu", "coherence length of light source", WAVE_COLOR),
        ], eq_fs=30, lbl_fs=22, buff=0.22)
        rows.next_to(title, DOWN, buff=0.4)
        for row in rows: self.play(FadeIn(row)); self.wait(0.5)
        self.wait(78.0); self.play(FadeOut(VGroup(title, rows)))

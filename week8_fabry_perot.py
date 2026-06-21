# week8_fabry_perot.py  —  Week 8: Fabry-Pérot Interferometer  (v2)
# Source: Bennett Ch. 7.10, 7.11
from manim import *
from utils import *


class Week8TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/Week8TitleCard.mp3", time_offset=0)
        card = make_title_card(
            "WEEK 8",
            "Multiple-Beam Interference & Fabry-Pérot",
            "Bennett Ch. 7.10, 7.11"
        )
        self.play(FadeIn(card)); self.wait(155.5); self.play(FadeOut(card))


class MultiBeamIntro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/MultiBeamIntro.mp3", time_offset=0)
        title = Text("From Two Beams to Multiple Beams  (Bennett 7.10)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b1 = txt_block([
            "Young's and Michelson use exactly TWO beams — limited resolving power.",
            "Fabry-Perot: light bounces back and forth between two parallel mirrors.",
            "Each bounce produces another transmitted/reflected beam — INFINITE series.",
            "All these beams interfere, giving a much sharper transmission peak.",
        ])
        safe_scale(b1, max_width=13.0, max_height=3.5)
        b1.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b1, run_time=0.1))
        self.wait(35)
        self.play(FadeOut(b1))
        b2 = txt_block([
            "Setup: two flat mirrors of reflectivity R, separated by gap d, medium n.",
            "Beam enters, bounces N times. Each round trip adds phase delta = 4*pi*n*d/lambda.",
            "Transmitted amplitudes form a geometric series — can be summed analytically.",
            "Result: the Airy function  I_t = I_0 / [1 + F sin^2(delta/2)].",
        ])
        safe_scale(b2, max_width=13.0, max_height=3.5)
        b2.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b2, run_time=0.1))
        self.wait(97.4)

class AiryFunction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/AiryFunction.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        airy = MathTex(r"I_t = \frac{I_0}{1 + F\sin^2(\delta/2)}\qquad F = \frac{4R}{(1-R)^2}",
                       font_size=46, color=INTENSITY_COLOR)
        safe_scale(airy)
        airy.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(airy, run_time=0.1))
        self.play(Create(gold_box(airy)))
        b = txt_block([
            "At resonance: delta = 2*N*pi -> sin^2(delta/2) = 0 -> I_t = I_0.  100% transmission!",
            "Off resonance: I_t << I_0 for large F (high R mirrors).",
            "F = 4R/(1-R)^2 is the COEFFICIENT OF FINESSE (NOT the finesse script-F).",
            "High R (e.g. R=0.99): F = 39600 — extremely sharp peaks.",
        ])
        safe_scale(b, max_width=13.0, max_height=3.0)
        b.next_to(airy, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(101.8)

class FinesseResolving(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/FinesseResolving.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"\mathcal{F} = \frac{\pi\sqrt{R}}{1-R}", "FINESSE (script F) = FSR / FWHM", GOLD, 42, 24),
            labeled_eq(r"N = 2nd/\lambda_0", "ORDER NUMBER at resonance", WHITE, 42, 24),
            labeled_eq(r"\text{RP} = N\mathcal{F}", "RESOLVING POWER", INTENSITY_COLOR, 42, 24),
            labeled_eq(r"\Delta\lambda_{\rm FSR} = \lambda_0^2/(2nd)", "FREE SPECTRAL RANGE", WAVE_COLOR, 42, 24),
            labeled_eq(r"\Delta\nu_{\rm FSR} = c/(2nd)", "FSR in frequency", WAVE_COLOR, 42, 24),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0, max_height=4.8)
        eqs.next_to(title, DOWN, buff=0.35)
        self.play(FadeIn(eqs, run_time=0.1))
        self.wait(117.6)

class FabryPerotExample(Scene):
    """Full Fabry-Perot example — Bennett Example 7.11"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/FabryPerotExample.mp3", time_offset=0)
        title = Text("Example: Resolving H and D Hα Lines  (Bennett Ex. 7.11)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        prob = section_intro([
            "Hydrogen Hα: λ₁ = 656.28 nm.  Deuterium Hα: λ₂ = 656.10 nm.",
            "Splitting: Δλ = 0.18 nm.  Fabry-Pérot mirrors: R = 90%.",
            "Find: required mirror spacing, finesse, resolving power, and verify resolution.",
        ], font_size=27)
        prob.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(prob))
        self.wait(10.2)
        self.wait(97.4)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

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
        solver.finalize()


class CoherenceLength(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/CoherenceLength.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"l_c = \lambda^2/\Delta\lambda = c/\Delta\nu", "COHERENCE LENGTH", GOLD, 44, 24),
            labeled_eq(r"\tau_c = l_c/c = 1/\Delta\nu", "COHERENCE TIME", WHITE, 44, 24),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(eqs, max_width=13.0)
        eqs.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(eqs, run_time=0.1))
        table = eq_table([
            (r"\text{White light}", "Delta_lambda~300nm -> l_c~1 micron", WHITE),
            (r"\text{Sodium lamp}", "Delta_lambda~0.001nm -> l_c~0.6mm", WAVE_COLOR),
            (r"\text{He-Ne laser}", "Delta_nu~1MHz -> l_c~300m", E_COLOR),
            (r"\text{LIGO laser}", "Delta_nu~1Hz -> l_c~300 000 km", GOLD),
        ], eq_fs=24, lbl_fs=20, buff=0.18)
        safe_scale(table, max_width=13.0, max_height=3.0)
        table.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(table, run_time=0.1))
        self.wait(93.1)

class Week8Summary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/Week8Summary.mp3", time_offset=0)
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
        for row in rows: self.play(FadeIn(row)); self.wait(3.9)
        self.wait(75.4); self.play(FadeOut(VGroup(title, rows)))

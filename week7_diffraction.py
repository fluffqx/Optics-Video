# week7_diffraction.py
# 31OPT Optics — Week 7: Fraunhofer Diffraction
from manim import *
from utils import *


class Week7TitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "WEEK 7",
            "Fraunhofer Diffraction: Slits, Circular Aperture & Gratings",
            "Bennett Ch. 8.1-8.3.8"
        )
        self.play(FadeIn(card)); self.wait(2); self.play(FadeOut(card))


class DiffractionIntroScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Introduction to Diffraction", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        intro = section_intro([
            "Diffraction is the bending and spreading of waves around obstacles and apertures.",
            "Huygens' principle: every point on a wavefront acts as a new point source.",
            "Fraunhofer (far-field): both source and observation point far from aperture.",
            "Condition: lambda >> h^2/(2r), where h is aperture size and r is distance.",
            "Babinet's principle: aperture + complement give the same diffraction pattern.",
            "Key result: smaller aperture → wider diffraction pattern."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)

        fraunhofer_cond = MathTex(
            r"\text{Fraunhofer condition: } \lambda \gg \frac{h^2}{2r}"
            r"\quad \Leftrightarrow \quad r \gg \frac{h^2}{\lambda}",
            font_size=34, color=GOLD)
        fraunhofer_cond.next_to(intro, DOWN, buff=0.4)
        self.play(Write(fraunhofer_cond)); self.wait(2)
        self.play(FadeOut(VGroup(title, intro, fraunhofer_cond)))


class SingleSlitScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Single-Slit Fraunhofer Diffraction", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "A single slit of width b creates a diffraction pattern.",
            "The pattern is a sinc-squared function of angle theta.",
            "Central maximum is twice as wide as the secondary maxima.",
            "Dark fringes (minima) occur at integer multiples of lambda/b."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        I_eq = MathTex(
            r"I(\theta) = I_0 \left(\frac{\sin\beta}{\beta}\right)^2",
            font_size=52, color=INTENSITY_COLOR)
        self.play(Write(I_eq)); self.wait(1)

        beta_def = MathTex(
            r"\beta \equiv \frac{1}{2} k b \sin\theta = \frac{\pi b \sin\theta}{\lambda}",
            font_size=40, color=WAVE_COLOR)
        b_label  = MathTex(r"b = \text{slit width}", font_size=32, color=WHITE)
        beta_group = VGroup(beta_def, b_label).arrange(DOWN, buff=0.2)
        beta_group.next_to(I_eq, DOWN, buff=0.4)
        self.play(Write(beta_group)); self.wait(1.5)

        self.play(FadeOut(beta_group))
        results = VGroup(
            MathTex(r"\text{Central max: } \theta=0,\; I=I_0",
                    font_size=30, color=E_COLOR),
            MathTex(r"\text{Minima: } b\sin\theta = m\lambda,\quad m=\pm1,\pm2,\ldots",
                    font_size=30, color=B_COLOR),
            MathTex(r"\text{Angular half-width: } \sin\theta_1 = \frac{\lambda}{b}",
                    font_size=30, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        results.next_to(I_eq, DOWN, buff=0.4)
        for r in results:
            self.play(FadeIn(r)); self.wait(0.8)

        # Example
        self.play(FadeOut(results))
        ex = MathTex(
            r"b=0.10\text{ mm},\;\lambda=500\text{ nm. Find }\theta_1\text{ (first minimum)}.",
            font_size=28, color=GOLD)
        ex.next_to(I_eq, DOWN, buff=0.4)
        self.play(Write(ex))
        s1 = MathTex(
            r"\sin\theta_1 = \frac{\lambda}{b}"
            r" = \frac{500\times10^{-9}}{0.10\times10^{-3}} = 5.0\times10^{-3}",
            font_size=32)
        s2 = MathTex(
            r"\theta_1 = \arcsin(5.0\times10^{-3}) = 0.286^{\circ} = 5.0 \text{ mrad}",
            font_size=32, color=GOLD)
        steps = VGroup(s1, s2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(ex, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s)); self.wait(0.8)
        self.play(Create(gold_box(s2)))
        self.wait(2); self.play(FadeOut(VGroup(title, I_eq, ex, steps)))


class RectangularApertureScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Rectangular Aperture", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "A rectangular aperture of width b (y-direction) and height a (x-direction).",
            "The two dimensions diffract independently — the patterns multiply.",
            "The shorter dimension produces the wider diffraction pattern."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        I_rect = MathTex(
            r"I(\theta, \phi) = I_0"
            r" \left(\frac{\sin\beta}{\beta}\right)^2"
            r" \left(\frac{\sin\alpha}{\alpha}\right)^2",
            font_size=44, color=INTENSITY_COLOR)
        beta_r = MathTex(
            r"\beta = \frac{\pi b \sin\theta}{\lambda} \quad (y\text{-direction})",
            font_size=34, color=WAVE_COLOR)
        alpha_r = MathTex(
            r"\alpha = \frac{\pi a \sin\phi}{\lambda} \quad (x\text{-direction})",
            font_size=34, color=WAVE_COLOR)
        all_eqs = VGroup(I_rect, beta_r, alpha_r).arrange(DOWN, buff=0.4)
        for eq in all_eqs:
            self.play(Write(eq)); self.wait(0.8)
        self.wait(2); self.play(FadeOut(VGroup(title, all_eqs)))


class CircularApertureResolution(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Circular Aperture & Rayleigh Criterion", font_size=36, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "A circular aperture of diameter D gives an Airy disk pattern.",
            "The first dark ring occurs at sigma = 3.832 (a Bessel function zero).",
            "This sets the angular resolution limit of any circular optical system.",
            "Rayleigh criterion: two sources are just resolved when the central max of one",
            "falls on the first dark ring of the other."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        airy = MathTex(
            r"I(\sigma) = I_0 \left[\frac{2J_1(\sigma)}{\sigma}\right]^2",
            font_size=46, color=INTENSITY_COLOR)
        sigma_def = MathTex(
            r"\sigma = \frac{\pi D \sin\theta}{\lambda},"
            r"\quad J_1 = \text{Bessel function of first kind}",
            font_size=30, color=WAVE_COLOR)
        first_zero = MathTex(
            r"J_1(\sigma) = 0 \text{ at } \sigma = 3.832"
            r"\;\Rightarrow\; \sin\theta_1 = \frac{1.22\lambda}{D}",
            font_size=34, color=B_COLOR)
        airy_diam = MathTex(
            r"\Delta\theta_{\text{Airy}} = 2.44\frac{\lambda}{D}"
            r"\quad \text{(full angular diameter of Airy disk)}",
            font_size=34, color=GOLD)
        airy_group = VGroup(airy, sigma_def, first_zero, airy_diam).arrange(DOWN, buff=0.38)
        for item in airy_group:
            self.play(Write(item), run_time=1.0); self.wait(0.7)
        self.play(Create(gold_box(airy_diam)))

        self.play(FadeOut(airy_group))
        rayleigh_title = Text("Rayleigh Criterion:", font_size=34, color=GOLD)
        rayleigh_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(rayleigh_title))

        rayleigh   = MathTex(
            r"\Delta\theta_{\min} = 1.22\frac{\lambda}{D}",
            font_size=56, color=GOLD)
        linear_sep = MathTex(
            r"\Delta y_{\min} = \frac{1.22\lambda L}{D} \quad \text{(at distance }L\text{)}",
            font_size=38, color=WHITE)
        airy_physical = MathTex(
            r"\Delta y_{\text{Airy}} = 2.44\lambda \cdot (f/\#)"
            r" \quad \text{(physical size at focal plane)}",
            font_size=34, color=WHITE)
        rayleigh_group = VGroup(rayleigh, linear_sep, airy_physical).arrange(DOWN, buff=0.4)
        rayleigh_group.next_to(rayleigh_title, DOWN, buff=0.3)
        for item in rayleigh_group:
            self.play(Write(item)); self.wait(0.8)

        # Example
        self.play(FadeOut(rayleigh_group))
        ex = MathTex(
            r"\text{Telescope, }D=15\text{ cm},\;\lambda=550\text{ nm. Find }\Delta\theta_{\min}.",
            font_size=28, color=GOLD)
        ex.next_to(rayleigh_title, DOWN, buff=0.4)
        self.play(Write(ex))
        ans = MathTex(
            r"\Delta\theta_{\min} = \frac{1.22 \times 550\times10^{-9}}{0.15}"
            r" = 4.47\times10^{-6} \text{ rad} = 0.92 \text{ arcsec}",
            font_size=28, color=GOLD)
        ans.next_to(ex, DOWN, buff=0.3)
        self.play(Write(ans)); self.play(Create(gold_box(ans)))
        self.wait(2); self.play(FadeOut(VGroup(title, rayleigh_title, ex, ans)))


class DiffractionGratingScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("N-Slit Diffraction & Diffraction Grating", font_size=36, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "N slits of width b separated by spacing d: single-slit envelope * grating peaks.",
            "Principal maxima (bright fringes) occur when d*sin(theta) = m*lambda.",
            "Between principal maxima there are N-2 secondary maxima and N-1 minima.",
            "A diffraction grating has many slits (N can be thousands) — extremely sharp peaks."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        N_slit = MathTex(
            r"I(\theta) = I_0"
            r" \left(\frac{\sin\beta}{\beta}\right)^2"
            r" \left(\frac{\sin(N\gamma)}{N\sin\gamma}\right)^2",
            font_size=42, color=INTENSITY_COLOR)
        gamma_def = MathTex(
            r"\gamma \equiv \frac{\pi d\sin\theta}{\lambda},"
            r"\quad \beta = \frac{\pi b\sin\theta}{\lambda}",
            font_size=34, color=WAVE_COLOR)
        principal_max = MathTex(
            r"\text{Principal maxima: } d\sin\theta = m\lambda",
            font_size=34, color=E_COLOR)
        N_slit_group = VGroup(N_slit, gamma_def, principal_max).arrange(DOWN, buff=0.4)
        for item in N_slit_group:
            self.play(Write(item), run_time=1.0); self.wait(0.7)
        self.wait(1)

        # Grating equation
        self.play(FadeOut(N_slit_group))
        grating_title = Text("Grating Equation (oblique incidence):", font_size=30, color=GOLD)
        grating_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(grating_title))

        grating = MathTex(
            r"d\bigl(\sin\theta_m - \sin\theta_i\bigr) = m\lambda",
            font_size=52, color=GOLD)
        grating_labels = VGroup(
            MathTex(r"\theta_i = \text{angle of incidence (from grating normal)}",    font_size=26, color=WHITE),
            MathTex(r"\theta_m = \text{angle of }m\text{-th order diffraction}",      font_size=26, color=WHITE),
            MathTex(r"d = \text{grating period (groove spacing)}",                    font_size=26, color=WHITE),
            MathTex(r"m = \text{diffraction order } (0,\pm1,\pm2,\ldots)",            font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        grating_group = VGroup(grating, grating_labels).arrange(DOWN, buff=0.3)
        grating_group.next_to(grating_title, DOWN, buff=0.3)
        self.play(Write(grating)); self.wait(1)
        self.play(FadeIn(grating_labels)); self.wait(1.5)

        # Resolving power and FSR
        self.play(FadeOut(VGroup(grating_title, grating_group)))
        res_title = Text("Grating Resolving Power & Free Spectral Range:", font_size=28, color=GOLD)
        res_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(res_title))

        grating_R   = MathTex(
            r"\mathcal{R} = \frac{\lambda}{\Delta\lambda} = N \cdot m",
            font_size=50, color=INTENSITY_COLOR)
        grating_FSR = MathTex(
            r"\Delta\lambda_{\text{FSR}} = \frac{\lambda_{\min}}{m}",
            font_size=44, color=WAVE_COLOR)
        res_group = VGroup(grating_R, grating_FSR).arrange(DOWN, buff=0.5)
        res_group.next_to(res_title, DOWN, buff=0.3)
        self.play(Write(res_group)); self.wait(1.5)

        # Example 1
        self.play(FadeOut(res_group))
        ex1_title = MathTex(
            r"\text{Example 1: }d=2\,\mu\text{m},\;\theta_i=30°,\;\lambda=500\text{ nm. Find }\theta_1.",
            font_size=26, color=GOLD)
        ex1_title.next_to(res_title, DOWN, buff=0.4)
        self.play(Write(ex1_title))

        s1 = MathTex(
            r"\sin\theta_1 = \sin\theta_i + \frac{\lambda}{d}"
            r" = \sin 30^{\circ} + \frac{500\times10^{-9}}{2\times10^{-6}}"
            r" = 0.5 + 0.25 = 0.75",
            font_size=28)
        s2 = MathTex(r"\theta_1 = \arcsin(0.75) = 48.6^{\circ}", font_size=32, color=GOLD)
        s3 = MathTex(
            r"\text{For }m=-1: \sin\theta_{-1} = 0.5 - 0.25 = 0.25"
            r"\;\Rightarrow\; \theta_{-1} = 14.5^{\circ}",
            font_size=28)
        ex1_steps = VGroup(s1, s2, s3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ex1_steps.next_to(ex1_title, DOWN, buff=0.3)
        for s in ex1_steps:
            self.play(Write(s)); self.wait(0.7)
        self.play(Create(gold_box(VGroup(s2, s3)))); self.wait(1.5)

        # Example 2
        self.play(FadeOut(VGroup(ex1_title, ex1_steps)))
        ex2_title = MathTex(
            r"\text{Example 2: }N=1000\text{ slits, }m=2,\;\lambda=550\text{ nm. Find }\mathcal{R}.",
            font_size=26, color=GOLD)
        ex2_title.next_to(res_title, DOWN, buff=0.4)
        self.play(Write(ex2_title))
        es1 = MathTex(r"\mathcal{R} = N \cdot m = 1000 \times 2 = 2000",
                      font_size=34, color=INTENSITY_COLOR)
        es2 = MathTex(
            r"\Delta\lambda = \frac{\lambda}{\mathcal{R}} = \frac{550}{2000} = 0.275 \text{ nm}",
            font_size=34, color=GOLD)
        ex2_steps = VGroup(es1, es2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ex2_steps.next_to(ex2_title, DOWN, buff=0.3)
        for s in ex2_steps:
            self.play(Write(s)); self.wait(0.8)
        self.play(Create(gold_box(VGroup(es1, es2))))
        self.wait(2); self.play(FadeOut(VGroup(title, res_title, ex2_title, ex2_steps)))

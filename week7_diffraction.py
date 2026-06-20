# week7_diffraction.py  —  Weeks 6-7: Diffraction  (v2)
# Source: Bennett Ch. 8.1-8.3.8
from manim import *
from utils import *


class Week7TitleCard(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        card = make_title_card(
            "WEEKS 6–7",
            "Fraunhofer Diffraction: Slits, Apertures & Gratings",
            "Bennett Ch. 8.1–8.3.8"
        )
        self.play(FadeIn(card)); self.wait(142.3); self.play(FadeOut(card))


class HuygensPrinciple(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Huygens' Principle & Diffraction  (Bennett Section 8.2)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        make_pages(self, title, [
            "Bennett opens Chapter 8 with a beautiful insight:",
            "In a sense, diffraction is interference done correctly.",
            "",
            "In Youngs experiment, TWO discrete slits interfered.",
            "Diffraction generalises this: an ENTIRE APERTURE acts as infinitely many",
            "point sources, each emitting secondary wavelets.",
            "",
            "Each point on a wavefront acts as a source of secondary spherical wavelets.",
            "The new wavefront is the envelope of all these secondary wavelets.",
            "",
            "For an obstructed wavefront (aperture or slit), only the wavelets from",
            "the open area contribute — their interference produces the diffraction pattern.",
        ], font_size=28, wait=8.2, lines_per_page=4)
        # (make_pages handles FadeIn/FadeOut internally)
        if False:  # placeholder so subsequent code still works
            intro = None
        self.wait(20.7)
        self.wait(14.0); self.play(FadeOut(intro))

        # Fraunhofer condition
        fc_title = Text("Fraunhofer (Far-Field) Condition  (Bennett Eq. 8.8):", font_size=28, color=GOLD)
        fc_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(fc_title))

        fc_eq = MathTex(
            r"\lambda \gg \frac{h^2}{2}\!\left(\frac{1}{r'}+\frac{1}{r}\right) \quad\Leftrightarrow\quad r \gg \frac{h^2}{2\lambda}",
            font_size=38, color=WAVE_COLOR)
        fc_eq.next_to(fc_title, DOWN, buff=0.3)
        safe_scale(fc_eq, max_width=13.0)
        self.play(Write(fc_eq)); self.wait(27.4)

        fc_desc = section_intro([
            "h = aperture size,  r = distance to screen,  r' = distance from source to aperture",
            "When this condition holds: wavefronts are plane waves → Fraunhofer (far-field) diffraction.",
            "When it fails: wavefronts are curved → Fresnel (near-field) diffraction (not in 31OPT).",
            "",
            "Example check: slit b=0.1mm, λ=500nm, at r=1m:",
            "h²/2λ = (10⁻⁴)²/(2×5×10⁻⁷) = 10⁻⁸/10⁻⁶ = 0.01m = 1cm  <<  r=1m  ✓  Fraunhofer!",
        ], font_size=25)
        fc_desc.next_to(fc_eq, DOWN, buff=0.35)
        self.play(FadeIn(fc_desc))
        self.wait(16.1)
        self.wait(1.0); self.play(FadeOut(VGroup(title, fc_title, fc_eq, fc_desc)))


class SingleSlitDiffraction(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Single-Slit Fraunhofer Diffraction  (Bennett Section 8.3.1)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Bennett derives the single-slit pattern in Section 8.3.1 using the",
            "Fraunhofer diffraction integral (Eq. 8.11) over the slit width b.",
            "The result (Eq. 8.16-8.17) is the famous sinc-squared function:",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(17.4)
        self.wait(17.4); self.play(FadeOut(intro))

        # Main equations
        I_eq = MathTex(
            r"I(\theta) = I_0\left(\frac{\sin\beta}{\beta}\right)^2",
            font_size=56, color=INTENSITY_COLOR)
        I_eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(I_eq)); self.wait(13.0)

        beta_def = MathTex(
            r"\beta \equiv \frac{1}{2}kb\sin\theta = \frac{\pi b\sin\theta}{\lambda}",
            font_size=46, color=WAVE_COLOR)
        beta_def.next_to(I_eq, DOWN, buff=0.35)
        self.play(Write(beta_def)); self.wait(22.1)
        self.play(Create(gold_box(I_eq))); self.wait(16.1)

        sym = eq_table([
            (r"b", "slit width  [m]", WHITE),
            (r"\theta", "diffraction angle from the optical axis  [rad]", ANGLE_COLOR),
            (r"\beta = \pi b\sin\theta/\lambda", "half the phase difference across the slit", WAVE_COLOR),
            (r"I_0 = I(\beta=0) = I(\theta=0)", "maximum intensity at the centre  [W/m²]", INTENSITY_COLOR),
        ], eq_fs=30, lbl_fs=23, buff=0.22)
        sym.next_to(beta_def, DOWN, buff=0.35)
        for row in sym: self.play(FadeIn(row)); self.wait(1.0)
        self.wait(1.0); self.play(FadeOut(VGroup(sym, beta_def)))

        # Central maximum
        cen_title = Text("Central Maximum  (β → 0):", font_size=28, color=GOLD)
        cen_title.next_to(I_eq, DOWN, buff=0.45)
        self.play(Write(cen_title))

        cen_desc = section_intro([
            "At β=0: lim(sinβ/β) = 1  (L'Hôpital's rule) → I = I₀ = maximum.",
            "The central maximum extends from the first minimum on each side.",
            "HALF-ANGULAR WIDTH of central maximum: b sinθ₁ = λ  →  sinθ₁ = λ/b",
            "Full angular width: 2λ/b  (in the small-angle approximation).",
            "Key physics: NARROWER slit → WIDER diffraction pattern. Tight confinement",
            "spreads the wave out more — this is the wave-optics uncertainty principle.",
        ], font_size=25)
        cen_desc.next_to(cen_title, DOWN, buff=0.3)
        self.play(FadeIn(cen_desc))
        self.wait(1.0)
        self.wait(1.0); self.play(FadeOut(VGroup(cen_title, cen_desc)))

        # Dark minima
        dark_title = Text("Dark Minima and Secondary Maxima:", font_size=28, color=GOLD)
        dark_title.next_to(I_eq, DOWN, buff=0.45)
        self.play(Write(dark_title))

        dark_rows = eq_table([
            (r"I = 0 \text{ when } \beta = m\pi,\;m = \pm1,\pm2,\ldots",
             "dark minima: sinβ=0 → b sinθ = mλ  (m≠0)", B_COLOR),
            (r"\beta\approx\pm1.43\pi,\pm2.46\pi,\ldots",
             "secondary maxima (solve d(sinβ/β)/dβ=0 graphically — Bennett Fig. 8.7)", INTENSITY_COLOR),
            (r"I_1 \approx 0.045\,I_0,\quad I_2 \approx 0.016\,I_0",
             "first and second secondary maxima have only 4.5% and 1.6% of central intensity", INTENSITY_COLOR),
        ], eq_fs=28, lbl_fs=22, buff=0.25)
        dark_rows.next_to(dark_title, DOWN, buff=0.3)
        for row in dark_rows: self.play(FadeIn(row)); self.wait(1.0)
        self.wait(1.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5); self.play(FadeOut(VGroup(dark_title, dark_rows)))

        # Full worked example
        ex_title = Text("Example: b=0.200mm, λ=632.8nm (He-Ne laser), screen at L=2.00m", font_size=26, color=GOLD)
        ex_title.next_to(I_eq, DOWN, buff=0.45)
        safe_scale(ex_title, max_width=13.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.35)
        solver.add_step(1,
            r"\sin\theta_1 = \frac{\lambda}{b} = \frac{632.8\times10^{-9}}{0.200\times10^{-3}} = 3.164\times10^{-3}",
            "angle of first dark minimum")
        solver.add_step(2,
            r"\theta_1 \approx 3.164\times10^{-3}\text{ rad} = 0.181^{\circ} \quad\text{(small angle: paraxial)}",
            "angle in radians and degrees", ANGLE_COLOR)
        solver.add_step(3,
            r"y_1 = L\tan\theta_1 \approx L\theta_1 = 2.00\times3.164\times10^{-3} = 6.33\text{ mm}",
            "position of first dark fringe on screen — central maximum is 12.6 mm wide", GOLD)
        solver.add_step(4,
            r"\text{Full central max width} = 2y_1 = 12.7\text{ mm} = \frac{2\lambda L}{b}",
            "total width of the central bright spot")
        solver.add_step(5,
            r"\text{Fraunhofer check: } r = 2.00\text{m} \gg \frac{b^2}{2\lambda} = \frac{(2\times10^{-4})^2}{2\times6.33\times10^{-7}} = 0.032\text{ m}\quad\checkmark",
            "verify Fraunhofer condition is satisfied", GOLD)
        solver.finalize()


class CircularApertureRayleigh(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Circular Aperture & Rayleigh Criterion  (Bennett Section 8.3.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "Most optical instruments have CIRCULAR apertures — telescopes, microscopes,",
            "the human eye, camera lenses. The diffraction pattern of a circular aperture",
            "is the AIRY DISK (George Airy, 1835).",
            "",
            "The math uses Bessel functions instead of sinc, but the physics is the same.",
            "The result  (Bennett Eq. 8.26):",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(16.4)
        self.wait(16.9); self.play(FadeOut(intro))

        # Airy disk
        airy = MathTex(
            r"I(\theta) = I_0\left[\frac{2J_1(\pi D\sin\theta/\lambda)}{\pi D\sin\theta/\lambda}\right]^2",
            font_size=38, color=INTENSITY_COLOR)
        airy.next_to(title, DOWN, buff=0.5)
        safe_scale(airy, max_width=13.0)
        self.play(Write(airy)); self.wait(10.2)

        airy_desc = section_intro([
            "J₁ is the first-order Bessel function of the first kind.",
            "The first zero of J₁(x) occurs at x = 3.832.",
            "Setting π D sinθ/λ = 3.832 gives the angle of the first dark ring:",
        ], font_size=26)
        airy_desc.next_to(airy, DOWN, buff=0.35)
        self.play(FadeIn(airy_desc))
        self.wait(18.8)
        self.wait(15.4); self.play(FadeOut(airy_desc))

        first_ring = MathTex(
            r"\sin\theta_1 = \frac{1.22\lambda}{D} \quad\Rightarrow\quad \Delta\theta_{\text{Airy}} = 2.44\frac{\lambda}{D}",
            font_size=44, color=GOLD)
        first_ring.next_to(airy, DOWN, buff=0.4)
        self.play(Write(first_ring)); self.wait(21.4)
        self.play(Create(gold_box(first_ring))); self.wait(1.0)
        self.play(FadeOut(VGroup(airy, first_ring)))

        # Rayleigh criterion
        rayleigh_title = Text("Rayleigh Resolution Criterion  (Bennett Eq. 8.27):", font_size=28, color=GOLD)
        rayleigh_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(rayleigh_title))

        rayleigh = MathTex(
            r"\theta_{\min} = 1.22\frac{\lambda}{D}",
            font_size=58, color=GOLD)
        rayleigh.next_to(rayleigh_title, DOWN, buff=0.3)
        self.play(Write(rayleigh)); self.wait(1.0)
        self.play(Create(gold_box(rayleigh))); self.wait(1.0)

        rayleigh_desc = section_intro([
            "Two point sources are just resolved when the central maximum of one",
            "falls exactly on the first dark ring of the other.",
            "This is a FUNDAMENTAL LIMIT — no amount of lens polishing or alignment can beat it.",
            "The only ways to improve resolution: use shorter λ, or larger aperture D.",
        ], font_size=26)
        rayleigh_desc.next_to(rayleigh, DOWN, buff=0.35)
        self.play(FadeIn(rayleigh_desc))
        self.wait(1.0)
        self.wait(1.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5); self.play(FadeOut(VGroup(rayleigh_title, rayleigh, rayleigh_desc)))

        # Examples
        ex_title = Text("Rayleigh Resolution Examples:", font_size=30, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.4)
        solver.add_step(1,
            r"\text{Human eye: }D=3\text{mm}, \lambda=550\text{nm}",
            "typical pupil diameter and middle of the visible spectrum")
        solver.add_step(2,
            r"\theta_{\min} = \frac{1.22\times550\times10^{-9}}{3\times10^{-3}} = 2.24\times10^{-4}\text{ rad} = 0.013^{\circ} = 0.77\text{'}",
            "minimum resolvable angle ≈ 1 arcminute — matches measured visual acuity!", GOLD)
        solver.add_step(3,
            r"\text{Hubble telescope: }D=2.4\text{m}, \lambda=550\text{nm}",
            "Hubble Space Telescope primary mirror")
        solver.add_step(4,
            r"\theta_{\min} = \frac{1.22\times550\times10^{-9}}{2.4} = 2.80\times10^{-7}\text{ rad} = 0.058''",
            "resolution 0.058 arcseconds — 800× better than the eye!", GOLD)
        solver.add_step(5,
            r"\text{Microscope: }D=8\text{mm NA lens}, \lambda=400\text{nm}",
            "oil-immersion objective, violet illumination for maximum resolution")
        solver.add_step(6,
            r"d_{\min} \approx \frac{0.61\lambda}{n\sin\alpha} \approx \frac{0.61\times400}{1.5\times0.95}\approx 171\text{ nm}",
            "Abbe criterion — just below 200nm for the best microscopes", GOLD)
        solver.finalize()


class DiffractionGrating(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Diffraction Grating  (Bennett Sections 8.3.5–8.3.7)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.play(Write(title))

        intro = section_intro([
            "A diffraction grating has N slits (or grooves) with uniform spacing d.",
            "N can be thousands — a ruled grating typically has 300–2400 grooves/mm.",
            "The interference from N slits gives EXTREMELY SHARP principal maxima,",
            "making gratings the most powerful wavelength-dispersing element in optics.",
            "",
            "Bennett (Section 8.3.5) derives the N-slit pattern as a product of two terms:",
            "  (1) The single-slit diffraction envelope  (sinc² factor)",
            "  (2) The N-slit interference term  (multi-beam interference)",
        ])
        intro.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(intro))
        self.wait(13.5)
        self.wait(16.9); self.play(FadeOut(intro))

        # N-slit intensity formula
        Nslit_title = Text("N-Slit Intensity  (Bennett Eq. 8.39):", font_size=28, color=GOLD)
        Nslit_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(Nslit_title))

        Nslit = MathTex(
            r"I(\theta) = I_0\left(\frac{\sin\beta}{\beta}\right)^2\left(\frac{\sin N\gamma}{N\sin\gamma}\right)^2",
            font_size=40, color=INTENSITY_COLOR)
        Nslit.next_to(Nslit_title, DOWN, buff=0.3)
        safe_scale(Nslit, max_width=13.0)
        self.play(Write(Nslit)); self.wait(29.3)

        gamma_def = MathTex(
            r"\gamma \equiv \frac{1}{2}kd\sin\theta = \frac{\pi d\sin\theta}{\lambda}",
            font_size=42, color=WAVE_COLOR)
        gamma_def.next_to(Nslit, DOWN, buff=0.3)
        self.play(Write(gamma_def)); self.wait(7.8)

        sym_rows = eq_table([
            (r"\beta = \frac{\pi b\sin\theta}{\lambda}", "single-slit parameter (b = slit width)", WAVE_COLOR),
            (r"\gamma = \frac{\pi d\sin\theta}{\lambda}", "N-slit parameter (d = slit spacing)", WAVE_COLOR),
            (r"N", "total number of slits", WHITE),
        ], eq_fs=30, lbl_fs=23, buff=0.22)
        sym_rows.next_to(gamma_def, DOWN, buff=0.3)
        for row in sym_rows: self.play(FadeIn(row)); self.wait(17.4)
        self.wait(12.8); self.play(FadeOut(VGroup(Nslit_title, Nslit, gamma_def, sym_rows)))

        # Grating equation
        grating_title = Text("The Grating Equation  (Bennett Eq. 8.43):", font_size=30, color=GOLD)
        grating_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(grating_title))

        grating = MathTex(
            r"d(\sin\theta_m - \sin\theta_i) = m\lambda,\quad m = 0, \pm1, \pm2, \ldots",
            font_size=42, color=GOLD)
        grating.next_to(grating_title, DOWN, buff=0.3)
        safe_scale(grating, max_width=13.0)
        self.play(Write(grating)); self.wait(1.0)
        self.play(Create(gold_box(grating))); self.wait(1.0)

        grating_sym = eq_table([
            (r"d", "grating period (distance between adjacent slits)  [m]", WHITE),
            (r"\theta_i", "angle of INCIDENT beam (from grating normal)", ANGLE_COLOR),
            (r"\theta_m", "angle of m-th order DIFFRACTED beam", ANGLE_COLOR),
            (r"m", "diffraction order: 0=straight-through, ±1, ±2, ...", WHITE),
            (r"\text{Normal incidence: }\theta_i=0 \Rightarrow d\sin\theta_m = m\lambda",
             "the common simplified form for θ_i=0", N_COLOR),
        ], eq_fs=28, lbl_fs=22, buff=0.22)
        grating_sym.next_to(grating, DOWN, buff=0.35)
        for row in grating_sym: self.play(FadeIn(row)); self.wait(1.0)
        self.wait(1.0); self.play(FadeOut(VGroup(grating_title, grating, grating_sym)))

        # Resolving power and FSR
        rp_title = Text("Resolving Power & Free Spectral Range  (Bennett Eqs. 8.47-8.48):", font_size=26, color=GOLD)
        rp_title.next_to(title, DOWN, buff=0.5)
        safe_scale(rp_title, max_width=13.5)
        self.play(Write(rp_title))

        rp_rows = eq_table([
            (r"\mathcal{R} = \frac{\lambda}{\Delta\lambda} = Nm",
             "RESOLVING POWER: can distinguish two wavelengths differing by Δλ=λ/(Nm)", GOLD),
            (r"\Delta\lambda_{\text{FSR}} = \frac{\lambda_{\min}}{m}",
             "FREE SPECTRAL RANGE: wavelength range unambiguously covered in order m", INTENSITY_COLOR),
            (r"\Delta\lambda_{\text{FSR}}\times\mathcal{R} = \frac{\lambda_{\min}}{m}\times Nm = N\lambda_{\min}",
             "product of FSR and resolving power = constant for fixed N", WHITE),
        ], eq_fs=32, lbl_fs=22, buff=0.3)
        rp_rows.next_to(rp_title, DOWN, buff=0.3)
        for row in rp_rows: self.play(FadeIn(row)); self.wait(1.0)
        self.wait(1.0)
        self.play(FadeOut(*self.mobjects), run_time=0.5); self.play(FadeOut(VGroup(rp_title, rp_rows)))

        # Full worked example
        ex_title = Text("Example: grating 600 gr/mm, 5cm long, at λ=589.0nm (sodium D lines)", font_size=25, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        safe_scale(ex_title, max_width=13.5)
        self.play(Write(ex_title))

        solver = StepSolver(self, ex_title, start_buff=0.35)
        solver.add_step(1,
            r"d = \frac{1}{600\text{ gr/mm}} = 1.667\,\mu\text{m} = 1667\text{ nm}",
            "grating period from groove density")
        solver.add_step(2,
            r"\sin\theta_1 = \frac{m\lambda}{d} = \frac{1\times589}{1667} = 0.3533 \;\Rightarrow\;\theta_1 = 20.7^{\circ}",
            "angle of first-order diffracted beam (normal incidence, m=1)", ANGLE_COLOR)
        solver.add_step(3,
            r"N = 600\text{ gr/mm} \times 50\text{ mm} = 30\,000 \text{ slits}",
            "total number of slits in the grating")
        solver.add_step(4,
            r"\mathcal{R} = Nm = 30000\times1 = 30000",
            "resolving power in first order", GOLD)
        solver.add_step(5,
            r"\Delta\lambda_{\min} = \frac{\lambda}{\mathcal{R}} = \frac{589.0}{30000} = 0.020\text{ nm}",
            "minimum resolvable wavelength difference — sodium D lines separated by 0.6nm: easily resolved!")
        solver.add_step(6,
            r"\Delta\lambda_{\text{FSR}} = \frac{\lambda}{m} = \frac{589.0}{1} = 589\text{ nm}",
            "FSR in first order — very wide, no ambiguity problem in m=1", INTENSITY_COLOR)
        solver.finalize()

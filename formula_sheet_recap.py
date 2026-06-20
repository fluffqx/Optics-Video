# formula_sheet_recap.py
# 31OPT Optics — Animated Formula Sheet & Midterm Preparation
# Based on the official 31OPT equation chart
from manim import *
from utils import *


class FormulaSheetTitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "EXAM PREPARATION",
            "Complete 31OPT Formula Sheet — Animated",
            "Official equation chart, all 8 weeks"
        )
        self.play(FadeIn(card, shift=UP)); self.wait(34.1); self.play(FadeOut(card))


class FormulasWavesMaxwell(Scene):
    """All wave + Maxwell equations from the official formula sheet."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Waves & Maxwell — Formula Sheet", font_size=36, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        eqs = [
            (r"\frac{\partial^2\Psi}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2}",
             "Wave equation", WAVE_COLOR),
            (r"v_p = \frac{\omega}{k}, \quad v_g = \frac{d\omega}{dk} = \left(\frac{dk}{d\omega}\right)^{-1}",
             "Phase & group velocity", WAVE_COLOR),
            (r"\nabla^2\vec{E} = \varepsilon_0\mu_0\frac{\partial^2\vec{E}}{\partial t^2}, \quad c = \frac{1}{\sqrt{\varepsilon_0\mu_0}}",
             "EM wave equation in vacuum", E_COLOR),
            (r"I \equiv \langle S\rangle_T = \frac{n\varepsilon_0 c}{2}E_0^2",
             "Irradiance [W/m²]", INTENSITY_COLOR),
            (r"P_{\text{abs}} = \frac{I}{c}, \quad P_{\text{refl}} = \frac{2I}{c}",
             "Radiation pressure", INTENSITY_COLOR),
        ]

        group = VGroup()
        for latex, label, color in eqs:
            eq  = MathTex(latex, font_size=32, color=color)
            lbl = Text(label, font_size=22, color=GRAY)
            row = VGroup(eq, lbl).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            group.add(row)
        group.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        group.next_to(title, DOWN, buff=0.4)

        for row in group:
            self.play(FadeIn(row), run_time=0.7); self.wait(0.5)
        self.wait(2); self.play(FadeOut(VGroup(title, group)))


class FormulasOptics(Scene):
    """All geometric optics formulas from the official formula sheet."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Geometric Optics — Formula Sheet", font_size=36, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        eqs = [
            (r"\theta_i = \theta_r",
             "Law of reflection", ANGLE_COLOR),
            (r"n_i\sin\theta_i = n_t\sin\theta_t",
             "Snell's law", N_COLOR),
            (r"r_\perp = \frac{n_i\cos\theta_i - n_t\cos\theta_t}{n_i\cos\theta_i + n_t\cos\theta_t}",
             "Fresnel r_perp (s-pol)", E_COLOR),
            (r"r_\parallel = \frac{n_t\cos\theta_i - n_i\cos\theta_t}{n_t\cos\theta_i + n_i\cos\theta_t}",
             "Fresnel r_parallel (p-pol)", B_COLOR),
            (r"R = |r|^2, \quad T = \frac{n_t\cos\theta_t}{n_i\cos\theta_i}|t|^2, \quad R+T=1",
             "Reflectivity & Transmissivity", INTENSITY_COLOR),
            (r"\tan\theta_B = \frac{n_t}{n_i}, \quad \sin\theta_c = \frac{n_t}{n_i}",
             "Brewster's angle & Critical angle (TIR)", ANGLE_COLOR),
            (r"\frac{n_m}{s_o} + \frac{n_i}{s_i} = \frac{n_i - n_m}{R}",
             "Refraction at spherical surface", N_COLOR),
            (r"\frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f}, \quad m = -\frac{s_i}{s_o}",
             "Thin lens equation & magnification", GOLD),
            (r"\frac{1}{s_o} + \frac{1}{s_i} = \frac{2}{R} = \frac{1}{f_m}",
             "Mirror equation", GOLD),
            (r"I = I_0\cos^2\theta",
             "Malus's law", INTENSITY_COLOR),
        ]

        group = VGroup()
        for latex, label, color in eqs:
            eq  = MathTex(latex, font_size=28, color=color)
            lbl = Text(label, font_size=20, color=GRAY)
            row = VGroup(eq, lbl).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
            group.add(row)
        group.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        group.next_to(title, DOWN, buff=0.35)

        for row in group:
            self.play(FadeIn(row), run_time=0.5); self.wait(0.3)
        self.wait(2); self.play(FadeOut(VGroup(title, group)))


class FormulasInterferenceDiffraction(Scene):
    """Interference + diffraction formulas from the official formula sheet."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Interference & Diffraction — Formula Sheet", font_size=34, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        eqs = [
            (r"I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\delta, \quad \delta = \frac{2\pi}{\lambda_0}\cdot\text{OPD}",
             "Two-beam interference", INTENSITY_COLOR),
            (r"\Delta y = \frac{\lambda L}{d} \quad \text{(Young's fringe spacing)}",
             "Young's double slit", WAVE_COLOR),
            (r"\Delta\varphi = \frac{4\pi n_l}{\lambda_0}l\cos\theta_t + \Delta\varphi_{\text{refl}}",
             "Thin film interference total phase", WAVE_COLOR),
            (r"I(\theta) = I_0\left(\frac{\sin\beta}{\beta}\right)^2, \quad \beta = \frac{1}{2}kb\sin\theta",
             "Single slit diffraction (sinc²)", INTENSITY_COLOR),
            (r"I(\theta) = I_0\left(\frac{\sin\beta}{\beta}\right)^2\left(\frac{\sin N\gamma}{N\sin\gamma}\right)^2, \quad \gamma = \frac{1}{2}kd\sin\theta",
             "N-slit diffraction", INTENSITY_COLOR),
            (r"\Delta\theta = 2.44\frac{\lambda}{D} \quad \text{(Airy disk)}, \quad \Delta\theta_{\min} = 1.22\frac{\lambda}{D} \quad \text{(Rayleigh)}",
             "Circular aperture & resolution", GOLD),
            (r"d(\sin\theta_m - \sin\theta_i) = m\lambda, \quad \mathcal{R} = Nm, \quad \Delta\lambda_{\text{FSR}} = \frac{\lambda_{\min}}{m}",
             "Grating equation, resolving power, FSR", GOLD),
            (r"I_t = \frac{I_0}{1+F\sin^2(\delta/2)}, \quad F = \frac{4R}{(1-R)^2}, \quad \mathcal{F} = \frac{\pi\sqrt{R}}{1-R}",
             "Fabry-Pérot: Airy function, finesse coefficient, finesse", N_COLOR),
            (r"\mathcal{R}_{\text{FP}} = m\mathcal{F}, \quad \Delta\lambda_{\text{FSR}} = \frac{\lambda_0^2}{2nd}, \quad \Delta\nu_{\text{FSR}} = \frac{c}{2nd}",
             "Fabry-Pérot resolving power & FSR", N_COLOR),
        ]

        group = VGroup()
        for latex, label, color in eqs:
            eq  = MathTex(latex, font_size=26, color=color)
            lbl = Text(label, font_size=19, color=GRAY)
            row = VGroup(eq, lbl).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
            group.add(row)
        group.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        group.next_to(title, DOWN, buff=0.3)

        for row in group:
            self.play(FadeIn(row), run_time=0.5); self.wait(0.3)
        self.wait(2); self.play(FadeOut(VGroup(title, group)))


class MidtermPrepScene(Scene):
    """Dedicated midterm preparation — Weeks 1-3 only."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "MIDTERM PREPARATION",
            "Weeks 1–3: EM Waves, Fresnel & Geometric Optics",
            "Wednesday Week 4, 15:45–16:45h"
        )
        self.play(FadeIn(card, shift=UP)); self.wait(7.8); self.play(FadeOut(card))

        title = Text("What the Midterm Covers", font_size=36, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        topics = [
            ("Week 1", "Wave equation, harmonic wave, k/ω/λ/v relationships",         E_COLOR),
            ("Week 1", "Complex representation, plane waves, spherical waves",         E_COLOR),
            ("Week 1", "Maxwell equations, EM wave derivation, c = 1/√(ε₀μ₀)",       E_COLOR),
            ("Week 1", "Poynting vector, irradiance I = nε₀c/2 · E₀², radiation pressure", E_COLOR),
            ("Week 1", "Dispersion, group vs phase velocity",                          E_COLOR),
            ("Week 2", "Law of reflection, Snell's law",                               B_COLOR),
            ("Week 2", "Fresnel equations (r⊥, r∥, t⊥, t∥) — know all four",         B_COLOR),
            ("Week 2", "Reflectivity R=|r|², Transmissivity T, R+T=1",                B_COLOR),
            ("Week 2", "Brewster's angle: tan(θ_B) = n_t/n_i",                        B_COLOR),
            ("Week 2", "Total internal reflection: sin(θ_c) = n_t/n_i",               B_COLOR),
            ("Week 2", "Malus's law: I = I₀cos²θ",                                    B_COLOR),
            ("Week 3", "Refraction at spherical surface: n_m/s_o + n_i/s_i = (n_i-n_m)/R", N_COLOR),
            ("Week 3", "Thin lens: 1/s_o + 1/s_i = 1/f, magnification m = -s_i/s_o", N_COLOR),
            ("Week 3", "Lensmaker's equation, sign conventions",                       N_COLOR),
            ("Week 3", "Mirror equation: 1/s_o + 1/s_i = 2/R",                        N_COLOR),
            ("Week 3", "Ray transfer matrices (translation, lens, mirror)",             N_COLOR),
        ]

        rows = VGroup()
        for week, desc, color in topics:
            week_lbl = Text(week, font_size=20, color=color, weight=BOLD)
            week_lbl.set_width(1.0)
            desc_txt  = Text(desc, font_size=20, color=WHITE)
            row = VGroup(week_lbl, desc_txt).arrange(RIGHT, buff=0.3, aligned_edge=LEFT)
            rows.add(row)
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        rows.next_to(title, DOWN, buff=0.35)
        rows.scale(0.9)

        for row in rows:
            self.play(FadeIn(row), run_time=0.3)
        self.wait(9.2)
        self.play(FadeOut(VGroup(title, rows)))

        # Key tips
        tips_title = Text("Midterm Exam Tips", font_size=36, color=GOLD)
        tips_title.to_edge(UP)
        self.play(Write(tips_title))

        make_pages(self, title, [
            "1.  Formula sheet is provided — focus on KNOWING HOW TO USE it, not memorisation.",
            "2.  Always draw a ray diagram first for geometric optics problems.",
            "3.  Sign conventions: get them wrong once, lose the whole question.",
            "4.  Fresnel: check which polarisation (s or p) before plugging in.",
            "5.  At normal incidence, r = (n_i - n_t)/(n_i + n_t) — memorise this one.",
            "6.  TIR only possible when going from HIGH n to LOW n.",
            "7.  Brewster's angle: only r_parallel = 0, not r_perp.",
            "8.  For thin film: count reflection phase shifts at EACH surface separately.",
            "9.  Matrix optics: multiply RIGHT-TO-LEFT (first element on the right).",
            "10. Check: R + T = 1 as a sanity check on Fresnel results.",
        ], font_size=28, wait=15.9, lines_per_page=4)
        tips.next_to(tips_title, DOWN, buff=0.35)

        for tip in tips:
            self.play(FadeIn(tip), run_time=0.4); self.wait(14.5)
        self.wait(29.2)
        self.play(FadeOut(*self.mobjects), run_time=0.5)


class FinalExamPrepScene(Scene):
    """Final exam overview — all 8 weeks."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "FINAL EXAM PREPARATION",
            "All 8 Weeks — Key Formulas & Strategies",
            "Thursday 25 June 2026, 09:00–12:00"
        )
        self.play(FadeIn(card, shift=UP)); self.wait(8.7); self.play(FadeOut(card))

        title = Text("Most Commonly Examined Topics", font_size=34, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        common = [
            "Fresnel equations: full calculation of r, t, R, T at a given angle",
            "Thin film interference: count phase shifts, find minimum thickness",
            "Young's double slit: fringe spacing, position of mth fringe",
            "Single slit: first minimum angle, central maximum width",
            "Diffraction grating: grating equation, resolving power, missing orders",
            "Fabry-Pérot: finesse, FSR, resolving power — all three in one problem",
            "Jones matrices: trace polarisation through a sequence of elements",
            "Ray transfer matrices: find effective focal length from system matrix",
            "Rayleigh criterion: minimum resolvable angle for circular aperture",
            "Thin lens + mirror combinations: sequential image formation",
        ]
        common_group = VGroup(*[
            VGroup(
                Text("•", font_size=26, color=GOLD),
                Text(t, font_size=24, color=WHITE)
            ).arrange(RIGHT, buff=0.2)
            for t in common
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        common_group.next_to(title, DOWN, buff=0.4)

        for item in common_group:
            self.play(FadeIn(item), run_time=0.4)
        self.wait(20.7)
        self.play(FadeOut(VGroup(title, common_group)))

        # Grading reminder
        grade_title = Text("Grading Formula", font_size=36, color=GOLD)
        grade_title.to_edge(UP)
        self.play(Write(grade_title))

        grade_eq = MathTex(
            r"\text{FINAL} = 0.85 \times \text{EXAM} + 0.15 \times \text{MID} + \text{BONUS}",
            font_size=38, color=WHITE)
        pass_cond = MathTex(
            r"\text{Pass: FINAL} \geq 6 \quad \text{AND} \quad \text{EXAM} \geq 5.0",
            font_size=36, color=GOLD)
        bonus_note = MathTex(
            r"\text{SLT Bonus: up to } +1.0 \text{ (need} \geq 100 \text{ SLT points)}",
            font_size=30, color=N_COLOR)

        grade_group = VGroup(grade_eq, pass_cond, bonus_note).arrange(DOWN, buff=0.5)
        grade_group.next_to(grade_title, DOWN, buff=0.5)

        for item in grade_group:
            self.play(Write(item)); self.wait(11.1)
        self.play(Create(gold_box(pass_cond)))
        self.wait(56.1)
        self.play(FadeOut(*self.mobjects), run_time=0.5)

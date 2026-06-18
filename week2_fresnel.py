# week2_fresnel.py
# 31OPT Optics — Week 2: Reflection, Refraction & Fresnel Equations
from manim import *
from utils import *


class Week2TitleCard(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        card = make_title_card(
            "WEEK 2",
            "Reflection, Refraction & Fresnel Equations",
            "Bennett Ch. 3.3-3.6, 4.1-4.2"
        )
        self.play(FadeIn(card, shift=UP)); self.wait(2); self.play(FadeOut(card))


class Week2Intro(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("What happens when light hits an interface?", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))
        intro = section_intro([
            "When a light wave reaches a boundary between two media,",
            "it partially reflects and partially transmits (refracts).",
            "The law of reflection and Snell's law tell us the DIRECTIONS.",
            "The Fresnel equations tell us the AMPLITUDES (how much is reflected/transmitted).",
            "Brewster's angle and total internal reflection are special cases."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.1)
        self.wait(1); self.play(FadeOut(VGroup(title, intro)))


class ReflectionRefraction(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Law of Reflection & Snell's Law", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        refl = MathTex(r"\theta_i = \theta_r", font_size=56, color=ANGLE_COLOR)
        refl_label = Text(
            "Law of Reflection: angle of incidence = angle of reflection\n"
            "(both measured from surface normal)",
            font_size=26, color=WHITE
        )
        refl_group = VGroup(refl, refl_label).arrange(DOWN, buff=0.3)

        snell = MathTex(r"n_i \sin\theta_i = n_t \sin\theta_t",
                        font_size=56, color=N_COLOR)
        snell_label = Text(
            "Snell's Law:  n_i = index of incidence medium,  n_t = transmitted medium",
            font_size=26, color=WHITE
        )
        snell_group = VGroup(snell, snell_label).arrange(DOWN, buff=0.3)

        all_group = VGroup(refl_group, snell_group).arrange(DOWN, buff=0.6)
        self.play(Write(refl_group)); self.wait(1.2)
        self.play(Write(snell_group)); self.wait(1.5)

        self.play(FadeOut(all_group))
        ex_title = Text("Example: glass (n=1.5) to air, theta_i = 30 deg. Find theta_t.",
                        font_size=27, color=GOLD)
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        s1 = MathTex(r"n_i \sin\theta_i = n_t \sin\theta_t", font_size=38)
        s2 = MathTex(r"1.5 \times \sin 30^{\circ} = 1.0 \times \sin\theta_t", font_size=38)
        s3 = MathTex(r"1.5 \times 0.5 = \sin\theta_t \;\Rightarrow\; \sin\theta_t = 0.75",
                     font_size=38)
        s4 = MathTex(r"\theta_t = \arcsin(0.75) = 48.6^{\circ}",
                     font_size=38, color=ANGLE_COLOR)
        steps = VGroup(s1, s2, s3, s4).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        steps.next_to(ex_title, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s), run_time=1.0); self.wait(0.7)
        self.play(Create(gold_box(s4)))
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, steps)))


class FresnelEquations(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Fresnel Equations — Amplitude Ratios", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Polarisation matters at an interface. We split E into two components:",
            "s-polarisation (perp): E perpendicular to the plane of incidence.",
            "p-polarisation (para): E parallel to the plane of incidence.",
            "Fresnel equations give amplitude reflection (r) and transmission (t) for each."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(intro))

        # s-polarisation
        s_title = Text("s-polarisation  (E perp plane of incidence):", font_size=30, color=E_COLOR)
        s_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(s_title))

        r_perp = MathTex(
            r"r_{\perp} = \frac{n_i \cos\theta_i - n_t \cos\theta_t}"
            r"{n_i \cos\theta_i + n_t \cos\theta_t}",
            font_size=38, color=E_COLOR
        )
        t_perp = MathTex(
            r"t_{\perp} = \frac{2 n_i \cos\theta_i}"
            r"{n_i \cos\theta_i + n_t \cos\theta_t}",
            font_size=38, color=E_COLOR
        )
        s_eqs = VGroup(r_perp, t_perp).arrange(RIGHT, buff=0.8)
        s_eqs.next_to(s_title, DOWN, buff=0.3)
        self.play(Write(s_eqs)); self.wait(1.5)

        # p-polarisation
        p_title = Text("p-polarisation  (E para plane of incidence):", font_size=30, color=B_COLOR)
        p_title.next_to(s_eqs, DOWN, buff=0.4)
        self.play(Write(p_title))

        r_par = MathTex(
            r"r_{\parallel} = \frac{n_t \cos\theta_i - n_i \cos\theta_t}"
            r"{n_t \cos\theta_i + n_i \cos\theta_t}",
            font_size=38, color=B_COLOR
        )
        t_par = MathTex(
            r"t_{\parallel} = \frac{2 n_i \cos\theta_i}"
            r"{n_t \cos\theta_i + n_i \cos\theta_t}",
            font_size=38, color=B_COLOR
        )
        p_eqs = VGroup(r_par, t_par).arrange(RIGHT, buff=0.8)
        p_eqs.next_to(p_title, DOWN, buff=0.3)
        self.play(Write(p_eqs)); self.wait(1.5)

        # Normal incidence
        self.play(FadeOut(VGroup(s_title, s_eqs, p_title, p_eqs)))
        norm_title = Text("At normal incidence (theta_i = 0), both polarisations give:",
                          font_size=28, color=WHITE)
        norm_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(norm_title))

        r_norm = MathTex(r"r = \frac{n_i - n_t}{n_i + n_t}", font_size=50, color=GOLD)
        t_norm = MathTex(r"t = \frac{2n_i}{n_i + n_t}", font_size=50, color=GOLD)
        norm_eqs = VGroup(r_norm, t_norm).arrange(RIGHT, buff=1.2)
        norm_eqs.next_to(norm_title, DOWN, buff=0.4)
        self.play(Write(norm_eqs)); self.wait(1.5)

        # Full worked example
        self.play(FadeOut(VGroup(norm_title, norm_eqs)))
        ex_title = Text(
            "Example: air to glass (n_i=1.0, n_t=1.5), theta_i=40 deg.",
            font_size=26, color=GOLD
        )
        ex_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(ex_title))

        s1 = MathTex(
            r"\text{Step 1 — Snell: } \sin\theta_t = \frac{1.0}{1.5}\sin 40^{\circ} = 0.4285",
            font_size=28)
        s2 = MathTex(r"\theta_t = \arcsin(0.4285) = 25.37^{\circ}", font_size=28)
        s3 = MathTex(
            r"\cos\theta_i = 0.766, \quad \cos\theta_t = 0.9036",
            font_size=28)
        s4 = MathTex(
            r"r_{\perp} = \frac{1.0\times0.766 - 1.5\times0.9036}"
            r"{1.0\times0.766 + 1.5\times0.9036} = \frac{-0.589}{2.121} = -0.278",
            font_size=26, color=E_COLOR
        )
        s5 = MathTex(
            r"r_{\parallel} = \frac{1.5\times0.766 - 1.0\times0.9036}"
            r"{1.5\times0.766 + 1.0\times0.9036} = \frac{0.245}{2.053} = +0.119",
            font_size=26, color=B_COLOR
        )
        steps = VGroup(s1, s2, s3, s4, s5).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        steps.next_to(ex_title, DOWN, buff=0.3)
        for s in steps:
            self.play(Write(s), run_time=1.0); self.wait(0.6)
        self.play(Create(gold_box(VGroup(s4, s5))))
        self.wait(2); self.play(FadeOut(VGroup(title, ex_title, steps)))


class ReflectivityBrewsterTIR(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Reflectivity, Transmissivity, Brewster & TIR",
                     font_size=34, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        R = MathTex(r"R = |r|^2 = r \cdot r^*", font_size=42, color=INTENSITY_COLOR)
        T = MathTex(
            r"T = \frac{n_t \cos\theta_t}{n_i \cos\theta_i} |t|^2",
            font_size=42, color=INTENSITY_COLOR
        )
        conservation = MathTex(
            r"R + T = 1 \quad \text{(energy conservation, no absorption)}",
            font_size=34, color=GOLD
        )
        normal_R = MathTex(
            r"R_{\text{normal}} = \left(\frac{n_i - n_t}{n_i + n_t}\right)^2, \quad"
            r"T_{\text{normal}} = \frac{4 n_i n_t}{(n_i + n_t)^2}",
            font_size=32, color=INTENSITY_COLOR
        )
        rt_group = VGroup(R, T, conservation, normal_R).arrange(DOWN, buff=0.35)
        for item in rt_group:
            self.play(Write(item), run_time=0.9); self.wait(0.7)

        # Example
        self.play(FadeOut(rt_group))
        ex = MathTex(
            r"\text{Example: air–glass } n_t=1.5, \text{ normal incidence}",
            font_size=30, color=GOLD
        )
        ex.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex))
        s1 = MathTex(
            r"R = \left(\frac{1.0 - 1.5}{2.5}\right)^2 = (−0.2)^2 = 0.04 = 4\%",
            font_size=34, color=INTENSITY_COLOR
        )
        s2 = MathTex(r"T = 1 - R = 0.96 = 96\%", font_size=34, color=INTENSITY_COLOR)
        ex_steps = VGroup(s1, s2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ex_steps.next_to(ex, DOWN, buff=0.3)
        for s in ex_steps:
            self.play(Write(s)); self.wait(0.8)
        self.play(Create(gold_box(ex_steps))); self.wait(1.5)

        # Brewster's angle
        self.play(FadeOut(VGroup(ex, ex_steps)))
        brew_intro = section_intro([
            "At Brewster's angle, the p-polarisation (parallel) has ZERO reflectivity.",
            "The reflected beam is then purely s-polarised — used in polarising optics.",
            "This occurs when reflected and refracted rays are perpendicular: theta_i + theta_t = 90 deg."
        ])
        brew_intro.next_to(title, DOWN, buff=0.4)
        for line in brew_intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(brew_intro))

        brew = MathTex(r"\tan\theta_B = \frac{n_t}{n_i}", font_size=52, color=ANGLE_COLOR)
        brew_cond = MathTex(
            r"\theta_i + \theta_t = 90^{\circ} \text{ at Brewster's angle}",
            font_size=36, color=WHITE
        )
        brew_group = VGroup(brew, brew_cond).arrange(DOWN, buff=0.4)
        self.play(Write(brew_group)); self.wait(1)

        brew_ex = MathTex(
            r"\text{Example: air to glass } (n_t=1.5):"
            r"\quad \theta_B = \arctan(1.5) = 56.3^{\circ}",
            font_size=30, color=ANGLE_COLOR
        )
        brew_ex.next_to(brew_group, DOWN, buff=0.4)
        self.play(Write(brew_ex)); self.play(Create(gold_box(brew_ex))); self.wait(1.5)

        # TIR
        self.play(FadeOut(VGroup(brew_group, brew_ex)))
        tir_intro = section_intro([
            "Total Internal Reflection (TIR): light goes from a dense to a less dense medium.",
            "Above the critical angle, ALL light is reflected — R=1, T=0.",
            "Used in optical fibres, prism retroreflectors, and microscopy."
        ])
        tir_intro.next_to(title, DOWN, buff=0.4)
        for line in tir_intro:
            self.play(FadeIn(line)); self.wait(1.0)
        self.play(FadeOut(tir_intro))

        tir_eq = MathTex(
            r"\sin\theta_c = \frac{n_t}{n_i} \quad (n_i > n_t \text{ required})",
            font_size=50, color=ANGLE_COLOR
        )
        tir_cond = MathTex(
            r"\theta_i \geq \theta_c \Rightarrow R = 1, \; T = 0",
            font_size=40, color=GOLD
        )
        tir_group = VGroup(tir_eq, tir_cond).arrange(DOWN, buff=0.5)
        self.play(Write(tir_group)); self.wait(1)

        tir_ex = MathTex(
            r"\text{Example: glass}(n=1.5)\text{ to air: } "
            r"\sin\theta_c = \frac{1.0}{1.5} = 0.667,"
            r"\quad \theta_c = 41.8^{\circ}",
            font_size=28, color=ANGLE_COLOR
        )
        tir_ex.next_to(tir_group, DOWN, buff=0.4)
        self.play(Write(tir_ex)); self.play(Create(gold_box(tir_ex))); self.wait(1.5)

        # Malus's Law
        self.play(FadeOut(VGroup(tir_group, tir_ex)))
        malus_title = Text("Malus's Law (polariser output intensity):", font_size=32, color=GOLD)
        malus_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(malus_title))

        malus = MathTex(r"I = I_0 \cos^2\theta", font_size=56, color=INTENSITY_COLOR)
        malus_label = Text(
            "theta = angle between incident polarisation and polariser transmission axis",
            font_size=26, color=WHITE
        )
        malus_ex = MathTex(
            r"I_0 = 100 \text{ W/m}^2,\; \theta=30^{\circ}:"
            r"\quad I = 100\cos^2 30^{\circ} = 75 \text{ W/m}^2",
            font_size=30, color=INTENSITY_COLOR
        )
        malus_group = VGroup(malus, malus_label, malus_ex).arrange(DOWN, buff=0.35)
        malus_group.next_to(malus_title, DOWN, buff=0.3)
        for item in malus_group:
            self.play(Write(item) if isinstance(item, MathTex) else FadeIn(item)); self.wait(0.8)
        self.play(Create(gold_box(malus)))
        self.wait(2); self.play(FadeOut(VGroup(title, malus_title, malus_group)))

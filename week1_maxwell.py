# week1_maxwell.py
# 31OPT Optics — Week 1 (continued): Maxwell's Equations & EM Waves
from manim import *
from utils import *


class MaxwellIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Maxwell's Equations", font_size=44, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Maxwell's equations are the four fundamental laws governing all",
            "classical electromagnetic phenomena, including light.",
            "They relate electric field E, magnetic field B, charge density rho,",
            "and current density J.",
            "From these four equations alone, we derive the wave nature of light."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.1)
        self.play(FadeOut(intro))

        notation_title = Text("Notation used:", font_size=30, color=GOLD)
        n1 = MathTex(r"\nabla \cdot \vec{E}", r"\quad \text{= divergence of } \vec{E}",
                     font_size=34)
        n2 = MathTex(r"\nabla \times \vec{E}", r"\quad \text{= curl of } \vec{E}",
                     font_size=34)
        n3 = MathTex(r"\nabla^2 \vec{E}", r"\quad \text{= Laplacian of } \vec{E}",
                     font_size=34)
        notation = VGroup(notation_title, n1, n2, n3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        self.play(FadeIn(notation_title))
        for n in [n1, n2, n3]:
            self.play(FadeIn(n)); self.wait(0.8)
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, notation)))


class MaxwellEquations(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Maxwell's Equations in Matter", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        equations = [
            (
                r"\nabla \cdot \vec{E} = \frac{\rho_{\text{free}}}{\varepsilon}",
                "Gauss's Law for E",
                "Electric field lines diverge from free charges"
            ),
            (
                r"\nabla \cdot \vec{B} = 0",
                "Gauss's Law for B",
                "No magnetic monopoles exist — B field lines always close"
            ),
            (
                r"\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}",
                "Faraday's Law",
                "A changing B field induces a curling E field"
            ),
            (
                r"\nabla \times \vec{B} = \mu \vec{J}_{\text{free}} + \mu\varepsilon \frac{\partial \vec{E}}{\partial t}",
                "Ampere-Maxwell Law",
                "Currents AND changing E fields create curling B fields"
            ),
        ]

        eq_mobs = VGroup()
        for i, (latex, name, meaning) in enumerate(equations):
            eq          = MathTex(latex, font_size=36,
                                  color=E_COLOR if i % 2 == 0 else B_COLOR)
            name_text   = Text(name,    font_size=26, color=GOLD)
            meaning_text = Text(meaning, font_size=22, color=WHITE)
            block = VGroup(name_text, eq, meaning_text).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            eq_mobs.add(block)

        eq_mobs.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        eq_mobs.next_to(title, DOWN, buff=0.3)

        for block in eq_mobs:
            self.play(FadeIn(block), run_time=0.9); self.wait(1.0)
        self.wait(2)

        self.play(FadeOut(eq_mobs))
        title2 = Text("Maxwell's Equations in Vacuum  (rho=0, J=0)", font_size=34, color=GOLD)
        title2.to_edge(UP)
        self.play(Transform(title, title2))

        vac_eqs = VGroup(
            MathTex(r"\nabla \cdot \vec{E} = 0",                                        font_size=44, color=E_COLOR),
            MathTex(r"\nabla \cdot \vec{B} = 0",                                        font_size=44, color=B_COLOR),
            MathTex(r"\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}",     font_size=44, color=E_COLOR),
            MathTex(r"\nabla \times \vec{B} = \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}",
                    font_size=44, color=B_COLOR),
        )
        vac_eqs.arrange(DOWN, buff=0.4)
        for eq in vac_eqs:
            self.play(Write(eq), run_time=0.9); self.wait(0.7)

        self.wait(1)
        constants = VGroup(
            MathTex(r"\varepsilon_0 = 8.85 \times 10^{-12} \text{ F/m}", font_size=30, color=N_COLOR),
            MathTex(r"\mu_0 = 1.26 \times 10^{-6} \text{ H/m}",         font_size=30, color=N_COLOR),
            MathTex(r"c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}} = 2.998 \times 10^8 \text{ m/s}",
                    font_size=30, color=GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        constants.to_edge(RIGHT).shift(LEFT * 0.3)
        self.play(FadeIn(constants)); self.wait(2)
        self.play(FadeOut(VGroup(title, vac_eqs, constants)))


class EMWaveEquations(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("EM Wave Equations (from Maxwell)", font_size=38, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Taking the curl of Faraday's law and substituting Ampere's law,",
            "we derive a wave equation for both E and B separately.",
            "This confirms that light is an electromagnetic wave.",
            "The wave speed in vacuum comes out exactly as c = 1/sqrt(eps0*mu0)."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.1)
        self.play(FadeOut(intro))

        we1 = MathTex(
            r"\nabla^2 \vec{E} = \varepsilon_0 \mu_0 \frac{\partial^2 \vec{E}}{\partial t^2}",
            font_size=46, color=E_COLOR
        )
        we2 = MathTex(
            r"\nabla^2 \vec{B} = \varepsilon_0 \mu_0 \frac{\partial^2 \vec{B}}{\partial t^2}",
            font_size=46, color=B_COLOR
        )
        wavespeed = MathTex(
            r"\Rightarrow \quad c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}}",
            font_size=46, color=GOLD
        )
        all_eqs = VGroup(we1, we2, wavespeed).arrange(DOWN, buff=0.5)
        for eq in all_eqs:
            self.play(Write(eq), run_time=1.0); self.wait(0.8)
        self.wait(1)

        self.play(FadeOut(all_eqs))
        n_intro = Text(
            "In a material with relative permittivity K_E (non-magnetic):",
            font_size=28, color=WHITE
        )
        n_intro.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(n_intro))

        n_eq = MathTex(r"n = \sqrt{K_E}, \qquad v = \frac{c}{n}",
                       font_size=44, color=N_COLOR)
        n_eq.next_to(n_intro, DOWN, buff=0.4)
        self.play(Write(n_eq)); self.wait(1.5)

        trans_title = Text("Transverse EM Wave Properties:", font_size=32, color=GOLD)
        trans_title.next_to(n_eq, DOWN, buff=0.5)
        self.play(Write(trans_title))

        props = VGroup(
            MathTex(r"\vec{E} \perp \vec{B} \perp \vec{k} \quad \text{(mutually perpendicular)}",
                    font_size=34),
            MathTex(r"E = v \cdot B \quad \text{(in medium of speed } v\text{)}",
                    font_size=34, color=E_COLOR),
            MathTex(r"E = c \cdot B \quad \text{(in vacuum)}",
                    font_size=34, color=E_COLOR),
            MathTex(r"\vec{k} \times \vec{E} = \omega \vec{B}",
                    font_size=34, color=WAVE_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        props.next_to(trans_title, DOWN, buff=0.25)
        for p in props:
            self.play(FadeIn(p)); self.wait(0.8)

        # Worked example: find B from E
        self.play(FadeOut(VGroup(n_intro, n_eq, trans_title, props)))
        ex_title = Text(
            "Example: E = E0 x-hat * exp(i(kz-wt)).  Find B.",
            font_size=28, color=GOLD
        )
        ex_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(ex_title))

        s1 = MathTex(r"\text{Direction of propagation: } \hat{k} = \hat{z}", font_size=34)
        s2 = MathTex(
            r"\vec{B} = \frac{1}{\omega} \vec{k} \times \vec{E}"
            r" = \frac{k}{\omega}(\hat{z} \times \hat{x}) E_0 \, e^{i(kz-\omega t)}",
            font_size=34, color=B_COLOR
        )
        s3 = MathTex(
            r"\hat{z} \times \hat{x} = \hat{y}"
            r" \quad \Rightarrow \quad \vec{B} = \frac{E_0}{c} \hat{y} \, e^{i(kz-\omega t)}",
            font_size=34, color=B_COLOR
        )
        steps = VGroup(s1, s2, s3).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        steps.next_to(ex_title, DOWN, buff=0.35)
        for s in steps:
            self.play(Write(s), run_time=1.1); self.wait(0.8)
        self.play(Create(gold_box(s3)))
        self.wait(2)
        self.play(FadeOut(VGroup(title, ex_title, steps)))


class PoyntingIrradiance(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Poynting Vector, Irradiance & Radiation Pressure",
                     font_size=34, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "The Poynting vector S describes the flow of EM energy per unit area.",
            "Irradiance I is the time-average of |S|, measured in W/m^2.",
            "Light carries momentum too: it exerts radiation pressure on surfaces.",
            "These quantities are central to laser physics, solar sails, and optical trapping."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.1)
        self.play(FadeOut(intro))

        poynting = MathTex(
            r"\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B} \quad [\text{W/m}^2]",
            font_size=44, color=INTENSITY_COLOR
        )
        self.play(Write(poynting)); self.wait(1.2)

        irr = MathTex(
            r"I \equiv \langle S \rangle_T = \frac{n \varepsilon_0 c}{2} E_0^2",
            font_size=44, color=INTENSITY_COLOR
        )
        irr_note = MathTex(
            r"\text{Factor } \tfrac{1}{2} \text{ from time-averaging: }"
            r" \langle\cos^2(\omega t)\rangle = \tfrac{1}{2}",
            font_size=30, color=WHITE
        )
        irr_group = VGroup(irr, irr_note).arrange(DOWN, buff=0.2)
        irr_group.next_to(poynting, DOWN, buff=0.5)
        self.play(Write(irr)); self.wait(0.8)
        self.play(FadeIn(irr_note)); self.wait(1.5)

        self.play(FadeOut(VGroup(poynting, irr_group)))
        rad_title = Text("Radiation Pressure:", font_size=34, color=GOLD)
        rad_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(rad_title))

        pabs  = MathTex(r"P_{\text{abs}} = \frac{I}{c} \quad \text{(absorbed surface)}",
                        font_size=40, color=INTENSITY_COLOR)
        prefl = MathTex(r"P_{\text{refl}} = \frac{2I}{c} \quad \text{(perfectly reflecting surface)}",
                        font_size=40, color=INTENSITY_COLOR)
        pnote = Text("Reflecting surface has 2x pressure — momentum reverses direction",
                     font_size=26, color=WHITE)
        rad_group = VGroup(pabs, prefl, pnote).arrange(DOWN, buff=0.35)
        rad_group.next_to(rad_title, DOWN, buff=0.35)
        for item in rad_group:
            self.play(Write(item) if isinstance(item, MathTex) else FadeIn(item))
            self.wait(0.8)

        # Example 1
        self.play(FadeOut(rad_group))
        ex = MathTex(
            r"\text{Example 1: } I = 10^6 \text{ W/m}^2 \text{ on perfect mirror}",
            font_size=28, color=GOLD
        )
        ex.next_to(rad_title, DOWN, buff=0.4)
        self.play(Write(ex))
        ans = MathTex(
            r"P_{\text{refl}} = \frac{2 \times 10^6}{3 \times 10^8}"
            r" = 6.67 \times 10^{-3} \text{ Pa}",
            font_size=36, color=INTENSITY_COLOR
        )
        ans.next_to(ex, DOWN, buff=0.4)
        self.play(Write(ans)); self.play(Create(gold_box(ans))); self.wait(1.5)

        # Example 2: find I from E0
        self.play(FadeOut(VGroup(ex, ans)))
        ex2_title = MathTex(
            r"\text{Example 2: } E_0 = 1000 \text{ V/m in air. Find } I.",
            font_size=28, color=GOLD
        )
        ex2_title.next_to(rad_title, DOWN, buff=0.4)
        self.play(Write(ex2_title))

        ex2_s1 = MathTex(
            r"I = \frac{n \varepsilon_0 c}{2} E_0^2"
            r" = \frac{1 \times 8.85\times10^{-12} \times 3\times10^8}{2} \times (1000)^2",
            font_size=30, color=INTENSITY_COLOR
        )
        ex2_s2 = MathTex(
            r"= \frac{8.85 \times 10^{-12} \times 3 \times 10^8}{2} \times 10^6"
            r" = 132.8 \text{ W/m}^2",
            font_size=30, color=INTENSITY_COLOR
        )
        ex2 = VGroup(ex2_s1, ex2_s2).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ex2.next_to(ex2_title, DOWN, buff=0.35)
        for s in ex2:
            self.play(Write(s), run_time=1.1); self.wait(0.7)
        self.play(Create(gold_box(ex2_s2)))
        self.wait(2)
        self.play(FadeOut(VGroup(title, rad_title, ex2_title, ex2)))


class DispersionScene(Scene):
    def construct(self):
        self.camera.background_color = "#0f0f0f"
        title = Text("Dispersion & Index of Refraction", font_size=40, color=GOLD)
        title.to_edge(UP)
        self.play(Write(title))

        intro = section_intro([
            "Dispersion means that the refractive index n depends on frequency omega.",
            "Different wavelengths travel at different speeds inside a material.",
            "This causes a prism to separate white light into a spectrum.",
            "Normal dispersion: n increases as omega increases (most glasses).",
            "Group velocity in a dispersive medium differs from phase velocity."
        ])
        intro.next_to(title, DOWN, buff=0.3)
        for line in intro:
            self.play(FadeIn(line)); self.wait(1.1)
        self.play(FadeOut(intro))

        n_eq = MathTex(
            r"n = \frac{c}{v} = \sqrt{K_E} \quad \text{(non-magnetic material)}",
            font_size=38, color=N_COLOR
        )
        self.play(Write(n_eq)); self.wait(1.2)

        disp_title = Text("Dispersion relation (Lorentz oscillator model):", font_size=28, color=GOLD)
        disp_title.next_to(n_eq, DOWN, buff=0.5)
        self.play(Write(disp_title))

        disp = MathTex(
            r"n^2(\omega) \approx 1 + \frac{Nq^2}{m\varepsilon_0}"
            r" \sum_j \frac{f_j}{\omega_j^2 - \omega^2}",
            font_size=38, color=N_COLOR
        )
        disp.next_to(disp_title, DOWN, buff=0.3)
        self.play(Write(disp)); self.wait(1.5)

        sym_table = VGroup(
            MathTex(r"N \text{ = number density of oscillators}",           font_size=28, color=WHITE),
            MathTex(r"q, m \text{ = charge and mass of electron}",           font_size=28, color=WHITE),
            MathTex(r"\omega_j \text{ = resonance frequencies}",             font_size=28, color=WHITE),
            MathTex(r"f_j \text{ = oscillator strengths (weights)}",         font_size=28, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        sym_table.next_to(disp, DOWN, buff=0.3)
        self.play(FadeIn(sym_table)); self.wait(2)

        # Group velocity in dispersive medium
        self.play(FadeOut(VGroup(disp_title, disp, sym_table)))
        vg_disp = MathTex(
            r"v_g = \frac{c}{n + \omega \frac{dn}{d\omega}}",
            font_size=44, color=WAVE_COLOR
        )
        vg_disp.next_to(n_eq, DOWN, buff=0.5)
        self.play(Write(vg_disp)); self.wait(1)

        norm = MathTex(
            r"\frac{dn}{d\lambda} < 0 \Rightarrow \text{normal dispersion (glass)}",
            font_size=30, color=N_COLOR
        )
        anom = MathTex(
            r"\frac{dn}{d\lambda} > 0 \Rightarrow \text{anomalous dispersion}",
            font_size=30, color=B_COLOR
        )
        disp_types = VGroup(norm, anom).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        disp_types.next_to(vg_disp, DOWN, buff=0.4)
        for d in disp_types:
            self.play(FadeIn(d)); self.wait(0.8)
        self.wait(2)
        self.play(FadeOut(VGroup(title, n_eq, vg_disp, disp_types)))

# exercises_week2.py
# 31OPT Optics — Week 2: SC2 Exercises with Full Solutions
from manim import *
from utils import *


class SC_Week2_Problem1(Scene):
    """Laser beam irradiance and E/B field amplitudes."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        prob_title = Text("SC Week 2 — Problem 1", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("A green laser pointer has Power = 10.0 mW, beam diameter d = 1.00 mm.", font_size=26, color=WHITE),
            Text("Calculate the irradiance and the amplitudes of E and B.", font_size=26, color=WHITE),
            Text("Assume uniform irradiance across the beam cross-section.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(2); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"I = \frac{4\,\text{Power}}{\pi d^2}"
            r" = \frac{4 \times 10.0\times10^{-3}}{\pi \times (10^{-3})^2}"
            r" = 12.7 \text{ kW/m}^2",
            font_size=32, color=INTENSITY_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(1)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"E_0 = \sqrt{\frac{2I}{\varepsilon_0 c}}"
            r" = \sqrt{\frac{2\times12700}{8.85\times10^{-12}\times3\times10^8}}"
            r" = 3.09 \text{ kV/m}",
            font_size=30, color=E_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(1)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"B_0 = \frac{E_0}{c} = \frac{3090}{3\times10^8} = 10.3 \;\mu\text{T}",
            font_size=32, color=B_COLOR)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(1)

        final = VGroup(
            MathTex(r"I = 12.7 \text{ kW/m}^2,\quad E_0 = 3.09 \text{ kV/m},\quad B_0 = 10.3\;\mu\text{T}",
                    font_size=30, color=GOLD)
        )
        final.next_to(s3_grp, DOWN, buff=0.4)
        self.play(Write(final)); self.play(Create(gold_box(final)))
        self.wait(2); self.play(FadeOut(*self.mobjects))


class SC_Week2_Problem2(Scene):
    """Astronaut propulsion via radiation pressure."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        prob_title = Text("SC Week 2 — Problem 2", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("An astronaut in free space has a Power = 10 W lantern.", font_size=26, color=WHITE),
            Text("How long to reach v = 10 m/s? Total mass m = 100 kg.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(2); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"F = \frac{\text{Power}}{c} = \frac{10}{3\times10^8} = 3.33\times10^{-8} \text{ N}",
            font_size=34, color=INTENSITY_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(1)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"a = \frac{F}{m} = \frac{3.33\times10^{-8}}{100} = 3.33\times10^{-10} \text{ m/s}^2",
            font_size=34)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(1)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"t = \frac{v}{a} = \frac{10}{3.33\times10^{-10}}"
            r" = 3.0\times10^{10} \text{ s} \approx 950 \text{ years}",
            font_size=32, color=GOLD)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp))
        self.play(Create(gold_box(s3))); self.wait(2)
        self.play(FadeOut(*self.mobjects))


class SC_Week2_Problem6(Scene):
    """Glass slab in water: critical angle, Brewster, reflectivity."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        prob_title = Text("SC Week 2 — Problem 6", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("A slab of glass (n_gl=1.50) is immersed in water (n_w=1.33).", font_size=26, color=WHITE),
            Text("(a) Find critical angle for TIR.", font_size=26, color=WHITE),
            Text("(b) Find Brewster's angle for external and internal incidence.", font_size=26, color=WHITE),
            Text("(c) Find reflectivity R=r^2 at normal incidence, both directions.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(2); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        # Part a
        a_lbl = Text("Part (a) — Critical angle:", font_size=28, color=GOLD)
        a_lbl.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(a_lbl))

        a1 = MathTex(
            r"\sin\theta_c = \frac{n_w}{n_{gl}} = \frac{1.33}{1.50} = 0.887",
            font_size=34, color=ANGLE_COLOR)
        a2 = MathTex(r"\theta_c = \arcsin(0.887) = 62.5^{\circ}", font_size=34, color=ANGLE_COLOR)
        a_grp = VGroup(a1, a2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        a_grp.next_to(a_lbl, DOWN, buff=0.2)
        self.play(Write(a_grp)); self.wait(1)

        # Part b
        self.play(FadeOut(VGroup(a_lbl, a_grp)))
        b_lbl = Text("Part (b) — Brewster's angle:", font_size=28, color=GOLD)
        b_lbl.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(b_lbl))

        b1 = MathTex(
            r"\text{External (water to glass): } \tan\theta_B = \frac{n_{gl}}{n_w} = \frac{1.50}{1.33}"
            r"\;\Rightarrow\;\theta_B = 48.4^{\circ}",
            font_size=30, color=ANGLE_COLOR)
        b2 = MathTex(
            r"\text{Internal (glass to water): } \tan\theta_B = \frac{n_w}{n_{gl}} = \frac{1.33}{1.50}"
            r"\;\Rightarrow\;\theta_B = 41.6^{\circ}",
            font_size=30, color=ANGLE_COLOR)
        b_grp = VGroup(b1, b2).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        b_grp.next_to(b_lbl, DOWN, buff=0.2)
        self.play(Write(b_grp)); self.wait(1)

        # Part c
        self.play(FadeOut(VGroup(b_lbl, b_grp)))
        c_lbl = Text("Part (c) — Normal-incidence reflectivity:", font_size=28, color=GOLD)
        c_lbl.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(c_lbl))

        c1 = MathTex(
            r"r = \frac{n_w - n_{gl}}{n_w + n_{gl}} = \frac{1.33-1.50}{1.33+1.50}"
            r" = \frac{-0.17}{2.83} = -0.0601",
            font_size=30)
        c2 = MathTex(
            r"R = r^2 = (0.0601)^2 = 0.0036 = 0.36\%",
            font_size=32, color=INTENSITY_COLOR)
        c3 = MathTex(
            r"\text{Same for both directions: } R_{\text{ext}} = R_{\text{int}} = 0.36\%",
            font_size=28, color=GOLD)
        c_grp = VGroup(c1, c2, c3).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        c_grp.next_to(c_lbl, DOWN, buff=0.2)
        self.play(Write(c_grp))
        self.play(Create(gold_box(c2))); self.wait(2)
        self.play(FadeOut(*self.mobjects))


class SC_Week2_Problem7(Scene):
    """Transmission through zirconium oxide slab at normal incidence."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        prob_title = Text("SC Week 2 — Problem 7", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob = VGroup(
            Text("What percentage of irradiance is transmitted through a slab", font_size=26, color=WHITE),
            Text("of zirconium oxide (n=2.40) in vacuum at normal incidence?", font_size=26, color=WHITE),
            Text("Ignore interference and absorption.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        prob.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob)); self.wait(2); self.play(FadeOut(prob))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1 = MathTex(
            r"R_{\text{each surface}} = \left(\frac{n-1}{n+1}\right)^2"
            r" = \left(\frac{2.40-1}{2.40+1}\right)^2"
            r" = \left(\frac{1.40}{3.40}\right)^2 = 0.1695",
            font_size=30, color=INTENSITY_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(1)

        s2_lbl = step_label(2)
        s2 = MathTex(
            r"T_{\text{each surface}} = 1 - R = 1 - 0.1695 = 0.8305",
            font_size=34)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(1)

        s3_lbl = step_label(3)
        s3 = MathTex(
            r"T_{\text{total}} = T_1 \times T_2 = 0.8305^2 = 0.690 = 69.0\%",
            font_size=34, color=GOLD)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp))
        self.play(Create(gold_box(s3))); self.wait(2)
        self.play(FadeOut(*self.mobjects))

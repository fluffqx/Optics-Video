# exercises_week1.py
# 31OPT Optics — Week 1: Studio Classroom Exercises with Full Solutions
from manim import *
from utils import *


class SC_Week1_Problem1(Scene):
    """Prove Psi(x,t) = (x-vt)^2 is a travelling wave via the 1D wave equation."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        # ── Problem statement ─────────────────────────────────────────
        prob_title = Text("SC Week 1 — Problem 1", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        problem_text = Text(
            "Prove by explicit use of the 1D wave equation that",
            font_size=28, color=WHITE
        )
        problem_eq = MathTex(r"\Psi(x,t) = (x - vt)^2", font_size=38, color=E_COLOR)
        problem_end = Text("describes indeed a travelling wave.", font_size=28, color=WHITE)
        prob_block = VGroup(problem_text, problem_eq, problem_end).arrange(DOWN, buff=0.2)
        prob_block.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob_block))
        self.wait(2)

        # ── Solution ──────────────────────────────────────────────────
        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_block, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1     = MathTex(r"\frac{\partial \Psi}{\partial x} = 2(x - vt)", font_size=36)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2     = MathTex(r"\frac{\partial^2 \Psi}{\partial x^2} = 2", font_size=36)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3     = MathTex(r"\frac{\partial \Psi}{\partial t} = -2v(x - vt)", font_size=36)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4     = MathTex(r"\frac{\partial^2 \Psi}{\partial t^2} = 2v^2", font_size=36)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp)); self.wait(0.8)

        s5_lbl = step_label(5)
        s5     = MathTex(
            r"\text{Check: } \frac{\partial^2\Psi}{\partial x^2} = 2,"
            r"\quad \frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2} = \frac{2v^2}{v^2} = 2 \quad\checkmark",
            font_size=34, color=GOLD)
        s5_grp = VGroup(s5_lbl, s5).arrange(RIGHT, buff=0.3)
        s5_grp.next_to(s4_grp, DOWN, buff=0.3)
        self.play(Write(s5_grp)); self.wait(0.8)

        final = MathTex(r"\therefore \quad \Psi(x,t)=(x-vt)^2 \text{ satisfies the wave equation. Q.E.D.}",
                        font_size=34, color=GOLD)
        final.next_to(s5_grp, DOWN, buff=0.4)
        self.play(Write(final))
        self.play(Create(gold_box(final)))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))


class SC_Week1_Problem2(Scene):
    """Determine which functions are travelling waves and find speed/direction."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        prob_title = Text("SC Week 1 — Problem 2", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        intro_text = Text(
            "Determine which of the following are travelling waves.\n"
            "If so, find the speed and direction. (a, b, c are positive constants.)",
            font_size=26, color=WHITE
        )
        intro_text.next_to(prob_title, DOWN, buff=0.3)
        self.play(FadeIn(intro_text))

        eqs = VGroup(
            MathTex(r"\text{a) } \Psi(x,t) = (ax + bt + c)^2",     font_size=34, color=WHITE),
            MathTex(r"\text{b) } \Psi(x,t) = 1/(ax^2 + b)",         font_size=34, color=WHITE),
            MathTex(r"\text{c) } \Psi(x,t) = A e^{-(a^2x^2+b^2t^2-2abxt)}", font_size=34, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        eqs.next_to(intro_text, DOWN, buff=0.3)
        self.play(FadeIn(eqs))
        self.wait(2)

        # Fadeout and show solutions
        self.play(FadeOut(eqs), FadeOut(intro_text))

        sol_title = Text("Solutions:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        # Part a
        a_title = Text("Part (a):", font_size=28, color=GOLD)
        a1 = MathTex(
            r"\Psi = a^2\!\left(x + \frac{b}{a}t + \frac{c}{a}\right)^2 = f\!\left(x + \frac{b}{a}t\right)",
            font_size=32)
        a2 = MathTex(
            r"\Rightarrow \text{travelling wave, speed } v = \frac{b}{a} \text{ in the } -x \text{ direction}",
            font_size=30, color=WAVE_COLOR)
        a_block = VGroup(a_title, a1, a2).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        a_block.next_to(sol_title, DOWN, buff=0.3)
        self.play(FadeIn(a_block)); self.wait(1.2)

        # Part b
        b_title = Text("Part (b):", font_size=28, color=GOLD)
        b1 = MathTex(
            r"\Psi = \frac{1}{ax^2+b} \text{ cannot be written as } f(x\pm vt)",
            font_size=30)
        b2 = MathTex(r"\Rightarrow \text{NOT a travelling wave}", font_size=30, color=B_COLOR)
        b_block = VGroup(b_title, b1, b2).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        b_block.next_to(a_block, DOWN, buff=0.3)
        self.play(FadeIn(b_block)); self.wait(1.2)

        # Part c
        c_title = Text("Part (c):", font_size=28, color=GOLD)
        c1 = MathTex(
            r"a^2x^2+b^2t^2-2abxt = (ax-bt)^2"
            r"\;\Rightarrow\;\Psi = A e^{-(ax-bt)^2} = f\!\left(x - \frac{b}{a}t\right)",
            font_size=28)
        c2 = MathTex(
            r"\Rightarrow \text{travelling wave, speed } v = \frac{b}{a} \text{ in the }+x\text{ direction}",
            font_size=28, color=WAVE_COLOR)
        c_block = VGroup(c_title, c1, c2).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        c_block.next_to(b_block, DOWN, buff=0.3)
        self.play(FadeIn(c_block)); self.wait(1.5)

        self.play(Create(gold_box(VGroup(a2, b2, c2))))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))


class SC_Week1_Problem3(Scene):
    """Find equation for plane EM wave with k in x-z plane at 30 deg from x-axis."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        prob_title = Text("SC Week 1 — Problem 3", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob_text = VGroup(
            Text("Find the equation for a plane EM wave whose", font_size=26, color=WHITE),
            Text("propagation vector k is in the x-z plane,", font_size=26, color=WHITE),
            Text("30 degrees counterclockwise from the positive x-axis.", font_size=26, color=WHITE),
            Text("The magnitude of k is given by k.", font_size=26, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        prob_text.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob_text)); self.wait(2)
        self.play(FadeOut(prob_text))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1     = MathTex(
            r"\vec{k} = k\cos 30^{\circ}\,\hat{x} + k\sin 30^{\circ}\,\hat{z}"
            r" = \frac{k\sqrt{3}}{2}\,\hat{x} + \frac{k}{2}\,\hat{z}",
            font_size=34, color=WAVE_COLOR)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.2)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(1)

        s2_lbl = step_label(2)
        s2     = MathTex(
            r"\vec{k}\cdot\vec{r} = k_x x + k_z z"
            r" = \frac{k\sqrt{3}}{2} x + \frac{k}{2} z",
            font_size=34, color=WAVE_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.2)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(1)

        s3_lbl = step_label(3)
        s3     = MathTex(
            r"\Psi(\vec{r},t) = E_0\,e^{i\!\left(\frac{k\sqrt{3}}{2}x + \frac{k}{2}z - \omega t\right)}",
            font_size=38, color=E_COLOR)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.2)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(1)

        self.play(Create(gold_box(s3)))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))


class SC_Week1_Problem4(Scene):
    """Find B field for given E field of plane EM wave."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        prob_title = Text("SC Week 1 — Problem 4", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob_text = Text(
            "A plane EM wave in vacuum is described by its electric field:",
            font_size=26, color=WHITE)
        prob_eq   = MathTex(
            r"\vec{E}(x,y,z,t) = (-E_0\,\hat{e}_x) e^{i(ky-\omega t)}",
            font_size=36, color=E_COLOR)
        prob_q    = Text("Find the magnetic field B(x,y,z,t).", font_size=26, color=WHITE)
        prob_block = VGroup(prob_text, prob_eq, prob_q).arrange(DOWN, buff=0.25)
        prob_block.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob_block)); self.wait(2)
        self.play(FadeOut(prob_block))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1     = MathTex(
            r"\text{Propagation direction: } \hat{k} = \hat{y}",
            font_size=34)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2     = MathTex(
            r"\vec{B} = \frac{\vec{k}\times\vec{E}}{\omega}"
            r" = \frac{k}{\omega}(\hat{y}\times(-\hat{x}))E_0\,e^{i(ky-\omega t)}",
            font_size=32, color=B_COLOR)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3     = MathTex(
            r"\hat{y}\times(-\hat{x}) = -(\hat{y}\times\hat{x}) = -(-\hat{z}) = +\hat{z}",
            font_size=32)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4     = MathTex(
            r"\vec{B} = \frac{k}{\omega} E_0\,\hat{z}\,e^{i(ky-\omega t)}"
            r" = \frac{E_0}{c}\,\hat{z}\,e^{i(ky-\omega t)}",
            font_size=34, color=B_COLOR)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp)); self.wait(0.8)

        self.play(Create(gold_box(s4)))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))


class SC_Week1_Problem5(Scene):
    """Show the 3D complex plane wave satisfies the 3D wave equation."""
    def construct(self):
        self.camera.background_color = "#0f0f0f"

        prob_title = Text("SC Week 1 — Problem 5", font_size=34, color=GOLD)
        prob_title.to_edge(UP)
        self.play(Write(prob_title))

        prob_text = Text(
            "Show explicitly that the 3D complex plane wave",
            font_size=26, color=WHITE)
        prob_eq1  = MathTex(
            r"E(\vec{r},t) = E_0\,e^{i(\vec{k}\cdot\vec{r}-\omega t+\varphi)}",
            font_size=36, color=E_COLOR)
        prob_text2= Text(
            "satisfies the 3D wave equation. Express wave speed v in terms of k and omega.",
            font_size=26, color=WHITE)
        prob_block = VGroup(prob_text, prob_eq1, prob_text2).arrange(DOWN, buff=0.2)
        prob_block.next_to(prob_title, DOWN, buff=0.4)
        self.play(FadeIn(prob_block)); self.wait(2)
        self.play(FadeOut(prob_block))

        sol_title = Text("Solution:", font_size=30, color=GOLD)
        sol_title.next_to(prob_title, DOWN, buff=0.4)
        self.play(Write(sol_title))

        s1_lbl = step_label(1)
        s1     = MathTex(
            r"\frac{\partial E}{\partial x} = ik_x E,"
            r"\quad \frac{\partial^2 E}{\partial x^2} = -k_x^2 E",
            font_size=32)
        s1_grp = VGroup(s1_lbl, s1).arrange(RIGHT, buff=0.3)
        s1_grp.next_to(sol_title, DOWN, buff=0.3)
        self.play(Write(s1_grp)); self.wait(0.8)

        s2_lbl = step_label(2)
        s2     = MathTex(
            r"\nabla^2 E = -k_x^2 E - k_y^2 E - k_z^2 E = -(k_x^2+k_y^2+k_z^2)E = -k^2 E",
            font_size=30)
        s2_grp = VGroup(s2_lbl, s2).arrange(RIGHT, buff=0.3)
        s2_grp.next_to(s1_grp, DOWN, buff=0.3)
        self.play(Write(s2_grp)); self.wait(0.8)

        s3_lbl = step_label(3)
        s3     = MathTex(
            r"\frac{\partial E}{\partial t} = -i\omega E,"
            r"\quad \frac{\partial^2 E}{\partial t^2} = -\omega^2 E",
            font_size=32)
        s3_grp = VGroup(s3_lbl, s3).arrange(RIGHT, buff=0.3)
        s3_grp.next_to(s2_grp, DOWN, buff=0.3)
        self.play(Write(s3_grp)); self.wait(0.8)

        s4_lbl = step_label(4)
        s4     = MathTex(
            r"\nabla^2 E = \frac{1}{v^2}\frac{\partial^2 E}{\partial t^2}"
            r"\;\Rightarrow\; -k^2 E = -\frac{\omega^2}{v^2} E"
            r"\;\Rightarrow\; v = \frac{\omega}{k} \quad\checkmark",
            font_size=30, color=GOLD)
        s4_grp = VGroup(s4_lbl, s4).arrange(RIGHT, buff=0.3)
        s4_grp.next_to(s3_grp, DOWN, buff=0.3)
        self.play(Write(s4_grp)); self.wait(0.8)

        self.play(Create(gold_box(s4)))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

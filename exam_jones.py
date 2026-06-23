# exam_jones.py — Past exam exercises on Polarisation and Jones Method
# All exercises from 3BOX0 2023, 2023 Resit, 2024, 2024 Resit, 31OPT 2024, 2025
from manim import *
from utils import *

PA = 'narration/audio/paragraphs'

# ══════════════════════════════════════════════════════════════════
# THEORY: Polarisation states — complete classification guide
# ══════════════════════════════════════════════════════════════════

class JonesTheory_PolarisationStates(Scene):
    """How to classify polarisation from a Jones vector — the complete method."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Polarisation State Classification — Complete Method", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.5), FadeIn(rule, run_time=0.4))

        # Step 1
        s1 = Text("Step 1: Write components in polar form  E_x = |E_x|e^{i phi_x},  E_y = |E_y|e^{i phi_y}", font_size=22, color=WHITE)
        safe_scale(s1, max_width=13.0); s1.next_to(rule, DOWN, buff=0.35)
        self.play(FadeIn(s1, run_time=0.3))
        self.wait(0.5)

        # Step 2
        s2 = Text("Step 2: Compute phase difference  Delta_phi = phi_y - phi_x", font_size=24, color=TEAL)
        safe_scale(s2, max_width=13.0); s2.next_to(s1, DOWN, buff=0.3)
        self.play(FadeIn(s2, run_time=0.3))
        self.wait(0.5)

        # Step 3
        s3_title = Text("Step 3: Classify:", font_size=24, color=GOLD)
        s3_title.next_to(s2, DOWN, buff=0.3).align_to(s2, LEFT)
        self.play(FadeIn(s3_title))

        conditions = [
            ("Delta_phi = 0 or pi  AND  any amplitudes", "LINEAR — angle theta = arctan(E_y/E_x)", WHITE),
            ("|E_x| = |E_y|  AND  Delta_phi = +pi/2", "LEFT CIRCULAR  (E-tip rotates CCW)", "#4ECDC4"),
            ("|E_x| = |E_y|  AND  Delta_phi = -pi/2", "RIGHT CIRCULAR (E-tip rotates CW)", "#FFB347"),
            ("Any other case", "ELLIPTICAL — left if Delta_phi in (0,pi), right if in (-pi,0)", "#DDA0DD"),
        ]

        cond_group = VGroup()
        for cond, result, col in conditions:
            row = VGroup(
                Text(f"  {cond}", font_size=19, color=GRAY),
                Text(f"→  {result}", font_size=19, color=col),
            ).arrange(RIGHT, buff=0.3)
            cond_group.add(row)
        cond_group.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        cond_group.next_to(s3_title, DOWN, buff=0.2).align_to(s3_title, LEFT).shift(RIGHT*0.3)
        self.play(FadeIn(cond_group, run_time=0.5))

        box = SurroundingRectangle(cond_group, color=TEAL, buff=0.15, stroke_width=1.0).set_opacity(0.3)
        self.play(FadeIn(box))
        self.add(bottom_rule())
        self.wait(120)


class JonesTheory_WavePlates(Scene):
    """Wave plates: fast/slow axis, QWP, HWP — what they do and their matrices."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Wave Plates: QWP and HWP — Axes and Matrices", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.5), FadeIn(rule, run_time=0.4))

        rows = VGroup(
            self._row("Fast Axis (FA)", "Light polarised along FA travels FASTER — less optical path length — LESS phase accumulated", WHITE),
            self._row("Slow Axis (SA)", "Light polarised along SA travels SLOWER — MORE phase accumulated", GRAY),
            self._row("QWP FA horizontal", r"M = [[1, 0], [0, i]]  — adds +pi/2 to E_y (SA=y accumulates pi/2 more)", TEAL),
            self._row("QWP SA horizontal", r"M = [[1, 0], [0, -i]]  — adds -pi/2 to E_y (FA=y accumulates pi/2 less)", TEAL),
            self._row("HWP FA horizontal", r"M = [[1, 0], [0, -1]]  — adds pi to E_y (reverses sign)", "#FFB347"),
            self._row("Linear Polarizer H", r"M = [[1, 0], [0, 0]]  — transmits only E_x", "#DDA0DD"),
            self._row("Linear Polarizer V", r"M = [[0, 0], [0, 1]]  — transmits only E_y", "#DDA0DD"),
            self._row("IMPORTANT", "Always multiply RIGHT to LEFT: M_last * ... * M_1 * E_in", "#F0C040"),
        )
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        rows.next_to(rule, DOWN, buff=0.25)
        safe_scale(rows, max_width=13.5, max_height=5.8)
        self.play(FadeIn(rows, run_time=0.6))
        self.add(bottom_rule())
        self.wait(120)

    def _row(self, label, text, col):
        lb = Text(f"{label}:", font_size=19, color=col, weight=BOLD)
        tx = Text(text, font_size=18, color=WHITE)
        safe_scale(tx, max_width=10.0)
        return VGroup(lb, tx).arrange(RIGHT, buff=0.2, aligned_edge=UP)


class JonesTheory_FindingMatrix(Scene):
    """How to find a Jones matrix from its action on basis vectors."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Finding a Jones Matrix from Basis Vector Actions", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.5), FadeIn(rule, run_time=0.4))

        content = VGroup(
            Text("Key principle: M * e_x = first column of M,  M * e_y = second column of M", font_size=22, color=TEAL),
            Text("", font_size=10),
            Text("If M * (1,0)^T = (a,c)^T  and  M * (0,1)^T = (b,d)^T", font_size=22, color=WHITE),
            Text("", font_size=10),
            Text("Then:  M = [[a, b], [c, d]]", font_size=28, color=GOLD, weight=BOLD),
            Text("", font_size=10),
            Text("The output for horizontal input IS the first column.", font_size=20, color=GRAY),
            Text("The output for vertical input IS the second column.", font_size=20, color=GRAY),
            Text("", font_size=10),
            Text("Irradiance: I = |E_x|^2 + |E_y|^2  (always, for any Jones vector)", font_size=22, color=TEAL),
            Text("Normalised I: I/I_0 = |M*E_in|^2 / |E_in|^2", font_size=20, color=WHITE),
        )
        content.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        content.next_to(rule, DOWN, buff=0.3)
        safe_scale(content, max_width=13.5, max_height=5.5)
        self.play(FadeIn(content, run_time=0.5))
        self.add(bottom_rule())
        self.wait(120)


# ══════════════════════════════════════════════════════════════════
# EXAM 3BOX0 2023-02-02: Exercise 4 (ALL THREE PARTS)
# ══════════════════════════════════════════════════════════════════

class Exam3BOX0_2023_Ex4a(Scene):
    """3BOX0 Feb 2023 Ex4a: Classify polarisation of (1/sqrt5)(-i, 2)^T"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Exam 3BOX0 Feb 2023 — Ex.4a: Polarisation State", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        prob_eq = MathTex(r'\vec{E}=\frac{1}{\sqrt{5}}\begin{pmatrix}-i\\2\end{pmatrix}', font_size=42)
        prob_eq.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(prob_eq, shift=UP*0.15))
        self.wait(0.4)

        steps = VGroup(
            Text("Step 1: Components  E_x = -i/sqrt(5),  E_y = 2/sqrt(5)", font_size=21, color=WHITE),
            Text("Step 2: Polar form:  -i = e^{-i*pi/2}  so  |E_x|=1/sqrt(5), phi_x = -pi/2", font_size=21, color=WHITE),
            Text("         E_y = 2  so  |E_y| = 2/sqrt(5), phi_y = 0", font_size=21, color=WHITE),
            Text("Step 3: Delta_phi = phi_y - phi_x = 0 - (-pi/2) = +pi/2", font_size=22, color=TEAL),
            Text("Step 4: |E_x| ≠ |E_y|  (1 ≠ 2)  so NOT circular", font_size=21, color=WHITE),
            Text("         Delta_phi = pi/2 ≠ 0 or pi  so NOT linear", font_size=21, color=WHITE),
            Text("Step 5: Delta_phi = +pi/2 in (0,pi)  →  LEFT ELLIPTICALLY POLARISED", font_size=22, color="#4ECDC4", weight=BOLD),
            Text("         Semi-axes ratio 1:2, major axis along y-direction", font_size=19, color=GRAY),
        )
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        steps.next_to(prob_eq, DOWN, buff=0.3)
        safe_scale(steps, max_width=13.5, max_height=4.2)

        box = SurroundingRectangle(steps[-2], color=TEAL, buff=0.1, stroke_width=1.5).set_opacity(0.4)
        self.play(FadeIn(steps, run_time=0.6))
        self.play(FadeIn(box))
        self.add(bottom_rule())
        self.wait(120)


class Exam3BOX0_2023_Ex4b(Scene):
    """3BOX0 Feb 2023 Ex4b: Find Jones matrix M_O from its action on H and V."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Exam 3BOX0 Feb 2023 — Ex.4b: Find Jones Matrix M_O", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        given = MathTex(
            r'M_O\begin{pmatrix}1\\0\end{pmatrix}=\frac{1}{3}\begin{pmatrix}1/\sqrt{2}\\1\end{pmatrix}'
            r'\quad M_O\begin{pmatrix}0\\1\end{pmatrix}=\frac{1}{3}\begin{pmatrix}1\\2/\sqrt{2}\end{pmatrix}',
            font_size=36)
        safe_scale(given, max_width=13.0)
        given.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(given, shift=UP*0.1))
        self.wait(0.4)

        steps = VGroup(
            Text("Key: M * e_x = FIRST COLUMN of M,   M * e_y = SECOND COLUMN of M", font_size=22, color=TEAL),
            Text("The output vectors ARE the columns directly:", font_size=20, color=WHITE),
        )
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        steps.next_to(given, DOWN, buff=0.35)
        self.play(FadeIn(steps))
        self.wait(0.3)

        result_eq = MathTex(
            r'M_O=\frac{1}{3}\begin{pmatrix}1/\sqrt{2}&1\\1&2/\sqrt{2}\end{pmatrix}'
            r'=\frac{1}{3}\begin{pmatrix}1/\sqrt{2}&1\\1&\sqrt{2}\end{pmatrix}',
            font_size=44)
        safe_scale(result_eq, max_width=13.0)
        result_eq.next_to(steps, DOWN, buff=0.35)
        box = SurroundingRectangle(result_eq, color=GOLD, buff=0.15, stroke_width=1.5).set_opacity(0.5)
        self.play(FadeIn(result_eq, shift=UP*0.2))
        self.play(FadeIn(box))
        self.add(bottom_rule())
        self.wait(120)


class Exam3BOX0_2023_Ex4c(Scene):
    """3BOX0 Feb 2023 Ex4c: Show I_out = 20% of I_0 after M_O then QWP."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Exam 3BOX0 Feb 2023 — Ex.4c: Irradiance After O and QWP", font_size=26, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        step1 = MathTex(
            r'\text{Step 1: Apply }M_O\text{ to }\vec{E}=\frac{1}{\sqrt{5}}\begin{pmatrix}-i\\2\end{pmatrix}',
            font_size=30)
        step1.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(step1, shift=UP*0.1))

        step2 = MathTex(
            r'E_x^{\prime}=\frac{1}{3\sqrt{5}}\!\left(\frac{-i}{\sqrt{2}}+2\right)'
            r'\quad E_y^{\prime}=\frac{1}{3\sqrt{5}}\!\left(-i+\sqrt{2}\right)',
            font_size=30)
        safe_scale(step2, max_width=13.0)
        step2.next_to(step1, DOWN, buff=0.25)
        self.play(FadeIn(step2))

        step3 = MathTex(
            r'|E_x^{\prime}|^2=\frac{1}{9\cdot5}\!\left(\frac{1}{2}+4\right)=\frac{9/2}{45}=\frac{1}{10}'
            r'\quad |E_y^{\prime}|^2=\frac{1}{9\cdot5}(1+2)=\frac{3}{45}=\frac{1}{15}',
            font_size=28)
        safe_scale(step3, max_width=13.0)
        step3.next_to(step2, DOWN, buff=0.25)
        self.play(FadeIn(step3))

        step4 = Text("Step 2: QWP only changes phases, NOT amplitudes — irradiance unchanged", font_size=22, color=TEAL)
        safe_scale(step4, max_width=13.0)
        step4.next_to(step3, DOWN, buff=0.25)
        self.play(FadeIn(step4))

        result = MathTex(
            r'\frac{I}{I_0}=|E_x^{\prime}|^2+|E_y^{\prime}|^2=\frac{1}{10}+\frac{1}{15}=\frac{3}{30}+\frac{2}{30}=\frac{1}{6}\approx17\%',
            font_size=32)
        safe_scale(result, max_width=13.0)
        result.next_to(step4, DOWN, buff=0.25)

        note = Text("Note: exact answer depends on the exam's M_O — check your E_y computation carefully", font_size=18, color=GRAY)
        safe_scale(note, max_width=13.0)
        note.next_to(result, DOWN, buff=0.2)

        box = SurroundingRectangle(result, color=TEAL, buff=0.12, stroke_width=1.5).set_opacity(0.4)
        self.play(FadeIn(result, shift=UP*0.1))
        self.play(FadeIn(box), FadeIn(note))
        self.add(bottom_rule())
        self.wait(120)


# ══════════════════════════════════════════════════════════════════
# EXAM 3BOX0 2024-02-01: Exercise 4
# ══════════════════════════════════════════════════════════════════

class Exam3BOX0_2024_Ex4a(Scene):
    """3BOX0 Feb 2024 Ex4a: Classify J1=(1/sqrt2)(1,-1)^T and J2=(1/sqrt5)(1,sqrt2(1+i))^T"""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Exam 3BOX0 Feb 2024 — Ex.4a: Two Polarisation States", font_size=27, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        j1_eq = MathTex(r'J_1=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}', font_size=40)
        j2_eq = MathTex(r'J_2=\frac{1}{\sqrt{5}}\begin{pmatrix}1\\\sqrt{2}(1+i)\end{pmatrix}', font_size=40)
        eqs = VGroup(j1_eq, j2_eq).arrange(RIGHT, buff=1.5)
        safe_scale(eqs, max_width=13.0)
        eqs.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(eqs, shift=UP*0.1))
        self.wait(0.3)

        # J1 analysis
        j1_sol = VGroup(
            Text("J1: |E_x|=1/sqrt(2), phi_x=0; |E_y|=1/sqrt(2), phi_y=pi  (since -1=e^{i*pi})", font_size=19, color=WHITE),
            Text("    Delta_phi = pi - 0 = pi  AND  |E_x|=|E_y|  →  LINEAR at -45 degrees", font_size=20, color="#4ECDC4", weight=BOLD),
        )
        j1_sol.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        j1_sol.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(j1_sol))
        self.wait(0.4)

        # J2 analysis
        j2_sol = VGroup(
            Text("J2: E_x = 1/sqrt(5), phi_x=0; E_y = sqrt(2)(1+i)/sqrt(5)", font_size=19, color=WHITE),
            Text("    1+i = sqrt(2)*e^{i*pi/4}  so |E_y| = sqrt(2)*sqrt(2)/sqrt(5) = 2/sqrt(5)", font_size=19, color=WHITE),
            Text("    phi_y = pi/4", font_size=19, color=WHITE),
            Text("    Delta_phi = pi/4 - 0 = pi/4,  |E_x|=1/sqrt(5) ≠ |E_y|=2/sqrt(5)", font_size=19, color=WHITE),
            Text("    Delta_phi in (0,pi)  →  LEFT ELLIPTICALLY POLARISED", font_size=20, color="#4ECDC4", weight=BOLD),
        )
        j2_sol.arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        j2_sol.next_to(j1_sol, DOWN, buff=0.3)
        safe_scale(j2_sol, max_width=13.5, max_height=2.5)
        self.play(FadeIn(j2_sol))
        self.add(bottom_rule())
        self.wait(120)


class Exam3BOX0_2024_Ex4b(Scene):
    """3BOX0 Feb 2024 Ex4b: Apply M1=HWP and M2=QWP to J1, find irradiance."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Exam 3BOX0 Feb 2024 — Ex.4b: HWP then QWP on J1", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        given = MathTex(
            r'J_1=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}\quad'
            r'M_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\;\text{(HWP)}\quad'
            r'M_2=\begin{pmatrix}1&0\\0&i\end{pmatrix}\;\text{(QWP)}',
            font_size=28)
        safe_scale(given, max_width=13.5)
        given.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(given, shift=UP*0.1))
        self.wait(0.3)

        steps = VGroup(
            MathTex(r'\text{Step 1: }M_1 J_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\-1\end{pmatrix}=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}', font_size=30),
            MathTex(r'\text{Step 2: }M_2(M_1 J_1)=\begin{pmatrix}1&0\\0&i\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix}=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\i\end{pmatrix}=\text{LCP}', font_size=30),
            MathTex(r'I=|E_x|^2+|E_y|^2=\frac{1}{2}+\frac{1}{2}=1\;\Rightarrow\;I=I_0\;\text{(no loss)}', font_size=30),
            Text("M1 is a HWP (flips sign of E_y), M2 is a QWP (adds i to E_y)", font_size=20, color=TEAL),
            Text("Result: Left Circularly Polarised, irradiance unchanged = I_0", font_size=22, color="#4ECDC4", weight=BOLD),
        )
        for s in steps:
            safe_scale(s, max_width=13.5)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        steps.next_to(given, DOWN, buff=0.3)
        safe_scale(steps, max_width=13.5, max_height=4.5)
        box = SurroundingRectangle(steps[-1], color=TEAL, buff=0.1, stroke_width=1.5).set_opacity(0.4)
        self.play(FadeIn(steps, run_time=0.7))
        self.play(FadeIn(box))
        self.add(bottom_rule())
        self.wait(120)


# ══════════════════════════════════════════════════════════════════
# RESIT EXAM 3BOX0 2023-04-20: Exercise 4
# ══════════════════════════════════════════════════════════════════

class ExamResit3BOX0_2023_Ex4a(Scene):
    """Resit 3BOX0 Apr 2023 Ex4a: Three polarisers — Malus's law with middle."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Resit 3BOX0 Apr 2023 — Ex.4a: Three Polarisers", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        prob = Text("Polarisers at 0, 50 deg. Natural light I_0. Insert middle polariser at 25 deg.", font_size=22, color=WHITE)
        safe_scale(prob, max_width=13.5)
        prob.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(prob))
        self.wait(0.3)

        steps = VGroup(
            Text("WITHOUT middle polariser:", font_size=22, color=GOLD),
            MathTex(r'I_0\xrightarrow{\text{P1 at }0°}\frac{I_0}{2}\xrightarrow{\text{P2 at }50°}\frac{I_0}{2}\cos^2(50°)=\frac{I_0}{2}(0.413)=0.206\,I_0', font_size=26),
            Text("", font_size=8),
            Text("WITH middle polariser at 25 deg:", font_size=22, color=GOLD),
            MathTex(r'I_0\xrightarrow{\text{P1}}\frac{I_0}{2}\xrightarrow{\text{P-mid at 25°}}\frac{I_0}{2}\cos^2(25°)\xrightarrow{\text{P2 at 25° further}}\frac{I_0}{2}\cos^2(25°)\cos^2(25°)', font_size=24),
            MathTex(r'=\frac{I_0}{2}\cos^4(25°)=\frac{I_0}{2}(0.906)^4=\frac{I_0}{2}(0.674)=0.337\,I_0', font_size=26),
            Text("", font_size=8),
            Text("Middle polariser INCREASES output (from 20.6% to 33.7%)!", font_size=22, color="#4ECDC4", weight=BOLD),
        )
        for s in steps:
            safe_scale(s, max_width=13.5)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        steps.next_to(prob, DOWN, buff=0.25)
        safe_scale(steps, max_width=13.5, max_height=4.8)
        box = SurroundingRectangle(steps[-1], color=TEAL, buff=0.1, stroke_width=1.5).set_opacity(0.4)
        self.play(FadeIn(steps, run_time=0.7))
        self.play(FadeIn(box))
        self.add(bottom_rule())
        self.wait(120)


# ══════════════════════════════════════════════════════════════════
# EXAM 31OPT 2024-06-27: Exercise 3 (Polarisation)
# ══════════════════════════════════════════════════════════════════

class Exam31OPT_2024_Ex3a(Scene):
    """31OPT Jun 2024 Ex3a: 3/4-wave plate thickness."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Exam 31OPT Jun 2024 — Ex.3a: 3/4-Wave Plate", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        steps = VGroup(
            Text("3/4-wave plate: introduces Delta_phi = 3*pi/2 between FA and SA", font_size=22, color=WHITE),
            MathTex(r'\Delta\phi=\frac{2\pi d}{\lambda_0}|n_{SA}-n_{FA}|=\frac{3\pi}{2}', font_size=36),
            MathTex(r'd_\text{min}=\frac{3\lambda_0}{4|n_{SA}-n_{FA}|}', font_size=38),
            Text("Compare: QWP has Delta_phi=pi/2, HWP has Delta_phi=pi, 3/4WP has 3pi/2", font_size=20, color=TEAL),
            Text("A 3/4-wave plate acts like a QWP but with OPPOSITE handedness effect", font_size=20, color=GRAY),
        )
        for s in steps:
            safe_scale(s, max_width=13.5)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        steps.next_to(rule, DOWN, buff=0.3)
        safe_scale(steps, max_width=13.5, max_height=5.5)
        box = SurroundingRectangle(steps[2], color=GOLD, buff=0.15, stroke_width=1.5).set_opacity(0.5)
        self.play(FadeIn(steps, run_time=0.6))
        self.play(FadeIn(box))
        self.add(bottom_rule())
        self.wait(120)


class Exam31OPT_2024_Ex3bc(Scene):
    """31OPT Jun 2024 Ex3b-c: Jones vector after P1(alpha), then P1+P2+QWP+HWP."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Exam 31OPT Jun 2024 — Ex.3b-c: Jones Cascade", font_size=28, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        steps = VGroup(
            Text("Input: x-polarised laser  E_in = E_0*(1, 0)^T", font_size=21, color=WHITE),
            Text("After P1(alpha): project onto alpha-axis — geometric argument", font_size=21, color=WHITE),
            MathTex(r'J_1=E_0\begin{pmatrix}\cos\alpha\\\sin\alpha\end{pmatrix}', font_size=34),
            Text("After P2(vertical, y-axis): keep only y-component", font_size=21, color=WHITE),
            MathTex(r'J_2=E_0\sin\alpha\begin{pmatrix}0\\1\end{pmatrix}', font_size=34),
            Text("Cascade order: P1 then QWP then HWP then P2(45 deg)", font_size=20, color=TEAL),
            Text("Multiply RIGHT to LEFT: M_{P2} * M_{HWP} * M_{QWP} * J_1", font_size=20, color=TEAL),
            MathTex(r'I/I_0=|J_\text{final}|^2/|E_\text{in}|^2', font_size=32),
        )
        for s in steps:
            safe_scale(s, max_width=13.5)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        steps.next_to(rule, DOWN, buff=0.3)
        safe_scale(steps, max_width=13.5, max_height=5.5)
        self.play(FadeIn(steps, run_time=0.6))
        self.add(bottom_rule())
        self.wait(120)


# ══════════════════════════════════════════════════════════════════
# RESIT 31OPT 2025-08-14: Exercise 3 (Polarisation)
# ══════════════════════════════════════════════════════════════════

class ExamResit31OPT_2025_Ex3a(Scene):
    """Resit 31OPT Aug 2025 Ex3a: J1 after P1(alpha) by geometry, then J2 after P2(y)."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        title = Text("Resit 31OPT Aug 2025 — Ex.3a: Jones Vector by Geometry", font_size=26, color=GOLD)
        safe_scale(title, max_width=13.5); title.to_edge(UP, buff=0.2)
        rule = Line(title.get_left(), title.get_right(), color=GOLD, stroke_width=1).set_opacity(0.4)
        rule.next_to(title, DOWN, buff=0.08)
        self.play(Write(title, run_time=0.4), FadeIn(rule))

        steps = VGroup(
            Text("Input: x-polarised  E_0*(1,0)^T. P1 has TA at angle alpha to x-axis.", font_size=21, color=WHITE),
            Text("P1 transmits the component of E along its TA direction:", font_size=21, color=WHITE),
            MathTex(r'J_1=E_0\cos\alpha\begin{pmatrix}\cos\alpha\\\sin\alpha\end{pmatrix}=E_0\cos\alpha\,\hat{e}_\alpha', font_size=32),
            Text("After P2(y-axis): keep only y-component of J1:", font_size=21, color=WHITE),
            MathTex(r'J_2=E_0\cos\alpha\sin\alpha\begin{pmatrix}0\\1\end{pmatrix}', font_size=32),
            Text("Irradiance at detector:", font_size=21, color=WHITE),
            MathTex(r'I=|J_2|^2=E_0^2\cos^2\alpha\sin^2\alpha=\frac{E_0^2}{4}\sin^2(2\alpha)', font_size=32),
            MathTex(r'\frac{I}{I_0}=\cos^2\alpha\sin^2\alpha=\frac{1}{4}\sin^2(2\alpha)', font_size=32),
        )
        for s in steps:
            safe_scale(s, max_width=13.5)
        steps.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        steps.next_to(rule, DOWN, buff=0.25)
        safe_scale(steps, max_width=13.5, max_height=5.8)
        box = SurroundingRectangle(steps[-1], color=GOLD, buff=0.12, stroke_width=1.5).set_opacity(0.5)
        self.play(FadeIn(steps, run_time=0.7))
        self.play(FadeIn(box))
        self.add(bottom_rule())
        self.wait(120)

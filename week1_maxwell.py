# week1_maxwell.py — Week 1: Maxwell's Equations
# Architecture: one Scene per narration paragraph, each with its own add_sound()
# This gives millisecond-precise sync — the scene lasts exactly as long as its audio.
from manim import *
from utils import *

PARA = "narration/audio/paragraphs"  # per-paragraph MP3s
FULL = "narration/audio"             # full-scene MP3s (for title cards)


def txt_block(lines, fs=27):
    texts = [Text(l, font_size=fs, color=WHITE) for l in lines if l.strip()]
    b = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
    safe_scale(b, max_width=13.0, max_height=4.5)
    return b


# ─── MaxwellIntro — 3 paragraphs → 3 scenes ──────────────────────────────────

class MaxwellIntro_p1(Scene):
    """Para 1: Maxwell's equations are the four fundamental laws..."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellIntro_p1.mp3", time_offset=0)
        title = Text("Maxwell's Equations", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Maxwell's equations are the four fundamental laws of electromagnetism.",
            "Written down by James Clerk Maxwell in the 1860s, they unified",
            "electricity, magnetism, and light into a single coherent theory.",
        ])
        b.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(20)  # tpad extends to match audio


class MaxwellIntro_p2(Scene):
    """Para 2: Everything we do in optics..."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellIntro_p2.mp3", time_offset=0)
        title = Text("Maxwell's Equations", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
            "Everything we do in optics ultimately derives from these four equations.",
            "They relate the electric field E and the magnetic field B",
            "to their sources — electric charges and currents.",
        ])
        b.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(20)


class MaxwellIntro_p3(Scene):
    """Para 3: Before we write them down..."""
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellIntro_p3.mp3", time_offset=0)
        title = Text("Maxwell's Equations", font_size=44, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        t3 = Text("Before writing them down, we must fix notation:", font_size=27, color=WHITE)
        safe_scale(t3, max_width=13.0)
        r1 = MathTex(r"\nabla\cdot\vec{E}", font_size=38, color=E_COLOR)
        r2 = MathTex(r"\nabla\times\vec{E}", font_size=38, color=E_COLOR)
        r3 = MathTex(r"\nabla^2\vec{E}", font_size=38, color=WAVE_COLOR)
        l1 = Text("= divergence of E  (how much E spreads from a point)", font_size=24, color=WHITE)
        l2 = Text("= curl of E  (how much E rotates around a point)", font_size=24, color=WHITE)
        l3 = Text("= Laplacian  (3D second spatial derivative)", font_size=24, color=WHITE)
        for x in [r1,r2,r3,l1,l2,l3]: safe_scale(x, max_width=6.0)
        rows = VGroup(r1,r2,r3).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        lbls = VGroup(l1,l2,l3).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        eq_row = VGroup(rows, lbls).arrange(RIGHT, buff=0.5, aligned_edge=UP)
        p3 = VGroup(t3, eq_row).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(p3, max_width=13.0, max_height=4.2)
        p3.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(p3, run_time=0.1))
        self.wait(40)


# ─── VectorCalculusNotation — 4 paragraphs ────────────────────────────────────

class VectorCalculusNotation_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/VectorCalculusNotation_p1.mp3", time_offset=0)
        title = Text("Vector Calculus Notation", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block(["Before writing Maxwell's equations, we need three differential operators."])
        b.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(10)


class VectorCalculusNotation_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/VectorCalculusNotation_p2.mp3", time_offset=0)
        title = Text("Vector Calculus Notation", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym  = MathTex(r"\nabla\cdot\vec{F}", font_size=52, color=E_COLOR)
        nm   = Text("DIVERGENCE", font_size=30, color=E_COLOR, weight=BOLD)
        d1   = Text("Measures how much the field spreads outward from a point.", font_size=26, color=WHITE)
        d2   = Text("Positive = source (field lines radiate out).  Zero = no sources.", font_size=26, color=COMMENT_COLOR)
        for x in [sym,nm,d1,d2]: safe_scale(x, max_width=13.0)
        blk = VGroup(sym,nm,d1,d2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        safe_scale(blk, max_width=13.0, max_height=4.2)
        blk.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(blk, run_time=0.1))
        self.wait(25)


class VectorCalculusNotation_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/VectorCalculusNotation_p3.mp3", time_offset=0)
        title = Text("Vector Calculus Notation", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym  = MathTex(r"\nabla\times\vec{F}", font_size=52, color=B_COLOR)
        nm   = Text("CURL", font_size=30, color=B_COLOR, weight=BOLD)
        d1   = Text("Measures how much the field rotates around a point.", font_size=26, color=WHITE)
        d2   = Text("A paddle wheel in the field spins if curl is nonzero.", font_size=26, color=COMMENT_COLOR)
        for x in [sym,nm,d1,d2]: safe_scale(x, max_width=13.0)
        blk = VGroup(sym,nm,d1,d2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        safe_scale(blk, max_width=13.0, max_height=4.2)
        blk.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(blk, run_time=0.1))
        self.wait(25)


class VectorCalculusNotation_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/VectorCalculusNotation_p4.mp3", time_offset=0)
        title = Text("Vector Calculus Notation", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym  = MathTex(r"\nabla^2 F", font_size=52, color=WAVE_COLOR)
        nm   = Text("LAPLACIAN", font_size=30, color=WAVE_COLOR, weight=BOLD)
        d1   = Text("The 3D generalisation of the second derivative.", font_size=26, color=WHITE)
        d2   = Text("Appears in the EM wave equation in three dimensions.", font_size=26, color=COMMENT_COLOR)
        for x in [sym,nm,d1,d2]: safe_scale(x, max_width=13.0)
        blk = VGroup(sym,nm,d1,d2).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        safe_scale(blk, max_width=13.0, max_height=4.2)
        blk.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(blk, run_time=0.1))
        self.wait(20)


# ─── MaxwellEquations — 7 paragraphs ─────────────────────────────────────────

def maxwell_title():
    t = Text("Maxwell's Equations in Matter", font_size=38, color=GOLD)
    t.to_edge(UP, buff=0.4)
    return t


def law_block(title_mob, latex, name, desc_lines, color):
    law_title = Text(name, font_size=26, color=GOLD)
    law_title.next_to(title_mob, DOWN, buff=0.4)
    eq = MathTex(latex, font_size=44, color=color)
    eq.next_to(law_title, DOWN, buff=0.25)
    safe_scale(eq, max_width=11.0)
    texts = [Text(l, font_size=24, color=WHITE) for l in desc_lines]
    for t in texts: safe_scale(t, max_width=13.0)
    desc = VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    desc.next_to(eq, DOWN, buff=0.28)
    safe_scale(desc, max_width=13.0, max_height=2.5)
    return VGroup(law_title, eq, desc)


class MaxwellEquations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellEquations_p1.mp3", time_offset=0)
        title = maxwell_title(); self.add(title)
        b = txt_block(["Here are Maxwell's four equations in matter."])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1)); self.wait(10)


class MaxwellEquations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellEquations_p2.mp3", time_offset=0)
        title = maxwell_title(); self.add(title)
        blk = law_block(title,
            r"\nabla\cdot\vec{E}=\frac{\rho}{\varepsilon}",
            "GAUSS'S LAW FOR E  (Bennett Eq. 2.5)",
            ["Electric field lines diverge from positive free charges.",
             "Where there are no charges, divergence of E equals zero."], E_COLOR)
        self.play(FadeIn(blk, run_time=0.1)); self.wait(25)


class MaxwellEquations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellEquations_p3.mp3", time_offset=0)
        title = maxwell_title(); self.add(title)
        blk = law_block(title,
            r"\nabla\cdot\vec{B}=0",
            "GAUSS'S LAW FOR B  (Bennett Eq. 2.6)",
            ["The divergence of B is always zero — no magnetic monopoles.",
             "All magnetic field lines form closed loops."], B_COLOR)
        self.play(FadeIn(blk, run_time=0.1)); self.wait(25)


class MaxwellEquations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellEquations_p4.mp3", time_offset=0)
        title = maxwell_title(); self.add(title)
        blk = law_block(title,
            r"\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t}",
            "FARADAY'S LAW  (Bennett Eq. 2.21)",
            ["A time-changing magnetic field induces a curling electric field.",
             "The minus sign (Lenz's law): induced E opposes the change in B."], E_COLOR)
        self.play(FadeIn(blk, run_time=0.1)); self.wait(25)


class MaxwellEquations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellEquations_p5.mp3", time_offset=0)
        title = maxwell_title(); self.add(title)
        blk = law_block(title,
            r"\nabla\times\vec{B}=\mu\vec{J}+\mu\varepsilon\frac{\partial\vec{E}}{\partial t}",
            "AMPERE-MAXWELL LAW  (Bennett Eq. 2.22)",
            ["Both electric currents AND changing E fields create curling B.",
             "Maxwell's displacement current term enables electromagnetic waves."], B_COLOR)
        self.play(FadeIn(blk, run_time=0.1)); self.wait(35)


class MaxwellEquations_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellEquations_p6.mp3", time_offset=0)
        title = maxwell_title(); self.add(title)
        vac = VGroup(
            Text("In vacuum (no charges, no currents):", font_size=26, color=WHITE),
            MathTex(r"\nabla\cdot\vec{E}=0,\quad\nabla\cdot\vec{B}=0", font_size=32, color=E_COLOR),
            MathTex(r"\nabla\times\vec{E}=-\partial\vec{B}/\partial t,\quad\nabla\times\vec{B}=\mu_0\varepsilon_0\partial\vec{E}/\partial t",
                    font_size=28, color=B_COLOR),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        safe_scale(vac, max_width=13.0, max_height=4.0)
        vac.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(vac, run_time=0.1)); self.wait(25)


class MaxwellEquations_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{PARA}/MaxwellEquations_p7.mp3", time_offset=0)
        title = maxwell_title(); self.add(title)
        c_eq = MathTex(r"c=\frac{1}{\sqrt{\varepsilon_0\mu_0}}=2.998\times10^8\text{ m/s}",
                       font_size=46, color=GOLD)
        c_note = Text("Maxwell derived this — not assumed. Light IS an electromagnetic wave.",
                      font_size=26, color=WHITE)
        safe_scale(c_eq); safe_scale(c_note, max_width=13.0)
        c_block = VGroup(c_eq, c_note).arrange(DOWN, buff=0.35)
        c_block.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(c_block, run_time=0.1))
        self.play(Create(gold_box(c_eq)))
        self.wait(30)


# ─── Remaining maxwell scenes (keep as single-scene for now) ─────────────────

class MaxwellVacuum(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{FULL}/MaxwellVacuum.mp3", time_offset=0)
        title = Text("Maxwell's Equations in Vacuum", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4); self.add(title)
        eqs = VGroup(
            MathTex(r"\nabla\cdot\vec{E}=0", font_size=44, color=E_COLOR),
            MathTex(r"\nabla\cdot\vec{B}=0", font_size=44, color=B_COLOR),
            MathTex(r"\nabla\times\vec{E}=-\frac{\partial\vec{B}}{\partial t}", font_size=44, color=E_COLOR),
            MathTex(r"\nabla\times\vec{B}=\mu_0\varepsilon_0\frac{\partial\vec{E}}{\partial t}", font_size=44, color=B_COLOR),
        ).arrange(DOWN, buff=0.35)
        eqs.next_to(title, DOWN, buff=0.5); safe_scale(eqs, max_height=5.0)
        self.play(FadeIn(eqs, run_time=0.1)); self.wait(60)


class EMWaveDerivation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{FULL}/EMWaveDerivation.mp3", time_offset=0)
        title = Text("Deriving the EM Wave Equation", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4); self.add(title)
        solver = StepSolver(self, title, start_buff=0.55)
        solver.add_step(1,
            r"\nabla\times(\nabla\times\vec{E})=-\frac{\partial}{\partial t}(\nabla\times\vec{B})=-\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}",
            "take curl of Faraday, substitute Ampere-Maxwell")
        solver.add_step(2,
            r"\nabla(\nabla\cdot\vec{E})-\nabla^2\vec{E}=-\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}",
            "vector identity: curl(curl) = grad(div) - laplacian")
        solver.add_step(3,
            r"\nabla^2\vec{E}=\mu_0\varepsilon_0\frac{\partial^2\vec{E}}{\partial t^2}\quad\Rightarrow\quad c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}",
            "use div E = 0 in vacuum. EM wave equation!", GOLD)
        solver.finalize(); self.wait(80)


class EMWaveProperties(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{FULL}/EMWaveProperties.mp3", time_offset=0)
        title = Text("Properties of EM Waves", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4); self.add(title)
        props = VGroup(
            txt_block(["Transverse: E and B both perpendicular to propagation direction k"], 26),
            txt_block(["Mutually perpendicular: E x B points along k (right-handed)"], 26),
            txt_block(["Amplitude ratio: E = cB  (in vacuum, from Faraday's law)"], 26),
            txt_block(["In phase: E and B reach maxima simultaneously"], 26),
            txt_block(["In a material: v = c/n,  n = sqrt(K_E) = sqrt(eps/eps0)"], 26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        safe_scale(props, max_width=13.0, max_height=4.5)
        props.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(props, run_time=0.1)); self.wait(60)


class EMWaveExample(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{FULL}/EMWaveExample.mp3", time_offset=0)
        title = Text("Example: Finding B from E", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4); self.add(title)
        E_field = MathTex(r"\vec{E}=E_0\hat{x}\,e^{i(kz-\omega t)}", font_size=46, color=E_COLOR)
        E_field.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(E_field, run_time=0.1))
        solver = StepSolver(self, E_field, start_buff=0.4)
        solver.add_step(1, r"\hat{k}=\hat{z}", "propagation in +z", ANGLE_COLOR)
        solver.add_step(2, r"\vec{B}=\frac{\vec{k}\times\vec{E}}{\omega}", "Faraday for plane waves", B_COLOR)
        solver.add_step(3, r"\hat{z}\times\hat{x}=\hat{y}\;\Rightarrow\;\vec{B}=\frac{E_0}{c}\hat{y}\,e^{i(kz-\omega t)}", "B in y-direction, magnitude E0/c", B_COLOR)
        solver.finalize(); self.wait(50)


class PoyntingIrradiance(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{FULL}/PoyntingIrradiance.mp3", time_offset=0)
        title = Text("Poynting Vector & Irradiance", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4); self.add(title)
        S_eq = MathTex(r"\vec{S}=\frac{1}{\mu_0}\vec{E}\times\vec{B}\quad[\text{W/m}^2]",
                       font_size=46, color=INTENSITY_COLOR)
        I_eq = MathTex(r"I=\langle|\vec{S}|\rangle=\frac{n\varepsilon_0 c}{2}E_0^2\quad[\text{W/m}^2]",
                       font_size=42, color=INTENSITY_COLOR)
        safe_scale(S_eq); safe_scale(I_eq)
        block = VGroup(S_eq, I_eq).arrange(DOWN, buff=0.5)
        block.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(block, run_time=0.1))
        self.play(Create(gold_box(I_eq)))
        self.wait(140)


class RadiationPressure(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{FULL}/RadiationPressure.mp3", time_offset=0)
        title = Text("Radiation Pressure", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4); self.add(title)
        eqs = VGroup(
            labeled_eq(r"P_{\text{abs}}=I/c", "absorbing surface  [Pa]", INTENSITY_COLOR, 48, 26),
            labeled_eq(r"P_{\text{refl}}=2I/c", "reflecting surface — momentum reverses", INTENSITY_COLOR, 48, 26),
        ).arrange(DOWN, buff=0.5)
        eqs.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(eqs, run_time=0.1)); self.wait(60)


class DispersionScene(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound(f"{FULL}/DispersionScene.mp3", time_offset=0)
        title = Text("Dispersion & Index of Refraction", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4); self.add(title)
        n_eq = MathTex(r"n=\frac{c}{v}=\sqrt{K_E}\quad K_E=\frac{\varepsilon}{\varepsilon_0}",
                       font_size=46, color=N_COLOR)
        vg_eq = MathTex(r"v_g=\frac{c}{n+\omega\,dn/d\omega}", font_size=42, color=WAVE_COLOR)
        desc = txt_block([
            "Normal dispersion: n increases with frequency — violet bends more than red.",
            "Anomalous dispersion: near absorption resonances, n decreases with frequency.",
            "Group velocity can appear to exceed c, but no information travels faster than c.",
        ], fs=25)
        safe_scale(n_eq); safe_scale(vg_eq)
        block = VGroup(n_eq, vg_eq, desc).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(block, max_width=13.0, max_height=4.5)
        block.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(block, run_time=0.1)); self.wait(115)

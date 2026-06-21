"""
scene_generator.py — generates all paragraph-split scene files
Run: python scene_generator.py
"""
from pathlib import Path
import re

BASE  = Path('/home/claude/Optics-Video')
NARR  = BASE / 'narration'
PARA  = BASE / 'narration/paragraphs'
AUDIO = 'narration/audio'
PAUDIO = 'narration/audio/paragraphs'

# ── helpers ──────────────────────────────────────────────────────────────────
def get_paras(scene):
    f = NARR / f'{scene}.txt'
    if not f.exists(): return []
    return [p.strip() for p in f.read_text(encoding='utf-8').split('\n\n') if p.strip()]

def wrap(text, width=64):
    """Wrap text into lines of at most width chars, return as list of strings."""
    words = text.split()
    lines, cur = [], []
    for w in words:
        cur.append(w)
        if len(' '.join(cur)) > width:
            if len(cur) > 1:
                lines.append(' '.join(cur[:-1]))
                cur = [w]
    if cur: lines.append(' '.join(cur))
    return lines[:5]  # max 5 lines

def lines_repr(para, indent=12):
    sp = ' ' * indent
    ls = wrap(para)
    return ',\n'.join(f'{sp}"{l}"' for l in ls)

# ── scene templates ──────────────────────────────────────────────────────────
def make_text_scene(scene, pidx, para, title, title_fs=40, extra_code=''):
    """Pure text paragraph scene."""
    cn = f'{scene}_p{pidx+1}'
    return f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{title}", font_size={title_fs}, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
{extra_code}        b = txt_block([
{lines_repr(para)},
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

def make_eq_scene(scene, pidx, para, title, title_fs, latex, eq_color='WHITE', extra_after=''):
    """Equation + explanation paragraph scene."""
    cn = f'{scene}_p{pidx+1}'
    return f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{title}", font_size={title_fs}, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"{latex}", font_size=44, color={eq_color})
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(eq, run_time=0.1))
        b = txt_block([
{lines_repr(para)},
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

# ── WEEK 1 WAVES ─────────────────────────────────────────────────────────────
def gen_week1_waves():
    out = '''# week1_waves.py — Week 1: Waves (paragraph-per-scene, zero overlap)
from manim import *
from utils import *
'''
    TITLE = "Waves, Wave Equation & Complex Representation"

    # ── Week1TitleCard ────────────────────────────────────────────────────────
    paras = get_paras('Week1TitleCard')
    for i, p in enumerate(paras):
        cn = f'Week1TitleCard_p{i+1}'
        out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        card = make_title_card("WEEK 1", "Waves, Wave Equation & Complex Representation",
                               "Bennett Ch. 1 & 2.1-2.3")
        self.play(FadeIn(card, run_time=0.3))
        b = txt_block([
{lines_repr(p)},
        ])
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

    # ── WaveIntroduction ──────────────────────────────────────────────────────
    paras = get_paras('WaveIntroduction')
    T = "What Is a Wave?"
    for i, p in enumerate(paras):
        out += make_text_scene('WaveIntroduction', i, p, T, 42)

    # ── WaveEquation1D ────────────────────────────────────────────────────────
    paras = get_paras('WaveEquation1D')
    T = "The 1D Wave Equation"
    EQ = r'\frac{\partial^2\Psi}{\partial x^2}=\frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2}'

    # p1: show equation, explain structure
    cn = 'WaveEquation1D_p1'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"{EQ}", font_size=52)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(gold_box(eq)))
        b = txt_block([
{lines_repr(paras[0])},
        ])
        b.next_to(eq, DOWN, buff=0.4)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

    # p2: left side
    cn = 'WaveEquation1D_p2'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        lhs = MathTex(r"\frac{{\partial^2\Psi}}{{\partial x^2}}", font_size=56, color=E_COLOR)
        lhs.next_to(title, DOWN, buff=0.45)
        lbl = Text("LEFT SIDE: spatial curvature of the wave", font_size=28, color=E_COLOR, weight=BOLD)
        safe_scale(lbl, max_width=13.0)
        lbl.next_to(lhs, DOWN, buff=0.3)
        b = txt_block([
{lines_repr(paras[1])},
        ])
        b.next_to(lbl, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(lhs, lbl, b), run_time=0.1))
        self.wait(1)
'''

    # p3: right side
    cn = 'WaveEquation1D_p3'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=42, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        rhs = MathTex(r"\frac{{1}}{{v^2}}\frac{{\partial^2\Psi}}{{\partial t^2}}", font_size=56, color=B_COLOR)
        rhs.next_to(title, DOWN, buff=0.45)
        lbl = Text("RIGHT SIDE: temporal acceleration / v squared", font_size=28, color=B_COLOR, weight=BOLD)
        safe_scale(lbl, max_width=13.0)
        lbl.next_to(rhs, DOWN, buff=0.3)
        b = txt_block([
{lines_repr(paras[2])},
        ])
        b.next_to(lbl, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(rhs, lbl, b), run_time=0.1))
        self.wait(1)
'''

    # p4-p6: text scenes
    for i in range(3, 6):
        out += make_text_scene('WaveEquation1D', i, paras[i], T, 42)

    # ── WaveEquationProof ────────────────────────────────────────────────────
    paras = get_paras('WaveEquationProof')
    T = "Proof: f(x-vt) Satisfies the Wave Equation"

    cn = 'WaveEquationProof_p1'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
{lines_repr(paras[0])},
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

    cn = 'WaveEquationProof_p2'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        s1 = labeled_eq(r"\partial^2\Psi/\partial x^2 = 2", "second x-derivative = 2", E_COLOR, 40, 24)
        s2 = labeled_eq(r"\partial^2\Psi/\partial t^2 = 2v^2", "second t-derivative = 2v squared", B_COLOR, 40, 24)
        s3 = labeled_eq(r"\\frac{{1}}{{v^2}}\\cdot 2v^2 = 2 = \\partial^2\\Psi/\\partial x^2\\;\\checkmark",
                        "LHS = RHS — wave equation satisfied!", GOLD, 36, 24)
        steps = VGroup(s1, s2, s3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        safe_scale(steps, max_width=13.0, max_height=4.5)
        steps.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(steps, run_time=0.1))
        self.wait(1)
'''

    cn = 'WaveEquationProof_p3'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
{lines_repr(paras[2])},
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

    # ── HarmonicWave (14 paras) ───────────────────────────────────────────────
    paras = get_paras('HarmonicWave')
    T = "Harmonic Traveling Waves"
    EQ_HARM = r'\Psi(x,t) = A\sin(kx - \omega t + \phi)'

    # p1: intro text
    out += make_text_scene('HarmonicWave', 0, paras[0], T, 40)

    # p2: show the equation
    cn = 'HarmonicWave_p2'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"{EQ_HARM}", font_size=52, color=E_COLOR)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(gold_box(eq)))
        self.wait(1)
'''

    # p3-p10: one symbol per paragraph
    symbols = [
        (r'A', 'AMPLITUDE', 'max displacement  [V/m for E-field]', 'INTENSITY_COLOR'),
        (r'k = 2\pi/\lambda', 'WAVE NUMBER', 'spatial frequency  [rad/m]', 'WAVE_COLOR'),
        (r'\omega = 2\pi f = 2\pi/T', 'ANGULAR FREQUENCY', '[rad/s]', 'WAVE_COLOR'),
        (r'\lambda', 'WAVELENGTH', 'distance between crests  [m]', 'WAVE_COLOR'),
        (r'f = 1/T', 'FREQUENCY', 'cycles per second  [Hz]', 'WAVE_COLOR'),
        (r'v = \omega/k = f\lambda', 'PHASE SPEED', 'speed of crests  [m/s]', 'WAVE_COLOR'),
        (r'\phi', 'INITIAL PHASE', 'shifts wave in time  [rad]', 'WHITE'),
    ]
    for idx, (latex, name, desc, color) in enumerate(symbols):
        cn = f'HarmonicWave_p{idx+3}'
        out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sym = MathTex(r"{latex}", font_size=56, color={color})
        safe_scale(sym, max_width=13.0)
        sym.next_to(title, DOWN, buff=0.45)
        nm = Text("{name}", font_size=30, color={color}, weight=BOLD)
        nm.next_to(sym, DOWN, buff=0.2)
        dd = Text("{desc}", font_size=26, color=WHITE)
        safe_scale(dd, max_width=13.0)
        dd.next_to(nm, DOWN, buff=0.2)
        b = txt_block([
{lines_repr(paras[idx+2])},
        ])
        b.next_to(dd, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(sym, nm, dd, b), run_time=0.1))
        self.wait(1)
'''

    # p10: key relations
    cn = 'HarmonicWave_p10'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        hdr = Text("Key Relations — MEMORISE", font_size=28, color=GOLD)
        hdr.next_to(title, DOWN, buff=0.4)
        rels = MathTex(r"v = f\lambda = \frac{{\omega}}{{k}}\qquad k=\frac{{2\pi}}{{\lambda}}\qquad \omega=2\pi f\qquad T=\frac{{1}}{{f}}", font_size=38)
        safe_scale(rels, max_width=13.0)
        rels.next_to(hdr, DOWN, buff=0.3)
        b = txt_block([
{lines_repr(paras[9])},
        ])
        b.next_to(rels, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(hdr, rels, b), run_time=0.1))
        self.wait(1)
'''

    # p11-p14: example calculation
    for i in range(10, 14):
        out += make_text_scene('HarmonicWave', i, paras[i], T, 40)

    # ── HarmonicWaveExample ───────────────────────────────────────────────────
    paras = get_paras('HarmonicWaveExample')
    T = "Example: Green Laser (lambda = 532 nm)"

    cn = 'HarmonicWaveExample_p1'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = txt_block([
{lines_repr(paras[0])},
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

    cn = 'HarmonicWaveExample_p2'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        steps = VGroup(
            labeled_eq(r"k=2\pi/(532\times10^{{-9}})=1.18\times10^7\,\\text{{rad/m}}", "wave number", WAVE_COLOR, 34, 22),
            labeled_eq(r"f=c/\lambda=5.64\times10^{{14}}\,\\text{{Hz}}", "frequency (564 THz)", WAVE_COLOR, 34, 22),
            labeled_eq(r"\omega=2\pi f=3.54\times10^{{15}}\,\\text{{rad/s}}", "angular frequency", WAVE_COLOR, 34, 22),
            labeled_eq(r"T=1/f=1.77\\times10^{{-15}}\,\\text{{s}}=1.77\\,\\text{{fs}}", "period (femtoseconds!)", GOLD, 34, 22),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        safe_scale(steps, max_width=13.0, max_height=4.8)
        steps.next_to(title, DOWN, buff=0.45)
        self.play(FadeIn(steps, run_time=0.1))
        self.wait(1)
'''

    out += make_text_scene('HarmonicWaveExample', 2, paras[2], T, 36)

    # ── SuperpositionPrinciple ────────────────────────────────────────────────
    paras = get_paras('SuperpositionPrinciple')
    T = "The Principle of Superposition"

    out += make_text_scene('SuperpositionPrinciple', 0, paras[0], T, 38)

    cn = 'SuperpositionPrinciple_p2'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=38, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        proof = MathTex(
            r"\\frac{{\\partial^2(\\Psi_1+\\Psi_2)}}{{\\partial x^2}}"
            r"=\\frac{{\\partial^2\\Psi_1}}{{\\partial x^2}}+\\frac{{\\partial^2\\Psi_2}}{{\\partial x^2}}"
            r"=\\frac{{1}}{{v^2}}\\frac{{\\partial^2(\\Psi_1+\\Psi_2)}}{{\\partial t^2}}\\;\\checkmark",
            font_size=32)
        safe_scale(proof, max_width=13.0)
        proof.next_to(title, DOWN, buff=0.45)
        b = txt_block([
{lines_repr(paras[1])},
        ])
        b.next_to(proof, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(proof, b), run_time=0.1))
        self.wait(1)
'''

    out += make_text_scene('SuperpositionPrinciple', 2, paras[2], T, 38)

    # ── PhaseGroupVelocity (10 paras) ─────────────────────────────────────────
    paras = get_paras('PhaseGroupVelocity')
    T = "Phase Velocity and Group Velocity"

    out += make_text_scene('PhaseGroupVelocity', 0, paras[0], T, 36)

    cn = 'PhaseGroupVelocity_p2'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = labeled_eq(r"v_p = \\omega/k", "PHASE VELOCITY — speed of wave crests  [m/s]", WAVE_COLOR, 52, 28)
        eq.next_to(title, DOWN, buff=0.5)
        b = txt_block([
{lines_repr(paras[1])},
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)
'''

    cn = 'PhaseGroupVelocity_p3'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = labeled_eq(r"v_g = d\\omega/dk", "GROUP VELOCITY — speed of energy and information  [m/s]", WAVE_COLOR, 52, 28)
        eq.next_to(title, DOWN, buff=0.5)
        b = txt_block([
{lines_repr(paras[2])},
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)
'''

    for i in range(3, 10):
        out += make_text_scene('PhaseGroupVelocity', i, paras[i], T, 36)

    # ── ComplexRepresentation (8 paras) ───────────────────────────────────────
    paras = get_paras('ComplexRepresentation')
    T = "Complex Representation of Waves"

    out += make_text_scene('ComplexRepresentation', 0, paras[0], T, 36)

    cn = 'ComplexRepresentation_p2'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"e^{{i\\theta}} = \\cos\\theta + i\\sin\\theta", font_size=60, color=GOLD)
        safe_scale(eq)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(eq, run_time=0.1))
        self.play(Create(gold_box(eq)))
        b = txt_block([
{lines_repr(paras[1])},
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

    cn = 'ComplexRepresentation_p3'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eqs = VGroup(
            labeled_eq(r"\\cos\\theta = \\mathrm{{Re}}[e^{{i\\theta}}]", "cosine = real part", WHITE, 40, 24),
            labeled_eq(r"\\sin\\theta = \\mathrm{{Im}}[e^{{i\\theta}}]", "sine = imaginary part", WHITE, 40, 24),
        ).arrange(DOWN, buff=0.4)
        eqs.next_to(title, DOWN, buff=0.5)
        b = txt_block([
{lines_repr(paras[2])},
        ])
        b.next_to(eqs, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eqs, b), run_time=0.1))
        self.wait(1)
'''

    cn = 'ComplexRepresentation_p4'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        cw = MathTex(r"\\tilde{{\\Psi}} = A\\,e^{{i(kx-\\omega t+\\phi)}}", font_size=50, color=E_COLOR)
        safe_scale(cw)
        cw.next_to(title, DOWN, buff=0.45)
        rule = MathTex(r"\\Psi_{{\\rm phys}} = \\mathrm{{Re}}[\\tilde{{\\Psi}}] = A\\cos(kx-\\omega t+\\phi)", font_size=34)
        safe_scale(rule, max_width=13.0)
        rule.next_to(cw, DOWN, buff=0.25)
        b = txt_block([
{lines_repr(paras[3])},
        ])
        b.next_to(rule, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(cw, rule, b), run_time=0.1))
        self.wait(1)
'''

    for i in range(4, 8):
        out += make_text_scene('ComplexRepresentation', i, paras[i], T, 36)

    # ── ThreeDWaves ───────────────────────────────────────────────────────────
    paras = get_paras('ThreeDWaves')
    T = "3D Plane Waves and Spherical Waves"

    cn = 'ThreeDWaves_p1'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        pw = MathTex(r"\\tilde{{\\Psi}}(\\mathbf{{r}},t)=A\\,e^{{i(\\mathbf{{k}}\\cdot\\mathbf{{r}}-\\omega t)}}", font_size=50, color=E_COLOR)
        safe_scale(pw)
        pw.next_to(title, DOWN, buff=0.45)
        sym = eq_table([
            (r"\\mathbf{{k}}", "wave vector — points in propagation direction", WAVE_COLOR),
            (r"|\\mathbf{{k}}|=k=2\\pi/\\lambda", "magnitude = wave number", WAVE_COLOR),
        ], eq_fs=30, lbl_fs=22, buff=0.22)
        sym.next_to(pw, DOWN, buff=0.35)
        b = txt_block([
{lines_repr(paras[0])},
        ])
        b.next_to(sym, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(pw, sym, b), run_time=0.1))
        self.wait(1)
'''

    out += make_text_scene('ThreeDWaves', 1, paras[1], T, 36)

    cn = 'ThreeDWaves_p3'
    out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        sw = labeled_eq(r"\\tilde{{\\Psi}}(r,t)=\\frac{{A}}{{r}}e^{{i(kr-\\omega t)}}",
                        "amplitude = A/r  →  intensity falls as 1/r squared", B_COLOR, 46, 25)
        sw.next_to(title, DOWN, buff=0.5)
        b = txt_block([
{lines_repr(paras[2])},
        ])
        b.next_to(sw, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(sw, b), run_time=0.1))
        self.wait(1)
'''

    # ── Week1WavesSummary ─────────────────────────────────────────────────────
    paras = get_paras('Week1WavesSummary')
    T = "Week 1 Summary — Key Equations"
    rows = [
        (r"\partial^2\Psi/\partial x^2=(1/v^2)\partial^2\Psi/\partial t^2", "wave equation", "GOLD"),
        (r"v=f\lambda=\omega/k,\;k=2\pi/\lambda,\;\omega=2\pi f", "harmonic wave relations", "WAVE_COLOR"),
        (r"\tilde\Psi=Ae^{i(kx-\omega t)},\;|\tilde\Psi|^2=A^2", "complex representation", "E_COLOR"),
    ]
    out += make_text_scene('Week1WavesSummary', 0, paras[0], T, 40)
    for i, (latex, lbl, color) in enumerate(rows):
        cn = f'Week1WavesSummary_p{i+2}'
        out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)
        title = Text("{T}", font_size=40, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = labeled_eq(r"{latex}", "{lbl}", {color}, 34, 24)
        eq.next_to(title, DOWN, buff=0.5)
        b = txt_block([
{lines_repr(paras[i+1])},
        ])
        b.next_to(eq, DOWN, buff=0.35)
        self.play(FadeIn(VGroup(eq, b), run_time=0.1))
        self.wait(1)
'''

    return out

# Write week1_waves.py
code = gen_week1_waves()
(BASE / 'week1_waves.py').write_text(code, encoding='utf-8')
print(f"week1_waves.py: {len(code.splitlines())} lines")

import ast
try:
    ast.parse(code)
    print("  syntax OK")
except SyntaxError as e:
    print(f"  SYNTAX ERROR line {e.lineno}: {e.msg}")

# ── WEEK 1 MAXWELL ────────────────────────────────────────────────────────────
def gen_week1_maxwell():
    out = '''# week1_maxwell.py — Week 1: Maxwell's Equations (paragraph-per-scene)
from manim import *
from utils import *
PARA = "narration/audio/paragraphs"
FULL = "narration/audio"
'''
    # Keep the existing paragraph scenes for MaxwellIntro, VectorCalc, MaxwellEquations
    existing = (BASE / 'week1_maxwell.py').read_text(encoding='utf-8')
    # Extract classes MaxwellIntro_p*, VectorCalculusNotation_p*, MaxwellEquations_p*
    existing_classes = re.findall(r'\nclass (Maxwell(?:Intro|Equations|Vacuum)|VectorCalculus\w*)\w*\(Scene\):.*?(?=\nclass |\Z)',
                                   existing, re.DOTALL)

    # Just keep the file as-is but add paragraph scenes for remaining scenes
    out = existing  # start with existing file

    def add_para_scenes(scene, title, title_fs=38, special_paras=None):
        nonlocal out
        paras = get_paras(scene)
        if not paras: return
        for i, p in enumerate(paras):
            cn = f'{scene}_p{i+1}'
            if f'class {cn}(Scene):' in out: continue  # already exists
            extra = special_paras.get(i, '') if special_paras else ''
            out += f'''
class {cn}(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/{cn}.mp3", time_offset=0)
        title = Text("{title}", font_size={title_fs}, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
{extra}        b = txt_block([
{lines_repr(p)},
        ])
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)
'''

    add_para_scenes('MaxwellVacuum', "Maxwell's Equations in Vacuum", 36)
    add_para_scenes('EMWaveDerivation', "Deriving the EM Wave Equation", 36)
    add_para_scenes('EMWaveProperties', "Properties of EM Waves", 38)
    add_para_scenes('EMWaveExample', "Example: Finding B from E", 38)
    add_para_scenes('PoyntingIrradiance', "Poynting Vector and Irradiance", 36)
    add_para_scenes('RadiationPressure', "Radiation Pressure", 40)
    add_para_scenes('DispersionScene', "Dispersion and Refractive Index", 36)

    return out

code = gen_week1_maxwell()
(BASE / 'week1_maxwell.py').write_text(code, encoding='utf-8')
import ast
try:
    ast.parse(code)
    print(f"week1_maxwell.py: {len(code.splitlines())} lines — OK")
except SyntaxError as e:
    print(f"week1_maxwell.py ERROR line {e.lineno}: {e.msg}")

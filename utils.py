# utils.py  —  31OPT Optics Manim Video Series  (v2 — layout-safe)
from manim import *

# ── Colour palette ────────────────────────────────────────────────────────────
E_COLOR         = "#58C4DD"   # electric field
B_COLOR         = "#FC6255"   # magnetic field
N_COLOR         = "#83C167"   # refractive index
ANGLE_COLOR     = "#FFFF00"   # angles
WAVE_COLOR      = "#9B59B6"   # wave quantities k, omega, lambda
INTENSITY_COLOR = "#FF9F40"   # energy / intensity
GOLD            = "#FFD700"   # highlights, boxes, answers
COMMENT_COLOR   = "#AAAAAA"   # grey annotation text

# ── Screen constants ──────────────────────────────────────────────────────────
SW = 14.2          # full scene width  (manim default)
SH = 8.0           # full scene height
TITLE_H  = 3.4     # y-position of top-edge title
BODY_TOP = 2.7     # y at which body content starts (below title)
BODY_BOT = -3.5    # y at which body content must end (above bottom)
SAFE_H   = BODY_TOP - BODY_BOT   # 6.2 units of safe vertical space

BG_COLOR = "#0f0f0f"


# ── Safe layout helpers ───────────────────────────────────────────────────────
def safe_scale(mob: Mobject, max_width: float = 13.0, max_height: float = 5.8) -> Mobject:
    """Scale a mobject down if it exceeds safe screen dimensions."""
    w = mob.width
    h = mob.height
    if w > max_width:
        mob.scale(max_width / w)
    if mob.height > max_height:
        mob.scale(max_height / mob.height)
    return mob


def place_below(mob: Mobject, ref: Mobject, buff: float = 0.35) -> Mobject:
    """Position mob below ref with buff, then clamp to bottom of safe area."""
    mob.next_to(ref, DOWN, buff=buff)
    # clamp: if bottom edge goes below safe zone, shift up
    bottom = mob.get_bottom()[1]
    if bottom < BODY_BOT:
        mob.shift(UP * (BODY_BOT - bottom + 0.05))
    return mob


def stacked_group(*mobs, buff: float = 0.30) -> VGroup:
    """Return a VGroup arranged vertically, each auto-scaled."""
    for m in mobs:
        safe_scale(m)
    g = VGroup(*mobs)
    g.arrange(DOWN, aligned_edge=LEFT, buff=buff)
    safe_scale(g, max_height=SAFE_H)
    return g


# ── Title card ────────────────────────────────────────────────────────────────
def make_title_card(week_str: str, topic_str: str, ref_str: str) -> VGroup:
    week_label  = Text(week_str,  font_size=40, color=GOLD)
    topic_label = Text(topic_str, font_size=52, color=WHITE)
    ref_label   = Text(ref_str,   font_size=26, color=GRAY)
    g = VGroup(week_label, topic_label, ref_label).arrange(DOWN, buff=0.45)
    safe_scale(g)
    return g


# ── Section intro ─────────────────────────────────────────────────────────────
def section_intro(lines: list, font_size: int = 28) -> VGroup:
    texts = [Text(line, font_size=font_size, color=WHITE) for line in lines]
    g = VGroup(*texts)
    g.arrange(DOWN, aligned_edge=LEFT, buff=0.22)
    safe_scale(g, max_width=12.5, max_height=5.5)
    return g


# ── Equation with label ───────────────────────────────────────────────────────
def labeled_eq(latex: str, label: str, eq_color=WHITE,
               eq_fs: int = 38, lbl_fs: int = 24) -> VGroup:
    """One MathTex equation + small grey label below it."""
    eq  = MathTex(latex, font_size=eq_fs, color=eq_color)
    lbl = Text(label, font_size=lbl_fs, color=COMMENT_COLOR)
    g   = VGroup(eq, lbl).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
    safe_scale(g)
    return g


# ── Equation table ────────────────────────────────────────────────────────────
def eq_table(rows: list, eq_fs: int = 32, lbl_fs: int = 22,
             buff: float = 0.28) -> VGroup:
    """
    rows = list of (latex_str, label_str, color) tuples.
    Returns a VGroup of labeled equations arranged vertically.
    """
    items = VGroup()
    for latex, label, color in rows:
        eq  = MathTex(latex, font_size=eq_fs, color=color)
        lbl = Text(label, font_size=lbl_fs, color=COMMENT_COLOR)
        row = VGroup(eq, lbl).arrange(RIGHT, buff=0.4)
        items.add(row)
    items.arrange(DOWN, aligned_edge=LEFT, buff=buff)
    safe_scale(items, max_height=SAFE_H)
    return items


# ── Boxes and labels ──────────────────────────────────────────────────────────
def gold_box(mob: Mobject) -> SurroundingRectangle:
    return SurroundingRectangle(mob, color=GOLD, buff=0.12)


def step_label(n: int) -> Text:
    return Text(f"Step {n}:", font_size=28, color=GOLD)


def part_label(s: str) -> Text:
    return Text(s, font_size=30, color=GOLD)


# ── Equation summary card ─────────────────────────────────────────────────────
def equation_summary_card(title_str: str, bullets: list) -> VGroup:
    title = Text(title_str, font_size=36, color=GOLD)
    items = VGroup()
    for b in bullets[:3]:
        dot = Text("•", font_size=30, color=GOLD)
        eq  = MathTex(b, font_size=32, color=WHITE)
        row = VGroup(dot, eq).arrange(RIGHT, buff=0.2)
        items.add(row)
    items.arrange(DOWN, aligned_edge=LEFT, buff=0.28)
    g = VGroup(title, items).arrange(DOWN, buff=0.4)
    safe_scale(g)
    return g


# ── Step-by-step solution builder ────────────────────────────────────────────
class StepSolver:
    """
    Helper that manages step-by-step solutions on screen.
    Automatically pages when running out of vertical space.
    Usage:
        solver = StepSolver(scene, ref_mob)
        solver.add_step(1, r"equation", "optional text annotation")
        solver.finalize()   # box last step in gold
    """
    def __init__(self, scene, ref: Mobject, start_buff: float = 0.35):
        self.scene = scene
        self.ref   = ref
        self.buff  = start_buff
        self.steps: list[VGroup] = []
        self.current_page_mobs: list[Mobject] = []
        self._y_used = 0.0

    def add_step(self, n: int, latex: str, annotation: str = "",
                 color=WHITE, fs: int = 34):
        lbl = step_label(n)
        eq  = MathTex(latex, font_size=fs, color=color)
        safe_scale(eq, max_width=12.0)
        if annotation:
            ann = Text(annotation, font_size=24, color=COMMENT_COLOR)
            block = VGroup(VGroup(lbl, eq).arrange(RIGHT, buff=0.25), ann)
            block.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        else:
            block = VGroup(lbl, eq).arrange(RIGHT, buff=0.25)
        safe_scale(block, max_width=13.0)

        # check if fits
        needed = block.height + self.buff
        if self._y_used + needed > SAFE_H - 0.5 and self.current_page_mobs:
            self._flush_page()

        if self.current_page_mobs:
            block.next_to(self.current_page_mobs[-1], DOWN,
                          buff=self.buff, aligned_edge=LEFT)
        else:
            block.next_to(self.ref, DOWN, buff=self.buff, aligned_edge=LEFT)

        self._y_used += needed
        self.current_page_mobs.append(block)
        self.steps.append(block)
        self.scene.play(Write(block), run_time=1.1)
        self.scene.wait(0.8)

    def _flush_page(self):
        self.scene.wait(1.0)
        self.scene.play(FadeOut(VGroup(*self.current_page_mobs)))
        self.current_page_mobs = []
        self._y_used = 0.0

    def finalize(self):
        if self.steps:
            last = self.steps[-1]
            self.scene.play(Create(gold_box(last)))
            self.scene.wait(2)

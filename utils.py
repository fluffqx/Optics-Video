# utils.py
# 31OPT Optics — Shared utilities for the Manim video series
from manim import *

# ── Colour palette ────────────────────────────────────────────────────────────
E_COLOR         = "#58C4DD"   # electric field quantities
B_COLOR         = "#FC6255"   # magnetic field quantities
N_COLOR         = "#83C167"   # refractive index
ANGLE_COLOR     = "#FFFF00"   # angles
WAVE_COLOR      = "#9B59B6"   # wave quantities k, omega, lambda
INTENSITY_COLOR = "#FF9F40"   # energy / intensity
GOLD            = "#FFD700"   # highlights, boxes, answers


# ── Title card ────────────────────────────────────────────────────────────────
def make_title_card(week_str: str, topic_str: str, ref_str: str) -> VGroup:
    """Full-screen title card with week, topic and textbook reference."""
    week_label  = Text(week_str,  font_size=36, color=GOLD)
    topic_label = Text(topic_str, font_size=48, color=WHITE)
    ref_label   = Text(ref_str,   font_size=24, color=GRAY)
    group = VGroup(week_label, topic_label, ref_label).arrange(DOWN, buff=0.4)
    return group


# ── Section introduction block ────────────────────────────────────────────────
def section_intro(lines: list, font_size: int = 30) -> VGroup:
    """Returns a VGroup of Text lines for a topic introduction paragraph."""
    texts = [Text(line, font_size=font_size, color=WHITE) for line in lines]
    return VGroup(*texts).arrange(DOWN, aligned_edge=LEFT, buff=0.2)


# ── Helpers ───────────────────────────────────────────────────────────────────
def gold_box(mobject: Mobject) -> SurroundingRectangle:
    """Returns a gold SurroundingRectangle around a mobject."""
    return SurroundingRectangle(mobject, color=GOLD, buff=0.15)


def step_label(n: int) -> Text:
    """Returns a small step label 'Step N:'."""
    return Text(f"Step {n}:", font_size=26, color=GOLD)


def equation_summary_card(title_str: str, bullets: list) -> VGroup:
    """
    Returns a VGroup with a title and up to 3 bullet MathTex equations.
    bullets: list of raw LaTeX strings.
    """
    title = Text(title_str, font_size=34, color=GOLD)
    items = VGroup()
    for b in bullets[:3]:
        dot   = Text("•", font_size=28, color=GOLD)
        eq    = MathTex(b, font_size=34, color=WHITE)
        row   = VGroup(dot, eq).arrange(RIGHT, buff=0.2)
        items.add(row)
    items.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
    return VGroup(title, items).arrange(DOWN, buff=0.4)

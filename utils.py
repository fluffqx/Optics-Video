from manim import *

BG_COLOR   = "#0D1117"
GOLD       = "#F0C040"
TEAL       = "#4ECDC4"
WAVE_COLOR = TEAL
BLUE_LIGHT = "#89CFF0"
GRAY_DIM   = "#444455"

def safe_scale(mob, max_width=13.0, max_height=6.0):
    w, h = mob.width, mob.height
    s = 1.0
    if w > max_width:  s = min(s, max_width / w)
    if h > max_height: s = min(s, max_height / h)
    if s < 1.0: mob.scale(s)
    return mob

def make_title_card(week_label, topic, reference):
    """Polished title card with decorative line."""
    wk = Text(week_label, font_size=56, color=GOLD, weight=BOLD)
    line = Line(LEFT * 5, RIGHT * 5, color=GOLD, stroke_width=1.5).set_opacity(0.5)
    tp = Text(topic, font_size=30, color=WHITE)
    rf = Text(reference, font_size=20, color=GRAY)
    safe_scale(tp, max_width=13.0)
    return VGroup(wk, line, tp, rf).arrange(DOWN, buff=0.4).move_to(ORIGIN)

def scene_title(text, font_size=34):
    """Consistent scene title at top edge."""
    t = Text(text, font_size=font_size, color=GOLD)
    safe_scale(t, max_width=13.5)
    t.to_edge(UP, buff=0.3)
    return t

def equation_with_caption(latex, caption, title_mob, font_size=52):
    """Vertically centred equation + teal caption below title."""
    eq = MathTex(latex, font_size=font_size)
    safe_scale(eq, max_width=12.5)
    cap = Text(caption, font_size=26, color=TEAL)
    safe_scale(cap, max_width=12.5)
    group = VGroup(eq, cap).arrange(DOWN, buff=0.35)
    t_bot = title_mob.get_bottom()[1]
    group.move_to([0, (t_bot + (-3.8)) / 2, 0])
    safe_scale(group, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
    return group

def text_caption(caption, title_mob, font_size=30):
    """Centred white text for no-equation slides."""
    cap = Text(caption, font_size=font_size, color=WHITE)
    safe_scale(cap, max_width=12.5)
    t_bot = title_mob.get_bottom()[1]
    cap.move_to([0, (t_bot + (-3.8)) / 2, 0])
    return cap

def bottom_rule():
    """Thin gold decorative rule at bottom of screen."""
    return Line(LEFT*6.5, RIGHT*6.5, color=GOLD, stroke_width=0.8).set_opacity(0.3).to_edge(DOWN, buff=0.15)

def week_badge(n, color=GOLD):
    """Small week number badge for title cards."""
    circle = Circle(radius=0.45, color=color, fill_opacity=0).set_stroke(color, width=2)
    label = Text(str(n), font_size=28, color=color, weight=BOLD)
    return VGroup(circle, label)

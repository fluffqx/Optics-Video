from manim import *

BG_COLOR  = "#0D1117"
GOLD      = "#F0C040"
TEAL      = "#4ECDC4"
WAVE_COLOR = TEAL

def safe_scale(mob, max_width=13.0, max_height=6.0):
    w, h = mob.width, mob.height
    s = 1.0
    if w > max_width:  s = min(s, max_width / w)
    if h > max_height: s = min(s, max_height / h)
    if s < 1.0: mob.scale(s)
    return mob

def make_title_card(week_label, topic, reference):
    wk = Text(week_label, font_size=52, color=GOLD, weight=BOLD)
    tp = Text(topic, font_size=32, color=WHITE)
    rf = Text(reference, font_size=22, color=GRAY)
    safe_scale(tp, max_width=13.0)
    return VGroup(wk, tp, rf).arrange(DOWN, buff=0.45).move_to(ORIGIN)

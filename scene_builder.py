"""
scene_builder.py — builds visually clean Manim scenes.

DESIGN RULES (from 3Blue1Brown / Khan Academy style):
1. Title at top in GOLD — always present, always readable
2. Main content (equation + caption) centered vertically in remaining space
3. Equation font 52 for main results, 40 for secondary
4. Caption 26px in WAVE_COLOR — brief, max 65 chars
5. Never have empty space > 30% of screen
6. No text walls — screen only shows the KEY VISUAL for that paragraph
7. Color: GOLD=title/key result box, WHITE=equation default, WAVE_COLOR=caption
8. All content safe_scaled to max_width=13.0
"""

from pathlib import Path

NARR = Path('narration')
PAUDIO = 'narration/audio/paragraphs'


def get_paras(scene: str):
    f = NARR / f'{scene}.txt'
    if not f.exists():
        return []
    return [p.strip() for p in f.read_text(encoding='utf-8').split('\n\n') if p.strip()]


def _e(s: str) -> str:
    """Escape for Python string inside double quotes."""
    return s.replace('\\', '\\\\').replace('"', '\\"')


def build_scene(scene: str, pidx: int, latex_or_none, caption: str,
                title: str, title_fs: int,
                is_titlecard: bool = False, week=None, subtitle=None, ref=None,
                highlight_box: bool = False) -> str:
    """
    Generate one Manim Scene class.

    Layout logic:
    - Title pinned to TOP edge
    - Content group (eq + caption OR just caption) vertically centered
      in the space below the title  →  no empty bottom gap
    """
    cn = f'{scene}_p{pidx + 1}'
    cap = _e(caption)
    ttl = _e(title)

    # ── header lines ────────────────────────────────────────────────────────
    lines = [
        f'class {cn}(Scene):',
        f'    def construct(self):',
        f'        self.camera.background_color = BG_COLOR',
        f'        self.add_sound("{PAUDIO}/{cn}.mp3", time_offset=0)',
    ]

    # ── title card (week opener) ─────────────────────────────────────────────
    if is_titlecard:
        lines += [
            f'        card = make_title_card("WEEK {week}", "{_e(subtitle)}", "{_e(ref)}")',
            f'        self.play(FadeIn(card, run_time=0.5))',
            f'        self.wait(0.5)',
            f'        self.play(FadeOut(card, run_time=0.3))',
        ]
        # caption centred in frame
        lines += [
            f'        b = Text("{cap}", font_size=28, color=WHITE)',
            f'        safe_scale(b, max_width=12.0)',
            f'        b.move_to(ORIGIN)',
            f'        self.play(FadeIn(b, run_time=0.15))',
            f'        self.wait(1)',
        ]
        return '\n'.join(lines) + '\n'

    # ── normal scene ─────────────────────────────────────────────────────────
    lines += [
        f'        title = Text("{ttl}", font_size={title_fs}, color=GOLD)',
        f'        title.to_edge(UP, buff=0.35)',
        f'        self.add(title)',
    ]

    if latex_or_none:
        lt = _e(latex_or_none)
        box_line = (
            '        self.play(Create(SurroundingRectangle(eq, color=GOLD,'
            ' buff=0.15, stroke_width=2)))\n'
        ) if highlight_box else ''

        lines += [
            # Build content group
            f'        eq = MathTex(r"{lt}", font_size=52)',
            f'        safe_scale(eq, max_width=12.5)',
            f'        cap_t = Text("{cap}", font_size=26, color=WAVE_COLOR)',
            f'        safe_scale(cap_t, max_width=12.5)',
            f'        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)',
            # Centre content vertically between title bottom and screen bottom
            f'        title_bottom = title.get_bottom()[1]',
            f'        available = title_bottom - (-3.8)',  # 3.8 ≈ half screen height
            f'        content.move_to([0, title_bottom - available/2, 0])',
            f'        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)',
            f'        self.play(FadeIn(content, run_time=0.15))',
        ]
        if highlight_box:
            lines.append(
                '        self.play(Create(SurroundingRectangle(eq, color=GOLD,'
                ' buff=0.15, stroke_width=2)))'
            )
    else:
        # Text-only caption — large, centred
        lines += [
            f'        cap_t = Text("{cap}", font_size=30, color=WHITE)',
            f'        safe_scale(cap_t, max_width=12.0)',
            f'        title_bottom = title.get_bottom()[1]',
            f'        available = title_bottom - (-3.8)',
            f'        cap_t.move_to([0, title_bottom - available/2, 0])',
            f'        self.play(FadeIn(cap_t, run_time=0.15))',
        ]

    lines.append('        self.wait(1)')
    return '\n'.join(lines) + '\n'

# week3_geometric.py
from manim import *
from utils import *

class Week3TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.add(card)
        sub_text = Text("Week 3: geometric optics — ray approximation to wave optics", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week3TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.add(card)
        sub_text = Text("Covers every lens, mirror, microscope, telescope and camera", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week3TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.add(card)
        sub_text = Text("Bennett Chapter 4 — Geometric Optics", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class Week3TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.add(card)
        sub_text = Text("Most critical skill: sign conventions — one sign error = wrong answer", font_size=26, color=WHITE)
        safe_scale(sub_text, max_width=12.0)
        sub_text.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(sub_text, run_time=0.3))
        self.wait(120)

class GeometricOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Geometric optics: wavelength << aperture size — rays in straight lines", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class GeometricOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Paraxial approximation: sin theta = theta, cos theta = 1", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class GeometricOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Paraxial regime: how real optical instruments are designed", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class GeometricOpticsIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p4.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"n\\cdot(\\text{geometric distance})=\\text{optical path length}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Optical path length = n times geometric distance  (Bennett 4.2)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class GeometricOpticsIntro_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p5.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("OPL determines phase — connects to interference (Week 6)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SignConventions_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p1.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Sign conventions  (Bennett Section 4.3.4) — follow rigorously", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SignConventions_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p2.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"s_o>0", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Object distance positive — real object on incoming side", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SignConventions_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p3.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"s_i>0\\;\\Rightarrow\\;\\text{real image}\\quad s_i<0\\;\\Rightarrow\\;\\text{virtual}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Image distance: positive = real, negative = virtual", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SignConventions_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p4.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"R>0", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Radius positive if centre of curvature on transmitted side", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SignConventions_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p5.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"m=-s_i/s_o", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Magnification — negative means inverted image", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SignConventions_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p6.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("m < 0: inverted | m > 0: upright | |m| > 1: enlarged", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SignConventions_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p7.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Mirror convention: positive toward incoming light (reversed)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SignConventions_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p8.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("ALWAYS draw a ray diagram first — it predicts sign of answer", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SphericalSurface_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p1.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{n_i}{s_o}+\\frac{n_t}{s_i}=\\frac{n_t-n_i}{R}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Refraction at spherical surface  (Bennett Eq. 4.18)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SphericalSurface_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p2.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{n_i}{s_o}+\\frac{n_t}{s_i}=0\\;\\Rightarrow\\;s_i=-\\frac{n_t}{n_i}s_o", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Flat surface (R->inf): apparent depth = n_t/n_i times real depth", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SphericalSurface_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p3.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Pool appears 75% as deep as it really is when viewed from air", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class SphericalSurface_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p4.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\text{Example: }n_i=1.0,\\;n_t=1.5,\\;R=10\\,\\mathrm{cm},\\;s_o=30\\,\\mathrm{cm}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Convex glass surface — find image distance", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class SphericalSurface_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p5.mp3", time_offset=0)
        title = Text("Refraction at a Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\text{Example: }n_i=1.0,\\;n_t=1.5,\\;R=10\\,\\mathrm{cm},\\;s_o=30\\,\\mathrm{cm}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Convex glass surface — find image distance", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p1.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{1}{s_o}+\\frac{1}{s_i}=\\frac{1}{f}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Thin lens equation  (Bennett Eq. 4.26)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p2.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"m=-\\frac{s_i}{s_o}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Lateral magnification", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p3.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"P=\\frac{1}{f}\\;[\\mathrm{D}]", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Dioptric power — optometrists use dioptres", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p4.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{1}{f}=(n_l-n_m)\\!\\left(\\frac{1}{R_1}-\\frac{1}{R_2}\\right)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Lensmaker's equation  (Bennett Eq. 4.30)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p5.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Contact lenses: P_eff = P1 + P2 when d = 0", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class ThinLensScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p6.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"s_o=60\\,\\text{cm},\\;f=20\\,\\text{cm}\\;\\Rightarrow\\;s_i=30\\,\\text{cm},\\;m=-0.5", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example 1: object at 3f gives image at 1.5f, half size", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p7.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"s_o=30\\,\\text{cm},\\;f=20\\,\\text{cm}\\;\\Rightarrow\\;s_i=60\\,\\text{cm},\\;m=-2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example 2: object at 1.5f gives image at 3f, double size", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p8.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"s_o=10\\,\\text{cm},\\;f=20\\,\\text{cm}\\;\\Rightarrow\\;s_i=-20\\,\\text{cm},\\;m=+2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example 3: inside focal length — virtual upright enlarged image", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p9.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Virtual image: cannot be projected on screen, only seen through lens", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class ThinLensScene_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p10.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"R_1=+20,\\;R_2=-20\\,\\text{cm},\\;n_l=1.5\\;\\Rightarrow\\;f=20\\,\\text{cm}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Biconvex lens lensmaker's equation worked out", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class ThinLensScene_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p11.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Principal ray 1: parallel to axis, bends through far focal point", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class MirrorScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p1.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{1}{s_o}+\\frac{1}{s_i}=\\frac{2}{R}=\\frac{1}{f_m}\\quad f_m=\\frac{R}{2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Mirror equation — same form as thin lens  (Bennett 4.3.2)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MirrorScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p2.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"s_o=60,\\;f_m=20\\,\\text{cm}\\;\\Rightarrow\\;s_i=30\\,\\text{cm},\\;m=-0.5", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Concave mirror: real inverted half-size image", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MirrorScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p3.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"s_o=10,\\;f_m=20\\,\\text{cm}\\;\\Rightarrow\\;s_i=-20\\,\\text{cm},\\;m=+2", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Inside focal length: virtual upright magnified — shaving mirror", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class MirrorScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p4.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Concave: converging, used in telescopes — no chromatic aberration", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class MirrorScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p5.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Convex: diverging, negative f, wide field — rear-view mirrors", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class MirrorScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p6.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Convex: diverging, negative f, wide field — rear-view mirrors", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class LensCombinations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p1.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Two lenses: image of first = object of second  (Bennett 4.4)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class LensCombinations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p2.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"s_{o2}=d-s_{i1}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Second object distance = separation minus first image distance", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class LensCombinations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p3.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\frac{1}{f_\\mathrm{eff}}=\\frac{1}{f_1}+\\frac{1}{f_2}-\\frac{d}{f_1 f_2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Effective focal length of two-lens system", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class LensCombinations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p4.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"P_\\mathrm{eff}=P_1+P_2\\;\\text{(contact, }d=0)", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Contact lenses: powers add directly", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class LensCombinations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p5.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Total magnification = m1 times m2 — magnifications multiply", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class OpticalInstruments_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p1.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"M_\\mathrm{mag}=\\frac{25\\,\\text{cm}}{f}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Magnifying glass: angular magnification  (Bennett 4.5)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class OpticalInstruments_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p2.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"M_\\mathrm{micro}=-\\frac{L}{f_\\mathrm{ob}}\\cdot\\frac{25\\,\\text{cm}}{f_e}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Compound microscope magnification  (Bennett Eq. 4.42)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class OpticalInstruments_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p3.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"M_\\mathrm{tel}=-\\frac{f_\\mathrm{ob}}{f_e}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Astronomical telescope magnification", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        content.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(title_bottom + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.2))
        self.wait(120)

class OpticalInstruments_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p4.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Microscope: f_ob=4mm, f_e=25mm, L=160mm -> M = -40", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)

class OpticalInstruments_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p5.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Telescope: f_ob=100cm, f_e=2cm -> M = -50", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        cap_t.move_to([0, (title_bottom + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.2))
        self.wait(120)


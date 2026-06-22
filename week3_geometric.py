# week3_geometric.py
from manim import *
from utils import *

class Week3TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.add(card)
        sub_t = Text("Week 3: geometric optics — rays, lenses, mirrors", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week3TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.add(card)
        sub_t = Text("Bennett Chapter 4 — paraxial approximation", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week3TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.add(card)
        sub_t = Text("Most critical skill: sign conventions", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week3TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week3TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 3", "Geometric Optics: Lenses, Mirrors and Instruments", "Bennett Ch. 4")
        self.add(card)
        sub_t = Text("Always draw a ray diagram before algebra", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class GeometricOpticsIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p1.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Rays perpendicular to wavefronts — valid when lambda << aperture", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class GeometricOpticsIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p2.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Paraxial: sin theta = theta, cos theta = 1", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class GeometricOpticsIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p3.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\text{OPL}=n\times d_\text{geom}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Optical path length determines phase", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class GeometricOpticsIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p4.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Connects geometric optics to interference and diffraction", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class GeometricOpticsIntro_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/GeometricOpticsIntro_p5.mp3", time_offset=0)
        title = Text("Geometric Optics  (Bennett 4.1-4.2)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Fails when aperture ~ wavelength — then Week 7 needed", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class SignConventions_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p1.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Distances measured FROM the optical element  (Bennett 4.3.4)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class SignConventions_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p2.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_o>0', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Object distance: positive = real object on incoming side", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class SignConventions_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p3.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_i>0\Rightarrow\text{real}\quad s_i<0\Rightarrow\text{virtual}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Image distance sign", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class SignConventions_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p4.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'm=-s_i/s_o', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Magnification: negative = inverted", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class SignConventions_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p5.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("m<0: inverted | |m|>1: enlarged", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class SignConventions_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p6.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Mirror convention: positive toward incoming light", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class SignConventions_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p7.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("ALWAYS draw ray diagram first", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class SignConventions_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SignConventions_p8.mp3", time_offset=0)
        title = Text("Sign Conventions  (Bennett 4.3.4)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Diagram predicts signs before algebra", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class SphericalSurface_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p1.mp3", time_offset=0)
        title = Text("Refraction at Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\frac{n_i}{s_o}+\frac{n_t}{s_i}=\frac{n_t-n_i}{R}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Refraction at spherical surface  (Bennett Eq. 4.18)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class SphericalSurface_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p2.mp3", time_offset=0)
        title = Text("Refraction at Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_i=-\frac{n_t}{n_i}s_o\quad(R\to\infty)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Flat surface: apparent depth", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class SphericalSurface_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p3.mp3", time_offset=0)
        title = Text("Refraction at Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Pool appears 75% as deep — n_t/n_i = 1/1.33", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class SphericalSurface_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p4.mp3", time_offset=0)
        title = Text("Refraction at Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'n_i=1,n_t=1.5,R=10,s_o=30\;\Rightarrow\;s_i=90\,\text{cm}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example: image 90cm inside glass", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class SphericalSurface_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SphericalSurface_p5.mp3", time_offset=0)
        title = Text("Refraction at Spherical Surface  (Bennett 4.3.3)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Apply: 1/30 + 1.5/si = 0.05, solve for si", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinLensScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p1.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\frac{1}{s_o}+\frac{1}{s_i}=\frac{1}{f}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Thin lens equation  (Bennett Eq. 4.26)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinLensScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p2.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'm=-s_i/s_o', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Lateral magnification", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinLensScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p3.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\frac{1}{f}=(n_l-n_m)\!\left(\frac{1}{R_1}-\frac{1}{R_2}\right)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Lensmaker equation  (Bennett Eq. 4.30)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinLensScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p4.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Contact lenses: P_eff = P1 + P2", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinLensScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p5.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_o=60,f=20\;\Rightarrow\;s_i=30,m=-0.5', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example 1: real inverted half-size", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinLensScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p6.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_o=30,f=20\;\Rightarrow\;s_i=60,m=-2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example 2: projector geometry", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinLensScene_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p7.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_o=10,f=20\;\Rightarrow\;s_i=-20,m=+2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Example 3: virtual upright — magnifying glass", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinLensScene_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p8.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Virtual image: only seen through lens", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinLensScene_p9(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p9.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'R_1=+20,R_2=-20,n_l=1.5\;\Rightarrow\;f=20\,\text{cm}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Biconvex lens worked out", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class ThinLensScene_p10(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p10.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Draw three principal rays first", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class ThinLensScene_p11(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/ThinLensScene_p11.mp3", time_offset=0)
        title = Text("The Thin Lens Equation  (Bennett 4.3)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Diagram gives sign of answer before algebra", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MirrorScene_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p1.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\frac{1}{s_o}+\frac{1}{s_i}=\frac{2}{R}=\frac{1}{f_m}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Mirror equation  (Bennett 4.3.2)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MirrorScene_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p2.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_o=60,f_m=20\;\Rightarrow\;s_i=30,m=-0.5', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Real inverted half-size", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MirrorScene_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p3.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_o=10,f_m=20\;\Rightarrow\;s_i=-20,m=+2', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Virtual upright magnified — shaving mirror", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MirrorScene_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p4.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Concave: converging, no chromatic aberration", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MirrorScene_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p5.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Convex: diverging — rear-view mirrors", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MirrorScene_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MirrorScene_p6.mp3", time_offset=0)
        title = Text("Spherical Mirrors  (Bennett 4.3.2)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Reflecting telescopes use concave mirrors", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class LensCombinations_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p1.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r's_{o2}=d-s_{i1}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Second object = separation minus first image", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class LensCombinations_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p2.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\frac{1}{f_\text{eff}}=\frac{1}{f_1}+\frac{1}{f_2}-\frac{d}{f_1 f_2}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Effective focal length", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class LensCombinations_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p3.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'P_\text{eff}=P_1+P_2\;(d=0)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Contact lenses: powers add", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class LensCombinations_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p4.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Total magnification = m1 times m2", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class LensCombinations_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/LensCombinations_p5.mp3", time_offset=0)
        title = Text("Lens Combinations  (Bennett 4.4)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'f_1=f_2=f,d=f\;\Rightarrow\;1/f_\text{eff}=0', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("4-f relay: afocal system", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class OpticalInstruments_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p1.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'M_\text{mag}=25\,\text{cm}/f', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Magnifying glass  (Bennett 4.5)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class OpticalInstruments_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p2.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'M_\text{micro}=-(L/f_\text{ob})(25\,\text{cm}/f_e)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Compound microscope  (Bennett Eq. 4.42)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class OpticalInstruments_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p3.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'M_\text{tel}=-f_\text{ob}/f_e', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Astronomical telescope", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class OpticalInstruments_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p4.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Microscope: fob=4mm, fe=25mm, L=160mm -> M=-40", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class OpticalInstruments_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/OpticalInstruments_p5.mp3", time_offset=0)
        title = Text("Optical Instruments  (Bennett 4.5)", font_size=36, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Human eye: 60 dioptres total power", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

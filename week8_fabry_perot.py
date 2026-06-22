# week8_fabry_perot.py
from manim import *
from utils import *

class Week8TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett 7.10-7.12")
        self.add(card)
        sub_t = Text("Week 8: Fabry-Perot interferometer  (Bennett 7.10-7.12)", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week8TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett 7.10-7.12")
        self.add(card)
        sub_t = Text("Multiple reflections -> geometric series -> Airy function", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week8TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett 7.10-7.12")
        self.add(card)
        sub_t = Text("Sharp peaks at resonance: 100% transmission", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class Week8TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett 7.10-7.12")
        self.add(card)
        sub_t = Text("Resolving power far exceeds diffraction gratings", font_size=26, color=WHITE)
        safe_scale(sub_t, max_width=12.0)
        sub_t.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(sub_t, run_time=0.3))
        self.wait(120)

class MultiBeamIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p1.mp3", time_offset=0)
        title = Text("Multi-Beam Interference  (Bennett 7.10)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Michelson: 2 beams, sinusoidal fringes", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MultiBeamIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p2.mp3", time_offset=0)
        title = Text("Multi-Beam Interference  (Bennett 7.10)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\tilde{T}=\frac{t^2}{1-r^2 e^{i\delta}}\quad\delta=\frac{4\pi nd\cos\theta}{\lambda}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Geometric series sum  (Bennett 7.10)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class MultiBeamIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p3.mp3", time_offset=0)
        title = Text("Multi-Beam Interference  (Bennett 7.10)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("At resonance: 100% transmission", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class MultiBeamIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p4.mp3", time_offset=0)
        title = Text("Multi-Beam Interference  (Bennett 7.10)", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Off resonance: very low transmission", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class AiryFunction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p1.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I_t=\frac{I_0}{1+F\sin^2(\delta/2)}\quad F=\frac{4R}{(1-R)^2}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("The Airy function  (Bennett Eq. 7.89)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class AiryFunction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p2.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("F = coefficient of finesse — NOT the same as script-F", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class AiryFunction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p3.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\delta=2N\pi\;\Rightarrow\;I_t=I_0', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("At resonance: complete transmission", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class AiryFunction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p4.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'R=0.9:\;F=360\;\Rightarrow\;I_t^\text{off}<0.3\%', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Off resonance: essentially opaque", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class AiryFunction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p5.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Higher R -> larger F -> sharper peaks -> better RP", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FinesseResolving_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p1.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathcal{F}=\frac{\pi\sqrt{R}}{1-R}=\frac{\pi\sqrt{F}}{2}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("FINESSE script-F  (NOT F)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FinesseResolving_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p2.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'N=2nd\cos\theta/\lambda_0', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Order number", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FinesseResolving_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p3.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\text{RP}=N\mathcal{F}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Resolving power = order times FINESSE", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FinesseResolving_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p4.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\Delta\lambda_\text{FSR}=\lambda_0^2/(2nd)\quad\Delta\nu_\text{FSR}=c/(2nd)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Free spectral range", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FinesseResolving_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p5.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'R=0.9:\;\mathcal{F}=29.8\qquad R=0.99:\;\mathcal{F}=312', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Finesse values", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FinesseResolving_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p6.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("EXAM: F=360 but script-F=29.8 for R=0.9 — very different", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FabryPerotExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p1.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'R=0.90,\;\lambda_0=656.2\,\text{nm},\;\Delta\lambda=0.18\,\text{nm}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("H and D alpha lines  (Bennett Example 7.11)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FabryPerotExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p2.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'F=360\;\Rightarrow\;\mathcal{F}=29.8', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 1: finesse", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FabryPerotExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p3.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'd=\lambda_0^2/(2\Delta\lambda_\text{FSR})=0.431\,\text{mm}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 2: spacing", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FabryPerotExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p4.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'N=2d/\lambda_0=1313', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 3: order", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FabryPerotExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p5.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\text{RP}=1313\times29.8=39100', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 4: resolving power", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FabryPerotExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p6.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\delta\lambda_\text{min}=0.017\,\text{nm}\ll0.18\,\text{nm}\;\checkmark', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 5: verified", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class FabryPerotExample_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p7.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Lines clearly resolved", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class FabryPerotExample_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p8.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Compare: 30000-slit grating RP=30000 — FP wins", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class CoherenceLength_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p1.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'l_c=\lambda^2/\Delta\lambda=c/\Delta\nu', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Coherence length  (Bennett 7.12)", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class CoherenceLength_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p2.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("FP: 2nd must be less than l_c", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class CoherenceLength_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p3.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("White light: 1um | Na: 0.35m | He-Ne: 300m", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class CoherenceLength_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p4.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("LIGO laser: delta-nu~mHz -> l_c~300,000 km", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class CoherenceLength_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p5.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Source coherence sets maximum usable cavity size", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class CoherenceLength_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p6.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Longer cavity: higher RP — if coherent enough", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class CoherenceLength_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p7.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Coherence time = 1/delta-nu", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class Week8Summary_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p1.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("Fabry-Perot complete formulas", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class Week8Summary_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p2.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'I_t=\frac{I_0}{1+F\sin^2(\delta/2)}\quad F=\frac{4R}{(1-R)^2}\quad\delta=\frac{4\pi nd}{\lambda_0}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Airy function, F and phase", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class Week8Summary_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p3.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\mathcal{F}=\frac{\pi\sqrt{R}}{1-R}\quad N=\frac{2nd}{\lambda_0}\quad\text{RP}=N\mathcal{F}', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Finesse, order, resolving power", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class Week8Summary_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p4.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        eq = MathTex(r'\Delta\lambda_\text{FSR}=\lambda_0^2/(2nd)\quad\Delta\nu_\text{FSR}=c/(2nd)', font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Free spectral range", font_size=26, color=TEAL)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.32)
        t_bot = title.get_bottom()[1]
        content.move_to([0, (t_bot + (-3.8)) / 2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(t_bot + 3.8) - 0.3)
        self.play(FadeIn(content, run_time=0.3))
        self.wait(120)

class Week8Summary_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p5.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("OPD=2nd must be less than coherence length", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class Week8Summary_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p6.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("R=0.9: F=360, script-F=29.8", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class Week8Summary_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p7.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("MOST COMMON ERROR: using F instead of script-F", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

class Week8Summary_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p8.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        safe_scale(title, max_width=13.5)
        title.to_edge(UP, buff=0.3)
        self.add(title)
        cap_t = Text("They differ by factor pi*sqrt(F)/2", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.5)
        t_bot = title.get_bottom()[1]
        cap_t.move_to([0, (t_bot + (-3.8)) / 2, 0])
        self.play(FadeIn(cap_t, run_time=0.3))
        self.wait(120)

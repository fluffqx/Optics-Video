# week8_fabry_perot.py
from manim import *
from utils import *

class Week8TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett 7.10-7.12")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Week 8: Fabry-Perot interferometer  (Bennett 7.10-7.12)", font_size=28, color=WHITE)
        safe_scale(b, max_width=12.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.15))
        self.wait(1)

class Week8TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett 7.10-7.12")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Multiple reflections between two mirrors — infinite geometric series", font_size=28, color=WHITE)
        safe_scale(b, max_width=12.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.15))
        self.wait(1)

class Week8TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett 7.10-7.12")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Airy function: sharp transmission peaks at resonance", font_size=28, color=WHITE)
        safe_scale(b, max_width=12.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.15))
        self.wait(1)

class Week8TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 8", "Fabry-Perot Interferometer", "Bennett 7.10-7.12")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Resolving power far exceeds diffraction gratings", font_size=28, color=WHITE)
        safe_scale(b, max_width=12.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.15))
        self.wait(1)

class MultiBeamIntro_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p1.mp3", time_offset=0)
        title = Text("Multi-Beam Interference  (Bennett 7.10)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Two-beam Michelson: sinusoidal fringes, limited resolving power", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class MultiBeamIntro_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p2.mp3", time_offset=0)
        title = Text("Multi-Beam Interference  (Bennett 7.10)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tilde{T}=\\frac{t^2}{1-r^2 e^{i\\delta}}\\quad\\delta=\\frac{4\\pi nd\\cos\\theta}{\\lambda_0}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Fabry-Perot: geometric series sums to this complex transmission", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class MultiBeamIntro_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p3.mp3", time_offset=0)
        title = Text("Multi-Beam Interference  (Bennett 7.10)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("t^2 = 1-r^2 (energy conservation at each mirror)", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class MultiBeamIntro_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/MultiBeamIntro_p4.mp3", time_offset=0)
        title = Text("Multi-Beam Interference  (Bennett 7.10)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("At resonance: all partial beams in phase — 100% transmission", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class AiryFunction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p1.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"I_t=\\frac{I_0}{1+F\\sin^2(\\delta/2)}\\quad F=\\frac{4R}{(1-R)^2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("The Airy function  (Bennett Eq. 7.89)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class AiryFunction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p2.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("F = coefficient of finesse — NOT the same as script-F finesse", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class AiryFunction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p3.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\delta=2N\\pi:\\;I_t=I_0", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("AT RESONANCE: complete transmission regardless of R", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class AiryFunction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p4.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"R=0.9:\\;F=360\\;\\Rightarrow\\;I_t^\\mathrm{off}=I_0/361<0.3\\%", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Off resonance with R=0.9: less than 0.3% transmitted", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class AiryFunction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/AiryFunction_p5.mp3", time_offset=0)
        title = Text("The Airy Function  (Bennett Eq. 7.89)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("High R: F large -> peaks become extremely sharp", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class FinesseResolving_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p1.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathcal{F}=\\frac{\\pi\\sqrt{R}}{1-R}=\\frac{\\pi\\sqrt{F}}{2}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("FINESSE script-F  (Bennett Section 7.10) — NOT F", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FinesseResolving_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p2.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"N=\\frac{2nd\\cos\\theta}{\\lambda_0}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Order number at resonance", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FinesseResolving_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p3.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathrm{RP}=N\\mathcal{F}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Resolving power = order number times finesse", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FinesseResolving_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p4.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Delta\\lambda_\\mathrm{FSR}=\\frac{\\lambda_0^2}{2nd}\\quad\\Delta\\nu_\\mathrm{FSR}=\\frac{c}{2nd}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Free spectral range in wavelength and frequency", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FinesseResolving_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p5.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"R=0.9:\\;\\mathcal{F}=29.8\\qquad R=0.99:\\;\\mathcal{F}=312", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Finesse values for typical reflectivities", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FinesseResolving_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FinesseResolving_p6.mp3", time_offset=0)
        title = Text("Finesse, Resolving Power and FSR", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("EXAM WARNING: never put F where script-F is needed — off by factor ~15", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class FabryPerotExample_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p1.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"R=0.90,\\;\\lambda_0=656.2\\,\\text{nm},\\;\\Delta\\lambda=0.18\\,\\text{nm}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("H and D alpha lines — Bennett Example 7.11", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FabryPerotExample_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p2.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"F=\\frac{4\\times0.9}{0.01}=360\\quad\\mathcal{F}=\\frac{\\pi\\sqrt{360}}{2}=29.8", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 1: coefficient of finesse and finesse", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FabryPerotExample_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p3.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"d=\\frac{\\lambda_0^2}{2\\Delta\\lambda_\\mathrm{FSR}}=\\frac{656.2^2}{2\\times0.5}=0.431\\,\\text{mm}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 2: choose FSR=0.5nm, find mirror spacing", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FabryPerotExample_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p4.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"N=\\frac{2d}{\\lambda_0}=\\frac{2\\times0.431\\,\\text{mm}}{656.2\\,\\text{nm}}=1313", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 3: order number", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FabryPerotExample_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p5.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathrm{RP}=N\\mathcal{F}=1313\\times29.8=39100", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 4: resolving power", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FabryPerotExample_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p6.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\delta\\lambda_\\mathrm{min}=\\frac{656.2}{39100}=0.0168\\,\\text{nm}\\ll0.18\\,\\text{nm}\\;\\checkmark", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Step 5: minimum resolvable — much smaller than 0.18 nm separation", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class FabryPerotExample_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p7.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("H and D alpha lines clearly resolved with 0.43 mm cavity", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class FabryPerotExample_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/FabryPerotExample_p8.mp3", time_offset=0)
        title = Text("Fabry-Perot Example: H and D Alpha Lines", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Compare: 30000-slit grating RP=30000 — FP wins", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class CoherenceLength_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p1.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"l_c=\\frac{\\lambda^2}{\\Delta\\lambda}=\\frac{c}{\\Delta\\nu}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Coherence length  (Bennett Section 7.12)", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class CoherenceLength_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p2.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\tau_c=l_c/c=1/\\Delta\\nu", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Coherence time", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class CoherenceLength_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p3.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\text{White light: }l_c\\approx1\\,\\mu\\text{m}\\quad\\text{Na lamp: }l_c\\approx0.35\\,\\text{m}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Coherence lengths for common sources", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class CoherenceLength_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p4.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\text{He-Ne: }l_c\\approx300\\,\\text{m}\\quad\\text{LIGO laser: }l_c\\approx300\\,000\\,\\text{km}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Laser coherence lengths — LIGO needs extraordinary stability", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class CoherenceLength_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p5.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("FP cavity: OPD = 2nd must be less than l_c for fringes to form", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class CoherenceLength_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p6.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("White light FP: only works for very small d — impractical", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class CoherenceLength_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CoherenceLength_p7.mp3", time_offset=0)
        title = Text("Coherence and the Fabry-Perot  (Bennett 7.12)", font_size=30, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Stabilised laser: delta-nu ~ mHz -> l_c ~ hundreds of thousands of km", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class Week8Summary_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p1.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Fabry-Perot complete formula summary", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class Week8Summary_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p2.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"I_t=\\frac{I_0}{1+F\\sin^2(\\delta/2)}\\quad F=\\frac{4R}{(1-R)^2}\\quad\\delta=\\frac{4\\pi nd}{\\lambda_0}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Airy function, F coefficient and round-trip phase", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class Week8Summary_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p3.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\mathcal{F}=\\frac{\\pi\\sqrt{R}}{1-R}\\quad N=\\frac{2nd}{\\lambda_0}\\quad\\mathrm{RP}=N\\mathcal{F}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Finesse, order number and resolving power", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class Week8Summary_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p4.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        eq = MathTex(r"\\Delta\\lambda_\\mathrm{FSR}=\\frac{\\lambda_0^2}{2nd}=\\frac{\\lambda_0}{N}\\quad\\Delta\\nu_\\mathrm{FSR}=\\frac{c}{2nd}", font_size=52)
        safe_scale(eq, max_width=12.5)
        cap_t = Text("Free spectral range in both lambda and frequency", font_size=26, color=WAVE_COLOR)
        safe_scale(cap_t, max_width=12.5)
        content = VGroup(eq, cap_t).arrange(DOWN, buff=0.35)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        content.move_to([0, title_bottom - available/2, 0])
        safe_scale(content, max_width=13.0, max_height=abs(available)-0.2)
        self.play(FadeIn(content, run_time=0.15))
        self.wait(1)

class Week8Summary_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p5.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("OPD = 2nd must be less than coherence length", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class Week8Summary_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p6.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("R=0.9: F=360, finesse=29.8 | R=0.99: F=39600, finesse=312", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class Week8Summary_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p7.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("EXAM: F (coefficient) vs script-F (finesse) — very different numbers", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)

class Week8Summary_p8(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week8Summary_p8.mp3", time_offset=0)
        title = Text("Week 8 Summary: Fabry-Perot Formulas", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.35)
        self.add(title)
        cap_t = Text("Most common error: substituting F in place of script-F", font_size=30, color=WHITE)
        safe_scale(cap_t, max_width=12.0)
        title_bottom = title.get_bottom()[1]
        available = title_bottom - (-3.8)
        cap_t.move_to([0, title_bottom - available/2, 0])
        self.play(FadeIn(cap_t, run_time=0.15))
        self.wait(1)


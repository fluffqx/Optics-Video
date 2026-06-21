# week7_diffraction.py
from manim import *
from utils import *

class Week7TitleCard_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p1.mp3", time_offset=0)
        card = make_title_card("WEEK 7", "Fraunhofer Diffraction", "Bennett Ch. 8")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Week 7: diffraction — wave optics when aperture ~ wavelength", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p2.mp3", time_offset=0)
        card = make_title_card("WEEK 7", "Fraunhofer Diffraction", "Bennett Ch. 8")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Huygens: every point on wavefront = secondary spherical source", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p3.mp3", time_offset=0)
        card = make_title_card("WEEK 7", "Fraunhofer Diffraction", "Bennett Ch. 8")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Fraunhofer pattern = Fourier transform of aperture  (Bennett Ch. 8)", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class Week7TitleCard_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/Week7TitleCard_p4.mp3", time_offset=0)
        card = make_title_card("WEEK 7", "Fraunhofer Diffraction", "Bennett Ch. 8")
        self.play(FadeIn(card, run_time=0.5))
        self.wait(0.5)
        self.play(FadeOut(card, run_time=0.3))
        b = Text("Larger aperture -> narrower pattern — optical uncertainty principle", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.move_to(ORIGIN)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p1.mp3", time_offset=0)
        title = Text("Huygens Principle  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Huygens 1678: each wavefront point emits a secondary wavelet", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p2.mp3", time_offset=0)
        title = Text("Huygens Principle  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Bennett Ch. 8: diffraction is interference done correctly", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p3.mp3", time_offset=0)
        title = Text("Huygens Principle  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Young: 2 discrete sources — Diffraction: continuous aperture", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class HuygensPrinciple_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/HuygensPrinciple_p4.mp3", time_offset=0)
        title = Text("Huygens Principle  (Bennett 8.2)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"L\gg\frac{a^2}{2\lambda}\;\Rightarrow\;\text{Fraunhofer (far field)}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Fraunhofer condition: screen in far field of aperture", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p1.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I=I_0\left(\frac{\sin\beta}{\beta}\right)^2\quad\beta=\frac{\pi b\sin\theta}{\lambda}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Single-slit Fraunhofer pattern — sinc squared  (Bennett 8.3.1)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p2.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"b\sin\theta=m\lambda\;\Rightarrow\;\text{dark minima}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Minima condition — m nonzero integer", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p3.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\theta_\mathrm{half}=\arcsin(\lambda/b)\approx\lambda/b", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Half-width of central maximum in radians", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p4.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Narrower slit -> wider diffraction pattern — inverse relationship", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p5.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Secondary maxima at ~4.7% and ~1.7% of central maximum", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p6.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"b=0.2\,\text{mm},\;\lambda=632.8\,\text{nm},\;L=2\,\text{m}:", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Worked example — He-Ne laser and 0.2 mm slit", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class SingleSlitDiffraction_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/SingleSlitDiffraction_p7.mp3", time_offset=0)
        title = Text("Single-Slit Diffraction  (Bennett 8.3.1)", font_size=34, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"y_1=L\sin\theta_1=L\lambda/b=6.33\,\text{mm}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("First dark fringe at 6.33 mm — central lobe width 12.7 mm", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p1.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"I=I_0\left(\frac{2J_1(x)}{x}\right)^2\quad x=\frac{\pi D r}{\lambda z}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Circular aperture — Airy disk with Bessel function J_1", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p2.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\sin\theta_1=\frac{1.22\lambda}{D}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("First dark ring — factor 1.22 from first zero of J_1  (Bennett 8.3.3)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p3.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\theta_\mathrm{min}=1.22\lambda/D", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Rayleigh criterion — minimum resolvable angular separation", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p4.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\theta_\mathrm{eye}=1.22\times550\,\text{nm}/3\,\text{mm}=2.2\times10^{-4}\,\text{rad}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Human eye: ~46 arcseconds resolution at 3 mm pupil", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p5.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\theta_\mathrm{HST}=1.22\times550\,\text{nm}/2.4\,\text{m}=2.8\times10^{-7}\,\text{rad}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Hubble: 0.058 arcseconds — 800x sharper than eye", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p6.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Better resolution: increase D or decrease lambda", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class CircularApertureRayleigh_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/CircularApertureRayleigh_p7.mp3", time_offset=0)
        title = Text("Circular Aperture and Rayleigh Criterion  (Bennett 8.3.3)", font_size=28, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("VLBI: Earth diameter baseline — microarcsecond resolution", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p1(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p1.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"d\sin\theta_m=m\lambda", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Grating equation for normal incidence  (Bennett Eq. 8.38)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class DiffractionGrating_p2(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p2.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\mathrm{RP}=\frac{\lambda}{\delta\lambda}=Nm", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Resolving power = N slits times order m  (Bennett Eq. 8.42)", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class DiffractionGrating_p3(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p3.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\Delta\lambda_\mathrm{FSR}=\lambda_\mathrm{min}/m", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Free spectral range — unambiguous wavelength interval", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class DiffractionGrating_p4(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p4.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("600 gr/mm grating, 5 cm: N=30000, RP=30000 in first order", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p5(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p5.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"\delta\lambda_\mathrm{min}=589/30000=0.020\,\text{nm}", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Resolves wavelengths 0.020 nm apart", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)

class DiffractionGrating_p6(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p6.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        b = Text("Sodium D lines: 0.6 nm separation — easily resolved", font_size=28, color=WHITE)
        safe_scale(b, max_width=13.0)
        b.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(b, run_time=0.1))
        self.wait(1)

class DiffractionGrating_p7(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR
        self.add_sound("narration/audio/paragraphs/DiffractionGrating_p7.mp3", time_offset=0)
        title = Text("Diffraction Grating  (Bennett 8.3.7-8.3.8)", font_size=32, color=GOLD)
        title.to_edge(UP, buff=0.4)
        self.add(title)
        eq = MathTex(r"d(\sin\theta_m-\sin\theta_i)=m\lambda", font_size=40)
        safe_scale(eq, max_width=13.0)
        eq.next_to(title, DOWN, buff=0.45)
        cap = Text("Oblique incidence grating equation", font_size=24, color=WAVE_COLOR)
        safe_scale(cap, max_width=13.0)
        cap.next_to(eq, DOWN, buff=0.3)
        self.play(FadeIn(VGroup(eq, cap), run_time=0.1))
        self.wait(1)


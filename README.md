# 31OPT Optics — Complete Manim Video Series
**TU/e Bachelor Applied Physics, Q4 2025-2026**  
Textbook: *Principles of Physical Optics* (2nd ed.) — Charles A. Bennett

A complete self-contained exam preparation video series built with [Manim Community](https://www.manim.community/), covering all 8 weeks of 31OPT. Every equation is animated on screen. Every exercise is solved step by step. Every SLT problem is presented for self-practice.

---

## Course Structure (from official Study Guide)

| Week | Lectures | Topics | Bennett Chapters |
|------|----------|--------|-----------------|
| 1 | 1.1, 1.2 | Waves, Wave Equation, Maxwell, EM Waves, Irradiance, Dispersion | 1, 2.1–2.5, 3.1–3.2 |
| 2 | 2.1, 2.2 | Fresnel Equations, Brewster, TIR, Spherical Surface, Thin Lenses | 3.3–3.6, 4.1–4.2 |
| 3 | 3.1, 3.2 | Mirrors, Aberrations, Lens Combinations, Matrix Optics, Instruments | 4.3–4.5, 5.2, 5.5 |
| 4 | 4.1 | **Midterm** (Weeks 1–3) + Superposition, Polarisation basics | 7.1–7.3.1, 6.1–6.2 |
| 5 | 5.1, 5.2 | Jones Formalism, Wave Plates, Interference, Young's, Thin Films | 6, 7.3–7.3.5 |
| 6 | 6.1 | Michelson Interferometer, Fraunhofer Diffraction, Single Slit | 7.8, 8.1–8.3.2 |
| 7 | 7.1 | Circular Aperture, Rayleigh, Diffraction Grating, FSR | 8.3.3–8.3.8 |
| 8 | 8.1 | Fabry-Pérot, Finesse, Coherence, Recap | 7.10 |

**Assessment:** Final exam 85% + Midterm 15% + SLT Bonus (up to +1.0)  
**Passing:** Final ≥ 6 AND Exam ≥ 5.0

---

## File Structure

```
Optics-Video/
├── utils.py                    # Shared colours, helpers (import in every file)
├── main.py                     # Render order + ffmpeg concat instructions
├── generate_audio.py           # Auto-generate narration MP3s via Edge TTS
│
├── week1_waves.py              # Wave equation, harmonic wave, phase/group velocity
├── week1_maxwell.py            # Maxwell equations, EM waves, Poynting, dispersion
├── week2_fresnel.py            # Snell, Fresnel, R/T, Brewster, TIR, Malus
├── week3_geometric.py          # Spherical surface, thin lens, mirror, combinations
├── week4_matrix_polarisation.py # Ray transfer matrices, cardinal points
├── week5_jones.py              # Polarisation states, QWP/HWP, Jones vectors/matrices
├── week6_interference.py       # Two-beam, Young's, thin film, Newton's rings, Michelson
├── week7_diffraction.py        # Single slit, Airy disk, Rayleigh, grating equation
├── week8_fabry_perot.py        # Airy function, finesse, resolving power, FSR, coherence
│
├── exercises_week1.py          # SC1 problems with full step-by-step solutions
├── exercises_week2.py          # SC2 problems with full step-by-step solutions
├── exercises_week3.py          # SC3 problems with full step-by-step solutions
├── exercises_week4.py          # SC4 problems with full step-by-step solutions
├── exercises_week5.py          # SC5 problems with full step-by-step solutions
├── exercises_week6.py          # SC6 problems with full step-by-step solutions
├── exercises_week7.py          # SC7/SC8 problems with full step-by-step solutions
├── exercises_week8.py          # SC8 Fabry-Perot problems with full solutions
│
├── slt_week1.py                # SLT Set 1 — problem statements only (no solutions)
├── slt_week2.py                # SLT Set 2
├── slt_week3.py                # SLT Set 3
├── slt_week5.py                # SLT Set 5
├── slt_week6.py                # SLT Set 6
├── slt_week7.py                # SLT Set 7
├── slt_week8.py                # SLT Set 8
├── slt_week9.py                # SLT Set 9
│
└── narration/
    ├── *.txt                   # Spoken narration scripts (one per scene)
    └── audio/                  # Generated MP3 files (created by generate_audio.py)
```

---

## Quick Start

### 1. Install dependencies
```powershell
pip install manim edge-tts
```
You also need **MiKTeX** for LaTeX rendering:  
→ Download from https://miktex.org/download (tick "install missing packages on-the-fly")

### 2. Test one scene (low quality preview)
```powershell
python -m manim -pql week1_waves.py WaveEquation1D
```
The video opens automatically. If it works, you're ready.

### 3. Generate narration audio
```powershell
python generate_audio.py          # generate all MP3s
python generate_audio.py --list   # check what's been generated
```

### 4. Render all scenes (high quality)
```powershell
python main.py --list             # prints all 70+ render commands
python main.py --list | ForEach-Object { Invoke-Expression $_ }  # run all (PowerShell)
```

### 5. Merge video + narration audio
```powershell
python generate_audio.py --sync   # prints ffmpeg merge commands
```

---

## Colour Coding (defined in utils.py)

| Colour | Used for |
|--------|---------|
| `#58C4DD` Blue | Electric field quantities (E) |
| `#FC6255` Red | Magnetic field quantities (B) |
| `#83C167` Green | Refractive index (n) |
| `#FFFF00` Yellow | Angles (θ) |
| `#9B59B6` Purple | Wave quantities (k, ω, λ) |
| `#FF9F40` Orange | Energy / Irradiance (I) |
| `#FFD700` Gold | Final answers, highlights, boxes |

---

## Key Equations (Official Formula Sheet)

### Waves
$$\frac{\partial^2\Psi}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2\Psi}{\partial t^2} \qquad v_p = \frac{\omega}{k} \qquad v_g = \frac{d\omega}{dk}$$

### Irradiance & Radiation Pressure
$$I = \frac{n\varepsilon_0 c}{2}E_0^2 \qquad P_\text{abs} = \frac{I}{c} \qquad P_\text{refl} = \frac{2I}{c}$$

### Fresnel (normal incidence)
$$r = \frac{n_i - n_t}{n_i + n_t} \qquad R = r^2 \qquad R + T = 1$$

### Thin Lens
$$\frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f} \qquad m = -\frac{s_i}{s_o}$$

### Interference (Young's)
$$\Delta y = \frac{\lambda L}{d} \qquad I = 4I_0\cos^2\!\left(\frac{\delta}{2}\right) \qquad \delta = \frac{2\pi}{\lambda_0}\cdot\text{OPD}$$

### Diffraction
$$I(\theta) = I_0\left(\frac{\sin\beta}{\beta}\right)^2 \quad \beta = \frac{\pi b\sin\theta}{\lambda} \qquad \Delta\theta_\text{Rayleigh} = 1.22\frac{\lambda}{D}$$

### Grating
$$d(\sin\theta_m - \sin\theta_i) = m\lambda \qquad \mathcal{R} = Nm \qquad \Delta\lambda_\text{FSR} = \frac{\lambda_\text{min}}{m}$$

### Fabry-Pérot
$$I_t = \frac{I_0}{1 + F\sin^2(\delta/2)} \qquad F = \frac{4R}{(1-R)^2} \qquad \mathcal{F} = \frac{\pi\sqrt{R}}{1-R} \qquad \mathcal{R} = m\mathcal{F}$$

---

## Narration Voice Options

Edit `VOICE` in `generate_audio.py`:

| Voice ID | Description |
|----------|-------------|
| `en-GB-RyanNeural` | British male (default) |
| `en-US-GuyNeural` | American male |
| `en-GB-SoniaNeural` | British female |
| `en-US-AriaNeural` | American female |
| `en-AU-WilliamNeural` | Australian male |

---

## Exam Tips (from Study Guide)

- **Midterm** (Week 4, 15:45–16:45): Weeks 1–3 only — EM waves, reflection, refraction, geometric optics
- **Final exam** (June): All 8 weeks, 85% of grade
- **Passing condition**: Final ≥ 6 AND Exam ≥ 5.0
- **SLT bonus**: Up to +1.0 on final grade (need ≥100 SLT points for full bonus)
- Formula sheet is provided in the exam — learn to use it, not just memorise it
- SLT problems are at exam level — solving them is the best exam practice

---

*Generated with Claude (Anthropic) | Course: 31OPT Optics, TU/e, Q4 2025-2026*

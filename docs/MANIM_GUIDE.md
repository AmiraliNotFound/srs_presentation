# Manim Presentation Engineering Guide

**Course:** Mechanical Vibrations (Semester 5) — School of Mechanical Engineering, University of Tehran  
**Technology:** Manim Community Edition (Python 3.11+ / `uv`), HTML5 Video Stage Integration

This guide provides the definitive engineering and animation manual for authoring mathematical scenes in this project. All scenes must adhere to the **3Blue1Brown fullscreen aesthetic**, pure black canvas background invariants, frame-accurate step-cuepoint synchronization, and zero-conflict multi-speaker workspace isolation.

---

## 1. Environment & CLI Setup

The project environment is managed via [`uv`](https://github.com/astral-sh/uv) or a standard Python virtual environment containing `manim`, `scipy`, `numpy`, and `moderngl`.

### Rendering Commands

```bash
# Rapid Development Render (720p, 30 FPS — fast iteration)
uv run manim -qm manim_scenes/part3/slide_16_stress_verification.py StressVerificationScene

# Full-Quality Production Freeze (1080p, 60 FPS — release standard)
uv run manim -qh manim_scenes/part3/slide_16_stress_verification.py StressVerificationScene

# Ultra High-DPI Presentation Freeze (4K, 60 FPS)
uv run manim -qk manim_scenes/part3/slide_16_stress_verification.py StressVerificationScene
```

### Useful CLI Flags for Development
- `-s`: Render only the final frame as a `.png` snapshot (instant visual check of layout).
- `-p`: Automatically preview the rendered video upon completion.
- `--disable_caching`: Force re-evaluation of all animation blocks if caching produces artifacts.

---

## 2. Canvas & Color Palette Invariants

### Pure Black Background (`#000000`)
Every Manim scene class constructor or `construct()` method **must** explicitly set:

```python
from manim import *

class StressVerificationScene(Scene):
    def construct(self):
        # Mandatory pure black invariant:
        self.camera.background_color = ManimColor("#000000")
```

> [!CAUTION]
> Never omit `self.camera.background_color = ManimColor("#000000")`. Without it, Manim defaults to dark gray (`#1a1a1a`), causing an ugly, visible flicker when embedded into the pure black (`#000000`) HTML5 stage.

### Project Color Standards

Always use `ManimColor("<HEX>")` for consistent cross-version color safety:

```python
AMBER       = ManimColor("#FFB703")   # Mass, Cantilever, Physical Bodies
CYAN        = ManimColor("#58C4DD")   # Restoring Spring, Stiffness, Elasticity
RED_SHOCK   = ManimColor("#FF644E")   # Shock Pulse, Dynamic Inertia, Failure/Stress Exceedance
GREEN_PASS  = ManimColor("#83C167")   # Permissible Stress, Certified Safe State, Static Equilibrium
UT_BLUE     = ManimColor("#0097F1")   # University of Tehran Blue, Accent Highlights
TEXT_WHITE  = ManimColor("#FFFFFF")   # Primary Equations & Numerical Values
TEXT_MUTED  = ManimColor("#94A3B8")   # Subscript Indicators, Axis Labels, Annotations
WALL_DARK   = ManimColor("#1E293B")   # Ground, Rigid Clamped Base, Foundations
WALL_STROKE = ManimColor("#475569")   # Boundaries & Boundary Hatches
```

---

## 3. Strict 3Blue1Brown Fullscreen Aesthetic

### The 4 Hard Rules
1. **NO Top Header Banners:** No horizontal colored lines, no breadcrumbs, no subtitle bars. Slides have either NO title or a single minimal 2–4 word title (e.g., `Tex(r"\textbf{Stress Verification}", font_size=36)`).
2. **Spoken Script in `data-mobile-notes` ONLY:** Never render explanatory text or paragraphs on screen. Visuals and equations must occupy >90% of screen space.
3. **The 10-Word Rule:** A slide canvas may contain at most **10–15 words of English text total**.
4. **One Visual Idea Per Screen:** Replace or morph visuals (`Transform`, `FadeTransform`, `ReplacementTransform`); never divide the screen into cluttered horizontal cards.

---

## 4. Mathematical Derivations & Equation Morphing

To achieve smooth 3Blue1Brown-style equation transitions without jarring layout jumps, structure equations using `MathTex` or `Tex` with substring tokens:

### Best Practices for `TransformMatchingTex`

```python
# Group 1: Initial governing equation
eq1 = MathTex(
    r"\sigma_{\max}", r"=", r"\frac{M_{\max} c}{I}", r"=", r"\frac{6 F_{\text{dyn}} l}{b d^2}"
).set_color_by_tex(r"F_{\text{dyn}}", RED_SHOCK).set_color_by_tex(r"d^2", AMBER)

# Group 2: Substitution of dynamic force
eq2 = MathTex(
    r"\sigma_{\max}", r"=", r"\frac{6 (100 \cdot \text{DLF} \cdot W_{\text{eq}}) l}{b d^2}"
).set_color_by_tex(r"\text{DLF}", CYAN).set_color_by_tex(r"W_{\text{eq}}", AMBER)

self.play(Write(eq1))
self.wait(2.0)
self.play(TransformMatchingTex(eq1, eq2))
self.wait(3.0)
```

### Morphing Guidelines:
- Break equations into granular, matching substring slices (e.g., `r"\sigma_{\max}"`, `r"="`).
- Use `key_map` when transforming symbols that change notation:
  ```python
  self.play(TransformMatchingTex(eq1, eq2, key_map={r"M_{\max}": r"F_{\text{dyn}} l"}))
  ```
- Center equations with explicit coordinate coordinates (`.move_to([0, 1.5, 0])`) or relative positioning (`.next_to(...)`).

---

## 5. Frame-Accurate Step & Cuepoint Synchronization

The HTML presentation engine uses discrete `step` cuepoints to pause and resume animations based on speaker pacing.

### Planning Animation Segments

When scripting a scene in Manim, plan your pauses (`self.wait(...)`) deliberately:

```python
class IterativeDesignScene(Scene):
    def construct(self):
        self.camera.background_color = ManimColor("#000000")
        
        # --- SEGMENT 0: Problem Formulation (0.0s to 3.5s) ---
        # Animate cantilever bracket schematic and root moment
        self.play(...)         # 2.0s
        self.wait(1.5)         # 1.5s -> Cumulative: 3.5s (CUEPOINT 1)
        
        # --- SEGMENT 1: SDOF Period Equation (3.5s to 8.0s) ---
        # Reveal natural period formula tau_n = 2*pi*sqrt(delta_st / g)
        self.play(...)         # 2.5s
        self.wait(2.0)         # 2.0s -> Cumulative: 8.0s (CUEPOINT 2)
        
        # --- SEGMENT 2: The Circular Dilemma Cycle (8.0s to 14.5s) ---
        # Animate circular dependency arrows
        self.play(...)         # 3.5s
        self.wait(3.0)         # 3.0s -> Cumulative: 14.5s (CUEPOINT 3 / End)
```

### Matching HTML Integration
In `presentation/index.html`, register the exact cumulative timestamps:

```html
<section class="slide" 
         id="slide-15" 
         data-slide-id="SLIDE-15" 
         data-slide-num="15" 
         data-speaker="person3" 
         data-speaker-name="Person 3: Design Resolution &amp; Applications" 
         data-cuepoints="3.5, 8.0"
         data-manim-scene="IterativeDesignScene">
  <div class="slide-stage">
    <video class="stage-video" preload="auto" playsinline muted>
      <source src="assets/videos/SLIDE_15_IterativeDesignScene.mp4" type="video/mp4">
    </video>
    <div class="step" data-step="1" data-cuepoint="3.5" data-step-name="SDOF Period Formula"></div>
    <div class="step" data-step="2" data-cuepoint="8.0" data-step-name="Circular Dilemma Cycle"></div>
  </div>
</section>
```

When the presenter presses `Space` or `ArrowRight`, the video plays until the next cuepoint timestamp and automatically pauses cleanly.

---

## 6. Output File Conventions & Asset Flow

### File Naming Convention
All production MP4 files must follow the strict naming schema:
```
presentation/assets/videos/SLIDE_<NUM>_<SceneName>.mp4
```

Examples:
- `SLIDE_15_IterativeDesignScene.mp4`
- `SLIDE_16_StressVerificationScene.mp4`
- `SLIDE_17_CraneSeismicScene.mp4`
- `SLIDE_18_CraneStiffnessLimitScene.mp4`
- `SLIDE_19_ECUResonanceScene.mp4`
- `SLIDE_20_ECUIsolatorScene.mp4`
- `SLIDE_21_MasterSummaryScene.mp4`

### Copying from Manim Output Cache to Production Assets

After rendering, copy the generated `.mp4` from Manim's build directory (`media/videos/<scene_file>/<resolution>/<SceneName>.mp4`) to `presentation/assets/videos/`:

```powershell
# PowerShell Example
Copy-Item "media\videos\slide_16_stress_verification\1080p60\StressVerificationScene.mp4" "presentation\assets\videos\SLIDE_16_StressVerificationScene.mp4"
```

```bash
# Bash Example
cp media/videos/slide_16_stress_verification/1080p60/StressVerificationScene.mp4 presentation/assets/videos/SLIDE_16_StressVerificationScene.mp4
```

---

## 7. Zero-Overlap Coordinate Plotting Checklist

When building coordinate plots (`Axes`, `FunctionGraph`, SRS curves):
1. **Set explicit ranges:** Use `x_range=[x_min, x_max, step]` and `y_range=[y_min, y_max, step]`.
2. **Buffer labels:** Always use `.next_to(axis, DIRECTION, buff=0.25)` to prevent axis numbers from clipping tick marks.
3. **Stroke widths:** Keep plot lines bold (`stroke_width=3.5` to `4.5`) so they remain sharp and readable on lecture hall projectors.
4. **Clean up mobjects:** When transitioning graphs, use `FadeOut(..., run_time=0.6)` or `ReplacementTransform` rather than leaving stale graph lines on the stage.

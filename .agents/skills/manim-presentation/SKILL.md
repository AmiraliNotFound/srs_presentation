---
name: manim-presentation
description: >-
  Guides the creation, 4K 60FPS rendering, and web deployment of publication-grade
  mathematical and engineering presentations using Manim Community, manim-slides,
  3Blue1Brown TransformMatchingTex equation morphing, bi-directional reverse playback,
  and zero-flash double-buffered HTML players.
---

# Manim Presentation Engineering Guide

Use this skill whenever authoring, rendering, or deploying mathematical or engineering lecture presentations using Manim and `manim-slides`.

---

## 1. Environment & Package Invariants

### A. Strict Dependency Pinning
Do not run unpinned `uv run --with manim`; `manim 0.22+` removes `write_to_movie` from `ManimConfig`, breaking `manim-slides 5.7.0`.
* **Required Invocation**:
  ```powershell
  uv run --with "manim<0.20.0" --with manim-slides manim-slides ...
  ```

### B. Background Color Type Invariant
Assigning `self.camera.background_color = "#13141f"` directly causes an `AttributeError: 'str' object has no attribute 'to_hex'` in `manim-slides`.
* **Correct Assignment**:
  ```python
  from manim import ManimColor
  self.camera.background_color = ManimColor("#13141f")  # 3b1b deep slate
  ```

---

## 2. High-Resolution Render CLI Recipes

Always use the `--` flag separator to forward quality options through `manim-slides render`:

| Quality Target | Resolution | Frame Rate | CLI Command |
| :--- | :--- | :--- | :--- |
| **Draft Preview** | $1280 \times 720$ | 30 FPS | `uv run --with "manim<0.20.0" --with manim-slides manim-slides render -- -qm <file>.py <Scene>` |
| **Full HD** | $1920 \times 1080$ | 60 FPS | `uv run --with "manim<0.20.0" --with manim-slides manim-slides render -- -qh <file>.py <Scene>` |
| **Auditorium 4K** | $3840 \times 2160$ | 60 FPS | `uv run --with "manim<0.20.0" --with manim-slides manim-slides render -- -qk <file>.py <Scene>` |
| **Custom 16:10 Projector** | $3840 \times 2400$ | 60 FPS | `uv run --with "manim<0.20.0" --with manim-slides manim-slides render -- -r 3840,2400 --fps 60 <file>.py <Scene>` |

---

## 3. 3Blue1Brown Equation Morphing (`TransformMatchingTex`)

To make equations slide and transform smoothly across presentation steps:
1. **Isolate Substrings**: Declare terms in `substrings_to_isolate` across all equation steps.
2. **Standard 3b1b Color Coding**:
   * Spring / Restoring terms: `#58c4dd` (Cyan)
   * Damper / Dissipative terms: `#83c167` (Green)
   * Inertia / Acceleration terms: `#ff644e` (Coral Red)
   * Force / Canonical roots: `#f7ca3b` (Yellow)
3. **Step Pauses**: Call `self.next_slide()` after every mathematical milestone.

```python
from manim import *
from manim_slides import Slide

class VibrationsDerivation(Slide):
    def construct(self):
        self.camera.background_color = ManimColor("#13141f")
        iso = [
            r"\sum F", r"- k x", r"- c \dot{x}", r"m \ddot{x}",
            r"\ddot{x}", r"2\zeta\omega_n", r"\omega_n^2", r"="
        ]

        # Step 1: Newton's Law
        eq1 = MathTex(r"\sum F", r"=", r"m \ddot{x}", substrings_to_isolate=iso, font_size=44)
        eq1.set_color_by_tex(r"\sum F", ManimColor("#f7ca3b"))
        eq1.set_color_by_tex(r"m \ddot{x}", ManimColor("#ff644e"))
        self.play(Write(eq1))
        self.next_slide()

        # Step 2: Smooth Glide Morph
        eq2 = MathTex(r"- k x", r"- c \dot{x}", r"=", r"m \ddot{x}", substrings_to_isolate=iso, font_size=44)
        eq2.set_color_by_tex(r"- k x", ManimColor("#58c4dd"))
        eq2.set_color_by_tex(r"- c \dot{x}", ManimColor("#83c167"))
        eq2.set_color_by_tex(r"m \ddot{x}", ManimColor("#ff644e"))
        self.play(TransformMatchingTex(eq1, eq2, transform_mismatches=True), run_time=1.2)
        self.next_slide()
```

---

## 4. Visual Composition Invariants (Zero Overlap)

For split-screen scenes (e.g. physical schematic alongside a graph):
* **Left Half (Schematic)**: Anchor wall at $x = -6.0$, ground at $y = -2.2$. Keep mass oscillation bounded within $x \in [-4.5, -1.5]$.
* **Right Half (Axes & Plot)**: Anchor coordinate axes shifted to $x \ge +0.8$ so ground lines never intersect plot axes.
* **Synchronized Trajectory**: Animate physical mass displacement and curve plot simultaneously with `always_redraw(lambda: Dot(...))` tied to a `ValueTracker`.

---

## 5. Web Delivery: Zero-Flash Double-Buffered Video Shell

Standard video swapping triggers a black flash because the browser clears the video decode buffer. Eliminate flashing using hardware-synchronized ping-pong buffering:

1. **Dual Video Elements (`playerA` and `playerB`)**: Positioned at `100vw × 100vh`, `object-fit: contain`, background `#13141f`.
2. **`requestVideoFrameCallback()` Swap**:
   * Outgoing player stays locked on screen.
   * Incoming player starts playing on the hidden layer behind it.
   * On the exact microsecond the GPU composites the first frame, flip `z-index` and show the new player.
3. **Bi-Directional Reverse Animations**:
   * Forward (<kbd>→</kbd>): Load `slide.fwd`.
   * Backward (<kbd>←</kbd>): Load `slide.rev` (the `_reversed.mp4` generated by Manim). On completion, land paused on the previous slide.
4. **Presenter HUD**: Overlay a semi-transparent HUD providing Laser Pointer (<kbd>L</kbd>), Drawing Pen (<kbd>P</kbd>), Clear (<kbd>C</kbd>), and Fullscreen (<kbd>F</kbd>).

---

## 6. HTML Template Implementation Reference

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>4K Presentation</title>
  <style>
    body { background: #13141f; margin: 0; overflow: hidden; }
    #stage { position: fixed; inset: 0; }
    .stage-video {
      position: absolute; inset: 0; width: 100%; height: 100%;
      object-fit: contain; background: #13141f; opacity: 0;
      image-rendering: -webkit-optimize-contrast;
    }
    .stage-video.active-layer { opacity: 1; }
  </style>
</head>
<body>
  <div id="stage">
    <video id="playerA" class="stage-video active-layer" style="z-index: 2;" playsinline muted></video>
    <video id="playerB" class="stage-video" style="z-index: 1;" playsinline muted></video>
  </div>
  <script>
    let currentStep = 0;
    let activePlayer = document.getElementById('playerA');
    let inactivePlayer = document.getElementById('playerB');

    function playSeamless(src, onComplete) {
      inactivePlayer.src = src;
      inactivePlayer.currentTime = 0;
      inactivePlayer.play().catch(console.error);

      function onPaint() {
        inactivePlayer.style.zIndex = "2";
        activePlayer.style.zIndex = "1";
        inactivePlayer.classList.add('active-layer');

        const old = activePlayer;
        activePlayer = inactivePlayer;
        inactivePlayer = old;
        old.classList.remove('active-layer');

        activePlayer.onended = () => {
          activePlayer.onended = null;
          if (onComplete) onComplete();
        };
      }

      if ('requestVideoFrameCallback' in inactivePlayer) {
        inactivePlayer.requestVideoFrameCallback(onPaint);
      } else {
        inactivePlayer.onplaying = onPaint;
      }
    }
  </script>
</body>
</html>
```

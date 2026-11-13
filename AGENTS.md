# AI Agent Operating Guidelines & Technical Invariants

> **Audience:** This document is mandatory reading for any AI assistant, subagent, or autonomous coding tool assisting contributors in this repository. All instructions and visual standards documented here must be enforced strictly without deviation.

---

## 1. The 4 Hard Visual Rules (Strict 3Blue1Brown Aesthetic)

The presentation engine is engineered to deliver a clean, cinematic, mathematics-first lecture experience inspired by 3Blue1Brown (*Grant Sanderson*). We do not produce typical bullet-point academic slides. Every slide is an edge-to-edge canvas where mathematics and physics speak for themselves.

### Rule 1: NO Top Header Banners
- **Forbidden:** No `Category • Subcategory` breadcrumb headers, no recurring top ribbons, no decorative horizontal divider lines, and no subtitle banners across the top of the screen.
- **Allowed:** A slide must either have **NO title at all** (pure fullscreen animated equation, schematic, or coordinate graph) or at most a single minimal **2–4 word title** floating organically without borders or background cards.

### Rule 2: Spoken Script Goes in `data-mobile-notes`, NEVER on Screen
- **Forbidden:** Never render descriptive paragraphs, bullet points, contextual definitions ("Primary Driver:", "Failure Mode:", "Motivating Scenario:", "MIL-STD-810H"), or problem narratives directly on the slide canvas.
- **Enforcement:** All spoken background narrative, speaker reminders, and contextual descriptions **must** be placed in the HTML `<section data-mobile-notes="...">` attribute. This content is broadcast dynamically to the presenter HUD and the mobile companion interface for audience smartphones.

### Rule 3: The 10-Word Rule
- **Threshold:** At most **10–15 words of English text total** may appear on any single slide canvas simultaneously.
- **Allocation:** Visual schematics, physical diagrams, and LaTeX equations must occupy **>90%** of the viewport area.
- If you find yourself writing complete explanatory sentences on a slide canvas, stop immediately and migrate the prose into `data-mobile-notes`.

### Rule 4: One Visual Idea Per Screen (Replace / Morph, Don't Stack)
- **Forbidden:** Never subdivide a 16:9 canvas into stacked top/bottom horizontal sections or cluttered multi-column card layouts.
- **Workflow:** When transitioning from a physical model to a mathematical derivation or design conclusion, animate the first visual transforming/morphing into the second via Manim, or split the topic cleanly into consecutive sub-slides (e.g., `SLIDE-15A`, `SLIDE-15B`).

---

## 2. Frame-Accurate Step Control & Cuepoints

Every multi-step slide must synchronise video playback with the presenter's delivery.

### Slide Configuration Standards
- In `presentation/index.html`, every slide with intermediate reveals must specify `data-cuepoints="..."` listing the exact timestamp cuepoints (in seconds):
  ```html
  <section class="slide" 
           id="slide-16" 
           data-slide-id="SLIDE-16" 
           data-slide-num="16" 
           data-speaker="person3" 
           data-speaker-name="Person 3: Design Resolution &amp; Applications" 
           data-time-budget="150" 
           data-cuepoints="3.5, 8.0, 14.2"
           data-mobile-summary="Evaluating bracket thickness d = 0.4, 0.5, 0.6 inches against 26 ksi allowable stress."
           data-mobile-notes="Explain the trade-off: thicker bracket increases inertia load but reduces bending stress quadratically."
           data-manim-scene="StressVerificationScene">
    <div class="slide-stage">
      <video class="stage-video" preload="auto" playsinline muted>
        <source src="assets/videos/SLIDE_16_StressVerificationScene.mp4" type="video/mp4">
      </video>
      <!-- Discrete Step Triggers -->
      <div class="step" data-step="1" data-cuepoint="3.5" data-step-name="Trial 1 (d = 0.4 in)"></div>
      <div class="step" data-step="2" data-cuepoint="8.0" data-step-name="Trial 2 (d = 0.5 in)"></div>
      <div class="step" data-step="3" data-cuepoint="14.2" data-step-name="Trial 3 (d = 0.6 in Certified)"></div>
      <div class="stage-fallback">
        <span class="slide-num-watermark">16</span>
        <h2 class="fallback-title">StressVerificationScene</h2>
        <p class="fallback-sub">Evaluating Cantilever Bracket Sizing</p>
      </div>
    </div>
  </section>
  ```
- **Rule:** Never dump all information onto the screen at once. Build animations with deliberate pauses (`self.wait(...)`) matching the presenter's spoken rhythm.

---

## 3. Canvas & Color Palette Invariants

All Manim scenes and CSS elements must adhere strictly to the established academic color palette:

| Element / Physical Role | Hex Code | Manim Construction | CSS Variable |
|---|---|---|---|
| **Canvas Background** | `#000000` | `self.camera.background_color = ManimColor("#000000")` | `--bg-black` |
| **Primary Accent / Brand** | `#0097F1` | `ManimColor("#0097F1")` (UT Blue) | `--accent-blue` |
| **Spring / Restoring Force** | `#58C4DD` | `ManimColor("#58C4DD")` (Cyan) | `--cyan` |
| **Shock Pulse / Inertia / Danger** | `#FF644E` | `ManimColor("#FF644E")` (Red-Orange) | `--shock-red` |
| **Lumped Mass / Accent Amber** | `#FFB703` | `ManimColor("#FFB703")` (Amber) | `--amber` |
| **Allowable / Safe / Pass** | `#83C167` | `ManimColor("#83C167")` (Green) | `--pass-green` |
| **Primary Equations & Text** | `#FFFFFF` | `WHITE` | `--text-white` |
| **Secondary Subtitles / Labels** | `#B0B8C4` | `ManimColor("#B0B8C4")` (Slate) | `--text-muted` |

### Background Color Invariant
- Every Manim scene class constructor or `construct()` method **must** explicitly set:
  ```python
  self.camera.background_color = ManimColor("#000000")
  ```
- Failure to set pure black causes visible gray flashing when embedding video frames into the black presentation stage.

### Typography Standards
- Visual text in Manim must use standard TeX fonts (`MathTex`, `Tex`) styled with Computer Modern / Latin Modern.
- HTML elements use `CMU Serif` / `Latin Modern Math` with monospace fallbacks (`Fira Code`).

---

## 4. Workspace Isolation & Multi-Speaker Branch Protocol

To prevent merge conflicts when multiple presenters and AI agents work simultaneously:

### Strict DOM Boundaries (`presentation/index.html`)
- **Part 1 & Part 2 (Slides 01–14):** Owned exclusively on branch `main`.
- **Part 3 (Slides 15–21):** Owned exclusively on branch `part-3` by Colleague.
- AI agents working on Part 3 must **only** modify lines inside the Part 3 boundary marker:
  ```html
  <!-- ========================================================================== -->
  <!-- PART 3 WORKSPACE (SLIDES 15 - 21) — OWNED BY COLLEAGUE (PART-3 BRANCH)    -->
  <!-- ========================================================================== -->
  ```
  **Never edit Slides 01 through 14 when working on `part-3`!**

### Modular Manim Directory
- Part 3 Manim scripts must be placed in `manim_scenes/part3/`.
- Do not add or edit files in `manim_scenes/scenes/` when working on Part 3.

### Modular Theme Stylesheet
- Custom styling, typography adjustments, and Phase 3 visual polish for Part 3 must be written in `presentation/css/part3_theme.css`.
- **Never modify `presentation/css/style.css` on `part-3`!**

---

## 5. Technical Source Materials

When authoring equations, numerical values, or physical models, consult the authoritative documentation files in `docs/`:
- **`docs/syllabus_and_problems.md`**: Contains complete, pre-calculated numerical solutions for:
  - **Problem 1 (Helicopter Drop-Box):** $d = 0.6\text{ in}$ sizing, $W_{\text{eq}} = 0.538\text{ lb}$, $k = 540\text{ lb/in}$, $\tau_n = 0.0101\text{ s}$, $t_0/\tau_n = 9.91$, $\text{DLF} = 1.07$, $\sigma_{\max} = 25,664\text{ psi} \le 26\text{ ksi}$.
  - **Problem 2 (Overhead Crane Derailment):** $S_a \ge 1.0g$ derailment threshold, girder stiffness limit $k < 365\text{ kN/m}$.
  - **Problem 3 (Municipal Water Tower Blast):** $35\text{ m}$ concrete pedestal, $M_{\text{eff}} = 311,653\text{ kg}$, $k = 3,919.7\text{ kN/m}$, $\tau_n = 1.7717\text{ s}$, half-sine wind blast $F_0 = 180\text{ kN}$, $t_0 = 1.60\text{ s}$, $\beta = 0.9031$, $\text{DLF} = 1.7587$, $x_{\max} = 80.76\text{ mm}$, $M_{b,\max} = 11,080\text{ kN}\cdot\text{m}$, $\sigma_{\max} = 8.31\text{ MPa} \le 12.0\text{ MPa}$ ($\text{FS} = 1.44$ Certified Safe).
- **`docs/presentation_script_and_pacing.md`**: Minute-by-minute speaking cues and rehearsal timing budgets.
- **`docs/MANIM_GUIDE.md`**: Manim CLI flags, equation morphing techniques, and video naming conventions.

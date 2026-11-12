# Contributor & Multi-Speaker Collaboration Guide

Welcome to the **Shock Response Spectrum (SRS)** interactive presentation project. This document outlines the Git branching strategy, workspace isolation boundaries, and technical references required for co-presenters and AI agents working on **Part 3 (Slides 15–21)** and **Phase 3 (Visual Polish)** in parallel with the main development team.

---

## 1. Branching Workflow & Team Roles

To enable completely independent development without merge conflicts, work is divided across strict feature branches:

```
main (Lead Presenter)
 ├── Part 1 (Slides 01–07): 100% Complete & Frozen
 └── Part 2 (Slides 08–14): Currently in active development on main
      │
      └── git checkout -b part-3 ──────► part-3 (Colleague Workspace)
                                          ├── Part 3 (Slides 15–21): Sizing, Crane & ECU
                                          └── Phase 3: Visual Polish & Theme Styling
```

### Getting Started on Part 3
If you are collaborating on Part 3:

```bash
# Clone the repository
git clone <REPO_URL>
cd "#Presentations/#Ours"

# Switch to the dedicated part-3 branch
git checkout part-3
```

---

## 2. Ownership Scope & Workspace Isolation

To ensure that merging `part-3` into `main` will be a 100% clean, conflict-free merge, observe the following ownership boundaries:

### A. HTML Slides (`presentation/index.html`)
- **Part 1 & 2 Workspace (Slides 01–14):** Owned exclusively on `main`. **DO NOT MODIFY.**
- **Part 3 Workspace (Slides 15–21):** Owned by you on `part-3`.
- In `presentation/index.html`, locate the explicit DOM boundary:
  ```html
  <!-- ========================================================================== -->
  <!-- PART 3 WORKSPACE (SLIDES 15 - 21) — OWNED BY COLLEAGUE (PART-3 BRANCH)    -->
  <!-- ========================================================================== -->
  ```
  All your slide edits, cuepoints, and video tags must stay strictly beneath this line.

### B. Manim Animation Scenes
- Author all your Manim Python scene files exclusively inside:
  ```
  manim_scenes/part3/
  ```
- **Do not edit or add files** to `manim_scenes/scenes/` (reserved for Parts 1 and 2).

### C. Visual Theme & Phase 3 Styling
- Add custom CSS overrides, TeX font adjustments, and Phase 3 visual polish in:
  ```
  presentation/css/part3_theme.css
  ```
- `part3_theme.css` is pre-linked in `presentation/index.html` after `style.css`.
- **Do not modify `presentation/css/style.css` on `part-3`**; this ensures your visual customizations never conflict with core presentation CSS updates.

---

## 3. Pre-Compiled Mathematical & Script References

You do not need to derive equations or guess numerical parameters from scratch. All derivations and speaking scripts have been pre-calculated, verified against course lecture notes, and documented:

### 1. `docs/syllabus_and_problems.md` (Authoritative Engineering Source)
Consult this document for exact numerical values, governing equations, and derivation steps:
- **Slide 15 & 16 (Helicopter Drop-Box Cantilever Bracket Sizing):**
  - Section 6 (Problem 1, pp. 74–76 of Dr. Yousefi notes / Rao Ex. 4.18).
  - Equivalent mass: $m_{\text{eq}} = m_{\text{PCB}} + 0.23 \, m_{\text{beam}}$.
  - Stiffness: $k = \frac{E b d^3}{4 l^3}$, static deflection $\delta_{\text{st}} = \frac{W_{\text{eq}}}{k}$.
  - Dynamic load: $F_{\text{dyn}} = 100 \cdot \text{DLF} \cdot W_{\text{eq}}$, root stress $\sigma_{\max} = \frac{6 F_{\text{dyn}} l}{b d^2}$.
  - Iteration table: $d = 0.40''$ fails ($41.3\text{ ksi}$), $d = 0.50''$ fails ($34.3\text{ ksi}$), $d = 0.60''$ passes ($\sigma = 25.66\text{ ksi} \le 26\text{ ksi}$).
- **Slide 17 & 18 (Overhead Crane Vertical Seismic Derailment):**
  - Section 6 (Problem 2 / Rao Ex. 4.17 & Problem 4.57).
  - Normal wheel contact force: $N(t) = m(g - S_a)$.
  - Derailment criterion: $N_{\min} \le 0 \iff S_a \ge 1.0g$.
  - Counter-intuitive stiffness limit: Girder stiffness must satisfy $k < 365\text{ kN/m}$ ($\tau_n > 0.52\text{ s}$) to prevent seismic resonance and wheel lift-off.
- **Slide 19 & 20 (Automotive ECU PCB Resonant Amplification & Base Isolator):**
  - Section 6 (Problem 3 / Rao Ex. 9.10 & 9.11).
  - Unisolated fixed PCB: $351\%$ resonant amplification ($T_d = 3.51$) under $3600\text{ rpm}$ engine excitation.
  - SDOF Base Isolator: Tuned to $(k_{\text{iso}} = 24.66\text{ kN/m}, c_{\text{iso}} = 5.21\text{ N}\cdot\text{s/m})$ achieving $T_d \le 10\%$.

### 2. `docs/presentation_script_and_pacing.md` (Presenter Timing & Spoken Script)
- Consult Part 3 (Minutes 30:00 to 45:00) for exact spoken lines, timing budgets, and slide hand-off cues.
- Copy spoken cues directly into the `data-mobile-notes="..."` attribute of each `<section>` in `presentation/index.html`.

### 3. `AGENTS.md` (Mandatory AI Rules)
- Enforce the **4 Hard Visual Rules** (No top banners, spoken text in notes only, $\le 15$ English words per screen, one visual idea per screen).
- Review pure black background invariant (`self.camera.background_color = ManimColor("#000000")`) and academic color hex codes.

### 4. `docs/MANIM_GUIDE.md` (Rendering Pipeline)
- Review CLI rendering commands (`uv run manim -qm ...`), cuepoint planning, and asset naming conventions (`presentation/assets/videos/SLIDE_XX_SceneName.mp4`).

---

## 4. Step-by-Step Production Checklist for Part 3 Slides

For each slide assigned to Part 3 (Slides 15 to 21):

1. **Author the Manim Scene:**
   - Create `manim_scenes/part3/slide_XX_<topic>.py`.
   - Inherit from `Scene` and set `self.camera.background_color = ManimColor("#000000")`.
   - Design step cuepoints with deliberate `self.wait(...)` pauses.
2. **Render Production Video:**
   - Fast check: `uv run manim -qm manim_scenes/part3/slide_XX_<topic>.py <SceneName>`
   - Production freeze: `uv run manim -qh manim_scenes/part3/slide_XX_<topic>.py <SceneName>`
3. **Move Asset to Video Directory:**
   - Copy rendered MP4 to `presentation/assets/videos/SLIDE_XX_<SceneName>.mp4`.
4. **Update `presentation/index.html` (Part 3 Block):**
   - Populate `<video>` source, `data-cuepoints="..."`, `<div class="step" ...>`, and `data-mobile-notes="..."`.
5. **Verify Locally:**
   - Start local server (`python -m http.server 8000`) and test in browser (`http://localhost:8000/presentation/index.html`).
   - Press `Space` / `ArrowRight` to step through every cuepoint and ensure perfect audio-visual synchronization.

---

## 5. Synchronizing & Submitting Changes

### Keeping Your Branch Up to Date with `main`
Periodically pull changes made by the lead presenter on `main`:

```bash
git fetch origin
git merge origin/main
# or: git rebase origin/main
```
Because of strict file and DOM isolation, merges will execute smoothly without conflicts.

### Pushing Your Branch & Opening a PR
When your slide scenes and HTML implementations are ready:

```bash
git add manim_scenes/part3/
git add presentation/assets/videos/SLIDE_*
git add presentation/css/part3_theme.css
git add presentation/index.html
git commit -m "feat(part3): implement slides 15-21 and phase 3 visual styling"

git push -u origin part-3
```

Then open a Pull Request from `part-3` into `main` for review.

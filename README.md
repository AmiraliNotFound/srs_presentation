# Shock Response Spectrum (SRS) — Interactive Academic Presentation

**Course:** Mechanical Vibrations (Semester 5)  
**Institution:** School of Mechanical Engineering, University of Tehran  
**Format:** 45-Minute 3-Speaker Interactive Lecture Presentation  
**Technology Stack:** Zero-Flash HTML5 / Vanilla JS Presentation Engine, 60FPS Manim Community Animation Suite, TeX / KaTeX Mathematical Typography, FastAPI + WebSocket Companion Sync.

---

## 1. Project Overview & Scope

This repository houses the complete interactive lecture presentation on the **Shock Response Spectrum (SRS) and Transient Mechanical Shock Dynamics**. Designed for a 45-minute synchronized lecture delivered by three co-presenters, the deck replaces conventional bullet-point slide decks with edge-to-edge **3Blue1Brown-style mathematical animations**, precise frame-accurate cuepoint stepping, and an interactive mobile companion system for real-time student engagement.

### Curricular & Pedagogical Architecture

```
                                  45-MINUTE MASTER LECTURE
                                             │
             ┌───────────────────────────────┼───────────────────────────────┐
             ▼                               ▼                               ▼
     PART 1 (00–15 min)              PART 2 (15–30 min)              PART 3 (30–45 min)
   Physical Foundations &          Mathematical Machinery &          Design Resolution &
   The Motivating Challenge        Analytical SRS Derivation         Real-World Applications
             │                               │                               │
    • Harmonic vs. Shock            • Laplace Transfer H(s)          • Helicopter Dilemma Solved
    • Failure Modes (Yield/Fatigue) • Duhamel Convolution            • Bracket Sizing (d = 0.6")
    • 100g Drop Shock Scenario      • Forced vs. Residual Eras       • Crane Seismic Derailment
    • Cantilever Rayleigh SDOF      • Rectangular & Half-Sine        • ECU PCB Base Isolation
    • The Circular Dilemma Loop     • Asymptotic Spectrum Limits     • Live Mobile Quiz Review
```

### Current Development Status

| Section | Slides | Core Focus | Ownership | Status |
|---|---|---|---|:---:|
| **Part 1** | Slides 01–07 | Physical Intuition, Rayleigh SDOF & The Circular Dilemma | Lead Presenter (`main`) | **100% Complete & Rendered** |
| **Part 2** | Slides 08–14 | Laplace Domain, Duhamel Integral & Canonical SRS | Lead Presenter (`main`) | **Queued on `main`** |
| **Part 3** | Slides 15–21 | Helicopter Sizing, Crane Derailment & ECU Isolator | Colleague (`part-3`) | **Assigned on `part-3`** |
| **Phase 3** | Whole Deck | Visual Polish, TeX Typography & Custom Styling | Colleague (`part-3`) | **Queued on `part-3`** |
| **Phase 4** | Companion | FastAPI WebSocket Server & Live Audience Quizzes | Joint Team | **Queued** |

---

## 2. Quickstart: How to Run Locally

Because modern web browsers enforce strict security sandboxes (CORS) on video playback from the `file://` protocol, the presentation must be served through a local HTTP server.

### Running the Presentation Engine

1. Clone or pull the repository:
   ```bash
   git clone <REPO_URL>
   cd "#Presentations/#Ours"
   ```

2. Start a lightweight HTTP server:
   ```bash
   python -m http.server 8000
   ```

3. Open your browser to the presentation URL:
   ```
   http://localhost:8000/presentation/index.html
   ```

> [!IMPORTANT]
> Always access the deck via `http://localhost:8000/presentation/index.html`. Do not rely on relative root redirects if folder names in your path contain special characters (such as `#`), as unencoded hash symbols can truncate URL fragments and disrupt video source resolution.

### Keyboard & Presentation Controls

| Key | Action | Description |
|---|---|---|
| `Space` / `ArrowRight` | **Step Cuepoint / Next Slide** | Plays next video animation segment, or advances to next slide |
| `ArrowLeft` | **Previous Step / Slide** | Steps back to previous animation cuepoint or slide |
| `KeyF` | **Toggle Fullscreen** | Expands canvas to 16:9 edge-to-edge projection mode |
| `KeyH` | **Toggle Rehearsal HUD** | Shows/hides elapsed timer, slide timer, speaker badge, and scene name |
| `KeyL` | **Laser Pointer** | Toggles virtual presentation laser cursor |
| `Home` / `End` | **Deck Bounds** | Jumps directly to Slide 01 or Slide 21 |

---

## 3. Directory Layout

```
.
├── README.md                      # Master project overview & quickstart (this file)
├── CONTRIBUTING.md                # Git branching model, Part 3 workflow & collaboration rules
├── AGENTS.md                      # AI agent constraints, 4 hard visual rules & styling invariants
├── ROADMAP.md                     # Curricular roadmap, phase checklists & task status
├── Mechanical_Vibrations_Sample_Problems.pdf  # Course worked problems reference
├── docs/
│   ├── MANIM_GUIDE.md             # Manim Community setup, rendering flags & animation patterns
│   ├── presentation_script_and_pacing.md # Minute-by-minute speaking cues & cuepoints
│   └── syllabus_and_problems.md   # Mathematical derivations & worked numerical solutions
├── presentation/
│   ├── index.html                 # Main presentation stage (with isolated Part 1-2 & Part 3 blocks)
│   ├── css/
│   │   ├── style.css              # Master presentation styles (black background, HUD, typography)
│   │   └── part3_theme.css        # Modular CSS override hook for Part 3 & Phase 3 polish
│   ├── js/
│   │   └── main.js                # Slide transition controller, cuepoint engine & HUD sync
│   └── assets/
│       ├── images/                # Static diagrams and branding logos
│       └── videos/                # Tracked production Manim MP4 slide videos (SLIDE_*.mp4)
├── manim_scenes/
│   ├── common/                    # Shared Manim styles, color palettes & helper functions
│   ├── scenes/                    # Manim Python scene files for Parts 1 & 2 (Slides 01–14)
│   └── part3/                     # Manim Python scene files for Part 3 (Slides 15–21)
└── backend/
    └── main.py                    # FastAPI + WebSocket server for mobile quiz & sync
```

---

## 4. Manim Community Animation Pipeline

All visual animations are rendered mathematically via **Manim Community**.

```bash
# Activate environment via uv
uv run manim -qm manim_scenes/scenes/slide_01_title.py TitleCardScene

# Production high-DPI freeze (1080p60)
uv run manim -qh manim_scenes/scenes/slide_01_title.py TitleCardScene
```

Rendered slide videos are tracked under `presentation/assets/videos/SLIDE_XX_SceneName.mp4`. Refer to [`docs/MANIM_GUIDE.md`](file:///docs/MANIM_GUIDE.md) for full rendering parameters, background color requirements, and equation morphing rules.

---

## 5. Team & Academic Credits

- **Course:** Mechanical Vibrations (Fall 2024 / Semester 5)
- **Institution:** School of Mechanical Engineering, College of Engineering, University of Tehran
- **Course Instructor:** Dr. H. Yousefi
- **Reference Texts:** S. S. Rao, *Mechanical Vibrations* (6th Ed.); Dr. Yousefi Course Lecture Notes (Sessions 18 & 19).

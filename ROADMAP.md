# Shock Response Spectrum (SRS) Presentation — Master Roadmap

**Project:** Interactive HTML5 + Manim Presentation on Shock Response Spectrum (SRS)  
**Academic Context:** Mechanical Vibrations (Semester 5) — School of Mechanical Engineering, University of Tehran  
**Format:** 45-minute 3-speaker presentation (15 min each), local zero-flash HTML deck with embedded 60FPS Manim video renders and live mobile companion quiz sync.

---

## Project Lifecycle Status Board

| Phase | Description | Status | Progress |
|---|---|---|---|
| **Phase 0** | Workspace Foundation, Git Setup, PDF Extraction & Syllabus Synthesis | **COMPLETED** | 100% |
| **Phase 1** | Detailed 3-Speaker Allocation, 45-Min Timing Script & HTML Presentation Shell | **COMPLETED** | 100% |
| **Phase 2** | Production of Manim Animation Scenes & Interactive Slide Decks | **READY FOR EXECUTION** | 0% |
| **Phase 3** | Visual & Aesthetic Polish (TeX Typography, Theme Styling & UI Transitions) | **QUEUED** | 0% |
| **Phase 4** | FastAPI + WebSocket Mobile Companion, Audience Engagement & Live Quiz Sync | **QUEUED** | 0% |

---

## Detailed Phase Breakdown & Task Checklists

### [x] Phase 0: Project Setup, Git Init, & PDF Extraction
- [x] Initialize Git repository with strict hygiene rules.
- [x] Configure production `.gitignore` ignoring video binaries (`*.mp4`, `*.webm`), Manim caches (`media/`, `__pycache__/`), and OS clutter.
- [x] Set up standard URL-safe folder structure:
  - `docs/`
  - `presentation/` (`assets/`, `css/`, `js/`, `index.html`)
  - `manim_scenes/` (`common/`, `scenes/`)
  - `backend/`
- [x] Extract and transcribe primary syllabus from Dr. Yousefi Lecture Notes (Session 18 & 19, pp. 68–76).
- [x] Extract complementary physical insights and derivations from S. S. Rao (6th Edition, Chapter 4 & 9).
- [x] Transcribe and synthesize all 3 worked case studies from `Mechanical_Vibrations_Sample_Problems.pdf`.
- [x] Identify and formalize Problem 1 (Helicopter Drop-Box PCB Cantilever Bracket) as the Unifying Motivating Problem.
- [x] Compile master technical document: `docs/syllabus_and_problems.md`.

---

### [x] Phase 1: Detailed Syllabus Allocation, 45-Min Timing Script & Presentation Shell
- [x] **1.1 Speaker Allocation Matrix:**
  - **Person 1 (0:00 – 15:00):** Real-world shock phenomena, physical intuition, military standards (MIL-STD-810H), the Helicopter Drop-Box Motivating Problem, SDOF continuous-to-lumped Rayleigh reduction, and the circular design dilemma.
  - **Person 2 (15:00 – 30:00):** Mathematical machinery of transient vibrations, Laplace transform transfer function $H(s)$, Duhamel convolution integral, dual temporal eras (Era 1 Forced vs. Era 2 Residual), analytical derivations for Rectangular & Half-Sine pulses, and SRS spectrum properties.
  - **Person 3 (30:00 – 45:00):** Step-by-step numerical iterative solution of the Helicopter Drop-Box Bracket ($d = 0.6\text{ in}$), Overhead Crane earthquake derailment analysis ($S_a < 1.0g$, stiffness ceiling $k < 365\text{ kN/m}$), Automotive ECU PCB isolation ($T_d \le 10\%$), audience live quiz, and concluding Q&A.
- [x] **1.2 45-Minute Synchronized Cue Script:**
  - Minute-by-minute speaking cues, slide transition triggers, and interactive pause points in `docs/presentation_script_and_pacing.md`.
- [x] **1.3 Minimalist HTML5 Presentation Engine:**
  - Build zero-flash slide runner in `presentation/index.html` with vanilla JavaScript controller (`presentation/js/main.js`).
  - Implement keyboard navigation (`ArrowRight`, `ArrowLeft`, `Space`, `F` for fullscreen, `L` for laser pointer, `Home`, `End`).
  - Add video synchronization with automatic play/pause, loop controls, next-video background preloading, and wireframe fallback visuals.
  - Create high-contrast dark academic styling (`presentation/css/style.css`) incorporating University of Tehran Mechanical Engineering accent palette (`#0097F1`).

---

### [ ] Phase 2: Iterative Slide & Manim Scene Production

#### Slide & Scene Production Matrix

| Slide ID | Speaker | Slide Title / Core Topic | Manim Scene Class | Render Status | Integration Status |
|---|---|---|---|:---:|:---:|
| **SLIDE-01** | Person 1 | Title Slide: Shock Response Spectrum & Transient Dynamics | `TitleCardScene` | [ ] | [ ] |
| **SLIDE-02** | Person 1 | Harmonic Vibration vs. Shock Loading: Why Statics Fails | `HarmonicVsShockScene` | [ ] | [ ] |
| **SLIDE-03** | Person 1 | Real-World Shock Environments & Military Testing Standards | `ShockTaxonomyScene` | [ ] | [ ] |
| **SLIDE-04** | Person 1 | The Motivating Problem: Helicopter Drop-Box Avionics | `HelicopterDropScene` | [ ] | [ ] |
| **SLIDE-05** | Person 1 | SDOF Idealization: Continuous Cantilever to Lumped Mass | `RayleighSDOFScene` | [ ] | [ ] |
| **SLIDE-06** | Person 1 | The Circular Design Dilemma: The Need for SRS | `CircularDilemmaScene` | [ ] | [ ] |
| **SLIDE-07** | Person 2 | Governing Equation & Laplace Transform Transfer Function | `LaplaceTransferScene` | [ ] | [ ] |
| **SLIDE-08** | Person 2 | Impulse Response Function & The Duhamel Convolution | `DuhamelConvolutionScene` | [ ] | [ ] |
| **SLIDE-09** | Person 2 | Two Temporal Eras: Forced ($t \le t_0$) vs. Residual ($t > t_0$) | `DualEraPartitionScene` | [ ] | [ ] |
| **SLIDE-10** | Person 2 | Rectangular Pulse Response & Peak Derivation | `RectangularPulseScene` | [ ] | [ ] |
| **SLIDE-11** | Person 2 | Half-Sine Shock Pulse: Era 1 & Era 2 Analytical Solution | `HalfSineAnalyticalScene` | [ ] | [ ] |
| **SLIDE-12** | Person 2 | Constructing the Shock Response Spectrum (SRS) | `SRSConstructionScene` | [ ] | [ ] |
| **SLIDE-13** | Person 2 | Asymptotic Master Insight: Impulsive vs. Quasi-Static Limits | `AsymptoticLimitsScene` | [ ] | [ ] |
| **SLIDE-14** | Person 3 | Hand-Off Resolution: Closing the Motivating Problem Loop | `IterativeDesignScene` | [ ] | [ ] |
| **SLIDE-15** | Person 3 | Bracket Thickness Sizing: Evaluating $d = 0.4'', 0.5'', 0.6''$ | `StressVerificationScene` | [ ] | [ ] |
| **SLIDE-16** | Person 3 | Case Study 2: Overhead Crane Vertical Seismic Derailment | `CraneSeismicScene` | [ ] | [ ] |
| **SLIDE-17** | Person 3 | Counter-Intuitive Stiffness: Why Softer Girders Prevent Derailment | `CraneStiffnessLimitScene` | [ ] | [ ] |
| **SLIDE-18** | Person 3 | Case Study 3: Automotive ECU PCB Resonant Amplification | `ECUResonanceScene` | [ ] | [ ] |
| **SLIDE-19** | Person 3 | Base Isolator Design: Tuning $(k_{\text{iso}}, c_{\text{iso}})$ for $T_d \le 10\%$ | `ECUIsolatorScene` | [ ] | [ ] |
| **SLIDE-20** | Person 3 | Master Synthesis, Live Audience Mobile Quiz & Conclusion | `MasterSummaryScene` | [ ] | [ ] |

---

### [ ] Phase 3: Visual & Aesthetic Polish
- [ ] Standardize typography with MathJax / KaTeX and Century Gothic fonts.
- [ ] Implement smooth 3Blue1Brown-style `TransformMatchingTex` transitions across all mathematical derivation steps.
- [ ] Embed university branding and color scheme: Primary Blue (`#0097F1`), Dark Slate Navy (`#0B0F19`), Accent Amber (`#FFB703`), Pass Green (`#2EC4B6`), Fail Red (`#E63946`).
- [ ] Ensure high-DPI (1080p60 / 4K) crisp rendering with zero compression banding.
- [ ] Implement responsive layout adjustments for lecture hall projection (16:9 aspect ratio).

---

### [ ] Phase 4: FastAPI + WebSocket Companion & Live Quiz Sync
- [ ] **4.1 Companion Backend Architecture:**
  - FastAPI server located in `backend/main.py`.
  - WebSocket hub broadcasting live slide state to student smartphones via QR code.
- [ ] **4.2 Interactive Audience Quizzes:**
  - **Quiz 1 (Person 1 Hand-Off):** "What happens to the cantilever bracket root stress if we double thickness $d$?"
  - **Quiz 2 (Person 2 Hand-Off):** "At what pulse-to-period ratio $t_0/\tau_n$ does a rectangular pulse produce zero residual vibration?"
  - **Quiz 3 (Person 3 Hand-Off):** "Why does making the crane girder stiffer increase derailment danger in an earthquake?"
- [ ] **4.3 Live Polling Display:**
  - Real-time animated bar chart overlay on the main presentation display showing aggregated audience responses.

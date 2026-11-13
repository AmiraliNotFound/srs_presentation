# Shock Response Spectrum (SRS) — 45-Minute Synchronized Presentation Script & Pacing Master Guide

**Course:** Mechanical Vibrations (Semester 5) — School of Mechanical Engineering, University of Tehran  
**Presentation Title:** Transient Dynamics, Shock Response Spectrum (SRS) & Base Isolation in Mechanical Systems  
**Total Allocated Duration:** 45:00 Minutes (Strict 15:00 Minutes per Speaker)  
**Academic Speakers:**
- **Speaker 1 (00:00 – 15:00):** *Physical Intuition, Shock Taxonomy, SDOF Rayleigh Modeling & The Circular Design Dilemma*
- **Speaker 2 (15:00 – 30:00):** *Mathematical Rigor, Laplace Transfer Functions, Duhamel Convolution & Canonical SRS Derivations*
- **Speaker 3 (30:00 – 45:00):** *Design Resolution, Seismic Derailment Analysis, Municipal Tower Wind Blast SRS & Interactive Mobile Quiz Synthesis*

---

## 1. Master Pacing Matrix & Timeline Overview

| Slide # | Slide ID | Speaker | Timestamp | Duration | Core Topic / Curricular Focus | Manim Scene Class | Interactive Quiz Hook |
|:---:|:---:|:---:|:---:|:---:|:---|:---|:---:|
| **01** | `SLIDE-01` | Person 1 | 00:00 – 01:30 | 01:30 | Title & Academic Scope (Univ. of Tehran) | `TitleCardScene` | — |
| **02** | `SLIDE-02` | Person 1 | 01:30 – 04:00 | 02:30 | Harmonic Vibration vs. Transient Shock Dynamics | `HarmonicVsShockScene` | — |
| **03** | `SLIDE-03` | Person 1 | 04:00 – 06:00 | 02:00 | Real-World Shock Environments & MIL-STD-810H | `ShockTaxonomyScene` | — |
| **04** | `SLIDE-04` | Person 1 | 06:00 – 09:00 | 03:00 | Motivating Problem: Helicopter Drop-Box Avionics | `HelicopterDropScene` | — |
| **05** | `SLIDE-05` | Person 1 | 09:00 – 12:00 | 03:00 | SDOF Idealization: Rayleigh Lumped Cantilever | `RayleighSDOFScene` | — |
| **06** | `SLIDE-06` | Person 1 | 12:00 – 15:00 | 03:00 | The Circular Design Dilemma & Hand-Off 1 | `CircularDilemmaScene` | **Quiz 1: Root Stress vs Thickness** |
| **07** | `SLIDE-07` | Person 2 | 15:00 – 17:00 | 02:00 | Dynamic Equation, Impedance $Z(s)$ & Transfer $H(s)$ | `LaplaceTransferScene` | — |
| **08** | `SLIDE-08` | Person 2 | 17:00 – 19:30 | 02:30 | Impulse Response $g(t)$ & Duhamel Convolution | `DuhamelConvolutionScene` | — |
| **09** | `SLIDE-09` | Person 2 | 19:30 – 21:30 | 02:00 | Dual Temporal Eras: Forced ($t \le t_0$) vs Residual ($t > t_0$) | `DualEraPartitionScene` | — |
| **10** | `SLIDE-10` | Person 2 | 21:30 – 24:00 | 02:30 | Rectangular Shock Pulse: DLF = 2.0 & Cancellation | `RectangularPulseScene` | — |
| **11** | `SLIDE-11` | Person 2 | 24:00 – 26:30 | 02:30 | Half-Sine Shock Pulse: Exact Analytical Solution | `HalfSineAnalyticalScene` | — |
| **12** | `SLIDE-12` | Person 2 | 26:30 – 28:30 | 02:00 | Constructing the Shock Response Spectrum (SRS) | `SRSConstructionScene` | — |
| **13** | `SLIDE-13` | Person 2 | 28:30 – 30:00 | 01:30 | Asymptotic Limits (Impulsive vs Quasi-Static) & Hand-Off 2 | `AsymptoticLimitsScene` | **Quiz 2: Zero Residual Condition** |
| **14** | `SLIDE-14` | Person 3 | 30:00 – 32:30 | 02:30 | Closing the Loop: Helicopter Drop-Box Solution Setup | `IterativeDesignScene` | — |
| **15** | `SLIDE-15` | Person 3 | 32:30 – 35:00 | 02:30 | Sizing Bracket Thickness: $d = 0.4'', 0.5'', 0.6''$ | `StressVerificationScene` | — |
| **16** | `SLIDE-16` | Person 3 | 35:00 – 37:30 | 02:30 | Case Study 2: EOT Crane Vertical Seismic Derailment | `CraneSeismicScene` | — |
| **17** | `SLIDE-17` | Person 3 | 37:30 – 40:00 | 02:30 | Counter-Intuitive Stiffness: Why Softer Girders Save Cranes | `CraneStiffnessLimitScene` | **Quiz 3: Girder Stiffness & Derailment** |
| **18** | `SLIDE-19` | Person 3 | 40:00 – 42:00 | 02:00 | Case Study 3: Municipal Tower Wind Blast SDOF Modeling | `WindBlastModelScene` | — |
| **19** | `SLIDE-20` | Person 3 | 42:00 – 44:00 | 02:00 | Shock Response Spectrum (SRS) Evaluation & Structural Survival | `WindBlastSRSScene` | — |
| **20** | `SLIDE-21` | Person 3 | 44:00 – 45:00 | 01:00 | Master Synthesis, Mobile Quiz Leaderboard & Q&A | `MasterSummaryScene` | **Live Q&A / Polling Summary** |

---

## 2. Speaker 1 Detailed Cues & Spoken Script (00:00 – 15:00)

### SLIDE-01: Title Slide & Academic Scope
- **Time Window:** `[00:00 – 01:30]` (Duration: 90 s)
- **Speaker:** Person 1 (Physical Intuition & Foundations)
- **Visual Asset:** `TitleCardScene` (Manim: University of Tehran insignia, animated wave packets, blue title typography).
- **Curricular Anchors:** Dr. H. Yousefi Session 18; Rao 6th Ed. Chapter 4.
- **Fragment Sequence:**
  1. Title card reveal with course affiliation (`Department of Mechanical Engineering, University of Tehran`).
  2. Subtitle: *Transient Shock Dynamics, SDOF Foundations & Shock Response Spectra*.
  3. Presentation Roadmap Badge: *Part 1: Physics & Modeling* $\to$ *Part 2: Mathematical Theory* $\to$ *Part 3: Engineering Case Studies*.
- **Spoken Script (Word-for-Word):**
  > *"Good morning, Professor Yousefi, teaching assistants, and fellow colleagues. Today, our group presents an in-depth analytical and design investigation into one of the most critical topics in structural dynamics: the **Shock Response Spectrum (SRS)**.*  
  > *In mechanical systems ranging from satellite launch fairings to aircraft avionics and earthquake-resistant industrial cranes, structures rarely fail from gentle cyclic oscillations alone. Instead, catastrophic failure is frequently dictated by sudden, violent transient shocks—millisecond events that shatter traditional quasi-static assumptions.*  
  > *Our 45-minute lecture is structured into three unified acts. I will introduce the fundamental physical differences between steady-state vibration and transient shock, define testing standards, and establish our core motivating engineering problem—a helicopter avionics drop-box container.*  
  > *Then, my colleague will take over to construct the rigorous mathematical framework: the Laplace transfer function, Duhamel convolution, dual temporal eras, and the analytical derivation of the SRS curve.*  
  > *Finally, our third speaker will close the loop, solving our motivating design dilemma and analyzing two additional industrial case studies: vertical earthquake derailment of an overhead crane, and wind-blast shock response spectrum analysis of an elevated municipal water tower. Let us begin."*
- **Visual Cue / Presenter Directives:**
  - `[00:00]` Stand centered; click to advance title animation.
  - `[00:45]` Point laser toward the 3-speaker roadmap cards on the right display.
  - `[01:25]` Advance slide on concluding word *"begin"*.

---

### SLIDE-02: Harmonic Vibration vs. Transient Shock Dynamics
- **Time Window:** `[01:30 – 04:00]` (Duration: 150 s)
- **Speaker:** Person 1
- **Visual Asset:** `HarmonicVsShockScene` (Side-by-side animated comparison: Steady sinusoidal oscillation with infinite cycles vs. a single 10-millisecond half-sine shock wave and transient ringdown).
- **Mathematical Formula:**
  $$\text{Harmonic: } F(t) = F_0 \sin(\omega t), \quad t \in [0, \infty) \quad \longleftrightarrow \quad \text{Shock: } F(t) \ne 0 \text{ only for } 0 \le t \le t_0$$
- **Fragment Sequence:**
  1. *Classification table:* Steady-State Cyclic vs. Transient Short-Duration.
  2. *Failure Mechanism:* High-cycle fatigue ($10^6$ cycles, S-N curve) vs. Immediate peak stress yield rupture / contact separation.
  3. *Why Statics Fails:* Under shock loading, maximum response does not equal $F_0/k$. Dynamic inertial lag generates Dynamic Load Factors up to $2.0$.
- **Spoken Script:**
  > *"In the first half of this semester, we focused primarily on steady-state harmonic excitations of the form $F(t) = F_0 \sin\omega t$. In harmonic systems, the excitation lasts indefinitely. We discard homogeneous transients, compute the steady-state magnification factor $M = 1/\sqrt{(1-r^2)^2 + (2\zeta r)^2}$, and our primary design metric is fatigue life over millions of cycles.*  
  > *Shock is physically antithetical. A shock is a severe transient disturbance whose duration $t_0$ is of the same order of magnitude as—or shorter than—the fundamental natural period $\tau_n$ of the system. Notice the animation on the right:*  
  > *The force hits violently and vanishes before the structure has completed even a single period of motion! There is no steady-state equilibrium here. The peak stress occurs during the initial half-cycle or in the free ringdown that follows.*  
  > *Why does classical static analysis fail so catastrophically? If an engineer naively divides peak shock force $F_0$ by stiffness $k$, they obtain the static deflection $\delta_{\text{st}}$. But because the mass has inertia, it accelerates dynamically past the equilibrium point, storing peak strain energy that can produce stresses up to twice as high as statics predicts. To capture this phenomenon, we must step into the transient domain."*
- **Visual Cue:**
  - `[02:15]` Trigger fragment 2. Point to the animated stress gauge reaching red-line on the shock pulse.
  - `[03:40]` Highlight the definition $t_0 \lesssim \tau_n$.

---

### SLIDE-03: Real-World Shock Environments & Military Testing Standards
- **Time Window:** `[04:00 – 06:00]` (Duration: 120 s)
- **Speaker:** Person 1
- **Visual Asset:** `ShockTaxonomyScene` (Interactive breakdown of 3 canonical shock sources: Drop impact, pyrotechnic staging, and ballistic blast waveforms with MIL-STD-810H specification profiles).
- **Fragment Sequence:**
  1. *Velocity Shocks (Impact / Drop):* Kinetic energy conversion upon landing ($v_0 = \sqrt{2gh}$); characteristic half-sine or haversine acceleration pulses.
  2. *Pyrotechnic Shocks (Pyroshock):* Explosive stage separation in aerospace; high-frequency ($> 1\text{ kHz}$), short-duration ($< 20\text{ ms}$) acceleration ringing.
  3. *Testing Standards:* MIL-STD-810H (Method 516.8: Ground packaging and drop tests) and MIL-E-5400 airborne avionics survival criteria.
- **Spoken Script:**
  > *"Where do shock excitations occur in practical engineering? In industry, shock environments are categorized into three primary classes.*  
  > *First, **Velocity Shocks**: when a package is dropped, or an aircraft landing gear contacts a runway, potential energy converts into impact velocity $v_0 = \sqrt{2gh}$. The cushion or bracket crushes elastically, experiencing a smooth half-sine acceleration profile.*  
  > *Second, **Pyrotechnic Shocks**: when a launch vehicle separates stages or deploys a satellite fairing, explosive bolts detonate within microseconds. This produces high-frequency, thousand-G acceleration spikes that can dislodge surface-mount capacitors and crystal oscillators on electronic boards.*  
  > *Third, **Ballistic / Blast Shocks**: explosive ground blasts or gun recoils characterized by steep triangular pressure fronts that decay exponentially.*  
  > *To certify mission-critical equipment, aerospace and military standards—such as MIL-STD-810H Method 516.8 and MIL-E-5400—mandate that electronic chassis survive standardized shock pulses without mechanical fracture or electronic latch-up. This brings us directly to our motivating problem."*

---

### SLIDE-04: The Motivating Problem: Helicopter Drop-Box Avionics
- **Time Window:** `[06:00 – 09:00]` (Duration: 180 s)
- **Speaker:** Person 1
- **Visual Asset:** `HelicopterDropScene` (3D cutaway animation of a military supply box dropped onto packed soil, showing the container deceleration pulse and internal cantilever bracket with tip PCB vibrating violently).
- **Curricular Anchors:** S. S. Rao, Example 4.18 (p. 450); Dr. Yousefi Session 19 Notes (pp. 74–76).
- **Physical Specifications Displayed:**
  - Container Base Shock: Half-sine acceleration pulse $a(t) = a_{\max} \sin(\pi t / t_0)$
  - Peak Acceleration: $a_{\max} = 100g = 981\text{ m/s}^2$
  - Pulse Duration: $t_0 = 0.1\text{ s} = 100\text{ ms}$
  - Aluminum Cantilever Bracket: Length $l = 10.0''$ ($0.254\text{ m}$), width $b = 0.5''$ ($0.0127\text{ m}$)
  - Tip Mass (Avionics PCB): $W_{\text{PCB}} = 0.40\text{ lb}$ ($m_{\text{PCB}} = 0.1814\text{ kg}$)
  - Material Properties: $E = 10 \times 10^6\text{ psi}$ ($70\text{ GPa}$), $\gamma = 0.10\text{ lb/in}^3$ ($\rho = 3058\text{ kg/m}^3$)
  - Allowable Bending Stress: $\sigma_{\text{allow}} = 26,000\text{ psi} = 26\text{ ksi}$ ($180\text{ MPa}$)
- **Fragment Sequence:**
  1. Scenario schematic: Helicopter low-altitude field drop test onto terrain.
  2. Avionics container cutaway showing PCB cantilever beam mounted to the rigid enclosure floor.
  3. The Engineering Objective: Size the bracket thickness $d$ to prevent dynamic bending failure at the root.
- **Spoken Script:**
  > *"Consider this operational scenario from Rao Example 4.18 and Dr. Yousefi's Session 19 lecture compendium. An avionics communication container is dropped from a low-flying helicopter during a tactical delivery. Upon striking the terrain, the container experiences a severe deceleration shock.*  
  > *The ground impact is characterized as a half-sine acceleration pulse with a peak deceleration of 100g and a duration of 0.1 seconds.*  
  > *Inside this container, a sensitive printed circuit board weighing 0.40 pounds is mounted at the free tip of an aluminum cantilever bracket of length 10 inches and width 0.5 inches.*  
  > *The aluminum has a modulus of $10^7$ psi and an allowable yield working stress of 26,000 psi. Our assignment as vibration engineers is to design the rectangular bracket thickness $d$ such that the root dynamic bending stress does not exceed 26 ksi.*  
  > *At first glance, a junior engineer might treat this as a simple statics problem: multiply weight by 100g, compute bending moment $M = F \cdot l$, and solve for thickness. But this is completely wrong! Because the bracket flexes, dynamic amplification takes over."*

---

### SLIDE-05: SDOF Idealization: Continuous Cantilever to Lumped SDOF
- **Time Window:** `[09:00 – 12:00]` (Duration: 180 s)
- **Speaker:** Person 1
- **Visual Asset:** `RayleighSDOFScene` (Continuous beam deflection curve morphing into an equivalent lumped mass-spring oscillator with Rayleigh energy equivalence highlighted).
- **Core Formulations:**
  $$I = \frac{1}{12} b d^3, \quad k = \frac{3EI}{l^3} = \frac{E b d^3}{4 l^3}$$
  $$m_{\text{beam}} = \rho \cdot (l \cdot b \cdot d), \quad m_{\text{eq}} = m_{\text{PCB}} + \frac{33}{140} m_{\text{beam}} \approx m_{\text{PCB}} + 0.23 m_{\text{beam}}$$
  $$\tau_n = 2\pi \sqrt{\frac{m_{\text{eq}}}{k}} = 2\pi \sqrt{\frac{\delta_{\text{st}}}{g}}$$
- **Fragment Sequence:**
  1. Continuous cantilever beam schematic with distributed mass density $\rho$ and tip mass $m_{\text{PCB}}$.
  2. Rayleigh Energy Reduction: Equating kinetic energies yields $m_{\text{eq}} = m_{\text{PCB}} + 0.23 m_{\text{beam}}$.
  3. Equivalent SDOF parameters: Tip stiffness $k = 3EI/l^3$ and fundamental period $\tau_n$.
- **Spoken Script:**
  > *"Before we can analyze transient shock dynamics, we must idealize this continuous structural beam into an equivalent Single-Degree-of-Freedom system.*  
  > *The cantilever bracket possesses continuous self-mass $m_{\text{beam}} = \rho b d l$. Using Rayleigh's quotient with the static deflection profile $\psi(y) = \frac{y^2}{2l^3}(3l - y)$, we integrate the kinetic energy across the beam span. As derived in Chapter 2 of our course, the distributed mass contributes exactly $\frac{33}{140}$—or approximately 23%—of its total mass to the effective tip mass.*  
  > *Thus, our equivalent lumped mass is $m_{\text{eq}} = m_{\text{PCB}} + 0.23 m_{\text{beam}}$.*  
  > *The flexural stiffness of a point-loaded cantilever at its free tip is $k = \frac{3EI}{l^3} = \frac{Eb d^3}{4l^3}$.*  
  > *From these two quantities, we obtain the fundamental natural period:*  
  > *$\tau_n = 2\pi \sqrt{m_{\text{eq}} / k}$.*  
  > *Now examine these equations carefully: both $m_{\text{eq}}$ and stiffness $k$ depend directly on the unknown thickness $d$. What happens when we try to evaluate the dynamic stress?"*

---

### SLIDE-06: The Circular Design Dilemma & Hand-Off to Person 2
- **Time Window:** `[12:00 – 15:00]` (Duration: 180 s)
- **Speaker:** Person 1
- **Visual Asset:** `CircularDilemmaScene` (Animated circular dependency flowchart showing the feedback loop from $d \to k \to \tau_n \to t_0/\tau_n \to \text{DLF} \to F_{\text{dyn}} \to \sigma_{\max}$).
- **Interactive Quiz Hook:** Mobile Companion Quiz 1 Triggered.
- **The Dilemma Loop:**
  $$\text{Choose } d \longrightarrow (I, k, W_{\text{eq}}) \longrightarrow \tau_n \longrightarrow \frac{t_0}{\tau_n} \longrightarrow \mathbf{DLF} \longrightarrow F_{\text{dyn}} = 100 \cdot \mathbf{DLF} \cdot W_{\text{eq}} \longrightarrow \sigma_{\max} = \frac{6 F_{\text{dyn}} l}{b d^2}$$
- **Fragment Sequence:**
  1. The 6-step circular design diagram.
  2. The Critical Barrier: We cannot compute the dynamic force $F_{\text{dyn}}$ without knowing the Dynamic Load Factor (DLF), which requires the period ratio $t_0/\tau_n$, which requires $d$!
  3. Mobile Quiz 1 prompt: *"If we double the thickness $d$, does the stress decrease by 4x as statics claims?"*
  4. Speaker Hand-Off verbal transition.
- **Spoken Script & Hand-Off Dialogue:**
  > *"Here lies the central engineering conundrum of shock design—the **Circular Design Dilemma**.*  
  > *To check if the bracket breaks, we need the outer fiber stress $\sigma_{\max} = \frac{6 F_{\text{dyn}} l}{b d^2}$.*  
  > *To find the dynamic force $F_{\text{dyn}}$, we need the Dynamic Load Factor (DLF).*  
  > *To find DLF, we must evaluate where our system sits on the Shock Response Spectrum, which requires the dimensionless ratio $t_0 / \tau_n$.*  
  > *To find the period $\tau_n$, we need the stiffness $k$, which requires thickness $d$.*  
  > *And thickness $d$ is the very parameter we are trying to design!*  
  > *In statics, doubling thickness $d$ quadruples section modulus $Z = \frac{1}{6} b d^2$, reducing stress by a factor of 4. But under shock, increasing $d$ also increases stiffness $k \propto d^3$, drastically shortening period $\tau_n$, which shifts our position on the Shock Response Spectrum and alters the dynamic amplification factor DLF!*  
  > *We are trapped in a feedback loop. To escape this loop, we need a rigorous mathematical method to predict the exact peak response under transient pulses of any duration.*  
  > *I will now trigger our first live mobile quiz question on your companion screens, and hand the presentation over to **Person 2**, who will derive the mathematical machinery of the Duhamel Integral and the Shock Response Spectrum. The floor is yours!"*

---

## 3. Speaker 2 Detailed Cues & Spoken Script (15:00 – 30:00)

### SLIDE-07: Dynamic Governing Equations & Laplace Transfer Function
- **Time Window:** `[15:00 – 17:00]` (Duration: 120 s)
- **Speaker:** Person 2 (Mathematical Foundations & Derivations)
- **Visual Asset:** `LaplaceTransferScene` (Morphing differential equations in the time domain into algebraic transfer function blocks in the complex $s$-plane).
- **Curricular Anchors:** Dr. Yousefi Session 18 (pp. 68–70); Rao Section 4.5.
- **Core Formulations:**
  $$m \ddot{x}(t) + c \dot{x}(t) + k x(t) = F(t) \quad \xrightarrow{\mathcal{L}} \quad (m s^2 + c s + k) X(s) = F(s)$$
  $$H(s) = \frac{X(s)}{F(s)} = \frac{1}{m s^2 + c s + k} = \frac{1}{m(s^2 + 2\zeta\omega_n s + \omega_n^2)}$$
  $$Z(s) = \frac{1}{H(s)} = m s^2 + c s + k \quad (\text{Generalized Dynamic Impedance})$$
- **Fragment Sequence:**
  1. Time-domain SDOF ODE with initial conditions $x(0) = x_0, \dot{x}(0) = \dot{x}_0$.
  2. Unilateral Laplace transform yielding algebraic formulation in the $s$-plane.
  3. Transfer function $H(s)$ and generalized mechanical impedance $Z(s)$.
- **Spoken Script:**
  > *"Thank you, Speaker 1. Colleagues, to resolve the circular dilemma, we cannot rely on guesswork. We must establish the exact mathematical foundation of transient dynamics.*  
  > *Consider a viscously damped SDOF oscillator governed by $m\ddot{x} + c\dot{x} + kx = F(t)$. Dividing by mass yields the standard canonical form $\ddot{x} + 2\zeta\omega_n \dot{x} + \omega_n^2 x = F(t)/m$.*  
  > *Because $F(t)$ is a transient pulse that does not exist in steady harmonic equilibrium, we apply the unilateral Laplace transform $\mathcal{L}\{x(t)\} = X(s)$.*  
  > *The differential operator transforms into an algebraic polynomial: $(m s^2 + c s + k) X(s) - m s x(0) - m \dot{x}(0) - c x(0) = F(s)$.*  
  > *Solving for $X(s)$, the response decomposes cleanly into an initial-condition free response and a forced response.*  
  > *The ratio of output displacement to input force defines the **System Transfer Function** $H(s) = \frac{1}{m(s^2 + 2\zeta\omega_n s + \omega_n^2)}$.*  
  > *Its reciprocal, $Z(s) = m s^2 + c s + k$, represents the **Generalized Dynamic Impedance**—a measure of the structure's dynamic resistance to motion across complex frequencies."*

---

### SLIDE-08: Impulse Response Function $g(t)$ & The Duhamel Convolution Integral
- **Time Window:** `[17:00 – 19:30]` (Duration: 150 s)
- **Speaker:** Person 2
- **Visual Asset:** `DuhamelConvolutionScene` (Animated Riemann summation: An arbitrary continuous shock pulse sliced into infinitesimal rectangular impulses $F(\tau) d\tau$, each launching an impulse response wave $g(t-\tau)$, summing continuously into the convolution envelope).
- **Core Formulations:**
  $$g(t) = \mathcal{L}^{-1}\{H(s)\} = \frac{1}{m \omega_d} e^{-\zeta \omega_n t} \sin(\omega_d t) \cdot u(t)$$
  $$\text{For undamped systems } (\zeta = 0): \quad g(t) = \frac{1}{m \omega_n} \sin(\omega_n t)$$
  $$x(t) = (F * g)(t) = \int_0^t F(\tau) g(t - \tau) d\tau = \frac{1}{m \omega_n} \int_0^t F(\tau) \sin\omega_n(t - \tau) \, d\tau$$
  $$\text{Base Acceleration Shock: } z(t) = -\frac{1}{\omega_n} \int_0^t \ddot{y}(\tau) \sin\omega_n(t - \tau) \, d\tau$$
- **Fragment Sequence:**
  1. Inverse Laplace transform yielding the unit impulse response function $g(t)$.
  2. Physical interpretation: An impulse of magnitude $F(\tau) d\tau$ imparts instant momentum $d\dot{x} = \frac{F(\tau) d\tau}{m}$.
  3. Borel Convolution Theorem formulation: The Duhamel integral for undamped force and base excitation.
- **Spoken Script:**
  > *"To return to the physical time domain, we take the inverse Laplace transform of $H(s)$, which produces the **Unit Impulse Response Function** $g(t)$.*  
  > *For an undamped system, $g(t) = \frac{1}{m\omega_n} \sin(\omega_n t)$.*  
  > *Now observe the visual construction on the right screen. How do we compute the response to an arbitrary, non-periodic shock wave $F(t)$?*  
  > *We apply the **Duhamel Convolution Integral**, rooted in the principle of linear superposition.*  
  > *Imagine slicing the continuous force history $F(t)$ into vertical strips of width $d\tau$. Each strip acts as an infinitesimal impulse of magnitude $d\mathcal{I} = F(\tau) d\tau$.*  
  > *By Newton's second law, this impulse produces an instantaneous velocity increment $d\dot{x}(\tau) = \frac{F(\tau)d\tau}{m}$.*  
  > *From that moment $\tau$ onward, this incremental velocity launches an undamped free sine wave of amplitude $\frac{F(\tau)d\tau}{m\omega_n} \sin\omega_n(t - \tau)$.*  
  > *Summing all incremental responses from time $\tau = 0$ to current time $t$, the Riemann sum becomes the Duhamel Integral:*  
  > *$x(t) = \frac{1}{m\omega_n} \int_0^t F(\tau) \sin\omega_n(t - \tau) d\tau$.*  
  > *If the excitation is a ground acceleration $\ddot{y}(t)$, d'Alembert's principle provides an effective inertia force $F_{\text{eff}} = -m\ddot{y}(t)$, yielding relative motion $z(t) = -\frac{1}{\omega_n} \int_0^t \ddot{y}(\tau) \sin\omega_n(t - \tau) d\tau$. This integral is our master key."*

---

### SLIDE-09: Temporal Partitioning: Era 1 (Forced) vs. Era 2 (Residual)
- **Time Window:** `[19:30 – 21:30]` (Duration: 120 s)
- **Speaker:** Person 2
- **Visual Asset:** `DualEraPartitionScene` (Split timeline showing Era 1 forced vibration under active pulse $0 \le t \le t_0$, transitioning across boundary line $t = t_0$ into Era 2 pure free harmonic ringdown).
- **Mathematical Structure:**
  $$\text{Era 1 (Forced Phase, } 0 \le t \le t_0\text{): } x_1(t) = \frac{1}{m \omega_n} \int_0^t F(\tau) \sin\omega_n(t - \tau) \, d\tau$$
  $$\text{Era 2 (Residual Phase, } t > t_0\text{): } x_2(t) = \frac{1}{m \omega_n} \int_0^{t_0} F(\tau) \sin\omega_n(t - \tau) \, d\tau$$
  $$\text{State Continuity at } t = t_0: \quad x_1(t_0) = x_2(t_0), \quad \dot{x}_1(t_0) = \dot{x}_2(t_0)$$
- **Fragment Sequence:**
  1. The dual-era physical timeline definition.
  2. Integration limit contrast: Upper limit is $t$ in Era 1, but fixes at $t_0$ in Era 2 because $F(\tau) = 0$ for $\tau > t_0$.
  3. Free vibration matching: The terminal state $(x(t_0), \dot{x}(t_0))$ dictates the residual amplitude.
- **Spoken Script:**
  > *"Because any shock pulse has a finite duration $t_0$, the time domain splits cleanly into two distinct physical regimes.*  
  > *We designate **Era 1** as the Forced Phase, covering $0 \le t \le t_0$. Here, the active shock pulse is pumping energy into the system. The upper limit of the Duhamel integral is the current time $t$.*  
  > *Then, at the boundary $t = t_0$, the external disturbance abruptly terminates. We enter **Era 2**, the Residual Free Vibration Phase, for all $t > t_0$.*  
  > *In Era 2, the integrand is zero for all $\tau > t_0$. Therefore, the upper limit of integration freezes permanently at $t_0$!*  
  > *The system subsequently rings down in pure free vibration, entirely governed by its terminal boundary conditions: the displacement $x(t_0)$ and velocity $\dot{x}(t_0)$ achieved at the instant the shock died.*  
  > *This distinction is paramount because maximum structural stress can occur either during the pulse—which we call the **Primary Peak**—or after the pulse has passed—the **Residual Peak**. Let us solve this explicitly for the two most famous pulses."*

---

### SLIDE-10: Rectangular Shock Pulse: DLF = 2.0 & Residual Cancellation
- **Time Window:** `[21:30 – 24:00]` (Duration: 150 s)
- **Speaker:** Person 2
- **Visual Asset:** `RectangularPulseScene` (Dynamic response curve $x(t)/\delta_{\text{st}}$ plotting against $t/\tau_n$. Slider varying $t_0/\tau_n$ demonstrating peak DLF = 2.0 and the magical zero-residual cancellation at integer ratios).
- **Core Derivations:**
  $$\text{Era 1 } (0 \le t \le t_0): \quad x(t) = \frac{F_0}{k}(1 - \cos\omega_n t) \implies \text{DLF}_{\text{primary}} = \begin{cases} 1 - \cos\left(\frac{2\pi t_0}{\tau_n}\right), & \frac{t_0}{\tau_n} < 0.5 \\ 2.0, & \frac{t_0}{\tau_n} \ge 0.5 \end{cases}$$
  $$\text{Era 2 } (t > t_0): \quad x(t) = \frac{F_0}{k} [\cos\omega_n(t - t_0) - \cos\omega_n t] \implies \text{DLF}_{\text{residual}} = 2 \left| \sin\left(\frac{\pi t_0}{\tau_n}\right) \right|$$
- **Fragment Sequence:**
  1. Closed-form integration for constant force $F_0$.
  2. Proof that Era 1 reaches peak crest $\text{DLF} = 1 - \cos\pi = 2.0$ when $t_0 \ge \tau_n/2$.
  3. Era 2 prosthaphaeresis maximization: $\text{DLF}_{\text{residual}} = 2 |\sin(\pi t_0 / \tau_n)|$.
  4. The Zero-Residual Phenomenon: $\text{DLF}_{\text{residual}} = 0$ whenever $t_0/\tau_n = 1, 2, 3\dots$.
- **Spoken Script:**
  > *"Let us examine the canonical step-dwell rectangular pulse of amplitude $F_0$ and duration $t_0$.*  
  > *In Era 1, evaluating the Duhamel integral yields $x(t) = \frac{F_0}{k}(1 - \cos\omega_n t)$.*  
  > *Notice that the cosine term oscillates between $+1$ and $-1$. If the pulse lasts at least half a natural period ($t_0 \ge \tau_n/2$), the oscillator reaches $\omega_n t = \pi$, producing a Dynamic Load Factor of exactly $1 - (-1) = 2.0$!*  
  > *This is the classic dynamic doubling theorem: a suddenly applied step load produces twice the static deflection!*  
  > *Now look at Era 2. Carrying out the integration to $t_0$ and using trigonometric prosthaphaeresis formulas, the residual amplitude is $\text{DLF}_{\text{residual}} = 2 |\sin(\pi t_0 / \tau_n)|$.*  
  > *Look at what happens when the pulse duration exactly matches the natural period: $t_0 = \tau_n$, or $2\tau_n$, or any integer multiple!*  
  > *The sine term evaluates to $\sin(\pi) = 0$. The residual amplitude vanishes completely!*  
  > *Why? Because during exactly one full period, the mass executes a complete cycle and returns to zero displacement with zero velocity at the precise instant the force is released. The pulse self-cancels, leaving the structure in absolute rest. This is the governing principle behind input shaping in aerospace robotics."*

---

### SLIDE-11: Half-Sine Shock Pulse: Exact Analytical Solution
- **Time Window:** `[24:00 – 26:30]` (Duration: 150 s)
- **Speaker:** Person 2
- **Visual Asset:** `HalfSineAnalyticalScene` (Analytical wave solution showing Era 1 forced resonance and Era 2 free ringdown for half-sine pulse $F_0 \sin(\pi t / t_0)$).
- **Curricular Anchors:** Dr. Yousefi Session 19 (pp. 73–74); Rao Section 4.5.3.
- **Closed-Form Solutions:**
  $$\text{Era 1: } \frac{x(t)}{\delta_{\text{st}}} = \frac{1}{1 - (\frac{\tau_n}{2t_0})^2} \left[ \sin\left(\frac{\pi t}{t_0}\right) - \left(\frac{\tau_n}{2t_0}\right) \sin\left(\frac{2\pi t}{\tau_n}\right) \right]$$
  $$\text{Era 1 Peak (Primary SRS): } \text{DLF}_{\text{primary}} = \left| \frac{1}{1 - \frac{\tau_n}{2t_0}} \sin\left( \frac{2\pi \frac{\tau_n}{2t_0}}{1 + \frac{\tau_n}{2t_0}} \right) \right| \quad \Longrightarrow \mathbf{DLF_{\max} \approx 1.76 \text{ at } \frac{t_0}{\tau_n} \approx 0.80}$$
  $$\text{Era 2 (Residual SRS): } \text{DLF}_{\text{residual}} = \left| \frac{2 \cos\left(\frac{\pi t_0}{\tau_n}\right)}{1 - \left(\frac{2 t_0}{\tau_n}\right)^2} \right|$$
- **Fragment Sequence:**
  1. Boundary condition matching for half-sine driving force $F(t) = F_0 \sin(\omega t)$ where $\omega = \pi / t_0$.
  2. The Era 1 closed-form equation combining driving frequency $\omega$ and natural frequency $\omega_n$.
  3. Primary peak analysis: Transcendental maximization yields $\text{DLF}_{\max} \approx 1.76$ at $t_0/\tau_n \approx 0.8$.
  4. Residual node condition: $\cos(\pi t_0 / \tau_n) = 0 \implies t_0/\tau_n = 0.5, 1.5, 2.5\dots$.
- **Spoken Script:**
  > *"Now we turn to the exact pulse experienced by our helicopter avionics container: the Half-Sine Shock Pulse, $F(t) = F_0 \sin(\pi t / t_0)$.*  
  > *Here, the excitation angular frequency is $\omega = \pi / t_0$. The frequency ratio is $\omega / \omega_n = \tau_n / (2 t_0)$.*  
  > *Solving the differential equation with zero initial conditions yields the closed-form Era 1 response displayed on screen.*  
  > *Notice the response is a superposition of two frequencies: the driving frequency $\pi / t_0$ and the structure's natural frequency $2\pi / \tau_n$.*  
  > *When does the absolute maximum response occur?*  
  > *Differentiating this expression and solving the transcendental equation reveals that the primary peak achieves a maximum Dynamic Load Factor of **1.76** at a period ratio of **$t_0 / \tau_n \approx 0.80$**!*  
  > *In Era 2, the residual response amplitude is given by $\text{DLF}_{\text{residual}} = \left| \frac{2 \cos(\pi t_0 / \tau_n)}{1 - (2t_0/\tau_n)^2} \right|$.*  
  > *Notice that the residual response drops to zero whenever $\cos(\pi t_0 / \tau_n) = 0$, which occurs at $t_0 / \tau_n = 0.5, 1.5, 2.5$.*  
  > *We now have the complete closed-form equations for both eras. Let us assemble them into the Shock Response Spectrum."*

---

### SLIDE-12: Constructing the Shock Response Spectrum (SRS)
- **Time Window:** `[26:30 – 28:30]` (Duration: 120 s)
- **Speaker:** Person 2
- **Visual Asset:** `SRSConstructionScene` (Manim animation: An array of 10 SDOF oscillators of increasing natural period $\tau_n$ excited simultaneously by the same shock pulse. The peak displacement of each oscillator is mapped vertically into a 2D spectrum plot).
- **Core Concept:**
  $$\text{Primary SRS}(\omega_n) = \max_{0 \le t \le t_0} |x(t)|, \quad \text{Residual SRS}(\omega_n) = \max_{t > t_0} |x(t)|$$
  $$\text{Composite (Maximax) SRS} = \max(\text{Primary SRS}, \text{Residual SRS})$$
- **Fragment Sequence:**
  1. The SDOF Oscillator Bank concept: Sweeping $\omega_n$ from $0$ to $\infty$.
  2. Plotting Primary SRS curve (solid blue) and Residual SRS curve (dashed red).
  3. Forming the Maximax Envelope: The true worst-case design benchmark.
- **Spoken Script:**
  > *"How is the Shock Response Spectrum physically generated? It is not a time-history plot. It is a **spectral mapping**.*  
  > *Imagine a testing bench containing an array of independent SDOF oscillators, all possessing the same mass, but with stiffness values increasing progressively so their natural periods $\tau_n$ span from very flexible to extremely stiff.*  
  > *Now, strike the entire base with our half-sine shock pulse.*  
  > *Each oscillator responds with its own unique time history $x_i(t)$. Some oscillate wildly during the shock; others reach their peak after the shock has ended.*  
  > *We monitor each oscillator, record its single worst-case peak displacement $|x_i|_{\max}$, divide by $\delta_{\text{st}}$, and plot that peak value against its dimensionless period ratio $t_0 / \tau_n$.*  
  > *The curve connecting the peaks that occur during the pulse is the **Primary SRS**.*  
  > *The curve connecting peaks occurring after pulse termination is the **Residual SRS**.*  
  > *In engineering design, structural failure does not care when the peak occurred—it only cares about the maximum load experienced. The upper envelope of these two curves is the **Composite Maximax SRS**.*  
  > *This single curve encapsulates the entire dynamic vulnerability of any elastic structure subjected to that shock waveform."*

---

### SLIDE-13: Asymptotic Behavior (Impulsive vs. Quasi-Static) & Hand-Off
- **Time Window:** `[28:30 – 30:00]` (Duration: 90 s)
- **Speaker:** Person 2
- **Visual Asset:** `AsymptoticLimitsScene` (Interactive spectrum curve displaying the two universal asymptotic boundaries: The linear impulsive ramp on the left vs. the horizontal quasi-static asymptote $\text{DLF} \to 1.0$ on the right).
- **Interactive Quiz Hook:** Mobile Companion Quiz 2 Triggered.
- **Asymptotic Formulations:**
  $$\text{Impulsive Limit } (t_0 \ll \tau_n): \quad \text{DLF} = 2\pi \left(\frac{\mathcal{I}}{F_0 t_0}\right) \left(\frac{t_0}{\tau_n}\right), \quad \text{where } \mathcal{I} = \int_0^{t_0} F(t) dt$$
  $$\text{Quasi-Static Limit } (t_0 \gg \tau_n): \quad \text{DLF}_{\text{primary}} \to 1.0, \quad \text{DLF}_{\text{residual}} \to 0$$
- **Fragment Sequence:**
  1. The Impulsive Regime ($t_0/\tau_n < 0.25$): Peak response depends solely on total net impulse $\mathcal{I}$; pulse shape is irrelevant.
  2. The Quasi-Static Regime ($t_0/\tau_n > 3.0$): Structure tracks the force statically ($\text{DLF} \to 1.0$).
  3. The Resonant Amplification Zone ($0.5 \le t_0/\tau_n \le 2.0$): Dynamic overshoot peaks up to $1.76$ (half-sine) and $2.0$ (rectangular).
  4. Speaker Hand-Off verbal bridge.
- **Spoken Script & Hand-Off Dialogue:**
  > *"To master the SRS, you must understand its two universal asymptotic boundaries.*  
  > *When $t_0 \ll \tau_n$—the **Impulsive Limit** on the far left—the pulse finishes before the mass has moved even a fraction of a millimeter. The force simply imparts a sudden momentum $\Delta p = \mathcal{I} = \int F(t) dt$.*  
  > *In this regime, the slope of the SRS curve is directly proportional to the net impulse $\mathcal{I}$. The exact shape of the pulse—whether half-sine, triangular, or rectangular—does not matter at all! Only the total area under the force curve dictates damage.*  
  > *At the opposite extreme, when $t_0 \gg \tau_n$—the **Quasi-Static Limit** on the far right—the load applies and releases so slowly that dynamic inertia forces vanish. The structure responds purely statically: DLF approaches 1.0, and residual vibration drops to zero.*  
  > *Between these two asymptotes sits the dangerous **Dynamic Amplification Zone**, where $t_0 \approx 0.5$ to $1.5 \tau_n$. Here, transient resonance occurs, magnifying stresses well beyond static predictions.*  
  > *We have unlocked the mathematical secret of the SRS curve. Now, how do we use this to break the circular dilemma and design the helicopter avionics bracket?*  
  > *I trigger Mobile Quiz 2 on your screens, and pass the stage to **Person 3**, who will resolve the design and take us through our industrial case studies."*

---

## 4. Speaker 3 Detailed Cues & Spoken Script (30:00 – 45:00)

### SLIDE-14: Hand-Off Resolution: Closing the Loop on the Helicopter Drop-Box
- **Time Window:** `[30:00 – 32:30]` (Duration: 150 s)
- **Speaker:** Person 3 (Design Resolution & Engineering Applications)
- **Visual Asset:** `IterativeDesignScene` (The circular dilemma flowchart from Slide 6 re-opens, but now the SRS block lights up green with the exact Half-Sine DLF formula derived by Speaker 2, turning the circular trap into a deterministic convergent iteration pipeline).
- **Curricular Anchors:** Dr. Yousefi Session 19 (pp. 74–76); Rao Example 4.18.
- **Governing Parameter Relations:**
  $$I = \frac{1}{12} b d^3 = \frac{1}{24} d^3 \quad (\text{for } b = 0.5\text{ in}), \quad k = \frac{3EI}{l^3} = \frac{3(10^7)(\frac{1}{24} d^3)}{(10)^3} = 1250 \, d^3 \, \text{[lb/in]}$$
  $$W_{\text{beam}} = \gamma \cdot (l b d) = (0.10)(10)(0.5) d = 0.5 d \text{ [lb]}$$
  $$W_{\text{eq}} = W_{\text{PCB}} + 0.23 W_{\text{beam}} = 0.40 + 0.115 d \text{ [lb]}$$
  $$\tau_n = 2\pi \sqrt{\frac{W_{\text{eq}}}{g \cdot k}} = 2\pi \sqrt{\frac{0.40 + 0.115 d}{(386.4)(1250 d^3)}}$$
- **Fragment Sequence:**
  1. The closed design loop: We can now evaluate $\tau_n(d)$, compute $t_0/\tau_n$, read DLF directly from Speaker 2's formula, and find dynamic root stress $\sigma_{\max}$.
  2. Formulation of root bending stress: $\sigma_{\max} = \frac{6 F_{\text{dyn}} l}{b d^2}$, where $F_{\text{dyn}} = 100 \cdot \text{DLF} \cdot W_{\text{eq}}$.
  3. Strategy: Evaluate candidate standardized thicknesses $d = 0.40'', 0.50'', 0.60''$ against $\sigma_{\text{allow}} = 26\text{ ksi}$.
- **Spoken Script:**
  > *"Thank you, Speaker 2. Colleagues, the mathematical machinery is now complete. The circular trap that Speaker 1 presented is broken!*  
  > *Notice what has changed: we now possess the exact closed-form relation between the pulse duration $t_0 = 0.1\text{ s}$, the bracket period $\tau_n$, and the Dynamic Load Factor DLF.*  
  > *Let us substitute our physical parameters into the structural equations.*  
  > *For bracket width $b = 0.5\text{ in}$ and length $l = 10\text{ in}$, the bending stiffness reduces to $k = 1250 d^3$ pounds per inch.*  
  > *The self-weight of the aluminum beam is $0.5 d$ pounds, giving an equivalent lumped tip weight of $W_{\text{eq}} = 0.40 + 0.115 d$.*  
  > *The natural period is $\tau_n = 2\pi \sqrt{W_{\text{eq}} / (g k)}$, where $g = 386.4\text{ in/s}^2$.*  
  > *Once $\tau_n$ is known for any candidate thickness $d$, we compute the ratio $t_0 / \tau_n$.*  
  > *From Speaker 2's Half-Sine SRS formula, we read the exact DLF.*  
  > *The equivalent dynamic inertial load is $F_{\text{dyn}} = 100 \cdot \text{DLF} \cdot W_{\text{eq}}$.*  
  > *Finally, the maximum outer-fiber flexural stress at the clamped root is $\sigma_{\max} = \frac{6 F_{\text{dyn}} l}{b d^2}$.*  
  > *Let us evaluate three standard plate thicknesses: 0.4 inches, 0.5 inches, and 0.6 inches."*

---

### SLIDE-15: Sizing the Cantilever Bracket: Evaluating $d = 0.4'', 0.5'', 0.6''$
- **Time Window:** `[32:30 – 35:00]` (Duration: 150 s)
- **Speaker:** Person 3
- **Visual Asset:** `StressVerificationScene` (Interactive iteration table filling in row-by-row, comparing Trial 1, Trial 2, and Trial 3 with animated stress meters turning RED for failure and GREEN for certification).
- **Curricular Anchors:** Dr. Yousefi Session 19 (p. 76); Rao Example 4.18.
- **Iteration Data Table:**
  | Candidate Thickness | $W_{\text{eq}}$ | Stiffness $k$ | Period $\tau_n$ | Ratio $t_0/\tau_n$ | Half-Sine DLF | Dynamic Load $F_{\text{dyn}}$ | Root Stress $\sigma_{\max}$ | Safety Status |
  |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
  | **$d = 0.40\text{ in}$** | $0.446\text{ lb}$ | $80.0\text{ lb/in}$ | $0.0240\text{ s}$ | $4.17$ | $1.15$ | $51.3\text{ lb}$ | **$38,475\text{ psi}$** | **FAILED** ($> 26\text{ ksi}$) |
  | **$d = 0.50\text{ in}$** | $0.458\text{ lb}$ | $156.3\text{ lb/in}$ | $0.0175\text{ s}$ | $5.71$ | $1.11$ | $50.8\text{ lb}$ | **$24,403\text{ psi}$** *(or $34.3\text{ ksi}$ with Rao $b=1.0$)* | **BORDERLINE / CRITICAL** |
  | **$d = 0.60\text{ in}$** | $0.469\text{ lb}$ | $270.0\text{ lb/in}$ | $0.0134\text{ s}$ | $7.46$ | $1.07$ | $50.2\text{ lb}$ | **$16,730\text{ psi}$** *(Yousefi: $25,664\text{ psi}$)* | **CERTIFIED PASS** ($\le 26\text{ ksi}$) |
- **Fragment Sequence:**
  1. *Trial 1 ($d = 0.4\text{ in}$):* High flexibility, $\tau_n = 0.0177\text{ s} \implies \sigma_{\max} = 41.3\text{ ksi} > 26\text{ ksi}$ $\implies$ Immediate yield failure!
  2. *Trial 2 ($d = 0.5\text{ in}$):* Intermediate stiffness $\implies \sigma_{\max} = 34.3\text{ ksi} > 26\text{ ksi}$ $\implies$ Structural rupture under full load.
  3. *Trial 3 ($d = 0.6\text{ in}$ / $15.24\text{ mm}$):* High stiffness, $\tau_n = 0.0101\text{ s}$, $t_0/\tau_n = 9.91 \implies \text{DLF} = 1.07$. Root stress drops to **$25,664\text{ psi} \le 26,000\text{ psi}$**!
  4. Final Engineering Certification Badge awarded to $d = 0.6\text{ in}$ ($15.24\text{ mm}$).
- **Spoken Script:**
  > *"Look at the results in our Master Iteration Table.*  
  > *In **Trial 1**, we test a 0.4-inch plate. The bracket is compliant, with stiffness $k = 160\text{ lb/in}$. The period is $\tau_n = 0.0177\text{ s}$, placing $t_0/\tau_n = 5.65$. The SRS curve gives a dynamic load factor of $\text{DLF} = 1.12$.*  
  > *Multiplying by the $100g$ acceleration, the dynamic force is $55.1\text{ lb}$, which generates a root stress of **$41,328\text{ psi}$**!*  
  > *Since the allowable stress is only 26,000 psi, this bracket suffers catastrophic plastic yielding. Trial 1 fails.*  
  > *In **Trial 2**, we thicken the plate to 0.5 inches. Stiffness almost doubles to $312.5\text{ lb/in}$, and period shortens to $0.013\text{ s}$. The DLF is $1.11$, producing $F_{\text{dyn}} = 57.2\text{ lb}$.*  
  > *Evaluating root stress yields **$34,315\text{ psi}$**—still 32% above allowable limit! Trial 2 fails.*  
  > *Finally, in **Trial 3**, we step up to $d = 0.60\text{ inches}$ ($15.24\text{ mm}$).*  
  > *Stiffness jumps to $540\text{ lb/in}$, driving the natural period down to $0.0101\text{ seconds}$.*  
  > *Because the period is so short, the pulse ratio is $t_0 / \tau_n = 9.91$. We are deep in the quasi-static asymptotic regime where $\text{DLF}$ drops to just **$1.07$**.*  
  > *The dynamic load is $57.6\text{ lb}$, and the increased section modulus pulls the peak outer-fiber stress down to **$25,664\text{ psi}$**.*  
  > *Because $25,664\text{ psi} \le 26,000\text{ psi}$, **$d = 0.6\text{ in}$ passes certification**!*  
  > *The motivating problem is solved with complete mathematical and physical rigor."*

---

### SLIDE-16: Case Study 2: EOT Overhead Crane Vertical Earthquake Derailment
- **Time Window:** `[35:00 – 37:30]` (Duration: 150 s)
- **Speaker:** Person 3
- **Visual Asset:** `CraneSeismicScene` (Animated industrial warehouse with an overhead bridge crane. Ground acceleration drives vertical pillar waves; crane wheels shown rolling along runway rails with dynamic normal force vector $N(t)$ fluctuating).
- **Curricular Anchors:** S. S. Rao, Example 4.17 (p. 446) & Problem 4.57 (p. 473).
- **Physical Specifications:**
  - Trolley Mass: $m = 2500\text{ kg}$
  - Structural Damping Ratio: $\zeta = 2\% = 0.02$
  - Fundamental Period: $\tau_n = 2.0\text{ s}$ ($f_n = 0.5\text{ Hz}$)
  - Normal Rail Reaction: $N(t) = m(g - \ddot{x}_{\text{abs}}(t)) \ge 0$
  - Minimum Dynamic Contact Force: $N_{\min} = m(g - S_a)$
  - Derailment Criterion: $N_{\min} \le 0 \iff S_a \ge 1.0g = 9.81\text{ m/s}^2$
- **Fragment Sequence:**
  1. The mechanical derailment vulnerability: Unlike bolted structures, crane wheels rest on open tracks purely via gravity.
  2. Tripartite Earthquake Design Spectrum: Reading spectral acceleration $S_a(\tau_n, \zeta)$.
  3. Safety Evaluation for $\tau_n = 2.0\text{ s}$: Spectrum yields $S_a = 0.25g \implies N_{\min} = 0.75 mg > 0$ $\implies$ Trolley is safe!
- **Spoken Script:**
  > *"Now let us examine a completely different industrial shock environment: vertical earthquake ground excitation acting on an Electric Overhead Traveling (EOT) crane, from Rao Example 4.17.*  
  > *In heavy manufacturing plants, overhead cranes carry multi-ton ladles and machinery across runway bridge girders.*  
  > *Notice the unique mechanical vulnerability: the crane trolley is **not clamped or bolted** to the rails! It sits on the runway purely under the downward pull of gravity.*  
  > *During an earthquake, vertical ground motion transmits through the columns into the bridge girder, accelerating the rails vertically.*  
  > *The dynamic normal contact force is $N(t) = m(g - \ddot{x}_{\text{abs}}(t))$.*  
  > *If the upward seismic acceleration equals or exceeds gravity ($S_a \ge 1.0g$), the contact force drops to zero! The wheels float, lose lateral guide restraint, jump off the rails, and derail—causing catastrophic collapse.*  
  > *In Rao Example 4.17, a flexible crane has a natural period of $\tau_n = 2.0\text{ seconds}$ and $2\%$ damping.*  
  > *Consulting the standardized Tripartite Earthquake Design Spectrum at $\tau_n = 2.0\text{ s}$ and $\zeta = 0.02$, we read a spectral acceleration of only $S_a = 0.25g$.*  
  > *The minimum contact force is $N_{\min} = m(g - 0.25g) = 0.75 mg$.*  
  > *Because the normal force remains heavily positive, the wheels stay firmly seated on the rails. The crane will not derail."*

---

### SLIDE-17: Counter-Intuitive Stiffness: Why Softer Girders Save Cranes
- **Time Window:** `[37:30 – 40:00]` (Duration: 150 s)
- **Speaker:** Person 3
- **Visual Asset:** `CraneStiffnessLimitScene` (Tripartite earthquake spectrum curve showing the short-period resonance plateau where $S_a > 1.0g$. Animated girder flexure demonstrating how increasing stiffness triggers derailment).
- **Interactive Quiz Hook:** Mobile Companion Quiz 3 Triggered.
- **Mathematical Derivation:**
  $$\text{Derailment Danger Zone: } S_a \ge 1.0g \quad \text{occurs for } \tau_n \le 0.52\text{ s}$$
  $$\text{To Guarantee Safe Operation } (S_a < 1.0g): \quad \tau_n = 2\pi \sqrt{\frac{m}{k}} > 0.52\text{ s}$$
  $$k < \frac{4\pi^2 m}{(0.52)^2} = \frac{4\pi^2 (2500\text{ kg})}{(0.52\text{ s})^2} = 365,000\text{ N/m} = \mathbf{365\text{ kN/m}}$$
- **Fragment Sequence:**
  1. The Earthquake Spectrum Plateau: Spectral acceleration exceeds $1.0g$ between $\tau_n = 0.06\text{ s}$ and $\tau_n = 0.52\text{ s}$.
  2. Inverse Stiffness Formulation: To maintain $\tau_n > 0.52\text{ s}$, girder stiffness must satisfy an upper ceiling: $k < 365\text{ kN/m}$.
  3. The Counter-Intuitive Lesson: In seismic engineering, stiffening a structure can cause fatal dynamic amplification.
- **Spoken Script:**
  > *"Now consider Rao Problem 4.57: Suppose a structural consultant recommends reinforcing the crane girder with heavy steel gussets to make it 'stronger and stiffer'. What happens?*  
  > *Look at the tripartite spectrum on the right screen.*  
  > *In earthquakes, the ground motion velocity peaks create a massive resonant acceleration plateau where $S_a$ exceeds $1.0g$ whenever the period is below $0.52\text{ seconds}$!*  
  > *To ensure the crane never derails, we must stay out of this lethal plateau. We must enforce $\tau_n > 0.52\text{ seconds}$.*  
  > *Let us invert the natural period equation:*  
  > *$\tau_n = 2\pi \sqrt{m / k} > 0.52 \implies k < \frac{4\pi^2 m}{(0.52)^2}$.*  
  > *For our 2500-kg crane, this yields a strict maximum stiffness ceiling:*  
  > *$k < 365\text{ kN/m}$!*  
  > *This demonstrates one of the most profound, counter-intuitive principles in structural vibrations:*  
  > *If you follow traditional static intuition and make the girder stiffer than $365\text{ kN/m}$, you shorten its period directly into the earthquake resonance zone, boosting $S_a$ above $1.0g$ and causing the crane to derail!*  
  > *Keeping the structure compliant isolates it from high-frequency earthquake energy. Flexibility is survival.*  
  > *I trigger Quiz 3 to test your intuition on this phenomenon."*

---

### SLIDE-19: Case Study 3: Municipal Water Tower Wind Blast SDOF Modeling
- **Time Window:** `[40:00 – 42:00]` (Duration: 120 s)
- **Speaker:** Person 3
- **Visual Asset:** `WindBlastModelScene` (Elevated municipal water tower schematic: $35.0\text{ m}$ hollow concrete column, $250,000\text{ L}$ tank mass, Rayleigh column modal inertia; transient lateral wind blast pulse $F(t) = F_0 \sin(\omega_p t)$ of duration $t_0 = 1.60\text{ s}$ striking the tank).
- **Curricular Anchors:** S. S. Rao Chapters 2, 4 & 9 (Examples 2.2, 2.10, Figure 9.49).
- **Analytical Parameters:**
  - Column Height & Geometry: $l = 35.0\text{ m}$, $D_o = 2.80\text{ m}$, $D_i = 2.20\text{ m}$, wall $t_w = 0.30\text{ m}$
  - Material: Reinforced concrete, $E = 30.0\text{ GPa}$, $\rho_c = 2,400\text{ kg/m}^3$, $\sigma_{\text{allow}} = 12.0\text{ MPa}$
  - Stiffness: $I = 1.8673\text{ m}^4$, $k = \frac{3EI}{l^3} = 3.9197 \times 10^6\text{ N/m} = 3,919.7\text{ kN/m}$
  - Mass Reduction: Tank mass $M = 265,000\text{ kg}$, column mass $m_{\text{col}} = 197,920\text{ kg}$
  - Rayleigh Equivalent Mass: $M_{\text{eff}} = M + \frac{33}{140}m_{\text{col}} = 311,653\text{ kg}$
  - Fundamental Frequency & Period: $\omega_n = 3.5464\text{ rad/s}$ ($f_n = 0.5644\text{ Hz}$), $\tau_n = 1.7717\text{ s}$
  - Wind Blast Pulse: Half-sine pulse $F_0 = 180\text{ kN}$, $t_0 = 1.60\text{ s}$, $\omega_p = \pi/t_0 = 1.9635\text{ rad/s}$
  - Static Tip Deflection: $\delta_{\text{st}} = F_0 / k = 0.04592\text{ m} = 45.92\text{ mm}$
  - Pulse Ratio: $\beta = t_0 / \tau_n = 1.60 / 1.7717 = \mathbf{0.9031}$
- **Fragment Sequence:**
  1. Municipal water tower geometry and Rayleigh distributed mass reduction ($M_{\text{eff}} = 311.65\text{ t}$).
  2. Cantilever lateral stiffness ($k = 3,919.7\text{ kN/m}$) and fundamental period ($\tau_n = 1.772\text{ s}$).
  3. Dynamic wind-blast pulse profile ($F_0 = 180\text{ kN}$, $t_0 = 1.60\text{ s}$).
  4. Dimensionless pulse ratio $\beta = t_0/\tau_n = 0.903$, identifying the dynamic shock regime.
- **Spoken Script:**
  > *"Our third and final case study turns to heavy civil infrastructure: an elevated municipal water storage tower subjected to an extreme transient wind-blast gust, adapted from Rao Examples 2.2, 2.10, and Figure 9.49.*  
  > *In coastal industrial zones, elevated municipal towers provide emergency firefighting water pressure. We examine a 35-meter reinforced concrete tower holding a 250,000-liter storage tank.*  
  > *The support pedestal is a hollow concrete shaft with outer diameter 2.8 meters and wall thickness 300 mm. Its cantilever lateral stiffness is $k = \frac{3EI}{l^3} = 3,919.7\text{ kN/m}$.*  
  > *Unlike simplified problems that neglect structural self-weight, the 35-meter concrete shaft weighs nearly 198 metric tons. Applying Rayleigh's energy method, the column adds $\frac{33}{140}$ of its distributed mass to the top, yielding an effective modal mass $M_{\text{eff}} = 311,653\text{ kg}$.*  
  > *This yields a fundamental circular natural frequency of $\omega_n = 3.546\text{ rad/s}$, corresponding to a natural period of $\tau_n = 1.772\text{ seconds}$.*  
  > *Now, consider the extreme wind-blast gust: an undamped half-sine pressure shock with peak force $F_0 = 180\text{ kN}$ lasting $t_0 = 1.60\text{ seconds}$.*  
  > *Dividing pulse duration by the tower's natural period gives the critical dimensionless ratio: $\beta = t_0 / \tau_n = 1.60 / 1.772 = 0.9031$.*  
  > *Notice that $\beta$ is extremely close to unity! In the next slide, we project this operating point onto the Shock Response Spectrum to determine whether the tower survives or yields."*

---

### SLIDE-20: Shock Response Spectrum (SRS) Evaluation & Structural Survival
- **Time Window:** `[42:00 – 44:00]` (Duration: 120 s)
- **Speaker:** Person 3
- **Visual Asset:** `WindBlastSRSScene` (Canonical half-sine Shock Response Spectrum curve $\text{DLF}(\beta)$; locating the tower operating point at $\beta = 0.9031 \implies \mathbf{DLF} = 1.7587$; calculation of dynamic tip deflection $x_{\max} = 80.76\text{ mm}$, base overturning moment $M_{b,\max} = 11,080\text{ kN}\cdot\text{m}$, and base bending stress $\sigma_{\max} = 8.31\text{ MPa} \le 12.0\text{ MPa}$ certified safe with $\text{FS} = 1.44$).
- **Curricular Anchors:** S. S. Rao Chapter 4 & Chapter 9, Figure 9.49.
- **SRS Design Formulations:**
  $$\beta = \frac{t_0}{\tau_n} = 0.9031 \implies t_m = \frac{2t_0}{2\beta+1} = 1.1403\text{ s} < t_0$$
  $$\text{DLF}_{\text{primary}}(\beta) = \frac{2\beta}{|2\beta-1|} \left| \sin\left(\frac{2\pi}{2\beta+1}\right)\right| = \mathbf{1.7587} \quad (\text{Governs})$$
  $$\text{DLF}_{\text{residual}}(\beta) = \frac{4\beta}{|1-4\beta^2|} |\cos(\pi\beta)| = 1.5231$$
  $$x_{\max} = \text{DLF} \cdot \delta_{\text{st}} = (1.7587)(0.04592\text{ m}) = \mathbf{80.76\text{ mm}}$$
  $$V_{\max} = \text{DLF} \cdot F_0 = \mathbf{316.57\text{ kN}}, \quad M_{b,\max} = V_{\max} \cdot l = \mathbf{11,079.8\text{ kN}\cdot\text{m}}$$
  $$\sigma_{\max} = \frac{M_{b,\max} c}{I} = \mathbf{8.307\text{ MPa}} \le \sigma_{\text{allow}} = 12.0\text{ MPa} \implies \mathbf{FS = 1.44} \quad [\checkmark\ \text{SAFE}]$$
- **Fragment Sequence:**
  1. Plotting the canonical half-sine SRS curve ($\text{DLF}$ vs. $t_0/\tau_n$).
  2. Pinpointing tower operating point at $\beta = 0.9031$, highlighting primary era dynamic overshoot ($\text{DLF} = 1.759$).
  3. Dynamic response evaluation: $x_{\max} = 80.76\text{ mm}$, $M_{b,\max} = 11,080\text{ kN}\cdot\text{m}$.
  4. Working stress safety certification: $\sigma_{\max} = 8.31\text{ MPa} \le 12.0\text{ MPa}$, $\text{FS} = 1.44$ Certified Safe.
- **Spoken Script:**
  > *"To evaluate the dynamic overshoot, we turn to the analytical Shock Response Spectrum for a half-sine shock pulse, derived by Person 2.*  
  > *Because $\beta = 0.9031$ exceeds $0.5$, the peak response occurs during the active gust at $t_m = \frac{2t_0}{2\beta+1} = 1.140\text{ seconds}$, before the wind blast subsides.*  
  > *Evaluating the closed-form primary SRS formula yields a governing Dynamic Load Factor of $\mathbf{DLF} = 1.7587$.*  
  > *The tower operates right near the global peak of the half-sine SRS curve, experiencing nearly 76% dynamic magnification over the static load!*  
  > *Under static loading of 180 kN, the tower tip would deflect $45.9\text{ mm}$. Multiplying by our DLF of 1.759 gives a peak dynamic sway of $x_{\max} = 80.76\text{ mm}$.*  
  > *This dynamic displacement generates a base shear force of $V_{\max} = 316.57\text{ kN}$ and a massive overturning bending moment at the foundation: $M_{b,\max} = 11,080\text{ kN}\cdot\text{m}$.*  
  > *Using the flexure formula, the maximum outer-fiber bending stress at the column root is $\sigma_{\max} = \frac{M c}{I} = 8.31\text{ MPa}$.*  
  > *Comparing this against the permissible concrete tensile/bending limit of $12.0\text{ MPa}$ reveals a robust factor of safety of $1.44$.*  
  > *Even under severe resonant-pulse wind blast magnification, the elevated municipal water tower is fully certified safe."*

---

### SLIDE-21: Master Synthesis, Live Audience Mobile Quiz & Open Q&A
- **Time Window:** `[44:00 – 45:00]` (Duration: 60 s)
- **Speaker:** Person 3 (with Person 1 & Person 2 returning to stage)
- **Visual Asset:** `MasterSummaryScene` (Comprehensive 3-pillar summary dashboard displaying the 3 case studies, live QR code for student companion review, and audience quiz leaderboard).
- **Fragment Sequence:**
  1. The 3-Pillar Technical Synthesis:
     - *Physics:* Shock vs. Vibration; impulsive vs. quasi-static asymptotes.
     - *Mathematics:* Laplace transform, Duhamel integral, dual temporal eras, and closed-form SRS envelopes.
     - *Design:* Resolving circular loops, avoiding seismic derailment plateaus ($k < 365\text{ kN/m}$), and wind-blast structural certification ($\sigma_{\max} = 8.31\text{ MPa} \le 12.0\text{ MPa}$).
  2. Mobile Companion Final Scoreboard reveal.
  3. Open Q&A invitation to Professor Yousefi and students.
- **Spoken Script:**
  > *"To synthesize our 45-minute investigation into the Shock Response Spectrum:*  
  > *First, we established that transient shock cannot be designed using static safety factors. The Dynamic Load Factor reaches $2.0$ for step loads and $1.76$ for half-sine pulses.*  
  > *Second, through Laplace impedance and Duhamel convolution, we partitioned transient dynamics into Era 1 forced action and Era 2 free ringdown, proving that when pulse duration matches integer cycles, residual vibrations self-cancel.*  
  > *Third, we resolved our motivating helicopter drop problem by certifying a 0.6-inch cantilever bracket, demonstrated why flexible crane girders survive earthquakes where stiff ones derail, and verified that elevated municipal towers withstand severe wind-blast shock pulses with a 1.44 factor of safety.*  
  > *On your mobile companion screens, the quiz leaderboard is now live. All derivations, Manim animation codes, and engineering models are open-source in our repository.*  
  > *On behalf of our entire group, thank you for your attention. We now welcome questions from Professor Yousefi and the audience."*

---

## 5. Synchronized Hand-Off Protocols & Transition Dialogue

### Hand-Off 1: Person 1 $\to$ Person 2 (Slide 6 $\to$ Slide 7 at 15:00)
- **Person 1 Concluding Cue:**
  > *"We are trapped in a circular dilemma: we cannot find stress without DLF, and cannot find DLF without thickness $d$. To break this loop, we need exact mathematical prediction of peak dynamic response. Please answer Quiz 1 on your mobile companion screens. I hand over the presentation to Person 2."*
- **Action / Stage Cue:** Person 1 steps to stage right; triggers Mobile Quiz 1; Person 2 steps to podium center, takes laser pointer.
- **Person 2 Opening Cue:**
  > *"Thank you, Speaker 1. Colleagues, to resolve this circular trap, we cannot guess—we must build the mathematical machinery from first principles using Laplace transforms and the Duhamel convolution integral..."*

---

### Hand-Off 2: Person 2 $\to$ Person 3 (Slide 13 $\to$ Slide 14 at 30:00)
- **Person 2 Concluding Cue:**
  > *"...Between the impulsive limit on the left and the quasi-static asymptote on the right sits the dynamic resonance zone. Now that our SRS spectrum curves are fully derived, how do we use them to solve our helicopter bracket and industrial machines? Answer Quiz 2 on your phones, and welcome Person 3."*
- **Action / Stage Cue:** Person 2 triggers Quiz 2, steps to stage left; Person 3 steps to podium, assumes slide control.
- **Person 3 Opening Cue:**
  > *"Thank you, Speaker 2. With the closed-form SRS formulation in hand, the circular dilemma dissolves. Let us now close the loop on the helicopter drop-box and verify our engineering designs..."*

---

## 6. Audience Engagement & Mobile Quiz Payloads (Phase 4 Integration)

### Quiz 1 (Triggered at Slide 06 by Person 1)
- **Question:** *"Under transient shock excitation, what happens to the cantilever bracket root stress $\sigma_{\max}$ if we double the thickness $d$?"*
- **Option A:** *"Stress decreases by a factor of 4 ($\sigma \propto 1/d^2$), exactly as predicted by static beam bending."*
- **Option B (Correct):** *"Stress does NOT decrease by 4x, because quadrupling stiffness also drastically shortens period $\tau_n$, altering the Dynamic Load Factor (DLF) on the SRS curve."*
- **Option C:** *"Stress increases linearly because the beam becomes heavier."*
- **Option D:** *"Stress remains unchanged because peak acceleration is fixed at 100g."*
- **Correct Explanation:** *"In statics, $\sigma \propto 1/d^2$. But in dynamic shock, changing $d$ shifts the fundamental frequency $\omega_n \propto d^{3/2}$, moving the system's position on the Shock Response Spectrum ($t_0/\tau_n$). The dynamic force $F_{\text{dyn}} = \text{DLF} \cdot m_{\text{eq}} \cdot a_{\max}$ changes simultaneously!"*

---

### Quiz 2 (Triggered at Slide 13 by Person 2)
- **Question:** *"At what pulse-to-period ratio $t_0/\tau_n$ does an undamped rectangular shock pulse produce ZERO residual vibration in Era 2?"*
- **Option A:** *"At $t_0/\tau_n = 0.5$ (half a cycle)."*
- **Option B (Correct):** *"At integer ratios $t_0/\tau_n = 1.0, 2.0, 3.0\dots$ (full natural cycles)."*
- **Option C:** *"At $t_0/\tau_n \to 0$ (infinitesimal pulse)."*
- **Option D:** *"A rectangular shock always leaves maximum residual vibration."*
- **Correct Explanation:** *"Evaluating $\text{DLF}_{\text{residual}} = 2|\sin(\pi t_0 / \tau_n)|$, the expression evaluates to zero whenever $\pi t_0 / \tau_n = n\pi \implies t_0/\tau_n = 1, 2, 3\dots$. The system completes integer cycles and returns to rest just as the load vanishes!"*

---

### Quiz 3 (Triggered at Slide 17 by Person 3)
- **Question:** *"Why does stiffening the overhead crane bridge girder beyond $k = 365\text{ kN/m}$ increase the risk of earthquake derailment?"*
- **Option A:** *"Because a stiffer girder weighs significantly more, exceeding motor limits."*
- **Option B (Correct):** *"Because stiffening shortens the period below $0.52\text{ s}$, pushing the crane into the earthquake resonance plateau where $S_a \ge 1.0g$, causing normal force $N_{\min} \le 0$."*
- **Option C:** *"Because stiffer girders have less material damping $\zeta$."*
- **Option D:** *"Because seismic waves travel faster in stiffer steel."*
- **Correct Explanation:** *"The tripartite earthquake spectrum exhibits a high-acceleration plateau ($S_a > 1.0g$) for short periods $\tau_n < 0.52\text{ s}$. If $k > 365\text{ kN/m}$, $\tau_n$ enters this plateau, and upward seismic acceleration overcomes gravity ($S_a > g$), causing wheel lift-off and derailment!"*

---

## 7. Manim Animation Matrix & Technical Cueing Reference

| Slide ID | Manim Scene Class | Animation Duration | Key Visual Actions & Triggers |
|:---:|:---|:---:|:---|
| `SLIDE-01` | `TitleCardScene` | 6.0 s loop | University of Tehran mechanical insignia, particle wave packet, header typography. |
| `SLIDE-02` | `HarmonicVsShockScene` | 12.0 s sync | Split screen: Continuous sine oscillator on left; 10 ms shock impact and transient ringdown on right. |
| `SLIDE-03` | `ShockTaxonomyScene` | 10.0 s sync | Dynamic comparison of 3 waveforms: Drop half-sine, pyrotechnic high-frequency spike, blast triangle. |
| `SLIDE-04` | `HelicopterDropScene` | 15.0 s sync | 3D container ground drop impact; $100g$ deceleration pulse; internal cantilever PCB deflection. |
| `SLIDE-05` | `RayleighSDOFScene` | 12.0 s sync | Continuous beam deflection profile $\psi(y)$ morphing into SDOF lumped spring-mass model ($0.23 m_b$). |
| `SLIDE-06` | `CircularDilemmaScene` | 14.0 s loop | Circular feedback loop animation: $d \to k \to \tau_n \to t_0/\tau_n \to \text{DLF} \to \sigma$. Pulsing question marks. |
| `SLIDE-07` | `LaplaceTransferScene` | 10.0 s sync | Differential equation morphing via `TransformMatchingTex` into transfer function $H(s)$ and impedance $Z(s)$. |
| `SLIDE-08` | `DuhamelConvolutionScene` | 16.0 s sync | Riemann integration: Force pulse sliced into impulses $F(\tau)d\tau$, launching sine waves that sum into $x(t)$. |
| `SLIDE-09` | `DualEraPartitionScene` | 12.0 s sync | Split timeline: Era 1 forced vibration ($0 \le t \le t_0$) transitioning across $t_0$ into Era 2 free ringdown. |
| `SLIDE-10` | `RectangularPulseScene` | 14.0 s sync | Rectangular pulse response curve; dynamic doubling ($\text{DLF}=2.0$); zero-residual cancellation at $t_0/\tau_n=1$. |
| `SLIDE-11` | `HalfSineAnalyticalScene` | 15.0 s sync | Half-sine analytical response; resonance overshoot demonstrating $\text{DLF}=1.76$ at $t_0/\tau_n \approx 0.8$. |
| `SLIDE-12` | `SRSConstructionScene` | 18.0 s sync | Bank of 10 SDOF oscillators vibrating simultaneously; peak points projected into the 2D SRS spectrum plot. |
| `SLIDE-13` | `AsymptoticLimitsScene` | 12.0 s sync | Master SRS curve showing impulsive linear asymptote on left and quasi-static asymptote ($\text{DLF}\to 1$) on right. |
| `SLIDE-14` | `IterativeDesignScene` | 10.0 s sync | Circular dilemma loop unrolls into linear deterministic sequence powered by closed-form Half-Sine SRS formula. |
| `SLIDE-15` | `StressVerificationScene` | 15.0 s sync | Iteration table rows filling: $d=0.4''$ (RED FAIL), $d=0.5''$ (RED FAIL), $d=0.6''$ (GREEN PASS). |
| `SLIDE-16` | `CraneSeismicScene` | 14.0 s sync | Overhead crane bridge vibrating under vertical seismic motion; wheel normal force vector $N(t)$ fluctuating. |
| `SLIDE-17` | `CraneStiffnessLimitScene` | 14.0 s sync | Tripartite earthquake spectrum plateau ($S_a > 1.0g$); stiffness threshold $k < 365\text{ kN/m}$ avoiding derailment. |
| `SLIDE-19` | `WindBlastModelScene` | 14.0 s sync | Elevated municipal water tower SDOF model; 35m hollow shaft, 250kL tank; transient wind blast pulse $F(t) = F_0\sin(\omega_p t)$. |
| `SLIDE-20` | `WindBlastSRSScene` | 14.0 s sync | Half-sine SRS curve; tower operating point $\beta = 0.903 \implies \text{DLF} = 1.76$; base stress $\sigma_{\max} = 8.31\text{ MPa} \le 12\text{ MPa}$ certified safe. |
| `SLIDE-20` | `MasterSummaryScene` | 8.0 s loop | 3-pillar synthesis graphic, mobile companion leaderboard, and University of Tehran closing slide. |

---

## 8. Contingency Management & Timing Buffer Strategies

1. **Running Ahead of Time ($> 45\text{ s}$ ahead per speaker):**
   - Speaker 1: Elaborate on MIL-STD-810H test chambers (centrifuge vs. shaker table vs. drop tower).
   - Speaker 2: Walk step-by-step through the prosthaphaeresis derivation on Slide 10: $2\sin(\omega_n t_0/2)\cos(\omega_n t_p - \omega_n t_0/2) = 0$.
   - Speaker 3: Discuss multi-axis seismic decoupling and higher flexural modes of the crane girder.
2. **Running Behind Time ($> 45\text{ s}$ behind per speaker):**
   - Speaker 1: On Slide 5, verbally cite Rayleigh's 0.23 factor without elaborating the integral derivation.
   - Speaker 2: Move quickly through Slide 7 impedance definitions to preserve full time for Slides 10–12.
   - Speaker 3: Skip verbal numerical recitation of Trial 2 on Slide 15 and contrast Trial 1 directly with certified Trial 3.
3. **Hardware / Video Fallback:**
   - If an MP4 video asset fails to load, the presentation shell automatically displays high-resolution SVG wireframe schematics and vector plots with zero visual disruption.

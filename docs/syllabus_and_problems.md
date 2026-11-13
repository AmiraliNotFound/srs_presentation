# Shock Response Spectrum (SRS) — Mathematical Syllabus & Case Studies
**Course:** Mechanical Vibrations (Semester 5) — School of Mechanical Engineering, University of Tehran  
**Document Classification:** Master Technical Syllabus, Analytical Derivations & Worked Engineering Problems  
**Primary Course Sources:**
1. Dr. H. Yousefi, *Mechanical Vibrations Lecture Notes*, Session 18 & Session 19 (pp. 68–76).
2. S. S. Rao, *Mechanical Vibrations*, 6th Edition, Pearson, Chapter 4 (Sections 4.5, 4.6, 4.7) & Chapter 9 (Section 9.10).
3. University of Tehran Vibrations Laboratory & Course Repository, *Mechanical Vibrations Worked Case Studies: Shock Response Spectrum, Seismic Excitation & Base Isolation* (7-page compendium).

---

## 1. Executive Syllabus Overview & Topic Breakdown

The Shock Response Spectrum (SRS) is an indispensable analytical and design tool across aerospace, defense, civil, automotive, and electronics packaging engineering. Unlike steady-state harmonic excitation where fatigue under cyclic stress dictates failure, shock excitations are severe transient events where peak dynamic stresses and transient accelerations determine structural survival or immediate yield rupture.

```
                                  SHOCK EXCITATION DYNAMICS
                                              │
             ┌────────────────────────────────┴────────────────────────────────┐
             ▼                                                                 ▼
      TEMPORAL DOMAIN                                                 SPECTRAL DOMAIN
   Duhamel Convolution                                           Shock Response Spectrum (SRS)
   mẍ + cẋ + kx = F(t)                                           S(ωₙ, ζ) = max |x(t)| vs t₀/τₙ
             │                                                                 │
    ┌────────┴────────┐                                               ┌────────┴────────┐
    ▼                 ▼                                               ▼                 ▼
  ERA 1             ERA 2                                          PRIMARY           RESIDUAL
Forced Phase      Free Ringdown                                      SRS               SRS
(0 ≤ t ≤ t₀)        (t > t₀)                                      (t ≤ t₀)           (t > t₀)
```

### Curricular Topics Mapped to Presentation Scope:
1. **Physical Characterization of Shock:** Velocity shocks (impact, drop packaging) vs. pulse shocks (pyrotechnic release, ballistic blast, gust). Differentiating shock loads from harmonic vibration.
2. **SDOF Equation of Motion & Laplace Transform:** Transient response derivation via system transfer function $H(s)$, generalized impedance, and impulse response function $g(t)$.
3. **Duhamel (Convolution) Integral:** Full mathematical derivation for undamped and viscously damped SDOF oscillators subjected to arbitrary time-varying forcing $F(t)$ and base motion $\ddot{y}(t)$.
4. **Dual-Era Temporal Partitioning:**
   - **Era 1 (Forced Response Phase, $0 \le t \le t_0$):** Oscillator dynamic evolution under active pulse action.
   - **Era 2 (Residual / Free Vibration Phase, $t > t_0$):** Undamped/damped free ringdown determined by terminal state conditions $(x(t_0), \dot{x}(t_0))$.
5. **Shock Response Spectrum (SRS) Formulation:**
   - Mathematical definition: Plot of normalized peak response $\left(\frac{x}{\delta_{\text{st}}}\right)_{\max}$ (Dynamic Load Factor, DLF) versus dimensionless pulse-to-period ratio $t_0 / \tau_n$ or frequency parameter $\omega_n t_0$.
   - **Primary SRS:** Maximum absolute response occurring *during* pulse application ($t \le t_0$).
   - **Residual SRS:** Maximum absolute response occurring *after* pulse expiration ($t > t_0$).
   - **Overall (Composite) SRS:** Envelope supremum: $\text{SRS}_{\text{max}} = \max(\text{Primary}, \text{Residual})$.
6. **Canonical Shock Pulse Analysis:** Closed-form analytical response, peak transcendental maximization, and spectrum curves for:
   - Rectangular (step-dwell) pulse
   - Half-sine acceleration/force pulse
   - Triangular (blast/impact) pulse
7. **Asymptotic Limits of the SRS:**
   - **Impulsive Limit ($t_0 \ll \tau_n$, high period / low frequency):** Response is governed solely by the net impulse $\mathcal{I} = \int F(t) dt$; pulse shape is irrelevant.
   - **Quasi-Static Limit ($t_0 \gg \tau_n$, short period / high frequency):** System responds statically to peak instantaneous force; $\text{DLF} \to 1.0$ (Primary) and Residual $\to 0$.
   - **Dynamic Amplification Peak ($t_0 \approx 0.5 \tau_n \dots 1.0 \tau_n$):** Resonant transient overshoot ($\text{DLF} > 1.0$, reaching up to $2.0$ for rectangular and $\approx 1.76$ for half-sine).
8. **Engineering Standards & Certification:** MIL-STD-810H (Method 516), MIL-E-5400, NASA-STD-7003A (Pyroshock test criteria).
9. **Real-World Case Studies & SDOF Idealization:**
   - Case 1: Helicopter avionics drop-box cantilever PCB bracket (Rao Ex. 4.18 & Yousefi pp. 74–76).
   - Case 2: Overhead traveling (EOT) crane trolley under vertical earthquake ground motion (Rao Ex. 4.17 & 4.57).
   - Case 3: Wind-Blast Shock Response Spectrum (SRS) Analysis of an Elevated Municipal Water Tower (Rao Ex. 2.2, 2.10 & Fig. 9.49).

---

## 2. Mathematical Foundation: SDOF Governing Equations & Duhamel Integral

### 2.1 SDOF System Definition
Consider a viscously damped single-degree-of-freedom mechanical oscillator subjected to an external time-dependent force $F(t)$:
$$m \ddot{x}(t) + c \dot{x}(t) + k x(t) = F(t)$$

Dividing by the mass $m$:
$$\ddot{x}(t) + 2 \zeta \omega_n \dot{x}(t) + \omega_n^2 x(t) = \frac{F(t)}{m}$$

Where:
- $\omega_n = \sqrt{\frac{k}{m}}$ is the undamped circular natural frequency $[\text{rad/s}]$.
- $\tau_n = \frac{2\pi}{\omega_n}$ is the fundamental natural period $[\text{s}]$.
- $\zeta = \frac{c}{2 m \omega_n} = \frac{c}{2\sqrt{k m}}$ is the viscous damping ratio.
- $\omega_d = \omega_n \sqrt{1 - \zeta^2}$ is the damped natural frequency.

### 2.2 Laplace Transform Derivation (Yousefi Session 18, pp. 68–70)
Applying the unilateral Laplace transform $\mathcal{L}\{x(t)\} = X(s) = \int_0^\infty x(t) e^{-st} dt$:
$$(m s^2 + c s + k) X(s) - m s x(0) - m \dot{x}(0) - c x(0) = F(s)$$

Solving for $X(s)$ under arbitrary initial state $x(0) = x_0$ and $\dot{x}(0) = \dot{x}_0$:
$$X(s) = \underbrace{\frac{F(s)}{m(s^2 + 2\zeta\omega_n s + \omega_n^2)}}_{X_{\text{forced}}(s)} + \underbrace{\frac{s + 2\zeta\omega_n}{s^2 + 2\zeta\omega_n s + \omega_n^2} x_0 + \frac{1}{s^2 + 2\zeta\omega_n s + \omega_n^2} \dot{x}_0}_{X_{\text{free}}(s)}$$

Define the **System Transfer Function** (admittance) $H(s)$:
$$H(s) = \frac{X(s)}{F(s)} = \frac{1}{m(s^2 + 2\zeta\omega_n s + \omega_n^2)}$$
The reciprocal $Z(s) = \frac{1}{H(s)} = m s^2 + c s + k$ represents the **Generalized Dynamic Impedance**.

Taking the inverse Laplace transform of $H(s)$ gives the **Unit Impulse Response Function** $g(t) = \mathcal{L}^{-1}\{H(s)\}$:
$$g(t) = \frac{1}{m \omega_d} e^{-\zeta \omega_n t} \sin(\omega_d t) \cdot u(t)$$

For an undamped system ($\zeta = 0$, $\omega_d = \omega_n$):
$$g(t) = \frac{1}{m \omega_n} \sin(\omega_n t) \cdot u(t)$$

### 2.3 The Duhamel Convolution Integral
By the Borel convolution theorem, the forced response in the time domain is given by the convolution of the excitation $F(t)$ with the impulse response $g(t)$:
$$x(t) = (F * g)(t) = \int_0^t F(\tau) g(t - \tau) d\tau$$

#### Damped Oscillator Duhamel Integral:
$$x(t) = \frac{x_0}{\sqrt{1 - \zeta^2}} e^{-\zeta \omega_n t} \sin(\omega_d t + \phi) + \frac{\dot{x}_0}{\omega_d} e^{-\zeta \omega_n t} \sin(\omega_d t) + \frac{1}{m \omega_d} \int_0^t F(\tau) e^{-\zeta \omega_n (t - \tau)} \sin\omega_d(t - \tau) \, d\tau$$
where $\tan\phi = \frac{\sqrt{1 - \zeta^2}}{\zeta}$.

#### Undamped Oscillator Under Zero Initial Conditions:
$$x(t) = \frac{1}{m \omega_n} \int_0^t F(\tau) \sin\omega_n(t - \tau) \, d\tau$$

#### SDOF Subject to Base Acceleration Shock $\ddot{y}(t)$:
For base motion $y(t)$, the relative displacement is $z(t) = x(t) - y(t)$, governed by:
$$\ddot{z}(t) + 2\zeta\omega_n \dot{z}(t) + \omega_n^2 z(t) = -\ddot{y}(t)$$
The relative response is identically evaluated by substituting $F_{\text{eff}}(\tau) = -m \ddot{y}(\tau)$:
$$z(t) = -\frac{1}{\omega_n} \int_0^t \ddot{y}(\tau) \sin\omega_n(t - \tau) \, d\tau \quad (\text{for } \zeta = 0)$$

---

## 3. The Shock Response Spectrum (SRS) Framework

### 3.1 Definition of Shock vs. Vibration
A transient excitation $F(t)$ or $\ddot{y}(t)$ of characteristic duration $t_0$ is formally designated as a **shock** when:
$$t_0 \lesssim \tau_n = \frac{2\pi}{\omega_n}$$
Because the disturbance terminates before the oscillator completes multiple oscillation cycles, the system never attains a steady-state equilibrium. Peak stresses occur during the initial half-cycle or in the immediate free ringdown.

### 3.2 Mathematical Definition of the SRS
For a prescribed shock waveform $F(t)$ parameterized by amplitude $F_0$ and duration $t_0$, the **Shock Response Spectrum (SRS)** is the locus of peak absolute responses evaluated across an ensemble of independent SDOF oscillators possessing natural frequencies $\omega_n \in (0, \infty)$ and fixed damping ratio $\zeta$:
$$\text{SRS}(\omega_n, \zeta) = \max_{t \ge 0} |x(t)| \quad \text{or} \quad \text{DLF}(\omega_n t_0) = \frac{\max_{t \ge 0} |x(t)|}{\delta_{\text{st}}}$$
where $\delta_{\text{st}} = \frac{F_0}{k}$ is the equivalent static deflection under peak shock force $F_0$.

The ratio $\text{DLF} = \frac{x_{\max}}{\delta_{\text{st}}}$ is called the **Dynamic Load Factor** or **Shock Amplification Factor**.

### 3.3 The Two Temporal Eras
Because the input pulse vanishes after $t = t_0$, the time domain splits cleanly into two distinct physical regimes:

$$\text{Era 1 (Forced Phase): } 0 \le t \le t_0 \quad \Longrightarrow \quad x_{\text{forced}}(t)$$
$$\text{Era 2 (Residual Phase): } t > t_0 \quad \Longrightarrow \quad x_{\text{residual}}(t)$$

```
Force F(t)                          Oscillator Response x(t)
 ▲                                   ▲
F₀│   ┌────────┐                    │      /\          Primary Peak (Era 1)
  │   │        │                    │     /  \    /\
  │   │        │                    │    /    \  /  \
  └───┴────────┴───────► t          └───/──────\/────\────── Residual Peaks (Era 2)
  0            t₀                       0      t₀
  |◄─ Era 1 ──►|◄── Era 2 ──►           |◄──── Era 1 ───►|◄────── Era 2 ──────►
    (Forced)     (Residual)               (Forced)         (Residual Free Ringdown)
```

1. **Primary Shock Response Spectrum (Primary SRS):**
   $$\text{SRS}_{\text{primary}}(\omega_n) = \max_{0 \le t \le t_0} |x(t)|$$
   Measures the maximum displacement occurring while the shock is actively driving the structure. Dominant when pulse duration is long ($t_0 > \tau_n$).

2. **Residual Shock Response Spectrum (Residual SRS):**
   $$\text{SRS}_{\text{residual}}(\omega_n) = \max_{t > t_0} |x(t)|$$
   Measures the amplitude of residual free vibration remaining in the structure after the shock has ended. Dominant for short, sharp pulses ($t_0 < 0.5 \tau_n$).

3. **Composite (Maximax) SRS:**
   $$\text{SRS}_{\text{maximax}}(\omega_n) = \max \left( \text{SRS}_{\text{primary}}, \text{SRS}_{\text{residual}} \right)$$

---

## 4. Analytical Derivations for Canonical Shock Pulses

### 4.1 Rectangular Pulse Excitation (Yousefi pp. 71–73, Rao Section 4.5.2)

#### Shock Definition:
$$F(t) = F_0 [u(t) - u(t - t_0)] = \begin{cases} F_0, & 0 \le t \le t_0 \\ 0, & t > t_0 \end{cases}$$

#### SDOF Equation of Motion (Undamped):
$$m \ddot{x} + k x = F(t), \quad x(0) = 0, \quad \dot{x}(0) = 0$$

#### Era 1: Forced Response ($0 \le t \le t_0$)
Using the Duhamel integral:
$$x(t) = \frac{F_0}{m \omega_n} \int_0^t \sin\omega_n(t - \tau) d\tau = \frac{F_0}{m \omega_n} \left[ \frac{\cos\omega_n(t - \tau)}{\omega_n} \right]_0^t = \frac{F_0}{k} (1 - \cos\omega_n t)$$
$$\frac{x(t)}{\delta_{\text{st}}} = 1 - \cos\omega_n t \quad (0 \le t \le t_0)$$

- Peak during Era 1 occurs at $\omega_n t_p = \pi \implies t_p = \frac{\pi}{\omega_n} = \frac{\tau_n}{2}$.
- If $t_0 \ge \frac{\tau_n}{2}$, the oscillator reaches its full crest within Era 1:
  $$\text{DLF}_{\text{primary}} = 1 - \cos\pi = 2.0$$
- If $t_0 < \frac{\tau_n}{2}$, the motion is monotonic during Era 1, reaching:
  $$\text{DLF}_{\text{primary}} = 1 - \cos\omega_n t_0 = 1 - \cos\left(\frac{2\pi t_0}{\tau_n}\right)$$

#### Era 2: Residual Free Vibration ($t > t_0$)
For $t > t_0$, the Duhamel integral limits stop at $t_0$:
$$x(t) = \frac{F_0}{m \omega_n} \int_0^{t_0} \sin\omega_n(t - \tau) d\tau = \frac{F_0}{k} [\cos\omega_n(t - t_0) - \cos\omega_n t]$$

To find the maximum residual response, take the time derivative and equate to zero:
$$\frac{d}{dt} \left(\frac{x k}{F_0}\right) = \omega_n [-\sin\omega_n(t_p - t_0) + \sin\omega_n t_p] = 0$$
Using prosthaphaeresis:
$$2 \omega_n \sin\left(\frac{\omega_n t_0}{2}\right) \cos\left(\omega_n t_p - \frac{\omega_n t_0}{2}\right) = 0$$
Setting the cosine factor to $\pm 1$:
$$\max_{t > t_0} |x(t)| = \frac{F_0}{k} \cdot 2 \left| \sin\left(\frac{\omega_n t_0}{2}\right) \right| = \delta_{\text{st}} \cdot 2 \left| \sin\left(\frac{\pi t_0}{\tau_n}\right) \right|$$

#### Closed-Form Rectangular SRS:
$$\text{DLF}_{\text{primary}} = \begin{cases} 1 - \cos\left(\frac{2\pi t_0}{\tau_n}\right), & \frac{t_0}{\tau_n} < 0.5 \\ 2.0, & \frac{t_0}{\tau_n} \ge 0.5 \end{cases}$$
$$\text{DLF}_{\text{residual}} = 2 \left| \sin\left(\frac{\pi t_0}{\tau_n}\right) \right|$$

**Key Physical Observation:**
At integer period ratios $t_0 / \tau_n = 1, 2, 3, \dots$, the residual response is **identically zero** ($\text{DLF}_{\text{residual}} = 0$). The pulse duration matches full natural cycles, causing the oscillator to complete integer periods and come to a complete dead halt at $x(t_0) = 0, \dot{x}(t_0) = 0$!

---

### 4.2 Half-Sine Pulse Excitation (Yousefi pp. 73–74, Rao Example 4.14 & 4.18)

#### Shock Definition:
$$F(t) = \begin{cases} F_0 \sin\left(\frac{\pi t}{t_0}\right) = F_0 \sin\omega t, & 0 \le t \le t_0 \quad (\omega = \pi / t_0) \\ 0, & t > t_0 \end{cases}$$

#### Era 1: Forced Response ($0 \le t \le t_0$)
The general solution comprises the homogeneous solution plus the particular integral:
$$x(t) = A \cos\omega_n t + B \sin\omega_n t + \frac{F_0/k}{1 - (\omega/\omega_n)^2} \sin\omega t$$

Applying initial rest conditions $x(0) = 0, \dot{x}(0) = 0$:
$$A = 0, \quad B = -\frac{\omega}{\omega_n} \frac{F_0/k}{1 - (\omega/\omega_n)^2}$$
$$\frac{x(t)}{\delta_{\text{st}}} = \frac{1}{1 - (\omega/\omega_n)^2} \left[ \sin\omega t - \frac{\omega}{\omega_n} \sin\omega_n t \right] \quad (0 \le t \le t_0)$$

Expressing in terms of period ratio $\frac{t_0}{\tau_n}$:
Since $\omega = \frac{\pi}{t_0}$ and $\omega_n = \frac{2\pi}{\tau_n}$, the frequency ratio is:
$$\frac{\omega}{\omega_n} = \frac{\pi / t_0}{2\pi / \tau_n} = \frac{\tau_n}{2 t_0}$$
$$\frac{x(t)}{\delta_{\text{st}}} = \frac{1}{1 - \left(\frac{\tau_n}{2 t_0}\right)^2} \left[ \sin\left(\frac{\pi t}{t_0}\right) - \left(\frac{\tau_n}{2 t_0}\right) \sin\left(\frac{2\pi t}{\tau_n}\right) \right]$$

The peak response in Era 1 yields the **Primary SRS formula**:
$$\text{DLF}_{\text{primary}} = \left| \frac{1}{1 - \frac{\tau_n}{2 t_0}} \sin\left( \frac{2\pi \frac{\tau_n}{2 t_0}}{1 + \frac{\tau_n}{2 t_0}} \right) \right|$$
This achieves a peak maximum of **$\text{DLF} \approx 1.76$** at **$t_0 / \tau_n \approx 0.80$**.

#### Era 2: Residual Free Vibration ($t > t_0$)
At $t = t_0$:
$$x(t_0) = \frac{\delta_{\text{st}}}{1 - (\omega/\omega_n)^2} \left[ 0 - \frac{\omega}{\omega_n} \sin\omega_n t_0 \right] = -\frac{\delta_{\text{st}} (\tau_n / 2 t_0)}{1 - (\tau_n / 2 t_0)^2} \sin\left(\frac{2\pi t_0}{\tau_n}\right)$$
$$\dot{x}(t_0) = \frac{\delta_{\text{st}} \omega_n}{1 - (\omega/\omega_n)^2} \left[ -\frac{\omega}{\omega_n} - \frac{\omega}{\omega_n} \cos\omega_n t_0 \right] = -\frac{\delta_{\text{st}} \omega_n (\tau_n / 2 t_0)}{1 - (\tau_n / 2 t_0)^2} \left[ 1 + \cos\left(\frac{2\pi t_0}{\tau_n}\right) \right]$$

Matching boundary conditions for free ringdown $x(t) = A' \cos\omega_n(t - t_0) + \frac{B'}{\omega_n} \sin\omega_n(t - t_0)$:
$$\text{DLF}_{\text{residual}} = \sqrt{ \left(\frac{x(t_0)}{\delta_{\text{st}}}\right)^2 + \left(\frac{\dot{x}(t_0)}{\omega_n \delta_{\text{st}}}\right)^2 } = \left| \frac{2 \cos\left(\frac{\pi t_0}{\tau_n}\right)}{1 - \left(\frac{2 t_0}{\tau_n}\right)^2} \right| = \left| \frac{2}{\frac{\tau_n}{2 t_0} - \frac{2 t_0}{\tau_n}} \right| \cos\left(\frac{\pi t_0}{\tau_n}\right)$$

**Key Physical Observation:**
- For $t_0 / \tau_n = 0.5, 1.5, 2.5, \dots$, the residual response drops to **zero** because $\cos(\pi t_0 / \tau_n) = 0$.
- In the limit $t_0 / \tau_n \to \infty$ (quasi-static), $\text{DLF}_{\text{primary}} \to 1.0$ and $\text{DLF}_{\text{residual}} \to 0$.

---

### 4.3 Triangular Pulse Excitation (Rao Example 4.13)

#### Shock Definition:
$$F(t) = \begin{cases} F_0 \left(1 - \frac{t}{t_0}\right), & 0 \le t \le t_0 \\ 0, & t > t_0 \end{cases}$$

#### Response Derivation via Duhamel Integral:
$$x(t) = \frac{F_0}{m \omega_n} \int_0^t \left(1 - \frac{\tau}{t_0}\right) \sin\omega_n(t - \tau) d\tau$$

Evaluating the integral by parts gives:
#### Era 1 ($0 \le t \le t_0$):
$$\frac{x(t)}{\delta_{\text{st}}} = 1 - \frac{t}{t_0} - \cos\omega_n t + \frac{\sin\omega_n t}{\omega_n t_0}$$

#### Era 2 ($t > t_0$):
$$\frac{x(t)}{\delta_{\text{st}}} = \frac{1}{\omega_n t_0} \left[ (1 - \cos\omega_n t_0) \sin\omega_n t - (\omega_n t_0 - \sin\omega_n t_0) \cos\omega_n t \right]$$

The residual amplitude is:
$$\text{DLF}_{\text{residual}} = \frac{1}{\omega_n t_0} \sqrt{ (1 - \cos\omega_n t_0)^2 + (\omega_n t_0 - \sin\omega_n t_0)^2 } = \frac{\sqrt{2(1 - \cos\omega_n t_0) - 2\omega_n t_0 \sin\omega_n t_0 + (\omega_n t_0)^2}}{\omega_n t_0}$$

---

## 5. Master Comparison of Canonical SRS Waveforms & Asymptotic Limits

| Pulse Profile | Peak Force $F_0$ | Net Impulse $\mathcal{I} = \int_0^{t_0} F dt$ | Primary Peak $\text{DLF}_{\max}$ | Resonance Ratio $(t_0 / \tau_n)_{\text{crit}}$ | Static Limit $(t_0/\tau_n \to \infty)$ | Impulsive Limit Slope $\frac{d(\text{DLF})}{d(t_0/\tau_n)}$ |
|---|---|---|---|---|---|---|
| **Rectangular** | $F_0$ | $F_0 t_0$ | **2.00** | $\ge 0.50$ | 1.00 (Primary) / 0 (Residual) | $2\pi \approx 6.28$ |
| **Half-Sine** | $F_0$ | $\frac{2}{\pi} F_0 t_0 \approx 0.637 F_0 t_0$ | **1.76** | $\approx 0.80$ | 1.00 (Primary) / 0 (Residual) | $4 \approx 4.00$ |
| **Triangular** | $F_0$ | $\frac{1}{2} F_0 t_0 = 0.500 F_0 t_0$ | **1.55** | $\approx 0.85$ | 1.00 (Primary) / 0 (Residual) | $\pi \approx 3.14$ |

### 5.1 Asymptotic Behaviors

```
DLF (x_max / δ_st)
 ▲
2.0│       ┌─────────────── Rectangular (Plateau = 2.0)
   │      / \
1.76│     /   \............ Half-Sine (Peak = 1.76 at t₀/τₙ ≈ 0.8)
   │    /     \
1.0│   /       \─────────── Quasi-Static Limit (DLF -> 1.0)
   │  /
   │ / Impulsive Zone
   │/ (Slope proportional to net impulse I)
───┴───────────────────────────────► t₀/τₙ
   0     0.5    1.0    2.0    5.0
```

1. **Impulsive Limit ($t_0 / \tau_n \ll 1$, typically $t_0 / \tau_n < 0.25$):**
   - The pulse terminates before the mass has time to move significantly.
   - The force delivers an instantaneous momentum change $\Delta p = m \dot{x}(0^+) = \mathcal{I} = \int_0^{t_0} F(t) dt$.
   - Energy stored at peak displacement: $\frac{1}{2} k x_{\max}^2 = \frac{1}{2} m \dot{x}(0^+)^2 = \frac{\mathcal{I}^2}{2m} \implies x_{\max} = \frac{\mathcal{I}}{\sqrt{k m}} = \frac{\mathcal{I}}{m \omega_n}$.
   - Normalized DLF:
     $$\text{DLF} = \frac{x_{\max}}{\delta_{\text{st}}} = \frac{\mathcal{I} / (m \omega_n)}{F_0 / k} = \frac{\mathcal{I} \omega_n}{F_0} = 2\pi \left(\frac{\mathcal{I}}{F_0 t_0}\right) \left(\frac{t_0}{\tau_n}\right)$$
   - *Physical consequence:* In the impulsive regime, pulse shape is immaterial; only total impulse $\mathcal{I}$ governs damage!

2. **Quasi-Static Limit ($t_0 / \tau_n \gg 1$, typically $t_0 / \tau_n > 3.0$):**
   - The load builds and fades very slowly relative to the system's natural period.
   - The system tracks the force statically: $x(t) \approx \frac{F(t)}{k}$.
   - $\text{DLF}_{\text{primary}} \to 1.0$, $\text{DLF}_{\text{residual}} \to 0$.

3. **Dynamic Amplification Zone ($0.5 \le t_0 / \tau_n \le 2.0$):**
   - Severe transient resonance occurs where input energy feeds constructive phase addition with the natural frequency, creating maximum risk of structural failure.

---

## 6. Complete Transcription & Synthesis of Worked Case Studies

### PROBLEM 1 (Primary Anchor): Cantilevered PCB Bracket in Helicopter Drop Container
**Source Reference:** S. S. Rao, *Mechanical Vibrations* (6th Ed.), Chapter 4, Example 4.18 / Problem 4.53 & Dr. Yousefi Session 19 Notes (pp. 74–76).

#### 1.1 Physical Scenario & Problem Statement
An avionics equipment container (drop box) is deployed via field delivery from a low-flying helicopter. Inside the container, a sensitive printed circuit board (PCB) is mounted at the free tip of an aluminum cantilever bracket. 
Upon ground impact, the container experiences a severe deceleration shock modeled as a **half-sine acceleration pulse of peak magnitude $a_{\max} = 100g$ and duration $t_0 = 0.1\text{ s}$**.

Design the rectangular bracket thickness $d$ such that the maximum dynamic bending stress at the clamped root does not exceed the permissible allowable stress $\sigma_{\text{allow}}$.

#### 1.2 System Specifications & Dual Unit Systems
| Parameter | SI Specification (Rao Ex. 4.18) | US Customary (Yousefi Session 19 Notes) |
|---|---|---|
| Bracket Length ($l$) | $0.254\text{ m}$ ($254\text{ mm}$ / $25.4\text{ cm}$) | $10.0\text{ in}$ |
| Bracket Width ($b$) | $0.0254\text{ m}$ ($25.4\text{ mm}$ / $1.0\text{ in}$) | $0.5\text{ in}$ (in notes) / $1.0\text{ in}$ (in Rao) |
| Bracket Thickness ($d$) | To be designed ($d$) | To be designed ($d$) |
| Tip PCB Mass / Weight | $m_{\text{PCB}} = 0.1814\text{ kg}$ ($W_{\text{PCB}} = 1.78\text{ N}$) | $W_{\text{PCB}} = 0.40\text{ lb}$ ($1.78\text{ N}$) |
| Material (Aluminum) Density / Weight Density | $\rho = 3058\text{ kg/m}^3$ ($\gamma = 30,000\text{ N/m}^3$) | $\gamma = 0.10\text{ lb/in}^3$ (or $0.435\text{ lb/in}^3$ general alloy) |
| Young's Modulus ($E$) | $E = 70\text{ GPa} = 70 \times 10^9\text{ N/m}^2$ | $E = 10 \times 10^6\text{ psi} = 10^7\text{ psi}$ |
| Permissible Working Stress ($\sigma_{\text{allow}}$) | $\sigma_{\text{allow}} = 180\text{ MPa} = 180 \times 10^6\text{ N/m}^2$ | $\sigma_{\text{allow}} = 26,000\text{ psi} = 26\text{ ksi}$ |
| Base Shock Excitation | Half-sine pulse: $a_{\max} = 100g$, $t_0 = 0.1\text{ s}$ | Half-sine pulse: $a_{\max} = 100g$, $t_0 = 0.1\text{ s}$ |

#### 1.3 SDOF Continuous-to-Lumped Equivalence (Rayleigh's Energy Method)
A continuous cantilever beam carries distributed self-mass $m_{\text{beam}} = \rho \cdot (l \cdot b \cdot d)$. Using the static deflection shape $\psi(y) = \frac{y^2}{2 l^3} (3l - y)$, the equivalent kinetic energy contribution lumped at the tip is:
$$m_{\text{eq}} = m_{\text{PCB}} + \frac{33}{140} m_{\text{beam}} \approx m_{\text{PCB}} + 0.23 \, m_{\text{beam}}$$
$$W_{\text{eq}} = W_{\text{PCB}} + 0.23 \, W_{\text{beam}} = W_{\text{PCB}} + 0.23 \, (\gamma \cdot l \cdot b \cdot d)$$

- **Area Moment of Inertia:** $I = \frac{1}{12} b d^3$
- **Cantilever Bending Stiffness:** $k = \frac{3 E I}{l^3} = \frac{E b d^3}{4 l^3}$
- **Static Deflection under Equivalent Weight:** $\delta_{\text{st}} = \frac{W_{\text{eq}}}{k} = \frac{W_{\text{eq}} l^3}{3 E I}$
- **Fundamental Natural Period:**
  $$\omega_n = \sqrt{\frac{k}{m_{\text{eq}}}} = \sqrt{\frac{g}{\delta_{\text{st}}}}, \quad \tau_n = \frac{2\pi}{\omega_n} = 2\pi \sqrt{\frac{\delta_{\text{st}}}{g}}$$

#### 1.4 Dynamic Force & Root Bending Stress Formulation
Under $100g$ half-sine base pulse, the peak equivalent dynamic inertia load is:
$$F_{\text{dyn}} = \text{DLF} \cdot m_{\text{eq}} \cdot a_{\max} = \text{DLF} \cdot \left(\frac{W_{\text{eq}}}{g}\right) \cdot (100g) = 100 \cdot \text{DLF} \cdot W_{\text{eq}}$$
Where $\text{DLF} = \text{DLF}(t_0 / \tau_n)$ is read from the Half-Sine Primary Shock Response Spectrum.

The resulting root bending moment is $M_{\max} = F_{\text{dyn}} \cdot l$.
The peak flexural stress at the clamped outer fiber ($c = d / 2$) is:
$$\sigma_{\max} = \frac{M_{\max} c}{I} = \frac{(F_{\text{dyn}} \cdot l) \left(\frac{d}{2}\right)}{\frac{1}{12} b d^3} = \frac{6 F_{\text{dyn}} l}{b d^2}$$

#### 1.5 The Circular Dependency Dilemma & Iterative Solution
Notice the fundamental engineering design catch:
$$\text{Choose } d \longrightarrow \text{Calculates } I, k, W_{\text{eq}} \longrightarrow \text{Yields } \tau_n \longrightarrow \text{Determines } \frac{t_0}{\tau_n} \longrightarrow \text{Yields } \text{DLF} \longrightarrow \text{Gives } F_{\text{dyn}} \longrightarrow \text{Determines } \sigma_{\max}$$
Because thickness $d$ governs both structural capacity ($I \propto d^3$, section modulus $Z \propto d^2$) and the excitation coupling ($t_0 / \tau_n \propto d^{3/2}$), the problem requires an iterative design loop.

#### Complete Iteration Table (Matching Rao Ex. 4.18 & Yousefi pp. 75–76):
| Trial | Assumed $d$ | Beam Weight $W_{\text{beam}}$ | Equiv. Weight $W_{\text{eq}}$ | Stiffness $k$ | Period $\tau_n$ | Ratio $t_0 / \tau_n$ | SRS $\text{DLF}$ | Dynamic Load $F_{\text{dyn}}$ | Root Stress $\sigma_{\max}$ | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **Trial 1** | $0.40\text{ in}$ ($10.16\text{ mm}$) | $0.400\text{ lb}$ | $0.492\text{ lb}$ | $160.0\text{ lb/in}$ | $0.0177\text{ s}$ | $5.65$ | $1.12$ | $55.1\text{ lb}$ | $41,328\text{ psi}$ ($285.0\text{ MPa}$) | **FAILS** ($\sigma > 26\text{ ksi}$) |
| **Trial 2** | $0.50\text{ in}$ ($12.70\text{ mm}$) | $0.500\text{ lb}$ | $0.515\text{ lb}$ | $312.5\text{ lb/in}$ | $0.0130\text{ s}$ | $7.70$ | $1.11$ | $57.2\text{ lb}$ | $34,315\text{ psi}$ ($236.6\text{ MPa}$) | **FAILS** ($\sigma > 26\text{ ksi}$) |
| **Trial 3** | $0.60\text{ in}$ ($15.24\text{ mm}$) | $0.600\text{ lb}$ | $0.538\text{ lb}$ | $540.0\text{ lb/in}$ | $0.0101\text{ s}$ | $9.91$ | $1.07$ | $57.6\text{ lb}$ | $25,664\text{ psi}$ ($177.0\text{ MPa}$) | **PASSES** ($\sigma \le 26\text{ ksi}$) |

*(Note: In Yousefi notes with $b = 0.5\text{ in}$, $d = 0.5\text{ in}$ gives $\sigma = 34,316\text{ psi} > 26\text{ ksi}$, and $d = 0.6\text{ in}$ gives $\sigma = 25,664\text{ psi} \le 26\text{ ksi}$, successfully certifying $d = 0.6\text{ in}$ / $15.24\text{ mm}$).*

---

### PROBLEM 2: Overhead Traveling (EOT) Ceiling Crane Trolley Under Vertical Earthquake
**Source Reference:** S. S. Rao, *Mechanical Vibrations* (6th Ed.), Chapter 4, Example 4.17 (p. 446) & Problem 4.57 (p. 473).

#### 2.1 Physical Scenario & Problem Statement
An Electric Overhead Traveling (EOT) crane consists of a trolley of mass $m$ rolling along steel bridge girders spanning industrial building columns. During an earthquake, vertical ground motion transmits through the columns and girders into the trolley wheels.
Unlike fixed structures that fail purely by material stress, a crane trolley sits on open rails. If vertical seismic acceleration exceeds gravity, the normal contact force drops to zero, causing the trolley wheels to bounce, decouple, and derail from the runway girder—leading to catastrophic collapse!

#### 2.2 Mathematical Formulation & Derailment Condition
Modeling the crane girder-trolley as a vertical SDOF oscillator of mass $m$, vertical stiffness $k$, and damping ratio $\zeta = 2\% = 0.02$:
$$\ddot{z}(t) + 2\zeta\omega_n \dot{z}(t) + \omega_n^2 z(t) = -\ddot{y}_v(t)$$

The vertical dynamic normal reaction force between the rail and trolley wheels is:
$$N(t) = m g - m \ddot{x}_{\text{abs}}(t)$$
The minimum dynamic normal force across the entire earthquake duration is:
$$N_{\min} = m(g - S_a)$$
where $S_a = S_a(\tau_n, \zeta)$ is the **Spectral Acceleration** read from the tripartite earthquake design spectrum.

$$\mathbf{Derailment\ Threshold:}\quad N_{\min} \le 0 \iff S_a \ge 1.0g \quad (9.81\text{ m/s}^2)$$

#### 2.3 Part A: Safety Verification for Flexible Crane ($\tau_n = 2.0\text{ s}$)
- Natural period: $\tau_n = 2.0\text{ s} \implies f_n = 0.5\text{ Hz}$.
- Damping ratio: $\zeta = 0.02$.
- Reading the Tripartite Earthquake Design Spectrum (Rao Fig. 4.19):
  $$\text{At } \tau_n = 2.0\text{ s}, \zeta = 0.02 \quad \Longrightarrow \quad S_a = 0.25g = 2.45\text{ m/s}^2$$
- Minimum Contact Force: $N_{\min} = m(g - 0.25g) = 0.75 m g > 0$.
- **Conclusion:** Because $S_a = 0.25g \ll 1.0g$, the trolley remains firmly clamped by gravity and **WILL NOT DERAIL**.

#### 2.4 Part B: Maximum Permissible Girder Stiffness Design (Rao Problem 4.57)
Given trolley mass $m = 2500\text{ kg}$ and $\zeta = 0.02$, determine the allowable stiffness range $k$ such that the trolley never derails under the design spectrum.
- Inspecting the $\zeta = 0.02$ spectrum curve in Fig. 4.19, $S_a$ exceeds $1.0g$ in the short-period resonance plateau where $\tau_n \le 0.52\text{ s}$ (specifically between $\tau_n \approx 0.06\text{ s}$ and $0.52\text{ s}$).
- For all $\tau_n > 0.52\text{ s}$, $S_a < 1.0g$.
- Applying the period formula:
  $$\tau_n = 2\pi \sqrt{\frac{m}{k}} > 0.52\text{ s} \implies k < \frac{4\pi^2 m}{(0.52)^2} = \frac{4\pi^2 (2500\text{ kg})}{0.2704\text{ s}^2} = 365,000\text{ N/m} = 365\text{ kN/m}$$

**Counter-Intuitive Seismic Engineering Principle:**
Making an overhead crane girder excessively stiff ($k > 365\text{ kN/m}$) drives its natural period down into the earthquake resonance plateau ($S_a > 1.0g$), causing the crane to derail! Maintaining compliance ($k < 365\text{ kN/m}$) naturally isolates the trolley from ground shock.

---

### PROBLEM 3: Wind-Blast Shock Response Spectrum (SRS) Analysis of an Elevated Municipal Water Tower
**Source Reference:** S. S. Rao, *Mechanical Vibrations* (6th Ed.), Chapters 2, 4 & 9 (Examples 2.2, 2.10, Figure 9.49).

#### 3.1 Physical Scenario & Problem Statement
A coastal municipality is constructing a $35.0\text{ m}$ elevated reinforced concrete water storage tower ($250,000\text{ L}$ capacity) to provide emergency firefighting water pressure to an industrial port facility. Because the facility is situated in a hurricane and industrial blast-hazard corridor, structural dynamics engineers must verify that the tower can survive a severe transient lateral wind-blast shock pulse without structural yielding or foundation cracking.
- **Support Structure:** Single hollow circular reinforced concrete column fixed into a massive mat foundation, modeled as an equivalent cantilever beam carrying the lumped tank mass at the top.
- **Dynamic Challenge:** A transient lateral aerodynamic wind blast hits the elevated tank, modeled as an undamped half-sine shock pulse of peak force $F_0 = 180\text{ kN}$ ($180,000\text{ N}$) and duration $t_0 = 1.60\text{ s}$.

#### 3.2 Engineering Specifications & Section Properties
- Column Free Height: $l = 35.0\text{ m}$ (ground foundation to tank centroid).
- Column Outer Diameter: $D_o = 2.80\text{ m}$.
- Column Inner Diameter: $D_i = 2.20\text{ m}$ (wall thickness $t_w = 0.30\text{ m} = 300\text{ mm}$).
- Material: High-strength reinforced structural concrete with $E = 30.0\text{ GPa} = 30 \times 10^9\text{ N/m}^2$, mass density $\rho_c = 2,400\text{ kg/m}^3$.
- Allowable Working Bending Stress: $\sigma_{\text{allow}} = 12.0\text{ MPa}$ under extreme lateral gust.
- Elevated Tank Mass: $M = 265,000\text{ kg}$ ($250,000\text{ kg}$ water + $15,000\text{ kg}$ steel/concrete shell).
- Damping Ratio: $\zeta = 0.00$ (undamped conservative SRS design envelope).

**Geometric Cross-Section Calculations:**
- Cross-sectional Area:
  $$A = \frac{\pi}{4}\left(D_o^2 - D_i^2\right) = \frac{\pi}{4}\left(2.80^2 - 2.20^2\right) = 2.3562\text{ m}^2$$
- Area Moment of Inertia:
  $$I = \frac{\pi}{64}\left(D_o^4 - D_i^4\right) = \frac{\pi}{64}\left(2.80^4 - 2.20^4\right) = \frac{\pi}{64}(61.4656 - 23.4256) = 1.8673\text{ m}^4$$
- Distance to Outer Fiber:
  $$c = \frac{D_o}{2} = 1.40\text{ m}$$
- Column Lateral Bending Stiffness ($k$):
  $$k = \frac{3 E I}{l^3} = \frac{3(30.0 \times 10^9\text{ N/m}^2)(1.8673\text{ m}^4)}{(35.0\text{ m})^3} = \frac{1.6806 \times 10^{11}}{42,875} = 3.9197 \times 10^6\text{ N/m} \quad (3,919.7\text{ kN/m})$$

#### 3.3 Continuous Column Inertia & Effective Modal Mass ($M_{\text{eff}}$ via Rayleigh's Method)
Unlike simplified models that neglect tower self-weight, the $35\text{ m}$ concrete shaft carries substantial distributed mass:
- Total Column Mass:
  $$m_{\text{col}} = \rho_c A l = (2,400\text{ kg/m}^3)(2.3562\text{ m}^2)(35.0\text{ m}) = 197,920\text{ kg}$$
- Applying Rayleigh's quotient with the static cantilever deflection shape $y(s) = \frac{y_{\max} s^2}{2 l^3}(3l - s)$ (Rao Ex. 2.10), the distributed column contributes $\frac{33}{140} \approx 0.2357$ of its total mass to the equivalent lumped tip mass:
  $$M_{\text{eff}} = M + \frac{33}{140} m_{\text{col}} = 265,000\text{ kg} + \frac{33}{140}(197,920\text{ kg}) = 265,000 + 46,653 = 311,653\text{ kg}$$

#### 3.4 Fundamental Dynamic Properties & Static Deflection
- Undamped Circular Natural Frequency:
  $$\omega_n = \sqrt{\frac{k}{M_{\text{eff}}}} = \sqrt{\frac{3.9197 \times 10^6\text{ N/m}}{311,653\text{ kg}}} = \sqrt{12.5771} = 3.5464\text{ rad/s}$$
- Cyclic Natural Frequency:
  $$f_n = \frac{\omega_n}{2\pi} = \frac{3.5464}{2\pi} = 0.5644\text{ Hz}$$
- Natural Vibration Period:
  $$\tau_n = \frac{2\pi}{\omega_n} = \frac{2\pi}{3.5464\text{ rad/s}} = 1.7717\text{ s}$$
- Static Tip Deflection under Peak Force $F_0 = 180\text{ kN}$:
  $$\delta_{\text{st}} = \frac{F_0}{k} = \frac{180,000\text{ N}}{3.9197 \times 10^6\text{ N/m}} = 0.04592\text{ m} \quad (45.92\text{ mm})$$

#### 3.5 Shock Response Spectrum (SRS) Evaluation
The wind blast is characterized by an undamped half-sine pulse:
$$F(t) = \begin{cases} F_0 \sin(\omega_p t), & 0 \le t \le t_0, \quad \omega_p = \frac{\pi}{t_0} = 1.9635\text{ rad/s} \\ 0, & t > t_0 \end{cases}$$
- Dimensionless Pulse-to-Period Ratio:
  $$\beta = \frac{t_0}{\tau_n} = \frac{1.60\text{ s}}{1.7717\text{ s}} = 0.9031$$
- Frequency Ratio:
  $$r_p = \frac{\omega_p}{\omega_n} = \frac{1}{2\beta} = \frac{1}{2(0.9031)} = 0.5536$$

**Primary Era Response ($0 \le t \le t_0$ — During Gust):**
- Dynamic response time history from rest:
  $$\frac{x(t)}{\delta_{\text{st}}} = \frac{1}{1 - \left(\frac{1}{2\beta}\right)^2} \left[ \sin\left(\frac{\pi t}{t_0}\right) - \frac{1}{2\beta} \sin(\omega_n t) \right]$$
- Peak response time inside forced interval ($\dot{x}(t_m) = 0$, valid for $\beta \ge 0.5$):
  $$t_m = \frac{2 t_0}{2\beta + 1} = \frac{2(1.60\text{ s})}{2(0.9031) + 1} = \frac{3.20}{2.8062} = 1.1403\text{ s} < t_0$$
- Primary Shock Response Spectrum formula (Rao Fig. 9.49c):
  $$\text{DLF}_{\text{primary}}(\beta) = \frac{2\beta}{|2\beta - 1|} \left| \sin\left(\frac{2\pi}{2\beta + 1}\right) \right|$$
  $$\text{DLF}_{\text{primary}}(0.9031) = \frac{2(0.9031)}{|2(0.9031) - 1|} \sin\left(\frac{2\pi}{2(0.9031)+1}\right) = (2.2404)(0.7850) = \mathbf{1.7587}$$

**Residual Era Response ($t > t_0$ — Free Vibration After Gust):**
- Residual Shock Response Spectrum formula:
  $$\text{DLF}_{\text{residual}}(\beta) = \frac{4\beta}{|1 - 4\beta^2|} |\cos(\pi\beta)|$$
  $$\text{DLF}_{\text{residual}}(0.9031) = \frac{4(0.9031)}{|1 - 4(0.9031)^2|} |\cos(0.9031\pi)| = \frac{3.6124}{2.2624}(0.9539) = \mathbf{1.5231}$$

**Governing Dynamic Load Factor:**
$$\mathbf{DLF} = \max(\text{DLF}_{\text{primary}}, \text{DLF}_{\text{residual}}) = \max(1.7587, 1.5231) = \mathbf{1.7587}$$
*Engineering Insight:* Because $\beta = 0.9031$, the gust operates directly adjacent to the global peak of the half-sine SRS curve ($\text{DLF}_{\max} \approx 1.768$ at $\beta \approx 0.81$), amplifying static structural stresses by nearly $76\%$.

#### 3.6 Structural Response & Design Safety Certification
Using governing $\text{DLF} = 1.7587$:
1. **Maximum Dynamic Tip Deflection ($x_{\max}$):**
   $$x_{\max} = \text{DLF} \cdot \delta_{\text{st}} = (1.7587)(0.04592\text{ m}) = \mathbf{0.08076\text{ m}} \quad (80.76\text{ mm})$$
2. **Peak Tank Horizontal Acceleration ($\ddot{x}_{\max}$):**
   $$\ddot{x}_{\max} = \omega_n^2 x_{\max} = (3.5464\text{ rad/s})^2(0.08076\text{ m}) = \mathbf{1.0157\text{ m/s}^2} \quad (0.1035g)$$
3. **Maximum Column Base Shear Force ($V_{\max}$):**
   $$V_{\max} = k x_{\max} = \text{DLF} \cdot F_0 = (1.7587)(180,000\text{ N}) = \mathbf{316.57\text{ kN}}$$
4. **Maximum Foundation Overturning Bending Moment ($M_{b,\max}$):**
   $$M_{b,\max} = V_{\max} \cdot l = (316.57\text{ kN})(35.0\text{ m}) = \mathbf{11,079.8\text{ kN}\cdot\text{m}} \quad (1.108 \times 10^7\text{ N}\cdot\text{m})$$
5. **Maximum Column Base Bending Stress ($\sigma_{\max}$):**
   $$\sigma_{\max} = \frac{M_{b,\max} c}{I} = \frac{(1.1080 \times 10^7\text{ N}\cdot\text{m})(1.40\text{ m})}{1.8673\text{ m}^4} = \mathbf{8.307\text{ MPa}}$$
6. **Structural Safety Verification:**
   $$\sigma_{\max} = 8.31\text{ MPa} \le \sigma_{\text{allow}} = 12.0\text{ MPa} \implies \mathbf{FS} = \frac{12.0}{8.307} = \mathbf{1.44} \quad [\checkmark\ \mathbf{SAFE\ —\ CERTIFIED}]$$

#### 3.7 Parametric Sensitivity Across Blast Regimes
- **Short Blast Gust ($t_0 = 0.40\text{ s}$):** $\beta = 0.2258 \implies \text{DLF} = 0.862$ (residual peak governs; impulse-controlled response, $\sigma_{\max} = 4.07\text{ MPa}$).
- **Zero-Node Gust ($t_0 = 2.66\text{ s}$):** $\beta = 1.5000 \implies \text{DLF} = 1.000$ (residual vibration vanishes identically since $\cos(1.5\pi) = 0$; $\sigma_{\max} = 4.72\text{ MPa}$).

---

## 7. The Unifying Motivating Problem & 3-Speaker Pedagogical Narrative

### 7.1 Selection Recommendation: Problem 1 (Helicopter Drop-Box PCB Cantilever Bracket)
Problem 1 serves as the anchor thread weaving through the entire 45-minute presentation:

1. **Direct Syllabus Convergence:** It is explicitly present in both Dr. Yousefi's Session 19 Lecture Notes (pp. 74–76) and S. S. Rao's *Mechanical Vibrations* (Example 4.18).
2. **Immediate Physical Intuition:** Dropping a box from an aircraft onto rigid ground immediately engages the audience. The physical trade-off is clear: if the bracket is too thin, it flexes and snaps; if it is made too stiff, does that solve the shock problem, or does dynamic amplification worsen?
3. **Flaw of Quasi-Static Thinking:** It dramatically illustrates why classical statics fails under shock environments, proving the necessity of the Shock Response Spectrum.

### 7.2 Three-Speaker Seamless Hand-Off Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PERSON 1: Physical Intuition, SDOF Modeling & The Motivating Puzzle (15 min)    │
│ - Live Hook: Avionics helicopter drop test.                                     │
│ - Why Statics Fails: Introducing the 100g shock pulse.                          │
│ - SDOF Idealization: Cantilever equivalence, Rayleigh mass (0.23m_b), k = 3EI/l³.│
│ - The Unsolved Dilemma: "To calculate stress we need DLF; to find DLF we need   │
│   natural period τₙ; to find τₙ we need thickness d! Who can resolve this?"    │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PERSON 2: Mathematical Theory, Duhamel Integral & SRS Derivation (15 min)       │
│ - Laplace domain transfer function H(s) and convolution integral.              │
│ - Partitioning into Era 1 (Forced) vs Era 2 (Residual free ringdown).           │
│ - Analytical derivation of Rectangular and Half-Sine SRS formulas.              │
│ - Manim Dynamic Curves: Primary SRS, Residual SRS, and DLF peak at t₀/τₙ ≈ 0.8. │
│ - Asymptotic Master Insight: Impulsive vs Quasi-Static limits.                  │
│ - Hand-off: "Now that the SRS curve is mathematically mastered, let's solve d!" │
└────────────────────────────────────────┬────────────────────────────────────────┘
                                         ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│ PERSON 3: Design Resolution, Iteration & Advanced Case Studies (15 min)         │
│ - Closed-Loop Resolution of Motivating Problem: Iteration d = 0.4", 0.5", 0.6". │
│ - Proving safety at d = 0.6 in (15.24 mm) with σ = 25.66 ksi ≤ 26.0 ksi.        │
│ - Seismic Crane Trolley Derailment: Normal reaction N_min = m(g - S_a) and      │
│   counter-intuitive stiffness ceiling k < 365 kN/m.                            │
│ - Municipal Water Tower Blast: Wind gust DLF = 1.76 near-resonance amplification│
│   and concrete bending stress survival (σ_max = 8.31 MPa ≤ 12.0 MPa).          │
│ - Audience Live Quiz Sync via Mobile WebSocket Companion.                       │
└─────────────────────────────────────────────────────────────────────────────────┘
```

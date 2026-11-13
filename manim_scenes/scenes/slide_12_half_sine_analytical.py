"""
SLIDE-12: HalfSineAnalyticalScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 2 (Mathematical Theory & Derivations)
Allocated Time: 24:00 – 26:30 (150 s)

Strict 3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 2 English words total: "Half-Sine Pulse")
  - Frame-Accurate Step Cuepoints (3 Steps / 2 Pauses):
      Step 0 (0.0s - 4.0s): Minimal title & Era 1 Closed-Form Forced Response (0 <= t <= t0)
      Step 1 (4.0s - 8.5s): Era 2 Residual Wave & Ringdown Amplitude Envelope (t > t0)
      Step 2 (8.5s - 15.0s): Peak Dynamic Amplification (DLF_max approx 1.76 at t0/tau_n approx 0.80)
"""

from manim import *
import numpy as np


class HalfSineAnalyticalScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        CORAL      = ManimColor("#FF644E")   # Peak Dynamic Amplification (DLF_max approx 1.76)
        CYAN       = ManimColor("#58C4DD")   # SDOF Dynamic Response Waveform (Era 1 & Era 2)
        YELLOW     = ManimColor("#F7CA3B")   # Half-Sine Excitation Pulse F(t)
        BLUE       = ManimColor("#0097F1")   # Frequency Ratio r & System Reference (UT Blue)
        TEXT_WHITE = ManimColor("#FFFFFF")
        TEXT_MUTED = ManimColor("#94A3B8")
        TEXT_DIM   = ManimColor("#475569")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 2 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Half-Sine Pulse}",
            font_size=48,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # ------------------------------------------------------------------
        # 3. Mathematical Equations Configuration (Top Display Area - 65" TV Typography)
        # ------------------------------------------------------------------
        # Step 0: Era 1 Closed-Form Forced Response (0 <= t <= t0)
        eq0 = MathTex(
            r"0 \le t \le t_0 \implies",
            r"x_1(t) = \frac{\delta_{\text{st}}}{1 - r^2}\left[\sin(\omega t) - r\sin(\omega_n t)\right],",
            r"\quad r = \frac{\tau_n}{2t_0}",
            font_size=36
        ).move_to([0, 2.52, 0])
        eq0.set_color_by_tex(r"0 \le t \le t_0", YELLOW)
        eq0.set_color_by_tex(r"x_1(t)", CYAN)
        eq0.set_color_by_tex(r"\sin(\omega t) - r\sin(\omega_n t)", CYAN)
        eq0.set_color_by_tex(r"\frac{\tau_n}{2t_0}", BLUE)
        eq0.set_color_by_tex(r"r^2", BLUE)
        eq0.set_color_by_tex(r"\implies", TEXT_MUTED)

        # Step 1: Era 2 Residual Harmonic Ringdown (t > t0)
        eq1 = MathTex(
            r"t > t_0 \implies",
            r"x_2(t) = \frac{2r\delta_{\text{st}}}{1 - r^2}\cos\left(\frac{\pi}{2r}\right)\cos\left[\omega_n\left(t - \frac{t_0}{2}\right)\right]",
            font_size=36
        ).move_to([0, 2.52, 0])
        eq1.set_color_by_tex(r"t > t_0", CYAN)
        eq1.set_color_by_tex(r"x_2(t)", CYAN)
        eq1.set_color_by_tex(r"r\delta_{\text{st}}", BLUE)
        eq1.set_color_by_tex(r"r^2", BLUE)
        eq1.set_color_by_tex(r"\cos\left(\frac{\pi}{2r}\right)", YELLOW)
        eq1.set_color_by_tex(r"\implies", TEXT_MUTED)

        # Step 2: Peak Dynamic Amplification Condition
        eq2 = MathTex(
            r"\frac{t_0}{\tau_n} \approx 0.80 \quad (r \approx 0.625)",
            r"\implies",
            r"\mathbf{DLF}_{\max} \approx 1.76",
            font_size=38
        ).move_to([0, 2.52, 0])
        eq2.set_color_by_tex(r"\frac{t_0}{\tau_n} \approx 0.80", YELLOW)
        eq2.set_color_by_tex(r"r \approx 0.625", BLUE)
        eq2.set_color_by_tex(r"\mathbf{DLF}_{\max} \approx 1.76", CORAL)
        eq2.set_color_by_tex(r"\implies", TEXT_MUTED)

        # ------------------------------------------------------------------
        # 4. Geometric Axes & Coordinate Mapping
        # ------------------------------------------------------------------
        # x-axis represents normalized time T = t / tau_n
        # y-axis represents normalized response x / delta_st and force F / F0
        axes = Axes(
            x_range=[0, 3.8, 0.5],
            y_range=[-2.0, 2.3, 0.5],
            x_length=10.8,
            y_length=4.0,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 2.5,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        ).move_to([0.2, -1.30, 0])

        lbl_t = MathTex(r"t / \tau_n", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(3.8, 0), RIGHT, buff=0.12)
        lbl_y = MathTex(r"x/\delta_{\text{st}}, \; F/F_0", font_size=20, color=TEXT_MUTED).next_to(axes.c2p(0, 2.3), UP, buff=0.10)

        # Horizontal Reference Level Lines
        line_1 = DashedLine(axes.c2p(0, 1.0), axes.c2p(3.6, 1.0), dash_length=0.08, color=TEXT_DIM, stroke_width=1.2)
        lbl_1 = MathTex(r"1.0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, 1.0), LEFT, buff=0.10)

        lbl_0 = MathTex(r"0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, 0), LEFT, buff=0.10)
        line_neg1 = DashedLine(axes.c2p(0, -1.0), axes.c2p(3.6, -1.0), dash_length=0.08, color=TEXT_DIM, stroke_width=1.0)
        lbl_neg1 = MathTex(r"-1.0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, -1.0), LEFT, buff=0.10)

        # Ticks along normalized time axis
        x_ticks = VGroup()
        for val, text in [(0.5, r"0.5"), (1.0, r"1.0"), (2.0, r"2.0"), (3.0, r"3.0")]:
            lbl = MathTex(text, font_size=18, color=TEXT_MUTED).next_to(axes.c2p(val, 0), DOWN, buff=0.22)
            tick = Line(axes.c2p(val, -0.06), axes.c2p(val, 0.06), stroke_width=1.2, color=TEXT_MUTED)
            x_ticks.add(lbl, tick)

        # Specific highlighted tick for critical t0 / tau_n = 0.8
        lbl_08 = MathTex(r"0.8", font_size=18, color=YELLOW).next_to(axes.c2p(0.8, 0), DOWN, buff=0.22)
        tick_08 = Line(axes.c2p(0.8, -0.07), axes.c2p(0.8, 0.07), stroke_width=1.6, color=YELLOW)
        x_ticks.add(lbl_08, tick_08)

        axes_group = VGroup(axes, lbl_t, lbl_y, line_1, lbl_1, lbl_0, line_neg1, lbl_neg1, x_ticks)

        # ------------------------------------------------------------------
        # 5. Physics Parameters & Waveform Geometry
        # ------------------------------------------------------------------
        T0 = 0.80               # Critical pulse duration ratio t0 / tau_n = 0.80
        r_val = 1.0 / (2.0 * T0)  # Frequency ratio r = tau_n / (2*t0) = 0.625

        # Half-Sine Excitation Pulse Geometry (0 <= T <= 0.80)
        t_vals_f = np.linspace(0, T0, 120)
        f_vals = np.sin(np.pi * t_vals_f / T0)
        pts_f = [axes.c2p(t, val) for t, val in zip(t_vals_f, f_vals)]

        pts_f_poly = [axes.c2p(0, 0)] + pts_f + [axes.c2p(T0, 0)]
        f_area = Polygon(*pts_f_poly, color=YELLOW, stroke_width=0, fill_color=YELLOW, fill_opacity=0.14)
        f_curve = VMobject().set_points_smoothly(pts_f).set_color(YELLOW).set_stroke(width=2.8)
        lbl_f0 = MathTex(r"F(t)", font_size=21, color=YELLOW).next_to(axes.c2p(0.40, 1.0), UP, buff=0.08)
        f_group = VGroup(f_area, f_curve, lbl_f0)

        # Boundary division at t0 = 0.80 tau_n
        boundary_t0 = DashedLine(
            axes.c2p(T0, -1.8),
            axes.c2p(T0, 2.1),
            dash_length=0.08,
            color=YELLOW,
            stroke_width=1.8
        )
        lbl_t0 = MathTex(r"t_0 = 0.80\tau_n", font_size=20, color=YELLOW).next_to(axes.c2p(T0, 2.1), UP, buff=0.10)

        # Era 1 Closed-Form Dynamic Response: 0 <= T <= 0.80
        # x1(T) = (1 / (1 - r^2)) * [sin(2*pi*r*T) - r*sin(2*pi*T)]
        t_vals_x1 = np.linspace(0, T0, 180)
        x1_vals = (1.0 / (1.0 - r_val**2)) * (
            np.sin(2.0 * np.pi * r_val * t_vals_x1) - r_val * np.sin(2.0 * np.pi * t_vals_x1)
        )
        pts_x1 = [axes.c2p(t, val) for t, val in zip(t_vals_x1, x1_vals)]
        x1_curve = VMobject().set_points_smoothly(pts_x1).set_color(CYAN).set_stroke(width=3.6)

        # Era 2 Residual Ringdown Response: 0.80 <= T <= 3.60
        # Continuous seamless connection with position and velocity matching
        t_vals_x2 = np.linspace(T0, 3.60, 350)
        x2_vals = -(2.0 * r_val / (1.0 - r_val**2)) * np.cos(np.pi / (2.0 * r_val)) * np.sin(
            2.0 * np.pi * (t_vals_x2 - 0.5 * T0)
        )
        pts_x2 = [axes.c2p(t, val) for t, val in zip(t_vals_x2, x2_vals)]
        x2_curve = VMobject().set_points_smoothly(pts_x2).set_color(CYAN).set_stroke(width=3.0)

        # Residual Oscillation Envelope Bounds (Amp approx 1.6595)
        amp_res = (2.0 * r_val / (1.0 - r_val**2)) * np.abs(np.cos(np.pi / (2.0 * r_val)))
        env_upper = DashedLine(
            axes.c2p(T0, amp_res),
            axes.c2p(3.6, amp_res),
            dash_length=0.08,
            color=CYAN,
            stroke_width=1.2,
            stroke_opacity=0.45
        )
        env_lower = DashedLine(
            axes.c2p(T0, -amp_res),
            axes.c2p(3.6, -amp_res),
            dash_length=0.08,
            color=CYAN,
            stroke_width=1.2,
            stroke_opacity=0.45
        )
        lbl_env = MathTex(
            r"\pm\mathbf{DLF}_{\text{res}} \approx 1.66",
            font_size=19,
            color=CYAN
        ).next_to(axes.c2p(3.0, amp_res), UP, buff=0.10)

        # ------------------------------------------------------------------
        # 6. Step 2: Peak Resonant Amplification Geometry
        # ------------------------------------------------------------------
        # Peak occurs at T_peak approx 0.6154 with DLF approx 1.7683
        t_peak = 0.6154
        x_peak = 1.7683

        dash_h = DashedLine(
            axes.c2p(0, x_peak),
            axes.c2p(t_peak, x_peak),
            dash_length=0.07,
            color=CORAL,
            stroke_width=1.4
        )
        dash_v = DashedLine(
            axes.c2p(t_peak, 0),
            axes.c2p(t_peak, x_peak),
            dash_length=0.07,
            color=CORAL,
            stroke_width=1.4
        )
        lbl_y_176 = MathTex(r"1.76", font_size=18, color=CORAL).next_to(axes.c2p(0, x_peak), LEFT, buff=0.10)
        lbl_t_062 = MathTex(r"0.62", font_size=16, color=CORAL).next_to(axes.c2p(t_peak, 0), DOWN, buff=0.20)

        dot_peak = Dot(axes.c2p(t_peak, x_peak), color=CORAL, radius=0.09)
        halo_peak = Dot(axes.c2p(t_peak, x_peak), color=CORAL, radius=0.22, fill_opacity=0.45)
        lbl_peak = MathTex(
            r"\mathbf{DLF}_{\max} \approx 1.76",
            font_size=22,
            color=CORAL
        ).next_to(axes.c2p(t_peak, x_peak), UP, buff=0.18)

        peak_group = VGroup(dash_h, dash_v, lbl_y_176, lbl_t_062, halo_peak, dot_peak, lbl_peak)

        # ------------------------------------------------------------------
        # 7. Animation Sequence (3 Steps, 2 Cuepoint Pauses)
        # ------------------------------------------------------------------

        # --- STEP 0: Minimal Title & Era 1 Forced Phase (0.0s - 4.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.5)
        self.play(Write(eq0), run_time=1.0)
        self.play(FadeIn(axes_group), run_time=0.6)
        self.play(
            FadeIn(f_group),
            Create(x1_curve),
            run_time=1.4
        )
        self.wait(0.5)  # Exact Cuepoint 0 = 4.0s (Pauses on slide entry)

        # --- STEP 1: Era 2 Residual Wave & Ringdown (4.0s - 8.5s) ---
        self.play(
            FadeTransform(eq0, eq1),
            Create(boundary_t0),
            FadeIn(lbl_t0),
            run_time=1.0
        )
        self.play(
            Create(x2_curve),
            run_time=1.3
        )
        self.play(
            Create(env_upper),
            Create(env_lower),
            FadeIn(lbl_env),
            run_time=0.9
        )
        self.wait(1.3)  # Exact Cuepoint 1 = 8.5s (Pauses for presenter explanation of residual ringdown)

        # --- STEP 2: Peak Resonant Amplification (8.5s - 15.0s) ---
        self.play(
            FadeTransform(eq1, eq2),
            FadeOut(lbl_env),
            run_time=1.0
        )
        self.play(
            FadeIn(peak_group, shift=UP * 0.10),
            run_time=1.2
        )
        self.play(
            Flash(axes.c2p(t_peak, x_peak), color=CORAL, line_length=0.22, num_lines=8, flash_radius=0.35),
            run_time=0.8
        )
        self.wait(3.5)  # Exact Cuepoint 2 = 15.0s (Calm final resting frame for Person 2 delivery)

"""
SLIDE-10: DualEraPartitionScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 2 (Mathematical Theory & Derivations)
Allocated Time: 19:30 – 21:30 (120 s)

Strict 3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 7 English words total)
      "Dual Temporal Eras" (3 words)
      "Primary Peak" (2 words)
      "Residual Peak" (2 words)
  - Frame-Accurate Step Cuepoints (3 Steps / 2 Pauses):
      Step 0 (0.0s - 4.0s): Minimal title & Era 1 (Forced Phase: 0 <= t <= t0) + Primary Peak
      Step 1 (4.0s - 8.0s): Boundary Handoff at t0: terminal state x(t0), x_dot(t0)
      Step 2 (8.0s - 14.5s): Era 2 (Residual Free Ringdown: t > t0) & Residual Peak comparison
"""

from manim import *
import numpy as np


class DualEraPartitionScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        CORAL      = ManimColor("#FF644E")   # Era 1 / Active Shock Pulse / Forced Response
        CYAN       = ManimColor("#58C4DD")   # Era 2 / Residual Free Ringdown Wave
        YELLOW     = ManimColor("#F7CA3B")   # Transient Force Pulse F(t)
        BLUE       = ManimColor("#0097F1")   # Boundary Handoff at t0 (UT Blue)
        GREEN      = ManimColor("#83C167")   # Natural Frequency omega_n
        TEXT_WHITE = ManimColor("#FFFFFF")
        TEXT_MUTED = ManimColor("#94A3B8")
        TEXT_DIM   = ManimColor("#475569")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Dual Temporal Eras}",
            font_size=48,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # ------------------------------------------------------------------
        # 3. Mathematical Equations Configuration (65" TV Large Typography)
        # ------------------------------------------------------------------
        # Step 0: Era 1 Governing Equation (0 <= t <= t0)
        eq1 = MathTex(
            r"0 \le t \le t_0",
            r"\implies",
            r"x_1(t)",
            r"=",
            r"\frac{1}{m\omega_n}",
            r"\int_0^t",
            r"F(\tau)",
            r"\sin\omega_n(t - \tau)",
            r"\, d\tau",
            font_size=38
        ).move_to([0, 2.45, 0])
        eq1.set_color_by_tex(r"0 \le t \le t_0", CORAL)
        eq1.set_color_by_tex(r"x_1(t)", CORAL)
        eq1.set_color_by_tex(r"F(\tau)", YELLOW)
        eq1.set_color_by_tex(r"\sin\omega_n(t - \tau)", CYAN)
        eq1.set_color_by_tex(r"\, d\tau", CORAL)
        eq1.set_color_by_tex(r"\implies", TEXT_MUTED)

        # Step 1: Boundary State Continuity at t = t0
        eq_boundary = MathTex(
            r"t = t_0",
            r"\implies",
            r"x(t_0) = x_1(t_0),",
            r"\quad",
            r"\dot{x}(t_0) = \dot{x}_1(t_0)",
            font_size=36
        ).move_to([0, 1.62, 0])
        eq_boundary.set_color_by_tex(r"t = t_0", BLUE)
        eq_boundary.set_color_by_tex(r"\implies", TEXT_MUTED)
        eq_boundary.set_color_by_tex(r"x(t_0)", BLUE)
        eq_boundary.set_color_by_tex(r"x_1(t_0)", CORAL)
        eq_boundary.set_color_by_tex(r"\dot{x}(t_0)", BLUE)
        eq_boundary.set_color_by_tex(r"\dot{x}_1(t_0)", CORAL)

        # Step 2: Era 2 Residual Free Vibration Equation (t > t0)
        eq2 = MathTex(
            r"t > t_0",
            r"\implies",
            r"x_2(t)",
            r"=",
            r"x(t_0)\cos\omega_n(t - t_0)",
            r"+",
            r"\frac{\dot{x}(t_0)}{\omega_n}\sin\omega_n(t - t_0)",
            font_size=36
        ).move_to([0, 1.62, 0])
        eq2.set_color_by_tex(r"t > t_0", CYAN)
        eq2.set_color_by_tex(r"\implies", TEXT_MUTED)
        eq2.set_color_by_tex(r"x_2(t)", CYAN)
        eq2.set_color_by_tex(r"x(t_0)", BLUE)
        eq2.set_color_by_tex(r"\dot{x}(t_0)", BLUE)
        eq2.set_color_by_tex(r"\cos\omega_n(t - t_0)", CYAN)
        eq2.set_color_by_tex(r"\sin\omega_n(t - t_0)", CYAN)
        eq2.set_color_by_tex(r"\omega_n", GREEN)

        # ------------------------------------------------------------------
        # 4. Geometric Axes & Dynamic Waveforms
        # ------------------------------------------------------------------
        axes = Axes(
            x_range=[0, 5.6, 1.0],
            y_range=[-1.6, 2.1, 1.0],
            x_length=11.2,
            y_length=3.4,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 2.5,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.15,
                "tip_height": 0.15,
            }
        ).move_to([0.2, -1.45, 0])

        lbl_t = MathTex(r"t", font_size=24, color=TEXT_MUTED).next_to(axes.c2p(5.6, 0), RIGHT, buff=0.12)
        lbl_y = MathTex(r"x, \, F", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(0, 2.1), UP, buff=0.10)

        # Physical Parameters
        t0 = 1.8
        tau_n = 2.0
        omega_n = 2.0 * np.pi / tau_n
        omega = np.pi / t0
        r_freq = omega / omega_n

        # --- ERA 1: Shock Force Pulse F(t) (0 <= t <= t0) ---
        t_pulse = np.linspace(0, t0, 120)
        pts_f = [axes.c2p(t, 1.15 * np.sin(omega * t)) for t in t_pulse]
        f_curve = VMobject().set_points_smoothly(pts_f).set_color(YELLOW).set_stroke(width=2.6)

        area_pts = [axes.c2p(0, 0)] + pts_f + [axes.c2p(t0, 0)]
        f_area = Polygon(*area_pts, color=YELLOW, stroke_width=0, fill_color=YELLOW, fill_opacity=0.14)
        lbl_f = MathTex(r"F(t)", font_size=22, color=YELLOW).move_to(axes.c2p(0.55, 1.25))

        # --- ERA 1: Forced Displacement Response x1(t) ---
        t_vals_1 = np.linspace(0, t0, 150)
        x1_vals = (1.0 / (1.0 - r_freq**2)) * (np.sin(omega * t_vals_1) - r_freq * np.sin(omega_n * t_vals_1))
        pts_x1 = [axes.c2p(t, x_val) for t, x_val in zip(t_vals_1, x1_vals)]
        x1_curve = VMobject().set_points_smoothly(pts_x1).set_color(CORAL).set_stroke(width=3.6)

        # Primary Peak in Era 1
        peak1_idx = int(np.argmax(x1_vals))
        t_peak1 = float(t_vals_1[peak1_idx])
        val_peak1 = float(x1_vals[peak1_idx])
        dot_primary = Dot(axes.c2p(t_peak1, val_peak1), color=CORAL, radius=0.075)
        halo_primary = Dot(axes.c2p(t_peak1, val_peak1), color=CORAL, radius=0.16, fill_opacity=0.35)
        lbl_primary = Tex(
            r"\textbf{Primary Peak}",
            font_size=20,
            color=CORAL
        ).next_to(dot_primary, UP, buff=0.14)
        primary_group = VGroup(halo_primary, dot_primary, lbl_primary)

        # --- BOUNDARY HANDOFF at t = t0 ---
        x_t0 = float(x1_vals[-1])
        v_t0 = float((1.0 / (1.0 - r_freq**2)) * (omega * np.cos(omega * t0) - r_freq * omega_n * np.cos(omega_n * t0)))

        boundary_line = DashedLine(
            axes.c2p(t0, -1.45),
            axes.c2p(t0, 1.95),
            dash_length=0.09,
            color=BLUE,
            stroke_width=2.0
        )
        lbl_t0 = MathTex(r"t_0", font_size=24, color=BLUE).next_to(axes.c2p(t0, 0), DOWN, buff=0.15)
        dot_boundary = Dot(axes.c2p(t0, x_t0), color=BLUE, radius=0.08)
        halo_boundary = Dot(axes.c2p(t0, x_t0), color=BLUE, radius=0.18, fill_opacity=0.40)
        lbl_boundary_state = MathTex(
            r"x(t_0), \, \dot{x}(t_0)",
            font_size=22,
            color=BLUE
        ).next_to(dot_boundary, UR, buff=0.18)

        # Tangent vector showing terminal velocity slope
        arrow_v = Arrow(
            axes.c2p(t0, x_t0),
            axes.c2p(t0 + 0.22, x_t0 + v_t0 * 0.22 * 0.16),
            color=BLUE,
            stroke_width=2.5,
            tip_length=0.13,
            buff=0
        )
        boundary_group = VGroup(boundary_line, lbl_t0, halo_boundary, dot_boundary, arrow_v, lbl_boundary_state)

        # --- ERA 2: Zero Force (t > t0) ---
        f_zero_line = DashedLine(
            axes.c2p(t0, 0),
            axes.c2p(5.4, 0),
            dash_length=0.10,
            color=TEXT_DIM,
            stroke_width=2.0
        )
        lbl_f_zero = MathTex(r"F(t) = 0", font_size=20, color=TEXT_MUTED).next_to(axes.c2p(3.6, 0), DOWN, buff=0.20)

        # --- ERA 2: Residual Free Vibration Wave x2(t) ---
        t_vals_2 = np.linspace(t0, 5.5, 300)
        x2_vals = x_t0 * np.cos(omega_n * (t_vals_2 - t0)) + (v_t0 / omega_n) * np.sin(omega_n * (t_vals_2 - t0))
        pts_x2 = [axes.c2p(t, x_val) for t, x_val in zip(t_vals_2, x2_vals)]
        x2_curve = VMobject().set_points_smoothly(pts_x2).set_color(CYAN).set_stroke(width=3.6)

        # Residual Peak in Era 2 (First positive crest in Era 2)
        mask_first_cycle = (t_vals_2 >= t0) & (t_vals_2 <= t0 + tau_n)
        sub_idx = int(np.argmax(x2_vals[mask_first_cycle]))
        t_peak2 = float(t_vals_2[mask_first_cycle][sub_idx])
        val_peak2 = float(x2_vals[mask_first_cycle][sub_idx])
        dot_residual = Dot(axes.c2p(t_peak2, val_peak2), color=CYAN, radius=0.075)
        halo_residual = Dot(axes.c2p(t_peak2, val_peak2), color=CYAN, radius=0.16, fill_opacity=0.35)
        lbl_residual = Tex(
            r"\textbf{Residual Peak}",
            font_size=20,
            color=CYAN
        ).next_to(dot_residual, UP, buff=0.14)
        residual_group = VGroup(halo_residual, dot_residual, lbl_residual)

        # ------------------------------------------------------------------
        # 5. Animation Sequence (3 Steps, 2 Cuepoint Pauses)
        # ------------------------------------------------------------------

        # --- STEP 0: Minimal Title & Era 1 Forced Phase (0.0s - 4.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.5)
        self.play(Write(eq1), run_time=1.0)
        self.play(
            Create(axes),
            FadeIn(lbl_t),
            FadeIn(lbl_y),
            run_time=0.6
        )
        self.play(
            Create(f_curve),
            FadeIn(f_area),
            FadeIn(lbl_f),
            Create(x1_curve),
            run_time=1.0
        )
        self.play(
            FadeIn(primary_group, shift=UP * 0.10),
            run_time=0.4
        )
        self.wait(0.5)  # Exact Cuepoint 0 = 4.0s (Pauses on slide entry)

        # --- STEP 1: Boundary Continuity at t = t0 (4.0s - 8.0s) ---
        self.play(
            Create(boundary_line),
            FadeIn(lbl_t0),
            FadeIn(halo_boundary, scale=1.4),
            FadeIn(dot_boundary),
            run_time=0.8
        )
        self.play(
            GrowArrow(arrow_v),
            FadeIn(lbl_boundary_state, shift=UR * 0.12),
            FadeIn(eq_boundary, shift=UP * 0.12),
            run_time=0.9
        )
        self.wait(2.3)  # Exact Cuepoint 1 = 8.0s (Pauses for presenter explanation of boundary state)

        # --- STEP 2: Era 2 Residual Free Vibration & Peak Comparison (8.0s - 14.5s) ---
        self.play(
            FadeTransform(eq_boundary, eq2),
            Create(f_zero_line),
            FadeIn(lbl_f_zero),
            run_time=1.1
        )
        self.play(
            Create(x2_curve),
            run_time=1.4
        )
        self.play(
            FadeIn(residual_group, shift=UP * 0.10),
            run_time=0.5
        )
        self.wait(3.5)  # Exact Cuepoint 2 = 14.5s (Calm final resting frame for Person 2 delivery)

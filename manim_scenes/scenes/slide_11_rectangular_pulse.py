"""
SLIDE-11: RectangularPulseScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 2 (Mathematical Theory & Derivations)
Allocated Time: 21:30 – 24:00 (150 s)

Strict 3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 4 English words total)
      "Rectangular Pulse" (2 words)
      "Zero Residual" (2 words)
  - Frame-Accurate Step Cuepoints (3 Steps / 2 Pauses):
      Step 0 (0.0s - 4.0s): Minimal title & Era 1 (Forced Phase: 0 <= t <= t0) + Dynamic Doubling (DLF = 2.0)
      Step 1 (4.0s - 8.5s): Era 2 Residual Amplitude Envelope (DLF_res = 2|sin(pi*t0/tau_n)|)
      Step 2 (8.5s - 15.0s): Complete Residual Cancellation (t0/tau_n = 1 -> DLF_res = 0)
"""

from manim import *
import numpy as np


class RectangularPulseScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        CORAL      = ManimColor("#FF644E")   # Era 1 / Forced Dynamic Doubling (DLF = 2.0)
        CYAN       = ManimColor("#58C4DD")   # Era 2 / Residual Free Oscillation Wave
        YELLOW     = ManimColor("#F7CA3B")   # Rectangular Shock Pulse F0
        GREEN      = ManimColor("#83C167")   # Cancellation Nodes & Zero Residual (DLF_res = 0)
        BLUE       = ManimColor("#0097F1")   # Boundary State / System Reference (UT Blue)
        TEXT_WHITE = ManimColor("#FFFFFF")
        TEXT_MUTED = ManimColor("#94A3B8")
        TEXT_DIM   = ManimColor("#475569")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 2 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Rectangular Pulse}",
            font_size=36,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # ------------------------------------------------------------------
        # 3. Mathematical Equations Configuration (Top Display Area)
        # ------------------------------------------------------------------
        # Step 0: Era 1 Closed-Form Forced Response (0 <= t <= t0)
        eq0 = MathTex(
            r"0 \le t \le t_0 \implies",
            r"x_1(t) = \delta_{\text{st}}(1 - \cos\omega_n t)",
            r"\implies",
            r"\mathbf{DLF}_{\max} = 2.0",
            font_size=31
        ).move_to([0, 2.50, 0])
        eq0.set_color_by_tex(r"0 \le t \le t_0", YELLOW)
        eq0.set_color_by_tex(r"x_1(t)", CORAL)
        eq0.set_color_by_tex(r"\cos\omega_n t", CORAL)
        eq0.set_color_by_tex(r"\mathbf{DLF}_{\max} = 2.0", CORAL)
        eq0.set_color_by_tex(r"\implies", TEXT_MUTED)

        # Step 1: Era 2 Residual Amplitude Envelope (t > t0)
        eq1 = MathTex(
            r"t > t_0 \implies",
            r"x_2(t)",
            r"\implies",
            r"\mathbf{DLF}_{\text{res}} = 2\left|\sin\left(\pi \frac{t_0}{\tau_n}\right)\right|",
            font_size=31
        ).move_to([0, 2.50, 0])
        eq1.set_color_by_tex(r"t > t_0", CYAN)
        eq1.set_color_by_tex(r"x_2(t)", CYAN)
        eq1.set_color_by_tex(r"\mathbf{DLF}_{\text{res}}", CYAN)
        eq1.set_color_by_tex(r"2\left|\sin", CYAN)
        eq1.set_color_by_tex(r"\frac{t_0}{\tau_n}", YELLOW)
        eq1.set_color_by_tex(r"\implies", TEXT_MUTED)

        # Step 2: Complete Residual Cancellation at Integer Periods
        eq2 = MathTex(
            r"\frac{t_0}{\tau_n} \in \{1, 2, 3, \dots\}",
            r"\implies",
            r"\mathbf{DLF}_{\text{res}} = 0",
            r"\quad \left[x(t_0) = 0, \; \dot{x}(t_0) = 0\right]",
            font_size=30
        ).move_to([0, 2.50, 0])
        eq2.set_color_by_tex(r"\frac{t_0}{\tau_n}", YELLOW)
        eq2.set_color_by_tex(r"\mathbf{DLF}_{\text{res}} = 0", GREEN)
        eq2.set_color_by_tex(r"x(t_0)", GREEN)
        eq2.set_color_by_tex(r"\dot{x}(t_0)", GREEN)
        eq2.set_color_by_tex(r"\implies", TEXT_MUTED)

        # ------------------------------------------------------------------
        # 4. Geometric Axes & Coordinate Mapping
        # ------------------------------------------------------------------
        # x-axis represents normalized time T = t / tau_n
        # y-axis represents normalized response x / delta_st and force F / F0
        axes = Axes(
            x_range=[0, 3.8, 0.5],
            y_range=[-1.5, 2.4, 0.5],
            x_length=10.8,
            y_length=3.8,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.6,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            }
        ).move_to([0.2, -1.25, 0])

        lbl_t = MathTex(r"t / \tau_n", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(3.8, 0), RIGHT, buff=0.12)
        lbl_y = MathTex(r"x/\delta_{\text{st}}, \; F/F_0", font_size=20, color=TEXT_MUTED).next_to(axes.c2p(0, 2.4), UP, buff=0.10)

        # Horizontal Reference Level Lines
        line_1 = DashedLine(axes.c2p(0, 1.0), axes.c2p(3.6, 1.0), dash_length=0.08, color=TEXT_DIM, stroke_width=1.2)
        lbl_1 = MathTex(r"1.0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, 1.0), LEFT, buff=0.10)

        line_2 = DashedLine(axes.c2p(0, 2.0), axes.c2p(3.6, 2.0), dash_length=0.08, color=CORAL, stroke_width=1.2, stroke_opacity=0.5)
        lbl_2 = MathTex(r"2.0", font_size=18, color=CORAL).next_to(axes.c2p(0, 2.0), LEFT, buff=0.10)

        lbl_0 = MathTex(r"0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, 0), LEFT, buff=0.10)
        line_neg1 = DashedLine(axes.c2p(0, -1.0), axes.c2p(3.6, -1.0), dash_length=0.08, color=TEXT_DIM, stroke_width=1.0)
        lbl_neg1 = MathTex(r"-1.0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, -1.0), LEFT, buff=0.10)

        # Ticks along normalized time axis
        x_ticks = VGroup()
        for val, text in [(0.5, r"0.5"), (1.0, r"1.0"), (2.0, r"2.0"), (3.0, r"3.0")]:
            lbl = MathTex(text, font_size=18, color=TEXT_MUTED).next_to(axes.c2p(val, 0), DOWN, buff=0.22)
            tick = Line(axes.c2p(val, -0.06), axes.c2p(val, 0.06), stroke_width=1.2, color=TEXT_MUTED)
            x_ticks.add(lbl, tick)

        axes_group = VGroup(axes, lbl_t, lbl_y, line_1, lbl_1, line_2, lbl_2, lbl_0, line_neg1, lbl_neg1, x_ticks)

        # ------------------------------------------------------------------
        # 5. Step 0 & 1 Setup: Arbitrary Pulse Duration (T0 = 1.25)
        # ------------------------------------------------------------------
        T0_val = 1.25

        # Rectangular Pulse F(t) geometry for T0 = 1.25
        pts_f_rect = [
            axes.c2p(0, 0),
            axes.c2p(0, 1.0),
            axes.c2p(T0_val, 1.0),
            axes.c2p(T0_val, 0)
        ]
        f_area_125 = Polygon(*pts_f_rect, color=YELLOW, stroke_width=0, fill_color=YELLOW, fill_opacity=0.14)
        f_top_125 = Line(axes.c2p(0, 1.0), axes.c2p(T0_val, 1.0), color=YELLOW, stroke_width=2.8)
        f_drop_125 = Line(axes.c2p(T0_val, 1.0), axes.c2p(T0_val, 0), color=YELLOW, stroke_width=2.8)
        lbl_f0 = MathTex(r"F_0", font_size=22, color=YELLOW).move_to(axes.c2p(0.35, 1.22))
        f_group_125 = VGroup(f_area_125, f_top_125, f_drop_125, lbl_f0)

        # Dashed vertical line at t0 = 1.25
        boundary_125 = DashedLine(
            axes.c2p(T0_val, -1.35),
            axes.c2p(T0_val, 2.2),
            dash_length=0.08,
            color=YELLOW,
            stroke_width=1.8
        )
        lbl_t0_125 = MathTex(r"t_0 = 1.25\tau_n", font_size=20, color=YELLOW).next_to(axes.c2p(T0_val, 2.2), UP, buff=0.10)

        # Era 1 Forced Response: x1(T) = 1 - cos(2*pi*T) for 0 <= T <= 1.25
        t_vals_1 = np.linspace(0, T0_val, 150)
        x1_vals = 1.0 - np.cos(2.0 * np.pi * t_vals_1)
        pts_x1 = [axes.c2p(t, val) for t, val in zip(t_vals_1, x1_vals)]
        x1_curve_125 = VMobject().set_points_smoothly(pts_x1).set_color(CORAL).set_stroke(width=3.6)

        # Primary Peak in Era 1 at T = 0.5 (DLF = 2.0)
        dot_peak = Dot(axes.c2p(0.5, 2.0), color=CORAL, radius=0.08)
        halo_peak = Dot(axes.c2p(0.5, 2.0), color=CORAL, radius=0.18, fill_opacity=0.35)
        lbl_peak = MathTex(r"\mathbf{DLF}_{\max} = 2.0", font_size=21, color=CORAL).next_to(dot_peak, UP, buff=0.14)
        peak_group = VGroup(halo_peak, dot_peak, lbl_peak)

        # Era 2 Residual Oscillation for T0 = 1.25 (T > 1.25)
        # Amplitude DLF_res = 2*|sin(pi*1.25)| = 2*(sqrt(2)/2) = sqrt(2) approx 1.414
        # Crest occurs at T = 2.375 where x2 = +1.414
        t_vals_2 = np.linspace(T0_val, 3.6, 250)
        x2_vals_125 = 2.0 * np.sin(np.pi * T0_val) * np.sin(2.0 * np.pi * (t_vals_2 - T0_val / 2.0))
        pts_x2 = [axes.c2p(t, val) for t, val in zip(t_vals_2, x2_vals_125)]
        x2_curve_125 = VMobject().set_points_smoothly(pts_x2).set_color(CYAN).set_stroke(width=3.6)

        # Residual Envelope Lines (+/- 1.414)
        env_upper = DashedLine(axes.c2p(T0_val, 1.414), axes.c2p(3.6, 1.414), dash_length=0.08, color=CYAN, stroke_width=1.5)
        env_lower = DashedLine(axes.c2p(T0_val, -1.414), axes.c2p(3.6, -1.414), dash_length=0.08, color=CYAN, stroke_width=1.5)
        lbl_env = MathTex(r"\pm \mathbf{DLF}_{\text{res}} = \pm 1.41", font_size=19, color=CYAN).next_to(axes.c2p(3.6, 1.414), UR, buff=0.10)

        # True crest in Era 2 at T = 2.375
        dot_res_peak = Dot(axes.c2p(2.375, 1.414), color=CYAN, radius=0.075)
        halo_res_peak = Dot(axes.c2p(2.375, 1.414), color=CYAN, radius=0.16, fill_opacity=0.35)
        lbl_res_peak = MathTex(r"\mathbf{DLF}_{\text{res}} = 1.41", font_size=19, color=CYAN).next_to(dot_res_peak, UP, buff=0.14)
        residual_peak_group = VGroup(halo_res_peak, dot_res_peak, lbl_res_peak)

        # ------------------------------------------------------------------
        # 6. Step 2 Setup: Complete Residual Cancellation (T0 = 1.0)
        # ------------------------------------------------------------------
        T0_cancel = 1.0

        pts_f_cancel = [
            axes.c2p(0, 0),
            axes.c2p(0, 1.0),
            axes.c2p(T0_cancel, 1.0),
            axes.c2p(T0_cancel, 0)
        ]
        f_area_100 = Polygon(*pts_f_cancel, color=YELLOW, stroke_width=0, fill_color=YELLOW, fill_opacity=0.14)
        f_top_100 = Line(axes.c2p(0, 1.0), axes.c2p(T0_cancel, 1.0), color=YELLOW, stroke_width=2.8)
        f_drop_100 = Line(axes.c2p(T0_cancel, 1.0), axes.c2p(T0_cancel, 0), color=YELLOW, stroke_width=2.8)

        boundary_100 = DashedLine(
            axes.c2p(T0_cancel, -1.35),
            axes.c2p(T0_cancel, 2.2),
            dash_length=0.08,
            color=GREEN,
            stroke_width=1.8
        )
        lbl_t0_100 = MathTex(r"t_0 = \tau_n", font_size=20, color=GREEN).next_to(axes.c2p(T0_cancel, 2.2), UP, buff=0.10)

        # Era 1 for T0 = 1.0 completes exactly 1 full cycle to (1.0, 0)
        t_vals_1_cancel = np.linspace(0, T0_cancel, 150)
        x1_vals_cancel = 1.0 - np.cos(2.0 * np.pi * t_vals_1_cancel)
        pts_x1_cancel = [axes.c2p(t, val) for t, val in zip(t_vals_1_cancel, x1_vals_cancel)]
        x1_curve_100 = VMobject().set_points_smoothly(pts_x1_cancel).set_color(CORAL).set_stroke(width=3.6)

        # Era 2 for T0 = 1.0 is IDENTICALLY ZERO! (Flatline along x-axis)
        flat_zero_line = Line(axes.c2p(T0_cancel, 0), axes.c2p(3.6, 0), stroke_width=4.0, color=GREEN)

        # Cancellation Node at (1.0, 0)
        dot_cancel = Dot(axes.c2p(1.0, 0), color=GREEN, radius=0.09)
        halo_cancel = Dot(axes.c2p(1.0, 0), color=GREEN, radius=0.22, fill_opacity=0.45)
        lbl_zero_res = Tex(r"\textbf{Zero Residual}", font_size=22, color=GREEN).next_to(axes.c2p(2.3, 0), UP, buff=0.22)
        cancel_group = VGroup(halo_cancel, dot_cancel, lbl_zero_res)

        # Additional Cancellation Nodes at integer multiples T = 2.0, 3.0
        dot_node2 = Dot(axes.c2p(2.0, 0), color=GREEN, radius=0.075)
        halo_node2 = Dot(axes.c2p(2.0, 0), color=GREEN, radius=0.18, fill_opacity=0.35)
        dot_node3 = Dot(axes.c2p(3.0, 0), color=GREEN, radius=0.075)
        halo_node3 = Dot(axes.c2p(3.0, 0), color=GREEN, radius=0.18, fill_opacity=0.35)
        integer_nodes_group = VGroup(halo_node2, dot_node2, halo_node3, dot_node3)

        # ------------------------------------------------------------------
        # 7. Animation Sequence (3 Steps, 2 Cuepoint Pauses)
        # ------------------------------------------------------------------

        # --- STEP 0: Minimal Title & Era 1 Forced Phase (0.0s - 4.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.5)
        self.play(Write(eq0), run_time=1.0)
        self.play(
            FadeIn(axes_group),
            run_time=0.6
        )
        self.play(
            FadeIn(f_group_125),
            Create(x1_curve_125),
            run_time=1.0
        )
        self.play(
            FadeIn(peak_group, shift=UP * 0.10),
            run_time=0.4
        )
        self.wait(0.5)  # Exact Cuepoint 0 = 4.0s (Pauses on slide entry)

        # --- STEP 1: Era 2 Residual Amplitude Envelope (4.0s - 8.5s) ---
        self.play(
            TransformMatchingTex(eq0, eq1),
            Create(boundary_125),
            FadeIn(lbl_t0_125),
            run_time=1.0
        )
        self.play(
            Create(x2_curve_125),
            run_time=1.2
        )
        self.play(
            Create(env_upper),
            Create(env_lower),
            FadeIn(lbl_env),
            FadeIn(residual_peak_group, shift=UP * 0.10),
            run_time=0.9
        )
        self.wait(1.4)  # Exact Cuepoint 1 = 8.5s (Pauses for presenter explanation of residual envelope)

        # --- STEP 2: Complete Residual Cancellation at t0 = tau_n (8.5s - 15.0s) ---
        self.play(
            TransformMatchingTex(eq1, eq2),
            FadeOut(env_upper),
            FadeOut(env_lower),
            FadeOut(lbl_env),
            FadeOut(residual_peak_group),
            run_time=0.9
        )
        self.play(
            Transform(boundary_125, boundary_100),
            Transform(lbl_t0_125, lbl_t0_100),
            Transform(f_area_125, f_area_100),
            Transform(f_top_125, f_top_100),
            Transform(f_drop_125, f_drop_100),
            Transform(x1_curve_125, x1_curve_100),
            Transform(x2_curve_125, flat_zero_line),
            run_time=1.5
        )
        self.play(
            FadeIn(cancel_group, shift=UP * 0.10),
            FadeIn(integer_nodes_group, shift=UP * 0.08),
            run_time=0.9
        )
        self.wait(3.2)  # Exact Cuepoint 2 = 15.0s (Calm final resting frame for Person 2 delivery)

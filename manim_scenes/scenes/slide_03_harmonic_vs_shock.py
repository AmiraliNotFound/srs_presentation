"""
SLIDE-03A: HarmonicVsShockScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Modeling)

Step-Controlled Visual Comparison:
  - Step 0 (0.0s - 1.4s): Minimal centered header on pure black.
  - Step 1 (1.4s - 5.2s): Left side reveals — Steady-State Harmonic curve (F(t) = F_0 sin(omega t)).
  - Step 2 (5.2s - 9.4s): Right side reveals — Transient Shock Pulse (0 <= t <= t_0) with +100% overshoot.
  - Step 3 (9.4s - 15.0s): Unboxed comparison metrics fade in below each plot (large typography, max 3-4 words/line).
"""

from manim import *
import numpy as np


class HarmonicVsShockScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black & UT Blue)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # University of Tehran Primary Accent
        FORCE_GOLD  = ManimColor("#F7CA3B")   # Harmonic Excitation & Static Accents
        DANGER_RED  = ManimColor("#FF644E")   # Shock Pulse, Dynamic Overshoot & Alert
        SPRING_CYAN = ManimColor("#58C4DD")   # Restoring Spring / Response Waveform
        SAFE_GREEN  = ManimColor("#83C167")   # Damping / Safe Zone
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        TEXT_DIM    = ManimColor("#64748B")
        CARD_BG     = ManimColor("#080D1A")
        BORDER_DIM  = ManimColor("#1E293B")
        BORDER_MID  = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Header & Title (Floating at top, minimal & centered)
        # ------------------------------------------------------------------
        header_tag = Tex(
            r"\textsc{Physical Foundations} \quad $\bullet$ \quad \textsc{The Core Distinction}",
            font_size=20,
            color=TEHRAN_BLUE
        ).move_to([0, 3.42, 0])

        main_title = Tex(
            r"\textbf{Harmonic Vibration vs. Transient Shock}",
            font_size=38,
            color=TEXT_WHITE
        ).next_to(header_tag, DOWN, buff=0.14)

        header_rule = Line(
            start=LEFT * 6.2,
            end=RIGHT * 6.2,
            color=TEHRAN_BLUE,
            stroke_width=1.5
        ).next_to(main_title, DOWN, buff=0.16)

        col_divider = DashedLine(
            start=[0, 2.38, 0],
            end=[0, -3.40, 0],
            color=BORDER_MID,
            stroke_width=1.2,
            dash_length=0.12
        )

        # ------------------------------------------------------------------
        # 3. Column Positions & Layout Geometry
        # ------------------------------------------------------------------
        left_cx = -3.55
        right_cx = 3.55

        # ==================================================================
        # LEFT COLUMN: Steady-State Harmonic Vibration
        # ==================================================================
        title_left = Tex(
            r"\textsc{\textbf{Steady-State Harmonic}}",
            font_size=23,
            color=FORCE_GOLD
        ).move_to([left_cx, 2.18, 0])

        eq_left = Tex(
            r"$F(t) = F_0 \sin(\omega t), \quad t \in [0, \infty)$",
            font_size=20,
            color=TEXT_OFFWH
        ).move_to([left_cx, 1.72, 0])

        # Left Axes & Waveforms (Harmonic)
        axes_left = Axes(
            x_range=[0, 3.5, 1],
            y_range=[-1.4, 1.4, 1],
            x_length=5.2,
            y_length=2.1,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([left_cx, 0.42, 0])

        lbl_left_x = Tex(r"Time $t$", font_size=13, color=TEXT_MUTED).next_to(axes_left.c2p(3.5, 0), RIGHT, buff=0.10)

        t_harm = np.linspace(0, 3.5, 200)
        harm_force_pts = [axes_left.c2p(t, 0.80 * np.sin(2 * np.pi * t)) for t in t_harm]
        harm_disp_pts  = [axes_left.c2p(t, 1.10 * np.sin(2 * np.pi * t - 0.45)) for t in t_harm]

        curve_harm_f = VMobject().set_points_smoothly(harm_force_pts).set_color(FORCE_GOLD).set_stroke(width=1.6)
        curve_harm_x = VMobject().set_points_smoothly(harm_disp_pts).set_color(SPRING_CYAN).set_stroke(width=2.5)

        env_top = DashedLine(
            start=axes_left.c2p(0, 1.10),
            end=axes_left.c2p(3.5, 1.10),
            color=BORDER_MID,
            stroke_width=1.0,
            dash_length=0.08
        )
        env_bot = DashedLine(
            start=axes_left.c2p(0, -1.10),
            end=axes_left.c2p(3.5, -1.10),
            color=BORDER_MID,
            stroke_width=1.0,
            dash_length=0.08
        )
        lbl_env = Tex(r"$\pm X_{\text{steady}} = M \delta_{\text{st}}$", font_size=13, color=TEXT_MUTED).move_to([left_cx - 1.25, 1.54, 0])

        leg_harm_x = Line(ORIGIN, RIGHT * 0.30, color=SPRING_CYAN, stroke_width=2.5)
        leg_harm_x_lbl = Tex(r"$x(t)$", font_size=13, color=SPRING_CYAN).next_to(leg_harm_x, RIGHT, buff=0.06)
        leg_harm_f = Line(ORIGIN, RIGHT * 0.30, color=FORCE_GOLD, stroke_width=1.8)
        leg_harm_f_lbl = Tex(r"$F(t)$", font_size=13, color=FORCE_GOLD).next_to(leg_harm_f, RIGHT, buff=0.06)
        leg_harm_grp = VGroup(
            VGroup(leg_harm_x, leg_harm_x_lbl),
            VGroup(leg_harm_f, leg_harm_f_lbl)
        ).arrange(RIGHT, buff=0.20).move_to([left_cx + 1.35, 1.54, 0])

        # Left Comparison Metrics (Unboxed, spacious, max 3-4 words/line)
        m_left_1 = Tex(r"$t \to \infty$ \ (Indefinite Duration)", font_size=20, color=TEXT_OFFWH)
        m_left_2 = Tex(r"Governed by $r = \omega / \omega_n$", font_size=21, color=FORCE_GOLD)
        m_left_3 = Tex(r"High-Cycle Fatigue Failure", font_size=20, color=TEXT_MUTED)
        metrics_left = VGroup(m_left_1, m_left_2, m_left_3).arrange(DOWN, buff=0.34).move_to([left_cx, -2.15, 0])

        # ==================================================================
        # RIGHT COLUMN: Transient Dynamic Shock Pulse
        # ==================================================================
        title_right = Tex(
            r"\textsc{\textbf{Transient Shock Pulse}}",
            font_size=23,
            color=DANGER_RED
        ).move_to([right_cx, 2.18, 0])

        eq_right = Tex(
            r"$F(t) \ne 0 \text{ only for } 0 \le t \le t_0 \quad (t_0 \lesssim \tau_n)$",
            font_size=20,
            color=TEXT_OFFWH
        ).move_to([right_cx, 1.72, 0])

        # Right Axes & Shock Response
        axes_right = Axes(
            x_range=[0, 3.5, 1],
            y_range=[-2.2, 2.5, 1],
            x_length=5.2,
            y_length=2.1,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([right_cx, 0.42, 0])

        lbl_right_x = Tex(r"Time $t$", font_size=13, color=TEXT_MUTED).next_to(axes_right.c2p(3.5, 0), RIGHT, buff=0.10)

        pulse_pts = [
            axes_right.c2p(0.0, 0.0),
            axes_right.c2p(0.0, 1.0),
            axes_right.c2p(1.0, 1.0),
            axes_right.c2p(1.0, 0.0)
        ]
        pulse_box = Polygon(*pulse_pts, color=DANGER_RED, stroke_width=1.6, fill_color=DANGER_RED, fill_opacity=0.22)
        pulse_lbl = Tex(r"Pulse $F_0$", font_size=13, color=DANGER_RED).move_to(axes_right.c2p(0.65, 0.35))

        line_static = DashedLine(
            start=axes_right.c2p(0, 1.0),
            end=axes_right.c2p(3.5, 1.0),
            color=FORCE_GOLD,
            stroke_width=1.4,
            dash_length=0.08
        )
        lbl_static = Tex(
            r"$\delta_{\text{st}} = \frac{F_0}{k} \text{ (Static Baseline)}$",
            font_size=12.5,
            color=FORCE_GOLD
        ).next_to(axes_right.c2p(3.5, 1.0), LEFT, buff=0.08).shift(DOWN * 0.13)

        line_overshoot = DashedLine(
            start=axes_right.c2p(0, 2.0),
            end=axes_right.c2p(3.5, 2.0),
            color=DANGER_RED,
            stroke_width=1.6,
            dash_length=0.08
        )
        lbl_overshoot = Tex(
            r"$x_{\max} = 2.0\,\delta_{\text{st}} \ (\textbf{DLF} = 2.0)$",
            font_size=13,
            color=DANGER_RED
        ).next_to(axes_right.c2p(3.5, 2.0), LEFT, buff=0.08).shift(UP * 0.13)

        t_shock = np.linspace(0, 3.5, 250)
        shock_pts = []
        for t in t_shock:
            if t <= 1.0:
                x_val = 1.0 - np.cos(np.pi * t)
            else:
                x_val = 2.0 * np.cos(np.pi * (t - 1.0)) * np.exp(-0.045 * np.pi * (t - 1.0))
            shock_pts.append(axes_right.c2p(t, x_val))

        curve_shock_x = VMobject().set_points_smoothly(shock_pts).set_color(SPRING_CYAN).set_stroke(width=2.6)

        peak_coord = axes_right.c2p(1.0, 2.0)
        peak_dot = Dot(point=peak_coord, radius=0.075, color=DANGER_RED)
        peak_ring = Arc(radius=0.16, start_angle=0, angle=TAU, stroke_color=DANGER_RED, stroke_width=2.0).move_to(peak_coord)

        overshoot_callout = Tex(
            r"\textbf{+100\% Dynamic Overshoot!}",
            font_size=14,
            color=DANGER_RED
        ).move_to([right_cx + 0.35, 1.54, 0])

        overshoot_arrow = Arrow(
            start=overshoot_callout.get_left() + LEFT * 0.05,
            end=peak_coord + UP * 0.08 + RIGHT * 0.08,
            color=DANGER_RED,
            stroke_width=2.0,
            tip_length=0.10
        )

        # Right Comparison Metrics (Unboxed, spacious, max 3-4 words/line)
        m_right_1 = Tex(r"$t_0 \lesssim \tau_n$ \ (Short Transient Pulse)", font_size=20, color=TEXT_OFFWH)
        m_right_2 = Tex(r"Governed by $t_0 / \tau_n$", font_size=21, color=DANGER_RED)
        m_right_3 = Tex(r"Immediate Peak Stress Rupture", font_size=20, color=TEXT_MUTED)
        metrics_right = VGroup(m_right_1, m_right_2, m_right_3).arrange(DOWN, buff=0.34).move_to([right_cx, -2.15, 0])

        # ------------------------------------------------------------------
        # 4. Step-Controlled Timeline & Cuepoint Milestones
        # ------------------------------------------------------------------
        # --- Step 0: Initial Load (0.0s - 1.4s) ---
        self.play(
            FadeIn(header_tag, shift=DOWN * 0.20),
            Write(main_title),
            GrowFromCenter(header_rule),
            GrowFromEdge(col_divider, UP),
            run_time=1.2
        )
        self.wait(0.2)  # Pause point: Step 0 completes at 1.4s

        # --- Step 1: Steady-State Harmonic Reveal (1.4s - 5.2s) ---
        self.play(
            FadeIn(title_left, shift=DOWN * 0.15),
            FadeIn(eq_left, shift=DOWN * 0.12),
            Create(axes_left),
            Write(lbl_left_x),
            FadeIn(leg_harm_grp),
            run_time=1.0
        )
        self.play(
            Create(curve_harm_f, run_time=2.0),
            Create(curve_harm_x, run_time=2.2),
            Create(env_top, run_time=1.5),
            Create(env_bot, run_time=1.5),
            FadeIn(lbl_env, run_time=1.0),
            rate_func=linear
        )
        self.wait(0.4)  # Pause point: Step 1 completes at 5.2s

        # --- Step 2: Transient Shock Pulse Reveal (5.2s - 9.4s) ---
        self.play(
            FadeIn(title_right, shift=DOWN * 0.15),
            FadeIn(eq_right, shift=DOWN * 0.12),
            Create(axes_right),
            Write(lbl_right_x),
            FadeIn(pulse_box),
            Write(pulse_lbl),
            Create(line_static),
            FadeIn(lbl_static),
            run_time=1.2
        )
        self.play(
            Create(curve_shock_x, run_time=2.2),
            rate_func=linear
        )
        self.play(
            Create(line_overshoot),
            FadeIn(lbl_overshoot),
            GrowFromCenter(peak_dot),
            GrowFromCenter(peak_ring),
            GrowArrow(overshoot_arrow),
            FadeIn(overshoot_callout, shift=UP * 0.1),
            run_time=1.0
        )
        self.wait(0.4)  # Pause point: Step 2 completes at 9.4s

        # --- Step 3: Comparison Metrics Fade-In (9.4s - 15.0s) ---
        self.play(
            FadeIn(metrics_left, shift=UP * 0.25),
            FadeIn(metrics_right, shift=UP * 0.25),
            run_time=1.4
        )

        # Pulse highlight on fatigue vs peak rupture metrics
        self.play(
            m_left_2.animate.scale(1.08),
            m_right_2.animate.scale(1.08),
            run_time=0.5
        )
        self.play(
            m_left_2.animate.scale(1 / 1.08),
            m_right_2.animate.scale(1 / 1.08),
            run_time=0.5
        )

        # Final resting hold frame for oral commentary
        self.wait(3.5)

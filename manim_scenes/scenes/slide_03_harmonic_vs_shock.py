"""
SLIDE-03: HarmonicVsShockScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Modeling)
Allocated Time: 01:30 - 04:00 (150 seconds / 2.5 minutes)

Theoretical Core:
  - Contrast steady-state harmonic excitation with transient shock loading.
  - Left Half: Steady-state harmonic (F(t) = F_0 sin(omega t), infinite cycles, fatigue S-N metric, r = omega/omega_n).
  - Right Half: Transient shock pulse (F(t) != 0 only for 0 <= t <= t_0, t_0 <= tau_n, immediate peak yield rupture, t_0/tau_n).
  - The Static Dilemma: Under rapid shock loading, dynamic inertial lag causes the mass to overshoot equilibrium,
    generating a Dynamic Load Factor (DLF = x_max / delta_st) up to 2.0 and 4x the static strain energy.
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
        # 2. Header & Title (Floating at top)
        # ------------------------------------------------------------------
        header_tag = Tex(
            r"\textsc{Physical Foundations} \quad $\bullet$ \quad \textsc{The Core Distinction}",
            font_size=20,
            color=TEHRAN_BLUE
        ).move_to([0, 3.52, 0])

        main_title = Tex(
            r"\textbf{Harmonic Vibration vs. Transient Shock}",
            font_size=36,
            color=TEXT_WHITE
        ).next_to(header_tag, DOWN, buff=0.12)

        subtitle = Tex(
            r"Why Classical Static Analysis Fails Catastrophically Under Shock Loading",
            font_size=18,
            color=TEXT_MUTED
        ).next_to(main_title, DOWN, buff=0.10)

        header_rule = Line(
            start=LEFT * 6.4,
            end=RIGHT * 6.4,
            color=TEHRAN_BLUE,
            stroke_width=1.5
        ).next_to(subtitle, DOWN, buff=0.12)

        header_group = VGroup(header_tag, main_title, subtitle, header_rule)

        # Subtle vertical separator between Left and Right columns
        col_divider = DashedLine(
            start=[0, 2.32, 0],
            end=[0, -1.65, 0],
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
        pill_left = RoundedRectangle(
            width=4.6,
            height=0.42,
            corner_radius=0.12,
            stroke_color=FORCE_GOLD,
            stroke_width=1.6,
            fill_color=CARD_BG,
            fill_opacity=0.95
        ).move_to([left_cx, 2.18, 0])

        pill_left_lbl = Tex(
            r"\textbf{STEADY-STATE HARMONIC VIBRATION}",
            font_size=18,
            color=FORCE_GOLD
        ).move_to(pill_left)

        pill_left_grp = VGroup(pill_left, pill_left_lbl)

        eq_left = Tex(
            r"$F(t) = F_0 \sin(\omega t), \quad t \in [0, \infty)$",
            font_size=19,
            color=TEXT_OFFWH
        ).move_to([left_cx, 1.76, 0])

        # Left Axes & Waveforms (Harmonic)
        axes_left = Axes(
            x_range=[0, 3.5, 1],
            y_range=[-1.35, 1.35, 1],
            x_length=4.9,
            y_length=1.45,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([left_cx, 0.74, 0])

        lbl_left_x = Tex(r"Time $t$", font_size=13, color=TEXT_MUTED).next_to(axes_left.c2p(3.5, 0), RIGHT, buff=0.10)

        # Harmonic Curves (Excitation + Response)
        t_harm = np.linspace(0, 3.5, 200)
        harm_force_pts = [axes_left.c2p(t, 0.75 * np.sin(2 * np.pi * t)) for t in t_harm]
        harm_disp_pts  = [axes_left.c2p(t, 1.05 * np.sin(2 * np.pi * t - 0.45)) for t in t_harm]

        curve_harm_f = VMobject().set_points_smoothly(harm_force_pts).set_color(FORCE_GOLD).set_stroke(width=1.6)
        curve_harm_x = VMobject().set_points_smoothly(harm_disp_pts).set_color(SPRING_CYAN).set_stroke(width=2.5)

        # Envelopes (+X and -X bounds)
        env_top = DashedLine(
            start=axes_left.c2p(0, 1.05),
            end=axes_left.c2p(3.5, 1.05),
            color=BORDER_MID,
            stroke_width=1.0,
            dash_length=0.08
        )
        env_bot = DashedLine(
            start=axes_left.c2p(0, -1.05),
            end=axes_left.c2p(3.5, -1.05),
            color=BORDER_MID,
            stroke_width=1.0,
            dash_length=0.08
        )
        lbl_env = Tex(r"$\pm X_{\text{steady}} = M \delta_{\text{st}}$", font_size=13, color=TEXT_MUTED).move_to([left_cx - 1.15, 1.52, 0])

        # Small Curve Legend on Left Plot
        leg_harm_x = Line(ORIGIN, RIGHT * 0.30, color=SPRING_CYAN, stroke_width=2.5)
        leg_harm_x_lbl = Tex(r"$x(t)$", font_size=13, color=SPRING_CYAN).next_to(leg_harm_x, RIGHT, buff=0.06)
        leg_harm_f = Line(ORIGIN, RIGHT * 0.30, color=FORCE_GOLD, stroke_width=1.8)
        leg_harm_f_lbl = Tex(r"$F(t)$", font_size=13, color=FORCE_GOLD).next_to(leg_harm_f, RIGHT, buff=0.06)
        leg_harm_grp = VGroup(
            VGroup(leg_harm_x, leg_harm_x_lbl),
            VGroup(leg_harm_f, leg_harm_f_lbl)
        ).arrange(RIGHT, buff=0.20).move_to([left_cx + 1.30, 1.52, 0])

        # Left Metrics Card
        card_left = RoundedRectangle(
            width=5.5,
            height=1.28,
            corner_radius=0.14,
            stroke_color=BORDER_DIM,
            stroke_width=1.4,
            fill_color=CARD_BG,
            fill_opacity=0.92
        ).move_to([left_cx, -0.92, 0])

        m_left_1 = Tex(r"$\bullet$ \ \textbf{Duration:} Indefinite ($t \to \infty$); homogeneous transients decay", font_size=15, color=TEXT_OFFWH)
        m_left_2 = Tex(r"$\bullet$ \ \textbf{Governing Metric:} Frequency Ratio $r = \omega / \omega_n \ \implies M(r, \zeta)$", font_size=15, color=FORCE_GOLD)
        m_left_3 = Tex(r"$\bullet$ \ \textbf{Failure Mode:} High-cycle fatigue ($10^6+$ cycles, S-N curve)", font_size=15, color=TEXT_MUTED)
        metrics_left = VGroup(m_left_1, m_left_2, m_left_3).arrange(DOWN, aligned_edge=LEFT, buff=0.13).move_to(card_left.get_center())

        left_column_grp = VGroup(
            pill_left_grp, eq_left, axes_left, lbl_left_x,
            leg_harm_grp, env_top, env_bot, lbl_env, card_left, metrics_left
        )

        # ==================================================================
        # RIGHT COLUMN: Transient Dynamic Shock Pulse
        # ==================================================================
        pill_right = RoundedRectangle(
            width=4.6,
            height=0.42,
            corner_radius=0.12,
            stroke_color=DANGER_RED,
            stroke_width=1.6,
            fill_color=CARD_BG,
            fill_opacity=0.95
        ).move_to([right_cx, 2.18, 0])

        pill_right_lbl = Tex(
            r"\textbf{TRANSIENT DYNAMIC SHOCK PULSE}",
            font_size=18,
            color=DANGER_RED
        ).move_to(pill_right)

        pill_right_grp = VGroup(pill_right, pill_right_lbl)

        eq_right = Tex(
            r"$F(t) \ne 0 \text{ only for } 0 \le t \le t_0 \quad (t_0 \lesssim \tau_n)$",
            font_size=19,
            color=TEXT_OFFWH
        ).move_to([right_cx, 1.76, 0])

        # Right Axes & Shock Response
        axes_right = Axes(
            x_range=[0, 3.5, 1],
            y_range=[-2.2, 2.45, 1],
            x_length=4.9,
            y_length=1.45,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([right_cx, 0.74, 0])

        lbl_right_x = Tex(r"Time $t$", font_size=13, color=TEXT_MUTED).next_to(axes_right.c2p(3.5, 0), RIGHT, buff=0.10)

        # Rectangular Pulse Graphic (0 <= t <= 1.0, height = 1.0 delta_st)
        pulse_pts = [
            axes_right.c2p(0.0, 0.0),
            axes_right.c2p(0.0, 1.0),
            axes_right.c2p(1.0, 1.0),
            axes_right.c2p(1.0, 0.0)
        ]
        pulse_box = Polygon(*pulse_pts, color=DANGER_RED, stroke_width=1.6, fill_color=DANGER_RED, fill_opacity=0.22)
        pulse_lbl = Tex(r"Pulse $F_0$", font_size=13, color=DANGER_RED).move_to(axes_right.c2p(0.65, 0.32))

        # Static Deflection Reference Line (delta_st = F0 / k = 1.0)
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

        # Dynamic Overshoot Peak Reference Line (x_max = 2.0 delta_st)
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

        # Exact Dynamic SDOF Shock Response
        t_shock = np.linspace(0, 3.5, 250)
        shock_pts = []
        for t in t_shock:
            if t <= 1.0:
                x_val = 1.0 - np.cos(np.pi * t)
            else:
                x_val = 2.0 * np.cos(np.pi * (t - 1.0)) * np.exp(-0.045 * np.pi * (t - 1.0))
            shock_pts.append(axes_right.c2p(t, x_val))

        curve_shock_x = VMobject().set_points_smoothly(shock_pts).set_color(SPRING_CYAN).set_stroke(width=2.6)

        # Overshoot Peak Indicator Dot & Callout (Shifted right of peak to avoid overlap)
        peak_coord = axes_right.c2p(1.0, 2.0)
        peak_dot = Dot(point=peak_coord, radius=0.075, color=DANGER_RED)
        peak_ring = Arc(radius=0.16, start_angle=0, angle=TAU, stroke_color=DANGER_RED, stroke_width=2.0).move_to(peak_coord)

        overshoot_callout = Tex(
            r"\textbf{+100\% Dynamic Overshoot!}",
            font_size=14,
            color=DANGER_RED
        ).move_to([3.88, 1.58, 0])

        overshoot_arrow = Arrow(
            start=[3.05, 1.54, 0],
            end=[2.68, 1.36, 0],
            color=DANGER_RED,
            stroke_width=2.0,
            tip_length=0.10
        )

        # Right Metrics Card
        card_right = RoundedRectangle(
            width=5.5,
            height=1.28,
            corner_radius=0.14,
            stroke_color=BORDER_DIM,
            stroke_width=1.4,
            fill_color=CARD_BG,
            fill_opacity=0.92
        ).move_to([right_cx, -0.92, 0])

        m_right_1 = Tex(r"$\bullet$ \ \textbf{Duration:} Pulse vanishes during cycle ($t_0 \lesssim \tau_n$); no steady state", font_size=15, color=TEXT_OFFWH)
        m_right_2 = Tex(r"$\bullet$ \ \textbf{Governing Metric:} Pulse Duration Ratio $t_0 / \tau_n \ \implies \text{Shock Spectrum}$", font_size=15, color=DANGER_RED)
        m_right_3 = Tex(r"$\bullet$ \ \textbf{Failure Mode:} Immediate peak dynamic stress, yield rupture, contact loss", font_size=15, color=TEXT_MUTED)
        metrics_right = VGroup(m_right_1, m_right_2, m_right_3).arrange(DOWN, aligned_edge=LEFT, buff=0.13).move_to(card_right.get_center())

        right_column_grp = VGroup(
            pill_right_grp, eq_right, axes_right, lbl_right_x,
            pulse_box, pulse_lbl, line_static, lbl_static, line_overshoot, lbl_overshoot,
            card_right, metrics_right
        )

        # ------------------------------------------------------------------
        # 4. Bottom Master Banner: The Static Analysis Dilemma
        # ------------------------------------------------------------------
        dilemma_box = RoundedRectangle(
            width=12.8,
            height=1.85,
            corner_radius=0.16,
            stroke_color=TEHRAN_BLUE,
            stroke_width=2.2,
            fill_color=CARD_BG,
            fill_opacity=0.96
        ).move_to([0, -2.82, 0])

        dilemma_tag = Tex(
            r"\textsc{\textbf{The Core Physical Dilemma: Why Classical Statics Fails}}",
            font_size=17,
            color=TEHRAN_BLUE
        ).move_to([0, -2.06, 0])

        dilemma_divider = Line(
            start=LEFT * 5.8,
            end=RIGHT * 5.8,
            color=BORDER_MID,
            stroke_width=1.0
        ).move_to([0, -2.26, 0])

        # Core Transformation Comparison Display
        f_static_title = Tex(r"\textsc{Naive Static Assumption}", font_size=14, color=TEXT_MUTED)
        f_static_math  = MathTex(r"x_{\text{static}} = \frac{F_0}{k}", font_size=25, color=FORCE_GOLD)
        f_static_grp   = VGroup(f_static_title, f_static_math).arrange(DOWN, buff=0.08)

        arrow_dyn = Arrow(
            start=LEFT * 1.4,
            end=RIGHT * 1.4,
            color=FORCE_GOLD,
            stroke_width=2.5,
            tip_length=0.15
        )
        arrow_lbl = Tex(r"\textbf{Dynamic Inertial Lag}", font_size=15, color=FORCE_GOLD).next_to(arrow_dyn, UP, buff=0.08)
        arrow_sub = Tex(r"($t_0 \lesssim \tau_n$, kinetic overshoot)", font_size=12, color=TEXT_MUTED).next_to(arrow_dyn, DOWN, buff=0.07)
        arrow_grp = VGroup(arrow_dyn, arrow_lbl, arrow_sub)

        f_dyn_title = Tex(r"\textsc{Transient Shock Reality}", font_size=14, color=DANGER_RED)
        f_dyn_math  = MathTex(r"x_{\max} = \textbf{DLF} \cdot \left(\frac{F_0}{k}\right), \quad \textbf{DLF} \le 2.0", font_size=25, color=DANGER_RED)
        f_dyn_grp   = VGroup(f_dyn_title, f_dyn_math).arrange(DOWN, buff=0.08)

        formula_row = VGroup(f_static_grp, arrow_grp, f_dyn_grp).arrange(RIGHT, buff=0.45).move_to([0, -2.76, 0])

        # Physical Strain Energy Consequence
        dilemma_consequence = VGroup(
            Tex(r"\textbf{Critical Consequence:} \ Peak Strain Energy", font_size=15, color=TEXT_OFFWH),
            MathTex(r"U_{\text{dyn}} = \tfrac{1}{2} k x_{\max}^2 = 4 \times U_{\text{static}}", font_size=16, color=DANGER_RED),
            Tex(r"$\implies$ \textbf{Statics underestimates shock deflection \& stress by up to 100\%!}", font_size=15, color=FORCE_GOLD)
        ).arrange(RIGHT, buff=0.14).move_to([0, -3.46, 0])

        dilemma_grp = VGroup(
            dilemma_box, dilemma_tag, dilemma_divider, formula_row, dilemma_consequence
        )

        # ------------------------------------------------------------------
        # 5. Animation Choreography & Timeline
        # ------------------------------------------------------------------
        # Step 1: Header Ingress (0.0s - 1.8s)
        self.play(
            FadeIn(header_tag, shift=DOWN * 0.20),
            Write(main_title),
            FadeIn(subtitle, shift=UP * 0.15),
            GrowFromCenter(header_rule),
            run_time=1.6
        )
        self.wait(0.2)

        # Step 2: Columns Setup (1.8s - 3.4s)
        self.play(
            GrowFromEdge(col_divider, UP),
            FadeIn(pill_left_grp, shift=DOWN * 0.2),
            FadeIn(eq_left, shift=DOWN * 0.15),
            Create(axes_left),
            Write(lbl_left_x),
            FadeIn(leg_harm_grp),
            FadeIn(pill_right_grp, shift=DOWN * 0.2),
            FadeIn(eq_right, shift=DOWN * 0.15),
            Create(axes_right),
            Write(lbl_right_x),
            run_time=1.6
        )

        # Step 3: Draw Shock Pulse & Static Reference Line on Right (3.4s - 4.4s)
        self.play(
            FadeIn(pulse_box),
            Write(pulse_lbl),
            Create(line_static),
            FadeIn(lbl_static),
            run_time=1.0
        )

        # Step 4: Synchronized Dual Waveform Creation (4.4s - 7.6s)
        self.play(
            Create(curve_harm_f, run_time=2.8),
            Create(curve_harm_x, run_time=3.0),
            Create(env_top, run_time=2.0),
            Create(env_bot, run_time=2.0),
            FadeIn(lbl_env, run_time=1.5),
            Create(curve_shock_x, run_time=3.2),
            rate_func=linear
        )

        # Step 5: Highlight Dynamic Overshoot & Reveal Metrics Cards (7.6s - 10.0s)
        self.play(
            Create(line_overshoot),
            FadeIn(lbl_overshoot),
            GrowFromCenter(peak_dot),
            GrowFromCenter(peak_ring),
            GrowArrow(overshoot_arrow),
            FadeIn(overshoot_callout, shift=UP * 0.1),
            FadeIn(card_left, shift=UP * 0.2),
            FadeIn(metrics_left, shift=UP * 0.2),
            FadeIn(card_right, shift=UP * 0.2),
            FadeIn(metrics_right, shift=UP * 0.2),
            run_time=2.2
        )

        # Subtle emphasis pulse on overshoot marker
        self.play(
            peak_ring.animate.scale(1.35).set_stroke(opacity=0.3),
            card_right.animate.set_stroke(color=DANGER_RED, width=2.4),
            run_time=0.6
        )
        self.play(
            peak_ring.animate.scale(1 / 1.35).set_stroke(opacity=1.0),
            card_right.animate.set_stroke(color=BORDER_DIM, width=1.4),
            run_time=0.6
        )

        # Step 6: The Static Dilemma Highlight (10.0s - 14.5s)
        self.play(
            FadeIn(dilemma_box, shift=UP * 0.25),
            FadeIn(dilemma_tag, shift=DOWN * 0.15),
            GrowFromCenter(dilemma_divider),
            run_time=1.2
        )

        self.play(
            FadeIn(f_static_grp, shift=RIGHT * 0.2),
            GrowArrow(arrow_dyn),
            FadeIn(arrow_lbl, shift=DOWN * 0.1),
            FadeIn(arrow_sub, shift=UP * 0.1),
            FadeIn(f_dyn_grp, shift=LEFT * 0.2),
            run_time=1.8
        )

        self.play(
            FadeIn(dilemma_consequence, shift=UP * 0.15),
            run_time=1.0
        )

        # Subtle golden border pulse on master dilemma box
        self.play(
            dilemma_box.animate.set_stroke(color=FORCE_GOLD, width=3.0),
            run_time=0.6
        )
        self.play(
            dilemma_box.animate.set_stroke(color=TEHRAN_BLUE, width=2.2),
            run_time=0.6
        )

        # Resting hold frame for Speaker 1 oral remarks
        self.wait(3.5)

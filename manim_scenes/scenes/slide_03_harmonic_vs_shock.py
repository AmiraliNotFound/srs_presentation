"""
SLIDE-03A: HarmonicVibrationScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Modeling)

Clean Presentation-Grade Slide (Zero Bulky Captions / Large Typography):
  - Step 0 (0.0s - 2.0s): Minimal centered header + Governing harmonic excitation formula.
  - Step 1 (2.0s - 6.5s): Expansive full-width graph + continuous sinusoidal waves + steady envelope.
  - Step 2 (6.5s - 11.5s): Three bold, punchy, unboxed presentation metrics.
"""

from manim import *
import numpy as np


class HarmonicVibrationScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black & UT Blue)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # University of Tehran Primary Accent
        FORCE_GOLD  = ManimColor("#F7CA3B")   # Harmonic Excitation & Accents
        DANGER_RED  = ManimColor("#FF644E")   # Fatigue / Failure Metric
        SPRING_CYAN = ManimColor("#58C4DD")   # Restoring Spring / Response Waveform
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        TEXT_DIM    = ManimColor("#64748B")
        BORDER_MID  = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Header & Title (Centered & Spacious)
        # ------------------------------------------------------------------
        header_tag = Tex(
            r"\textsc{Physical Foundations} \quad $\bullet$ \quad \textsc{Excitation Classification}",
            font_size=22,
            color=TEHRAN_BLUE
        ).move_to([0, 3.42, 0])

        main_title = Tex(
            r"\textbf{Steady-State Harmonic Vibration}",
            font_size=44,
            color=TEXT_WHITE
        ).next_to(header_tag, DOWN, buff=0.14)

        header_rule = Line(
            start=LEFT * 6.2,
            end=RIGHT * 6.2,
            color=TEHRAN_BLUE,
            stroke_width=1.6
        ).next_to(main_title, DOWN, buff=0.15)

        # ------------------------------------------------------------------
        # 3. Governing Excitation Formula Line (Large & Clean)
        # ------------------------------------------------------------------
        formula_math = MathTex(
            r"F(t) = F_0 \sin(\omega t), \quad t \in [0, \infty)",
            font_size=32,
            color=FORCE_GOLD
        ).move_to([0, 2.25, 0])

        # ------------------------------------------------------------------
        # 4. Full-Width Expansive 16:9 Waveform Graph
        # ------------------------------------------------------------------
        axes = Axes(
            x_range=[0, 4.0, 1],
            y_range=[-1.4, 1.4, 1],
            x_length=10.6,
            y_length=2.6,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.5,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            }
        ).move_to([0, 0.12, 0])

        lbl_time = Tex(r"Time $t \to \infty$", font_size=20, color=TEXT_MUTED).next_to(axes.c2p(4.0, 0), RIGHT, buff=0.14)

        # Continuous periodic waveforms
        t_vals = np.linspace(0, 4.0, 300)
        force_pts = [axes.c2p(t, 0.80 * np.sin(2 * np.pi * t)) for t in t_vals]
        disp_pts  = [axes.c2p(t, 1.15 * np.sin(2 * np.pi * t - 0.45)) for t in t_vals]

        curve_force = VMobject().set_points_smoothly(force_pts).set_color(FORCE_GOLD).set_stroke(width=2.4)
        curve_disp  = VMobject().set_points_smoothly(disp_pts).set_color(SPRING_CYAN).set_stroke(width=3.4)

        # Steady amplitude envelopes (+X and -X bounds)
        env_top = DashedLine(
            start=axes.c2p(0, 1.15),
            end=axes.c2p(4.0, 1.15),
            color=BORDER_MID,
            stroke_width=1.4,
            dash_length=0.12
        )
        env_bot = DashedLine(
            start=axes.c2p(0, -1.15),
            end=axes.c2p(4.0, -1.15),
            color=BORDER_MID,
            stroke_width=1.4,
            dash_length=0.12
        )
        lbl_env = Tex(r"$\pm X_{\text{steady}} = M \delta_{\text{st}}$", font_size=20, color=TEXT_MUTED).move_to([-2.6, 1.62, 0])

        # Large, Clean Wave Legend
        leg_disp = Line(ORIGIN, RIGHT * 0.50, color=SPRING_CYAN, stroke_width=3.4)
        leg_disp_lbl = Tex(r"$x(t)$ Response", font_size=20, color=SPRING_CYAN).next_to(leg_disp, RIGHT, buff=0.10)
        leg_force = Line(ORIGIN, RIGHT * 0.50, color=FORCE_GOLD, stroke_width=2.4)
        leg_force_lbl = Tex(r"$F(t)$ Force", font_size=20, color=FORCE_GOLD).next_to(leg_force, RIGHT, buff=0.10)
        leg_grp = VGroup(
            VGroup(leg_disp, leg_disp_lbl),
            VGroup(leg_force, leg_force_lbl)
        ).arrange(RIGHT, buff=0.45).move_to([2.6, 1.62, 0])

        # ------------------------------------------------------------------
        # 5. Bottom Stage: Bold, Punchy Presentation Metrics (No paragraph text)
        # ------------------------------------------------------------------
        row_y = -2.50

        # Column 1: Duration
        c1_title = Tex(r"\textsc{Indefinite Duration}", font_size=22, color=TEXT_OFFWH)
        c1_main  = MathTex(r"t \to \infty", font_size=34, color=FORCE_GOLD)
        col1 = VGroup(c1_title, c1_main).arrange(DOWN, buff=0.16).move_to([-4.40, row_y, 0])

        # Column 2: Governing Law
        c2_title = Tex(r"\textsc{Governing Parameter}", font_size=22, color=TEXT_OFFWH)
        c2_main  = MathTex(r"r = \frac{\omega}{\omega_n} \ \implies \ M(r, \zeta)", font_size=32, color=TEHRAN_BLUE)
        col2 = VGroup(c2_title, c2_main).arrange(DOWN, buff=0.16).move_to([0.0, row_y, 0])

        # Column 3: Design Metric
        c3_title = Tex(r"\textsc{Primary Failure Mode}", font_size=22, color=TEXT_OFFWH)
        c3_main  = Tex(r"\textbf{High-Cycle Fatigue}", font_size=28, color=DANGER_RED)
        col3 = VGroup(c3_title, c3_main).arrange(DOWN, buff=0.16).move_to([4.40, row_y, 0])

        # ------------------------------------------------------------------
        # 6. Step-Controlled Timeline with Exact Runtimes & Rest Holds
        # ------------------------------------------------------------------
        # --- Step 0: Initial Load (Total: 2.0s -> Cuepoint 0 = 2.0s) ---
        self.play(
            FadeIn(header_tag, shift=DOWN * 0.15),
            Write(main_title),
            GrowFromCenter(header_rule),
            run_time=0.8
        )
        self.play(
            FadeIn(formula_math, shift=UP * 0.15),
            run_time=0.6
        )
        self.wait(0.6)  # Stably resting at t = 2.0s

        # --- Step 1: Expansive Waveforms Reveal (Total: 4.5s -> Cuepoint 1 = 6.5s) ---
        self.play(
            Create(axes),
            Write(lbl_time),
            Create(env_top),
            Create(env_bot),
            FadeIn(lbl_env),
            FadeIn(leg_grp),
            run_time=0.8
        )
        self.play(
            Create(curve_force, run_time=2.2),
            Create(curve_disp, run_time=2.2),
            rate_func=linear
        )
        self.wait(1.5)  # Stably resting at t = 6.5s

        # --- Step 2: Bold Presentation Metrics Reveal (Total: 5.0s -> Cuepoint 2 = 11.5s) ---
        self.play(
            LaggedStart(
                FadeIn(col1, shift=UP * 0.25),
                FadeIn(col2, shift=UP * 0.25),
                FadeIn(col3, shift=UP * 0.25),
                lag_ratio=0.25
            ),
            run_time=1.2
        )
        self.play(
            c3_main.animate.scale(1.10),
            run_time=0.3
        )
        self.play(
            c3_main.animate.scale(1 / 1.10),
            run_time=0.3
        )
        self.wait(3.2)  # Stable resting hold until t = 11.5s

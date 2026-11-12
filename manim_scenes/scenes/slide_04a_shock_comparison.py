"""
SLIDE-04A: ShockComparisonScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Foundations & Modeling)

3Blue1Brown Visual-First Comparison:
  - 90% open dark canvas.
  - Zero prose text or bloated headers.
  - Step 0 (0.0s - 1.8s): Clean modest title "Two Extremes of Mechanical Shock" + empty axes.
  - Step 1 (1.8s - 5.5s): Left curve (Drop Impact) smooth half-sine + [Delta t ~ 50 ms, a_max ~ 50g].
  - Step 2 (5.5s - 9.5s): Right curve (Pyroshock) high-frequency ringing + [Delta t < 1 ms, a_max ~ 5000g].
"""

from manim import *
import numpy as np


class ShockComparisonScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black Canvas)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SPRING_CYAN = ManimColor("#58C4DD")   # Drop Impact Waveform
        DANGER_RED  = ManimColor("#FF644E")   # Pyroshock Waveform
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        TEXT_DIM    = ManimColor("#64748B")
        BORDER_MID  = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Modest Floating Title (No pills, no subtitle, no divider lines)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Two Extremes of Mechanical Shock}",
            font_size=36,
            color=TEXT_WHITE
        ).move_to([0, 3.25, 0])

        # ------------------------------------------------------------------
        # 3. Two Centered Large Plots (Left & Right with Generous Breathing Room)
        # ------------------------------------------------------------------
        col_x = 3.65

        # === LEFT PLOT: DROP IMPACT ===
        lbl_left = Tex(
            r"\textbf{Drop Impact}",
            font_size=28,
            color=SPRING_CYAN
        ).move_to([-col_x, 1.80, 0])

        ax_left = Axes(
            x_range=[0, 1.4, 0.5],
            y_range=[0, 1.3, 0.5],
            x_length=4.6,
            y_length=2.4,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([-col_x, 0.15, 0])

        lbl_t_left = Tex(r"Time $t$", font_size=17, color=TEXT_MUTED).next_to(ax_left.c2p(1.4, 0), RIGHT, buff=0.10)
        lbl_a_left = Tex(r"$a(t)$", font_size=17, color=TEXT_MUTED).next_to(ax_left.c2p(0, 1.3), UP, buff=0.08)

        # Half-sine waveform: a(t) = sin(pi * t) for 0 <= t <= 1.0, 0 for 1.0 <= t <= 1.3
        t_vals_drop = np.linspace(0, 1.0, 120)
        pts_drop = [ax_left.c2p(t, 1.05 * np.sin(np.pi * t)) for t in t_vals_drop]
        pts_drop_flat = [ax_left.c2p(t, 0.0) for t in np.linspace(1.0, 1.3, 30)]
        curve_drop = VMobject().set_points_smoothly(pts_drop + pts_drop_flat).set_color(SPRING_CYAN).set_stroke(width=3.6)

        # Subtle translucent pulse fill
        area_pts = [ax_left.c2p(0, 0)] + pts_drop + [ax_left.c2p(1.0, 0)]
        area_drop = Polygon(*area_pts, color=SPRING_CYAN, stroke_width=0, fill_color=SPRING_CYAN, fill_opacity=0.15)

        # Only two clean labels
        lbl_drop_metrics = MathTex(
            r"\Delta t \approx 50\text{ ms}, \quad a_{\max} \approx 50g",
            font_size=26,
            color=SPRING_CYAN
        ).next_to(ax_left, DOWN, buff=0.45)

        # === RIGHT PLOT: PYROSHOCK ===
        lbl_right = Tex(
            r"\textbf{Pyroshock}",
            font_size=28,
            color=DANGER_RED
        ).move_to([col_x, 1.80, 0])

        ax_right = Axes(
            x_range=[0, 1.4, 0.5],
            y_range=[-1.2, 1.2, 0.5],
            x_length=4.6,
            y_length=2.4,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([col_x, 0.15, 0])

        lbl_t_right = Tex(r"Time $t$", font_size=17, color=TEXT_MUTED).next_to(ax_right.c2p(1.4, 0), RIGHT, buff=0.10)
        lbl_a_right = Tex(r"$a(t)$", font_size=17, color=TEXT_MUTED).next_to(ax_right.c2p(0, 1.2), UP, buff=0.08)

        # High-frequency damped ringing: a(t) = 1.05 * exp(-3.8*t) * sin(2*pi*8*t)
        t_vals_pyro = np.linspace(0, 1.3, 350)
        pts_pyro = [
            ax_right.c2p(t, 1.05 * np.exp(-3.8 * t) * np.sin(2 * np.pi * 8.0 * t))
            for t in t_vals_pyro
        ]
        curve_pyro = VMobject().set_points_smoothly(pts_pyro).set_color(DANGER_RED).set_stroke(width=2.4)

        # Subtle decaying envelope guides
        env_pos = [ax_right.c2p(t, 1.05 * np.exp(-3.8 * t)) for t in t_vals_pyro]
        env_neg = [ax_right.c2p(t, -1.05 * np.exp(-3.8 * t)) for t in t_vals_pyro]
        curve_env_pos = VMobject().set_points_smoothly(env_pos).set_color(BORDER_MID).set_stroke(width=1.2)
        curve_env_neg = VMobject().set_points_smoothly(env_neg).set_color(BORDER_MID).set_stroke(width=1.2)

        # Only two clean labels
        lbl_pyro_metrics = MathTex(
            r"\Delta t < 1\text{ ms}, \quad a_{\max} \approx 5{,}000g",
            font_size=26,
            color=DANGER_RED
        ).next_to(ax_right, DOWN, buff=0.45)

        # ------------------------------------------------------------------
        # 4. Step-Controlled Timeline & Cuepoint Choreography
        # ------------------------------------------------------------------
        # --- Step 0: Minimal Load (0.0s - 1.8s -> Cuepoint 0 = 1.8s) ---
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            run_time=0.6
        )
        self.play(
            FadeIn(lbl_left),
            Create(ax_left),
            Write(lbl_t_left),
            Write(lbl_a_left),
            FadeIn(lbl_right),
            Create(ax_right),
            Write(lbl_t_right),
            Write(lbl_a_right),
            run_time=0.7
        )
        self.wait(0.5)  # Rest hold at t = 1.8s

        # --- Step 1: Drop Impact Reveal (1.8s - 5.5s -> Cuepoint 1 = 5.5s) ---
        self.play(
            Create(curve_drop),
            FadeIn(area_drop),
            run_time=1.8,
            rate_func=linear
        )
        self.play(
            FadeIn(lbl_drop_metrics, shift=UP * 0.15),
            run_time=0.6
        )
        self.wait(1.3)  # Rest hold at t = 5.5s

        # --- Step 2: Pyroshock Reveal (5.5s - 9.5s -> Cuepoint 2 = 9.5s) ---
        self.play(
            Create(curve_env_pos),
            Create(curve_env_neg),
            Create(curve_pyro),
            run_time=1.8,
            rate_func=linear
        )
        self.play(
            FadeIn(lbl_pyro_metrics, shift=UP * 0.15),
            run_time=0.6
        )
        self.wait(1.6)  # Rest hold at t = 9.5s

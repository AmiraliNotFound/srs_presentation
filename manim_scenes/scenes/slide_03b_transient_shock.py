"""
SLIDE-03B: TransientShockScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Modeling)

Clean Presentation-Grade Slide (Zero Bulky Captions / Large Typography):
  - Step 0 (0.0s - 2.0s): Minimal centered header + Governing transient excitation condition.
  - Step 1 (2.0s - 7.0s): Expansive full-width graph + pulse F_0 + response surging to +100% overshoot.
  - Step 2 (7.0s - 12.0s): Three bold, punchy, unboxed presentation metrics.
"""

from manim import *
import numpy as np


class TransientShockScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black & UT Blue)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # University of Tehran Primary Accent
        FORCE_GOLD  = ManimColor("#F7CA3B")   # Static Baseline & Accents
        DANGER_RED  = ManimColor("#FF644E")   # Shock Pulse, Dynamic Overshoot & Failure Alert
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
            r"\textbf{Transient Dynamic Shock Pulse}",
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
            r"F(t) \ne 0 \text{ only for } 0 \le t \le t_0 \quad (t_0 \lesssim \tau_n)",
            font_size=32,
            color=DANGER_RED
        ).move_to([0, 2.25, 0])

        # ------------------------------------------------------------------
        # 4. Full-Width Expansive 16:9 Waveform Graph
        # ------------------------------------------------------------------
        axes = Axes(
            x_range=[0, 3.5, 1],
            y_range=[-2.2, 2.5, 1],
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

        lbl_time = Tex(r"Time $t$", font_size=20, color=TEXT_MUTED).next_to(axes.c2p(3.5, 0), RIGHT, buff=0.14)

        # Rectangular Pulse Graphic (0 <= t <= 1.0, height = 1.0 delta_st)
        pulse_pts = [
            axes.c2p(0.0, 0.0),
            axes.c2p(0.0, 1.0),
            axes.c2p(1.0, 1.0),
            axes.c2p(1.0, 0.0)
        ]
        pulse_box = Polygon(*pulse_pts, color=DANGER_RED, stroke_width=2.0, fill_color=DANGER_RED, fill_opacity=0.22)
        
        # Clean Shock Pulse label placed under the pulse duration (zero overlap with curve)
        pulse_lbl = Tex(r"\textbf{Shock Pulse } $F_0$", font_size=19, color=DANGER_RED)
        pulse_sub = Tex(r"Duration $t_0$", font_size=16, color=TEXT_MUTED)
        pulse_annot = VGroup(pulse_lbl, pulse_sub).arrange(DOWN, buff=0.06).next_to(axes.c2p(0.5, 0), DOWN, buff=0.18)

        # Static Deflection Reference Line (delta_st = F0 / k = 1.0)
        line_static = DashedLine(
            start=axes.c2p(0, 1.0),
            end=axes.c2p(3.5, 1.0),
            color=FORCE_GOLD,
            stroke_width=1.6,
            dash_length=0.10
        )
        lbl_static = Tex(
            r"$\delta_{\text{st}} = \frac{F_0}{k} \text{ (Static Baseline)}$",
            font_size=20,
            color=FORCE_GOLD
        ).next_to(axes.c2p(3.5, 1.0), LEFT, buff=0.15).shift(DOWN * 0.22)

        # Dynamic Overshoot Peak Reference Line (x_max = 2.0 delta_st)
        line_overshoot = DashedLine(
            start=axes.c2p(0, 2.0),
            end=axes.c2p(3.5, 2.0),
            color=DANGER_RED,
            stroke_width=2.0,
            dash_length=0.10
        )
        lbl_overshoot = Tex(
            r"$x_{\max} = 2.0\,\delta_{\text{st}} \quad (\textbf{DLF} = 2.0)$",
            font_size=22,
            color=DANGER_RED
        ).next_to(axes.c2p(3.5, 2.0), LEFT, buff=0.15).shift(UP * 0.22)

        # Exact Dynamic SDOF Shock Response
        t_shock = np.linspace(0, 3.5, 300)
        shock_pts = []
        for t in t_shock:
            if t <= 1.0:
                x_val = 1.0 - np.cos(np.pi * t)
            else:
                x_val = 2.0 * np.cos(np.pi * (t - 1.0)) * np.exp(-0.045 * np.pi * (t - 1.0))
            shock_pts.append(axes.c2p(t, x_val))

        curve_shock_x = VMobject().set_points_smoothly(shock_pts).set_color(SPRING_CYAN).set_stroke(width=3.6)

        # Overshoot Peak Indicator Dot & Prominent Callout
        peak_coord = axes.c2p(1.0, 2.0)
        peak_dot = Dot(point=peak_coord, radius=0.10, color=DANGER_RED)
        peak_ring = Arc(radius=0.22, start_angle=0, angle=TAU, stroke_color=DANGER_RED, stroke_width=2.5).move_to(peak_coord)

        overshoot_callout = Tex(
            r"\textbf{+100\% Dynamic Overshoot!}",
            font_size=24,
            color=DANGER_RED
        ).move_to([peak_coord[0] + 1.95, peak_coord[1] + 0.38, 0])

        overshoot_arrow = Arrow(
            start=overshoot_callout.get_left() + LEFT * 0.08,
            end=peak_coord + UP * 0.12 + RIGHT * 0.12,
            color=DANGER_RED,
            stroke_width=2.4,
            tip_length=0.14
        )

        # ------------------------------------------------------------------
        # 5. Bottom Stage: Bold, Punchy Presentation Metrics (No paragraph text)
        # ------------------------------------------------------------------
        row_y = -2.50

        # Column 1: Duration
        c1_title = Tex(r"\textsc{Transient Disturbance}", font_size=22, color=TEXT_OFFWH)
        c1_main  = MathTex(r"t_0 \lesssim \tau_n", font_size=34, color=DANGER_RED)
        col1 = VGroup(c1_title, c1_main).arrange(DOWN, buff=0.16).move_to([-4.40, row_y, 0])

        # Column 2: Governing Law
        c2_title = Tex(r"\textsc{Governing Parameter}", font_size=22, color=TEXT_OFFWH)
        c2_main  = MathTex(r"\frac{t_0}{\tau_n} \ \implies \ \text{SRS}", font_size=32, color=TEHRAN_BLUE)
        col2 = VGroup(c2_title, c2_main).arrange(DOWN, buff=0.16).move_to([0.0, row_y, 0])

        # Column 3: Design Metric
        c3_title = Tex(r"\textsc{Primary Failure Mode}", font_size=22, color=TEXT_OFFWH)
        c3_main  = Tex(r"\textbf{Peak Stress Rupture}", font_size=28, color=DANGER_RED)
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

        # --- Step 1: Expansive Shock Waveform & Overshoot (Total: 5.0s -> Cuepoint 1 = 7.0s) ---
        self.play(
            Create(axes),
            Write(lbl_time),
            FadeIn(pulse_box),
            FadeIn(pulse_annot),
            Create(line_static),
            FadeIn(lbl_static),
            run_time=0.8
        )
        self.play(
            Create(curve_shock_x, run_time=2.0),
            rate_func=linear
        )
        self.play(
            Create(line_overshoot),
            FadeIn(lbl_overshoot),
            GrowFromCenter(peak_dot),
            GrowFromCenter(peak_ring),
            GrowArrow(overshoot_arrow),
            FadeIn(overshoot_callout, shift=UP * 0.1),
            run_time=0.7
        )
        self.wait(1.5)  # Stably resting at t = 7.0s

        # --- Step 2: Bold Presentation Metrics Reveal (Total: 5.0s -> Cuepoint 2 = 12.0s) ---
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
        self.wait(3.2)  # Stable resting hold until t = 12.0s

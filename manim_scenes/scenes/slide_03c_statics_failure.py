"""
SLIDE-03C: StaticsFailureScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Modeling)

Clean Presentation-Grade Slide (Zero Bulky Captions / Large Typography):
  - Step 0 (0.0s - 2.0s): Minimal header + Naive static assumption (x_static = F_0 / k).
  - Step 1 (2.0s - 6.0s): Perfectly centered equidistant Dynamic Inertial Lag arrow -> Transient reality (DLF <= 2.0).
  - Step 2 (6.0s - 11.0s): Large, bold takeaway: U_dyn = 4 * U_static => Quadrupled stored energy!
"""

from manim import *
import numpy as np


class StaticsFailureScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black & UT Blue)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # University of Tehran Primary Accent
        FORCE_GOLD  = ManimColor("#F7CA3B")   # Static Formula & Transition Accents
        DANGER_RED  = ManimColor("#FF644E")   # Shock Overshoot, Strain Energy & Alert
        SPRING_CYAN = ManimColor("#58C4DD")   # Restoring Term
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        TEXT_DIM    = ManimColor("#64748B")
        BORDER_MID  = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Header & Title (Floating at top, spacious & minimal)
        # ------------------------------------------------------------------
        header_tag = Tex(
            r"\textsc{Physical Foundations} \quad $\bullet$ \quad \textsc{The Static Analysis Dilemma}",
            font_size=22,
            color=TEHRAN_BLUE
        ).move_to([0, 3.42, 0])

        main_title = Tex(
            r"\textbf{Why Classical Statics Fails}",
            font_size=46,
            color=TEXT_WHITE
        ).next_to(header_tag, DOWN, buff=0.14)

        header_rule = Line(
            start=LEFT * 6.0,
            end=RIGHT * 6.0,
            color=TEHRAN_BLUE,
            stroke_width=1.6
        ).next_to(main_title, DOWN, buff=0.15)

        # ------------------------------------------------------------------
        # 3. Center Stage: The Dynamic Transformation (Perfect Equidistant Spacing)
        # ------------------------------------------------------------------
        center_y = 0.70

        # --- Left: Naive Static Assumption ---
        f_static_title = Tex(
            r"\textsc{Static Sizing}",
            font_size=24,
            color=TEXT_MUTED
        )
        f_static_math = MathTex(
            r"x_{\text{static}} = \frac{F_0}{k}",
            font_size=46,
            color=FORCE_GOLD
        )
        f_static_grp = VGroup(f_static_title, f_static_math).arrange(DOWN, buff=0.22).move_to([-4.40, center_y, 0])

        # --- Right: Transient Dynamic Reality ---
        f_dyn_title = Tex(
            r"\textsc{Dynamic Shock Reality}",
            font_size=24,
            color=DANGER_RED
        )
        f_dyn_math = MathTex(
            r"x_{\max} = \textbf{DLF} \cdot \left(\frac{F_0}{k}\right), \quad \textbf{DLF} \le 2.0",
            font_size=38,
            color=DANGER_RED
        )
        f_dyn_grp = VGroup(f_dyn_title, f_dyn_math).arrange(DOWN, buff=0.22).move_to([3.40, center_y, 0])

        # --- Center: Perfectly Centered Transition Arrow (Equidistant from both formulas) ---
        # Right edge of static math is at approx -3.25; Left edge of dynamic math is at approx 0.85.
        # Center of gap = (-3.25 + 0.85)/2 = -1.20. Arrow span = [-2.20, -0.20].
        # Distance to static = 1.05; Distance to dynamic = 1.05! Perfectly balanced!
        arrow_dyn = Arrow(
            start=[-2.20, center_y - 0.10, 0],
            end=[-0.20, center_y - 0.10, 0],
            color=FORCE_GOLD,
            stroke_width=3.6,
            tip_length=0.20
        )
        arrow_lbl = Tex(
            r"\textbf{Dynamic Inertial Lag}",
            font_size=22,
            color=FORCE_GOLD
        ).next_to(arrow_dyn, UP, buff=0.16)
        arrow_grp = VGroup(arrow_dyn, arrow_lbl)

        # ------------------------------------------------------------------
        # 4. Bottom Stage: Master Takeaway (Large, Presentation-Grade, Zero Bulky Text)
        # ------------------------------------------------------------------
        takeaway_math = MathTex(
            r"U_{\text{dyn}} = \tfrac{1}{2} k (2\delta_{\text{st}})^2 = 4 \times U_{\text{static}}",
            font_size=36,
            color=DANGER_RED
        )
        takeaway_arrow = Tex(
            r"$\implies$",
            font_size=34,
            color=TEXT_WHITE
        )
        takeaway_txt = Tex(
            r"\textbf{Doubling Deflection Quadruples Stored Energy!}",
            font_size=28,
            color=FORCE_GOLD
        )
        takeaway_row = VGroup(takeaway_math, takeaway_arrow, takeaway_txt).arrange(RIGHT, buff=0.30).move_to([0, -1.65, 0])

        takeaway_warn = Tex(
            r"\textbf{Classical Static Sizing Guarantees Catastrophic Shock Rupture!}",
            font_size=26,
            color=DANGER_RED
        ).next_to(takeaway_row, DOWN, buff=0.35)

        takeaway_grp = VGroup(takeaway_row, takeaway_warn)

        # ------------------------------------------------------------------
        # 5. Step-Controlled Timeline with Exact Runtimes & Rest Holds
        # ------------------------------------------------------------------
        # --- Step 0: Initial Load (Total: 2.0s -> Cuepoint 0 = 2.0s) ---
        self.play(
            FadeIn(header_tag, shift=DOWN * 0.15),
            Write(main_title),
            GrowFromCenter(header_rule),
            run_time=0.8
        )
        self.play(
            FadeIn(f_static_grp, shift=UP * 0.15),
            run_time=0.6
        )
        self.wait(0.6)  # Stably resting at t = 2.0s

        # --- Step 1: Centered Inertial Lag Arrow & Dynamic Reality (Total: 4.0s -> Cuepoint 1 = 6.0s) ---
        self.play(
            GrowArrow(arrow_dyn),
            FadeIn(arrow_lbl, shift=UP * 0.1),
            FadeIn(f_dyn_grp, shift=UP * 0.15),
            run_time=1.4
        )
        self.play(
            f_dyn_math[0][17:23].animate.scale(1.15),
            run_time=0.4
        )
        self.play(
            f_dyn_math[0][17:23].animate.scale(1 / 1.15),
            run_time=0.4
        )
        self.wait(1.8)  # Stably resting at t = 6.0s

        # --- Step 2: Bold Energy Takeaway (Total: 5.0s -> Cuepoint 2 = 11.0s) ---
        self.play(
            FadeIn(takeaway_row, shift=UP * 0.2),
            run_time=1.0
        )
        self.play(
            FadeIn(takeaway_warn, shift=UP * 0.15),
            run_time=0.8
        )
        self.wait(3.2)  # Stable resting hold until t = 11.0s

"""
SLIDE-03B: StaticsFailureScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Modeling)

Step-Controlled Mathematical Insight:
  - Step 0 (0.0s - 1.4s): Minimal header + Naive static assumption (x_static = F_0 / k).
  - Step 1 (1.4s - 4.2s): Dynamic Inertial Lag transition arrow -> Transient reality (x_max = DLF * (F_0/k), DLF <= 2.0).
  - Step 2 (4.2s - 11.0s): Unboxed key takeaway: U_dyn = 4 * U_static => Up to 100% deflection overshoot!
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
            font_size=21,
            color=TEHRAN_BLUE
        ).move_to([0, 3.32, 0])

        main_title = Tex(
            r"\textbf{Why Classical Statics Fails}",
            font_size=44,
            color=TEXT_WHITE
        ).next_to(header_tag, DOWN, buff=0.15)

        header_rule = Line(
            start=LEFT * 5.8,
            end=RIGHT * 5.8,
            color=TEHRAN_BLUE,
            stroke_width=1.6
        ).next_to(main_title, DOWN, buff=0.18)

        # ------------------------------------------------------------------
        # 3. Center Stage: The Dynamic Transformation
        # ------------------------------------------------------------------
        center_y = 0.55

        # --- Left: Naive Static Assumption ---
        f_static_title = Tex(
            r"\textsc{Naive Static Assumption}",
            font_size=22,
            color=TEXT_MUTED
        )
        f_static_math = MathTex(
            r"x_{\text{static}} = \frac{F_0}{k}",
            font_size=40,
            color=FORCE_GOLD
        )
        f_static_sub = Tex(
            r"Assumes instantaneous equilibrium",
            font_size=16,
            color=TEXT_DIM
        )
        f_static_grp = VGroup(f_static_title, f_static_math, f_static_sub).arrange(DOWN, buff=0.16).move_to([-4.15, center_y, 0])

        # --- Center: Transition Arrow with Inertial Lag ---
        arrow_dyn = Arrow(
            start=[-1.35, center_y, 0],
            end=[1.35, center_y, 0],
            color=FORCE_GOLD,
            stroke_width=3.2,
            tip_length=0.18
        )
        arrow_lbl = Tex(
            r"\textbf{Dynamic Inertial Lag}",
            font_size=20,
            color=FORCE_GOLD
        ).next_to(arrow_dyn, UP, buff=0.12)
        arrow_sub = Tex(
            r"$t_0 \lesssim \tau_n$ \ (Mass cannot accelerate instantly)",
            font_size=15,
            color=TEXT_MUTED
        ).next_to(arrow_dyn, DOWN, buff=0.12)
        arrow_grp = VGroup(arrow_dyn, arrow_lbl, arrow_sub)

        # --- Right: Transient Dynamic Reality ---
        f_dyn_title = Tex(
            r"\textsc{Transient Dynamic Reality}",
            font_size=22,
            color=DANGER_RED
        )
        f_dyn_math = MathTex(
            r"x_{\max} = \textbf{DLF} \cdot \left(\frac{F_0}{k}\right), \quad \textbf{DLF} \le 2.0",
            font_size=34,
            color=DANGER_RED
        )
        f_dyn_sub = Tex(
            r"Dynamic kinetic energy drives $+100\%$ overshoot",
            font_size=16,
            color=TEXT_MUTED
        )
        f_dyn_grp = VGroup(f_dyn_title, f_dyn_math, f_dyn_sub).arrange(DOWN, buff=0.16).move_to([4.15, center_y, 0])

        # ------------------------------------------------------------------
        # 4. Bottom Stage: Master Takeaway (Unboxed, large, clean typography)
        # ------------------------------------------------------------------
        takeaway_math = MathTex(
            r"U_{\text{dyn}} = \tfrac{1}{2} k x_{\max}^2 = 4 \times U_{\text{static}}",
            font_size=28,
            color=DANGER_RED
        )
        takeaway_arrow = Tex(
            r"$\implies$",
            font_size=28,
            color=TEXT_WHITE
        )
        takeaway_txt = Tex(
            r"\textbf{Up to 100\% Deflection \& Stress Overshoot!}",
            font_size=26,
            color=FORCE_GOLD
        )
        takeaway_row = VGroup(takeaway_math, takeaway_arrow, takeaway_txt).arrange(RIGHT, buff=0.25).move_to([0, -1.75, 0])

        takeaway_sub = Tex(
            r"Because strain energy scales quadratically ($U = \frac{1}{2} k x^2$), doubling deflection quadruples stored internal energy.",
            font_size=18,
            color=TEXT_OFFWH
        ).next_to(takeaway_row, DOWN, buff=0.28)

        takeaway_warn = Tex(
            r"\textbf{Result: Classical static sizing guarantees catastrophic yield or rupture under shock!}",
            font_size=19,
            color=DANGER_RED
        ).next_to(takeaway_sub, DOWN, buff=0.24)

        takeaway_grp = VGroup(takeaway_row, takeaway_sub, takeaway_warn)

        # ------------------------------------------------------------------
        # 5. Step-Controlled Timeline & Cuepoint Milestones
        # ------------------------------------------------------------------
        # --- Step 0: Initial Load (0.0s - 1.4s) ---
        self.play(
            FadeIn(header_tag, shift=DOWN * 0.20),
            Write(main_title),
            GrowFromCenter(header_rule),
            run_time=1.2
        )
        self.play(
            FadeIn(f_static_grp, shift=RIGHT * 0.25),
            run_time=0.8
        )
        self.wait(0.2)  # Pause point: Step 0 completes at 1.4s

        # --- Step 1: Transition Arrow & Transient Reality (1.4s - 4.2s) ---
        self.play(
            GrowArrow(arrow_dyn),
            FadeIn(arrow_lbl, shift=DOWN * 0.1),
            FadeIn(arrow_sub, shift=UP * 0.1),
            run_time=1.2
        )
        self.play(
            FadeIn(f_dyn_grp, shift=LEFT * 0.25),
            run_time=1.0
        )
        # Emphasis pulse on DLF term
        self.play(
            f_dyn_math.animate.scale(1.08),
            run_time=0.4
        )
        self.play(
            f_dyn_math.animate.scale(1 / 1.08),
            run_time=0.4
        )
        self.wait(0.2)  # Pause point: Step 1 completes at 4.2s

        # --- Step 2: Key Takeaway & Quadratic Energy Scaling (4.2s - 11.0s) ---
        self.play(
            FadeIn(takeaway_row, shift=UP * 0.25),
            run_time=1.2
        )
        self.play(
            FadeIn(takeaway_sub, shift=UP * 0.15),
            FadeIn(takeaway_warn, shift=UP * 0.15),
            run_time=1.2
        )
        # Subtle pulse on warning
        self.play(
            takeaway_warn.animate.scale(1.05),
            run_time=0.4
        )
        self.play(
            takeaway_warn.animate.scale(1 / 1.05),
            run_time=0.4
        )
        # Resting hold frame for speaker commentary
        self.wait(3.5)

"""
SLIDE-20A: WindBlastSRSScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 60 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars
  - High breathing room, large presentation math typography
  - Fullscreen canonical Half-Sine Shock Response Spectrum DLF vs beta
  - Primary era curve (Cyan), Residual era curve (Slate dashed), Static reference (DLF = 1.0)
  - Municipal tower operating point: beta = 0.9031 => DLF = 1.7587 (+75.9% overshoot)
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine, there_and_back
import numpy as np


class WindBlastSRSScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SLATE       = ManimColor("#B0B8C4")
        CYAN        = ManimColor("#58C4DD")
        AMBER       = ManimColor("#FFB703")
        RED_SHOCK   = ManimColor("#FF644E")
        UT_BLUE     = ManimColor("#0097F1")
        TEXT_WHITE  = ManimColor("#FFFFFF")
        WALL_STROKE = ManimColor("#3B4D63")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Wind-Blast Shock Spectrum (SRS)}",
            font_size=42,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # ------------------------------------------------------------------
        # 3. Canonical Fullscreen SRS Coordinate System (Shifted Left)
        # ------------------------------------------------------------------
        axes_srs = Axes(
            x_range=[0, 2.40, 0.40],
            y_range=[0, 2.20, 0.50],
            x_length=5.80,
            y_length=4.20,
            axis_config={
                "color": SLATE,
                "stroke_width": 2.2,
                "include_ticks": True,
                "tick_size": 0.08,
            }
        ).move_to([-2.60, -0.40, 0])

        # Axis Labels
        x_lbl = MathTex(
            r"\beta = \frac{t_0}{\tau_n}",
            font_size=23, color=SLATE
        ).next_to(axes_srs.x_axis, RIGHT, buff=0.15)

        y_lbl = MathTex(
            r"\mathbf{DLF} = \frac{x_{\max}}{\delta_{\text{st}}}",
            font_size=23, color=SLATE
        ).next_to(axes_srs.y_axis, UP, buff=0.12)

        # Static Reference Line (DLF = 1.0)
        p_stat_start = axes_srs.c2p(0, 1.0)
        p_stat_end = axes_srs.c2p(2.40, 1.0)
        static_line = DashedLine(
            p_stat_start, p_stat_end,
            dash_length=0.10, dashed_ratio=0.5,
            color=ManimColor("#4A5568"), stroke_width=1.8
        )
        static_lbl = Tex(
            r"Static Limit $(\text{DLF} = 1.0)$",
            font_size=15, color=ManimColor("#718096")
        ).move_to(axes_srs.c2p(1.70, 0.88))

        # ------------------------------------------------------------------
        # 4. Exact Canonical Closed-Form Half-Sine SRS Curves (Rao / Harris)
        # ------------------------------------------------------------------
        def dlf_governing(b):
            if b <= 0.001:
                return 0.0
            if b <= 0.50:
                # Residual era governs for beta <= 0.5 (impulsive regime)
                denom = abs(1.0 - 4.0 * b**2)
                if denom < 0.008:
                    return np.pi / 2.0
                return float((4.0 * b / denom) * abs(np.cos(np.pi * b)))
            else:
                # Primary era governs for beta > 0.5 (dynamic amplification)
                denom = abs(2.0 * b - 1.0)
                if denom < 0.008:
                    return np.pi / 2.0
                return float((2.0 * b / denom) * abs(np.sin(2.0 * np.pi / (2.0 * b + 1.0))))

        def dlf_residual(b):
            if b <= 0.001:
                return 0.0
            denom = abs(1.0 - 4.0 * b**2)
            if denom < 0.008:
                return np.pi / 2.0
            return float((4.0 * b / denom) * abs(np.cos(np.pi * b)))

        # Plot curves
        curve_primary = axes_srs.plot(
            dlf_governing,
            x_range=[0.02, 2.38],
            color=CYAN,
            stroke_width=3.6
        )

        curve_residual = axes_srs.plot(
            dlf_residual,
            x_range=[0.52, 2.38],
            color=SLATE,
            stroke_width=1.8
        )
        curve_residual.set_stroke(opacity=0.55)

        # Legend / Curve Labels
        lbl_pri = Tex(r"Maximax Spectrum ($\mathbf{DLF}$)", font_size=16, color=CYAN).move_to(axes_srs.c2p(2.00, 1.55))
        lbl_res = Tex(r"Residual Era ($t > t_0$)", font_size=15, color=SLATE).move_to(axes_srs.c2p(1.70, 0.35))

        # ------------------------------------------------------------------
        # 5. Tower Operating Point: beta = 0.9031 => DLF = 1.7587
        # ------------------------------------------------------------------
        beta_oper = 0.9031
        dlf_oper = 1.7587

        pt_oper = axes_srs.c2p(beta_oper, dlf_oper)
        pt_x_axis = axes_srs.c2p(beta_oper, 0)
        pt_y_axis = axes_srs.c2p(0, dlf_oper)

        # Guide lines
        guide_v = DashedLine(pt_x_axis, pt_oper, dash_length=0.08, dashed_ratio=0.5, color=AMBER, stroke_width=2.0)
        guide_h = DashedLine(pt_y_axis, pt_oper, dash_length=0.08, dashed_ratio=0.5, color=AMBER, stroke_width=2.0)

        # Markers on axes
        oper_x_lbl = MathTex(r"\beta = \mathbf{0.903}", font_size=20, color=AMBER).next_to(pt_x_axis, DOWN, buff=0.14)
        oper_y_lbl = MathTex(r"\mathbf{DLF} = \mathbf{1.76}", font_size=20, color=AMBER).next_to(pt_y_axis, LEFT, buff=0.14)

        # Operating Point Dot & Glow
        dot_oper = Dot(point=pt_oper, radius=0.10, color=RED_SHOCK)
        glow_oper = Dot(point=pt_oper, radius=0.22, color=AMBER, fill_opacity=0.35)
        oper_marker = VGroup(glow_oper, dot_oper)

        # ------------------------------------------------------------------
        # 6. Spacious Callout Card (Floating on Right, Center x = 4.25)
        # ------------------------------------------------------------------
        x_c = 4.25
        callout_box = RoundedRectangle(
            corner_radius=0.18, width=4.80, height=4.80,
            color=CARD_STROKE, stroke_width=2.0,
            fill_color=BG_DARK, fill_opacity=0.94
        ).move_to([x_c, -0.25, 0])

        callout_line1 = MathTex(
            r"\mathbf{DLF} = \mathbf{1.7587}",
            font_size=36, color=AMBER
        ).move_to([x_c, 1.45, 0])

        callout_line2 = Tex(
            r"$+75.9\%$ Dynamic Overshoot",
            font_size=23, color=RED_SHOCK
        ).move_to([x_c, 0.85, 0])

        callout_sep = Line([x_c - 2.00, 0.45, 0], [x_c + 2.00, 0.45, 0], color=CARD_STROKE, stroke_width=1.4)

        callout_line3 = Tex(
            r"Primary Pulse Era Governs ($t_m = 1.14\text{ s} \le t_0$)",
            font_size=18, color=SLATE
        ).move_to([x_c, 0.05, 0])

        callout_line4 = MathTex(
            r"x_{\max} = \mathbf{DLF} \cdot \delta_{\text{st}} = \mathbf{80.76\text{ mm}}",
            font_size=23, color=CYAN
        ).move_to([x_c, -0.65, 0])

        callout_badge = RoundedRectangle(
            corner_radius=0.12, width=4.30, height=0.55,
            color=RED_SHOCK, stroke_width=2.0,
            fill_color=ManimColor("#1A0E0B"), fill_opacity=0.95
        ).move_to([x_c, -1.45, 0])
        callout_badge_txt = Tex(
            r"$\beta \approx 0.90 \implies$ Near SRS Resonance Peak",
            font_size=18, color=RED_SHOCK
        ).move_to(callout_badge.get_center())
        callout_badge_group = VGroup(callout_badge, callout_badge_txt)

        callout_group = VGroup(
            callout_box, callout_line1, callout_line2,
            callout_sep, callout_line3, callout_line4,
            callout_badge_group
        )

        # Connecting arrow from Operating Point to Callout
        connect_arrow = Arrow(
            start=pt_oper + [0.18, 0, 0],
            end=[1.20, pt_oper[1], 0],
            color=AMBER,
            stroke_width=2.2,
            tip_length=0.18,
            buff=0
        )

        # ==================================================================
        # 7. ANIMATION CHOREOGRAPHY
        # ==================================================================
        # 0.0s - 0.8s: Title & Axes
        self.play(
            Write(title),
            Create(axes_srs),
            Write(x_lbl),
            Write(y_lbl),
            Create(static_line),
            Write(static_lbl),
            run_time=1.0,
            rate_func=ease_out_cubic
        )

        # 1.0s - 3.0s: SRS Curves reveal (Primary & Residual)
        self.play(
            Create(curve_primary),
            Create(curve_residual),
            FadeIn(lbl_pri, shift=UP * 0.1),
            FadeIn(lbl_res, shift=UP * 0.1),
            run_time=2.0,
            rate_func=ease_out_cubic
        )

        # 3.0s - 3.8s: Hold for Cuepoint 1
        self.wait(0.8)  # Cuepoint 1 = 3.8s

        # 3.8s - 5.5s: Operating Point illuminates with guides
        self.play(
            Create(guide_v),
            Create(guide_h),
            Write(oper_x_lbl),
            Write(oper_y_lbl),
            FadeIn(oper_marker, scale=1.5),
            run_time=1.5,
            rate_func=ease_out_cubic
        )

        # 5.5s - 7.0s: Callout Box illuminates with dynamic deflection
        self.play(
            Create(connect_arrow),
            FadeIn(callout_group, shift=LEFT * 0.20),
            callout_box.animate.set_stroke(color=AMBER, width=2.4),
            run_time=1.5,
            rate_func=ease_out_cubic
        )

        # 7.0s - 7.8s: Settle and subtle emphasis
        self.play(
            glow_oper.animate.scale(1.25),
            rate_func=there_and_back,
            run_time=0.8
        )

        # 7.8s - 8.5s: Final buffer
        self.wait(0.7)

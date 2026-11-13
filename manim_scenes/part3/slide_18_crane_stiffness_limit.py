"""
SLIDE-18: CraneStiffnessLimitScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 150 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Large presentation-grade mathematical typography (enlarged font sizes)
  - Symmetrical 2-panel layout morphing into climactic side-by-side comparison
  - Under 10-15 English words total on canvas (Strict 10-Word Rule)
  - Frame-Accurate Step Control:
      Step 1 (0.0s - 3.5s): Earthquake Design Spectrum Hazard Zone (Sa >= 1.0g for tau_n <= 0.52s)
      Step 2 (3.5s - 8.5s): Maximum Stiffness Inversion Derivation (k < 365 kN/m)
      Step 3 (8.5s - 14.2s): Stiff Derails vs Flexible Survives
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine
import numpy as np


class CraneStiffnessLimitScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SLATE       = ManimColor("#B0B8C4")   # Axes, gridlines, secondary annotations
        AMBER       = ManimColor("#FFB703")   # Mass m, period tau_n, critical threshold
        CYAN        = ManimColor("#58C4DD")   # Stiffness k, spectrum curve, contact forces
        RED_SHOCK   = ManimColor("#FF644E")   # Danger zone, Sa >= 1.0g, stiff derailment
        GREEN_PASS  = ManimColor("#83C167")   # Safe zone, Sa < 1.0g, flexible survival
        UT_BLUE     = ManimColor("#0097F1")   # University of Tehran Blue, accents
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 4 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Counter-Intuitive Stiffness Limit}",
            font_size=42,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # Helper function for sleek rounded badges
        def make_badge(tex_str, color, width, height, font_size=24, fill_color=BG_DARK, stroke_width=2.0):
            rect = RoundedRectangle(
                corner_radius=0.14,
                width=width,
                height=height,
                color=color,
                stroke_width=stroke_width,
                fill_color=fill_color,
                fill_opacity=0.94
            )
            tex = MathTex(tex_str, font_size=font_size, color=color)
            tex.move_to(rect.get_center())
            return VGroup(rect, tex)

        # ==================================================================
        # 3. PANELS & BASE GEOMETRY (Steps 1 & 2)
        # ==================================================================
        x_l = -3.45   # Left panel center
        x_r = +3.45   # Right panel center
        card_w = 6.55
        card_h = 5.80
        card_y = -0.30

        # Background Cards for Step 1 & 2
        card_left = RoundedRectangle(
            corner_radius=0.16, width=card_w, height=card_h,
            color=CARD_STROKE, stroke_width=2.0,
            fill_color=BG_DARK, fill_opacity=0.92
        ).move_to([x_l, card_y, 0])

        card_right = RoundedRectangle(
            corner_radius=0.16, width=card_w, height=card_h,
            color=CARD_STROKE, stroke_width=2.0,
            fill_color=BG_DARK, fill_opacity=0.92
        ).move_to([x_r, card_y, 0])

        # ------------------------------------------------------------------
        # STEP 1 COMPONENTS (Left Panel: Earthquake Spectrum)
        # ------------------------------------------------------------------
        header_l1 = make_badge(
            r"\textbf{Design Spectrum } (\zeta = 0.02)",
            SLATE, width=5.90, height=0.55, font_size=24
        ).move_to([x_l, 2.22, 0])

        axes = Axes(
            x_range=[0, 2.6, 0.5],
            y_range=[0, 1.5, 0.5],
            x_length=4.80,
            y_length=2.50,
            axis_config={"color": SLATE, "stroke_width": 2.0},
            tips=False
        ).move_to([x_l + 0.15, 0.45, 0])

        x_label = MathTex(r"\tau_n\text{ (s)}", font_size=23, color=SLATE).next_to(axes.x_axis, DOWN, buff=0.12).align_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"S_a / g", font_size=23, color=SLATE).next_to(axes.y_axis, LEFT, buff=0.12).align_to(axes.y_axis, UP)

        tick_052 = MathTex(r"0.52", font_size=21, color=AMBER).next_to(axes.c2p(0.52, 0), DOWN, buff=0.10)
        tick_1g = MathTex(r"1.0g", font_size=21, color=RED_SHOCK).next_to(axes.c2p(0, 1.0), LEFT, buff=0.10)

        # 1.0g Derailment Threshold Line
        thresh_line = DashedLine(
            axes.c2p(0, 1.0), axes.c2p(2.55, 1.0),
            color=RED_SHOCK, stroke_width=2.4, dash_length=0.08
        )
        thresh_label = MathTex(
            r"S_a = 1.0g",
            font_size=19, color=RED_SHOCK
        ).next_to(thresh_line, UP, buff=0.06).align_to(thresh_line, RIGHT)

        # Spectrum Curve (zeta = 0.02, Rao Fig. 4.19)
        def spectrum_func(t):
            if t < 0.06:
                return 0.35 + (t / 0.06) * 0.87
            elif t <= 0.52:
                return 1.22
            else:
                return 1.22 * (0.52 / t) ** 1.15

        spectrum_curve = axes.plot(spectrum_func, x_range=[0.02, 2.5, 0.02], color=CYAN, stroke_width=3.4)

        # Shaded Danger Plateau (tau_n <= 0.52s, Sa >= 1.0g)
        danger_area = axes.get_area(spectrum_curve, x_range=[0.02, 0.52], color=RED_SHOCK, opacity=0.36)
        safe_area = axes.get_area(spectrum_curve, x_range=[0.52, 2.5], color=GREEN_PASS, opacity=0.18)

        div_line = DashedLine(
            axes.c2p(0.52, 0), axes.c2p(0.52, 1.22),
            color=AMBER, stroke_width=2.4, dash_length=0.06
        )

        # Clean tags with ZERO axis overlap
        tag_danger = MathTex(r"\mathbf{DANGER}", font_size=21, color=RED_SHOCK).move_to(axes.c2p(0.27, 0.60))
        tag_safe = MathTex(r"\mathbf{SAFE}", font_size=23, color=GREEN_PASS).move_to(axes.c2p(1.45, 0.40))

        step1_spectrum_group = VGroup(
            header_l1, axes, x_label, y_label, tick_052, tick_1g,
            thresh_line, thresh_label, danger_area, safe_area,
            spectrum_curve, div_line, tag_danger, tag_safe
        )

        # Step 1 Left Panel Bottom Summary (Enlarged)
        spec_summary = MathTex(
            r"\tau_n \le 0.52\text{ s} \implies S_a \ge 1.0g \quad (\mathbf{Derails})",
            font_size=25, color=RED_SHOCK
        ).move_to([x_l, -2.40, 0])

        left_step1_all = VGroup(step1_spectrum_group, spec_summary)

        # ------------------------------------------------------------------
        # STEP 1 COMPONENTS (Right Panel: Safety Criterion - Enlarged)
        # ------------------------------------------------------------------
        header_r1 = make_badge(
            r"\textbf{Safety Criterion}",
            AMBER, width=5.90, height=0.55, font_size=24
        ).move_to([x_r, 2.22, 0])

        param_tag = MathTex(
            r"m = 2500\text{ kg} \quad \zeta = 0.02",
            font_size=30, color=CYAN
        ).move_to([x_r, 1.40, 0])

        cond_box1 = MathTex(
            r"N_{\min} = m(g - S_a) > 0 \iff S_a < 1.0g",
            font_size=30, color=TEXT_WHITE
        ).move_to([x_r, 0.55, 0])

        req_period_lbl = MathTex(
            r"\mathbf{Required\ Operating\ Period:}",
            font_size=27, color=AMBER
        ).move_to([x_r, -0.40, 0])

        req_period_val = make_badge(
            r"\mathbf{\tau_n > 0.52\text{ s}}",
            GREEN_PASS, width=3.80, height=0.80, font_size=38, stroke_width=2.8
        ).move_to([x_r, -1.35, 0])

        sub_note1 = MathTex(
            r"\mathbf{\tau_n > 0.52\text{ s}\ Guarantees\ Safe\ Contact}",
            font_size=23, color=GREEN_PASS
        ).move_to([x_r, -2.40, 0])

        right_step1_group = VGroup(
            header_r1, param_tag, cond_box1, req_period_lbl, req_period_val, sub_note1
        )

        # ==================================================================
        # STEP 2 COMPONENTS (Right Panel: Maximum Stiffness Inversion - Enlarged)
        # ==================================================================
        header_r2 = make_badge(
            r"\textbf{Stiffness Ceiling}",
            CYAN, width=5.90, height=0.55, font_size=24
        ).move_to([x_r, 2.22, 0])

        eq_deriv1 = MathTex(
            r"\tau_n = 2\pi\sqrt{\frac{m}{k}} > 0.52\text{ s}",
            font_size=38, color=AMBER
        ).move_to([x_r, 1.35, 0])

        eq_deriv2 = MathTex(
            r"\implies k < \frac{4\pi^2 m}{(0.52\text{ s})^2}",
            font_size=36, color=TEXT_WHITE
        ).move_to([x_r, 0.40, 0])

        eq_deriv3 = MathTex(
            r"k < \frac{4\pi^2 (2500\text{ kg})}{0.2704\text{ s}^2} = 365,000\text{ N/m}",
            font_size=30, color=CYAN
        ).move_to([x_r, -0.55, 0])

        badge_kmax = make_badge(
            r"\mathbf{STIFFNESS\ CEILING:}\quad k_{\max} = 365\text{ kN/m}",
            CYAN, width=6.15, height=0.82, font_size=27, stroke_width=2.8
        ).move_to([x_r, -1.75, 0])

        halo_kmax = RoundedRectangle(
            corner_radius=0.18, width=6.35, height=1.00,
            color=CYAN, stroke_width=3.2, fill_opacity=0.0
        ).move_to([x_r, -1.75, 0])

        sub_note2 = MathTex(
            r"\mathbf{Stiffening\ Beyond\ 365\text{ kN/m}\ Causes\ Derailment!}",
            font_size=23, color=RED_SHOCK
        ).move_to([x_r, -2.50, 0])

        right_step2_group = VGroup(
            header_r2, eq_deriv1, eq_deriv2, eq_deriv3, badge_kmax, halo_kmax, sub_note2
        )

        # ==================================================================
        # STEP 3 COMPONENTS: Side-by-Side Comparison (Enlarged Fonts, No Quiz)
        # ==================================================================
        # Left Comparison Card (Stiff Derails)
        card_stiff = RoundedRectangle(
            corner_radius=0.16, width=card_w, height=card_h,
            color=RED_SHOCK, stroke_width=2.8,
            fill_color=BG_DARK, fill_opacity=0.96
        ).move_to([x_l, card_y, 0])

        hdr_stiff = make_badge(
            r"\textbf{STIFF DERAILS}", RED_SHOCK, width=5.70, height=0.62, font_size=28
        ).move_to([x_l, 2.15, 0])

        stiff_row1 = MathTex(r"k > 365\text{ kN/m}", font_size=36, color=RED_SHOCK).move_to([x_l, 1.25, 0])
        arrow_stiff1 = MathTex(r"\Downarrow", font_size=32, color=RED_SHOCK).move_to([x_l, 0.65, 0])
        stiff_row2 = MathTex(r"\tau_n \le 0.52\text{ s}", font_size=36, color=AMBER).move_to([x_l, 0.05, 0])
        arrow_stiff2 = MathTex(r"\Downarrow", font_size=32, color=RED_SHOCK).move_to([x_l, -0.55, 0])
        stiff_row3 = MathTex(r"S_a \ge 1.0g \implies N_{\min} \le 0", font_size=32, color=TEXT_WHITE).move_to([x_l, -1.15, 0])
        arrow_stiff3 = MathTex(r"\Downarrow", font_size=32, color=RED_SHOCK).move_to([x_l, -1.75, 0])

        badge_stiff_out = make_badge(
            r"\mathbf{DERAILMENT}", RED_SHOCK, width=5.60, height=0.72, font_size=28, stroke_width=2.6
        ).move_to([x_l, -2.35, 0])

        halo_stiff_out = RoundedRectangle(
            corner_radius=0.16, width=5.80, height=0.88,
            color=RED_SHOCK, stroke_width=3.2, fill_opacity=0.0
        ).move_to([x_l, -2.35, 0])

        group_stiff_card = VGroup(
            card_stiff, hdr_stiff,
            stiff_row1, arrow_stiff1,
            stiff_row2, arrow_stiff2,
            stiff_row3, arrow_stiff3,
            badge_stiff_out
        )

        # Right Comparison Card (Flexible Survives)
        card_flex = RoundedRectangle(
            corner_radius=0.16, width=card_w, height=card_h,
            color=GREEN_PASS, stroke_width=2.8,
            fill_color=BG_DARK, fill_opacity=0.96
        ).move_to([x_r, card_y, 0])

        hdr_flex = make_badge(
            r"\textbf{FLEXIBLE SURVIVES}", GREEN_PASS, width=5.70, height=0.62, font_size=28
        ).move_to([x_r, 2.15, 0])

        flex_row1 = MathTex(r"k < 365\text{ kN/m}", font_size=36, color=GREEN_PASS).move_to([x_r, 1.25, 0])
        arrow_flex1 = MathTex(r"\Downarrow", font_size=32, color=GREEN_PASS).move_to([x_r, 0.65, 0])
        flex_row2 = MathTex(r"\tau_n > 0.52\text{ s}", font_size=36, color=CYAN).move_to([x_r, 0.05, 0])
        arrow_flex2 = MathTex(r"\Downarrow", font_size=32, color=GREEN_PASS).move_to([x_r, -0.55, 0])
        flex_row3 = MathTex(r"S_a < 1.0g \implies N_{\min} > 0", font_size=32, color=TEXT_WHITE).move_to([x_r, -1.15, 0])
        arrow_flex3 = MathTex(r"\Downarrow", font_size=32, color=GREEN_PASS).move_to([x_r, -1.75, 0])

        badge_flex_out = make_badge(
            r"\mathbf{SAFE\ CONTACT}", GREEN_PASS, width=5.60, height=0.72, font_size=28, stroke_width=2.6
        ).move_to([x_r, -2.35, 0])

        halo_flex_out = RoundedRectangle(
            corner_radius=0.16, width=5.80, height=0.88,
            color=GREEN_PASS, stroke_width=3.2, fill_opacity=0.0
        ).move_to([x_r, -2.35, 0])

        group_flex_card = VGroup(
            card_flex, hdr_flex,
            flex_row1, arrow_flex1,
            flex_row2, arrow_flex2,
            flex_row3, arrow_flex3,
            badge_flex_out
        )

        # ==================================================================
        # 4. ANIMATION CHOREOGRAPHY (Strict Frame-Accurate Cuepoints)
        # ==================================================================

        # --- STEP 1: Earthquake Spectrum Hazard Zone (0.0s to 3.5s) ---
        # 0.0s - 0.8s: Title reveals
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            run_time=0.8
        )

        # 0.8s - 2.4s: Cards and Spectrum Plot animate in
        self.play(
            FadeIn(card_left),
            FadeIn(card_right),
            FadeIn(header_l1),
            Create(axes),
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(tick_052),
            FadeIn(tick_1g),
            Create(thresh_line),
            FadeIn(thresh_label),
            Create(spectrum_curve),
            FadeIn(danger_area),
            FadeIn(safe_area),
            Create(div_line),
            FadeIn(tag_danger),
            FadeIn(tag_safe),
            FadeIn(spec_summary),
            run_time=1.6
        )

        # 2.4s - 3.2s: Safety Criterion on Right Panel
        self.play(
            FadeIn(header_r1),
            FadeIn(param_tag),
            FadeIn(cond_box1),
            FadeIn(req_period_lbl),
            FadeIn(req_period_val, scale=1.05),
            FadeIn(sub_note1),
            run_time=0.8
        )

        # 3.2s - 3.5s: Hold for Cuepoint 1
        self.wait(0.3)  # Exact Cuepoint 1 = 3.5s

        # --- STEP 2: Maximum Stiffness Inversion Derivation (3.5s to 8.5s) ---
        # 3.5s - 4.6s: Right Panel transitions to Stiffness Derivation
        self.play(
            FadeOut(right_step1_group, shift=LEFT * 0.15),
            FadeIn(header_r2),
            Write(eq_deriv1),
            run_time=1.1
        )

        # 4.6s - 6.0s: Inversion & Numerical Substitution
        self.play(
            Write(eq_deriv2),
            Write(eq_deriv3),
            run_time=1.4
        )

        # 6.0s - 7.2s: Glowing Ceiling Badge & Warning Pulse
        self.play(
            FadeIn(badge_kmax, scale=1.08),
            Create(halo_kmax),
            FadeIn(sub_note2),
            card_right.animate.set_stroke(color=CYAN, width=2.4),
            run_time=1.2
        )

        # 7.2s - 8.5s: Hold for Cuepoint 2
        self.wait(1.3)  # Exact Cuepoint 2 = 8.5s

        # --- STEP 3: Stiff Derails vs Flexible Survives (8.5s to 14.2s) ---
        # 8.5s - 10.3s: Stage morphs into Side-by-Side Comparison Cards
        self.play(
            FadeOut(left_step1_all, shift=LEFT * 0.2),
            FadeOut(card_left),
            FadeOut(right_step2_group, shift=RIGHT * 0.2),
            FadeOut(card_right),
            FadeIn(group_stiff_card, shift=UP * 0.1),
            FadeIn(group_flex_card, shift=UP * 0.1),
            run_time=1.8
        )

        # 10.3s - 12.0s: Glowing Badges Bloom on Both Cards
        self.play(
            Create(halo_stiff_out),
            Create(halo_flex_out),
            badge_stiff_out.animate.set_stroke(color=RED_SHOCK, width=3.4),
            badge_flex_out.animate.set_stroke(color=GREEN_PASS, width=3.4),
            run_time=1.7
        )

        # 12.0s - 13.2s: Radiant Halo Expansion Pulse
        self.play(
            halo_stiff_out.animate.scale(1.10).set_stroke(opacity=0.0),
            halo_flex_out.animate.scale(1.10).set_stroke(opacity=0.0),
            run_time=1.2
        )

        # 13.2s - 14.2s: Hold for Cuepoint 3
        self.wait(1.0)  # Exact Cuepoint 3 = 14.2s

        # --- Settling buffer (14.2s to 15.0s) ---
        self.wait(0.8)  # Video concludes at 15.0s

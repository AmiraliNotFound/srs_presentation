"""
SLIDE-20: WindBlastSRSScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 120 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Large presentation-grade mathematical typography (enlarged fonts & expanded cards)
  - Symmetrical 2-panel layout: Shock Response Spectrum vs Structural Response & Safety Certification
  - Under 10-15 English words total on canvas (Strict 10-Word Rule)
  - Frame-Accurate Step Control:
      Step 1 (0.0s - 3.5s): Half-Sine Shock Response Spectrum Curves (DLF vs beta)
      Step 2 (3.5s - 8.5s): Tower Operating Point (beta = 0.9031 -> DLF = 1.7587, x_max, V_max, M_b,max)
      Step 3 (8.5s - 14.2s): Root Bending Stress & Safety Verification (sigma_max = 8.31 MPa <= 12.0 MPa, FS = 1.44)
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine, there_and_back
import numpy as np


class WindBlastSRSScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SLATE       = ManimColor("#B0B8C4")   # Axes, residual curve, secondary notes
        CYAN        = ManimColor("#58C4DD")   # Primary SRS curve, displacement x_max
        AMBER       = ManimColor("#FFB703")   # Operating point, DLF, base moment Mb,max
        RED_SHOCK   = ManimColor("#FF644E")   # Near-peak dynamic overshoot
        GREEN_PASS  = ManimColor("#83C167")   # Permissible stress, FS = 1.44, certified safe
        UT_BLUE     = ManimColor("#0097F1")   # University of Tehran Blue accents
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        WALL_STROKE = ManimColor("#3B4D63")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")
        PASS_BG     = ManimColor("#06170E")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Blast SRS Verification}",
            font_size=40,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # Helper function for sleek rounded badges with zero text overflow
        def make_badge(tex_str, color, width, height, font_size=20, fill_color=BG_DARK, stroke_width=2.0):
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
        # 3. COORDINATE LAYOUT: Left Panel vs Right Panel
        # ==================================================================
        x_l = -3.55   # Left panel center (Half-Sine Shock Response Spectrum)
        x_r = +3.55   # Right panel center (Structural Response & Safety Certification)
        card_w = 6.45
        card_h = 5.85
        card_y = -0.25

        # Background Cards
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

        # ==================================================================
        # 4. LEFT PANEL: Half-Sine Shock Response Spectrum (SRS)
        # ==================================================================
        header_l = make_badge(
            r"\textbf{Half-Sine Shock Spectrum}\text{ (SRS)}",
            CYAN, width=5.90, height=0.52, font_size=20
        ).move_to([x_l, 2.24, 0])

        # 4.1 SRS Coordinate Axes
        axes_srs = Axes(
            x_range=[0, 2.40, 0.50],
            y_range=[0, 2.10, 0.50],
            x_length=5.10,
            y_length=3.40,
            axis_config={
                "color": SLATE,
                "stroke_width": 2.0,
                "include_ticks": True,
                "tick_size": 0.08,
            }
        ).move_to([x_l + 0.15, -0.15, 0])

        srs_x_lbl = MathTex(r"\beta = \frac{t_0}{\tau_n}", font_size=21, color=SLATE).next_to(axes_srs.x_axis, RIGHT, buff=0.12)
        srs_y_lbl = MathTex(r"\mathbf{DLF}", font_size=22, color=SLATE).next_to(axes_srs.y_axis, UP, buff=0.12)
        srs_axes_group = VGroup(axes_srs, srs_x_lbl, srs_y_lbl)

        # 4.2 Analytical SRS Curves
        # Primary Era DLF: DLF_p = 2*b / |2*b - 1| * |sin(2*pi / (2*b + 1))|
        def dlf_primary(b):
            if np.isclose(b, 0.5, atol=1e-3):
                return np.pi / 2.0
            return (2.0 * b / np.abs(2.0 * b - 1.0)) * np.abs(np.sin(2.0 * np.pi / (2.0 * b + 1.0)))

        # Residual Era DLF: DLF_r = 4*b / |1 - 4*b^2| * |cos(pi * b)|
        def dlf_residual(b):
            if np.isclose(b, 0.5, atol=1e-3):
                return np.pi / 2.0
            return (4.0 * b / np.abs(1.0 - 4.0 * b**2)) * np.abs(np.cos(np.pi * b))

        curve_primary = axes_srs.plot(
            dlf_primary,
            x_range=[0.05, 2.35],
            color=CYAN,
            stroke_width=3.2
        )

        curve_residual = axes_srs.plot(
            dlf_residual,
            x_range=[0.05, 2.35],
            color=SLATE,
            stroke_width=2.0
        ).set_stroke(opacity=0.60)

        # Static Reference Line (DLF = 1.0)
        line_static = DashedLine(
            axes_srs.c2p(0, 1.0), axes_srs.c2p(2.35, 1.0),
            color=TEXT_MUTED, stroke_width=1.5, dash_length=0.08
        )
        static_lbl = MathTex(r"\text{Static } (\mathbf{DLF} = 1.0)", font_size=16, color=TEXT_MUTED).next_to(line_static, UP, buff=0.04).align_to(axes_srs.c2p(1.9, 1.0), LEFT)

        # Legend annotations
        leg_prim = MathTex(r"—\ \text{Primary Era } (t \le t_0)", font_size=17, color=CYAN).move_to([x_l - 0.70, -2.40, 0])
        leg_res  = MathTex(r"--\ \text{Residual Era } (t > t_0)", font_size=17, color=SLATE).move_to([x_l + 1.40, -2.40, 0])
        legend_group = VGroup(leg_prim, leg_res, line_static, static_lbl)

        # 4.3 Tower Operating Point at beta = 0.9031
        beta_tower = 0.9031
        dlf_tower  = 1.7587

        pt_tower = axes_srs.c2p(beta_tower, dlf_tower)
        dot_tower = Dot(point=pt_tower, radius=0.09, color=RED_SHOCK)
        halo_tower = Circle(radius=0.20, color=AMBER, stroke_width=2.0).move_to(pt_tower)

        # Projection lines
        proj_x = DashedLine(axes_srs.c2p(beta_tower, 0), pt_tower, color=AMBER, stroke_width=1.8)
        proj_y = DashedLine(axes_srs.c2p(0, dlf_tower), pt_tower, color=RED_SHOCK, stroke_width=1.8)

        lbl_beta = MathTex(r"\beta = 0.903", font_size=18, color=AMBER).next_to(axes_srs.c2p(beta_tower, 0), DOWN, buff=0.10)
        lbl_dlf  = MathTex(r"\mathbf{DLF} = 1.76", font_size=18, color=RED_SHOCK).next_to(axes_srs.c2p(0, dlf_tower), LEFT, buff=0.10)

        operating_point_group = VGroup(proj_x, proj_y, dot_tower, halo_tower, lbl_beta, lbl_dlf)

        op_badge = make_badge(
            r"\mathbf{DLF} = 1.7587 \quad (+75.9\%\ \text{Dynamic Overshoot})",
            AMBER, width=5.90, height=0.52, font_size=19,
            fill_color=ManimColor("#1A1408"), stroke_width=2.0
        ).move_to([x_l, 1.58, 0])

        # ==================================================================
        # 5. RIGHT PANEL: Structural Response & Safety Verification
        # ==================================================================
        header_r = make_badge(
            r"\textbf{Structural Response \& Safety}",
            GREEN_PASS, width=5.90, height=0.52, font_size=20
        ).move_to([x_r, 2.24, 0])

        # 5.1 Step 2: Dynamic Response Quantities (y = 1.45 to -0.10)
        r_row1 = MathTex(
            r"x_{\max} = \mathbf{DLF} \cdot \delta_{\text{st}} = (1.7587)(45.92\text{ mm}) = \mathbf{80.76\text{ mm}}",
            font_size=22, color=CYAN
        ).move_to([x_r, 1.50, 0])

        r_row2 = MathTex(
            r"V_{\max} = \mathbf{DLF} \cdot F_0 = (1.7587)(180\text{ kN}) = \mathbf{316.57\text{ kN}}",
            font_size=22, color=TEXT_WHITE
        ).move_to([x_r, 0.90, 0])

        r_row3 = MathTex(
            r"M_{b,\max} = V_{\max} \cdot l = (316.57\text{ kN})(35.0\text{ m}) = \mathbf{11,079.8\text{ kN}\cdot\text{m}}",
            font_size=21, color=AMBER
        ).move_to([x_r, 0.30, 0])

        # 5.2 Step 3: Root Bending Stress & Certified Safe Badge (y = -0.30 to -2.70)
        divider_r = Line([x_r - 2.80, -0.20, 0], [x_r + 2.80, -0.20, 0], color=WALL_STROKE, stroke_width=1.5)

        r_row4 = MathTex(
            r"\sigma_{\max} = \frac{M_{b,\max} c}{I} = \frac{(1.1080 \times 10^7\text{ N}\cdot\text{m})(1.40\text{ m})}{1.8673\text{ m}^4} = \mathbf{8.307\text{ MPa}}",
            font_size=20, color=TEXT_WHITE
        ).move_to([x_r, -0.65, 0])

        r_row5 = MathTex(
            r"\sigma_{\max} = 8.31\text{ MPa} \le \sigma_{\text{allow}} = 12.0\text{ MPa}",
            font_size=23, color=GREEN_PASS
        ).move_to([x_r, -1.22, 0])

        cert_badge = make_badge(
            r"\mathbf{FS} = \frac{12.0}{8.31} = \mathbf{1.44} \quad [\checkmark\ \mathbf{CERTIFIED\ SAFE}]",
            GREEN_PASS, width=5.90, height=0.62, font_size=23,
            fill_color=PASS_BG, stroke_width=2.8
        ).move_to([x_r, -1.95, 0])

        cert_sub = MathTex(
            r"\text{Municipal Water Tower Survives Extreme Gust}",
            font_size=19, color=SLATE
        ).move_to([x_r, -2.55, 0])

        # ==================================================================
        # ANIMATION CHOREOGRAPHY & FRAME-ACCURATE TIMESTAMPS
        # ==================================================================

        # --- STEP 1: Half-Sine Shock Spectrum Curves (0.0s - 3.5s) ---
        # 0.0s - 0.7s: Title & Background Cards appear
        self.play(
            Write(title),
            FadeIn(card_left, shift=UP * 0.15),
            FadeIn(card_right, shift=UP * 0.15),
            run_time=0.7
        )

        # 0.7s - 2.4s: SRS Axes & Curves Plot
        self.play(
            FadeIn(header_l),
            Create(srs_axes_group),
            Create(curve_primary),
            Create(curve_residual),
            FadeIn(legend_group),
            run_time=1.7,
            rate_func=ease_out_cubic
        )

        # 2.4s - 3.2s: Left card subtle glow
        self.play(
            card_left.animate.set_stroke(color=CYAN, width=2.4),
            run_time=0.8
        )

        # 3.2s - 3.5s: Hold for Cuepoint 1
        self.wait(0.3)  # Exact Cuepoint 1 = 3.5s

        # --- STEP 2: Operating Point & Dynamic Load Quantities (3.5s - 8.5s) ---
        # 3.5s - 5.0s: Operating Point beta = 0.9031 illuminates on SRS curve
        self.play(
            Create(proj_x),
            Create(proj_y),
            FadeIn(operating_point_group),
            FadeIn(op_badge, shift=UP * 0.10),
            run_time=1.5
        )

        # 5.0s - 7.5s: Right Card Header & Dynamic Response Quantities Reveal
        self.play(
            card_right.animate.set_stroke(color=AMBER, width=2.4),
            FadeIn(header_r, shift=UP * 0.12),
            Write(r_row1),
            Write(r_row2),
            Write(r_row3),
            Create(divider_r),
            run_time=2.5,
            rate_func=ease_out_cubic
        )

        # 7.5s - 8.5s: Hold for Cuepoint 2
        self.wait(1.0)  # Exact Cuepoint 2 = 8.5s

        # --- STEP 3: Root Bending Stress & Certified Safe Badge (8.5s - 14.2s) ---
        # 8.5s - 10.4s: Root Bending Stress and Limit Evaluation
        self.play(
            Write(r_row4),
            Write(r_row5),
            run_time=1.9,
            rate_func=ease_out_cubic
        )

        # 10.4s - 12.2s: Factor of Safety & Certified Safe Badge Reveal
        self.play(
            FadeIn(cert_badge, shift=UP * 0.18),
            FadeIn(cert_sub, shift=UP * 0.10),
            card_right.animate.set_stroke(color=GREEN_PASS, width=2.8),
            run_time=1.8
        )

        # 12.2s - 13.5s: Pulsing Glow on Certified Badge
        self.play(
            cert_badge.animate.scale(1.04),
            halo_tower.animate.scale(1.25),
            rate_func=there_and_back,
            run_time=1.3
        )

        # 13.5s - 14.2s: Hold for Cuepoint 3
        self.wait(0.7)  # Exact Cuepoint 3 = 14.2s

        # 14.2s - 15.0s: Settle and loop buffer
        self.wait(0.8)

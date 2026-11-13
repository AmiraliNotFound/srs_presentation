"""
SLIDE-20B: WindBlastSafetyScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 60 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars
  - High breathing room, large presentation math typography
  - Left: Deflected municipal tower with dynamic deflection x_max and base moment M_b,max
  - Right: Spacious stress verification and certified factor of safety FS = 1.44
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine, there_and_back
import numpy as np


class WindBlastSafetyScene(Scene):
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
        PASS_GREEN  = ManimColor("#83C167")
        TEXT_WHITE  = ManimColor("#FFFFFF")
        WALL_STROKE = ManimColor("#3B4D63")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Structural Response \& Safety Certification}",
            font_size=40,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        def make_badge(tex_str, color, width, height, font_size=22, fill_color=BG_DARK, stroke_width=2.2):
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
        # 3. LEFT HALF: Dynamically Deflected Water Tower (Center x = -4.3)
        # ==================================================================
        x_t = -4.3

        # 3.1 Foundation Ground Slab
        ground_slab = RoundedRectangle(
            corner_radius=0.08, width=3.40, height=0.36,
            color=WALL_STROKE, stroke_width=1.8,
            fill_color=ManimColor("#131D2A"), fill_opacity=0.92
        ).move_to([x_t, -2.65, 0])

        # 3.2 Deflected Column (Cantilever Cubic Deflection y = -2.47 to 0.57)
        # y from 0 to 1 normalized: x_bend(y) = delta * (3*y^2 - y^3)/2
        y_bot = -2.47
        y_top = 0.57
        H_col = y_top - y_bot
        delta_vis = 0.45  # Visual deflection scale

        pts_left = []
        pts_right = []
        for s in np.linspace(0, 1, 40):
            y_curr = y_bot + s * H_col
            dx = delta_vis * (1.5 * s**2 - 0.5 * s**3)
            pts_left.append([x_t - 0.325 + dx, y_curr, 0])
            pts_right.append([x_t + 0.325 + dx, y_curr, 0])

        curve_l = VMobject(color=SLATE, stroke_width=2.4).set_points_smoothly(pts_left)
        curve_r = VMobject(color=SLATE, stroke_width=2.4).set_points_smoothly(pts_right)

        # Fill between curves
        fill_poly_pts = pts_left + pts_right[::-1]
        col_fill = Polygon(*fill_poly_pts, color=SLATE, stroke_width=0, fill_color=ManimColor("#1A2433"), fill_opacity=0.85)
        col_deflected = VGroup(col_fill, curve_l, curve_r)

        # Undeflected ghost column (dashed)
        ghost_col = Rectangle(
            width=0.65, height=H_col,
            color=WALL_STROKE, stroke_width=1.2,
            fill_opacity=0
        ).move_to([x_t, (y_bot + y_top)/2, 0])
        ghost_centerline = DashedLine([x_t, y_bot, 0], [x_t, y_top, 0], color=WALL_STROKE, stroke_width=1.2)

        # 3.3 Deflected Water Tank (at top of deflected column)
        tank_w = 1.90
        tank_cyl_h = 0.75
        tank_x = x_t + delta_vis

        tank_cyl = RoundedRectangle(
            corner_radius=0.08, width=tank_w, height=tank_cyl_h,
            color=SLATE, stroke_width=2.4,
            fill_color=UT_BLUE, fill_opacity=0.70
        ).move_to([tank_x, y_top + tank_cyl_h/2, 0])

        tank_dome = Arc(radius=tank_w/2, start_angle=0, angle=PI, color=SLATE, stroke_width=2.4).move_to([tank_x, y_top + tank_cyl_h + 0.20, 0])
        tank_dome_fill = Sector(radius=tank_w/2, start_angle=0, angle=PI, color=UT_BLUE, fill_opacity=0.70, stroke_width=0).move_to([tank_x, y_top + tank_cyl_h + 0.20, 0])
        water_lbl = MathTex(r"250\text{ kL Tank}", font_size=18, color=TEXT_WHITE).move_to([tank_x, y_top + 0.35, 0])
        tank_deflected = VGroup(tank_cyl, tank_dome_fill, tank_dome, water_lbl)

        # 3.4 Deflection Indicator Arrow cleanly positioned above Tank Dome
        y_arrow = 2.65
        ref_line_undef = DashedLine([x_t, y_top + tank_cyl_h + 0.20, 0], [x_t, y_arrow + 0.15, 0], color=WALL_STROKE, stroke_width=1.2)
        ref_line_def = DashedLine([tank_x, y_top + tank_cyl_h + 0.20, 0], [tank_x, y_arrow + 0.15, 0], color=CYAN, stroke_width=1.2)
        defl_arrow = DoubleArrow(
            [x_t, y_arrow, 0], [tank_x, y_arrow, 0],
            color=CYAN, tip_length=0.10, stroke_width=2.0
        )
        defl_lbl = MathTex(r"x_{\max} = \mathbf{80.8\text{ mm}}", font_size=19, color=CYAN).next_to(defl_arrow, UP, buff=0.08)
        defl_group = VGroup(ref_line_undef, ref_line_def, defl_arrow, defl_lbl)

        # 3.5 Base Moment Indicator Arc & Label
        moment_arc = CurvedArrow(
            start_point=[x_t - 0.75, -2.15, 0],
            end_point=[x_t + 0.75, -2.15, 0],
            radius=-0.95,
            color=AMBER,
            stroke_width=2.6,
            tip_length=0.18
        )
        moment_lbl = MathTex(
            r"M_{b,\max} = \mathbf{11,080\text{ kN}\cdot\text{m}}",
            font_size=19, color=AMBER
        ).next_to(ground_slab, DOWN, buff=0.12)
        base_group = VGroup(moment_arc, moment_lbl)

        # ==================================================================
        # 4. RIGHT HALF: Spacious Derivation & Safety Card (Center x = 2.10)
        # ==================================================================
        x_r = 2.10

        card_r = RoundedRectangle(
            corner_radius=0.18, width=7.80, height=5.70,
            color=CARD_STROKE, stroke_width=2.0,
            fill_color=BG_DARK, fill_opacity=0.92
        ).move_to([x_r, -0.25, 0])

        # Step 1: Dynamic Deflection
        eq_disp = MathTex(
            r"x_{\max} = \mathbf{DLF} \cdot \delta_{\text{st}} = (1.7587)(45.92\text{ mm}) = \mathbf{80.76\text{ mm}}",
            font_size=23, color=CYAN
        ).move_to([x_r, 1.65, 0])

        # Step 2: Base Shear & Overturning Moment
        eq_moment = MathTex(
            r"M_{b,\max} = V_{\max} \cdot l = (\mathbf{316.57\text{ kN}})(35.0\text{ m}) = \mathbf{11,079.8\text{ kN}\cdot\text{m}}",
            font_size=23, color=AMBER
        ).move_to([x_r, 0.75, 0])

        # Step 3: Column Base Bending Stress
        eq_stress_calc = MathTex(
            r"\sigma_{\max} = \frac{M_{b,\max} \cdot c}{I} = \frac{(1.1080 \times 10^7\text{ N}\cdot\text{m})(1.40\text{ m})}{1.8673\text{ m}^4} = \mathbf{8.31\text{ MPa}}",
            font_size=22, color=TEXT_WHITE
        ).move_to([x_r, -0.15, 0])

        # Step 4: Allowable Stress Comparison
        eq_stress_check = MathTex(
            r"\sigma_{\max} = \mathbf{8.31\text{ MPa}} \le \sigma_{\text{allow}} = \mathbf{12.0\text{ MPa}}",
            font_size=24, color=SLATE
        ).move_to([x_r, -1.05, 0])

        # Step 5: Certified Safety Factor Badge
        badge_safe = make_badge(
            r"\mathbf{FS} = \frac{12.0}{8.31} = \mathbf{1.44} \quad \left[\checkmark\ \mathbf{CERTIFIED\ SAFE}\right]",
            PASS_GREEN, width=7.00, height=0.62, font_size=23,
            fill_color=ManimColor("#0E1D13"), stroke_width=2.5
        ).move_to([x_r, -2.05, 0])

        # Subtitle below badge
        sub_safe = Tex(
            r"Elevated Municipal Tower Withstands Peak SRS Dynamic Blast Shock",
            font_size=18, color=PASS_GREEN
        ).move_to([x_r, -2.62, 0])

        # ==================================================================
        # 5. ANIMATION CHOREOGRAPHY
        # ==================================================================
        # 0.0s - 0.8s: Title & Stage Setup
        self.play(
            Write(title),
            FadeIn(card_r, shift=UP * 0.15),
            FadeIn(ground_slab),
            Create(ghost_col),
            Create(ghost_centerline),
            run_time=0.8
        )

        # 0.8s - 2.5s: Dynamic Deflection occurs with arrow & label
        self.play(
            Create(col_deflected),
            FadeIn(tank_deflected),
            Create(defl_group),
            run_time=1.7,
            rate_func=ease_out_cubic
        )

        # 2.5s - 3.2s: Hold for Cuepoint 1
        self.wait(0.7)  # Cuepoint 1 = 3.2s

        # 3.2s - 5.0s: Step 1 (Disp) & Step 2 (Moment) reveal
        self.play(
            Write(eq_disp),
            Write(eq_moment),
            Create(base_group),
            run_time=1.8,
            rate_func=ease_out_cubic
        )

        # 5.0s - 6.5s: Step 3 (Stress) & Step 4 (Allowable Check) reveal
        self.play(
            Write(eq_stress_calc),
            Write(eq_stress_check),
            run_time=1.5,
            rate_func=ease_out_cubic
        )

        # 6.5s - 7.8s: Factor of Safety & Certified Safe Badge illuminates
        self.play(
            FadeIn(badge_safe, shift=UP * 0.15),
            FadeIn(sub_safe, shift=UP * 0.10),
            card_r.animate.set_stroke(color=PASS_GREEN, width=2.4),
            run_time=1.3,
            rate_func=ease_out_cubic
        )

        # 7.8s - 8.5s: Subtle pulse on Certified Badge
        self.play(
            badge_safe.animate.scale(1.03),
            rate_func=there_and_back,
            run_time=0.7
        )

        # 8.5s - 9.2s: Final buffer
        self.wait(0.7)

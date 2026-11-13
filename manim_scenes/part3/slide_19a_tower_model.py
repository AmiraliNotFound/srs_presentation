"""
SLIDE-19A: MunicipalTowerModelScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 60 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars
  - Generous spacing, large presentation math typography (23-28 pt)
  - SDOF Idealization: 35m hollow concrete pedestal + 250,000 L elevated storage tank
  - Rayleigh mass reduction, lateral stiffness, natural period tau_n = 1.7717s
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine, there_and_back
import numpy as np


class MunicipalTowerModelScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SLATE       = ManimColor("#B0B8C4")
        CYAN        = ManimColor("#58C4DD")
        AMBER       = ManimColor("#FFB703")
        UT_BLUE     = ManimColor("#0097F1")
        TEXT_WHITE  = ManimColor("#FFFFFF")
        WALL_STROKE = ManimColor("#3B4D63")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Municipal Tower SDOF Model}",
            font_size=42,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        def make_badge(tex_str, color, width, height, font_size=22, fill_color=BG_DARK, stroke_width=2.0):
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
        # 3. LEFT HALF: Physical Water Tower Schematic (Centered at x = -3.8)
        # ==================================================================
        x_t = -3.8

        # 3.1 Ground Foundation Slab & Hatching
        ground_slab = RoundedRectangle(
            corner_radius=0.08, width=4.80, height=0.45,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#131D2A"), fill_opacity=0.92
        ).move_to([x_t, -2.60, 0])

        ground_hatches = VGroup()
        for i in range(10):
            hx = (x_t - 2.10) + i * 0.46
            h_line = Line([hx - 0.14, -2.80, 0], [hx + 0.14, -2.60, 0], color=WALL_STROKE, stroke_width=1.6)
            ground_hatches.add(h_line)

        # 3.2 Concrete Shaft Column (y = -2.375 to 0.70)
        col_w = 0.75
        col_h = 3.075
        col_y = -0.8375
        col_body = Rectangle(
            width=col_w, height=col_h,
            color=SLATE, stroke_width=0,
            fill_color=ManimColor("#1A2433"), fill_opacity=0.85
        ).move_to([x_t, col_y, 0])

        col_core = Rectangle(
            width=0.45, height=col_h,
            color=ManimColor("#0E1622"), stroke_width=1.2,
            fill_color=ManimColor("#0B0F19"), fill_opacity=0.95
        ).move_to([x_t, col_y, 0])

        col_left = Line([x_t - col_w/2, -2.375, 0], [x_t - col_w/2, 0.70, 0], color=SLATE, stroke_width=2.8)
        col_right = Line([x_t + col_w/2, -2.375, 0], [x_t + col_w/2, 0.70, 0], color=SLATE, stroke_width=2.8)
        column_assembly = VGroup(col_body, col_core, col_left, col_right)

        # Height Dimension Arrow (l = 35.0 m) placed safely on left
        dim_line = DoubleArrow([x_t - 1.50, -2.375, 0], [x_t - 1.50, 0.70, 0], color=CYAN, tip_length=0.18, stroke_width=2.0)
        dim_label = MathTex(r"l = 35.0\text{ m}", font_size=21, color=CYAN).next_to(dim_line, LEFT, buff=0.12)
        dim_group = VGroup(dim_line, dim_label)

        # 3.3 Elevated Water Tank (y = 0.70 to 2.10)
        tank_w = 2.10
        tank_cyl_h = 0.85
        tank_cyl = RoundedRectangle(
            corner_radius=0.10, width=tank_w, height=tank_cyl_h,
            color=SLATE, stroke_width=2.6,
            fill_color=UT_BLUE, fill_opacity=0.70
        ).move_to([x_t, 0.70 + tank_cyl_h/2, 0])

        tank_dome = Arc(
            radius=tank_w/2, start_angle=0, angle=PI,
            color=SLATE, stroke_width=2.6
        ).move_to([x_t, 0.70 + tank_cyl_h + 0.24, 0])

        tank_dome_fill = Sector(
            radius=tank_w/2, start_angle=0, angle=PI,
            color=UT_BLUE, fill_opacity=0.70, stroke_width=0
        ).move_to([x_t, 0.70 + tank_cyl_h + 0.24, 0])

        water_line = DashedLine([x_t - tank_w/2 + 0.12, 1.25, 0], [x_t + tank_w/2 - 0.12, 1.25, 0], color=TEXT_WHITE, stroke_width=1.8)
        water_label = MathTex(r"250\text{ kL Water}", font_size=19, color=TEXT_WHITE).move_to([x_t, 0.98, 0])
        tank_assembly = VGroup(tank_cyl, tank_dome_fill, tank_dome, water_line, water_label)

        # Tank Mass Indicator neatly above the dome
        tank_mass_lbl = MathTex(r"M = 265,000\text{ kg}", font_size=21, color=AMBER).move_to([x_t, 2.45, 0])
        tank_mass_arr = Arrow(start=[x_t, 2.30, 0], end=[x_t, 1.95, 0], color=AMBER, stroke_width=2.2, tip_length=0.15, buff=0)
        mass_callout = VGroup(tank_mass_lbl, tank_mass_arr)

        # ==================================================================
        # 4. RIGHT HALF: Spacious Mathematical SDOF Parameters (Center x = 2.8)
        # ==================================================================
        x_r = 2.80
        card_r = RoundedRectangle(
            corner_radius=0.18, width=6.60, height=5.60,
            color=CARD_STROKE, stroke_width=2.0,
            fill_color=BG_DARK, fill_opacity=0.92
        ).move_to([x_r, -0.20, 0])

        header_r = make_badge(
            r"\textbf{Section Properties \& SDOF Parameters}",
            SLATE, width=6.10, height=0.52, font_size=21
        ).move_to([x_r, 2.15, 0])

        row1 = MathTex(
            r"D_o = 2.80\text{ m}, \quad D_i = 2.20\text{ m} \implies I = 1.8673\text{ m}^4",
            font_size=23, color=SLATE
        ).move_to([x_r, 1.40, 0])

        row2 = MathTex(
            r"k = \frac{3EI}{l^3} = \frac{3(30\text{ GPa})(1.867\text{ m}^4)}{(35.0\text{ m})^3} = \mathbf{3,919.7\text{ kN/m}}",
            font_size=23, color=CYAN
        ).move_to([x_r, 0.60, 0])

        row3 = MathTex(
            r"M_{\text{eff}} = M + \frac{33}{140}m_{\text{col}} = 265\text{ t} + 46.7\text{ t} = \mathbf{311,653\text{ kg}}",
            font_size=23, color=AMBER
        ).move_to([x_r, -0.20, 0])

        row4 = MathTex(
            r"\omega_n = \sqrt{\frac{k}{M_{\text{eff}}}} = \mathbf{3.5464\text{ rad/s}} \quad (f_n = 0.564\text{ Hz})",
            font_size=23, color=TEXT_WHITE
        ).move_to([x_r, -1.00, 0])

        period_badge = make_badge(
            r"\tau_n = \frac{2\pi}{\omega_n} = \mathbf{1.7717\text{ s}} \quad (\text{Fundamental Period})",
            UT_BLUE, width=6.10, height=0.62, font_size=22,
            fill_color=ManimColor("#07121E"), stroke_width=2.4
        ).move_to([x_r, -1.85, 0])

        math_content = VGroup(row1, row2, row3, row4, period_badge)

        # ==================================================================
        # 5. ANIMATION CHOREOGRAPHY
        # ==================================================================
        # 0.0s - 0.7s: Title & Background Card
        self.play(
            Write(title),
            FadeIn(card_r, shift=UP * 0.15),
            run_time=0.7
        )

        # 0.7s - 2.5s: Tower Schematic reveals cleanly
        self.play(
            FadeIn(ground_slab),
            Create(ground_hatches),
            Create(column_assembly),
            FadeIn(tank_assembly),
            Create(dim_group),
            FadeIn(mass_callout),
            run_time=1.8,
            rate_func=ease_out_cubic
        )

        # 2.5s - 3.2s: Hold for Cuepoint 1
        self.wait(0.7)  # Cuepoint 1 = 3.2s

        # 3.2s - 4.4s: Right Header & Stiffness k reveal
        self.play(
            FadeIn(header_r, shift=UP * 0.10),
            Write(row1),
            Write(row2),
            card_r.animate.set_stroke(color=CYAN, width=2.4),
            run_time=1.2
        )

        # 4.4s - 5.8s: Rayleigh Mass & Frequency reveal
        self.play(
            Write(row3),
            Write(row4),
            run_time=1.4
        )

        # 5.8s - 6.8s: Natural Period Badge illuminates
        self.play(
            FadeIn(period_badge, shift=UP * 0.15),
            run_time=0.8
        )
        self.play(
            period_badge.animate.scale(1.04),
            rate_func=there_and_back,
            run_time=0.8
        )

        # 7.6s - 8.5s: Final settle buffer
        self.wait(0.9)

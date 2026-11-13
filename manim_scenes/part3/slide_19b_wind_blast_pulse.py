"""
SLIDE-19B: WindBlastPulseScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 60 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars
  - High breathing room, large presentation math typography (22-26 pt)
  - Left: Aerodynamic wind blast front striking the elevated water tower
  - Right: Spacious Half-Sine shock pulse plot F(t) vs t, peak F0 = 180 kN, duration t0 = 1.60s
  - Dimensionless pulse ratio beta = t0 / tau_n = 0.9031 (Dynamic Shock Regime)
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine, there_and_back
import numpy as np


class WindBlastPulseScene(Scene):
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
            r"\textbf{Wind-Blast Shock Pulse}",
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
        # 3. LEFT HALF: Tower & Wind Blast Front (Center x = -4.4)
        # ==================================================================
        x_t = -4.4

        # 3.1 Foundation
        ground_slab = RoundedRectangle(
            corner_radius=0.08, width=3.40, height=0.36,
            color=WALL_STROKE, stroke_width=1.8,
            fill_color=ManimColor("#131D2A"), fill_opacity=0.92
        ).move_to([x_t, -2.65, 0])

        # 3.2 Pedestal Column
        col_w = 0.65
        col_h = 3.05
        col_body = Rectangle(
            width=col_w, height=col_h,
            color=SLATE, stroke_width=0,
            fill_color=ManimColor("#1A2433"), fill_opacity=0.85
        ).move_to([x_t, -0.95, 0])

        col_l = Line([x_t - col_w/2, -2.47, 0], [x_t - col_w/2, 0.57, 0], color=SLATE, stroke_width=2.4)
        col_r = Line([x_t + col_w/2, -2.47, 0], [x_t + col_w/2, 0.57, 0], color=SLATE, stroke_width=2.4)
        col_group = VGroup(col_body, col_l, col_r)

        # 3.3 Water Tank
        tank_w = 1.90
        tank_cyl_h = 0.75
        tank_cyl = RoundedRectangle(
            corner_radius=0.08, width=tank_w, height=tank_cyl_h,
            color=SLATE, stroke_width=2.4,
            fill_color=UT_BLUE, fill_opacity=0.70
        ).move_to([x_t, 0.57 + tank_cyl_h/2, 0])

        tank_dome = Arc(radius=tank_w/2, start_angle=0, angle=PI, color=SLATE, stroke_width=2.4).move_to([x_t, 0.57 + tank_cyl_h + 0.20, 0])
        tank_dome_fill = Sector(radius=tank_w/2, start_angle=0, angle=PI, color=UT_BLUE, fill_opacity=0.70, stroke_width=0).move_to([x_t, 0.57 + tank_cyl_h + 0.20, 0])
        water_lbl = MathTex(r"250\text{ kL Tank}", font_size=18, color=TEXT_WHITE).move_to([x_t, 0.92, 0])
        tank_group = VGroup(tank_cyl, tank_dome_fill, tank_dome, water_lbl)

        # 3.4 Wind Blast Dynamic Shock Front
        wind_arrows = VGroup()
        for dy in [-0.25, 0.00, 0.25]:
            arr = Arrow(
                start=[x_t - 2.10, 1.02 + dy, 0],
                end=[x_t - 1.05, 1.02 + dy, 0],
                color=RED_SHOCK,
                stroke_width=3.2,
                tip_length=0.20,
                buff=0
            )
            wind_arrows.add(arr)
        wind_txt = Tex(r"\textbf{Wind Gust}", font_size=20, color=RED_SHOCK).next_to(wind_arrows, UP, buff=0.12)
        wind_front = VGroup(wind_arrows, wind_txt)

        # ==================================================================
        # 4. RIGHT HALF: Large Shock Pulse Coordinate Plot (Center x = 2.20)
        # ==================================================================
        x_r = 2.20

        # Card container with generous padding (No nested top header banner)
        card_r = RoundedRectangle(
            corner_radius=0.18, width=7.60, height=5.70,
            color=CARD_STROKE, stroke_width=2.0,
            fill_color=BG_DARK, fill_opacity=0.92
        ).move_to([x_r, -0.25, 0])

        # 4.1 Pulse Coordinate Axes
        axes_pulse = Axes(
            x_range=[0, 2.50, 0.50],
            y_range=[0, 220, 50],
            x_length=5.80,
            y_length=2.40,
            axis_config={
                "color": SLATE,
                "stroke_width": 2.0,
                "include_ticks": True,
                "tick_size": 0.07,
            }
        ).move_to([x_r - 0.25, 0.90, 0])

        x_lbl = MathTex(r"t\text{ (s)}", font_size=19, color=SLATE).next_to(axes_pulse.x_axis, RIGHT, buff=0.15)
        y_lbl = MathTex(r"F(t)\text{ (kN)}", font_size=19, color=SLATE).next_to(axes_pulse.y_axis, UP, buff=0.12)
        pulse_axes_group = VGroup(axes_pulse, x_lbl, y_lbl)

        # 4.2 Pulse Curve & Shading
        t0_val = 1.60
        f0_val = 180.0

        def pulse_func(t):
            if t <= t0_val:
                return f0_val * np.sin(np.pi * t / t0_val)
            return 0.0

        curve_pulse = axes_pulse.plot(
            pulse_func,
            x_range=[0, 2.40],
            color=RED_SHOCK,
            stroke_width=3.2
        )

        area_pulse = axes_pulse.get_area(
            curve_pulse,
            x_range=[0, t0_val],
            color=RED_SHOCK,
            opacity=0.25
        )

        # Peak force indicator F0 = 180 kN at t = 0.80s
        peak_pt = axes_pulse.c2p(0.80, 180.0)
        peak_dot = Dot(point=peak_pt, radius=0.08, color=AMBER)
        peak_lbl = MathTex(r"F_0 = 180\text{ kN}", font_size=21, color=AMBER).next_to(peak_dot, UP, buff=0.15)
        peak_group = VGroup(peak_dot, peak_lbl)

        # Pulse duration bracket cleanly positioned below x-axis
        t0_y = axes_pulse.c2p(0, 0)[1] - 0.32
        t0_x1 = axes_pulse.c2p(0, 0)[0]
        t0_x2 = axes_pulse.c2p(t0_val, 0)[0]
        t0_arrow = DoubleArrow([t0_x1, t0_y, 0], [t0_x2, t0_y, 0], color=TEXT_WHITE, tip_length=0.14, stroke_width=1.8)
        t0_lbl = MathTex(r"t_0 = 1.60\text{ s}", font_size=19, color=TEXT_WHITE).next_to(t0_arrow, DOWN, buff=0.08)
        duration_group = VGroup(t0_arrow, t0_lbl)

        # 4.3 Dimensionless Ratio, Static Deflection & Dynamic Shock Regime Badge
        beta_tex = MathTex(
            r"\beta = \frac{t_0}{\tau_n} = \frac{1.60\text{ s}}{1.7717\text{ s}} = \mathbf{0.9031}",
            font_size=23, color=CYAN
        ).move_to([x_r, -1.35, 0])

        delta_st_tex = MathTex(
            r"\delta_{\text{st}} = \frac{F_0}{k} = \frac{180\text{ kN}}{3,919.7\text{ kN/m}} = \mathbf{45.92\text{ mm}}",
            font_size=22, color=SLATE
        ).move_to([x_r, -1.95, 0])

        regime_badge = make_badge(
            r"\beta \approx 0.90 \implies \mathbf{Dynamic\ Shock\ Regime\ (Severe\ Magnification)}",
            RED_SHOCK, width=7.00, height=0.55, font_size=20,
            fill_color=ManimColor("#1A0E0B"), stroke_width=2.2
        ).move_to([x_r, -2.55, 0])

        # ==================================================================
        # 5. ANIMATION CHOREOGRAPHY
        # ==================================================================
        # 0.0s - 0.8s: Title & Physical Tower
        self.play(
            Write(title),
            FadeIn(card_r, shift=UP * 0.15),
            FadeIn(ground_slab),
            FadeIn(col_group),
            FadeIn(tank_group),
            run_time=0.8
        )

        # 0.8s - 2.5s: Wind Blast Front strikes Tower while Axes reveal
        self.play(
            FadeIn(wind_front, shift=RIGHT * 0.75),
            Create(pulse_axes_group),
            run_time=1.7,
            rate_func=ease_out_cubic
        )

        # 2.5s - 3.2s: Hold for Cuepoint 1
        self.wait(0.7)  # Cuepoint 1 = 3.2s

        # 3.2s - 5.0s: Half-sine Pulse Curve plots with area fill
        self.play(
            Create(curve_pulse),
            FadeIn(area_pulse),
            FadeIn(peak_group, shift=UP * 0.10),
            Create(duration_group),
            card_r.animate.set_stroke(color=RED_SHOCK, width=2.4),
            run_time=1.8,
            rate_func=ease_out_cubic
        )

        # 5.0s - 6.2s: Static deflection & Pulse ratio beta reveal
        self.play(
            Write(beta_tex),
            Write(delta_st_tex),
            run_time=1.2
        )

        # 6.2s - 7.5s: Dynamic Shock Regime Badge illuminates
        self.play(
            FadeIn(regime_badge, shift=UP * 0.12),
            run_time=1.3
        )

        # 7.5s - 8.2s: Subtle pulse on Shock Regime Badge
        self.play(
            regime_badge.animate.scale(1.03),
            rate_func=there_and_back,
            run_time=0.7
        )

        # 8.2s - 9.0s: Final settle buffer
        self.wait(0.8)

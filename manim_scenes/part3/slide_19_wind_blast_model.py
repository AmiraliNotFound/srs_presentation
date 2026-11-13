"""
SLIDE-19: WindBlastModelScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 120 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Large presentation-grade mathematical typography (enlarged fonts & expanded cards)
  - Symmetrical 2-panel layout: Elevated Municipal Tower SDOF Model vs Wind-Blast Shock Pulse
  - Under 10-15 English words total on canvas (Strict 10-Word Rule)
  - Frame-Accurate Step Control:
      Step 1 (0.0s - 3.5s): Elevated Water Tower SDOF Model (35m hollow pedestal, Meff = 311.7 t, tau_n = 1.772s)
      Step 2 (3.5s - 8.5s): Dynamic Wind-Blast Pulse Profile (Half-sine pulse, F0 = 180 kN, t0 = 1.60s)
      Step 3 (8.5s - 14.2s): Dimensionless Pulse Ratio & Shock Regime (beta = 0.9031, Dynamic Shock Regime)
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine, there_and_back
import numpy as np


class WindBlastModelScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SLATE       = ManimColor("#B0B8C4")   # Tower structure, pedestal, axes, annotations
        CYAN        = ManimColor("#58C4DD")   # Column stiffness k, delta_st, pulse ratio beta
        AMBER       = ManimColor("#FFB703")   # Modal mass Meff, peak force F0, period tau_n
        RED_SHOCK   = ManimColor("#FF644E")   # Wind blast front, shock pulse, dynamic danger
        GREEN_PASS  = ManimColor("#83C167")   # Safe / verification indicators
        UT_BLUE     = ManimColor("#0097F1")   # Water reservoir, UT brand accent
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        WALL_STROKE = ManimColor("#3B4D63")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Municipal Tower Blast}",
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
        x_l = -3.55   # Left panel center (Elevated Tower SDOF Model)
        x_r = +3.55   # Right panel center (Wind-Blast Shock Pulse)
        card_w = 6.45
        card_h = 5.85
        card_y = -0.25

        # Background Cards for Structure
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
        # 4. LEFT PANEL: Elevated Municipal Tower SDOF Model
        # ==================================================================
        header_l = make_badge(
            r"\textbf{Elevated Water Tower}\text{ (SDOF Model)}",
            SLATE, width=5.90, height=0.52, font_size=20
        ).move_to([x_l, 2.24, 0])

        # 4.1 Ground Foundation Slab (y = -2.60 to -2.25)
        ground_slab = RoundedRectangle(
            corner_radius=0.08, width=5.50, height=0.45,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#131D2A"), fill_opacity=0.92
        ).move_to([x_l, -2.45, 0])

        ground_hatches = VGroup()
        for i in range(11):
            hx = (x_l - 2.50) + i * 0.50
            h_line = Line([hx - 0.15, -2.68, 0], [hx + 0.15, -2.45, 0], color=WALL_STROKE, stroke_width=1.8)
            ground_hatches.add(h_line)

        # 4.2 Reinforced Concrete Shaft (Cantilever Pedestal)
        # Height from ground slab top (y = -2.225) to tank base (y = 0.55)
        col_w = 0.70
        col_left = Line([x_l - col_w/2, -2.225, 0], [x_l - col_w/2, 0.55, 0], color=SLATE, stroke_width=2.8)
        col_right = Line([x_l + col_w/2, -2.225, 0], [x_l + col_w/2, 0.55, 0], color=SLATE, stroke_width=2.8)
        col_body = Rectangle(
            width=col_w, height=2.775,
            color=SLATE, stroke_width=0,
            fill_color=ManimColor("#1A2433"), fill_opacity=0.75
        ).move_to([x_l, -0.8375, 0])

        # Inner cavity representation (hollow tubular column)
        col_core = Rectangle(
            width=0.45, height=2.775,
            color=ManimColor("#0E1622"), stroke_width=1.2,
            fill_color=ManimColor("#0B0F19"), fill_opacity=0.95
        ).move_to([x_l, -0.8375, 0])

        column_assembly = VGroup(col_body, col_core, col_left, col_right)

        # Height Dimension Arrow (l = 35.0 m)
        dim_line = DoubleArrow([x_l - 1.25, -2.225, 0], [x_l - 1.25, 0.55, 0], color=CYAN, tip_length=0.18, stroke_width=2.0)
        dim_label = MathTex(r"l = 35.0\text{ m}", font_size=20, color=CYAN).next_to(dim_line, LEFT, buff=0.12)

        # 4.3 Elevated Spherical-Cylindrical Water Tank (y = 0.55 to 1.75)
        tank_base_y = 0.55
        tank_w = 1.90
        tank_cyl_h = 0.75
        tank_cyl = RoundedRectangle(
            corner_radius=0.10, width=tank_w, height=tank_cyl_h,
            color=SLATE, stroke_width=2.6,
            fill_color=UT_BLUE, fill_opacity=0.65
        ).move_to([x_l, tank_base_y + tank_cyl_h/2, 0])

        # Tank top dome (cap)
        tank_dome = Arc(
            radius=tank_w/2, start_angle=0, angle=PI,
            color=SLATE, stroke_width=2.6
        ).move_to([x_l, tank_base_y + tank_cyl_h + 0.22, 0])
        tank_dome_fill = Sector(
            radius=tank_w/2, start_angle=0, angle=PI,
            color=UT_BLUE, fill_opacity=0.65, stroke_width=0
        ).move_to([x_l, tank_base_y + tank_cyl_h + 0.22, 0])

        # Water level indicator line inside tank
        water_line = DashedLine([x_l - tank_w/2 + 0.10, 1.15, 0], [x_l + tank_w/2 - 0.10, 1.15, 0], color=TEXT_WHITE, stroke_width=1.8)
        water_label = MathTex(r"250\text{ kL Water}", font_size=18, color=TEXT_WHITE).move_to([x_l, 0.92, 0])

        tank_assembly = VGroup(tank_cyl, tank_dome_fill, tank_dome, water_line, water_label)

        # 4.4 Left Panel Mathematical Parameter Badges (Below Tower & Side)
        p1_mass = MathTex(
            r"M_{\text{eff}} = 311,653\text{ kg} \quad \left(M + \frac{33}{140}m_{\text{col}}\right)",
            font_size=21, color=AMBER
        ).move_to([x_l, -1.82, 0])

        p1_stiff = MathTex(
            r"k = \frac{3EI}{l^3} = 3,919.7\text{ kN/m}",
            font_size=22, color=CYAN
        ).move_to([x_l, -1.25, 0])

        p1_period = MathTex(
            r"\tau_n = \frac{2\pi}{\omega_n} = 1.7717\text{ s} \quad (\omega_n = 3.55\text{ rad/s})",
            font_size=21, color=TEXT_WHITE
        ).move_to([x_l, -0.68, 0])

        # ==================================================================
        # 5. RIGHT PANEL: Wind-Blast Shock Pulse & Dynamic Ratio
        # ==================================================================
        header_r = make_badge(
            r"\textbf{Wind-Blast Shock Pulse}\text{ (Half-Sine)}",
            RED_SHOCK, width=5.90, height=0.52, font_size=20
        ).move_to([x_r, 2.24, 0])

        # 5.1 Coordinate Axes for Shock Pulse F(t) vs t
        axes_pulse = Axes(
            x_range=[0, 2.40, 0.50],
            y_range=[0, 220, 50],
            x_length=5.00,
            y_length=2.50,
            axis_config={
                "color": SLATE,
                "stroke_width": 2.0,
                "include_ticks": True,
                "tick_size": 0.08,
            }
        ).move_to([x_r, 0.65, 0])

        x_lbl = MathTex(r"t\text{ (s)}", font_size=19, color=SLATE).next_to(axes_pulse.x_axis, RIGHT, buff=0.12)
        y_lbl = MathTex(r"F(t)\text{ (kN)}", font_size=19, color=SLATE).next_to(axes_pulse.y_axis, UP, buff=0.12)
        pulse_axes_group = VGroup(axes_pulse, x_lbl, y_lbl)

        # Pulse Function: Half-sine F0 * sin(pi * t / t0) for t <= 1.60s, 0 for t > 1.60s
        t0_val = 1.60
        f0_val = 180.0

        def pulse_func(t):
            if t <= t0_val:
                return f0_val * np.sin(np.pi * t / t0_val)
            return 0.0

        curve_pulse = axes_pulse.plot(
            pulse_func,
            x_range=[0, 2.30],
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
        peak_dot = Dot(point=peak_pt, radius=0.07, color=AMBER)
        peak_lbl = MathTex(r"F_0 = 180\text{ kN}", font_size=21, color=AMBER).next_to(peak_dot, UP, buff=0.10)
        peak_group = VGroup(peak_dot, peak_lbl)

        # Pulse duration bracket t0 = 1.60 s
        t0_pt1 = axes_pulse.c2p(0, -18)
        t0_pt2 = axes_pulse.c2p(t0_val, -18)
        t0_arrow = DoubleArrow(t0_pt1, t0_pt2, color=TEXT_WHITE, tip_length=0.14, stroke_width=1.8)
        t0_lbl = MathTex(r"t_0 = 1.60\text{ s}", font_size=19, color=TEXT_WHITE).next_to(t0_arrow, DOWN, buff=0.08)
        duration_group = VGroup(t0_arrow, t0_lbl)

        # 5.2 Step 3 Equations & Dynamic Shock Regime Badge
        r_row1 = MathTex(
            r"\beta = \frac{t_0}{\tau_n} = \frac{1.60\text{ s}}{1.7717\text{ s}} = \mathbf{0.9031}",
            font_size=24, color=CYAN
        ).move_to([x_r, -1.05, 0])

        r_row2 = MathTex(
            r"\delta_{\text{st}} = \frac{F_0}{k} = \frac{180,000\text{ N}}{3,919.7\text{ kN/m}} = \mathbf{45.92\text{ mm}}",
            font_size=21, color=SLATE
        ).move_to([x_r, -1.55, 0])

        regime_badge = make_badge(
            r"\beta \approx 0.90 \implies \mathbf{Dynamic\ Shock\ Regime}",
            RED_SHOCK, width=5.90, height=0.56, font_size=22,
            fill_color=ManimColor("#1A0E0B"), stroke_width=2.4
        ).move_to([x_r, -2.18, 0])

        regime_sub = MathTex(
            r"t_0 \approx \tau_n \implies \text{Severe Dynamic Magnification}",
            font_size=19, color=AMBER
        ).move_to([x_r, -2.70, 0])

        # Wind Shock Wave Visual Front (striking the tower at Cuepoint 1)
        wind_arrows = VGroup()
        for dy in [-0.25, 0.00, 0.25]:
            w_arr = Arrow(
                start=[x_l - 2.80, 1.15 + dy, 0],
                end=[x_l - 1.10, 1.15 + dy, 0],
                color=RED_SHOCK,
                stroke_width=3.2,
                tip_length=0.22,
                buff=0
            )
            wind_arrows.add(w_arr)
        wind_lbl = Tex(r"\textbf{Wind Gust}", font_size=19, color=RED_SHOCK).next_to(wind_arrows, UP, buff=0.08)
        wind_blast_front = VGroup(wind_arrows, wind_lbl)

        # ==================================================================
        # ANIMATION CHOREOGRAPHY & FRAME-ACCURATE TIMESTAMPS
        # ==================================================================

        # --- STEP 1: Elevated Water Tower SDOF Model (0.0s - 3.5s) ---
        # 0.0s - 0.7s: Title & Background Cards appear
        self.play(
            Write(title),
            FadeIn(card_left, shift=UP * 0.15),
            FadeIn(card_right, shift=UP * 0.15),
            run_time=0.7
        )

        # 0.7s - 2.3s: Left Panel Assembly (Ground, Column, Tank, Parameters)
        self.play(
            FadeIn(header_l),
            FadeIn(ground_slab),
            Create(ground_hatches),
            Create(column_assembly),
            FadeIn(tank_assembly),
            Create(dim_line),
            Write(dim_label),
            run_time=1.6,
            rate_func=ease_out_cubic
        )

        # 2.3s - 3.2s: Tower Dynamic Parameter Badges Reveal
        self.play(
            Write(p1_mass),
            Write(p1_stiff),
            Write(p1_period),
            run_time=0.9
        )

        # 3.2s - 3.5s: Hold for Cuepoint 1
        self.wait(0.3)  # Exact Cuepoint 1 = 3.5s

        # --- STEP 2: Wind-Blast Shock Pulse Profile (3.5s - 8.5s) ---
        # 3.5s - 4.3s: Right Panel Header & Axes Reveal
        self.play(
            card_right.animate.set_stroke(color=RED_SHOCK, width=2.4),
            FadeIn(header_r, shift=UP * 0.12),
            Create(pulse_axes_group),
            run_time=0.8
        )

        # 4.3s - 6.2s: Wind Blast Front strikes Tower while Pulse Curve Plots
        self.play(
            FadeIn(wind_blast_front, shift=RIGHT * 0.80),
            Create(curve_pulse),
            FadeIn(area_pulse),
            run_time=1.9,
            rate_func=ease_out_cubic
        )

        # 6.2s - 7.5s: Peak Force & Pulse Duration Indicators Reveal
        self.play(
            FadeIn(peak_group, shift=UP * 0.12),
            Create(duration_group),
            run_time=1.3
        )

        # 7.5s - 8.5s: Hold for Cuepoint 2
        self.wait(1.0)  # Exact Cuepoint 2 = 8.5s

        # --- STEP 3: Dimensionless Ratio & Shock Regime (8.5s - 14.2s) ---
        # 8.5s - 10.4s: Calculation of beta and delta_st writes smoothly
        self.play(
            Write(r_row1),
            Write(r_row2),
            run_time=1.9,
            rate_func=ease_out_cubic
        )

        # 10.4s - 12.2s: Dynamic Shock Regime Badge and Hazard Note Illuminate
        self.play(
            FadeIn(regime_badge, shift=UP * 0.15),
            FadeIn(regime_sub, shift=UP * 0.10),
            run_time=1.8
        )

        # 12.2s - 13.5s: Subtle Dynamic Breathing Pulse on Shock Regime Badge
        self.play(
            regime_badge.animate.scale(1.04),
            card_right.animate.set_stroke(color=AMBER, width=2.6),
            rate_func=there_and_back,
            run_time=1.3
        )

        # 13.5s - 14.2s: Hold for Cuepoint 3
        self.wait(0.7)  # Exact Cuepoint 3 = 14.2s

        # 14.2s - 15.0s: Settle and loop buffer
        self.wait(0.8)

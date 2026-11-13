"""
SLIDE-20: ECUIsolatorScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 120 s

3Blue1Brown Fullscreen Aesthetic (Refined Multi-Image Edition — 6 Discrete Visual States):
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars
  - Wider card geometry (card_w = 6.75) for spacious, edge-to-edge layout
  - Significantly enlarged mathematical typography (23-32 pt fonts)
  - Ultra-low text density per step (1 key equation + 1 key badge)
  - Dedicated engineering graphic/diagram on every single step:
      Step 1: Full Transmissibility Curve T_d(r) with colored isolation zone
      Step 2: Frequency Spectral Tuning & Softening Gauge (omega_engine -> omega_n,iso)
      Step 3: Equivalent SDOF Restoring Stiffness Mechanics Model (m_total, k_iso)
      Step 4: 4-Corner Bushing Sizing Top-Down Footprint Diagram (k_each = k_iso / 4)
      Step 5: SDOF Viscous Dashpot Damping Model Diagram (c_iso, c_each, zeta = 1%)
      Step 6: Dual Waveform Oscilloscope Comparison Chart + 90% Certified Badge
  - Frame-Accurate Step Control:
      Step 1 (0.0s - 3.5s): Isolation Threshold (r > sqrt(2), Td <= 0.10 -> r >= sqrt(11) = 3.32)
      Step 2 (3.5s - 6.5s): Frequency Softening (omega_n,iso = 94.7 rad/s, fn = 15.1 Hz)
      Step 3 (6.5s - 9.5s): Total Stiffness Sizing (k_iso = 24.66 kN/m)
      Step 4 (9.5s - 12.5s): 4-Corner Bushings (k_each = 6.17 kN/m each)
      Step 5 (12.5s - 15.5s): Damping Sizing (c_iso = 5.21 N s/m, c_each = 1.30 N s/m)
      Step 6 (15.5s - 19.0s): Dynamic Attenuation Waveforms & 90% Certification
"""

from manim import *
import numpy as np


class ECUIsolatorScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SLATE       = ManimColor("#B0B8C4")   # Enclosure, clamps, axes, secondary notes
        CYAN        = ManimColor("#58C4DD")   # Isolator springs, stiffness k_iso, PCB
        AMBER       = ManimColor("#FFB703")   # Engine speed 3000 rpm, frequency ratio r, input
        RED_SHOCK   = ManimColor("#FF644E")   # Resonance danger zone (r < sqrt(2))
        GREEN_PASS  = ManimColor("#83C167")   # Isolation zone (r > sqrt(2)), 90% certified safe
        UT_BLUE     = ManimColor("#0097F1")   # Isolator dampers c_iso, UT brand accent
        TEXT_WHITE  = ManimColor("#FFFFFF")
        WALL_STROKE = ManimColor("#3B4D63")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Base Isolator Design}",
            font_size=42,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # Helper function for sleek rounded badges with zero text overflow
        def make_badge(tex_str, color, width, height, font_size=23, fill_color=BG_DARK, stroke_width=2.4):
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

        # Helper function for realistic engineering springs
        def make_spring(x0, y_start, y_end, num_coils=6, width=0.30, color=CYAN, stroke_width=2.4):
            h = y_end - y_start
            lead = 0.10 * h
            y1 = y_start + lead
            y2 = y_end - lead
            coil_h = (y2 - y1) / (2.0 * num_coils)
            pts = [[x0, y_start, 0], [x0, y1, 0]]
            for i in range(2 * num_coils):
                y_c = y1 + (i + 0.5) * coil_h
                sign = 1.0 if (i % 2 == 0) else -1.0
                pts.append([x0 + sign * width / 2.0, y_c, 0])
            pts.append([x0, y2, 0])
            pts.append([x0, y_end, 0])
            return VMobject().set_points_as_corners(pts).set_stroke(color=color, width=stroke_width)

        # Helper function for realistic engineering dashpots
        def make_dashpot(x0, y_start, y_end, width=0.24, color=UT_BLUE, stroke_width=2.0):
            h = y_end - y_start
            cyl_bot = y_start + 0.08 * h
            cyl_top = cyl_bot + 0.48 * h
            cyl_pts = [
                [x0 - width / 2.0, cyl_top, 0],
                [x0 - width / 2.0, cyl_bot, 0],
                [x0 + width / 2.0, cyl_bot, 0],
                [x0 + width / 2.0, cyl_top, 0]
            ]
            cylinder = VMobject().set_points_as_corners(cyl_pts).set_stroke(color=color, width=stroke_width)
            cyl_stem = Line([x0, y_start, 0], [x0, cyl_bot, 0], color=color, stroke_width=stroke_width)
            piston_head_y = cyl_bot + 0.52 * (cyl_top - cyl_bot)
            piston_stem = Line([x0, y_end, 0], [x0, piston_head_y, 0], color=color, stroke_width=stroke_width)
            piston_plate = Line(
                [x0 - width * 0.40, piston_head_y, 0],
                [x0 + width * 0.40, piston_head_y, 0],
                color=color, stroke_width=stroke_width + 0.6
            )
            return VGroup(cylinder, cyl_stem, piston_stem, piston_plate)

        # ==================================================================
        # 3. COORDINATE LAYOUT: Left Panel vs Right Panel (Wider Boxes!)
        # ==================================================================
        x_l = -3.48   # Left panel center
        x_r = +3.48   # Right panel center
        card_w = 6.75 # Expanded width for clean margins
        card_h = 5.95
        card_y = -0.22

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
        # 4. LEFT PANEL: Physical Base-Isolated ECU Mechanical Assembly
        # ==================================================================
        header_l = make_badge(
            r"\textbf{Base-Isolated ECU Chassis}",
            SLATE, width=6.25, height=0.48, font_size=20
        ).move_to([x_l, 2.38, 0])

        # 4.1 Aluminum ECU Chassis Enclosure
        y_chassis_center = 1.15
        chassis_w = 5.75
        chassis_h = 1.95
        chassis_box = RoundedRectangle(
            corner_radius=0.12, width=chassis_w, height=chassis_h,
            color=SLATE, stroke_width=2.2,
            fill_color=ManimColor("#090E17"), fill_opacity=0.96
        ).move_to([x_l, y_chassis_center, 0])

        chassis_mass_tag = MathTex(
            r"m_{\text{total}} = m_c + m_{\text{PCB}} = 2.75\text{ kg}",
            font_size=23, color=TEXT_WHITE
        ).move_to([x_l, y_chassis_center + 0.65, 0])

        # 4.2 Internal Clamped PCB + MCU Microchip
        y_pcb = y_chassis_center - 0.05
        t_pcb = 0.12

        clamp_l = Rectangle(width=0.35, height=0.95, color=SLATE, stroke_width=1.8, fill_color=ManimColor("#1A2436"), fill_opacity=1.0).move_to([x_l - 2.15, y_pcb, 0])
        clamp_r = Rectangle(width=0.35, height=0.95, color=SLATE, stroke_width=1.8, fill_color=ManimColor("#1A2436"), fill_opacity=1.0).move_to([x_l + 2.15, y_pcb, 0])

        pcb_rect = Rectangle(
            width=3.95, height=t_pcb, color=CYAN, stroke_width=2.2,
            fill_color=ManimColor("#102838"), fill_opacity=0.98
        ).move_to([x_l, y_pcb, 0])

        chip_w = 0.90
        chip_h = 0.28
        mcu_body = RoundedRectangle(
            corner_radius=0.04, width=chip_w, height=chip_h,
            color=SLATE, stroke_width=1.8,
            fill_color=ManimColor("#1C2533"), fill_opacity=1.0
        ).move_to([x_l, y_pcb + t_pcb / 2.0 + chip_h / 2.0 + 0.02, 0])
        mcu_label = Tex(r"\textbf{MCU}", font_size=17, color=TEXT_WHITE).move_to(mcu_body.get_center())

        solder_l = Dot([x_l - chip_w / 2.0 - 0.08, y_pcb + t_pcb / 2.0 + 0.02, 0], radius=0.06, color=GREEN_PASS)
        solder_r = Dot([x_l + chip_w / 2.0 + 0.08, y_pcb + t_pcb / 2.0 + 0.02, 0], radius=0.06, color=GREEN_PASS)
        safe_halo_l = Circle(radius=0.11, color=GREEN_PASS, stroke_width=1.8).move_to(solder_l.get_center())
        safe_halo_r = Circle(radius=0.11, color=GREEN_PASS, stroke_width=1.8).move_to(solder_r.get_center())

        smd1 = Rectangle(width=0.45, height=0.16, color=SLATE, stroke_width=1.3, fill_color=ManimColor("#1A202C"), fill_opacity=1.0).move_to([x_l - 1.10, y_pcb + t_pcb / 2.0 + 0.08, 0])
        smd2 = Rectangle(width=0.45, height=0.16, color=SLATE, stroke_width=1.3, fill_color=ManimColor("#1A202C"), fill_opacity=1.0).move_to([x_l + 1.10, y_pcb + t_pcb / 2.0 + 0.08, 0])

        tag_solder_safe_left = MathTex(
            r"\mathbf{Solder\ Joints\ Safe\ (\sigma \ll \sigma_{\text{allow}})}",
            font_size=18, color=GREEN_PASS
        ).move_to([x_l, y_chassis_center - 0.62, 0])

        pcb_group = VGroup(
            clamp_l, clamp_r, pcb_rect, mcu_body, mcu_label,
            solder_l, solder_r, safe_halo_l, safe_halo_r, smd1, smd2, tag_solder_safe_left
        )

        # 4.3 Engine Bay Foundation Slab
        y_slab = -2.80
        engine_slab = RoundedRectangle(
            corner_radius=0.08, width=6.10, height=0.46,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#121A28"), fill_opacity=1.0
        ).move_to([x_l, y_slab, 0])

        engine_hatches = VGroup(*[
            Line([x, y_slab - 0.23, 0], [x - 0.16, y_slab - 0.38, 0], color=WALL_STROKE, stroke_width=1.5)
            for x in np.linspace(x_l - 2.80, x_l + 2.80, 18)
        ])

        engine_lbl = Tex(
            r"\textbf{Engine Bay Foundation} (3000 rpm)",
            font_size=18, color=AMBER
        ).move_to([x_l, y_slab, 0])

        engine_bay_group = VGroup(engine_slab, engine_hatches, engine_lbl)

        # 4.4 Four Base Isolator Mounts (Clean Flanks, Zero Overlap!)
        y_mount_bot = y_slab + 0.23   # -2.57
        y_mount_top = y_chassis_center - chassis_h / 2.0  # +0.175
        x_mount_l = x_l - 2.05
        x_mount_r = x_l + 2.05

        pad_w = 0.95
        pad_h = 0.10
        top_pad_l = Rectangle(width=pad_w, height=pad_h, color=SLATE, stroke_width=1.8, fill_color=ManimColor("#1E293B"), fill_opacity=1.0).move_to([x_mount_l, y_mount_top - pad_h / 2.0, 0])
        bot_pad_l = Rectangle(width=pad_w, height=pad_h, color=SLATE, stroke_width=1.8, fill_color=ManimColor("#1E293B"), fill_opacity=1.0).move_to([x_mount_l, y_mount_bot + pad_h / 2.0, 0])
        top_pad_r = Rectangle(width=pad_w, height=pad_h, color=SLATE, stroke_width=1.8, fill_color=ManimColor("#1E293B"), fill_opacity=1.0).move_to([x_mount_r, y_mount_top - pad_h / 2.0, 0])
        bot_pad_r = Rectangle(width=pad_w, height=pad_h, color=SLATE, stroke_width=1.8, fill_color=ManimColor("#1E293B"), fill_opacity=1.0).move_to([x_mount_r, y_mount_bot + pad_h / 2.0, 0])
        pads_group = VGroup(top_pad_l, bot_pad_l, top_pad_r, bot_pad_r)

        dx_sp = 0.22
        y_sp_bot = y_mount_bot + pad_h
        y_sp_top = y_mount_top - pad_h

        spring_l = make_spring(x_mount_l - dx_sp, y_sp_bot, y_sp_top, num_coils=6, width=0.28, color=CYAN, stroke_width=2.4)
        dashpot_l = make_dashpot(x_mount_l + dx_sp, y_sp_bot, y_sp_top, width=0.22, color=UT_BLUE, stroke_width=2.0)

        spring_r = make_spring(x_mount_r - dx_sp, y_sp_bot, y_sp_top, num_coils=6, width=0.28, color=CYAN, stroke_width=2.4)
        dashpot_r = make_dashpot(x_mount_r + dx_sp, y_sp_bot, y_sp_top, width=0.22, color=UT_BLUE, stroke_width=2.0)

        isolator_mounts_group = VGroup(pads_group, spring_l, dashpot_l, spring_r, dashpot_r)

        # Step 6 Dynamic Attenuation Benefit in Clean Central Corridor (Zero Overlap!)
        arrow_base_in = Arrow([x_l, -2.42, 0], [x_l, -1.90, 0], color=AMBER, stroke_width=2.4, tip_length=0.12)
        lbl_base_in = MathTex(r"\mathbf{Input\ } Y_0", font_size=18, color=AMBER).next_to(arrow_base_in, RIGHT, buff=0.12)

        arrow_chassis_out = Arrow([x_l, -0.90, 0], [x_l, -0.58, 0], color=GREEN_PASS, stroke_width=2.4, tip_length=0.10)
        lbl_chassis_out = MathTex(r"X_0 \le 0.10 Y_0", font_size=18, color=GREEN_PASS).next_to(arrow_chassis_out, RIGHT, buff=0.12)

        badge_shielded_left = make_badge(
            r"\mathbf{90\%\ VIBRATION\ SHIELDED}",
            GREEN_PASS, width=3.30, height=0.50, font_size=18, stroke_width=2.4
        ).move_to([x_l, -1.40, 0])

        step6_center_demo = VGroup(arrow_base_in, lbl_base_in, arrow_chassis_out, lbl_chassis_out, badge_shielded_left)

        left_base_group = VGroup(
            card_left, header_l, engine_bay_group, chassis_box,
            chassis_mass_tag, pcb_group, isolator_mounts_group
        )

        # ==================================================================
        # 5. RIGHT PANEL: STEP 1 (Transmissibility Curve & Isolation Boundary)
        # ==================================================================
        header_r1 = make_badge(
            r"\textbf{Displacement Transmissibility } T_d(r)",
            SLATE, width=6.25, height=0.48, font_size=20
        ).move_to([x_r, 2.38, 0])

        # Large, high-resolution Transmissibility Plot
        axes_td = Axes(
            x_range=[0, 4.0, 1.0],
            y_range=[0, 4.2, 1.0],
            x_length=5.20,
            y_length=2.40,
            axis_config={"color": SLATE, "stroke_width": 1.8},
            tips=False
        ).move_to([x_r + 0.12, 0.72, 0])

        x_lbl = MathTex(r"r = \omega / \omega_n", font_size=19, color=SLATE).next_to(axes_td.x_axis, DOWN, buff=0.10).align_to(axes_td.x_axis, RIGHT)
        y_lbl = MathTex(r"T_d", font_size=19, color=SLATE).next_to(axes_td.y_axis, LEFT, buff=0.10).align_to(axes_td.y_axis, UP)

        res_line = DashedLine(
            axes_td.c2p(1.0, 0), axes_td.c2p(1.0, 4.0),
            color=RED_SHOCK, stroke_width=1.8, dash_length=0.07
        )
        res_tag = MathTex(r"r = 1.0", font_size=15, color=RED_SHOCK).next_to(res_line, UP, buff=0.04)

        r_iso_bound = np.sqrt(2.0)
        iso_bound_line = DashedLine(
            axes_td.c2p(r_iso_bound, 0), axes_td.c2p(r_iso_bound, 2.2),
            color=AMBER, stroke_width=1.8, dash_length=0.07
        )
        iso_bound_tick = MathTex(r"\sqrt{2}", font_size=17, color=AMBER).next_to(axes_td.c2p(r_iso_bound, 0), DOWN, buff=0.08)
        iso_bound_tag = MathTex(r"\mathbf{Isolation\ Boundary}", font_size=14, color=AMBER).next_to(axes_td.c2p(r_iso_bound, 2.2), UP, buff=0.04)

        line_td_one = DashedLine(
            axes_td.c2p(0, 1.0), axes_td.c2p(3.9, 1.0),
            color=SLATE, stroke_width=1.4, dash_length=0.06
        )
        tick_td_one = MathTex(r"1.0", font_size=16, color=SLATE).next_to(axes_td.c2p(0, 1.0), LEFT, buff=0.06)

        curve_amp_left = axes_td.plot(
            lambda r: 1.0 / abs(1.0 - r**2),
            x_range=[0.0, 0.82, 0.02],
            color=CYAN, stroke_width=2.5
        )
        curve_amp_mid = axes_td.plot(
            lambda r: 1.0 / abs(1.0 - r**2),
            x_range=[1.20, r_iso_bound, 0.02],
            color=CYAN, stroke_width=2.5
        )
        curve_isolation = axes_td.plot(
            lambda r: 1.0 / abs(1.0 - r**2),
            x_range=[r_iso_bound, 3.85, 0.02],
            color=GREEN_PASS, stroke_width=3.4
        )

        r_target = np.sqrt(11.0)
        td_target = 0.10
        target_dot = Dot(point=axes_td.c2p(r_target, td_target), radius=0.09, color=AMBER)
        proj_v_target = DashedLine(axes_td.c2p(r_target, 0), axes_td.c2p(r_target, td_target), color=AMBER, stroke_width=1.6, dash_length=0.06)
        proj_h_target = DashedLine(axes_td.c2p(0, td_target), axes_td.c2p(r_target, td_target), color=GREEN_PASS, stroke_width=1.6, dash_length=0.06)
        tick_r_target = MathTex(r"\sqrt{11}", font_size=17, color=AMBER).next_to(axes_td.c2p(r_target, 0), DOWN, buff=0.08)
        tag_target_pt = MathTex(r"T_d = 0.10", font_size=17, color=GREEN_PASS).next_to(target_dot, UR, buff=0.08)

        zone_amp_lbl = MathTex(r"\mathbf{Amplification}", font_size=16, color=RED_SHOCK).move_to(axes_td.c2p(0.55, 3.2))
        zone_iso_lbl = MathTex(r"\mathbf{Isolation\ (T_d < 1)}", font_size=16, color=GREEN_PASS).move_to(axes_td.c2p(2.70, 1.8))

        plot_step1_group = VGroup(
            axes_td, x_lbl, y_lbl, res_line, res_tag,
            iso_bound_line, iso_bound_tick, iso_bound_tag,
            line_td_one, tick_td_one, curve_amp_left, curve_amp_mid,
            curve_isolation, zone_amp_lbl, zone_iso_lbl,
            proj_v_target, proj_h_target, target_dot, tick_r_target, tag_target_pt
        )

        # Large Clean Condition Formula (Zero Missing Glyph Glitches)
        eq_condition = MathTex(
            r"T_d \le 0.10 \implies r \ge \sqrt{11} \approx 3.32",
            font_size=28, color=TEXT_WHITE
        ).move_to([x_r, -1.15, 0])

        badge_criterion = make_badge(
            r"\mathbf{ISOLATION\ REGION:}\quad r > \sqrt{2} \approx 1.41",
            AMBER, width=6.25, height=0.68, font_size=23, stroke_width=2.6
        ).move_to([x_r, -2.00, 0])

        step1_right_group = VGroup(
            header_r1, plot_step1_group, eq_condition, badge_criterion
        )

        # ==================================================================
        # 6. RIGHT PANEL: STEP 2 (Frequency Spectral Softening Diagram)
        # ==================================================================
        header_r2 = make_badge(
            r"\textbf{Natural Frequency Tuning}",
            AMBER, width=6.25, height=0.48, font_size=20
        ).move_to([x_r, 2.38, 0])

        # Dedicated Diagram 2: Frequency Spectral Comparison Gauge
        y_spec = 0.72
        spec_box = RoundedRectangle(
            corner_radius=0.12, width=5.60, height=2.20,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#0B1320"), fill_opacity=0.96
        ).move_to([x_r, y_spec, 0])

        # Spectral axis
        x_spec_start = x_r - 2.40
        x_spec_end   = x_r + 2.40
        spec_axis = Line([x_spec_start, y_spec - 0.45, 0], [x_spec_end, y_spec - 0.45, 0], color=SLATE, stroke_width=2.0)
        spec_lbl = MathTex(r"\text{Frequency Band (rad/s)}", font_size=16, color=SLATE).next_to(spec_axis, DOWN, buff=0.12)

        # Shaded Isolation Region on Spectral Axis
        x_iso_div = x_spec_start + (x_spec_end - x_spec_start) * 0.45
        iso_band = Rectangle(
            width=(x_iso_div - x_spec_start), height=0.20,
            color=GREEN_PASS, fill_color=GREEN_PASS, fill_opacity=0.25, stroke_width=0
        ).move_to([(x_spec_start + x_iso_div) / 2.0, y_spec - 0.45, 0])
        iso_band_lbl = MathTex(r"\mathbf{Safe\ Isolation\ Band}", font_size=14, color=GREEN_PASS).move_to([(x_spec_start + x_iso_div) / 2.0, y_spec - 0.75, 0])

        # Engine excitation frequency marker (Amber)
        x_engine_pt = x_r + 1.80
        dot_engine = Dot([x_engine_pt, y_spec - 0.45, 0], radius=0.12, color=AMBER)
        stem_engine = Line([x_engine_pt, y_spec - 0.45, 0], [x_engine_pt, y_spec + 0.45, 0], color=AMBER, stroke_width=2.4)
        lbl_engine_spec = MathTex(
            r"\omega_{\text{engine}} = \mathbf{314.16\text{ rad/s}}\ (50\text{ Hz})",
            font_size=17, color=AMBER
        ).next_to(stem_engine, UP, buff=0.08)

        # Target isolated frequency marker (Cyan)
        x_iso_pt = x_r - 1.50
        dot_iso = Dot([x_iso_pt, y_spec - 0.45, 0], radius=0.12, color=CYAN)
        stem_iso = Line([x_iso_pt, y_spec - 0.45, 0], [x_iso_pt, y_spec + 0.45, 0], color=CYAN, stroke_width=2.4)
        lbl_iso_spec = MathTex(
            r"\omega_{n,\text{iso}} = \mathbf{94.70\text{ rad/s}}\ (15.1\text{ Hz})",
            font_size=17, color=CYAN
        ).next_to(stem_iso, UP, buff=0.08)

        # Curved Shift Arrow (Softening: divide by r = 3.32)
        shift_arc = CurvedArrow(
            [x_engine_pt - 0.20, y_spec + 0.25, 0],
            [x_iso_pt + 0.20, y_spec + 0.25, 0],
            radius=-2.2, color=AMBER, stroke_width=2.4
        )
        shift_txt = MathTex(r"\div r = 3.32\ \text{(Softening)}", font_size=15, color=AMBER).next_to(shift_arc, UP, buff=0.05)

        spec_group = VGroup(
            spec_box, spec_axis, spec_lbl, iso_band, iso_band_lbl,
            dot_engine, stem_engine, lbl_engine_spec,
            dot_iso, stem_iso, lbl_iso_spec, shift_arc, shift_txt
        )

        eq_wn_big = MathTex(
            r"\omega_{n,\text{iso}} = \frac{\omega_{\text{engine}}}{r} = \frac{314.16}{3.318} = \mathbf{94.70\text{ rad/s}} \quad (15.1\text{ Hz})",
            font_size=25, color=AMBER
        ).move_to([x_r, -1.15, 0])

        badge_softening = make_badge(
            r"\mathbf{FREQUENCY\ SOFTENING:}\quad \omega_{n,\text{iso}} \ll \omega_{\text{engine}}",
            AMBER, width=6.25, height=0.68, font_size=22, stroke_width=2.6
        ).move_to([x_r, -2.00, 0])

        step2_right_group = VGroup(
            header_r2, spec_group, eq_wn_big, badge_softening
        )

        # ==================================================================
        # 7. RIGHT PANEL: STEP 3 (Base Isolator Total Stiffness Mechanics)
        # ==================================================================
        header_r3 = make_badge(
            r"\textbf{System Stiffness Sizing}",
            CYAN, width=6.25, height=0.48, font_size=20
        ).move_to([x_r, 2.38, 0])

        # Dedicated Diagram 3: Total SDOF Restoring Stiffness Model
        y_sdof3 = 0.72
        sdof_box3 = RoundedRectangle(
            corner_radius=0.12, width=5.60, height=2.20,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#0B1320"), fill_opacity=0.96
        ).move_to([x_r, y_sdof3, 0])

        mass_block3 = RoundedRectangle(
            corner_radius=0.08, width=3.80, height=0.55,
            color=SLATE, stroke_width=2.0,
            fill_color=ManimColor("#1A2436"), fill_opacity=1.0
        ).move_to([x_r, y_sdof3 + 0.58, 0])
        mass_lbl3 = MathTex(r"m_{\text{total}} = 2.75\text{ kg}\ (m_c + m_{\text{PCB}})", font_size=20, color=TEXT_WHITE).move_to(mass_block3.get_center())

        base_slab3 = RoundedRectangle(
            corner_radius=0.06, width=3.80, height=0.28,
            color=WALL_STROKE, stroke_width=1.8,
            fill_color=ManimColor("#121A28"), fill_opacity=1.0
        ).move_to([x_r, y_sdof3 - 0.72, 0])
        base_lbl3 = Tex(r"\textbf{Vibrating Engine Base}", font_size=16, color=AMBER).move_to(base_slab3.get_center())

        spring_center3 = make_spring(x_r, y_sdof3 - 0.58, y_sdof3 + 0.30, num_coils=5, width=0.40, color=CYAN, stroke_width=2.8)
        k_tag3 = MathTex(r"k_{\text{iso}}", font_size=24, color=CYAN).next_to(spring_center3, RIGHT, buff=0.25)
        force_tag3 = MathTex(r"F_s = k_{\text{iso}}(x - y)", font_size=18, color=CYAN).next_to(spring_center3, LEFT, buff=0.25)

        sdof_stiff_group = VGroup(
            sdof_box3, mass_block3, mass_lbl3, base_slab3, base_lbl3,
            spring_center3, k_tag3, force_tag3
        )

        eq_k_total_big = MathTex(
            r"k_{\text{iso}} = m_{\text{total}} \omega_{n,\text{iso}}^2 = (2.75)(94.70)^2 = \mathbf{24.66\text{ kN/m}}",
            font_size=25, color=CYAN
        ).move_to([x_r, -1.15, 0])

        badge_stiff_result = make_badge(
            r"\mathbf{TOTAL\ STIFFNESS:}\quad k_{\text{iso}} = \mathbf{24.66\text{ kN/m}}",
            CYAN, width=6.25, height=0.68, font_size=23, stroke_width=2.8
        ).move_to([x_r, -2.00, 0])

        step3_right_group = VGroup(
            header_r3, sdof_stiff_group, eq_k_total_big, badge_stiff_result
        )

        # ==================================================================
        # 8. RIGHT PANEL: STEP 4 (4-Corner Bushing Sizing Footprint Diagram)
        # ==================================================================
        header_r4 = make_badge(
            r"\textbf{Corner Bushing Stiffness Sizing}",
            CYAN, width=6.25, height=0.48, font_size=20
        ).move_to([x_r, 2.38, 0])

        # Dedicated Diagram 4: Top-Down Chassis Mounting Footprint
        y_foot4 = 0.72
        foot_box4 = RoundedRectangle(
            corner_radius=0.12, width=5.60, height=2.20,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#0B1320"), fill_opacity=0.96
        ).move_to([x_r, y_foot4, 0])

        # Chassis outline in footprint
        plate_w4 = 4.80
        plate_h4 = 1.65
        plate_rect4 = RoundedRectangle(
            corner_radius=0.10, width=plate_w4, height=plate_h4,
            color=SLATE, stroke_width=1.8,
            fill_color=ManimColor("#131D2E"), fill_opacity=0.96
        ).move_to([x_r, y_foot4, 0])

        plate_lbl4 = Tex(r"\textbf{ECU Chassis Mounting Footprint}", font_size=19, color=TEXT_WHITE).move_to([x_r, y_foot4 + 0.32, 0])

        dx_b4 = plate_w4 / 2.0 - 0.45
        dy_b4 = plate_h4 / 2.0 - 0.35
        bushings = []
        for sx in [-1, 1]:
            for sy in [-1, 1]:
                pt = [x_r + sx * dx_b4, y_foot4 + sy * dy_b4, 0]
                dot_b = Dot(pt, radius=0.14, color=CYAN)
                halo_b = Circle(radius=0.22, color=CYAN, stroke_width=2.0).move_to(pt)
                bushings.extend([dot_b, halo_b])

        lbl_corner_bush = MathTex(
            r"\mathbf{Symmetric\ Bushings:}\quad k_{\text{each}} = \frac{k_{\text{iso}}}{4}",
            font_size=19, color=CYAN
        ).move_to([x_r, y_foot4 - 0.32, 0])

        footprint_group4 = VGroup(
            foot_box4, plate_rect4, plate_lbl4,
            *bushings, lbl_corner_bush
        )

        eq_k_corner_big = MathTex(
            r"k_{\text{each}} = \frac{k_{\text{iso}}}{4} = \frac{24.66\text{ kN/m}}{4} = \mathbf{6.17\text{ kN/m}}",
            font_size=27, color=CYAN
        ).move_to([x_r, -1.15, 0])

        badge_bushing_result = make_badge(
            r"\mathbf{4\ CORNER\ BUSHINGS:}\quad \mathbf{6.17\text{ kN/m\ each}}",
            CYAN, width=6.25, height=0.68, font_size=23, stroke_width=2.8
        ).move_to([x_r, -2.00, 0])

        step4_right_group = VGroup(
            header_r4, footprint_group4, eq_k_corner_big, badge_bushing_result
        )

        # ==================================================================
        # 9. RIGHT PANEL: STEP 5 (Isolator Damping Sizing & Dashpot Model)
        # ==================================================================
        header_r5 = make_badge(
            r"\textbf{Isolator Damping Sizing}",
            UT_BLUE, width=6.25, height=0.48, font_size=20
        ).move_to([x_r, 2.38, 0])

        # Dedicated Diagram 5: SDOF Spring-Dashpot Dissipation Model
        y_sdof5 = 0.72
        sdof_frame5 = RoundedRectangle(
            corner_radius=0.12, width=5.60, height=2.20,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#0B1320"), fill_opacity=0.96
        ).move_to([x_r, y_sdof5, 0])

        mass_block5 = RoundedRectangle(
            corner_radius=0.08, width=3.80, height=0.50,
            color=SLATE, stroke_width=2.0,
            fill_color=ManimColor("#1A2436"), fill_opacity=1.0
        ).move_to([x_r, y_sdof5 + 0.58, 0])
        mass_lbl5 = MathTex(r"m_{\text{total}} = 2.75\text{ kg}", font_size=20, color=TEXT_WHITE).move_to(mass_block5.get_center())

        base_block5 = RoundedRectangle(
            corner_radius=0.06, width=3.80, height=0.28,
            color=WALL_STROKE, stroke_width=1.8,
            fill_color=ManimColor("#121A28"), fill_opacity=1.0
        ).move_to([x_r, y_sdof5 - 0.72, 0])
        base_lbl5 = Tex(r"\textbf{Engine Base Excitation } y(t)", font_size=16, color=AMBER).move_to(base_block5.get_center())

        sdof_spring5 = make_spring(x_r - 0.95, y_sdof5 - 0.58, y_sdof5 + 0.33, num_coils=4, width=0.26, color=CYAN, stroke_width=2.2)
        sdof_k_lbl5 = MathTex(r"k_{\text{iso}}", font_size=19, color=CYAN).next_to(sdof_spring5, LEFT, buff=0.12)

        sdof_dashpot5 = make_dashpot(x_r + 0.95, y_sdof5 - 0.58, y_sdof5 + 0.33, width=0.24, color=UT_BLUE, stroke_width=2.2)
        sdof_c_lbl5 = MathTex(r"c_{\text{iso}}", font_size=19, color=UT_BLUE).next_to(sdof_dashpot5, RIGHT, buff=0.12)

        sdof_group5 = VGroup(
            sdof_frame5, mass_block5, mass_lbl5, base_block5, base_lbl5,
            sdof_spring5, sdof_k_lbl5, sdof_dashpot5, sdof_c_lbl5
        )

        eq_c_formula_big = MathTex(
            r"c_{\text{iso}} = 2 \zeta m_{\text{total}} \omega_{n,\text{iso}} = \mathbf{5.21\text{ N}\cdot\text{s/m}} \quad (\zeta = 1\%)",
            font_size=24, color=UT_BLUE
        ).move_to([x_r, -0.92, 0])

        eq_c_corner_big = MathTex(
            r"c_{\text{each}} = \frac{c_{\text{iso}}}{4} = \frac{5.21}{4} = \mathbf{1.30\text{ N}\cdot\text{s/m}}",
            font_size=25, color=UT_BLUE
        ).move_to([x_r, -1.48, 0])

        badge_damping_result = make_badge(
            r"\mathbf{ISOLATOR\ DAMPING:}\quad c_{\text{iso}} = \mathbf{5.21\text{ N}\cdot\text{s/m}}",
            UT_BLUE, width=6.25, height=0.68, font_size=23, stroke_width=2.8
        ).move_to([x_r, -2.18, 0])

        step5_right_group = VGroup(
            header_r5, sdof_group5, eq_c_formula_big, eq_c_corner_big, badge_damping_result
        )

        # ==================================================================
        # 10. RIGHT PANEL: STEP 6 (Waveform Comparison & 90% Certification)
        # ==================================================================
        header_r6 = make_badge(
            r"\textbf{Dynamic Shielding Certification}",
            GREEN_PASS, width=6.25, height=0.48, font_size=20
        ).move_to([x_r, 2.38, 0])

        # Dedicated Diagram 6: Waveform Attenuation Comparison Chart
        y_wave = 0.72
        wave_box = RoundedRectangle(
            corner_radius=0.12, width=5.60, height=2.20,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#0B1320"), fill_opacity=0.96
        ).move_to([x_r, y_wave, 0])

        x_w_start = x_r - 2.50
        x_w_end   = x_r + 2.50
        n_pts_w   = 80
        xs_w      = np.linspace(x_w_start, x_w_end, n_pts_w)

        ys_engine = y_wave + 0.65 * np.sin(2.4 * (xs_w - x_w_start))
        pts_engine = [[xs_w[i], ys_engine[i], 0] for i in range(n_pts_w)]
        wave_engine_path = VMobject().set_points_as_corners(pts_engine).set_stroke(color=AMBER, width=2.6)

        ys_chassis = y_wave + 0.065 * np.sin(2.4 * (xs_w - x_w_start) - 0.4)
        pts_chassis = [[xs_w[i], ys_chassis[i], 0] for i in range(n_pts_w)]
        wave_chassis_path = VMobject().set_points_as_corners(pts_chassis).set_stroke(color=GREEN_PASS, width=3.6)

        center_line = DashedLine([x_w_start, y_wave, 0], [x_w_end, y_wave, 0], color=SLATE, stroke_width=1.2, dash_length=0.08)

        lbl_engine_wave = MathTex(r"\mathbf{Engine\ Input\ } Y_0", font_size=17, color=AMBER).move_to([x_r - 1.35, y_wave + 0.78, 0])
        lbl_chassis_wave = MathTex(r"\mathbf{Chassis\ Motion\ } (X_0 \le 0.10 Y_0)", font_size=17, color=GREEN_PASS).move_to([x_r + 1.15, y_wave - 0.78, 0])

        waveform_group = VGroup(
            wave_box, center_line, wave_engine_path, wave_chassis_path,
            lbl_engine_wave, lbl_chassis_wave
        )

        eq_atten_metric = MathTex(
            r"\mathbf{Transmitted\ Vibration:\ } T_d \le 10\% \implies \mathbf{90\%\ Attenuation}",
            font_size=23, color=GREEN_PASS
        ).move_to([x_r, -0.82, 0])

        badge_certified = make_badge(
            r"\mathbf{90\%\ ATTENUATION\ CERTIFIED}",
            GREEN_PASS, width=6.25, height=0.76, font_size=25, stroke_width=3.2
        ).move_to([x_r, -1.55, 0])

        tag_solder_shielded = MathTex(
            r"\mathbf{Delicate\ Solder\ Joints\ Permanently\ Shielded}",
            font_size=21, color=GREEN_PASS
        ).move_to([x_r, -2.25, 0])

        step6_right_group = VGroup(
            header_r6, waveform_group, eq_atten_metric, badge_certified, tag_solder_shielded
        )

        # ==================================================================
        # 11. ANIMATION TIMELINE & FRAME-ACCURATE CUEPOINTS (6 Steps!)
        # ==================================================================

        # --- STEP 1: Transmissibility Curve & Isolation Boundary (0.0s to 3.5s) ---
        # 0.0s - 0.8s: Title reveals
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            run_time=0.8
        )

        # 0.8s - 2.2s: Left base assembly and Right step 1 plot reveal
        self.play(
            FadeIn(left_base_group),
            FadeIn(card_right),
            FadeIn(header_r1),
            Create(axes_td),
            FadeIn(x_lbl),
            FadeIn(y_lbl),
            Create(res_line),
            FadeIn(res_tag),
            Create(line_td_one),
            FadeIn(tick_td_one),
            Create(curve_amp_left),
            Create(curve_amp_mid),
            Create(curve_isolation),
            run_time=1.4
        )

        # 2.2s - 3.2s: Isolation Boundary, Target Point Lock, and Criterion Badge
        self.play(
            Create(iso_bound_line),
            FadeIn(iso_bound_tick),
            FadeIn(iso_bound_tag),
            FadeIn(zone_amp_lbl),
            FadeIn(zone_iso_lbl),
            Create(proj_v_target),
            Create(proj_h_target),
            FadeIn(target_dot),
            FadeIn(tick_r_target),
            FadeIn(tag_target_pt),
            Write(eq_condition),
            FadeIn(badge_criterion, scale=1.05),
            run_time=1.0
        )

        # 3.2s - 3.5s: Hold for Cuepoint 1
        self.wait(0.3)  # Exact Cuepoint 1 = 3.5s

        # --- STEP 2: Natural Frequency Softening & Spectral Gauge (3.5s to 6.5s) ---
        # 3.5s - 4.9s: Right Panel transitions to Step 2 (Spectral Gauge)
        self.play(
            FadeOut(step1_right_group, shift=LEFT * 0.15),
            FadeIn(header_r2),
            FadeIn(spec_group),
            Write(eq_wn_big),
            card_right.animate.set_stroke(color=AMBER, width=2.2),
            run_time=1.4
        )

        # 4.9s - 6.2s: Foundation pulses in Amber & Softening Badge reveals
        self.play(
            engine_slab.animate.set_stroke(color=AMBER, width=2.4),
            FadeIn(badge_softening, scale=1.05),
            run_time=1.3
        )

        # 6.2s - 6.5s: Hold for Cuepoint 2
        self.wait(0.3)  # Exact Cuepoint 2 = 6.5s

        # --- STEP 3: Total Stiffness Sizing & SDOF Mechanics (6.5s to 9.5s) ---
        # 6.5s - 7.9s: Right Panel transitions to Step 3 (SDOF Stiffness)
        self.play(
            FadeOut(step2_right_group, shift=UP * 0.15),
            FadeIn(header_r3),
            FadeIn(sdof_stiff_group),
            Write(eq_k_total_big),
            card_right.animate.set_stroke(color=CYAN, width=2.2),
            run_time=1.4
        )

        # 7.9s - 9.2s: Left Panel Springs illuminate in bright Cyan
        self.play(
            spring_l.animate.set_stroke(color=CYAN, width=3.4),
            spring_r.animate.set_stroke(color=CYAN, width=3.4),
            chassis_box.animate.set_stroke(color=CYAN, width=2.5),
            FadeIn(badge_stiff_result, scale=1.05),
            run_time=1.3
        )

        # 9.2s - 9.5s: Hold for Cuepoint 3
        self.wait(0.3)  # Exact Cuepoint 3 = 9.5s

        # --- STEP 4: 4-Corner Bushing Sizing Footprint (9.5s to 12.5s) ---
        # 9.5s - 10.9s: Right Panel transitions to Step 4 (Chassis Footprint)
        self.play(
            FadeOut(step3_right_group, shift=UP * 0.15),
            FadeIn(header_r4),
            FadeIn(footprint_group4),
            Write(eq_k_corner_big),
            run_time=1.4
        )

        # 10.9s - 12.2s: Corner bushing badge reveals
        self.play(
            FadeIn(badge_bushing_result, scale=1.05),
            run_time=1.3
        )

        # 12.2s - 12.5s: Hold for Cuepoint 4
        self.wait(0.3)  # Exact Cuepoint 4 = 12.5s

        # --- STEP 5: Isolator Damping Sizing (12.5s to 15.5s) ---
        # 12.5s - 13.9s: Right Panel transitions to Step 5 (Damping SDOF)
        self.play(
            FadeOut(step4_right_group, shift=UP * 0.15),
            FadeIn(header_r5),
            FadeIn(sdof_group5),
            Write(eq_c_formula_big),
            Write(eq_c_corner_big),
            card_right.animate.set_stroke(color=UT_BLUE, width=2.2),
            run_time=1.4
        )

        # 13.9s - 15.2s: Left Panel Dashpots activate in UT Blue
        self.play(
            dashpot_l.animate.set_stroke(color=UT_BLUE, width=3.0),
            dashpot_r.animate.set_stroke(color=UT_BLUE, width=3.0),
            FadeIn(badge_damping_result, scale=1.05),
            run_time=1.3
        )

        # 15.2s - 15.5s: Hold for Cuepoint 5
        self.wait(0.3)  # Exact Cuepoint 5 = 15.5s

        # --- STEP 6: Dynamic Waveforms & 90% Certification (15.5s to 19.0s) ---
        # 15.5s - 17.0s: Right Panel transitions to Dual Waveform Chart
        self.play(
            FadeOut(step5_right_group, shift=UP * 0.15),
            FadeIn(header_r6),
            FadeIn(waveform_group),
            FadeIn(eq_atten_metric),
            card_right.animate.set_stroke(color=GREEN_PASS, width=2.4),
            run_time=1.5
        )

        # 17.0s - 18.2s: Dynamic isolation demonstration & Certified badge
        self.play(
            FadeIn(step6_center_demo),
            chassis_box.animate.set_stroke(color=GREEN_PASS, width=2.8),
            FadeIn(badge_certified, scale=1.06),
            FadeIn(tag_solder_shielded),
            run_time=1.2
        )

        # 18.2s - 19.0s: Hold for Cuepoint 6
        self.wait(0.8)  # Exact Cuepoint 6 = 19.0s

        # --- Settling buffer (19.0s to 19.5s) ---
        self.wait(0.5)  # Video concludes cleanly at 19.5s

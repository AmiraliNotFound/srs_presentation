"""
SLIDE-19: ECUResonanceScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 120 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Large presentation-grade mathematical typography (enlarged fonts & expanded cards)
  - Symmetrical 2-panel layout: Automotive ECU Physical Chassis vs Mathematical Transmissibility
  - Under 10-15 English words total on canvas (Strict 10-Word Rule)
  - Frame-Accurate Step Control:
      Step 1 (0.0s - 3.5s): Clamped PCB Natural Frequency (omega_n = 52.9 Hz, k = 82.9 kN/m, m_eff = 0.75 kg)
      Step 2 (3.5s - 8.5s): Engine Base Excitation at 3600 rpm (omega = 60.0 Hz, r = 1.134 near-resonance)
      Step 3 (8.5s - 14.2s): Resonant Amplification (Td = 3.51, +351% amplification, Solder Fatigue Failure)
"""

from manim import *
import numpy as np


class ECUResonanceScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SLATE       = ManimColor("#B0B8C4")   # Enclosure, clamps, axes, annotations
        CYAN        = ManimColor("#58C4DD")   # PCB board, stiffness k, omega_n, Td curve
        AMBER       = ManimColor("#FFB703")   # Engine speed 3600 rpm, omega = 60 Hz, r = 1.134
        RED_SHOCK   = ManimColor("#FF644E")   # Resonance danger, Td = 3.51, fatigue failure
        GREEN_PASS  = ManimColor("#83C167")   # Safe / isolation reference
        UT_BLUE     = ManimColor("#0097F1")   # University of Tehran Blue accents
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        WALL_STROKE = ManimColor("#3B4D63")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{ECU Resonant Amplification}",
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
        x_l = -3.55   # Left panel center (ECU Mechanical Assembly)
        x_r = +3.55   # Right panel center (Mathematical & Transmissibility)
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
        # 4. LEFT PANEL: Physical ECU & Fixed-Fixed PCB Mechanical Assembly
        # ==================================================================
        header_l = make_badge(
            r"\textbf{Automotive ECU Chassis}\text{ (Rigid Mount)}",
            SLATE, width=5.90, height=0.52, font_size=20
        ).move_to([x_l, 2.24, 0])

        # 4.1 Engine Bay Foundation Slab (y = -2.35 to -3.00)
        engine_slab = RoundedRectangle(
            corner_radius=0.08, width=5.80, height=0.65,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#121A28"), fill_opacity=1.0
        ).move_to([x_l, -2.60, 0])

        engine_hatches = VGroup(*[
            Line([x, -2.92, 0], [x - 0.20, -3.12, 0], color=WALL_STROKE, stroke_width=1.5)
            for x in np.linspace(x_l - 2.65, x_l + 2.65, 17)
        ])

        engine_lbl = Tex(
            r"\textbf{Engine Bay Foundation } (3600\text{ rpm})",
            font_size=18, color=AMBER
        ).move_to([x_l, -2.60, 0])

        engine_bay_group = VGroup(engine_slab, engine_hatches, engine_lbl)

        # 4.2 Aluminum ECU Enclosure Body
        enclosure_w = 5.20
        enclosure_h = 3.30
        enclosure_y = 0.05
        chassis_box = RoundedRectangle(
            corner_radius=0.12, width=enclosure_w, height=enclosure_h,
            color=SLATE, stroke_width=2.2,
            fill_color=ManimColor("#090E17"), fill_opacity=0.96
        ).move_to([x_l, enclosure_y, 0])

        # Rigid mounting feet bolted to engine bay
        foot_l = Rectangle(width=0.70, height=0.35, color=SLATE, stroke_width=2.0, fill_color=ManimColor("#1E293B"), fill_opacity=1.0).move_to([x_l - 2.15, -1.75, 0])
        foot_r = Rectangle(width=0.70, height=0.35, color=SLATE, stroke_width=2.0, fill_color=ManimColor("#1E293B"), fill_opacity=1.0).move_to([x_l + 2.15, -1.75, 0])
        bolt_l = Circle(radius=0.08, color=AMBER, stroke_width=1.8, fill_color=BG_DARK, fill_opacity=1.0).move_to([x_l - 2.15, -1.75, 0])
        bolt_r = Circle(radius=0.08, color=AMBER, stroke_width=1.8, fill_color=BG_DARK, fill_opacity=1.0).move_to([x_l + 2.15, -1.75, 0])
        mount_feet_group = VGroup(foot_l, foot_r, bolt_l, bolt_r)

        # 4.3 Clamping Jaws (Fixed-Fixed boundary at x_l - 1.80 and x_l + 1.80)
        clamp_w = 0.45
        clamp_h = 1.70
        y_pcb_center = 0.35

        clamp_left = Rectangle(
            width=clamp_w, height=clamp_h, color=SLATE, stroke_width=2.0,
            fill_color=ManimColor("#1A2436"), fill_opacity=1.0
        ).move_to([x_l - 1.95, y_pcb_center, 0])

        clamp_right = Rectangle(
            width=clamp_w, height=clamp_h, color=SLATE, stroke_width=2.0,
            fill_color=ManimColor("#1A2436"), fill_opacity=1.0
        ).move_to([x_l + 1.95, y_pcb_center, 0])

        # Clamp hatches indicating rigid wall fixation
        clamp_hatches_l = VGroup(*[
            Line([x_l - 2.18, y, 0], [x_l - 2.38, y - 0.12, 0], color=SLATE, stroke_width=1.5)
            for y in np.linspace(y_pcb_center - 0.70, y_pcb_center + 0.70, 7)
        ])
        clamp_hatches_r = VGroup(*[
            Line([x_l + 2.18, y, 0], [x_l + 2.38, y - 0.12, 0], color=SLATE, stroke_width=1.5)
            for y in np.linspace(y_pcb_center - 0.70, y_pcb_center + 0.70, 7)
        ])
        clamps_group = VGroup(clamp_left, clamp_right, clamp_hatches_l, clamp_hatches_r)

        # Span and thickness dimensions
        x_pcb_start = x_l - 1.725
        x_pcb_end   = x_l + 1.725
        L_span = x_pcb_end - x_pcb_start   # 3.45 in coordinates representing l = 0.25 m
        t_pcb = 0.14                       # Visual thickness representing t = 3 mm

        # Boundary condition text
        bc_tag_l = MathTex(r"\theta = 0", font_size=18, color=CYAN).move_to([x_l - 1.95, y_pcb_center + 1.05, 0])
        bc_tag_r = MathTex(r"\theta = 0", font_size=18, color=CYAN).move_to([x_l + 1.95, y_pcb_center + 1.05, 0])
        span_dim = MathTex(r"l = 0.25\text{ m}", font_size=19, color=TEXT_WHITE).move_to([x_l, y_pcb_center + 1.05, 0])
        span_arrow = DoubleArrow([x_pcb_start, y_pcb_center + 0.85, 0], [x_pcb_end, y_pcb_center + 0.85, 0], color=SLATE, stroke_width=1.5, tip_length=0.12)
        dim_group = VGroup(bc_tag_l, bc_tag_r, span_dim, span_arrow)

        # Function to build PCB + Microchips assembly at given center deflection A
        def build_pcb_assembly(A, solder_color=SLATE, is_cracking=False):
            n_pts = 41
            xs = np.linspace(x_pcb_start, x_pcb_end, n_pts)
            # Clamped-clamped beam mode shape: w(x) = A * 0.5 * (1 + cos(2*pi*(x - x_l)/L_span))
            # Downward deflection
            ws = A * 0.5 * (1.0 + np.cos(2.0 * np.pi * (xs - x_l) / L_span))
            y_tops = y_pcb_center - ws + t_pcb / 2.0
            y_bots = y_pcb_center - ws - t_pcb / 2.0

            poly_pts = []
            for i in range(n_pts):
                poly_pts.append([xs[i], y_tops[i], 0])
            for i in range(n_pts - 1, -1, -1):
                poly_pts.append([xs[i], y_bots[i], 0])

            pcb_poly = Polygon(
                *poly_pts,
                color=CYAN, stroke_width=2.6,
                fill_color=ManimColor("#102838"), fill_opacity=0.98
            )

            # Center MCU Chip sitting on the board at x = x_l
            w_center = A
            y_mcu_base = y_pcb_center - w_center + t_pcb / 2.0
            chip_w = 0.85
            chip_h = 0.28
            mcu_body = RoundedRectangle(
                corner_radius=0.04, width=chip_w, height=chip_h,
                color=SLATE, stroke_width=1.8,
                fill_color=ManimColor("#1C2533"), fill_opacity=1.0
            ).move_to([x_l, y_mcu_base + chip_h / 2.0 + 0.05, 0])

            mcu_label = Tex(r"\textbf{MCU}", font_size=15, color=TEXT_WHITE).move_to(mcu_body.get_center())

            # Solder Pins & Joints on left and right edges of MCU
            pins = []
            pin_offsets = [-0.08, 0.0, 0.08]
            for dy in pin_offsets:
                # Left pin
                p_l1 = [x_l - chip_w / 2.0, mcu_body.get_center()[1] + dy, 0]
                p_l2 = [x_l - chip_w / 2.0 - 0.12, y_mcu_base + 0.02, 0]
                pins.append(Line(p_l1, p_l2, color=SLATE, stroke_width=1.8))
                # Right pin
                p_r1 = [x_l + chip_w / 2.0, mcu_body.get_center()[1] + dy, 0]
                p_r2 = [x_l + chip_w / 2.0 + 0.12, y_mcu_base + 0.02, 0]
                pins.append(Line(p_r1, p_r2, color=SLATE, stroke_width=1.8))

            # Solder fillets
            solder_l = Dot([x_l - chip_w / 2.0 - 0.12, y_mcu_base + 0.01, 0], radius=0.05, color=solder_color)
            solder_r = Dot([x_l + chip_w / 2.0 + 0.12, y_mcu_base + 0.01, 0], radius=0.05, color=solder_color)

            # Flanking SMD Resistors / Memory chips
            x_c1 = x_l - 0.95
            w_c1 = A * 0.5 * (1.0 + np.cos(2.0 * np.pi * (x_c1 - x_l) / L_span))
            chip1 = Rectangle(width=0.45, height=0.18, color=SLATE, stroke_width=1.4, fill_color=ManimColor("#1A202C"), fill_opacity=1.0).move_to([x_c1, y_pcb_center - w_c1 + t_pcb / 2.0 + 0.09, 0])

            x_c2 = x_l + 0.95
            w_c2 = A * 0.5 * (1.0 + np.cos(2.0 * np.pi * (x_c2 - x_l) / L_span))
            chip2 = Rectangle(width=0.45, height=0.18, color=SLATE, stroke_width=1.4, fill_color=ManimColor("#1A202C"), fill_opacity=1.0).move_to([x_c2, y_pcb_center - w_c2 + t_pcb / 2.0 + 0.09, 0])

            res = VGroup(pcb_poly, mcu_body, mcu_label, *pins, solder_l, solder_r, chip1, chip2)

            if is_cracking:
                # Glowing fatigue crack stress halos around solder joints
                crack_l1 = Circle(radius=0.13, color=RED_SHOCK, stroke_width=2.5).move_to(solder_l.get_center())
                crack_l2 = Circle(radius=0.22, color=RED_SHOCK, stroke_width=1.5).move_to(solder_l.get_center())
                crack_r1 = Circle(radius=0.13, color=RED_SHOCK, stroke_width=2.5).move_to(solder_r.get_center())
                crack_r2 = Circle(radius=0.22, color=RED_SHOCK, stroke_width=1.5).move_to(solder_r.get_center())
                crack_tag = MathTex(r"\mathbf{SOLDER\ CRACKING!}", font_size=16, color=RED_SHOCK).move_to([x_l, y_mcu_base + 0.58, 0])
                res.add(crack_l1, crack_l2, crack_r1, crack_r2, crack_tag)

            return res

        # Three assembly states:
        assembly_step1 = build_pcb_assembly(0.08, solder_color=SLATE, is_cracking=False)
        assembly_step2 = build_pcb_assembly(0.10, solder_color=AMBER, is_cracking=False)
        assembly_step3 = build_pcb_assembly(0.38, solder_color=RED_SHOCK, is_cracking=True)

        left_base_group = VGroup(card_left, header_l, engine_bay_group, chassis_box, mount_feet_group, clamps_group, dim_group)

        # Engine Excitation Harmonic Wave Vectors (Step 2)
        wave_arrows = VGroup(*[
            Arrow([x, -2.25, 0], [x, -1.68, 0], color=AMBER, stroke_width=2.2, tip_length=0.12)
            for x in np.linspace(x_l - 1.70, x_l + 1.70, 5)
        ])
        wave_lbl = MathTex(r"\mathbf{Engine\ Harmonic\ Vibration:}\quad 60\text{ Hz}", font_size=18, color=AMBER).move_to([x_l, -1.35, 0])
        engine_pulse_group = VGroup(wave_arrows, wave_lbl)

        # Solder Fatigue Warning Tag on Left Panel (Step 3)
        badge_fatigue_left = make_badge(
            r"\mathbf{FATIGUE\ FAILURE:}\; \text{Solder Joint Shear}",
            RED_SHOCK, width=5.60, height=0.60, font_size=19, stroke_width=2.4
        ).move_to([x_l, -1.35, 0])

        # ==================================================================
        # 5. RIGHT PANEL: Step 1 (Natural Frequency Derivation)
        # ==================================================================
        header_r1 = make_badge(
            r"\textbf{Fixed-Fixed PCB Dynamics}",
            CYAN, width=5.90, height=0.52, font_size=21
        ).move_to([x_r, 2.24, 0])

        params_row = MathTex(
            r"l = 0.25\text{ m}, \quad w = 0.20\text{ m}, \quad t = 3\text{ mm}, \quad m = 1.5\text{ kg}",
            font_size=20, color=SLATE
        ).move_to([x_r, 1.58, 0])

        eq_inertia = MathTex(
            r"I = \frac{1}{12} w t^3 = \frac{1}{12}(0.20)(0.003)^3 = 4.50 \times 10^{-10}\text{ m}^4",
            font_size=20, color=TEXT_WHITE
        ).move_to([x_r, 1.00, 0])

        eq_stiff = MathTex(
            r"k = \frac{192 E I}{l^3} = \frac{192(15 \times 10^9)(4.50 \times 10^{-10})}{(0.25)^3} = \mathbf{82,944\text{ N/m}}",
            font_size=20, color=CYAN
        ).move_to([x_r, 0.38, 0])

        eq_meff = MathTex(
            r"\text{Rayleigh Effective Mass:}\quad m_{\text{eff}} = 0.5\, m = \mathbf{0.75\text{ kg}}",
            font_size=20, color=SLATE
        ).move_to([x_r, -0.28, 0])

        eq_wn = MathTex(
            r"\omega_n = \sqrt{\frac{k}{m_{\text{eff}}}} = \sqrt{\frac{82,944}{0.75}} = \mathbf{332.55\text{ rad/s}} \quad (52.93\text{ Hz})",
            font_size=21, color=TEXT_WHITE
        ).move_to([x_r, -0.92, 0])

        badge_fn = make_badge(
            r"\mathbf{PCB\ NATURAL\ FREQUENCY:}\quad f_n = 52.9\text{ Hz}",
            CYAN, width=5.90, height=0.70, font_size=21, stroke_width=2.6
        ).move_to([x_r, -1.85, 0])

        step1_right_group = VGroup(
            header_r1, params_row, eq_inertia, eq_stiff, eq_meff, eq_wn, badge_fn
        )

        # ==================================================================
        # 6. RIGHT PANEL: Step 2 (Engine Base Excitation & Near Resonance)
        # ==================================================================
        header_r2 = make_badge(
            r"\textbf{Engine Base Excitation}\text{ (3600 rpm)}",
            AMBER, width=5.90, height=0.52, font_size=21
        ).move_to([x_r, 2.24, 0])

        eq_speed = MathTex(
            r"\text{Engine Operating Speed: } N = 3600\text{ rpm}",
            font_size=24, color=TEXT_WHITE
        ).move_to([x_r, 1.48, 0])

        eq_omega = MathTex(
            r"\omega = \frac{2\pi(3600)}{60} = \mathbf{376.99\text{ rad/s}} \quad (60.0\text{ Hz})",
            font_size=22, color=AMBER
        ).move_to([x_r, 0.82, 0])

        eq_ratio = MathTex(
            r"r = \frac{\omega}{\omega_n} = \frac{376.99\text{ rad/s}}{332.55\text{ rad/s}} = \mathbf{1.1336} \approx 1.13",
            font_size=24, color=TEXT_WHITE
        ).move_to([x_r, 0.05, 0])

        note_proximity = MathTex(
            r"\text{Resonance Proximity: } |1 - r| = 13.4\% \quad (\mathbf{Near\ Resonance!})",
            font_size=21, color=AMBER
        ).move_to([x_r, -0.72, 0])

        badge_near_res = make_badge(
            r"\mathbf{CRITICAL\ NEAR\ RESONANCE:}\quad r = 1.134 \approx 1.0",
            AMBER, width=5.90, height=0.70, font_size=19, stroke_width=2.6
        ).move_to([x_r, -1.75, 0])

        halo_amber = RoundedRectangle(
            corner_radius=0.18, width=6.10, height=0.88,
            color=AMBER, stroke_width=3.0, fill_opacity=0.0
        ).move_to([x_r, -1.75, 0])

        step2_right_group = VGroup(
            header_r2, eq_speed, eq_omega, eq_ratio, note_proximity, badge_near_res, halo_amber
        )

        # ==================================================================
        # 7. RIGHT PANEL: Step 3 (Displacement Transmissibility & Fatigue)
        # ==================================================================
        header_r3 = make_badge(
            r"\textbf{Displacement Transmissibility } T_d(r)",
            RED_SHOCK, width=5.90, height=0.52, font_size=21
        ).move_to([x_r, 2.24, 0])

        # Classical Transmissibility Curve T_d(r)
        axes_td = Axes(
            x_range=[0, 2.4, 0.5],
            y_range=[0, 4.5, 1.0],
            x_length=4.80,
            y_length=1.85,
            axis_config={"color": SLATE, "stroke_width": 1.8},
            tips=False
        ).move_to([x_r + 0.15, 0.70, 0])

        x_lbl = MathTex(r"r = \omega / \omega_n", font_size=19, color=SLATE).next_to(axes_td.x_axis, DOWN, buff=0.10).align_to(axes_td.x_axis, RIGHT)
        y_lbl = MathTex(r"T_d", font_size=19, color=SLATE).next_to(axes_td.y_axis, LEFT, buff=0.10).align_to(axes_td.y_axis, UP)

        tick_r_op = MathTex(r"1.13", font_size=16, color=AMBER).next_to(axes_td.c2p(1.134, 0), DOWN, buff=0.08)
        tick_sqrt2 = MathTex(r"\sqrt{2}", font_size=16, color=SLATE).next_to(axes_td.c2p(np.sqrt(2), 0), DOWN, buff=0.08)

        # Vertical Resonance Asymptote at r = 1.0
        res_line = DashedLine(
            axes_td.c2p(1.0, 0), axes_td.c2p(1.0, 4.3),
            color=RED_SHOCK, stroke_width=1.8, dash_length=0.07
        )
        res_tag = MathTex(r"\text{Resonance } (r = 1.0)", font_size=14, color=RED_SHOCK).next_to(res_line, UP, buff=0.04)

        # Curve branches (left and right of r = 1)
        curve_left = axes_td.plot(
            lambda r: 1.0 / abs(1.0 - r**2),
            x_range=[0.0, 0.85, 0.02],
            color=CYAN, stroke_width=2.6
        )
        curve_right = axes_td.plot(
            lambda r: 1.0 / abs(1.0 - r**2),
            x_range=[1.12, 2.35, 0.02],
            color=CYAN, stroke_width=2.6
        )

        # Operating Point at r = 1.1336, T_d = 3.508
        r_val = 1.1336
        td_val = 3.508
        pt_dot = Dot(point=axes_td.c2p(r_val, td_val), radius=0.08, color=AMBER)
        proj_v = DashedLine(axes_td.c2p(r_val, 0), axes_td.c2p(r_val, td_val), color=AMBER, stroke_width=1.6, dash_length=0.06)
        proj_h = DashedLine(axes_td.c2p(0, td_val), axes_td.c2p(r_val, td_val), color=RED_SHOCK, stroke_width=1.6, dash_length=0.06)
        pt_badge = MathTex(r"T_d = 3.51", font_size=18, color=RED_SHOCK).next_to(pt_dot, UR, buff=0.08)

        # Isolation boundary line T_d = 1.0 at r = sqrt(2)
        iso_line = DashedLine(axes_td.c2p(0, 1.0), axes_td.c2p(2.35, 1.0), color=SLATE, stroke_width=1.4, dash_length=0.06)

        plot_group = VGroup(
            axes_td, x_lbl, y_lbl, tick_r_op, tick_sqrt2,
            res_line, res_tag, curve_left, curve_right,
            iso_line, proj_v, proj_h, pt_dot, pt_badge
        )

        # Transmissibility calculation & amplification evaluation
        eq_td_eval = MathTex(
            r"T_d = \frac{1}{|1 - r^2|} = \frac{1}{|1 - (1.1336)^2|} = \frac{1}{0.2851} = \mathbf{3.508}",
            font_size=21, color=TEXT_WHITE
        ).move_to([x_r, -0.78, 0])

        badge_amplification = make_badge(
            r"\mathbf{RESONANT\ AMPLIFICATION:}\quad \mathbf{+351\%} \quad (T_d = 3.51)",
            RED_SHOCK, width=6.05, height=0.72, font_size=19, stroke_width=2.8
        ).move_to([x_r, -1.65, 0])

        halo_red = RoundedRectangle(
            corner_radius=0.18, width=6.25, height=0.90,
            color=RED_SHOCK, stroke_width=3.2, fill_opacity=0.0
        ).move_to([x_r, -1.65, 0])

        tag_failure_right = MathTex(
            r"\mathbf{High\text{-}Cycle\ Solder\ Fatigue\ \implies\ Electronic\ Failure}",
            font_size=19, color=RED_SHOCK
        ).move_to([x_r, -2.40, 0])

        step3_right_group = VGroup(
            header_r3, plot_group, eq_td_eval, badge_amplification, halo_red, tag_failure_right
        )

        # ==================================================================
        # 8. ANIMATION TIMELINE & FRAME-ACCURATE CUEPOINTS
        # ==================================================================

        # --- STEP 1: Clamped PCB Natural Frequency (0.0s to 3.5s) ---
        # 0.0s - 0.8s: Title reveals
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            run_time=0.8
        )

        # 0.8s - 2.2s: Left panel enclosure, clamps, and baseline PCB assembly
        self.play(
            FadeIn(left_base_group),
            FadeIn(assembly_step1),
            FadeIn(card_right),
            run_time=1.4
        )

        # 2.2s - 3.2s: Step 1 Right panel equations draw in
        self.play(
            FadeIn(header_r1),
            FadeIn(params_row),
            Write(eq_inertia),
            Write(eq_stiff),
            FadeIn(eq_meff),
            Write(eq_wn),
            FadeIn(badge_fn, scale=1.05),
            run_time=1.0
        )

        # 3.2s - 3.5s: Hold for Cuepoint 1
        self.wait(0.3)  # Exact Cuepoint 1 = 3.5s

        # --- STEP 2: Engine Excitation & Near Resonance (3.5s to 8.5s) ---
        # 3.5s - 4.8s: Engine Bay Excitation Activates on Left Panel
        self.play(
            FadeIn(engine_pulse_group),
            ReplacementTransform(assembly_step1, assembly_step2),
            chassis_box.animate.set_stroke(color=AMBER, width=2.4),
            run_time=1.3
        )

        # 4.8s - 6.2s: Right Panel transitions from Step 1 to Step 2
        self.play(
            FadeOut(step1_right_group, shift=LEFT * 0.15),
            FadeIn(header_r2),
            FadeIn(eq_speed),
            Write(eq_omega),
            Write(eq_ratio),
            FadeIn(note_proximity),
            run_time=1.4
        )

        # 6.2s - 7.5s: Critical Near-Resonance Warning Badge & Halo Pulse
        self.play(
            FadeIn(badge_near_res, scale=1.06),
            Create(halo_amber),
            run_time=1.3
        )

        # 7.5s - 8.5s: Hold for Cuepoint 2
        self.wait(1.0)  # Exact Cuepoint 2 = 8.5s

        # --- STEP 3: Resonant Amplification & Solder Fatigue (8.5s to 14.2s) ---
        # 8.5s - 10.3s: Right Panel Morphs into Transmissibility Curve Plot
        self.play(
            FadeOut(step2_right_group, shift=UP * 0.15),
            FadeIn(header_r3),
            Create(axes_td),
            FadeIn(x_lbl),
            FadeIn(y_lbl),
            FadeIn(tick_r_op),
            FadeIn(tick_sqrt2),
            Create(res_line),
            FadeIn(res_tag),
            Create(curve_left),
            Create(curve_right),
            Create(iso_line),
            Create(proj_v),
            Create(proj_h),
            FadeIn(pt_dot),
            FadeIn(pt_badge),
            card_right.animate.set_stroke(color=RED_SHOCK, width=2.4),
            run_time=1.8
        )

        # 10.3s - 11.8s: Amplification Evaluation & Dramatic Deflection Surge (351%!)
        self.play(
            Write(eq_td_eval),
            FadeIn(badge_amplification, scale=1.08),
            Create(halo_red),
            FadeOut(engine_pulse_group),
            FadeIn(badge_fatigue_left),
            ReplacementTransform(assembly_step2, assembly_step3),
            chassis_box.animate.set_stroke(color=RED_SHOCK, width=2.8),
            run_time=1.5
        )

        # 11.8s - 13.0s: Solder joint fatigue warning & Halo Expansion Pulse
        self.play(
            FadeIn(tag_failure_right),
            halo_red.animate.scale(1.10).set_stroke(opacity=0.0),
            run_time=1.2
        )

        # 13.0s - 14.2s: Hold for Cuepoint 3
        self.wait(1.2)  # Exact Cuepoint 3 = 14.2s

        # --- Settling buffer (14.2s to 15.0s) ---
        self.wait(0.8)  # Video concludes cleanly at 15.0s

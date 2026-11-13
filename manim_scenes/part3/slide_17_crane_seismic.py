"""
SLIDE-17: CraneSeismicScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 150 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Large presentation-grade mathematical typography (enlarged fonts & expanded box)
  - Symmetrical 2-panel layout (Mechanical Wheel/Rail Interface & Physics Derivation)
  - Under 10 English words total on canvas (Strict 10-Word Rule)
  - Frame-Accurate Step Control:
      Step 1 (0.0s - 3.5s): Unbolted Gravity Contact Vulnerability (N(t) = m(g - x_ddot))
      Step 2 (3.5s - 8.5s): Seismic Derailment Threshold (Sa >= 1.0g causes N_min <= 0)
      Step 3 (8.5s - 14.2s): Flexible Crane Evaluation (Sa = 0.25g -> N_min = 0.75mg > 0: SAFE)
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine
import numpy as np


class CraneSeismicScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SLATE       = ManimColor("#B0B8C4")   # Rail, girder structure, axes
        AMBER       = ManimColor("#FFB703")   # Mass, gravity force vector (mg), natural period tau_n
        CYAN        = ManimColor("#58C4DD")   # Normal dynamic contact force N(t)
        RED_SHOCK   = ManimColor("#FF644E")   # Seismic ground motion, inertia, derailment limit Sa >= 1.0g
        GREEN_PASS  = ManimColor("#83C167")   # Safe state, clamped contact, N_min > 0, NO DERAILMENT
        UT_BLUE     = ManimColor("#0097F1")   # University of Tehran Blue, accents
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        WALL_STROKE = ManimColor("#3B4D63")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 4 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Overhead Crane Seismic Derailment}",
            font_size=38,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # ------------------------------------------------------------------
        # 3. Helper Function for Sleek Rounded Badges
        # ------------------------------------------------------------------
        def make_badge(tex_str, color, width, height, font_size=24):
            rect = RoundedRectangle(
                corner_radius=0.14,
                width=width,
                height=height,
                color=color,
                stroke_width=2.2,
                fill_color=BG_DARK,
                fill_opacity=0.94
            )
            tex = MathTex(tex_str, font_size=font_size, color=color)
            tex.move_to(rect.get_center())
            return VGroup(rect, tex)

        # ==================================================================
        # 4. LEFT PANEL: Mechanical Crane Rail & Trolley Wheel Interface
        # ==================================================================
        x_c = -3.85   # Crane assembly horizontal center line

        # 4.1 Ground Bedrock Slab & Foundation
        # Dedicated Bedrock Block (y = -2.65 to -3.75)
        bedrock_box = RoundedRectangle(
            corner_radius=0.08, width=3.80, height=1.10,
            color=WALL_STROKE, stroke_width=2.0,
            fill_color=ManimColor("#0D1420"), fill_opacity=0.98
        ).move_to([x_c, -3.20, 0])

        ground_line = Line([x_c - 1.90, -2.65, 0], [x_c + 1.90, -2.65, 0], color=SLATE, stroke_width=2.5)

        hatches = VGroup(*[
            Line([x, -3.75, 0], [x - 0.18, -3.95, 0], color=WALL_STROKE, stroke_width=1.5)
            for x in np.linspace(x_c - 1.70, x_c + 1.70, 11)
        ])
        foundation_group = VGroup(bedrock_box, ground_line, hatches)

        # 4.2 Girder Support Column (y = -2.65 to -2.15)
        support_col = Rectangle(
            width=1.10, height=0.50, color=SLATE, stroke_width=2.0,
            fill_color=ManimColor("#162030"), fill_opacity=1.0
        ).move_to([x_c, -2.40, 0])

        # 4.3 ASCE Crane Runway Rail Cross-Section
        # Rail base: y = -2.15 to -1.93
        rail_base = RoundedRectangle(
            corner_radius=0.04, width=2.20, height=0.22,
            color=SLATE, stroke_width=2.0,
            fill_color=ManimColor("#141E2C"), fill_opacity=1.0
        ).move_to([x_c, -2.04, 0])

        # Rail vertical web: y = -1.93 to -1.08
        rail_web = Rectangle(
            width=0.42, height=0.85,
            color=SLATE, stroke_width=2.0,
            fill_color=ManimColor("#141E2C"), fill_opacity=1.0
        ).move_to([x_c, -1.505, 0])

        # Rail head: y = -1.08 to -0.70 (top surface at y = -0.70)
        rail_head = RoundedRectangle(
            corner_radius=0.08, width=1.50, height=0.38,
            color=SLATE, stroke_width=2.2,
            fill_color=ManimColor("#1E2A3B"), fill_opacity=1.0
        ).move_to([x_c, -0.89, 0])

        rail_group = VGroup(support_col, rail_base, rail_web, rail_head)

        # 4.4 Double-Flanged Crane Trolley Wheel & Chassis Assembly
        y_contact = -0.70
        r_wheel = 0.90
        y_wheel0 = y_contact + r_wheel   # 0.20

        # Concentric Outer Flange Ring (Authentic Double-Flanged Crane Wheel)
        wheel_flange = Circle(
            radius=1.04, color=SLATE, stroke_width=1.8,
            fill_color=ManimColor("#182334"), fill_opacity=0.94
        ).move_to([x_c, y_wheel0, 0])

        # Wheel main tread cylinder
        wheel_tread = Circle(
            radius=r_wheel, color=SLATE, stroke_width=2.4,
            fill_color=ManimColor("#0F172A"), fill_opacity=0.98
        ).move_to([x_c, y_wheel0, 0])

        # Wheel inner decorative groove
        wheel_rim = Circle(
            radius=0.70, color=ManimColor("#263445"), stroke_width=1.4
        ).move_to([x_c, y_wheel0, 0])

        # Wheel central hub & axle pin
        wheel_hub = Circle(
            radius=0.28, color=UT_BLUE, stroke_width=2.0,
            fill_color=ManimColor("#162032"), fill_opacity=1.0
        ).move_to([x_c, y_wheel0, 0])
        axle_pin = Dot(point=[x_c, y_wheel0, 0], radius=0.09, color=AMBER)

        # Diagonal cross spokes
        spoke1 = Line([x_c - 0.48, y_wheel0 - 0.48, 0], [x_c + 0.48, y_wheel0 + 0.48, 0], color=SLATE, stroke_width=1.2)
        spoke2 = Line([x_c - 0.48, y_wheel0 + 0.48, 0], [x_c + 0.48, y_wheel0 - 0.48, 0], color=SLATE, stroke_width=1.2)
        wheel_spokes = VGroup(spoke1, spoke2)

        # Chassis suspension struts and trolley mass
        strut_l = Line([x_c, y_wheel0, 0], [x_c - 0.90, 1.48, 0], color=SLATE, stroke_width=3.2)
        strut_r = Line([x_c, y_wheel0, 0], [x_c + 0.90, 1.48, 0], color=SLATE, stroke_width=3.2)
        bed_plate = Rectangle(
            width=2.60, height=0.14, color=SLATE,
            fill_color=ManimColor("#1E293B"), fill_opacity=1.0
        ).move_to([x_c, 1.48, 0])

        mass_box = RoundedRectangle(
            corner_radius=0.14, width=2.80, height=0.92,
            color=AMBER, stroke_width=2.4,
            fill_color=ManimColor("#151D2A"), fill_opacity=0.95
        ).move_to([x_c, 2.08, 0])

        mass_label = MathTex(r"m = 2500\text{ kg}", font_size=25, color=AMBER).move_to([x_c, 2.08, 0])

        # Complete Mobile Trolley Assembly (Translates UP during derailment float)
        trolley_group = VGroup(
            wheel_flange, wheel_tread, wheel_rim, wheel_spokes,
            wheel_hub, axle_pin, strut_l, strut_r, bed_plate, mass_box, mass_label
        )

        # 4.5 Mechanical Contact Indicators & Force Vectors
        contact_line = Line([x_c - 0.40, y_contact, 0], [x_c + 0.40, y_contact, 0], color=CYAN, stroke_width=4.5)
        contact_badge = MathTex(r"\text{Unbolted Contact}", font_size=18, color=TEXT_MUTED).move_to([-1.95, y_contact, 0])
        contact_pointer = DashedLine([-2.65, y_contact, 0], [x_c + 0.45, y_contact, 0], color=TEXT_MUTED, stroke_width=1.5)
        contact_callout = VGroup(contact_line, contact_badge, contact_pointer)

        # Downward gravity force vector mg with subtle dark backing
        arrow_mg = Arrow([x_c, 1.48, 0], [x_c, 0.42, 0], color=AMBER, stroke_width=4.0, tip_length=0.22)
        bg_mg = RoundedRectangle(corner_radius=0.08, width=0.62, height=0.38, color=BG_DARK, fill_color=BG_DARK, fill_opacity=0.9, stroke_width=0).move_to([x_c - 0.65, 0.95, 0])
        label_mg = MathTex(r"m g", font_size=25, color=AMBER).move_to([x_c - 0.65, 0.95, 0])
        gravity_vector = VGroup(arrow_mg, bg_mg, label_mg)

        # Upward dynamic normal contact force N(t)
        arrow_n = Arrow([x_c, y_contact, 0], [x_c, 0.32, 0], color=CYAN, stroke_width=4.0, tip_length=0.22)
        bg_n = RoundedRectangle(corner_radius=0.08, width=0.68, height=0.38, color=BG_DARK, fill_color=BG_DARK, fill_opacity=0.9, stroke_width=0).move_to([x_c + 0.65, -0.20, 0])
        label_n = MathTex(r"N(t)", font_size=25, color=CYAN).move_to([x_c + 0.65, -0.20, 0])
        normal_vector = VGroup(arrow_n, bg_n, label_n)

        # 4.6 Publication-Grade Seismic Wavefronts (Clean Concentric Radiating Waves)
        wave_origin = [x_c, -3.75, 0]
        arc_w1 = Arc(radius=0.35, start_angle=0.15*PI, angle=0.70*PI, color=RED_SHOCK, stroke_width=2.4, arc_center=wave_origin)
        arc_w2 = Arc(radius=0.60, start_angle=0.15*PI, angle=0.70*PI, color=RED_SHOCK, stroke_width=2.4, arc_center=wave_origin)
        arc_w3 = Arc(radius=0.85, start_angle=0.15*PI, angle=0.70*PI, color=RED_SHOCK, stroke_width=2.4, arc_center=wave_origin)

        arrow_seis_l = Arrow([x_c - 1.25, -3.65, 0], [x_c - 1.25, -2.80, 0], color=RED_SHOCK, stroke_width=4.0, tip_length=0.20)
        arrow_seis_r = Arrow([x_c + 1.25, -3.65, 0], [x_c + 1.25, -2.80, 0], color=RED_SHOCK, stroke_width=4.0, tip_length=0.20)

        bg_seis = RoundedRectangle(
            corner_radius=0.10, width=2.60, height=0.46,
            color=RED_SHOCK, fill_color=BG_DARK, fill_opacity=0.96, stroke_width=1.8
        ).move_to([x_c, -3.20, 0])
        label_seis = MathTex(r"\mathbf{\ddot{y}_v(t)\; Earthquake}", font_size=20, color=RED_SHOCK).move_to([x_c, -3.20, 0])

        seismic_pulse_group = VGroup(
            arc_w1, arc_w2, arc_w3, arrow_seis_l, arrow_seis_r, bg_seis, label_seis
        )

        # Step 2 Derailment gap indicators (when wheel floats up)
        gap_dashed = DashedLine([x_c - 0.45, y_contact + 0.17, 0], [x_c + 0.45, y_contact + 0.17, 0], color=RED_SHOCK, stroke_width=2.5)
        gap_arrow = DoubleArrow([x_c, y_contact, 0], [x_c, y_contact + 0.34, 0], color=RED_SHOCK, stroke_width=2.5, tip_length=0.10)
        gap_badge = MathTex(r"\Delta z > 0 \implies N = 0", font_size=19, color=RED_SHOCK).move_to([-1.90, y_contact + 0.17, 0])
        gap_group = VGroup(gap_dashed, gap_arrow, gap_badge)

        # Step 3 Safe Clamping Indicators (wheel firmly seated)
        clamp_glow = Line([x_c - 0.50, y_contact, 0], [x_c + 0.50, y_contact, 0], color=GREEN_PASS, stroke_width=6.0)
        arrow_n_safe = Arrow([x_c, y_contact, 0], [x_c, 0.12, 0], color=CYAN, stroke_width=4.0, tip_length=0.20)
        bg_n_safe = RoundedRectangle(corner_radius=0.08, width=1.55, height=0.38, color=BG_DARK, fill_color=BG_DARK, fill_opacity=0.9, stroke_width=0).move_to([x_c + 1.05, -0.30, 0])
        label_n_safe = MathTex(r"N_{\min} = 0.75\,mg", font_size=21, color=CYAN).move_to([x_c + 1.05, -0.30, 0])
        safe_contact_group = VGroup(clamp_glow, arrow_n_safe, bg_n_safe, label_n_safe)

        # ==================================================================
        # 5. RIGHT PANEL: Expanded Box & Large Presentation Typography
        # ==================================================================
        x_r = 3.35   # Right panel horizontal center line
        card_w = 6.90
        card_h = 6.10
        card_y = -0.40

        card_bg = RoundedRectangle(
            corner_radius=0.16, width=card_w, height=card_h,
            color=CARD_STROKE, stroke_width=2.0,
            fill_color=BG_DARK, fill_opacity=0.94
        ).move_to([x_r, card_y, 0])

        # ------------------------------------------------------------------
        # STEP 1 COMPONENTS (0.0s - 3.5s): Unbolted Gravity Contact Mechanics
        # ------------------------------------------------------------------
        header1 = make_badge(
            r"\textbf{Dynamic Normal Contact Force}",
            CYAN, width=6.20, height=0.62, font_size=25
        ).move_to([x_r, 2.15, 0])

        eq_dyn1 = MathTex(
            r"N(t) = m\left(g - \ddot{x}_{\text{abs}}(t)\right)",
            font_size=38, color=TEXT_WHITE
        ).move_to([x_r, 1.15, 0])

        box_clamped = make_badge(
            r"\mathbf{Contact\ Maintained} \iff N(t) > 0",
            AMBER, width=6.00, height=0.68, font_size=26
        ).move_to([x_r, -0.05, 0])

        sub_eq2 = MathTex(
            r"\mathbf{Unbolted\ Trolley\ Held\ Purely\ by\ Gravity}",
            font_size=25, color=TEXT_WHITE
        ).move_to([x_r, -1.20, 0])

        param_row = MathTex(
            r"m = 2500\text{ kg} \quad \zeta = 0.02 \quad \tau_n = 2.0\text{ s}",
            font_size=24, color=CYAN
        ).move_to([x_r, -2.15, 0])

        step1_group = VGroup(header1, eq_dyn1, box_clamped, sub_eq2, param_row)

        # ------------------------------------------------------------------
        # STEP 2 COMPONENTS (3.5s - 8.5s): Seismic Derailment Threshold
        # ------------------------------------------------------------------
        header2 = make_badge(
            r"\textbf{Seismic Derailment Condition}",
            RED_SHOCK, width=6.20, height=0.62, font_size=25
        ).move_to([x_r, 2.15, 0])

        eq_nmin = MathTex(
            r"N_{\min} = m\left(g - S_a\right)",
            font_size=38, color=TEXT_WHITE
        ).move_to([x_r, 1.20, 0])

        eq_thresh = MathTex(
            r"\mathbf{Derailment\ Threshold:}\quad N_{\min} \le 0 \iff S_a \ge 1.0g",
            font_size=26, color=RED_SHOCK
        ).move_to([x_r, 0.25, 0])

        badge_derail = make_badge(
            r"\mathbf{DERAILMENT\; RISK:}\; S_a \ge 1.0g \quad (9.81\text{ m/s}^2)",
            RED_SHOCK, width=6.30, height=0.72, font_size=24
        ).move_to([x_r, -0.75, 0])

        sub_derail = MathTex(
            r"S_a \ge 1.0g \implies N(t) = 0 \implies \mathbf{Wheel\ Decouples\ \&\ Derails}",
            font_size=23, color=TEXT_WHITE
        ).move_to([x_r, -1.75, 0])

        sub_derail2 = MathTex(
            r"-m \ddot{x}_{\text{abs}} > m g \iff S_a > 1.0g",
            font_size=25, color=RED_SHOCK
        ).move_to([x_r, -2.50, 0])

        step2_group = VGroup(header2, eq_nmin, eq_thresh, badge_derail, sub_derail, sub_derail2)

        # ------------------------------------------------------------------
        # STEP 3 COMPONENTS (8.5s - 14.2s): Flexible Crane Verification
        # ------------------------------------------------------------------
        header3 = make_badge(
            r"\textbf{Flexible Crane Verification } (\tau_n = 2.0\text{ s})",
            GREEN_PASS, width=6.20, height=0.62, font_size=24
        ).move_to([x_r, 2.15, 0])

        # Large, Crisp Tripartite Earthquake Design Spectrum (zeta = 0.02)
        axes = Axes(
            x_range=[0, 3.2, 0.5],
            y_range=[0, 1.5, 0.5],
            x_length=5.10,
            y_length=2.00,
            axis_config={"color": SLATE, "stroke_width": 1.8},
            tips=False
        ).move_to([x_r, 0.70, 0])

        x_label = MathTex(r"\tau_n\text{ (s)}", font_size=19, color=SLATE).next_to(axes.x_axis, DOWN, buff=0.10).align_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"S_a / g", font_size=19, color=SLATE).next_to(axes.y_axis, LEFT, buff=0.10).align_to(axes.y_axis, UP)
        tick_2s = MathTex(r"2.0", font_size=17, color=AMBER).next_to(axes.c2p(2.0, 0), DOWN, buff=0.08)
        tick_1g = MathTex(r"1.0g", font_size=17, color=RED_SHOCK).next_to(axes.c2p(0, 1.0), LEFT, buff=0.08)

        # Derailment threshold line Sa = 1.0g
        thresh_line = DashedLine(
            axes.c2p(0, 1.0), axes.c2p(3.1, 1.0),
            color=RED_SHOCK, stroke_width=2.2, dash_length=0.09
        )
        thresh_label = MathTex(
            r"\text{Derailment Boundary } (1.0g)",
            font_size=15, color=RED_SHOCK
        ).next_to(thresh_line, UP, buff=0.04).align_to(thresh_line, RIGHT)

        # Physical design spectrum curve (zeta = 0.02, Rao Fig. 4.19)
        def spectrum_func(t):
            if t < 0.06:
                return 0.35 + (t / 0.06) * 0.87
            elif t <= 0.52:
                return 1.22
            else:
                return 1.22 * (0.52 / t) ** 1.15

        spectrum_curve = axes.plot(spectrum_func, x_range=[0.06, 3.0, 0.02], color=CYAN, stroke_width=2.6)

        # Operating point at tau_n = 2.0 s, Sa = 0.25g
        pt_dot = Dot(point=axes.c2p(2.0, 0.25), radius=0.09, color=AMBER)
        proj_v = DashedLine(axes.c2p(2.0, 0), axes.c2p(2.0, 0.25), color=AMBER, stroke_width=2.0)
        proj_h = DashedLine(axes.c2p(0, 0.25), axes.c2p(2.0, 0.25), color=AMBER, stroke_width=2.0)
        pt_badge = MathTex(r"S_a = 0.25g", font_size=19, color=AMBER).next_to(pt_dot, UR, buff=0.08)

        spectrum_all = VGroup(
            axes, x_label, y_label, tick_2s, tick_1g,
            thresh_line, thresh_label, spectrum_curve,
            proj_v, proj_h, pt_dot, pt_badge
        )

        calc_sa = MathTex(
            r"\tau_n = 2.0\text{ s}, \; \zeta = 0.02 \implies S_a = 0.25g = 2.45\text{ m/s}^2",
            font_size=23, color=CYAN
        ).move_to([x_r, -0.80, 0])

        calc_nmin = MathTex(
            r"N_{\min} = m(g - 0.25g) = \mathbf{0.75\,mg > 0}",
            font_size=28, color=TEXT_WHITE
        ).move_to([x_r, -1.45, 0])

        badge_safe = make_badge(
            r"\mathbf{SAFE:\; NO\; DERAILMENT} \quad (S_a \ll 1.0g)",
            GREEN_PASS, width=6.20, height=0.72, font_size=24
        ).move_to([x_r, -2.35, 0])

        safe_halo = RoundedRectangle(
            corner_radius=0.18, width=6.36, height=0.88,
            color=GREEN_PASS, stroke_width=3.4, fill_opacity=0.0
        ).move_to([x_r, -2.35, 0])

        step3_calcs = VGroup(calc_sa, calc_nmin, badge_safe)

        # ==================================================================
        # 6. ANIMATION TIMELINE & FRAME-ACCURATE CUEPOINTS
        # ==================================================================

        # --- STEP 1: Unbolted Gravity Contact (0.0s to 3.5s) ---
        # 0.0s - 0.9s: Minimalist Title, Foundation, and ASCE Rail Fade In
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            FadeIn(foundation_group),
            FadeIn(rail_group, shift=UP * 0.10),
            FadeIn(card_bg),
            run_time=0.9
        )

        # 0.9s - 2.0s: Trolley Wheel Assembly Appears, Gravity & Normal Forces Draw In
        self.play(
            FadeIn(trolley_group, shift=DOWN * 0.15),
            Create(contact_callout),
            GrowArrow(arrow_mg),
            FadeIn(bg_mg),
            FadeIn(label_mg),
            GrowArrow(arrow_n),
            FadeIn(bg_n),
            FadeIn(label_n),
            run_time=1.1
        )

        # 2.0s - 3.2s: Step 1 Dynamic Equations Fade In on Right Panel (Filling Box)
        self.play(
            FadeIn(header1),
            Write(eq_dyn1),
            FadeIn(box_clamped),
            FadeIn(sub_eq2),
            FadeIn(param_row),
            run_time=1.2
        )

        # 3.2s - 3.5s: Hold for Cuepoint 1
        self.wait(0.3)  # Exact Cuepoint 1 = 3.5s

        # --- STEP 2: Seismic Derailment Threshold (3.5s to 8.5s) ---
        # 3.5s - 4.6s: Concentric Seismic Ground Wavefronts Emerge from Bedrock
        self.play(
            Create(arc_w1),
            Create(arc_w2),
            Create(arc_w3),
            GrowArrow(arrow_seis_l),
            GrowArrow(arrow_seis_r),
            FadeIn(bg_seis),
            FadeIn(label_seis),
            card_bg.animate.set_stroke(color=RED_SHOCK, width=2.4),
            run_time=1.1
        )

        # 4.6s - 5.8s: Right Panel Morphs into Derailment Threshold Condition
        self.play(
            FadeOut(step1_group, shift=LEFT * 0.15),
            FadeIn(step2_group, shift=RIGHT * 0.15),
            run_time=1.2
        )

        # 5.8s - 7.0s: Wheel Assembly Lifts Off Rail by Delta z (Normal Force Drops to Zero!)
        self.play(
            trolley_group.animate.shift(UP * 0.34),
            arrow_mg.animate.shift(UP * 0.34),
            bg_mg.animate.shift(UP * 0.34),
            label_mg.animate.shift(UP * 0.34),
            FadeOut(normal_vector),
            FadeOut(contact_callout),
            FadeIn(gap_group),
            run_time=1.2,
            rate_func=ease_out_cubic
        )

        # 7.0s - 8.5s: Red Warning Pulse & Hold for Cuepoint 2
        self.play(
            badge_derail[0].animate.set_stroke(color=RED_SHOCK, width=3.8),
            run_time=0.6
        )
        self.wait(0.9)  # Exact Cuepoint 2 = 8.5s

        # --- STEP 3: Flexible Crane Verification (8.5s to 14.2s) ---
        # 8.5s - 10.3s: Right Panel Morphs to Expanded Response Spectrum Analysis
        self.play(
            FadeOut(step2_group, shift=UP * 0.15),
            FadeIn(header3),
            Create(axes),
            FadeIn(x_label),
            FadeIn(y_label),
            FadeIn(tick_2s),
            FadeIn(tick_1g),
            Create(thresh_line),
            FadeIn(thresh_label),
            Create(spectrum_curve),
            card_bg.animate.set_stroke(color=CARD_STROKE, width=2.0),
            run_time=1.8
        )

        # 10.3s - 11.5s: Operating Point Highlight (tau_n = 2.0s -> Sa = 0.25g) & Calculation
        self.play(
            Create(proj_v),
            Create(proj_h),
            FadeIn(pt_dot, scale=1.3),
            FadeIn(pt_badge),
            FadeIn(calc_sa),
            Write(calc_nmin),
            run_time=1.2
        )

        # 11.5s - 12.7s: Wheel Returns Firmly to Rail, Clamped by Gravity (N_min = 0.75 mg > 0)
        self.play(
            trolley_group.animate.shift(DOWN * 0.34),
            arrow_mg.animate.shift(DOWN * 0.34),
            bg_mg.animate.shift(DOWN * 0.34),
            label_mg.animate.shift(DOWN * 0.34),
            FadeOut(gap_group),
            FadeOut(seismic_pulse_group),
            FadeIn(safe_contact_group),
            card_bg.animate.set_stroke(color=GREEN_PASS, width=2.6),
            run_time=1.2,
            rate_func=ease_in_out_sine
        )

        # 12.7s - 13.5s: SAFE: NO DERAILMENT Badge Blooms with Radiant Green Halo
        self.play(
            FadeIn(badge_safe, scale=1.06),
            Create(safe_halo),
            run_time=0.8
        )

        # 13.5s - 14.2s: Hold for Cuepoint 3
        self.wait(0.7)  # Exact Cuepoint 3 = 14.2s

        # --- Settling buffer (14.2s to 15.0s) ---
        self.wait(0.8)  # Video concludes at 15.0s


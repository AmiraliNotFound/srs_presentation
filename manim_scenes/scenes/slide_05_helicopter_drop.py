"""
SLIDE-05: HelicopterDropScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Foundations & Modeling)

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas
  - Step 0 (0.0s - 3.0s): Physical schematic of helicopter drop container & cantilever bracket
  - Step 1 (3.0s - 7.5s): Base shock impact (100g half-sine, t0 = 100 ms)
  - Step 2 (7.5s - 13.0s): Dynamic cantilever flexure & governing root stress constraint (sigma_max <= 26 ksi)
"""

from manim import *
import numpy as np


class HelicopterDropScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (3Blue1Brown Aesthetic)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        SPRING_CYAN      = ManimColor("#58C4DD")   # Cantilever bracket
        FORCE_GOLD       = ManimColor("#FFB703")   # Tip mass (amber) / Peak
        DANGER_RED       = ManimColor("#FF644E")   # Shock pulse / ground impact / stress highlight
        SAFE_GREEN       = ManimColor("#83C167")   # Allowable limit (26 ksi)
        TEXT_WHITE       = ManimColor("#FFFFFF")
        TEXT_OFFWH       = ManimColor("#ECEFF4")
        TEXT_MUTED       = ManimColor("#94A3B8")
        TEXT_DIM         = ManimColor("#64748B")
        CONTAINER_DARK   = ManimColor("#1E293B")
        CONTAINER_STROKE = ManimColor("#475569")
        CONTAINER_ACCENT = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Minimal Floating Title (3 words, no banner, no rule)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Avionics Drop Shock}",
            font_size=38,
            color=TEXT_WHITE
        ).move_to([0, 3.35, 0])

        # ------------------------------------------------------------------
        # 3. Parametric Cantilever & Tip Mass Geometry Helper Functions
        # ------------------------------------------------------------------
        x0 = -5.025
        y0 = 0.20
        L  = 3.40
        h  = 0.18

        def get_cantilever_state(delta):
            xi_vals = np.linspace(0, L, 60)
            if abs(delta) < 1e-6:
                w_vals = np.zeros_like(xi_vals)
                theta = np.zeros_like(xi_vals)
            else:
                # Exact cubic deflection profile for clamped cantilever:
                # w(xi) = -delta * [1.5 * (xi/L)^2 - 0.5 * (xi/L)^3]
                w_vals = -delta * (1.5 * (xi_vals / L)**2 - 0.5 * (xi_vals / L)**3)
                w_prime = -delta * (3.0 * xi_vals / (L**2) - 1.5 * (xi_vals**2) / (L**3))
                theta = np.arctan(w_prime)

            top_pts = []
            bot_pts = []
            for i in range(len(xi_vals)):
                x = x0 + xi_vals[i]
                y = y0 + w_vals[i]
                th = theta[i]
                nx = -np.sin(th)
                ny = np.cos(th)
                top_pts.append([x + (h / 2.0) * nx, y + (h / 2.0) * ny, 0])
                bot_pts.append([x - (h / 2.0) * nx, y - (h / 2.0) * ny, 0])

            beam_poly = Polygon(
                *(top_pts + bot_pts[::-1]),
                stroke_color=SPRING_CYAN,
                stroke_width=2.0,
                fill_color=SPRING_CYAN,
                fill_opacity=0.88
            )

            tip_x = x0 + L
            tip_y = y0 + w_vals[-1]
            tip_angle = theta[-1]
            return beam_poly, tip_x, tip_y, tip_angle

        def get_pcb_mass(tip_x, tip_y, tip_angle, w_m=0.85, h_m=0.52):
            box = RoundedRectangle(
                corner_radius=0.06,
                width=w_m,
                height=h_m,
                color=FORCE_GOLD,
                stroke_width=2.2,
                fill_color=FORCE_GOLD,
                fill_opacity=0.92
            )
            chip = Rectangle(
                width=0.32,
                height=0.24,
                color=ManimColor("#78350F"),
                stroke_width=1.2,
                fill_color=CONTAINER_DARK,
                fill_opacity=1.0
            )
            pin1 = Line(LEFT * 0.18, LEFT * 0.15, color=FORCE_GOLD, stroke_width=1.5)
            pin2 = Line(RIGHT * 0.15, RIGHT * 0.18, color=FORCE_GOLD, stroke_width=1.5)
            pcb = VGroup(box, chip, pin1, pin2)

            center_x = tip_x + (w_m / 2.0) * np.cos(tip_angle)
            center_y = tip_y + (w_m / 2.0) * np.sin(tip_angle)
            pcb.move_to([center_x, center_y, 0])
            pcb.rotate(tip_angle, about_point=[center_x, center_y, 0])
            return pcb

        # ------------------------------------------------------------------
        # 4. Construct Container Structure (Floor, Left Wall, Clamping)
        # ------------------------------------------------------------------
        wall = Rectangle(
            width=0.35,
            height=3.6,
            color=CONTAINER_STROKE,
            stroke_width=2.0,
            fill_color=CONTAINER_DARK,
            fill_opacity=1.0
        ).move_to([-5.20, 0.0, 0])

        wall_hatches = VGroup(*[
            Line(
                [-5.55, y - 0.15, 0],
                [-5.375, y + 0.05, 0],
                color=CONTAINER_ACCENT,
                stroke_width=1.5
            )
            for y in np.linspace(-1.6, 1.6, 9)
        ])

        clamp_mount = Rectangle(
            width=0.20,
            height=0.55,
            color=CONTAINER_STROKE,
            stroke_width=1.8,
            fill_color=CONTAINER_ACCENT,
            fill_opacity=1.0
        ).move_to([-5.025, 0.20, 0])

        bolt1 = Dot([-5.025, 0.36, 0], radius=0.035, color=TEXT_MUTED)
        bolt2 = Dot([-5.025, 0.04, 0], radius=0.035, color=TEXT_MUTED)

        floor = Rectangle(
            width=5.0,
            height=0.30,
            color=CONTAINER_STROKE,
            stroke_width=2.0,
            fill_color=CONTAINER_DARK,
            fill_opacity=1.0
        ).move_to([-2.90, -1.80, 0])

        ceiling = Line([-5.375, 1.80, 0], [-0.40, 1.80, 0], color=CONTAINER_ACCENT, stroke_width=2.0)
        right_border = DashedLine(
            [-0.40, 1.80, 0],
            [-0.40, -1.65, 0],
            color=CONTAINER_ACCENT,
            stroke_width=1.5,
            dash_length=0.15
        )

        ground_line = Line([-5.85, -1.95, 0], [0.05, -1.95, 0], color=CONTAINER_STROKE, stroke_width=2.5)
        ground_hatches = VGroup(*[
            Line(
                [x, -1.95, 0],
                [x - 0.22, -2.25, 0],
                color=CONTAINER_ACCENT,
                stroke_width=1.5
            )
            for x in np.linspace(-5.6, -0.1, 16)
        ])

        container_grp = VGroup(
            wall, wall_hatches, clamp_mount, bolt1, bolt2,
            floor, ceiling, right_border, ground_line, ground_hatches
        )

        # ------------------------------------------------------------------
        # 5. Cantilever Beam, PCB Mass & Dimensions (Straight State: Step 0)
        # ------------------------------------------------------------------
        beam0, tx0, ty0, th0 = get_cantilever_state(0.0)
        pcb0 = get_pcb_mass(tx0, ty0, th0)

        lbl_mass0 = MathTex(
            r"W_{\mathrm{PCB}} = 0.4\text{ lb}",
            font_size=24,
            color=FORCE_GOLD
        ).next_to(pcb0, UP, buff=0.18)

        # Dimension annotations (placed with clear vertical headroom, zero overlap)
        dim_l_arrow = DoubleArrow(
            start=[x0, 1.20, 0],
            end=[x0 + L, 1.20, 0],
            color=TEXT_MUTED,
            buff=0,
            tip_length=0.13,
            stroke_width=1.8
        )
        tick_root = Line([x0, 1.05, 0], [x0, 1.35, 0], color=TEXT_DIM, stroke_width=1.5)
        tick_tip  = Line([x0 + L, 1.05, 0], [x0 + L, 1.35, 0], color=TEXT_DIM, stroke_width=1.5)
        lbl_l     = MathTex(r"l = 10''", font_size=25, color=TEXT_OFFWH).next_to(dim_l_arrow, UP, buff=0.08)
        dim_l_grp = VGroup(dim_l_arrow, tick_root, tick_tip, lbl_l)

        lbl_d = MathTex(r"d = \text{?}", font_size=25, color=SPRING_CYAN)
        lbl_b = MathTex(r"b = 0.5''", font_size=23, color=TEXT_MUTED)
        dim_bot_grp = VGroup(lbl_d, lbl_b).arrange(RIGHT, buff=0.45).move_to([-3.325, -0.42, 0])
        arrow_d = Arrow(
            start=[-3.75, -0.30, 0],
            end=[-3.75, 0.09, 0],
            color=SPRING_CYAN,
            stroke_width=1.8,
            tip_length=0.10
        )
        dim_props_grp = VGroup(dim_bot_grp, arrow_d)
        dims_group = VGroup(dim_l_grp, dim_props_grp)

        # ------------------------------------------------------------------
        # 6. Step 1 Elements: Ground Impact & Shock Pulse Plot
        # ------------------------------------------------------------------
        ground_impact = Line([-5.85, -1.95, 0], [0.05, -1.95, 0], color=DANGER_RED, stroke_width=5.5)
        ripple1 = Arc(
            radius=0.45,
            start_angle=0,
            angle=-PI,
            color=DANGER_RED,
            stroke_width=2.4,
            arc_center=[-2.90, -1.95, 0]
        )
        ripple2 = Arc(
            radius=0.85,
            start_angle=0,
            angle=-PI,
            color=DANGER_RED,
            stroke_width=1.6,
            arc_center=[-2.90, -1.95, 0]
        )
        accel_arrow = Arrow(
            start=[-2.90, -3.20, 0],
            end=[-2.90, -1.98, 0],
            color=DANGER_RED,
            stroke_width=5.0,
            tip_length=0.25
        )
        accel_lbl = MathTex(r"\ddot{y}(t)", font_size=32, color=DANGER_RED).next_to(accel_arrow, LEFT, buff=0.14)
        impact_grp = VGroup(ground_impact, ripple1, ripple2, accel_arrow, accel_lbl)

        # Right Half Shock Pulse Plot
        ax = Axes(
            x_range=[0, 1.4, 0.5],
            y_range=[0, 1.25, 0.5],
            x_length=4.8,
            y_length=2.5,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([3.70, 0.35, 0])

        lbl_t = Tex(r"Time $t$", font_size=18, color=TEXT_MUTED).next_to(ax.c2p(1.4, 0), RIGHT, buff=0.10)
        lbl_a = MathTex(r"\ddot{y}", font_size=20, color=TEXT_MUTED).next_to(ax.c2p(0, 1.25), UP, buff=0.08)

        t_vals = np.linspace(0, 1.0, 100)
        pts_sine = [ax.c2p(t, 1.0 * np.sin(np.pi * t)) for t in t_vals]
        pts_flat = [ax.c2p(t, 0.0) for t in np.linspace(1.0, 1.35, 30)]
        pulse_curve = VMobject().set_points_smoothly(pts_sine + pts_flat).set_color(DANGER_RED).set_stroke(width=3.8)

        area_pts = [ax.c2p(0, 0)] + pts_sine + [ax.c2p(1.0, 0)]
        pulse_fill = Polygon(*area_pts, color=DANGER_RED, stroke_width=0, fill_color=DANGER_RED, fill_opacity=0.16)

        peak_line = DashedLine(ax.c2p(0, 1.0), ax.c2p(0.5, 1.0), color=FORCE_GOLD, stroke_width=1.4, dash_length=0.10)
        peak_dot  = Dot(ax.c2p(0.5, 1.0), radius=0.05, color=FORCE_GOLD)
        lbl_peak  = MathTex(r"100g", font_size=24, color=FORCE_GOLD).next_to(ax.c2p(0, 1.0), LEFT, buff=0.10)

        t0_line = DashedLine(ax.c2p(1.0, 0), ax.c2p(1.0, 1.0), color=TEXT_DIM, stroke_width=1.2, dash_length=0.10)
        lbl_t0  = MathTex(r"t_0 = 100\text{ ms}", font_size=23, color=TEXT_OFFWH).next_to(ax.c2p(1.0, 0), DOWN, buff=0.20)

        formula_pulse = MathTex(
            r"\ddot{y}(t) = 100g \sin\left(\frac{\pi t}{t_0}\right)",
            font_size=32,
            color=DANGER_RED
        ).next_to(ax, UP, buff=0.35)

        pulse_grp = VGroup(
            ax, lbl_t, lbl_a, pulse_fill, pulse_curve,
            peak_line, peak_dot, lbl_peak, t0_line, lbl_t0, formula_pulse
        )

        # ------------------------------------------------------------------
        # 7. Step 2 Elements: Dynamic Cantilever Flexure & Stress Goal
        # ------------------------------------------------------------------
        beam1, tx1, ty1, th1 = get_cantilever_state(0.85)
        pcb1 = get_pcb_mass(tx1, ty1, th1)

        lbl_mass1 = MathTex(
            r"W_{\mathrm{PCB}} = 0.4\text{ lb}",
            font_size=24,
            color=FORCE_GOLD
        ).next_to(pcb1, UP, buff=0.18)

        # Root stress concentration highlight
        stress_arc = Arc(
            radius=0.22,
            start_angle=0,
            angle=PI,
            color=DANGER_RED,
            stroke_width=4.0,
            arc_center=[-4.88, 0.29, 0]
        )
        stress_dot = Dot([-4.88, 0.29, 0], radius=0.07, color=FORCE_GOLD)
        lbl_sigma  = MathTex(r"\sigma_{\max}", font_size=28, color=DANGER_RED).next_to(stress_arc, UP, buff=0.10)
        root_stress_grp = VGroup(stress_arc, stress_dot, lbl_sigma)

        # Governing design constraint
        constraint = MathTex(
            r"\sigma_{\max}",
            r"\ \le \ ",
            r"26\text{ ksi}",
            font_size=42
        ).move_to([3.70, -1.85, 0])
        constraint[0].set_color(FORCE_GOLD)
        constraint[1].set_color(TEXT_WHITE)
        constraint[2].set_color(SAFE_GREEN)

        goal_lbl = MathTex(
            r"\text{Find required thickness } d",
            font_size=25,
            color=SPRING_CYAN
        ).next_to(constraint, DOWN, buff=0.22)
        constraint_grp = VGroup(constraint, goal_lbl)

        # ==================================================================
        # TIMELINE CHOREOGRAPHY & FRAME-ACCURATE CUEPOINTS
        # ==================================================================

        # --- STEP 0: Physical Schematic (0.0s - 3.0s -> Cuepoint 0 = 3.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.6)
        self.play(
            FadeIn(container_grp),
            FadeIn(beam0),
            FadeIn(pcb0),
            FadeIn(lbl_mass0),
            run_time=0.8
        )
        self.play(FadeIn(dims_group, shift=UP * 0.10), run_time=0.6)
        self.wait(1.0)  # Reaches exactly 3.0s

        # --- STEP 1: Base Shock Impact (3.0s - 7.5s -> Cuepoint 1 = 7.5s) ---
        self.play(
            FadeIn(ground_impact),
            FadeIn(ripple1, scale=0.5),
            FadeIn(ripple2, scale=0.5),
            GrowArrow(accel_arrow),
            FadeIn(accel_lbl, shift=RIGHT * 0.10),
            run_time=1.2
        )
        self.play(
            FadeIn(ax),
            FadeIn(lbl_t),
            FadeIn(lbl_a),
            Write(formula_pulse),
            Create(pulse_curve),
            FadeIn(pulse_fill),
            FadeIn(peak_line),
            FadeIn(peak_dot),
            FadeIn(lbl_peak),
            FadeIn(t0_line),
            FadeIn(lbl_t0),
            run_time=1.8
        )
        self.wait(1.5)  # Reaches exactly 7.5s

        # --- STEP 2: Cantilever Flexure & Constraint (7.5s - 13.0s -> Cuepoint 2 = 13.0s) ---
        self.play(
            FadeOut(dims_group, run_time=0.4),
            Transform(beam0, beam1, run_time=1.6, rate_func=rush_into),
            Transform(pcb0, pcb1, run_time=1.6, rate_func=rush_into),
            Transform(lbl_mass0, lbl_mass1, run_time=1.6, rate_func=rush_into),
        )
        self.play(
            FadeIn(root_stress_grp, scale=0.8),
            Write(constraint),
            FadeIn(goal_lbl, shift=UP * 0.10),
            run_time=1.2
        )
        self.wait(2.7)  # Reaches exactly 13.0s

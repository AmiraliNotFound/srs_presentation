"""
SLIDE-06: RayleighSDOFScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Foundations & Modeling)

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Exactly 3 words: "Continuous to SDOF")
  - Step 0 (0.0s - 3.0s): Continuous cantilever beam with distributed mass rho*b*d*l and tip mass m_PCB
  - Step 1 (3.0s - 7.5s): Rayleigh energy condensation -> lumped tip mass m_eq = m_PCB + 0.23*m_beam
  - Step 2 (7.5s - 13.0s): Beam stiffness morphs into equivalent spring k = E*b*d^3/(4*l^3) & tau_n = 2*pi*sqrt(m_eq/k)
"""

from manim import *
import numpy as np


def get_horizontal_spring(start, end, num_coils=7, height=0.42, color=ManimColor("#58C4DD"), stroke_width=2.8):
    """Generates a clean horizontal zigzag coiled spring VMobject."""
    x0, y0 = start[0], start[1]
    x1, y1 = end[0], end[1]
    lead = 0.22
    coil_x0 = x0 + lead
    coil_x1 = x1 - lead
    total_coil_dx = coil_x1 - coil_x0
    pts = [start, np.array([coil_x0, y0, 0])]
    num_pts = num_coils * 2
    for i in range(num_pts):
        fraction = (i + 0.5) / num_pts
        x = coil_x0 + fraction * total_coil_dx
        side = 1.0 if (i % 2 == 0) else -1.0
        y = y0 + side * (height / 2.0)
        pts.append(np.array([x, y, 0]))
    pts.append(np.array([coil_x1, y1, 0]))
    pts.append(end)
    return VMobject().set_points_as_corners(pts).set_color(color).set_stroke(width=stroke_width)


class RayleighSDOFScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (3Blue1Brown Aesthetic)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        AMBER       = ManimColor("#FFB703")   # Continuous Beam & Lumped Mass
        CYAN        = ManimColor("#58C4DD")   # Flexural Spring & Stiffness
        YELLOW      = ManimColor("#F7CA3B")   # Natural Period / Time
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        WALL_DARK   = ManimColor("#1E293B")
        WALL_STROKE = ManimColor("#475569")
        WALL_ACCENT = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Minimal Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Continuous to SDOF}",
            font_size=36,
            color=TEXT_WHITE
        ).move_to([0, 3.35, 0])

        # ------------------------------------------------------------------
        # 3. Geometric Parameters for Clamped Wall, Beam & Lumped Mass
        # ------------------------------------------------------------------
        x0 = -4.825
        y0 = 0.60
        L  = 3.60
        h  = 0.20
        w_m = 0.90
        h_m = 0.55

        def get_cantilever_state(delta, opacity=0.88):
            xi_vals = np.linspace(0, L, 60)
            if abs(delta) < 1e-6:
                w_vals = np.zeros_like(xi_vals)
                theta = np.zeros_like(xi_vals)
            else:
                w_vals = delta * (1.5 * (xi_vals / L)**2 - 0.5 * (xi_vals / L)**3)
                w_prime = delta * (3.0 * xi_vals / (L**2) - 1.5 * (xi_vals**2) / (L**3))
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
                stroke_color=AMBER,
                stroke_width=2.0,
                fill_color=AMBER,
                fill_opacity=opacity
            )

            tip_x = x0 + L
            tip_y = y0 + w_vals[-1]
            tip_angle = theta[-1]
            return beam_poly, tip_x, tip_y, tip_angle

        def get_pcb_mass(tip_x, tip_y, tip_angle):
            box = RoundedRectangle(
                corner_radius=0.08,
                width=w_m,
                height=h_m,
                color=AMBER,
                stroke_width=2.2,
                fill_color=AMBER,
                fill_opacity=0.92
            )
            chip = Rectangle(
                width=0.34,
                height=0.25,
                color=ManimColor("#78350F"),
                stroke_width=1.2,
                fill_color=WALL_DARK,
                fill_opacity=1.0
            )
            pin1 = Line(LEFT * 0.19, LEFT * 0.16, color=AMBER, stroke_width=1.5)
            pin2 = Line(RIGHT * 0.16, RIGHT * 0.19, color=AMBER, stroke_width=1.5)
            pcb = VGroup(box, chip, pin1, pin2)

            center_x = tip_x + (w_m / 2.0) * np.cos(tip_angle)
            center_y = tip_y + (w_m / 2.0) * np.sin(tip_angle)
            pcb.move_to([center_x, center_y, 0])
            pcb.rotate(tip_angle, about_point=[center_x, center_y, 0])
            return pcb

        def get_pcb_mass_fixed_x(center_x, center_y):
            box = RoundedRectangle(
                corner_radius=0.08,
                width=w_m,
                height=h_m,
                color=AMBER,
                stroke_width=2.2,
                fill_color=AMBER,
                fill_opacity=0.92
            )
            chip = Rectangle(
                width=0.34,
                height=0.25,
                color=ManimColor("#78350F"),
                stroke_width=1.2,
                fill_color=WALL_DARK,
                fill_opacity=1.0
            )
            pin1 = Line(LEFT * 0.19, LEFT * 0.16, color=AMBER, stroke_width=1.5)
            pin2 = Line(RIGHT * 0.16, RIGHT * 0.19, color=AMBER, stroke_width=1.5)
            pcb = VGroup(box, chip, pin1, pin2)
            pcb.move_to([center_x, center_y, 0])
            return pcb

        def get_pcb_label(tip_x, tip_y, tip_angle, tex_str=r"m_{\text{PCB}}"):
            center_x = tip_x + (w_m / 2.0) * np.cos(tip_angle)
            center_y = tip_y + (w_m / 2.0) * np.sin(tip_angle)
            norm_x = -np.sin(tip_angle)
            norm_y = np.cos(tip_angle)
            pos = [
                center_x + (h_m / 2.0 + 0.22) * norm_x,
                center_y + (h_m / 2.0 + 0.22) * norm_y,
                0
            ]
            return MathTex(tex_str, font_size=28, color=AMBER).move_to(pos)

        def get_beam_label(delta):
            mid_w = delta * (1.5 * 0.25 - 0.5 * 0.125)
            return MathTex(
                r"\rho b d l",
                font_size=28,
                color=TEXT_OFFWH
            ).move_to([x0 + L / 2.0, y0 + mid_w + 0.38, 0])

        # ------------------------------------------------------------------
        # 4. Clamped Support / Wall Construction
        # ------------------------------------------------------------------
        wall = Rectangle(
            width=0.35,
            height=2.5,
            color=WALL_STROKE,
            stroke_width=2.0,
            fill_color=WALL_DARK,
            fill_opacity=1.0
        ).move_to([-5.05, y0, 0])

        wall_hatches = VGroup(*[
            Line(
                [-5.40, y - 0.15, 0],
                [-5.225, y + 0.05, 0],
                color=WALL_ACCENT,
                stroke_width=1.5
            )
            for y in np.linspace(y0 - 1.1, y0 + 1.1, 8)
        ])

        clamp_plate = Rectangle(
            width=0.18,
            height=0.60,
            color=WALL_STROKE,
            stroke_width=1.8,
            fill_color=WALL_ACCENT,
            fill_opacity=1.0
        ).move_to([-4.875, y0, 0])

        bolt1 = Dot([-4.875, y0 + 0.18, 0], radius=0.035, color=TEXT_MUTED)
        bolt2 = Dot([-4.875, y0 - 0.18, 0], radius=0.035, color=TEXT_MUTED)

        wall_group = VGroup(wall, wall_hatches, clamp_plate, bolt1, bolt2)

        # ------------------------------------------------------------------
        # 5. Baseline State (Step 0: Continuous Beam & Labels)
        # ------------------------------------------------------------------
        beam0, tx0, ty0, th0 = get_cantilever_state(0.0)
        pcb0 = get_pcb_mass(tx0, ty0, th0)
        lbl_pcb0 = get_pcb_label(tx0, ty0, th0, r"m_{\text{PCB}}")
        lbl_beam0 = get_beam_label(0.0)

        # ------------------------------------------------------------------
        # 6. Step 1 Elements: Mass Condensation & Rayleigh Formula
        # ------------------------------------------------------------------
        formula_meq = MathTex(
            r"m_{\text{eq}}", r"=", r"m_{\text{PCB}}", r"+", r"0.23", r"\,m_{\text{beam}}",
            font_size=38
        ).move_to([2.90, y0, 0])
        formula_meq[0].set_color(AMBER)
        formula_meq[1].set_color(TEXT_WHITE)
        formula_meq[2].set_color(AMBER)
        formula_meq[3].set_color(TEXT_WHITE)
        formula_meq[4].set_color(YELLOW)
        formula_meq[5].set_color(CYAN)

        lbl_meq = MathTex(r"m_{\text{eq}}", font_size=28, color=AMBER).move_to(lbl_pcb0.get_center())

        # ------------------------------------------------------------------
        # 7. Step 2 Elements: Stiffness Formula & Period Equation
        # ------------------------------------------------------------------
        spring0 = get_horizontal_spring(
            start=np.array([x0, y0, 0]),
            end=np.array([tx0, y0, 0]),
            num_coils=7,
            height=0.42,
            color=CYAN,
            stroke_width=2.8
        )

        formula_k = MathTex(
            r"k", r"=", r"\frac{E b \, d^3}{4 l^3}",
            font_size=36
        ).move_to([-3.025, y0 + 1.25, 0])
        formula_k[0].set_color(CYAN)
        formula_k[1].set_color(TEXT_WHITE)
        formula_k[2].set_color(TEXT_OFFWH)
        formula_k[2][2:4].set_color(YELLOW)

        formula_tau = MathTex(
            r"\tau_n", r"=", r"2\pi", r"\sqrt{\frac{m_{\text{eq}}}{k}}",
            font_size=48
        ).move_to([0.0, -1.80, 0])
        formula_tau[0].set_color(YELLOW)
        formula_tau[1].set_color(TEXT_WHITE)
        formula_tau[2].set_color(TEXT_WHITE)
        formula_tau[3].set_color(TEXT_WHITE)
        formula_tau[3][2:5].set_color(AMBER)
        formula_tau[3][6].set_color(CYAN)

        # ==================================================================
        # TIMELINE CHOREOGRAPHY & FRAME-ACCURATE CUEPOINTS
        # ==================================================================

        # --- STEP 0: Continuous Baseline & Dynamic Bending (0.0s - 3.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.6)
        self.play(
            FadeIn(wall_group),
            FadeIn(beam0),
            FadeIn(pcb0),
            FadeIn(lbl_pcb0),
            FadeIn(lbl_beam0),
            run_time=0.6
        )

        # Dynamic cantilever flexure (1.4s gentle damped vibration)
        vgroup_cantilever = VGroup(beam0, pcb0, lbl_pcb0, lbl_beam0)

        def flex_update(mob, alpha):
            delta = 0.40 * np.sin(2.0 * np.pi * 1.5 * alpha) * (1.0 - alpha)
            b_curr, tx, ty, th = get_cantilever_state(delta)
            p_curr = get_pcb_mass(tx, ty, th)
            lp_curr = get_pcb_label(tx, ty, th, r"m_{\text{PCB}}")
            lb_curr = get_beam_label(delta)
            mob[0].become(b_curr)
            mob[1].become(p_curr)
            mob[2].become(lp_curr)
            mob[3].become(lb_curr)

        self.play(UpdateFromAlphaFunc(vgroup_cantilever, flex_update), run_time=1.4, rate_func=linear)
        self.wait(0.4)  # Exact Cuepoint 0 = 3.0s

        # --- STEP 1: Rayleigh Mass Condensation (3.0s - 7.5s) ---
        # 1. Beam turns translucent & distributed label fades
        beam_translucent, _, _, _ = get_cantilever_state(0.0, opacity=0.18)
        self.play(
            FadeOut(lbl_beam0, run_time=0.4),
            Transform(beam0, beam_translucent, run_time=0.8),
        )

        # 2. Glowing mass condensation packets glide into tip mass
        packets = VGroup(*[
            Dot([x, y0, 0], radius=0.07, color=AMBER)
            for x in np.linspace(-4.3, -1.8, 6)
        ])
        self.play(FadeIn(packets, scale=0.5), run_time=0.3)
        self.play(
            LaggedStart(
                *[p.animate.move_to([tx0 + w_m / 2.0, y0, 0]).set_opacity(0) for p in packets],
                lag_ratio=0.10
            ),
            run_time=1.0
        )
        self.remove(packets)

        # 3. Tip mass absorbs kinetic energy, label transforms to m_eq
        self.play(
            pcb0.animate.scale(1.08),
            Transform(lbl_pcb0, lbl_meq),
            run_time=0.5
        )
        self.play(pcb0.animate.scale(1.0 / 1.08), run_time=0.3)

        # 4. Write Rayleigh equivalent mass formula
        self.play(Write(formula_meq), run_time=1.0)
        self.wait(0.6)  # Exact Cuepoint 1 = 7.5s

        # --- STEP 2: Flexural Stiffness Morph & Period (7.5s - 13.0s) ---
        # 1. Translucent beam morphs into equivalent coiled spring
        self.play(
            ReplacementTransform(beam0, spring0),
            Write(formula_k),
            run_time=1.4
        )

        # 2. Write master natural period formula
        self.play(Write(formula_tau), run_time=1.4)

        # 3. Harmonic SDOF oscillation resolving to calm resting state
        sdof_grp = VGroup(spring0, pcb0, lbl_pcb0)

        def sdof_osc_update(mob, alpha):
            disp = 0.32 * np.cos(2.0 * np.pi * 1.0 * alpha * 2.0) * np.exp(-2.2 * alpha)
            curr_spring = get_horizontal_spring(
                start=np.array([x0, y0, 0]),
                end=np.array([tx0 + disp, y0, 0]),
                num_coils=7,
                height=0.42,
                color=CYAN,
                stroke_width=2.8
            )
            curr_pcb = get_pcb_mass_fixed_x(center_x=tx0 + w_m / 2.0 + disp, center_y=y0)
            curr_lbl = MathTex(r"m_{\text{eq}}", font_size=28, color=AMBER).move_to([tx0 + w_m / 2.0 + disp, y0 + h_m / 2.0 + 0.22, 0])
            mob[0].become(curr_spring)
            mob[1].become(curr_pcb)
            mob[2].become(curr_lbl)

        self.play(UpdateFromAlphaFunc(sdof_grp, sdof_osc_update), run_time=2.0, rate_func=linear)
        self.wait(0.7)  # Exact Cuepoint 2 = 13.0s

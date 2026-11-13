"""
SLIDE-13: SRSConstructionScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 2 (Mathematical Theory & Derivations)
Allocated Time: 26:30 – 28:30 (120 s)

Strict 3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 6 English words total:
      "Constructing the SRS", "Primary", "Residual", "Maximax")
  - Frame-Accurate Step Cuepoints (3 Steps / 2 Pauses):
      Step 0 (0.0s - 4.0s): Minimal title & SDOF Oscillator Ensemble (tau_n,1 > tau_n,2 > tau_n,3)
      Step 1 (4.0s - 8.5s): Peak projection onto the dimensionless Spectrum Plane (t0/tau_n vs DLF)
      Step 2 (8.5s - 15.0s): Smooth emergence of continuous Primary, Residual & Maximax envelopes + Master DLF definition
"""

from manim import *
import numpy as np


def get_spring(start, end, num_coils=7, width=0.30, color=WHITE, stroke_width=2.2):
    """Generates a clean zigzag spring VMobject between start and end points."""
    lead = -0.16
    coil_start_y = start[1] + lead
    coil_end_y = end[1] - lead
    total_coil_dy = coil_end_y - coil_start_y
    pts = [start, np.array([start[0], coil_start_y, 0])]
    num_pts = num_coils * 2
    for i in range(num_pts):
        fraction = (i + 0.5) / num_pts
        y = coil_start_y + fraction * total_coil_dy
        side = 1 if (i % 2 == 0) else -1
        x = start[0] + side * (width / 2)
        pts.append(np.array([x, y, 0]))
    pts.append(np.array([end[0], coil_end_y, 0]))
    pts.append(end)
    return VMobject().set_points_as_corners(pts).set_color(color).set_stroke(width=stroke_width)


class SRSConstructionScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        CORAL      = ManimColor("#FF644E")   # Maximax Envelope & Critical Resonant Peak
        CYAN       = ManimColor("#58C4DD")   # Residual SRS Curve & Flexible Oscillator
        YELLOW     = ManimColor("#F7CA3B")   # Primary SRS Curve & Excitation
        AMBER      = ManimColor("#FFB703")   # SDOF Masses & Peak Displacements
        BLUE       = ManimColor("#0097F1")   # University of Tehran Primary Brand Accent
        TEXT_WHITE = ManimColor("#FFFFFF")
        TEXT_MUTED = ManimColor("#94A3B8")
        TEXT_DIM   = ManimColor("#475569")
        BORDER_MID = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Constructing the SRS}",
            font_size=46,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # ------------------------------------------------------------------
        # 3. Step 0: SDOF Oscillator Ensemble Configuration (Left Stage)
        # ------------------------------------------------------------------
        # 3 SDOF oscillators representing distinct physical regimes:
        #   Oscillator 1 (Left): Flexible / Impulsive regime (tau_n,1 large, t0/tau_n = 0.35)
        #   Oscillator 2 (Center): Resonant tuned regime (tau_n,2 approx 1.25 t0, t0/tau_n = 0.80)
        #   Oscillator 3 (Right): Stiff / Quasi-static regime (tau_n,3 small, t0/tau_n = 2.00)

        x_coords = [-5.2, -3.8, -2.4]
        y_ceil = 1.90
        y_eq = 0.45
        m_w, m_h = 0.85, 0.42

        # Overhead mounting ceiling
        ceil_line = Line([-5.9, y_ceil, 0], [-1.7, y_ceil, 0], color=TEXT_DIM, stroke_width=2.4)
        ceil_hatches = VGroup(*[
            Line([-5.8 + i * 0.22, y_ceil, 0], [-5.8 + i * 0.22 + 0.12, y_ceil + 0.12, 0], color=TEXT_DIM, stroke_width=1.2)
            for i in range(19)
        ])
        ceiling = VGroup(ceil_line, ceil_hatches)

        # Equilibrium reference baseline
        eq_line = DashedLine([-5.8, y_eq, 0], [-1.7, y_eq, 0], dash_length=0.08, color=BORDER_MID, stroke_width=1.2)

        # Initial resting state of oscillators
        springs_init = []
        masses_init = []
        labels_tau = []
        coil_counts = [4, 7, 11]
        spring_colors = [CYAN, AMBER, BLUE]
        tau_labels_tex = [r"\tau_{n,1}", r"\tau_{n,2}", r"\tau_{n,3}"]

        for i, (xc, coils, col, t_lbl) in enumerate(zip(x_coords, coil_counts, spring_colors, tau_labels_tex)):
            sp = get_spring(
                np.array([xc, y_ceil, 0]),
                np.array([xc, y_eq + m_h / 2, 0]),
                num_coils=coils,
                width=0.30 - i * 0.02,
                color=col,
                stroke_width=2.0 + i * 0.3
            )
            springs_init.append(sp)

            box = RoundedRectangle(
                width=m_w, height=m_h, corner_radius=0.08,
                color=col, stroke_width=2.2, fill_color=col, fill_opacity=0.20
            ).move_to([xc, y_eq, 0])
            txt_m = MathTex(r"m", font_size=20, color=TEXT_WHITE).move_to([xc, y_eq, 0])
            masses_init.append(VGroup(box, txt_m))

            # Placed comfortably below the lowest excursion (zero overlap with x_max)
            lbl = MathTex(t_lbl, font_size=20, color=TEXT_MUTED).move_to([xc, -1.80, 0])
            labels_tau.append(lbl)

        # Displaced peak state under the half-sine shock pulse
        # Deflections: delta_y1 = 0.65 (DLF = 1.23), delta_y2 = 1.25 (DLF = 1.77, resonant!), delta_y3 = 0.78 (DLF = 1.27)
        deflections = [0.65, 1.25, 0.78]
        springs_peak = []
        masses_peak = []
        peak_markers = VGroup()
        peak_points = []

        xmax_labels_tex = [r"x_{\max,1}", r"x_{\max,2}", r"x_{\max,3}"]
        xmax_colors = [CYAN, CORAL, BLUE]

        for i, (xc, coils, col, dy, x_lbl, xm_col) in enumerate(zip(
            x_coords, coil_counts, spring_colors, deflections, xmax_labels_tex, xmax_colors
        )):
            y_curr = y_eq - dy
            sp_p = get_spring(
                np.array([xc, y_ceil, 0]),
                np.array([xc, y_curr + m_h / 2, 0]),
                num_coils=coils,
                width=0.30 - i * 0.02,
                color=col,
                stroke_width=2.0 + i * 0.3
            )
            springs_peak.append(sp_p)

            box_p = RoundedRectangle(
                width=m_w, height=m_h, corner_radius=0.08,
                color=col, stroke_width=2.2, fill_color=col, fill_opacity=0.25
            ).move_to([xc, y_curr, 0])
            txt_mp = MathTex(r"m", font_size=20, color=TEXT_WHITE).move_to([xc, y_curr, 0])
            masses_peak.append(VGroup(box_p, txt_mp))

            # Peak marker tick & glowing dot with label placed cleanly to the left
            p_tick = Line([xc - 0.28, y_curr - m_h / 2, 0], [xc + 0.28, y_curr - m_h / 2, 0], color=xm_col, stroke_width=2.2)
            p_dot = Dot([xc, y_curr - m_h / 2, 0], color=xm_col, radius=0.07)
            p_halo = Dot([xc, y_curr - m_h / 2, 0], color=xm_col, radius=0.18, fill_opacity=0.35)
            p_lbl = MathTex(x_lbl, font_size=18, color=xm_col).next_to(p_tick, LEFT, buff=0.10)
            peak_markers.add(VGroup(p_tick, p_dot, p_halo, p_lbl))
            peak_points.append(np.array([xc, y_curr - m_h / 2, 0]))

        oscillators_init_grp = VGroup(
            ceiling, eq_line, *springs_init, *masses_init, *labels_tau
        )

        # ------------------------------------------------------------------
        # 4. Step 1: Spectrum Plane Geometry & Point Projections (Right Stage)
        # ------------------------------------------------------------------
        # Horizontal: t0 / tau_n in [0, 3.0]
        # Vertical: DLF in [0, 2.2]
        axes = Axes(
            x_range=[0, 3.0, 0.5],
            y_range=[0, 2.2, 0.5],
            x_length=5.8,
            y_length=3.6,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.6,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            }
        ).move_to([3.4, -0.7, 0])

        lbl_x = MathTex(r"t_0 / \tau_n", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(3.0, 0), RIGHT, buff=0.14)
        lbl_y = MathTex(r"\mathbf{DLF}", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(0, 2.2), UP, buff=0.12)

        # Static reference baseline DLF = 1.0 (static displacement delta_st)
        line_1 = DashedLine(axes.c2p(0, 1.0), axes.c2p(3.0, 1.0), dash_length=0.08, color=TEXT_DIM, stroke_width=1.2)
        lbl_1 = MathTex(r"1.0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, 1.0), LEFT, buff=0.10)
        lbl_0 = MathTex(r"0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, 0), LEFT, buff=0.10)

        # X-axis ticks
        x_ticks = VGroup()
        for val, txt in [(0.5, r"0.5"), (1.0, r"1.0"), (1.5, r"1.5"), (2.0, r"2.0"), (2.5, r"2.5"), (3.0, r"3.0")]:
            t_lbl = MathTex(txt, font_size=17, color=TEXT_MUTED).next_to(axes.c2p(val, 0), DOWN, buff=0.20)
            t_line = Line(axes.c2p(val, -0.05), axes.c2p(val, 0.05), stroke_width=1.2, color=TEXT_MUTED)
            x_ticks.add(t_lbl, t_line)

        # Highlighted critical tick at t0 / tau_n = 0.8
        lbl_08 = MathTex(r"0.8", font_size=17, color=YELLOW).next_to(axes.c2p(0.8, 0), DOWN, buff=0.20)
        tick_08 = Line(axes.c2p(0.8, -0.07), axes.c2p(0.8, 0.07), stroke_width=1.6, color=YELLOW)
        x_ticks.add(lbl_08, tick_08)

        axes_group = VGroup(axes, lbl_x, lbl_y, line_1, lbl_1, lbl_0, x_ticks)

        # Target spectrum coordinates for the 3 oscillators:
        #   Oscillator 1: t0/tau_n = 0.35, DLF approx 1.235 (Residual dominant)
        #   Oscillator 2: t0/tau_n = 0.80, DLF approx 1.768 (Resonant Primary peak)
        #   Oscillator 3: t0/tau_n = 2.00, DLF approx 1.267 (Forced Primary dominant)
        target_t = [0.35, 0.80, 2.00]
        target_dlf = [1.235, 1.768, 1.267]
        target_pts = [axes.c2p(t, d) for t, d in zip(target_t, target_dlf)]

        # Projection lines mapping oscillator peaks directly to spectrum plane
        # Using upward curved arcs for zero-crossing elegance
        projection_lines = VGroup()
        sample_dots_group = VGroup()

        for p_src, p_dst, col, t_val, d_val in zip(peak_points, target_pts, xmax_colors, target_t, target_dlf):
            # Upward arched mapping curve
            arc = ArcBetweenPoints(p_src, p_dst, angle=-0.32)
            p_arc = DashedVMobject(arc, num_dashes=24, dashed_ratio=0.55).set_color(col).set_stroke(width=1.5, opacity=0.80)
            projection_lines.add(p_arc)

            dot = Dot(p_dst, color=col, radius=0.08)
            halo = Dot(p_dst, color=col, radius=0.20, fill_opacity=0.35)
            drop_v = DashedLine(p_dst, axes.c2p(t_val, 0), dash_length=0.06, color=col, stroke_width=1.2, stroke_opacity=0.6)
            drop_h = DashedLine(axes.c2p(0, d_val), p_dst, dash_length=0.06, color=col, stroke_width=1.2, stroke_opacity=0.6)
            sample_dots_group.add(VGroup(dot, halo, drop_v, drop_h))

        # Peak 2 Callout (Resonant Dynamic Magnification)
        lbl_peak2 = MathTex(
            r"\mathbf{DLF}_{\max} \approx 1.76",
            font_size=20,
            color=CORAL
        ).next_to(target_pts[1], UP, buff=0.22)
        sample_dots_group.add(lbl_peak2)

        # ------------------------------------------------------------------
        # 5. Step 2: Continuous Spectrum Envelopes & Master Equation
        # ------------------------------------------------------------------
        # Analytical Half-Sine Primary & Residual Curves
        t_domain = np.linspace(0.05, 3.0, 320)
        pri_coords = []
        res_coords = []
        max_coords = []

        for T in t_domain:
            r = 1.0 / (2.0 * T)
            if np.isclose(T, 0.5, atol=1e-3):
                p = 1.570796
                res = 1.570796
            else:
                t_fine = np.linspace(0, T, 600)
                x1 = (1.0 / (1.0 - r**2)) * (np.sin(np.pi * t_fine / T) - r * np.sin(2.0 * np.pi * t_fine))
                p = np.max(np.abs(x1))
                res = np.abs((2.0 * r / (1.0 - r**2)) * np.cos(np.pi / (2.0 * r)))
            pri_coords.append(axes.c2p(T, p))
            res_coords.append(axes.c2p(T, res))
            max_coords.append(axes.c2p(T, max(p, res)))

        # Primary as dashed yellow curve, Residual as dashed cyan curve
        pri_raw = VMobject().set_points_smoothly(pri_coords)
        pri_curve = DashedVMobject(pri_raw, num_dashes=48, dashed_ratio=0.65).set_color(YELLOW).set_stroke(width=2.4)

        res_raw = VMobject().set_points_smoothly(res_coords)
        res_curve = DashedVMobject(res_raw, num_dashes=48, dashed_ratio=0.65).set_color(CYAN).set_stroke(width=2.2)

        # Maximax as bold solid coral red envelope
        max_curve = VMobject().set_points_smoothly(max_coords).set_color(CORAL).set_stroke(width=3.8)

        # Labels (Strict 10-Word Rule: Exactly 3 single words)
        lbl_pri = Tex(r"\textbf{Primary}", font_size=19, color=YELLOW).next_to(axes.c2p(2.7, 1.14), UP, buff=0.18)
        lbl_res = Tex(r"\textbf{Residual}", font_size=19, color=CYAN).next_to(axes.c2p(2.0, 0.53), DOWN, buff=0.16)
        lbl_max = Tex(r"\textbf{Maximax}", font_size=21, color=CORAL).next_to(axes.c2p(0.80, 1.77), UP, buff=0.20)
        curve_labels = VGroup(lbl_pri, lbl_res)

        # Master DLF Equation (Zero English words — purely mathematical)
        master_eq = MathTex(
            r"\mathbf{DLF}\left(\frac{t_0}{\tau_n}\right)",
            r"=",
            r"\frac{\max_{t \ge 0} |x(t)|}{\delta_{\text{st}}}",
            font_size=32
        ).move_to([3.4, 2.55, 0])
        master_eq[0][:3].set_color(CORAL)
        master_eq[0][3:].set_color(TEXT_WHITE)
        master_eq[1].set_color(TEXT_MUTED)
        master_eq[2][:12].set_color(AMBER)
        master_eq[2][12].set_color(TEXT_MUTED)
        master_eq[2][13:].set_color(BLUE)

        # ------------------------------------------------------------------
        # 6. Animation Sequence (3 Steps, 2 Cuepoint Pauses)
        # ------------------------------------------------------------------

        # --- STEP 0: Minimal Title & SDOF Oscillator Ensemble (0.0s - 4.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.5)
        self.play(FadeIn(oscillators_init_grp), run_time=0.8)

        # Animate shock pulse excitation: masses displace dynamically to peak excursion
        self.play(
            *[Transform(sp, sp_p) for sp, sp_p in zip(springs_init, springs_peak)],
            *[Transform(m, m_p) for m, m_p in zip(masses_init, masses_peak)],
            FadeIn(peak_markers, shift=DOWN * 0.10),
            run_time=1.8
        )
        self.wait(0.9)  # Exact Cuepoint 0 = 4.0s (Pauses on slide entry)

        # --- STEP 1: Projection onto Spectrum Plane (4.0s - 8.5s) ---
        self.play(FadeIn(axes_group), run_time=0.9)
        self.play(Create(projection_lines), run_time=1.4)
        self.play(FadeIn(sample_dots_group), run_time=1.0)
        self.wait(1.2)  # Exact Cuepoint 1 = 8.5s (Pauses for presenter explanation of peak mapping)

        # --- STEP 2: Continuous Maximax Envelope (8.5s - 15.0s) ---
        self.play(
            Create(pri_curve),
            Create(res_curve),
            FadeIn(curve_labels),
            run_time=1.5
        )
        self.play(
            Create(max_curve),
            FadeTransform(lbl_peak2, lbl_max),
            run_time=1.2
        )
        self.play(
            Write(master_eq),
            ceiling.animate.set_opacity(0.30),
            eq_line.animate.set_opacity(0.20),
            *[sp.animate.set_opacity(0.30) for sp in springs_init],
            *[m.animate.set_opacity(0.30) for m in masses_init],
            *[lbl.animate.set_opacity(0.30) for lbl in labels_tau],
            peak_markers.animate.set_opacity(0.30),
            FadeOut(projection_lines),
            run_time=1.3
        )
        self.play(
            Flash(axes.c2p(0.80, 1.768), color=CORAL, line_length=0.22, num_lines=8, flash_radius=0.35),
            run_time=0.6
        )
        self.wait(1.9)  # Exact Cuepoint 2 = 15.0s (Calm final resting frame for Person 2 delivery)

"""
SLIDE-14: AsymptoticLimitsScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 2 (Mathematical Theory & Derivations — Hand-Off to Person 3)
Allocated Time: 28:30 – 30:00 (90 s)

Strict 3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 7 English words total:
      "Asymptotic Limits", "Impulsive", "Dynamic", "Quasi-Static", "Applications", "Person")
  - Frame-Accurate Step Cuepoints (3 Steps / 2 Pauses):
      Step 0 (0.0s - 4.0s): Minimal title, Continuous Master SRS Curve & Impulsive Regime (t0 << tau_n)
      Step 1 (4.0s - 8.5s): Quasi-Static Regime (t0 >> tau_n, DLF -> 1.0)
      Step 2 (8.5s - 15.0s): Dynamic Amplification Peak & Hand-Off to Person 3 (Applications)
"""

from manim import *
import numpy as np


class AsymptoticLimitsScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        CORAL      = ManimColor("#FF644E")   # Impulsive Regime (Energy / Impulse Tangent)
        GREEN      = ManimColor("#83C167")   # Quasi-Static Regime (Static Equilibrium Limit)
        YELLOW     = ManimColor("#F7CA3B")   # Dynamic Resonance Zone (Severe Amplification)
        AMBER      = ManimColor("#FFB703")   # Dynamic Resonant Peak (DLF max approx 1.76)
        BLUE       = ManimColor("#0097F1")   # University of Tehran Primary Brand Accent
        CYAN       = ManimColor("#58C4DD")   # Master SRS Maximax Envelope
        TEXT_WHITE = ManimColor("#FFFFFF")
        TEXT_MUTED = ManimColor("#94A3B8")
        TEXT_DIM   = ManimColor("#475569")
        BORDER_MID = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 2 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Asymptotic Limits}",
            font_size=36,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # ------------------------------------------------------------------
        # 3. Master Spectrum Axes Configuration (Fullscreen Dimensionless Plane)
        # ------------------------------------------------------------------
        # Horizontal: t0 / tau_n in [0, 4.0]
        # Vertical: DLF in [0, 2.2]
        axes = Axes(
            x_range=[0, 4.0, 0.5],
            y_range=[0, 2.2, 0.5],
            x_length=10.6,
            y_length=4.0,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.6,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            }
        ).move_to([0, -1.05, 0])

        lbl_x = MathTex(r"t_0 / \tau_n", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(4.0, 0), RIGHT, buff=0.14)
        lbl_y = MathTex(r"\mathbf{DLF}", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(0, 2.2), UP, buff=0.12)

        # Static baseline reference DLF = 1.0
        line_static = DashedLine(
            axes.c2p(0, 1.0), axes.c2p(4.0, 1.0),
            dash_length=0.08, color=TEXT_DIM, stroke_width=1.3
        )
        lbl_1 = MathTex(r"1.0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, 1.0), LEFT, buff=0.10)
        lbl_0 = MathTex(r"0", font_size=18, color=TEXT_MUTED).next_to(axes.c2p(0, 0), LEFT, buff=0.10)

        # X-axis ticks
        x_ticks = VGroup()
        for val in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]:
            t_lbl = MathTex(f"{val:g}", font_size=16, color=TEXT_MUTED).next_to(axes.c2p(val, 0), DOWN, buff=0.18)
            t_line = Line(axes.c2p(val, -0.05), axes.c2p(val, 0.05), stroke_width=1.2, color=TEXT_MUTED)
            x_ticks.add(t_lbl, t_line)

        axes_group = VGroup(axes, lbl_x, lbl_y, line_static, lbl_1, lbl_0, x_ticks)

        # ------------------------------------------------------------------
        # 4. Continuous Master SRS Waveform (Half-Sine Maximax Envelope)
        # ------------------------------------------------------------------
        def calc_dlf(T):
            if np.isclose(T, 0.5, atol=1e-3):
                return np.pi / 2.0
            r = 1.0 / (2.0 * T)
            t_fine = np.linspace(0, T, 400)
            x1 = (1.0 / (1.0 - r**2)) * (np.sin(np.pi * t_fine / T) - r * np.sin(2.0 * np.pi * t_fine))
            p = np.max(np.abs(x1))
            res = np.abs((2.0 * r / (1.0 - r**2)) * np.cos(np.pi / (2.0 * r)))
            return max(p, res)

        t_domain = np.linspace(0.01, 4.0, 400)
        srs_coords = [axes.c2p(T, calc_dlf(T)) for T in t_domain]
        srs_curve = VMobject().set_points_smoothly(srs_coords).set_color(CYAN).set_stroke(width=3.6)

        # ------------------------------------------------------------------
        # 5. Step 0: Impulsive Limit Elements (Far Left: t0 << tau_n)
        # ------------------------------------------------------------------
        # Translucent shaded polygon for impulsive regime (0 <= T <= 0.40)
        imp_pts = [axes.c2p(0, 0)]
        for T in np.linspace(0.01, 0.40, 50):
            imp_pts.append(axes.c2p(T, calc_dlf(T)))
        imp_pts.append(axes.c2p(0.40, 0))
        imp_pts.append(axes.c2p(0, 0))
        imp_poly = Polygon(*imp_pts, stroke_width=0, fill_color=CORAL, fill_opacity=0.22)

        # Linear tangent asymptote line (slope = 4)
        imp_tangent = DashedLine(
            axes.c2p(0, 0), axes.c2p(0.44, 1.76),
            dash_length=0.07, color=CORAL, stroke_width=2.4
        )

        # Region Tag (Strict 10-Word Rule: 1 word)
        lbl_imp = Tex(r"\textbf{Impulsive}", font_size=19, color=CORAL).move_to([axes.c2p(0.20, 0)[0], -2.20, 0])

        # Mathematical Governing Equation at Top Left
        eq_imp = MathTex(
            r"t_0 \ll \tau_n \implies x_{\max} = \frac{\mathcal{I}}{m\omega_n}, \quad \mathbf{DLF} \to 0",
            font_size=21
        ).move_to([-4.70, 2.52, 0])
        eq_imp[0][:7].set_color(CORAL)
        eq_imp[0][7].set_color(TEXT_MUTED)
        eq_imp[0][8:16].set_color(TEXT_WHITE)
        eq_imp[0][16].set_color(TEXT_MUTED)
        eq_imp[0][17:].set_color(CORAL)

        # ------------------------------------------------------------------
        # 6. Step 1: Quasi-Static Limit Elements (Far Right: t0 >> tau_n)
        # ------------------------------------------------------------------
        # Translucent shaded polygon for quasi-static regime (2.40 <= T <= 4.0)
        stat_pts = [axes.c2p(2.40, 0)]
        for T in np.linspace(2.40, 4.0, 60):
            stat_pts.append(axes.c2p(T, calc_dlf(T)))
        stat_pts.append(axes.c2p(4.0, 0))
        stat_pts.append(axes.c2p(2.40, 0))
        stat_poly = Polygon(*stat_pts, stroke_width=0, fill_color=GREEN, fill_opacity=0.18)

        # Static horizontal asymptote line (Green)
        stat_line = DashedLine(
            axes.c2p(2.20, 1.0), axes.c2p(4.0, 1.0),
            dash_length=0.08, color=GREEN, stroke_width=2.8
        )

        # Region Tag (Strict 10-Word Rule: 1 word)
        lbl_stat = Tex(r"\textbf{Quasi-Static}", font_size=19, color=GREEN).move_to([axes.c2p(3.20, 0)[0], -2.20, 0])

        # Mathematical Governing Equation at Top Right
        eq_stat = MathTex(
            r"t_0 \gg \tau_n \implies \mathbf{DLF} \to 1.0",
            font_size=22
        ).move_to([4.60, 2.52, 0])
        eq_stat[0][:7].set_color(GREEN)
        eq_stat[0][7].set_color(TEXT_MUTED)
        eq_stat[0][8:].set_color(GREEN)

        # ------------------------------------------------------------------
        # 7. Step 2: Dynamic Resonance Zone & Hand-Off Elements
        # ------------------------------------------------------------------
        # Translucent shaded polygon for dynamic resonance zone (0.50 <= T <= 2.0)
        dyn_pts = [axes.c2p(0.50, 0)]
        for T in np.linspace(0.50, 2.0, 60):
            dyn_pts.append(axes.c2p(T, calc_dlf(T)))
        dyn_pts.append(axes.c2p(2.0, 0))
        dyn_pts.append(axes.c2p(0.50, 0))
        dyn_poly = Polygon(*dyn_pts, stroke_width=0, fill_color=YELLOW, fill_opacity=0.18)

        # Resonant peak marker at t0 / tau_n = 0.80, DLF approx 1.768
        peak_pt = axes.c2p(0.80, 1.768)
        peak_dot = Dot(peak_pt, color=AMBER, radius=0.08)
        peak_halo = Dot(peak_pt, color=AMBER, radius=0.22, fill_opacity=0.35)
        lbl_peak = MathTex(r"\mathbf{DLF}_{\max} \approx 1.76", font_size=20, color=AMBER).next_to(peak_pt, UP, buff=0.16)
        peak_group = VGroup(peak_dot, peak_halo, lbl_peak)

        # Region Tag (Strict 10-Word Rule: 1 word)
        lbl_dyn = Tex(r"\textbf{Dynamic}", font_size=19, color=YELLOW).move_to([axes.c2p(1.25, 0)[0], -2.20, 0])

        # Mathematical Governing Equation at Top Center
        eq_dyn = MathTex(
            r"0.5 \le \frac{t_0}{\tau_n} \le 2.0 \implies \mathbf{DLF} \approx 1.5 - 2.0",
            font_size=21
        ).move_to([0, 2.52, 0])
        eq_dyn[0][:11].set_color(YELLOW)
        eq_dyn[0][11].set_color(TEXT_MUTED)
        eq_dyn[0][12:].set_color(AMBER)

        # Hand-off forward indicator badge to Person 3 (Strict 10-Word Rule: 2 words)
        handoff_box = RoundedRectangle(
            width=4.4, height=0.58, corner_radius=0.10,
            color=BLUE, stroke_width=1.6, fill_color=BLUE, fill_opacity=0.16
        ).move_to([0, 1.82, 0])
        handoff_text = MathTex(
            r"\implies \text{Applications (Person 3)}",
            font_size=23,
            color=TEXT_WHITE
        ).move_to([0, 1.82, 0])
        handoff_text[0][:1].set_color(BLUE)
        handoff_text[0][1:].set_color(TEXT_WHITE)
        handoff_group = VGroup(handoff_box, handoff_text)

        # ------------------------------------------------------------------
        # 8. Animation Sequence (3 Steps, 2 Cuepoint Pauses)
        # ------------------------------------------------------------------

        # --- STEP 0: Minimal Title, SRS Curve & Impulsive Limit (0.0s - 4.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.5)
        self.play(
            FadeIn(axes_group),
            Create(srs_curve),
            run_time=1.3
        )
        self.play(
            FadeIn(imp_poly),
            Create(imp_tangent),
            FadeIn(lbl_imp),
            Write(eq_imp),
            run_time=1.3
        )
        self.wait(0.9)  # Exact Cuepoint 0 = 4.0s (Pauses on slide entry)

        # --- STEP 1: Quasi-Static Limit (4.0s - 8.5s) ---
        self.play(
            FadeIn(stat_poly),
            Create(stat_line),
            FadeIn(lbl_stat),
            Write(eq_stat),
            run_time=1.6
        )
        self.play(
            ShowPassingFlash(stat_line.copy().set_color(WHITE), time_width=0.4),
            run_time=1.0
        )
        self.wait(1.9)  # Exact Cuepoint 1 = 8.5s (Pauses for presenter explanation of static limit)

        # --- STEP 2: Dynamic Zone & Hand-Off to Person 3 (8.5s - 15.0s) ---
        self.play(
            FadeIn(dyn_poly),
            FadeIn(peak_group),
            FadeIn(lbl_dyn),
            Write(eq_dyn),
            run_time=1.6
        )
        self.play(
            Flash(axes.c2p(0.80, 1.768), color=AMBER, line_length=0.22, flash_radius=0.35),
            FadeIn(handoff_group, shift=UP * 0.10),
            run_time=1.4
        )
        self.wait(3.5)  # Exact Cuepoint 2 = 15.0s (Calm resting frame for Person 2 Hand-Off)

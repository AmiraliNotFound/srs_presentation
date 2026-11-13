"""
SLIDE-09: DuhamelConvolutionScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 2 (Mathematical Theory & Derivations)
Allocated Time: 17:00 – 19:30 (150 s)

Strict 3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 5 English words total)
      "Duhamel Convolution" (2 words)
      "Base Shock Acceleration" (3 words)
  - Frame-Accurate Step Cuepoints (4 Steps / 3 Pauses):
      Step 0 (0.0s - 3.5s): Minimal title & Unit impulse response g(t) harmonic ripple
      Step 1 (3.5s - 8.5s): Slicing pulse F(tau) into dI = F(tau) dtau & launching wave dx(t)
      Step 2 (8.5s - 11.5s): Riemann superposition wave x(t) across pulse envelope (PAUSES HERE)
      Step 3 (11.5s - 17.0s): Master Duhamel Integral x(t) & Base shock z(t) center focus
"""

from manim import *
import numpy as np


class DuhamelConvolutionScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        CORAL      = ManimColor("#FF644E")   # Impulse strip dI = F(tau) dtau / Shock excitation
        CYAN       = ManimColor("#58C4DD")   # Unit impulse response g(t) & wave dx(t)
        YELLOW     = ManimColor("#F7CA3B")   # Transient shock force pulse F(tau)
        BLUE       = ManimColor("#0097F1")   # Convolution integral x(t) (UT Blue)
        AMBER      = ManimColor("#FFB703")   # Relative base displacement z(t)
        GREEN      = ManimColor("#83C167")   # Time delay lag (t - tau)
        TEXT_WHITE = ManimColor("#FFFFFF")
        TEXT_MUTED = ManimColor("#94A3B8")
        TEXT_DIM   = ManimColor("#475569")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 2 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Duhamel Convolution}",
            font_size=36,
            color=TEXT_WHITE
        ).move_to([0, 3.35, 0])

        # ------------------------------------------------------------------
        # 3. Mathematical Formulae Objects
        # ------------------------------------------------------------------
        # Step 0: Unit Impulse Response Building Block
        eq0 = MathTex(
            r"g(t)", r"=", r"\frac{1}{m\omega_n}", r"\sin(\omega_n t)",
            font_size=42
        ).move_to([0, 2.25, 0])
        eq0.set_color_by_tex(r"g(t)", CYAN)
        eq0.set_color_by_tex(r"\frac{1}{m\omega_n}", TEXT_WHITE)
        eq0.set_color_by_tex(r"\sin(\omega_n t)", CYAN)

        # Step 1: Infinitesimal Impulse Slicing
        eq1 = MathTex(
            r"d\mathcal{I} = F(\tau) d\tau",
            r"\quad \implies \quad",
            r"dx(t) = F(\tau) g(t - \tau) d\tau",
            font_size=38
        ).move_to([0, 2.25, 0])
        eq1.set_color_by_tex(r"d\mathcal{I} = F(\tau) d\tau", CORAL)
        eq1.set_color_by_tex(r"dx(t) = F(\tau) g(t - \tau) d\tau", CYAN)

        # Step 3: Master Duhamel Integral
        eq_duhamel = MathTex(
            r"x(t)", r"=", r"\frac{1}{m\omega_n}", r"\int_0^t", r"F(\tau)", r"\sin\omega_n(t - \tau)", r"\, d\tau",
            font_size=42
        ).move_to([0, 1.15, 0])
        eq_duhamel.set_color_by_tex(r"x(t)", BLUE)
        eq_duhamel.set_color_by_tex(r"\frac{1}{m\omega_n}", TEXT_WHITE)
        eq_duhamel.set_color_by_tex(r"\int_0^t", TEXT_WHITE)
        eq_duhamel.set_color_by_tex(r"F(\tau)", YELLOW)
        eq_duhamel.set_color_by_tex(r"\sin\omega_n(t - \tau)", CYAN)
        eq_duhamel.set_color_by_tex(r"\, d\tau", CORAL)

        box_duhamel = SurroundingRectangle(
            eq_duhamel,
            buff=0.25,
            corner_radius=0.14,
            stroke_color=BLUE,
            stroke_width=2.0
        )

        # Base Acceleration Shock Formulation
        eq_base = MathTex(
            r"z(t)", r"=", r"-\frac{1}{\omega_n}", r"\int_0^t", r"\ddot{y}(\tau)", r"\sin\omega_n(t - \tau)", r"\, d\tau",
            font_size=40
        ).move_to([0, -0.95, 0])
        eq_base.set_color_by_tex(r"z(t)", AMBER)
        eq_base.set_color_by_tex(r"-\frac{1}{\omega_n}", TEXT_WHITE)
        eq_base.set_color_by_tex(r"\int_0^t", TEXT_WHITE)
        eq_base.set_color_by_tex(r"\ddot{y}(\tau)", CORAL)
        eq_base.set_color_by_tex(r"\sin\omega_n(t - \tau)", CYAN)
        eq_base.set_color_by_tex(r"\, d\tau", CORAL)

        lbl_base = Tex(
            r"\textbf{Base Shock Acceleration}",
            font_size=24,
            color=TEXT_MUTED
        ).next_to(eq_base, DOWN, buff=0.25)

        # ------------------------------------------------------------------
        # 4. Geometric Axes & Waveforms
        # ------------------------------------------------------------------
        axes = Axes(
            x_range=[0, 6.2, 1.0],
            y_range=[-1.3, 1.5, 1.0],
            x_length=9.2,
            y_length=3.4,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.6,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12,
            }
        ).move_to([0, -0.65, 0])

        lbl_t = MathTex(r"\tau, \, t", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(6.2, 0), RIGHT, buff=0.12)
        lbl_y = MathTex(r"x, \, F", font_size=22, color=TEXT_MUTED).next_to(axes.c2p(0, 1.5), UP, buff=0.10)

        # --- Harmonic ripple g(t) ---
        t_vals_g = np.linspace(0, 5.8, 160)
        pts_g = [axes.c2p(t, 0.90 * np.sin(2 * np.pi * t / 1.8)) for t in t_vals_g]
        g_curve = VMobject().set_points_smoothly(pts_g).set_color(CYAN).set_stroke(width=3.4)
        lbl_g = MathTex(r"g(t)", font_size=24, color=CYAN).move_to(axes.c2p(0.45, 1.15))

        # --- Continuous Force Pulse F(tau) (localized pulse 0 <= tau <= 2.0) ---
        t_pulse = np.linspace(0, 2.0, 90)
        pts_f = [axes.c2p(t, 1.15 * np.sin(np.pi * t / 2.0)) for t in t_pulse]
        f_curve = VMobject().set_points_smoothly(pts_f).set_color(YELLOW).set_stroke(width=3.4)

        area_pts = [axes.c2p(0, 0)] + pts_f + [axes.c2p(2.0, 0)]
        f_area = Polygon(*area_pts, color=YELLOW, stroke_width=0, fill_color=YELLOW, fill_opacity=0.14)
        lbl_f = MathTex(r"F(\tau)", font_size=24, color=YELLOW).move_to(axes.c2p(0.45, 1.15))

        # --- Infinitesimal Impulse Strip at tau = 1.0 ---
        tau_0 = 1.0
        d_tau = 0.16
        h_strip = 1.15 * np.sin(np.pi * tau_0 / 2.0)
        p1 = axes.c2p(tau_0 - d_tau / 2, 0)
        p2 = axes.c2p(tau_0 - d_tau / 2, h_strip)
        p3 = axes.c2p(tau_0 + d_tau / 2, h_strip)
        p4 = axes.c2p(tau_0 + d_tau / 2, 0)
        strip_rect = Polygon(p1, p2, p3, p4, color=CORAL, stroke_width=1.8, fill_color=CORAL, fill_opacity=0.85)
        lbl_strip = MathTex(r"d\mathcal{I} = F(\tau)d\tau", font_size=20, color=CORAL).next_to(strip_rect, UP, buff=0.14)

        # --- Wavelet dx(t) launching from tau = 1.0 into t > tau ---
        t_vals_wave = np.linspace(1.0, 5.8, 120)
        pts_wave = [axes.c2p(t, 0.58 * np.sin(2 * np.pi * (t - 1.0) / 1.5)) for t in t_vals_wave]
        wave_dx = VMobject().set_points_smoothly(pts_wave).set_color(CYAN).set_stroke(width=3.2)
        lbl_wave_dx = MathTex(r"dx(t)", font_size=22, color=CYAN).move_to(axes.c2p(2.1, 0.78))

        # --- Time delay lag (t - tau) indicator ---
        t_obs = 2.8
        y_arrow = -0.42
        arrow_dt = DoubleArrow(
            axes.c2p(tau_0, y_arrow),
            axes.c2p(t_obs, y_arrow),
            color=GREEN,
            tip_length=0.11,
            stroke_width=2.0
        )
        lbl_dt = MathTex(r"t - \tau", font_size=20, color=GREEN).next_to(arrow_dt, DOWN, buff=0.08)
        dl1 = DashedLine(axes.c2p(tau_0, 0), axes.c2p(tau_0, y_arrow - 0.05), stroke_width=1.2, color=TEXT_MUTED)
        y_wave_obs = 0.58 * np.sin(2 * np.pi * (t_obs - 1.0) / 1.5)
        dl2 = DashedLine(axes.c2p(t_obs, y_wave_obs), axes.c2p(t_obs, y_arrow - 0.05), stroke_width=1.2, color=TEXT_MUTED)
        lbl_tau_axis = MathTex(r"\tau", font_size=18, color=CORAL).next_to(axes.c2p(tau_0, 0), DOWN, buff=0.08)
        lbl_t_axis = MathTex(r"t", font_size=18, color=TEXT_WHITE).next_to(axes.c2p(t_obs, 0), DOWN, buff=0.08)
        delay_group = VGroup(arrow_dt, lbl_dt, dl1, dl2, lbl_tau_axis, lbl_t_axis)

        # --- Riemann Strips across pulse envelope ---
        riemann_strips = VGroup()
        for i in range(8):
            t_mid = 0.125 + i * 0.25
            h_val = 1.15 * np.sin(np.pi * t_mid / 2.0)
            w = 0.21
            sp1 = axes.c2p(t_mid - w / 2, 0)
            sp2 = axes.c2p(t_mid - w / 2, h_val)
            sp3 = axes.c2p(t_mid + w / 2, h_val)
            sp4 = axes.c2p(t_mid + w / 2, 0)
            s_poly = Polygon(sp1, sp2, sp3, sp4, color=CORAL, stroke_width=1.0, fill_color=CORAL, fill_opacity=0.45)
            riemann_strips.add(s_poly)

        # Resulting convolution response wave x(t)
        pts_conv = [axes.c2p(t, 0.85 * (1 - np.cos(2 * np.pi * t / 1.5)) * np.exp(-0.12 * t)) for t in np.linspace(0, 5.8, 140)]
        conv_wave = VMobject().set_points_smoothly(pts_conv).set_color(BLUE).set_stroke(width=3.6)
        lbl_conv = MathTex(r"x(t)", font_size=24, color=BLUE).move_to(axes.c2p(3.2, 1.15))

        # ------------------------------------------------------------------
        # 5. Animation Sequence (4 Steps, 3 Cuepoint Pauses)
        # ------------------------------------------------------------------

        # --- STEP 0: Impulse Response Building Block (0.0s - 3.5s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.6)
        self.play(Write(eq0), run_time=1.2)
        self.play(
            Create(axes),
            FadeIn(lbl_t),
            FadeIn(lbl_y),
            Create(g_curve),
            FadeIn(lbl_g),
            run_time=1.2
        )
        self.wait(0.5)  # Exact Cuepoint 0 = 3.5s

        # --- STEP 1: Slicing the Shock Pulse into Impulses (3.5s - 8.5s) ---
        self.play(
            TransformMatchingTex(eq0, eq1),
            FadeOut(g_curve),
            FadeOut(lbl_g),
            run_time=1.0
        )
        self.play(
            Create(f_curve),
            FadeIn(f_area),
            FadeIn(lbl_f),
            run_time=1.0
        )
        self.play(
            Create(strip_rect),
            FadeIn(lbl_strip),
            run_time=0.7
        )
        self.play(
            Create(wave_dx),
            FadeIn(lbl_wave_dx),
            run_time=1.1
        )
        self.play(
            FadeIn(delay_group),
            run_time=0.6
        )
        self.wait(0.6)  # Exact Cuepoint 1 = 8.5s

        # --- STEP 2: Riemann Superposition Wave x(t) (8.5s - 11.5s) ---
        # User requested pause point: Presenter explains continuous superposition
        self.play(
            FadeIn(riemann_strips, lag_ratio=0.08),
            run_time=0.8
        )
        self.play(
            Create(conv_wave),
            FadeIn(lbl_conv),
            FadeOut(wave_dx),
            FadeOut(lbl_wave_dx),
            FadeOut(delay_group),
            run_time=1.2
        )
        self.wait(1.0)  # Exact Cuepoint 2 = 11.5s (Pauses here for audience explanation)

        # --- STEP 3: Master Duhamel Integral & Base Shock (11.5s - 17.0s) ---
        # Triggered by presenter advancing to resolve derivation
        self.play(
            FadeOut(VGroup(
                axes, lbl_t, lbl_y, f_curve, f_area, lbl_f,
                strip_rect, lbl_strip, riemann_strips, conv_wave, lbl_conv, eq1
            )),
            run_time=0.8
        )
        self.play(
            Write(eq_duhamel),
            Create(box_duhamel),
            run_time=1.3
        )
        self.play(
            FadeIn(eq_base, shift=UP * 0.15),
            FadeIn(lbl_base, shift=UP * 0.15),
            run_time=0.9
        )
        self.wait(2.5)  # Exact Cuepoint 3 = 17.0s (Calm resting state for Person 2)

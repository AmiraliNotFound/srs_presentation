"""
SLIDE-04: ShockTaxonomyScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Foundations & Modeling)

Clean Presentation-Grade Slide (Zero Clutter / Large Crisp Typography):
  - Step 0 (0.0s - 2.0s): Top Header & Subtitle (Shock Taxonomy & Testing Standards).
  - Step 1 (2.0s - 7.0s): Velocity Shock (Drop / Impact) — Half-sine waveform & kinematics.
  - Step 2 (7.0s - 12.0s): Pyrotechnic Shock (Pyroshock) — High-frequency decaying burst & PCB failure.
  - Step 3 (12.0s - 17.5s): Military Standards (MIL-STD-810H) & Why Peak-g Fails -> The SRS Mandate.
"""

from manim import *
import numpy as np


class ShockTaxonomyScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black & UT Blue)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # University of Tehran Primary Accent
        FORCE_GOLD  = ManimColor("#F7CA3B")   # Accents, Standards & SRS Formula
        DANGER_RED  = ManimColor("#FF644E")   # Pyroshock, Failure Drivers & Alert
        SPRING_CYAN = ManimColor("#58C4DD")   # Velocity Shock & Half-Sine Waveform
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        TEXT_DIM    = ManimColor("#64748B")
        BORDER_MID  = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Header & Title (Floating at Top, Spacious & Clean)
        # ------------------------------------------------------------------
        header_tag = Tex(
            r"\textsc{Physical Foundations} \quad $\bullet$ \quad \textsc{Environmental Taxonomy}",
            font_size=22,
            color=TEHRAN_BLUE
        ).move_to([0, 3.50, 0])

        main_title = Tex(
            r"\textbf{Real-World Shock Taxonomy \& Testing Standards}",
            font_size=42,
            color=TEXT_WHITE
        ).next_to(header_tag, DOWN, buff=0.14)

        header_rule = Line(
            start=LEFT * 6.2,
            end=RIGHT * 6.2,
            color=TEHRAN_BLUE,
            stroke_width=1.6
        ).next_to(main_title, DOWN, buff=0.15)

        subtitle = Tex(
            r"From Drop Impacts to Pyroshocks: Why Peak-$g$ Alone Fails",
            font_size=23,
            color=FORCE_GOLD
        ).next_to(header_rule, DOWN, buff=0.14)

        # ------------------------------------------------------------------
        # 3. Middle Stage: Two Physical Shock Classes (Left & Right Columns)
        # ------------------------------------------------------------------
        col_x = 3.55

        # === COLUMN 1: VELOCITY SHOCK (DROP / IMPACT) ===
        c1_title = Tex(
            r"\textbf{1. Velocity Shock (Drop / Impact)}",
            font_size=25,
            color=SPRING_CYAN
        ).move_to([-col_x, 1.82, 0])

        c1_formula = MathTex(
            r"\text{Kinetic Energy Transfer: } v_0 = \sqrt{2gh}",
            font_size=20,
            color=TEXT_OFFWH
        ).move_to([-col_x, 1.44, 0])

        # Left Axes: Half-Sine Acceleration Pulse
        ax_drop = Axes(
            x_range=[0, 1.4, 0.5],
            y_range=[0, 1.3, 0.5],
            x_length=4.8,
            y_length=1.35,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([-col_x, 0.55, 0])

        lbl_ax_drop_t = Tex(r"Time $t$", font_size=16, color=TEXT_MUTED).next_to(ax_drop.c2p(1.4, 0), RIGHT, buff=0.08)
        lbl_ax_drop_a = Tex(r"$a(t)$", font_size=16, color=TEXT_MUTED).next_to(ax_drop.c2p(0, 1.3), LEFT, buff=0.08)

        # Half-sine waveform: a(t) = a_max * sin(pi * t / t0) for 0 <= t <= 1.0
        t_vals_drop = np.linspace(0, 1.0, 100)
        pts_drop = [ax_drop.c2p(t, 1.0 * np.sin(np.pi * t)) for t in t_vals_drop]
        pts_drop_flat = [ax_drop.c2p(t, 0.0) for t in np.linspace(1.0, 1.3, 30)]
        curve_drop = VMobject().set_points_smoothly(pts_drop + pts_drop_flat).set_color(SPRING_CYAN).set_stroke(width=3.2)

        # Shaded area under half-sine representing Delta v
        area_pts = [ax_drop.c2p(0, 0)] + pts_drop + [ax_drop.c2p(1.0, 0)]
        area_drop = Polygon(*area_pts, color=SPRING_CYAN, stroke_width=0, fill_color=SPRING_CYAN, fill_opacity=0.18)
        lbl_area = MathTex(r"\Delta v = v_0", font_size=18, color=SPRING_CYAN).move_to(ax_drop.c2p(0.5, 0.40))

        # Annotations below Left Plot
        c1_metric1 = MathTex(
            r"t_0 \in [10, 100]\text{ ms}, \quad a_{\max} \sim 10\text{--}100g",
            font_size=20,
            color=FORCE_GOLD
        ).move_to([-col_x, -0.38, 0])

        c1_metric2 = Tex(
            r"\textbf{Primary Driver:} Structural Flexure \& Yield",
            font_size=18,
            color=DANGER_RED
        ).move_to([-col_x, -0.68, 0])

        c1_app = Tex(
            r"Motivating Problem: Helicopter Avionics Drop",
            font_size=16,
            color=TEXT_MUTED
        ).move_to([-col_x, -0.95, 0])

        grp_col1 = VGroup(
            c1_title, c1_formula,
            ax_drop, lbl_ax_drop_t, lbl_ax_drop_a,
            curve_drop, area_drop, lbl_area,
            c1_metric1, c1_metric2, c1_app
        )

        # === COLUMN 2: PYROTECHNIC SHOCK (PYROSHOCK) ===
        c2_title = Tex(
            r"\textbf{2. Pyrotechnic Shock (Pyroshock)}",
            font_size=25,
            color=DANGER_RED
        ).move_to([col_x, 1.82, 0])

        c2_formula = MathTex(
            r"\text{Explosive Staging: } \mu\text{s Detonation}",
            font_size=20,
            color=TEXT_OFFWH
        ).move_to([col_x, 1.44, 0])

        # Right Axes: High-Frequency Decaying Oscillation
        ax_pyro = Axes(
            x_range=[0, 1.4, 0.5],
            y_range=[-1.2, 1.2, 0.5],
            x_length=4.8,
            y_length=1.35,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.4,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10,
            }
        ).move_to([col_x, 0.55, 0])

        lbl_ax_pyro_t = Tex(r"Time $t$", font_size=16, color=TEXT_MUTED).next_to(ax_pyro.c2p(1.4, 0), RIGHT, buff=0.08)
        lbl_ax_pyro_a = Tex(r"$a(t)$", font_size=16, color=TEXT_MUTED).next_to(ax_pyro.c2p(0, 1.2), LEFT, buff=0.08)

        # High-frequency damped ringing: a(t) = exp(-3.8*t) * sin(2*pi*8*t)
        t_vals_pyro = np.linspace(0, 1.3, 350)
        pts_pyro = [
            ax_pyro.c2p(t, 1.05 * np.exp(-3.8 * t) * np.sin(2 * np.pi * 7.5 * t))
            for t in t_vals_pyro
        ]
        curve_pyro = VMobject().set_points_smoothly(pts_pyro).set_color(DANGER_RED).set_stroke(width=2.2)

        # Envelope lines (+/- exp(-3.8t))
        env_pts_pos = [ax_pyro.c2p(t, 1.05 * np.exp(-3.8 * t)) for t in t_vals_pyro]
        env_pts_neg = [ax_pyro.c2p(t, -1.05 * np.exp(-3.8 * t)) for t in t_vals_pyro]
        curve_env_pos = VMobject().set_points_smoothly(env_pts_pos).set_color(BORDER_MID).set_stroke(width=1.2)
        curve_env_neg = VMobject().set_points_smoothly(env_pts_neg).set_color(BORDER_MID).set_stroke(width=1.2)

        # Annotations below Right Plot
        c2_metric1 = MathTex(
            r"t_0 < 20\text{ ms} \ (f > 1\text{ kHz}), \quad a_{\max} \sim 1{,}000\text{--}10{,}000g",
            font_size=20,
            color=FORCE_GOLD
        ).move_to([col_x, -0.38, 0])

        c2_metric2 = Tex(
            r"\textbf{Primary Driver:} PCB Component \& Solder Fracture",
            font_size=18,
            color=DANGER_RED
        ).move_to([col_x, -0.68, 0])

        c2_app = Tex(
            r"Spacecraft Staging, Explosive Bolts \& Deployments",
            font_size=16,
            color=TEXT_MUTED
        ).move_to([col_x, -0.95, 0])

        grp_col2 = VGroup(
            c2_title, c2_formula,
            ax_pyro, lbl_ax_pyro_t, lbl_ax_pyro_a,
            curve_pyro, curve_env_pos, curve_env_neg,
            c2_metric1, c2_metric2, c2_app
        )

        # ------------------------------------------------------------------
        # 4. Bottom Stage: Testing Standards & The SRS Mandate
        # ------------------------------------------------------------------
        bot_div = Line(
            start=LEFT * 6.2,
            end=RIGHT * 6.2,
            color=BORDER_MID,
            stroke_width=1.2
        ).move_to([0, -1.18, 0])

        std_banner = Tex(
            r"\mbox{\textsc{Military Qualification Standards: MIL-STD-810H (Method 516.8) \quad $\bullet$ \quad MIL-E-5400}}",
            font_size=18,
            color=FORCE_GOLD
        ).move_to([0, -1.44, 0])

        # Bottom Left: The Peak-g Fallacy
        p_fallacy_title = Tex(
            r"\textbf{The Peak-$g$ Fallacy}",
            font_size=20,
            color=DANGER_RED
        ).move_to([-col_x, -1.88, 0])

        p_fallacy_line1 = MathTex(
            r"1{,}000g \ (\mu\text{s pulse}) \implies \text{Harmless } (t_0 \ll \tau_n, \text{DLF} \to 0)",
            font_size=18,
            color=TEXT_OFFWH
        ).move_to([-col_x, -2.22, 0])

        p_fallacy_line2 = MathTex(
            r"50g \ (t_0 \approx \tau_n) \implies \textbf{Catastrophic Resonance!}",
            font_size=18,
            color=DANGER_RED
        ).move_to([-col_x, -2.54, 0])

        p_fallacy_summary = Tex(
            r"Peak acceleration alone cannot predict structural damage.",
            font_size=16,
            color=TEXT_MUTED
        ).move_to([-col_x, -2.88, 0])

        grp_fallacy = VGroup(p_fallacy_title, p_fallacy_line1, p_fallacy_line2, p_fallacy_summary)

        # Center Connector Arrow
        conn_arrow = Arrow(
            start=[-0.45, -2.35, 0],
            end=[0.45, -2.35, 0],
            color=FORCE_GOLD,
            stroke_width=3.2,
            tip_length=0.18
        )
        conn_lbl = Tex(r"\textsc{Necessitates}", font_size=15, color=FORCE_GOLD).next_to(conn_arrow, UP, buff=0.08)
        grp_conn = VGroup(conn_arrow, conn_lbl)

        # Bottom Right: The SRS Mandate
        p_srs_title = Tex(
            r"\textbf{The Solution: Shock Response Spectrum}",
            font_size=20,
            color=TEHRAN_BLUE
        ).move_to([col_x, -1.88, 0])

        p_srs_formula = MathTex(
            r"S_a(\omega_n, \zeta) = \max_{t} |\ddot{x}(t)|",
            font_size=32,
            color=FORCE_GOLD
        ).move_to([col_x, -2.32, 0])

        p_srs_desc = Tex(
            r"Evaluates peak dynamic response across all frequencies $\omega_n$",
            font_size=16,
            color=TEXT_OFFWH
        ).move_to([col_x, -2.76, 0])

        p_srs_mandate = Tex(
            r"\textbf{Mandatory for Aerospace \& Defense Certification}",
            font_size=16,
            color=SPRING_CYAN
        ).move_to([col_x, -3.05, 0])

        grp_srs = VGroup(p_srs_title, p_srs_formula, p_srs_desc, p_srs_mandate)

        # ------------------------------------------------------------------
        # 5. Step-Controlled Timeline & Cuepoint Choreography
        # ------------------------------------------------------------------
        # --- Step 0: Header & Subtitle Reveal (Total: 2.0s -> Cuepoint 0 = 2.0s) ---
        self.play(
            FadeIn(header_tag, shift=DOWN * 0.15),
            Write(main_title),
            GrowFromCenter(header_rule),
            run_time=0.8
        )
        self.play(
            FadeIn(subtitle, shift=UP * 0.15),
            run_time=0.6
        )
        self.wait(0.6)  # Stable rest hold at t = 2.0s

        # --- Step 1: Velocity Shock (Drop / Impact) (Total: 5.0s -> Cuepoint 1 = 7.0s) ---
        self.play(
            FadeIn(c1_title, shift=DOWN * 0.10),
            FadeIn(c1_formula, shift=DOWN * 0.10),
            Create(ax_drop),
            Write(lbl_ax_drop_t),
            Write(lbl_ax_drop_a),
            run_time=0.8
        )
        self.play(
            Create(curve_drop),
            FadeIn(area_drop),
            FadeIn(lbl_area),
            run_time=1.8,
            rate_func=linear
        )
        self.play(
            FadeIn(c1_metric1, shift=UP * 0.10),
            FadeIn(c1_metric2, shift=UP * 0.10),
            FadeIn(c1_app, shift=UP * 0.10),
            run_time=0.9
        )
        self.wait(1.5)  # Stable rest hold at t = 7.0s

        # --- Step 2: Pyrotechnic Shock (Pyroshock) (Total: 5.0s -> Cuepoint 2 = 12.0s) ---
        self.play(
            FadeIn(c2_title, shift=DOWN * 0.10),
            FadeIn(c2_formula, shift=DOWN * 0.10),
            Create(ax_pyro),
            Write(lbl_ax_pyro_t),
            Write(lbl_ax_pyro_a),
            Create(curve_env_pos),
            Create(curve_env_neg),
            run_time=0.8
        )
        self.play(
            Create(curve_pyro),
            run_time=1.8,
            rate_func=linear
        )
        self.play(
            FadeIn(c2_metric1, shift=UP * 0.10),
            FadeIn(c2_metric2, shift=UP * 0.10),
            FadeIn(c2_app, shift=UP * 0.10),
            run_time=0.9
        )
        self.wait(1.5)  # Stable rest hold at t = 12.0s

        # --- Step 3: Military Standards & SRS Mandate (Total: 5.5s -> Cuepoint 3 = 17.5s) ---
        self.play(
            Create(bot_div),
            FadeIn(std_banner, shift=DOWN * 0.10),
            run_time=0.8
        )
        self.play(
            LaggedStart(
                FadeIn(grp_fallacy, shift=UP * 0.15),
                FadeIn(grp_conn, shift=UP * 0.15),
                FadeIn(grp_srs, shift=UP * 0.15),
                lag_ratio=0.20
            ),
            run_time=1.0
        )
        # Pulse formula for emphasis
        self.play(
            p_srs_formula.animate.scale(1.10),
            run_time=0.3
        )
        self.play(
            p_srs_formula.animate.scale(1 / 1.10),
            run_time=0.3
        )
        self.wait(3.1)  # Stable rest hold until t = 17.5s

"""
SLIDE-01: TitleCardScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Foundations)
"""

from manim import *
import numpy as np


class TitleCardScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black & UT Blue)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # University of Tehran Primary Accent
        SPRING_CYAN = ManimColor("#58C4DD")   # Restoring / Spring
        ACCEL_RED   = ManimColor("#FF644E")   # Inertia / Mass
        FORCE_GOLD  = ManimColor("#F7CA3B")   # Excitation Force / Shock
        DAMP_GREEN  = ManimColor("#83C167")   # Viscous Damper / Dissipation
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        CARD_BG     = ManimColor("#080D1A")
        BORDER_DIM  = ManimColor("#1E293B")
        BORDER_MID  = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Top Header & Academic Affiliation
        # ------------------------------------------------------------------
        univ_header = Tex(
            r"\textsc{University of Tehran}",
            font_size=26,
            color=TEHRAN_BLUE
        ).move_to([0, 3.42, 0])

        dept_header = Tex(
            r"Department of Mechanical Engineering \quad $\bullet$ \quad Mechanical Vibrations",
            font_size=18,
            color=TEXT_MUTED
        ).next_to(univ_header, DOWN, buff=0.10)

        header_rule = Line(
            start=LEFT * 5.8,
            end=RIGHT * 5.8,
            color=TEHRAN_BLUE,
            stroke_width=1.5
        ).next_to(dept_header, DOWN, buff=0.14)

        # Main Title & Subtitle
        main_title = Tex(
            r"\textbf{Shock Response Spectrum (SRS)}",
            font_size=44,
            color=TEXT_WHITE
        ).next_to(header_rule, DOWN, buff=0.22)

        subtitle = Tex(
            r"Transient Shock Dynamics, SDOF Foundations \& Base Isolation Design",
            font_size=21,
            color=TEXT_OFFWH
        ).next_to(main_title, DOWN, buff=0.14)

        # ------------------------------------------------------------------
        # 3. Physical Motif: SDOF Schematic + Transient Shock Waveform
        # ------------------------------------------------------------------
        # Left Side: SDOF Schematic
        wall_x = -5.8
        wall_line = Line([wall_x, -0.65, 0], [wall_x, 0.65, 0], color=TEXT_MUTED, stroke_width=2.5)
        hatches = VGroup(*[
            Line([wall_x, y, 0], [wall_x - 0.2, y + 0.14, 0], color=TEXT_MUTED, stroke_width=1.2)
            for y in np.linspace(-0.6, 0.52, 7)
        ])
        ground_line = Line([wall_x, -0.65, 0], [-2.2, -0.65, 0], color=BORDER_DIM, stroke_width=1.5)

        # Helical Spring (top branch, y = +0.22)
        def create_spring(start, end, coils=5, width=0.15):
            start = np.array(start)
            end = np.array(end)
            vec = end - start
            length = np.linalg.norm(vec)
            u = vec / length
            p = np.array([-u[1], u[0], 0])
            lead = 0.18 * length
            coil_len = length - 2 * lead
            pts = [start, start + lead * u]
            n_pts = coils * 2
            for i in range(1, n_pts):
                frac = i / n_pts
                sign = 1 if i % 2 == 1 else -1
                pts.append(start + (lead + frac * coil_len) * u + sign * width * p)
            pts.append(end - lead * u)
            pts.append(end)
            spring = VMobject()
            spring.set_points_as_corners(pts)
            return spring

        spring = create_spring([wall_x, 0.22, 0], [-3.8, 0.22, 0], coils=5, width=0.14)
        spring.set_color(SPRING_CYAN).set_stroke(width=2.5)
        spring_lbl = MathTex(r"k", font_size=22, color=SPRING_CYAN).next_to(spring, UP, buff=0.07)

        # Viscous Damper (bottom branch, y = -0.22)
        d_rod_left = Line([wall_x, -0.22, 0], [-4.85, -0.22, 0], color=DAMP_GREEN, stroke_width=2)
        d_cylinder = VMobject().set_points_as_corners([
            [-4.4, -0.09, 0], [-4.85, -0.09, 0], [-4.85, -0.35, 0], [-4.4, -0.35, 0]
        ]).set_color(DAMP_GREEN).set_stroke(width=2)
        d_piston = Line([-4.62, -0.11, 0], [-4.62, -0.33, 0], color=DAMP_GREEN, stroke_width=2.5)
        d_rod_right = Line([-4.62, -0.22, 0], [-3.8, -0.22, 0], color=DAMP_GREEN, stroke_width=2)
        damper = VGroup(d_rod_left, d_cylinder, d_piston, d_rod_right)
        damper_lbl = MathTex(r"c", font_size=22, color=DAMP_GREEN).next_to(damper, DOWN, buff=0.07)

        # Mass Block
        mass_box = RoundedRectangle(
            width=1.1,
            height=0.88,
            corner_radius=0.12,
            stroke_color=TEHRAN_BLUE,
            stroke_width=2.5,
            fill_color=CARD_BG,
            fill_opacity=0.95
        ).move_to([-3.25, 0, 0])
        mass_lbl = MathTex(r"m", font_size=28, color=TEXT_WHITE).move_to(mass_box)
        mass_group = VGroup(mass_box, mass_lbl)

        # Rollers under mass
        rollers = VGroup(
            Circle(radius=0.065, color=TEXT_MUTED, stroke_width=1.2).move_to([-3.55, -0.51, 0]),
            Circle(radius=0.065, color=TEXT_MUTED, stroke_width=1.2).move_to([-2.95, -0.51, 0])
        )

        # Shock Input Arrow
        shock_arrow = Arrow(
            start=[-6.65, 0, 0],
            end=[-5.85, 0, 0],
            color=FORCE_GOLD,
            stroke_width=3,
            tip_length=0.16
        )
        shock_lbl = MathTex(r"\ddot{y}_0(t)", font_size=22, color=FORCE_GOLD).next_to(shock_arrow, UP, buff=0.08)

        # Right Side: Transient Shock Waveform & Coordinate Axes
        ax = Axes(
            x_range=[0, 7.5, 2],
            y_range=[-1.2, 1.4, 1],
            x_length=5.6,
            y_length=1.65,
            axis_config={
                "color": BORDER_MID,
                "stroke_width": 1.5,
                "include_tip": True,
                "tip_width": 0.10,
                "tip_height": 0.10
            }
        ).move_to([2.4, -0.05, 0])

        t_lbl = MathTex(r"t", font_size=18, color=TEXT_MUTED).next_to(ax.x_axis.get_end(), DOWN, buff=0.1)
        y_lbl = MathTex(r"F(t), \, x(t)", font_size=18, color=TEXT_MUTED).next_to(ax.y_axis.get_end(), UP, buff=0.1)

        # Exact Analytical SDOF Response to Half-Sine Pulse
        # Pulse duration t0 = 1.5, ratio r = omega / omega_n = 0.70
        t0 = 1.5
        omega_pulse = np.pi / t0
        r_ratio = 0.70
        omega_nat = omega_pulse / r_ratio
        zeta_val = 0.05
        f0_scaled = 0.68  # Scale factor for pristine visual balance

        def analytical_response(t):
            if t <= t0:
                # Era 1: Forced response
                return f0_scaled * (1.0 / (1.0 - r_ratio**2)) * (
                    np.sin(omega_pulse * t) - r_ratio * np.sin(omega_nat * t)
                )
            else:
                # Era 2: Damped residual free vibration
                x0 = f0_scaled * (1.0 / (1.0 - r_ratio**2)) * (
                    np.sin(omega_pulse * t0) - r_ratio * np.sin(omega_nat * t0)
                )
                v0 = f0_scaled * (1.0 / (1.0 - r_ratio**2)) * (
                    omega_pulse * np.cos(omega_pulse * t0) - r_ratio * omega_nat * np.cos(omega_nat * t0)
                )
                dt = t - t0
                wd = omega_nat * np.sqrt(1.0 - zeta_val**2)
                return np.exp(-zeta_val * omega_nat * dt) * (
                    x0 * np.cos(wd * dt) + ((v0 + zeta_val * omega_nat * x0) / wd) * np.sin(wd * dt)
                )

        # Half-Sine Shock Pulse (Excitation)
        pulse_curve = ax.plot(
            lambda t: 1.0 * np.sin(np.pi * t / t0) if t <= t0 else 0.0,
            x_range=[0, t0, 0.02],
            color=FORCE_GOLD,
            stroke_width=3.2
        )
        pulse_tag = Tex(r"\text{Shock Pulse } $F(t)$", font_size=15, color=FORCE_GOLD).move_to(ax.c2p(1.15, 1.25))

        # Dynamic SDOF Response
        resp_curve = ax.plot(
            analytical_response,
            x_range=[0, 7.2, 0.02],
            color=TEHRAN_BLUE,
            stroke_width=2.8
        )
        resp_tag = Tex(r"\text{SDOF Response } $x(t)$ \text{ [DLF $> 1$]}", font_size=15, color=TEHRAN_BLUE).move_to(ax.c2p(4.8, 0.95))

        # Governing Equation Tag centered above plot
        gov_eq = MathTex(
            r"m \ddot{x}", r"+", r"c \dot{x}", r"+", r"k x", r"=", r"F(t)",
            font_size=22
        ).move_to([2.4, 1.15, 0])
        gov_eq[0].set_color(ACCEL_RED)
        gov_eq[2].set_color(DAMP_GREEN)
        gov_eq[4].set_color(SPRING_CYAN)
        gov_eq[6].set_color(FORCE_GOLD)

        # ------------------------------------------------------------------
        # 4. Bottom Canvas: 3-Speaker Curricular Structure (Horizontal Cards)
        # ------------------------------------------------------------------
        def build_card(part_num, speaker_num, title_text, bullets_text, time_str, color, is_active=False):
            card_w = 4.1
            card_h = 1.36
            border_color = color if is_active else BORDER_DIM
            stroke_w = 2.4 if is_active else 1.2

            box = RoundedRectangle(
                width=card_w,
                height=card_h,
                corner_radius=0.14,
                stroke_color=border_color,
                stroke_width=stroke_w,
                fill_color=CARD_BG,
                fill_opacity=0.94
            )

            # Header row: Badge on left, Time budget on right
            badge_str = rf"\textbf{{PART {part_num}}} \quad $\bullet$ \quad \textsc{{Person {speaker_num}}}"
            badge = Tex(badge_str, font_size=15, color=color).move_to(box.get_top() + DOWN * 0.22 + LEFT * 0.45)

            time_badge = Tex(rf"\texttt{{{time_str}}}", font_size=13, color=color if is_active else TEXT_MUTED).move_to(
                box.get_top() + DOWN * 0.22 + RIGHT * 1.35
            )

            # Card Title
            card_title = Tex(rf"\textbf{{{title_text}}}", font_size=16.5, color=TEXT_WHITE).next_to(badge, DOWN, buff=0.12)
            card_title.set_x(box.get_x())

            # Bullets
            card_bullets = Tex(bullets_text, font_size=13, color=TEXT_MUTED).next_to(card_title, DOWN, buff=0.08)
            card_bullets.set_x(box.get_x())

            elements = [box, badge, time_badge, card_title, card_bullets]
            if is_active:
                pulse_dot = Dot(color=color, radius=0.055).move_to(box.get_top() + DOWN * 0.22 + LEFT * 1.7)
                elements.append(pulse_dot)

            return VGroup(*elements)

        card_y = -2.38
        card1 = build_card(
            1, 1,
            "Physical Intuition \& SDOF Modeling",
            r"Harmonic vs Shock $\bullet$ MIL-STD-810H $\bullet$ Drop-Box",
            "00:00 -- 15:00",
            TEHRAN_BLUE,
            is_active=True
        ).move_to([-4.4, card_y, 0])

        card2 = build_card(
            2, 2,
            "Mathematical Rigor \& SRS Theory",
            r"Duhamel Integral $\bullet$ Dual Eras $\bullet$ SRS Spectra",
            "15:00 -- 30:00",
            ManimColor("#818CF8"),
            is_active=False
        ).move_to([0.0, card_y, 0])

        card3 = build_card(
            3, 3,
            "Case Studies \& Isolator Sizing",
            r"Helicopter Sizing $\bullet$ Crane Derailment $\bullet$ ECU Isolator",
            "30:00 -- 45:00",
            ManimColor("#2DD4BF"),
            is_active=False
        ).move_to([4.4, card_y, 0])

        # Connecting Chevrons between cards
        chev1 = MathTex(r"\rightarrow", font_size=24, color=BORDER_MID).move_to([-2.2, card_y, 0])
        chev2 = MathTex(r"\rightarrow", font_size=24, color=BORDER_MID).move_to([2.2, card_y, 0])

        # ------------------------------------------------------------------
        # 5. Animation Choreography (0.0s -- 12.0s + Hold Frame)
        # ------------------------------------------------------------------
        # Phase 1: Academic Branding & Title Reveal (0.0s - 3.5s)
        self.play(
            FadeIn(univ_header, shift=DOWN * 0.22),
            FadeIn(dept_header, shift=DOWN * 0.18),
            GrowFromCenter(header_rule),
            run_time=1.2
        )
        self.play(
            Write(main_title),
            FadeIn(subtitle, shift=UP * 0.18),
            run_time=1.8
        )
        self.wait(0.3)

        # Phase 2: Physical Motif Animation (3.5s - 7.5s)
        self.play(
            Create(wall_line),
            Create(hatches),
            Create(ground_line),
            Create(spring),
            FadeIn(spring_lbl),
            Create(damper),
            FadeIn(damper_lbl),
            FadeIn(mass_group),
            FadeIn(rollers),
            GrowArrow(shock_arrow),
            FadeIn(shock_lbl),
            run_time=1.4
        )
        self.play(
            Create(ax),
            FadeIn(t_lbl),
            FadeIn(y_lbl),
            FadeIn(gov_eq, shift=DOWN * 0.12),
            run_time=0.8
        )
        self.play(
            Create(pulse_curve),
            FadeIn(pulse_tag),
            run_time=1.2
        )
        self.play(
            Create(resp_curve),
            FadeIn(resp_tag),
            run_time=1.5
        )
        self.wait(0.3)

        # Phase 3: 3-Speaker Curricular Structure (7.5s - 11.5s)
        self.play(
            LaggedStart(
                FadeIn(card1, shift=UP * 0.35),
                FadeIn(chev1),
                FadeIn(card2, shift=UP * 0.35),
                FadeIn(chev2),
                FadeIn(card3, shift=UP * 0.35),
                lag_ratio=0.18
            ),
            run_time=1.8
        )

        # Subtle emphasis pulse on Card 1 (Person 1 active speaker)
        card1_box = card1[0]
        self.play(
            card1_box.animate.set_stroke(color=TEHRAN_BLUE, width=3.4),
            run_time=0.55
        )
        self.play(
            card1_box.animate.set_stroke(color=TEHRAN_BLUE, width=2.4),
            run_time=0.55
        )

        # Resting hold frame for Person 1 verbal introduction
        self.wait(2.5)

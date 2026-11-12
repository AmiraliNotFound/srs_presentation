"""
SLIDE-01: TitleCardScene, TitleCardSeg1, TitleCardSeg2
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Foundations)

Visual Choreography:
  - TitleCardSeg1: Signature 3Blue1Brown Write() stroke-draw-and-fill animation for
    "Shock Response Spectrum (SRS)" centered on pure black canvas, followed by
    subtle upward fade-in of the subtitle. Holds final resting frame.
  - TitleCardSeg2: Begins from centered title resting frame. Title glides upward into
    upper position; University of Tehran academic header slides down; SDOF mass-spring-damper
    schematic and pure visual transient excitation/response curves animate in below (zero equation clutter).
  - TitleCardScene: Unified continuous animation of both segments.
"""

from manim import *
import numpy as np


def build_sdof_schematic(motif_y=-0.75, colors=None):
    if colors is None:
        colors = {}
    TEHRAN_BLUE = colors.get("TEHRAN_BLUE", ManimColor("#0097F1"))
    SPRING_CYAN = colors.get("SPRING_CYAN", ManimColor("#58C4DD"))
    FORCE_GOLD  = colors.get("FORCE_GOLD",  ManimColor("#F7CA3B"))
    DAMP_GREEN  = colors.get("DAMP_GREEN",  ManimColor("#83C167"))
    TEXT_WHITE  = colors.get("TEXT_WHITE",  ManimColor("#FFFFFF"))
    TEXT_MUTED  = colors.get("TEXT_MUTED",  ManimColor("#94A3B8"))
    CARD_BG     = colors.get("CARD_BG",     ManimColor("#080D1A"))
    BORDER_DIM  = colors.get("BORDER_DIM",  ManimColor("#1E293B"))

    wall_x = -5.8
    wall_line = Line([wall_x, motif_y - 0.75, 0], [wall_x, motif_y + 0.75, 0], color=TEXT_MUTED, stroke_width=2.5)
    hatches = VGroup(*[
        Line([wall_x, y, 0], [wall_x - 0.22, y + 0.16, 0], color=TEXT_MUTED, stroke_width=1.2)
        for y in np.linspace(motif_y - 0.7, motif_y + 0.62, 8)
    ])
    ground_line = Line([wall_x, motif_y - 0.75, 0], [-2.0, motif_y - 0.75, 0], color=BORDER_DIM, stroke_width=1.5)

    def create_spring(start, end, coils=5, width=0.16):
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

    spring = create_spring([wall_x, motif_y + 0.25, 0], [-3.8, motif_y + 0.25, 0], coils=5, width=0.16)
    spring.set_color(SPRING_CYAN).set_stroke(width=2.5)
    spring_lbl = MathTex(r"k", font_size=24, color=SPRING_CYAN).next_to(spring, UP, buff=0.08)

    d_rod_left = Line([wall_x, motif_y - 0.25, 0], [-4.85, motif_y - 0.25, 0], color=DAMP_GREEN, stroke_width=2)
    d_cylinder = VMobject().set_points_as_corners([
        [-4.4, motif_y - 0.11, 0], [-4.85, motif_y - 0.11, 0],
        [-4.85, motif_y - 0.39, 0], [-4.4, motif_y - 0.39, 0]
    ]).set_color(DAMP_GREEN).set_stroke(width=2)
    d_piston = Line([-4.62, motif_y - 0.13, 0], [-4.62, motif_y - 0.37, 0], color=DAMP_GREEN, stroke_width=2.5)
    d_rod_right = Line([-4.62, motif_y - 0.25, 0], [-3.8, motif_y - 0.25, 0], color=DAMP_GREEN, stroke_width=2)
    damper = VGroup(d_rod_left, d_cylinder, d_piston, d_rod_right)
    damper_lbl = MathTex(r"c", font_size=24, color=DAMP_GREEN).next_to(damper, DOWN, buff=0.08)

    mass_box = RoundedRectangle(
        width=1.2,
        height=0.96,
        corner_radius=0.12,
        stroke_color=TEHRAN_BLUE,
        stroke_width=2.5,
        fill_color=CARD_BG,
        fill_opacity=0.95
    ).move_to([-3.2, motif_y, 0])
    mass_lbl = MathTex(r"m", font_size=30, color=TEXT_WHITE).move_to(mass_box)
    mass_group = VGroup(mass_box, mass_lbl)

    rollers = VGroup(
        Circle(radius=0.07, color=TEXT_MUTED, stroke_width=1.2).move_to([-3.55, motif_y - 0.58, 0]),
        Circle(radius=0.07, color=TEXT_MUTED, stroke_width=1.2).move_to([-2.85, motif_y - 0.58, 0])
    )

    shock_arrow = Arrow(
        start=[-6.65, motif_y, 0],
        end=[-5.85, motif_y, 0],
        color=FORCE_GOLD,
        stroke_width=3.5,
        tip_length=0.18
    )

    return (
        wall_line, hatches, ground_line,
        spring, spring_lbl, damper, damper_lbl,
        mass_group, rollers, shock_arrow
    )


def build_response_curves(motif_y=-0.75, colors=None):
    if colors is None:
        colors = {}
    TEHRAN_BLUE = colors.get("TEHRAN_BLUE", ManimColor("#0097F1"))
    FORCE_GOLD  = colors.get("FORCE_GOLD",  ManimColor("#F7CA3B"))
    BORDER_MID  = colors.get("BORDER_MID",  ManimColor("#334155"))

    ax = Axes(
        x_range=[0, 7.5, 2],
        y_range=[-1.2, 1.4, 1],
        x_length=6.0,
        y_length=2.2,
        axis_config={
            "color": BORDER_MID,
            "stroke_width": 1.5,
            "include_tip": True,
            "tip_width": 0.12,
            "tip_height": 0.12
        }
    ).move_to([2.5, motif_y, 0])

    t0 = 1.5
    omega_pulse = np.pi / t0
    r_ratio = 0.70
    omega_nat = omega_pulse / r_ratio
    zeta_val = 0.05
    f0_scaled = 0.68

    def analytical_response(t):
        if t <= t0:
            return f0_scaled * (1.0 / (1.0 - r_ratio**2)) * (
                np.sin(omega_pulse * t) - r_ratio * np.sin(omega_nat * t)
            )
        else:
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

    pulse_curve = ax.plot(
        lambda t: 1.0 * np.sin(np.pi * t / t0) if t <= t0 else 0.0,
        x_range=[0, t0, 0.02],
        color=FORCE_GOLD,
        stroke_width=3.2
    )

    resp_curve = ax.plot(
        analytical_response,
        x_range=[0, 7.2, 0.02],
        color=TEHRAN_BLUE,
        stroke_width=2.8
    )

    return ax, pulse_curve, resp_curve


class TitleCardSeg1(Scene):
    """
    Step 0: Center screen 3b1b Write() stroke-draw-and-fill of main title and subtitle.
    Holds resting frame.
    """
    def construct(self):
        self.camera.background_color = ManimColor("#000000")

        TEXT_WHITE = ManimColor("#FFFFFF")
        TEXT_OFFWH = ManimColor("#ECEFF4")

        main_title = Tex(
            r"\textbf{Shock Response Spectrum (SRS)}",
            font_size=48,
            color=TEXT_WHITE
        )

        subtitle = Tex(
            r"Transient Shock Dynamics, SDOF Foundations \& Base Isolation Design",
            font_size=23,
            color=TEXT_OFFWH
        )

        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.22).move_to(ORIGIN)

        # Signature 3Blue1Brown stroke-draw-and-fill Write animation
        self.play(Write(main_title), run_time=2.0)
        self.play(FadeIn(subtitle, shift=UP * 0.22), run_time=1.0)
        self.wait(2.5)


class TitleCardSeg2(Scene):
    """
    Step 1: Begins with title centered. Glides up to header position while
    University of Tehran header slides down and uncluttered SDOF schematic & response curves animate in.
    """
    def construct(self):
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")
        SPRING_CYAN = ManimColor("#58C4DD")
        FORCE_GOLD  = ManimColor("#F7CA3B")
        DAMP_GREEN  = ManimColor("#83C167")
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        CARD_BG     = ManimColor("#080D1A")
        BORDER_DIM  = ManimColor("#1E293B")
        BORDER_MID  = ManimColor("#334155")

        colors = {
            "TEHRAN_BLUE": TEHRAN_BLUE,
            "SPRING_CYAN": SPRING_CYAN,
            "FORCE_GOLD":  FORCE_GOLD,
            "DAMP_GREEN":  DAMP_GREEN,
            "TEXT_WHITE":  TEXT_WHITE,
            "TEXT_MUTED":  TEXT_MUTED,
            "CARD_BG":     CARD_BG,
            "BORDER_DIM":  BORDER_DIM,
            "BORDER_MID":  BORDER_MID,
        }

        # Title group at initial centered position (matching end of Seg 1)
        main_title = Tex(
            r"\textbf{Shock Response Spectrum (SRS)}",
            font_size=48,
            color=TEXT_WHITE
        )

        subtitle = Tex(
            r"Transient Shock Dynamics, SDOF Foundations \& Base Isolation Design",
            font_size=23,
            color=TEXT_OFFWH
        )

        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.22).move_to(ORIGIN)
        self.add(title_group)

        # Academic Affiliation Header
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

        # Physical Schematic & Curves
        (
            wall_line, hatches, ground_line,
            spring, spring_lbl, damper, damper_lbl,
            mass_group, rollers, shock_arrow
        ) = build_sdof_schematic(motif_y=-0.75, colors=colors)

        ax, pulse_curve, resp_curve = build_response_curves(motif_y=-0.75, colors=colors)

        # Title glides up, header slides down
        self.play(
            title_group.animate.move_to([0, 1.88, 0]),
            FadeIn(univ_header, shift=DOWN * 0.25),
            FadeIn(dept_header, shift=DOWN * 0.2),
            GrowFromCenter(header_rule),
            run_time=1.4
        )

        # SDOF Schematic enters
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
            run_time=1.3
        )

        # Dynamic excitation pulse and analytical response
        self.play(Create(ax), run_time=0.6)
        self.play(Create(pulse_curve), run_time=1.1)
        self.play(Create(resp_curve), run_time=1.4)

        # Hold final resting frame for speaker verbal presentation
        self.wait(3.0)


class TitleCardScene(Scene):
    """
    Unified 2-step title sequence for single-file playback.
    """
    def construct(self):
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")
        SPRING_CYAN = ManimColor("#58C4DD")
        FORCE_GOLD  = ManimColor("#F7CA3B")
        DAMP_GREEN  = ManimColor("#83C167")
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        CARD_BG     = ManimColor("#080D1A")
        BORDER_DIM  = ManimColor("#1E293B")
        BORDER_MID  = ManimColor("#334155")

        colors = {
            "TEHRAN_BLUE": TEHRAN_BLUE,
            "SPRING_CYAN": SPRING_CYAN,
            "FORCE_GOLD":  FORCE_GOLD,
            "DAMP_GREEN":  DAMP_GREEN,
            "TEXT_WHITE":  TEXT_WHITE,
            "TEXT_MUTED":  TEXT_MUTED,
            "CARD_BG":     CARD_BG,
            "BORDER_DIM":  BORDER_DIM,
            "BORDER_MID":  BORDER_MID,
        }

        main_title = Tex(
            r"\textbf{Shock Response Spectrum (SRS)}",
            font_size=48,
            color=TEXT_WHITE
        )

        subtitle = Tex(
            r"Transient Shock Dynamics, SDOF Foundations \& Base Isolation Design",
            font_size=23,
            color=TEXT_OFFWH
        )

        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.22).move_to(ORIGIN)

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

        (
            wall_line, hatches, ground_line,
            spring, spring_lbl, damper, damper_lbl,
            mass_group, rollers, shock_arrow
        ) = build_sdof_schematic(motif_y=-0.75, colors=colors)

        ax, pulse_curve, resp_curve = build_response_curves(motif_y=-0.75, colors=colors)

        # 3Blue1Brown Write title animation
        self.play(Write(main_title), run_time=2.0)
        self.play(FadeIn(subtitle, shift=UP * 0.22), run_time=1.0)
        self.wait(1.5)

        # Glide up and reveal
        self.play(
            title_group.animate.move_to([0, 1.88, 0]),
            FadeIn(univ_header, shift=DOWN * 0.25),
            FadeIn(dept_header, shift=DOWN * 0.2),
            GrowFromCenter(header_rule),
            run_time=1.4
        )

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
            run_time=1.3
        )

        self.play(Create(ax), run_time=0.6)
        self.play(Create(pulse_curve), run_time=1.1)
        self.play(Create(resp_curve), run_time=1.4)
        self.wait(3.0)

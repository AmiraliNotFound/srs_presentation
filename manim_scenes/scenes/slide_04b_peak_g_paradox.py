"""
SLIDE-04B: PeakGParadoxScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Foundations & Modeling)

3Blue1Brown Physical Intuition Step:
  - 90% open dark canvas.
  - Step 0 (0.0s - 2.0s): Identical shock pulse + Two SDOF spring-mass systems side-by-side:
      Left: Stiff structure (tau_n << Delta t)
      Right: Flexible/tuned structure (tau_n ~ Delta t)
  - Step 1 (2.0s - 7.5s): Animate dynamic response showing vastly different peak deflections x_max.
      Takeaway: Damage depends on natural period (Delta t vs. tau_n), NOT peak g alone!
  - Step 2 (7.5s - 12.0s): The big motivating question for Person 1:
      "How do we predict the peak response for ANY structure (omega_n)?"
"""

from manim import *
import numpy as np


def get_spring(start, end, num_coils=7, width=0.38, color=WHITE, stroke_width=2.4):
    """Generates a clean zigzag spring VMobject between start and end points."""
    dy = end[1] - start[1]
    lead = -0.18
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


class PeakGParadoxScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black Canvas)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # University of Tehran Primary Accent
        SPRING_CYAN = ManimColor("#58C4DD")   # Stiff Structure
        DANGER_RED  = ManimColor("#FF644E")   # Flexible / Resonant Structure & Failure
        FORCE_GOLD  = ManimColor("#F7CA3B")   # Shock Pulse & Motivating Question
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        TEXT_DIM    = ManimColor("#64748B")
        BORDER_MID  = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Top Stage: Title & Identical Shock Pulse
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Same Shock Pulse — Two Different Structures}",
            font_size=32,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # Miniature Input Shock Pulse Display
        ax_pulse = Axes(
            x_range=[0, 1.4, 0.5],
            y_range=[0, 1.2, 0.5],
            x_length=2.4,
            y_length=0.9,
            axis_config={
                "color": TEXT_DIM,
                "stroke_width": 1.2,
                "include_ticks": False,
                "include_tip": True,
                "tip_width": 0.08,
                "tip_height": 0.08,
            }
        ).move_to([-1.1, 2.45, 0])

        t_p = np.linspace(0, 1.0, 60)
        pts_p = [ax_pulse.c2p(t, 1.0 * np.sin(np.pi * t)) for t in t_p]
        pts_p_flat = [ax_pulse.c2p(t, 0.0) for t in np.linspace(1.0, 1.3, 20)]
        curve_pulse = VMobject().set_points_smoothly(pts_p + pts_p_flat).set_color(FORCE_GOLD).set_stroke(width=2.8)
        area_pulse_pts = [ax_pulse.c2p(0, 0)] + pts_p + [ax_pulse.c2p(1.0, 0)]
        area_pulse = Polygon(*area_pulse_pts, color=FORCE_GOLD, stroke_width=0, fill_color=FORCE_GOLD, fill_opacity=0.20)

        lbl_pulse = MathTex(
            r"\text{Identical Input: } a_{\max}, \ \Delta t",
            font_size=20,
            color=FORCE_GOLD
        ).next_to(ax_pulse, RIGHT, buff=0.35)

        pulse_grp = VGroup(ax_pulse, curve_pulse, area_pulse, lbl_pulse)

        # ------------------------------------------------------------------
        # 3. Middle Stage: Two SDOF Spring-Mass Systems
        # ------------------------------------------------------------------
        col_x = 3.70
        y_ceiling = 1.22
        y_eq = -0.05
        m_w, m_h = 1.20, 0.65

        # === LEFT SYSTEM: STIFF STRUCTURE ===
        lbl_stiff_title = Tex(r"\textbf{Stiff Structure}", font_size=24, color=SPRING_CYAN).move_to([-col_x, 1.95, 0])
        lbl_stiff_sub   = MathTex(r"\tau_n \ll \Delta t \ \text{ (Short Period)}", font_size=20, color=TEXT_MUTED).next_to(lbl_stiff_title, DOWN, buff=0.10)

        # Ceiling
        ceil_left_line = Line([-col_x - 1.1, y_ceiling, 0], [-col_x + 1.1, y_ceiling, 0], color=TEXT_DIM, stroke_width=2.4)
        ceil_left_hatches = VGroup(*[
            Line([-col_x - 1.0 + i * 0.22, y_ceiling, 0], [-col_x - 1.0 + i * 0.22 + 0.12, y_ceiling + 0.12, 0], color=TEXT_DIM, stroke_width=1.2)
            for i in range(10)
        ])
        ceil_left = VGroup(ceil_left_line, ceil_left_hatches)

        # Equilibrium baseline
        base_left = DashedLine([-col_x - 1.3, y_eq, 0], [-col_x + 1.3, y_eq, 0], color=BORDER_MID, stroke_width=1.2, dash_length=0.10)

        # Dynamic Mass 1 Tracker
        disp_stiff = ValueTracker(0.0)  # downward displacement

        def get_left_mass():
            y_curr = y_eq - disp_stiff.get_value()
            box = RoundedRectangle(width=m_w, height=m_h, corner_radius=0.10, color=SPRING_CYAN, stroke_width=2.4, fill_color=SPRING_CYAN, fill_opacity=0.22).move_to([-col_x, y_curr, 0])
            txt = MathTex(r"m", font_size=26, color=TEXT_WHITE).move_to([-col_x, y_curr, 0])
            return VGroup(box, txt)

        def get_left_spring():
            y_curr = y_eq - disp_stiff.get_value()
            return get_spring(
                np.array([-col_x, y_ceiling, 0]),
                np.array([-col_x, y_curr + m_h / 2, 0]),
                num_coils=9,
                width=0.36,
                color=SPRING_CYAN,
                stroke_width=2.4
            )

        left_mass = always_redraw(get_left_mass)
        left_spring = always_redraw(get_left_spring)

        # === RIGHT SYSTEM: TUNED / FLEXIBLE STRUCTURE ===
        lbl_flex_title = Tex(r"\textbf{Flexible Structure}", font_size=24, color=DANGER_RED).move_to([col_x, 1.95, 0])
        lbl_flex_sub   = MathTex(r"\tau_n \approx \Delta t \ \text{ (Resonant Period)}", font_size=20, color=TEXT_MUTED).next_to(lbl_flex_title, DOWN, buff=0.10)

        # Ceiling
        ceil_right_line = Line([col_x - 1.1, y_ceiling, 0], [col_x + 1.1, y_ceiling, 0], color=TEXT_DIM, stroke_width=2.4)
        ceil_right_hatches = VGroup(*[
            Line([col_x - 1.0 + i * 0.22, y_ceiling, 0], [col_x - 1.0 + i * 0.22 + 0.12, y_ceiling + 0.12, 0], color=TEXT_DIM, stroke_width=1.2)
            for i in range(10)
        ])
        ceil_right = VGroup(ceil_right_line, ceil_right_hatches)

        # Equilibrium baseline
        base_right = DashedLine([col_x - 1.3, y_eq, 0], [col_x + 1.3, y_eq, 0], color=BORDER_MID, stroke_width=1.2, dash_length=0.10)

        # Dynamic Mass 2 Tracker
        disp_flex = ValueTracker(0.0)  # downward displacement

        def get_right_mass():
            y_curr = y_eq - disp_flex.get_value()
            box = RoundedRectangle(width=m_w, height=m_h, corner_radius=0.10, color=DANGER_RED, stroke_width=2.4, fill_color=DANGER_RED, fill_opacity=0.22).move_to([col_x, y_curr, 0])
            txt = MathTex(r"m", font_size=26, color=TEXT_WHITE).move_to([col_x, y_curr, 0])
            return VGroup(box, txt)

        def get_right_spring():
            y_curr = y_eq - disp_flex.get_value()
            return get_spring(
                np.array([col_x, y_ceiling, 0]),
                np.array([col_x, y_curr + m_h / 2, 0]),
                num_coils=5,
                width=0.42,
                color=DANGER_RED,
                stroke_width=2.4
            )

        right_mass = always_redraw(get_right_mass)
        right_spring = always_redraw(get_right_spring)

        # Static representations for Step 0 initialization
        init_left_spring = get_spring(np.array([-col_x, y_ceiling, 0]), np.array([-col_x, y_eq + m_h / 2, 0]), num_coils=9, width=0.36, color=SPRING_CYAN)
        init_left_mass = get_left_mass()
        init_right_spring = get_spring(np.array([col_x, y_ceiling, 0]), np.array([col_x, y_eq + m_h / 2, 0]), num_coils=5, width=0.42, color=DANGER_RED)
        init_right_mass = get_right_mass()

        # ------------------------------------------------------------------
        # 4. Step 1 Callouts: Peak Deflections & Takeaway
        # ------------------------------------------------------------------
        y_peak_stiff = y_eq - 0.32
        y_peak_flex  = y_eq - 1.15

        # Left Peak Deflection Arrow & Label
        arr_left = DoubleArrow(
            start=[-col_x + 0.85, y_eq, 0],
            end=[-col_x + 0.85, y_peak_stiff, 0],
            color=SPRING_CYAN,
            stroke_width=2.4,
            tip_length=0.14
        )
        lbl_left_pk = MathTex(r"x_{\max} \text{ (Small)}", font_size=19, color=SPRING_CYAN).next_to(arr_left, RIGHT, buff=0.12)
        callout_left = VGroup(arr_left, lbl_left_pk)

        # Right Peak Deflection Arrow & Label
        arr_right = DoubleArrow(
            start=[col_x + 0.85, y_eq, 0],
            end=[col_x + 0.85, y_peak_flex, 0],
            color=DANGER_RED,
            stroke_width=2.8,
            tip_length=0.16
        )
        lbl_right_pk1 = MathTex(r"x_{\max} \ (3.6\times\text{ Larger!})", font_size=20, color=DANGER_RED)
        lbl_right_pk2 = Tex(r"\textbf{Dynamic Yield \& Failure}", font_size=17, color=DANGER_RED)
        lbl_right_pk = VGroup(lbl_right_pk1, lbl_right_pk2).arrange(DOWN, buff=0.08).next_to(arr_right, RIGHT, buff=0.12)
        callout_right = VGroup(arr_right, lbl_right_pk)

        # Center Dynamic Insight
        insight_text = Tex(
            r"\textbf{Damage depends on natural period } $\tau_n$\textbf{, NOT just peak } $g$\textbf{!}",
            font_size=23,
            color=TEXT_OFFWH
        ).move_to([0, -1.85, 0])

        # ------------------------------------------------------------------
        # 5. Step 2 Callout: The Big Motivating Question
        # ------------------------------------------------------------------
        big_question = MathTex(
            r"\text{How do we predict the peak response for ANY structure } (\omega_n)\text{?}",
            font_size=36,
            color=FORCE_GOLD
        ).move_to([0, -2.75, 0])

        q_sub = Tex(
            r"The motivating challenge behind the Shock Response Spectrum",
            font_size=20,
            color=TEXT_MUTED
        ).next_to(big_question, DOWN, buff=0.16)

        grp_question = VGroup(big_question, q_sub)

        # ------------------------------------------------------------------
        # 6. Step-Controlled Timeline & Cuepoint Choreography
        # ------------------------------------------------------------------
        # --- Step 0: Minimal Load (0.0s - 2.0s -> Cuepoint 0 = 2.0s) ---
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            FadeIn(pulse_grp, shift=DOWN * 0.12),
            run_time=0.8
        )
        self.play(
            FadeIn(lbl_stiff_title),
            FadeIn(lbl_stiff_sub),
            Create(ceil_left),
            Create(base_left),
            FadeIn(lbl_flex_title),
            FadeIn(lbl_flex_sub),
            Create(ceil_right),
            Create(base_right),
            FadeIn(init_left_spring),
            FadeIn(init_left_mass),
            FadeIn(init_right_spring),
            FadeIn(init_right_mass),
            run_time=0.7
        )
        self.wait(0.5)  # Rest hold at t = 2.0s

        # Swap static initial objects with always_redraw dynamic objects
        self.remove(init_left_spring, init_left_mass, init_right_spring, init_right_mass)
        self.add(left_spring, left_mass, right_spring, right_mass)

        # --- Step 1: Dynamic Response & Peak Deflections (2.0s - 7.5s -> Cuepoint 1 = 7.5s) ---
        # Animate oscillations
        # First major downward stroke reaching peak deflection:
        self.play(
            disp_stiff.animate.set_value(0.32),
            disp_flex.animate.set_value(1.15),
            run_time=1.0,
            rate_func=smooth
        )
        # Callouts reveal at maximum deflection:
        self.play(
            FadeIn(callout_left, shift=DOWN * 0.1),
            FadeIn(callout_right, shift=DOWN * 0.1),
            FadeIn(insight_text, shift=UP * 0.15),
            run_time=0.8
        )
        # Continue free oscillation rebound with damping:
        self.play(
            disp_stiff.animate.set_value(-0.18),
            disp_flex.animate.set_value(-0.45),
            run_time=0.8,
            rate_func=smooth
        )
        self.play(
            disp_stiff.animate.set_value(0.08),
            disp_flex.animate.set_value(0.25),
            run_time=0.6,
            rate_func=smooth
        )
        self.play(
            disp_stiff.animate.set_value(0.0),
            disp_flex.animate.set_value(0.0),
            run_time=0.5,
            rate_func=smooth
        )
        self.wait(1.8)  # Rest hold at t = 7.5s

        # --- Step 2: The Motivating Question (7.5s - 12.0s -> Cuepoint 2 = 12.0s) ---
        self.play(
            Write(big_question),
            FadeIn(q_sub, shift=UP * 0.15),
            run_time=1.2
        )
        # Subtle pulse on the question
        self.play(
            big_question.animate.scale(1.05),
            run_time=0.3
        )
        self.play(
            big_question.animate.scale(1 / 1.05),
            run_time=0.3
        )
        self.wait(2.7)  # Rest hold until t = 12.0s

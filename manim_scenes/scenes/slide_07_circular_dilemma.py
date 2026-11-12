"""
SLIDE-07: CircularDilemmaScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Foundations & Modeling — Hand-Off to Person 2)
Allocated Time: 12:00 – 15:00 (180 s)

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 6 English words total)
      "The Circular Dilemma" (3 words)
      "Requires SRS Theory" (3 words)
  - Step 0 (0.0s - 3.0s): Title & center-stage design parameter d
  - Step 1 (3.0s - 7.5s): Closed circular feedback loop blooms with glowing tracer
  - Step 2 (7.5s - 13.0s): Loop freezes at unknown DLF = ?, forward arrow breaks out: Requires SRS Theory
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic
import numpy as np


class CircularDilemmaScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        AMBER       = ManimColor("#FFB703")   # Design parameter d & tracer
        CYAN        = ManimColor("#58C4DD")   # Stiffness k, period tau_n, ratio t0/tau_n
        CORAL       = ManimColor("#FF644E")   # DLF & SRS breakout
        YELLOW      = ManimColor("#F7CA3B")   # Peak root stress sigma_max
        BARRIER_RED = ManimColor("#E63946")   # DLF = ? unknown barrier
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        BG_DARK     = ManimColor("#0B0F19")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{The Circular Dilemma}",
            font_size=36,
            color=TEXT_WHITE
        ).move_to([0, 3.35, 0])

        # ------------------------------------------------------------------
        # 3. Geometry of the 6-Node Circular Feedback Loop
        # ------------------------------------------------------------------
        x_c = -0.90
        y_c = -0.25
        center = np.array([x_c, y_c, 0])
        R = 2.30

        # Mathematical angles for 6 nodes (Counter-Clockwise along unit circle)
        # Node 4 (DLF) sits at 0 deg (rightmost equator)
        # Node 5 (sigma_max) sits at 60 deg
        # Node 0 (d) sits at 120 deg (top-left)
        # Node 1 (k) sits at 180 deg (leftmost equator)
        # Node 2 (tau_n) sits at 240 deg (bottom-left)
        # Node 3 (t0/tau_n) sits at 300 deg (bottom-right)
        node_angles_deg = [120, 180, 240, 300, 0, 60]
        node_pos = [
            center + np.array([R * np.cos(np.radians(deg)), R * np.sin(np.radians(deg)), 0])
            for deg in node_angles_deg
        ]

        # Helper function for sleek dark rounded badges
        def make_badge(tex_str, color, width, height, font_size=28):
            rect = RoundedRectangle(
                corner_radius=0.14,
                width=width,
                height=height,
                color=color,
                stroke_width=2.2,
                fill_color=BG_DARK,
                fill_opacity=0.92
            )
            tex = MathTex(tex_str, font_size=font_size, color=color)
            tex.move_to(rect.get_center())
            return VGroup(rect, tex)

        # Create the 6 mathematical node badges
        badge_d = make_badge(r"d", AMBER, width=1.15, height=0.66, font_size=36)
        badge_d.move_to(node_pos[0])

        badge_k = make_badge(r"k \propto d^3", CYAN, width=1.45, height=0.66, font_size=28)
        badge_k.move_to(node_pos[1])

        badge_tau = make_badge(r"\tau_n = 2\pi\sqrt{\frac{m_{\text{eq}}}{k}}", CYAN, width=1.80, height=0.72, font_size=22)
        badge_tau.move_to(node_pos[2])

        badge_ratio = make_badge(r"\frac{t_0}{\tau_n}", CYAN, width=1.25, height=0.72, font_size=30)
        badge_ratio.move_to(node_pos[3])

        badge_dlf = make_badge(r"\mathbf{DLF}", CORAL, width=1.30, height=0.66, font_size=32)
        badge_dlf.move_to(node_pos[4])

        badge_sigma = make_badge(r"\sigma_{\max} = \frac{6 F_{\text{dyn}} l}{b d^2}", YELLOW, width=1.85, height=0.72, font_size=22)
        badge_sigma.move_to(node_pos[5])

        # All badges to bloom in Step 1
        all_loop_badges = [badge_k, badge_tau, badge_ratio, badge_dlf, badge_sigma]
        # Badges to dim in Step 2 (DLF stays fully highlighted)
        dimmed_badges = [badge_k, badge_tau, badge_ratio, badge_sigma]
        dimmed_badges_group = VGroup(*dimmed_badges)

        # ------------------------------------------------------------------
        # 4. Connecting Arrows (Boundary-Exact, Zero-Overlap)
        # ------------------------------------------------------------------
        arrows = [
            # Arrow 0: d -> k (curving down-left)
            CurvedArrow(np.array([-2.40, 1.35, 0]), np.array([-3.15, 0.18, 0]), angle=-TAU / 14, color=AMBER, stroke_width=2.5),
            # Arrow 1: k -> tau_n (curving down-right)
            CurvedArrow(np.array([-3.15, -0.68, 0]), np.array([-2.55, -1.82, 0]), angle=-TAU / 14, color=CYAN, stroke_width=2.5),
            # Arrow 2: tau_n -> ratio (clean horizontal across bottom)
            Arrow(start=np.array([-1.05, -2.24, 0]), end=np.array([-0.45, -2.24, 0]), color=CYAN, stroke_width=2.5, buff=0.0, max_tip_length_to_length_ratio=0.30),
            # Arrow 3: ratio -> DLF (curving up-right)
            CurvedArrow(np.array([0.82, -1.80, 0]), np.array([1.35, -0.68, 0]), angle=-TAU / 14, color=CYAN, stroke_width=2.5),
            # Arrow 4: DLF -> sigma_max (curving up-left)
            CurvedArrow(np.array([1.35, 0.18, 0]), np.array([0.82, 1.30, 0]), angle=-TAU / 14, color=CORAL, stroke_width=2.5),
            # Arrow 5: sigma_max -> d (clean horizontal across top)
            Arrow(start=np.array([-0.75, 1.74, 0]), end=np.array([-1.38, 1.74, 0]), color=YELLOW, stroke_width=2.5, buff=0.0, max_tip_length_to_length_ratio=0.30),
        ]

        arrows_group = VGroup(*arrows)

        # ------------------------------------------------------------------
        # 5. Continuous Luminous Tracer Particle
        # ------------------------------------------------------------------
        circle_path = Circle(radius=R).move_to(center)
        tracer_alpha = ValueTracker(2.0 / 6.0)  # Starts at Node 0 (120 deg = 2/6 proportion)

        tracer_dot = Dot(radius=0.08, color=AMBER)
        tracer_halo = Dot(radius=0.18, color=AMBER, fill_opacity=0.35)
        tracer_group = VGroup(tracer_halo, tracer_dot)
        tracer_group.move_to(circle_path.point_from_proportion(tracer_alpha.get_value() % 1.0))

        tracer_group.add_updater(
            lambda mob: mob.move_to(circle_path.point_from_proportion(tracer_alpha.get_value() % 1.0))
        )

        # ------------------------------------------------------------------
        # 6. Step 0 Initial Center-Stage Visuals
        # ------------------------------------------------------------------
        d_center_box = RoundedRectangle(
            corner_radius=0.18,
            width=1.65,
            height=1.15,
            color=AMBER,
            stroke_width=2.4,
            fill_color=BG_DARK,
            fill_opacity=0.92
        ).move_to([0, 0, 0])

        d_center_tex = MathTex(r"d", font_size=48, color=AMBER).move_to(d_center_box.get_center() + UP * 0.12)
        d_center_sub = Tex(r"\text{Thickness}", font_size=20, color=AMBER).move_to(d_center_box.get_center() + DOWN * 0.28)
        d_center_group = VGroup(d_center_box, d_center_tex, d_center_sub)

        # ------------------------------------------------------------------
        # 7. Step 2 Unknown Barrier & Hand-Off Climax
        # ------------------------------------------------------------------
        # DLF Barrier Halo & Unknown Alert
        dlf_pos = node_pos[4]
        dlf_halo = RoundedRectangle(
            corner_radius=0.18,
            width=1.52,
            height=0.86,
            color=BARRIER_RED,
            stroke_width=3.6,
            stroke_opacity=0.75,
            fill_opacity=0.0
        ).move_to(dlf_pos)

        dlf_unknown_tex = MathTex(
            r"\mathbf{DLF} = \boldsymbol{?}",
            font_size=34,
            color=BARRIER_RED
        ).move_to([dlf_pos[0], dlf_pos[1] + 0.68, 0])

        # Forward breakout arrow to Person 2
        arrow_srs = Arrow(
            start=np.array([dlf_pos[0] + 0.90, dlf_pos[1], 0]),
            end=np.array([dlf_pos[0] + 1.85, dlf_pos[1], 0]),
            color=CORAL,
            stroke_width=3.6,
            max_tip_length_to_length_ratio=0.22
        )

        srs_text = Tex(
            r"\textbf{Requires SRS Theory}",
            font_size=28,
            color=TEXT_WHITE
        ).next_to(arrow_srs, RIGHT, buff=0.25)

        # ------------------------------------------------------------------
        # ANIMATION SEQUENCE (3 Steps, 2 Cuepoint Pauses)
        # ------------------------------------------------------------------

        # --- STEP 0: Title & Design Parameter d (0.0s - 3.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(d_center_group, scale=0.85), run_time=0.6)
        self.play(d_center_group.animate.scale(1.10), run_time=0.4)
        self.play(d_center_group.animate.scale(1.0 / 1.10), run_time=0.4)
        self.wait(1.0)  # Exact Cuepoint 0 = 3.0s

        # --- STEP 1: The Closed Feedback Loop Forms (3.0s - 7.5s) ---
        # 1. d moves to circular position (120 deg) while "Thickness" fades
        self.play(FadeOut(d_center_sub), run_time=0.3)
        self.play(
            ReplacementTransform(d_center_box, badge_d[0]),
            ReplacementTransform(d_center_tex, badge_d[1]),
            run_time=0.7
        )

        # 2. Bloom remaining 5 badges and 6 connecting curved arrows
        self.play(
            LaggedStart(
                *[FadeIn(b, scale=0.85) for b in all_loop_badges],
                *[Create(a) for a in arrows],
                lag_ratio=0.10
            ),
            run_time=1.2
        )

        # 3. Luminous tracer particle appears and circulates full loop
        self.play(FadeIn(tracer_group, scale=0.6), run_time=0.3)
        self.play(
            tracer_alpha.animate.set_value(2.0 / 6.0 + 1.0),
            run_time=1.5,
            rate_func=linear
        )
        self.wait(0.5)  # Exact Cuepoint 1 = 7.5s

        # --- STEP 2: The Barrier on DLF & Hand-Off Climax (7.5s - 13.0s) ---
        # 1. Tracer completes fraction into DLF (0 deg / alpha = 2.0) and freezes
        self.play(
            tracer_alpha.animate.set_value(2.0),
            run_time=0.8,
            rate_func=ease_out_cubic
        )
        tracer_group.clear_updaters()

        # 2. Loop dims, tracer dissolves, DLF pulses red barrier with DLF = ?
        self.play(
            dimmed_badges_group.animate.set_opacity(0.24),
            arrows_group.animate.set_opacity(0.20),
            badge_d.animate.set_opacity(0.24),
            FadeOut(tracer_group, run_time=0.4),
            badge_dlf[0].animate.set_stroke(color=BARRIER_RED, width=3.8),
            badge_dlf[1].animate.set_color(TEXT_WHITE),
            FadeIn(dlf_halo, scale=1.08),
            Write(dlf_unknown_tex),
            run_time=1.2
        )

        # 3. Forward breakout arrow and SRS Theory resolution for Person 2
        self.play(
            GrowArrow(arrow_srs),
            Write(srs_text),
            run_time=1.5
        )
        self.wait(2.0)  # Exact Cuepoint 2 = 13.0s

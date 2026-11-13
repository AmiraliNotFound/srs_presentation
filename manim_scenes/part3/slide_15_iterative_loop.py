"""
SLIDE-15: IterativeDesignScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 150 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Large presentation-grade mathematical typography (font sizes 27-42)
  - Perfectly balanced, harmonious widescreen elliptical cycle (zero scattered appearance)
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 7 English words total)
      "Closing the Dilemma Loop" (4 words)
      "Iterate until safe" (3 words)
  - Frame-Accurate Step Control:
      Step 0 (0.0s - 3.5s): Recall circular dilemma with DLF = ? unknown barrier
      Step 1 (3.5s - 8.5s): Half-Sine SRS curve bridges the gap, unlocks DLF
      Step 2 (8.5s - 14.2s): Dynamic load F_dyn, flexural stress sigma_max, and closed iteration loop
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine, linear
import numpy as np


class IterativeDesignScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        AMBER       = ManimColor("#FFB703")   # Parameter d & tracer
        CYAN        = ManimColor("#58C4DD")   # Stiffness k, period tau_n, ratio t0/tau_n
        CORAL       = ManimColor("#FF644E")   # Half-Sine SRS spectrum curve & DLF
        UT_BLUE     = ManimColor("#0097F1")   # Dynamic force F_dyn
        GREEN_PASS  = ManimColor("#83C167")   # Stress check & closed loop safe state
        BARRIER_RED = ManimColor("#E63946")   # DLF = ? barrier
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        BG_DARK     = ManimColor("#0B0F19")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 4 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Closing the Dilemma Loop}",
            font_size=38,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        # ------------------------------------------------------------------
        # 3. Helper function for sleek rounded dark badges
        # ------------------------------------------------------------------
        def make_badge(tex_str, color, width, height, font_size=28):
            rect = RoundedRectangle(
                corner_radius=0.15,
                width=width,
                height=height,
                color=color,
                stroke_width=2.4,
                fill_color=BG_DARK,
                fill_opacity=0.92
            )
            tex = MathTex(tex_str, font_size=font_size, color=color)
            tex.move_to(rect.get_center())
            return VGroup(rect, tex)

        # ------------------------------------------------------------------
        # 4. Geometry and Node Layout (Harmonious 16:9 Symmetrical Cycle)
        # ------------------------------------------------------------------
        # Left Arc: Dilemma chain
        pos_d      = np.array([-3.30,  1.50, 0])
        pos_k      = np.array([-4.60, -0.20, 0])
        pos_tau    = np.array([-3.15, -2.00, 0])
        pos_ratio  = np.array([-0.75, -2.00, 0])

        # Right Arc: Solution chain
        pos_srs    = np.array([ 1.65, -1.90, 0])  # Miniature SRS bridge
        pos_dlf    = np.array([ 4.35, -0.25, 0])
        pos_fdyn   = np.array([ 3.65,  1.30, 0])
        pos_sigma  = np.array([ 0.05,  1.80, 0])

        # Node Badges with enlarged, presentation-grade fonts
        badge_d = make_badge(r"d", AMBER, width=1.30, height=0.82, font_size=42).move_to(pos_d)
        badge_k = make_badge(r"k \propto d^3", CYAN, width=1.85, height=0.82, font_size=32).move_to(pos_k)
        badge_tau = make_badge(r"\tau_n = 2\pi\sqrt{\frac{W_{\text{eq}}}{g k}}", CYAN, width=2.40, height=0.86, font_size=28).move_to(pos_tau)
        badge_ratio = make_badge(r"\frac{t_0}{\tau_n}", CYAN, width=1.40, height=0.86, font_size=36).move_to(pos_ratio)

        # DLF Badge (Step 1 reveal)
        badge_dlf = make_badge(r"\mathbf{DLF}", CORAL, width=1.55, height=0.82, font_size=38).move_to(pos_dlf)

        # Dynamic Force & Stress Badges (Step 2 reveal)
        badge_fdyn = make_badge(
            r"F_{\text{dyn}} = 100 \cdot \text{DLF} \cdot W_{\text{eq}}",
            UT_BLUE,
            width=3.25,
            height=0.86,
            font_size=27
        ).move_to(pos_fdyn)

        badge_sigma = make_badge(
            r"\sigma_{\max} = \frac{6 F_{\text{dyn}} l}{b d^2} \le 26\text{ ksi}",
            GREEN_PASS,
            width=3.30,
            height=0.86,
            font_size=27
        ).move_to(pos_sigma)

        # ------------------------------------------------------------------
        # 5. Connecting Curved Arrows for Dilemma Arc
        # ------------------------------------------------------------------
        arrow_d_k = CurvedArrow(
            badge_d[0].get_edge_center(DOWN + LEFT) + RIGHT * 0.1,
            badge_k[0].get_edge_center(UP + RIGHT) + DOWN * 0.05,
            angle=TAU / 16,
            color=AMBER,
            stroke_width=2.8
        )
        arrow_k_tau = CurvedArrow(
            badge_k[0].get_edge_center(DOWN + RIGHT) + UP * 0.05,
            badge_tau[0].get_edge_center(UP + LEFT) + RIGHT * 0.1,
            angle=TAU / 16,
            color=CYAN,
            stroke_width=2.8
        )
        arrow_tau_ratio = Arrow(
            start=badge_tau[0].get_right(),
            end=badge_ratio[0].get_left(),
            buff=0.12,
            color=CYAN,
            stroke_width=2.8,
            max_tip_length_to_length_ratio=0.28
        )

        # ------------------------------------------------------------------
        # 6. Step 0: Blocked Barrier at DLF = ?
        # ------------------------------------------------------------------
        pos_barrier = np.array([1.65, -1.90, 0])

        arrow_ratio_barrier = Arrow(
            start=badge_ratio[0].get_right(),
            end=pos_barrier + np.array([-1.05, 0.0, 0]),
            buff=0.12,
            color=BARRIER_RED,
            stroke_width=2.8,
            max_tip_length_to_length_ratio=0.25
        )

        dlf_barrier_box = RoundedRectangle(
            corner_radius=0.15,
            width=2.10,
            height=0.95,
            color=BARRIER_RED,
            stroke_width=2.8,
            fill_color=BG_DARK,
            fill_opacity=0.92
        ).move_to(pos_barrier)

        dlf_barrier_tex = MathTex(
            r"\mathbf{DLF} = \boldsymbol{?}",
            font_size=34,
            color=BARRIER_RED
        ).move_to(pos_barrier)

        dlf_barrier_halo = RoundedRectangle(
            corner_radius=0.18,
            width=2.30,
            height=1.15,
            color=BARRIER_RED,
            stroke_width=2.0,
            stroke_opacity=0.45,
            fill_opacity=0.0
        ).move_to(pos_barrier)

        barrier_group = VGroup(arrow_ratio_barrier, dlf_barrier_box, dlf_barrier_tex, dlf_barrier_halo)

        # ------------------------------------------------------------------
        # 7. Step 1: Miniature Half-Sine SRS Spectrum Bridge
        # ------------------------------------------------------------------
        # Coordinate frame for miniature SRS
        srs_frame = RoundedRectangle(
            corner_radius=0.14,
            width=2.45,
            height=1.80,
            color=CORAL,
            stroke_width=2.0,
            stroke_opacity=0.85,
            fill_color=BG_DARK,
            fill_opacity=0.94
        ).move_to(pos_srs)

        # Miniature Axes inside the frame
        srs_axes = Axes(
            x_range=[0, 3.0, 1.0],
            y_range=[0, 2.0, 1.0],
            x_length=1.85,
            y_length=1.15,
            axis_config={
                "color": TEXT_MUTED,
                "stroke_width": 1.6,
                "include_tip": True,
                "tip_width": 0.12,
                "tip_height": 0.12
            }
        ).move_to(pos_srs + np.array([-0.05, -0.10, 0]))

        # Exact smooth Half-Sine Maximax SRS curve (no singularity)
        def srs_maximax(u):
            if u <= 0.0:
                return 0.0
            elif u < 0.8:
                return 1.76 * np.sin((np.pi / 2.0) * (u / 0.8)**0.88)
            else:
                return 1.0 + 0.76 * np.exp(-1.3 * (u - 0.8)) * np.cos(3.2 * (u - 0.8))

        srs_curve = srs_axes.plot(
            srs_maximax,
            x_range=[0.02, 2.8, 0.02],
            color=CORAL,
            stroke_width=2.8
        )

        srs_curve_glow = srs_curve.copy().set_stroke(color=CORAL, width=6.0, opacity=0.35)

        srs_label_x = MathTex(r"\frac{t_0}{\tau_n}", font_size=20, color=TEXT_MUTED).next_to(
            srs_axes.x_axis.get_end(), DOWN, buff=0.08
        )
        srs_label_y = MathTex(r"\text{DLF}", font_size=20, color=CORAL).next_to(
            srs_axes.y_axis.get_end(), UP, buff=0.08
        )

        srs_bridge_group = VGroup(
            srs_frame, srs_axes, srs_curve_glow, srs_curve, srs_label_x, srs_label_y
        )

        # Bridge arrow from ratio to SRS frame (clean horizontal connector)
        arrow_ratio_srs = Arrow(
            start=badge_ratio[0].get_right(),
            end=srs_frame.get_left(),
            buff=0.12,
            color=CYAN,
            stroke_width=2.8,
            max_tip_length_to_length_ratio=0.25
        )

        # Output curved arrow from SRS frame to DLF badge (flowing naturally up-right)
        arrow_srs_dlf = CurvedArrow(
            srs_frame.get_edge_center(RIGHT) + UP * 0.10,
            badge_dlf[0].get_edge_center(LEFT) + DOWN * 0.10,
            angle=-TAU / 20,
            color=CORAL,
            stroke_width=3.0
        )

        # Luminous tracer on SRS operating point (u = 0.8, DLF = 1.76)
        tracer_point = Dot(
            point=srs_axes.c2p(0.8, 1.76),
            radius=0.08,
            color=AMBER
        )
        tracer_point_glow = Dot(
            point=srs_axes.c2p(0.8, 1.76),
            radius=0.20,
            color=AMBER,
            fill_opacity=0.45
        )
        tracer_val_tex = MathTex(r"1.76", font_size=17, color=AMBER).next_to(
            tracer_point, UP, buff=0.10
        )
        srs_sample_dot = VGroup(tracer_point_glow, tracer_point, tracer_val_tex)

        # ------------------------------------------------------------------
        # 8. Step 2: Solution Chain Arrows & Feedback Loop
        # ------------------------------------------------------------------
        # Arrow DLF -> F_dyn (smooth upward curve along elliptical contour)
        arrow_dlf_fdyn = CurvedArrow(
            badge_dlf[0].get_edge_center(UP) + LEFT * 0.15,
            badge_fdyn[0].get_edge_center(DOWN) + RIGHT * 0.20,
            angle=TAU / 20,
            color=UT_BLUE,
            stroke_width=2.8
        )

        # Arrow F_dyn -> sigma_max (smooth curving arch from right to center-top)
        arrow_fdyn_sigma = CurvedArrow(
            badge_fdyn[0].get_edge_center(LEFT) + UP * 0.05,
            badge_sigma[0].get_edge_center(RIGHT) + DOWN * 0.05,
            angle=TAU / 18,
            color=GREEN_PASS,
            stroke_width=2.8
        )

        # Feedback arrow: sigma_max -> d (closing loop across top-left)
        arrow_feedback = CurvedArrow(
            badge_sigma[0].get_edge_center(LEFT) + UP * 0.10,
            badge_d[0].get_edge_center(RIGHT + UP) + DOWN * 0.05,
            angle=TAU / 14,
            color=GREEN_PASS,
            stroke_width=3.2
        )

        # Elegant feedback badge sitting comfortably above between sigma and d
        feedback_rect = RoundedRectangle(
            corner_radius=0.14,
            width=2.25,
            height=0.52,
            color=GREEN_PASS,
            stroke_width=1.8,
            fill_color=BG_DARK,
            fill_opacity=0.92
        ).move_to([-1.65, 2.50, 0])

        feedback_tex = Tex(
            r"\textbf{Iterate until safe}",
            font_size=23,
            color=GREEN_PASS
        ).move_to(feedback_rect.get_center())

        feedback_group = VGroup(arrow_feedback, feedback_rect, feedback_tex)

        # Full closed loop glowing halo around badge_d
        d_glow = RoundedRectangle(
            corner_radius=0.20,
            width=1.50,
            height=1.00,
            color=GREEN_PASS,
            stroke_width=2.6,
            stroke_opacity=0.60,
            fill_opacity=0.0
        ).move_to(pos_d)

        # Luminous tracer sweeping closed circuit
        loop_path = VMobject()
        loop_path.set_points_smoothly([
            pos_d,
            pos_k,
            pos_tau,
            pos_ratio,
            pos_srs + np.array([0, 0.15, 0]),
            pos_dlf,
            pos_fdyn,
            pos_sigma,
            pos_d
        ])

        tracer_circle = Dot(radius=0.09, color=GREEN_PASS)
        tracer_halo = Dot(radius=0.22, color=GREEN_PASS, fill_opacity=0.40)
        sweeper = VGroup(tracer_halo, tracer_circle).move_to(loop_path.point_from_proportion(0))

        # ------------------------------------------------------------------
        # ANIMATION SEQUENCE (3 Steps, Frame-Accurate Cuepoints: 3.5, 8.5, 14.2)
        # ------------------------------------------------------------------

        # ==================================================================
        # STEP 0: Recall Circular Dilemma & Unknown Barrier (0.0s - 3.5s)
        # ==================================================================
        # 0.0s - 0.5s: Title fade
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.5)

        # 0.5s - 2.0s: Dilemma chain blooms (d -> k -> tau_n -> t0/tau_n -> barrier)
        self.play(
            FadeIn(badge_d, scale=0.90),
            Create(arrow_d_k),
            FadeIn(badge_k, scale=0.90),
            Create(arrow_k_tau),
            FadeIn(badge_tau, scale=0.90),
            Create(arrow_tau_ratio),
            FadeIn(badge_ratio, scale=0.90),
            run_time=1.5
        )

        # 2.0s - 2.7s: Barrier red DLF = ? flashes on right
        self.play(
            Create(arrow_ratio_barrier),
            FadeIn(dlf_barrier_box),
            Write(dlf_barrier_tex),
            FadeIn(dlf_barrier_halo, scale=1.08),
            run_time=0.7
        )

        # 2.7s - 3.5s: Hold for cuepoint 1
        self.wait(0.8)  # Exact Cuepoint 1 = 3.5s

        # ==================================================================
        # STEP 1: SRS Curve Bridges the Gap & Unlocks DLF (3.5s - 8.5s)
        # ==================================================================
        # 3.5s - 4.2s: Dissolve barrier
        self.play(
            FadeOut(barrier_group),
            run_time=0.7
        )

        # 4.2s - 5.6s: Miniature SRS Spectrum Bridge blooms into place
        self.play(
            Create(arrow_ratio_srs),
            FadeIn(srs_frame),
            Create(srs_axes),
            Write(srs_label_x),
            Write(srs_label_y),
            Create(srs_curve_glow),
            Create(srs_curve),
            run_time=1.4
        )

        # 5.6s - 6.6s: Luminous tracer indexes into SRS curve
        self.play(
            FadeIn(srs_sample_dot, scale=0.6),
            srs_sample_dot.animate.scale(1.15).set_color(AMBER),
            run_time=1.0
        )

        # 6.6s - 7.6s: Output arrow extends to DLF badge (Unlocked!)
        self.play(
            Create(arrow_srs_dlf),
            FadeIn(badge_dlf, scale=0.85),
            badge_dlf[0].animate.set_stroke(color=CORAL, width=3.2),
            run_time=1.0
        )

        # 7.6s - 8.5s: Hold for cuepoint 2
        self.wait(0.9)  # Exact Cuepoint 2 = 8.5s

        # ==================================================================
        # STEP 2: Complete Design Loop Closure & Iteration (8.5s - 14.2s+)
        # ==================================================================
        # 8.5s - 9.6s: DLF feeds dynamic inertia force F_dyn
        self.play(
            Create(arrow_dlf_fdyn),
            FadeIn(badge_fdyn, shift=LEFT * 0.2),
            run_time=1.1
        )

        # 9.6s - 10.7s: F_dyn feeds root bending stress sigma_max
        self.play(
            Create(arrow_fdyn_sigma),
            FadeIn(badge_sigma, shift=DOWN * 0.15),
            run_time=1.1
        )

        # 10.7s - 12.0s: Feedback arrow routes back to d, closing the loop
        self.play(
            Create(arrow_feedback),
            FadeIn(feedback_rect),
            Write(feedback_tex),
            FadeIn(d_glow, scale=1.08),
            run_time=1.3
        )

        # 12.0s - 13.5s: Luminous green circuit sweeper animates full loop
        self.play(
            MoveAlongPath(sweeper, loop_path),
            run_time=1.5,
            rate_func=linear
        )
        self.play(FadeOut(sweeper), run_time=0.2)

        # 13.7s - 15.0s: Final state hold (Cuepoint 3 = 14.2s)
        self.wait(1.3)  # Reaches 15.0s total duration

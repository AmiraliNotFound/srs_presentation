"""
SLIDE-16: StressVerificationScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 150 s

3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Large presentation-grade mathematical typography
  - Symmetrical 3-column comparative iteration matrix
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 6 English words total)
      "Evaluating Bracket Thickness" (3 words)
      "FAIL" (1 word)
      "FAIL" (1 word)
      "CERTIFIED" (1 word)
  - Frame-Accurate Step Control:
      Step 1 (0.0s - 3.5s): Trial 1 (d = 0.40 in: sigma = 41.3 ksi > 26 ksi FAILS)
      Step 2 (3.5s - 8.0s): Trial 2 (d = 0.50 in: sigma = 34.3 ksi > 26 ksi FAILS)
      Step 3 (8.0s - 14.2s): Trial 3 (d = 0.60 in: sigma = 25.7 ksi <= 26 ksi CERTIFIED)
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic
import numpy as np


class StressVerificationScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        AMBER       = ManimColor("#FFB703")   # Candidate thicknesses d & allowable line
        CYAN        = ManimColor("#58C4DD")   # Stiffness k, natural period tau_n
        RED_SHOCK   = ManimColor("#FF644E")   # Stress exceedance, failure badge & gauge
        GREEN_PASS  = ManimColor("#83C167")   # Permissible stress & certified pass
        UT_BLUE     = ManimColor("#0097F1")   # Dynamic force F_dyn
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")
        BG_DARK     = ManimColor("#0B0F19")
        CARD_STROKE = ManimColor("#263346")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title & Constraint Benchmark (Strict 10-Word Rule)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Evaluating Bracket Thickness}",
            font_size=38,
            color=TEXT_WHITE
        ).move_to([0, 3.42, 0])

        allowable_header = MathTex(
            r"\sigma_{\text{allow}} = 26\text{ ksi} \quad (180\text{ MPa})",
            font_size=25,
            color=AMBER
        ).move_to([0, 2.92, 0])

        # ------------------------------------------------------------------
        # 3. Helper Functions for Cards & Badges
        # ------------------------------------------------------------------
        def make_badge(tex_str, color, width, height, font_size=22):
            rect = RoundedRectangle(
                corner_radius=0.12,
                width=width,
                height=height,
                color=color,
                stroke_width=2.0,
                fill_color=BG_DARK,
                fill_opacity=0.92
            )
            tex = MathTex(tex_str, font_size=font_size, color=color)
            tex.move_to(rect.get_center())
            return VGroup(rect, tex)

        # ------------------------------------------------------------------
        # 4. Column Geometry & Layout Setup
        # ------------------------------------------------------------------
        x_centers = [-4.35, 0.00, 4.35]
        card_w = 3.92
        card_h = 5.50
        card_y = -0.45

        # Horizontal Dashed Reference Line for sigma_allow = 26 ksi
        # Baseline = -2.05, 26 ksi = -0.75 (Delta = 1.30 -> 0.050 units/ksi)
        y_allow = -0.75
        dashed_line = DashedLine(
            start=[-6.60, y_allow, 0],
            end=[6.60, y_allow, 0],
            color=AMBER,
            stroke_width=2.4,
            dash_length=0.10
        )

        # ------------------------------------------------------------------
        # 5. TRIAL 1 (d = 0.40 in / 10.2 mm) Components
        # ------------------------------------------------------------------
        x1 = x_centers[0]
        card1_box = RoundedRectangle(
            corner_radius=0.18,
            width=card_w,
            height=card_h,
            color=CARD_STROKE,
            stroke_width=1.8,
            fill_color=BG_DARK,
            fill_opacity=0.88
        ).move_to([x1, card_y, 0])

        card1_header = make_badge(r"d = 0.40'' \quad (10.2\text{ mm})", AMBER, width=3.40, height=0.48, font_size=23)
        card1_header.move_to([x1, 1.95, 0])

        p1_row1 = MathTex(r"k = 160.0\text{ lb/in}", r"\quad", r"\tau_n = 0.0177\text{ s}", font_size=20, color=CYAN).move_to([x1, 1.45, 0])
        p1_row2 = MathTex(r"t_0/\tau_n = 5.65", r"\implies", r"\mathbf{DLF} = 1.12", font_size=20)
        p1_row2[0].set_color(TEXT_WHITE)
        p1_row2[1].set_color(TEXT_MUTED)
        p1_row2[2].set_color(RED_SHOCK)
        p1_row2.move_to([x1, 1.05, 0])
        p1_row3 = MathTex(r"F_{\text{dyn}} = 100 \cdot \text{DLF} \cdot W_{\text{eq}} = 55.1\text{ lb}", font_size=19, color=UT_BLUE).move_to([x1, 0.65, 0])
        card1_params = VGroup(p1_row1, p1_row2, p1_row3)

        # Gauge Track 1
        gauge1_track = RoundedRectangle(
            corner_radius=0.10,
            width=0.82,
            height=2.30,
            color=CARD_STROKE,
            stroke_width=1.8,
            fill_color=ManimColor("#070B12"),
            fill_opacity=0.95
        ).move_to([x1, -0.95, 0])

        tick1_0 = MathTex(r"0", font_size=16, color=TEXT_MUTED).move_to([x1 - 0.60, -2.05, 0])
        tick1_allow = MathTex(r"26", font_size=16, color=AMBER).move_to([x1 - 0.62, y_allow, 0])
        gauge1_ticks = VGroup(tick1_0, tick1_allow)

        tracker1 = ValueTracker(0.0)

        def get_bar1():
            val = tracker1.get_value()
            h = max(0.001, val * 0.050)
            col = RED_SHOCK if val > 26.0 else AMBER
            bar = RoundedRectangle(
                corner_radius=min(0.08, h / 2),
                width=0.68,
                height=h,
                stroke_width=0,
                fill_color=col,
                fill_opacity=0.92
            )
            bar.move_to([x1, -2.05 + h / 2, 0])
            return bar

        bar1_dyn = always_redraw(get_bar1)

        readout1 = DecimalNumber(
            0.0,
            num_decimal_places=1,
            unit=r"\text{ ksi}",
            font_size=20,
            color=AMBER
        )
        readout1.move_to([x1, -2.05 + 0.22, 0])
        readout1.set_opacity(0)

        def update_readout1(m):
            val = tracker1.get_value()
            m.set_value(val)
            if val < 2.0:
                m.set_opacity(0)
            else:
                m.set_opacity(1)
                col = RED_SHOCK if val > 26.0 else AMBER
                m.set_color(col)
                m.move_to([x1, -2.05 + val * 0.050 + 0.22, 0])

        readout1.add_updater(update_readout1)

        badge_verdict1 = RoundedRectangle(
            corner_radius=0.12,
            width=3.45,
            height=0.60,
            color=RED_SHOCK,
            stroke_width=2.2,
            fill_color=ManimColor("#1A070A"),
            fill_opacity=0.95
        ).move_to([x1, -2.65, 0])
        tex_verdict1 = MathTex(
            r"\sigma = 41.3\text{ ksi} > 26\text{ ksi} \quad \mathbf{FAIL}",
            font_size=21,
            color=RED_SHOCK
        ).move_to(badge_verdict1.get_center())
        verdict1_group = VGroup(badge_verdict1, tex_verdict1)

        # ------------------------------------------------------------------
        # 6. TRIAL 2 (d = 0.50 in / 12.7 mm) Components
        # ------------------------------------------------------------------
        x2 = x_centers[1]
        card2_box = RoundedRectangle(
            corner_radius=0.18,
            width=card_w,
            height=card_h,
            color=CARD_STROKE,
            stroke_width=1.8,
            fill_color=BG_DARK,
            fill_opacity=0.88
        ).move_to([x2, card_y, 0])

        card2_header = make_badge(r"d = 0.50'' \quad (12.7\text{ mm})", AMBER, width=3.40, height=0.48, font_size=23)
        card2_header.move_to([x2, 1.95, 0])

        p2_row1 = MathTex(r"k = 312.5\text{ lb/in}", r"\quad", r"\tau_n = 0.0130\text{ s}", font_size=20, color=CYAN).move_to([x2, 1.45, 0])
        p2_row2 = MathTex(r"t_0/\tau_n = 7.70", r"\implies", r"\mathbf{DLF} = 1.11", font_size=20)
        p2_row2[0].set_color(TEXT_WHITE)
        p2_row2[1].set_color(TEXT_MUTED)
        p2_row2[2].set_color(RED_SHOCK)
        p2_row2.move_to([x2, 1.05, 0])
        p2_row3 = MathTex(r"F_{\text{dyn}} = 100 \cdot \text{DLF} \cdot W_{\text{eq}} = 57.2\text{ lb}", font_size=19, color=UT_BLUE).move_to([x2, 0.65, 0])
        card2_params = VGroup(p2_row1, p2_row2, p2_row3)

        # Gauge Track 2
        gauge2_track = RoundedRectangle(
            corner_radius=0.10,
            width=0.82,
            height=2.30,
            color=CARD_STROKE,
            stroke_width=1.8,
            fill_color=ManimColor("#070B12"),
            fill_opacity=0.95
        ).move_to([x2, -0.95, 0])

        tick2_0 = MathTex(r"0", font_size=16, color=TEXT_MUTED).move_to([x2 - 0.60, -2.05, 0])
        tick2_allow = MathTex(r"26", font_size=16, color=AMBER).move_to([x2 - 0.62, y_allow, 0])
        gauge2_ticks = VGroup(tick2_0, tick2_allow)

        tracker2 = ValueTracker(0.0)

        def get_bar2():
            val = tracker2.get_value()
            h = max(0.001, val * 0.050)
            col = RED_SHOCK if val > 26.0 else AMBER
            bar = RoundedRectangle(
                corner_radius=min(0.08, h / 2),
                width=0.68,
                height=h,
                stroke_width=0,
                fill_color=col,
                fill_opacity=0.92
            )
            bar.move_to([x2, -2.05 + h / 2, 0])
            return bar

        bar2_dyn = always_redraw(get_bar2)

        readout2 = DecimalNumber(
            0.0,
            num_decimal_places=1,
            unit=r"\text{ ksi}",
            font_size=20,
            color=AMBER
        )
        readout2.move_to([x2, -2.05 + 0.22, 0])
        readout2.set_opacity(0)

        def update_readout2(m):
            val = tracker2.get_value()
            m.set_value(val)
            if val < 2.0:
                m.set_opacity(0)
            else:
                m.set_opacity(1)
                col = RED_SHOCK if val > 26.0 else AMBER
                m.set_color(col)
                m.move_to([x2, -2.05 + val * 0.050 + 0.22, 0])

        readout2.add_updater(update_readout2)

        badge_verdict2 = RoundedRectangle(
            corner_radius=0.12,
            width=3.45,
            height=0.60,
            color=RED_SHOCK,
            stroke_width=2.2,
            fill_color=ManimColor("#1A070A"),
            fill_opacity=0.95
        ).move_to([x2, -2.65, 0])
        tex_verdict2 = MathTex(
            r"\sigma = 34.3\text{ ksi} > 26\text{ ksi} \quad \mathbf{FAIL}",
            font_size=21,
            color=RED_SHOCK
        ).move_to(badge_verdict2.get_center())
        verdict2_group = VGroup(badge_verdict2, tex_verdict2)

        # ------------------------------------------------------------------
        # 7. TRIAL 3 (d = 0.60 in / 15.2 mm) Components
        # ------------------------------------------------------------------
        x3 = x_centers[2]
        card3_box = RoundedRectangle(
            corner_radius=0.18,
            width=card_w,
            height=card_h,
            color=CARD_STROKE,
            stroke_width=1.8,
            fill_color=BG_DARK,
            fill_opacity=0.88
        ).move_to([x3, card_y, 0])

        card3_header = make_badge(r"d = 0.60'' \quad (15.2\text{ mm})", AMBER, width=3.40, height=0.48, font_size=23)
        card3_header.move_to([x3, 1.95, 0])

        p3_row1 = MathTex(r"k = 540.0\text{ lb/in}", r"\quad", r"\tau_n = 0.0101\text{ s}", font_size=20, color=CYAN).move_to([x3, 1.45, 0])
        p3_row2 = MathTex(r"t_0/\tau_n = 9.91", r"\implies", r"\mathbf{DLF} = 1.07", font_size=20)
        p3_row2[0].set_color(TEXT_WHITE)
        p3_row2[1].set_color(TEXT_MUTED)
        p3_row2[2].set_color(GREEN_PASS)
        p3_row2.move_to([x3, 1.05, 0])
        p3_row3 = MathTex(r"F_{\text{dyn}} = 100 \cdot \text{DLF} \cdot W_{\text{eq}} = 57.6\text{ lb}", font_size=19, color=UT_BLUE).move_to([x3, 0.65, 0])
        card3_params = VGroup(p3_row1, p3_row2, p3_row3)

        # Gauge Track 3
        gauge3_track = RoundedRectangle(
            corner_radius=0.10,
            width=0.82,
            height=2.30,
            color=CARD_STROKE,
            stroke_width=1.8,
            fill_color=ManimColor("#070B12"),
            fill_opacity=0.95
        ).move_to([x3, -0.95, 0])

        tick3_0 = MathTex(r"0", font_size=16, color=TEXT_MUTED).move_to([x3 - 0.60, -2.05, 0])
        tick3_allow = MathTex(r"26", font_size=16, color=AMBER).move_to([x3 - 0.62, y_allow, 0])
        gauge3_ticks = VGroup(tick3_0, tick3_allow)

        tracker3 = ValueTracker(0.0)

        def get_bar3():
            val = tracker3.get_value()
            h = max(0.001, val * 0.050)
            col = GREEN_PASS if val >= 25.0 else AMBER
            bar = RoundedRectangle(
                corner_radius=min(0.08, h / 2),
                width=0.68,
                height=h,
                stroke_width=0,
                fill_color=col,
                fill_opacity=0.92
            )
            bar.move_to([x3, -2.05 + h / 2, 0])
            return bar

        bar3_dyn = always_redraw(get_bar3)

        readout3 = DecimalNumber(
            0.0,
            num_decimal_places=1,
            unit=r"\text{ ksi}",
            font_size=20,
            color=AMBER
        )
        readout3.move_to([x3, -2.05 + 0.22, 0])
        readout3.set_opacity(0)

        def update_readout3(m):
            val = tracker3.get_value()
            m.set_value(val)
            if val < 2.0:
                m.set_opacity(0)
            else:
                m.set_opacity(1)
                col = GREEN_PASS if val >= 25.0 else AMBER
                m.set_color(col)
                m.move_to([x3, -2.05 + val * 0.050 + 0.22, 0])

        readout3.add_updater(update_readout3)

        badge_verdict3 = RoundedRectangle(
            corner_radius=0.12,
            width=3.45,
            height=0.60,
            color=GREEN_PASS,
            stroke_width=2.4,
            fill_color=ManimColor("#06170E"),
            fill_opacity=0.95
        ).move_to([x3, -2.65, 0])
        tex_verdict3 = MathTex(
            r"\sigma = 25.7\text{ ksi} \le 26\text{ ksi} \quad \mathbf{CERTIFIED}",
            font_size=19,
            color=GREEN_PASS
        ).move_to(badge_verdict3.get_center())
        verdict3_group = VGroup(badge_verdict3, tex_verdict3)

        # Certification Golden Halo
        cert_halo = RoundedRectangle(
            corner_radius=0.22,
            width=card_w + 0.16,
            height=card_h + 0.16,
            stroke_width=4.0,
            color=GREEN_PASS
        ).move_to(card3_box.get_center())

        # ==================================================================
        # CHOREOGRAPHY & FRAME-ACCURATE CUEPOINT SYNCHRONIZATION
        # ==================================================================

        # --- STEP 1: Problem Baseline & Trial 1 (0.0s to 3.5s) ---
        # 0.0s - 0.7s: Title, Allowable Constraint, and Dashed Baseline
        self.play(
            FadeIn(title, shift=DOWN * 0.15),
            FadeIn(allowable_header, shift=DOWN * 0.10),
            Create(dashed_line),
            run_time=0.7
        )

        # 0.7s - 1.5s: Trial 1 Card & Parameters Bloom In
        self.play(
            FadeIn(card1_box, scale=0.96),
            FadeIn(card1_header),
            FadeIn(card1_params, shift=DOWN * 0.10),
            FadeIn(gauge1_track),
            FadeIn(gauge1_ticks),
            run_time=0.8
        )
        self.add(bar1_dyn, readout1)

        # 1.5s - 2.5s: Dynamic Stress Gauge Shoots Up to 41.3 ksi (Breaches line!)
        self.play(
            tracker1.animate.set_value(41.328),
            run_time=1.0,
            rate_func=ease_out_cubic
        )

        # 2.5s - 3.0s: Red FAIL Verdict Badge Pops In
        self.play(
            FadeIn(verdict1_group, scale=1.05),
            card1_box.animate.set_stroke(color=RED_SHOCK, width=2.4),
            run_time=0.5
        )

        # 3.0s - 3.5s: Hold for Cuepoint 1
        self.wait(0.5)  # Exact Cuepoint 1 = 3.5s

        # --- STEP 2: Trial 2 Evaluation (3.5s to 8.0s) ---
        # 3.5s - 4.5s: Trial 2 Card & Parameters Bloom In
        self.play(
            FadeIn(card2_box, scale=0.96),
            FadeIn(card2_header),
            FadeIn(card2_params, shift=DOWN * 0.10),
            FadeIn(gauge2_track),
            FadeIn(gauge2_ticks),
            run_time=1.0
        )
        self.add(bar2_dyn, readout2)

        # 4.5s - 5.6s: Gauge 2 Shoots Up to 34.3 ksi (Exceeds line by 32%)
        self.play(
            tracker2.animate.set_value(34.315),
            run_time=1.1,
            rate_func=ease_out_cubic
        )

        # 5.6s - 6.2s: Red FAIL Verdict Badge Pops In
        self.play(
            FadeIn(verdict2_group, scale=1.05),
            card2_box.animate.set_stroke(color=RED_SHOCK, width=2.4),
            run_time=0.6
        )

        # 6.2s - 8.0s: Hold for Cuepoint 2
        self.wait(1.8)  # Exact Cuepoint 2 = 8.0s

        # --- STEP 3: Trial 3 Certification (8.0s to 14.2s) ---
        # 8.0s - 9.1s: Trial 3 Card & Parameters Bloom In
        self.play(
            FadeIn(card3_box, scale=0.96),
            FadeIn(card3_header),
            FadeIn(card3_params, shift=DOWN * 0.10),
            FadeIn(gauge3_track),
            FadeIn(gauge3_ticks),
            run_time=1.1
        )
        self.add(bar3_dyn, readout3)

        # 9.1s - 10.5s: Gauge 3 Climbs Smoothly to 25.7 ksi and Halts Right Below Threshold!
        self.play(
            tracker3.animate.set_value(25.664),
            run_time=1.4,
            rate_func=ease_out_cubic
        )

        # 10.5s - 11.3s: Green CERTIFIED Badge Pops In
        self.play(
            FadeIn(verdict3_group, scale=1.08),
            card3_box.animate.set_stroke(color=GREEN_PASS, width=2.8),
            run_time=0.8
        )

        # 11.3s - 12.5s: Golden / Green Halo Envelops Certified Trial 3
        self.play(
            Create(cert_halo),
            cert_halo.animate.set_stroke(color=AMBER, width=4.5),
            run_time=1.2
        )

        # 12.5s - 14.2s: Hold for Cuepoint 3
        self.wait(1.7)  # Exact Cuepoint 3 = 14.2s

        # --- Settling buffer (14.2s to 15.0s) ---
        self.wait(0.8)  # Video concludes at 15.0s

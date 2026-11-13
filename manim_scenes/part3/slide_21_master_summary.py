"""
SLIDE-21: MasterSummaryScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 3 (Design Resolution & Applications)
Allocated Time: 60 s

3Blue1Brown Fullscreen Aesthetic (Enlarged High-Legibility Edition — Zero Collision):
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero horizontal dividing bars
  - Floating minimal 3-word title: "Master Technical Synthesis" (Enlarged 44pt)
  - Expanded Symmetrical Cards (width = 4.35, height = 4.65) for maximum screen coverage (>90%)
  - Significantly enlarged mathematical typography (21 - 24 pt formulas, 34 pt Q&A badge)
  - Discrete step-by-step sequential revelation controlled via laptop clicks:
      Step 1 (0.0s - 3.0s): Case 1: Helicopter Drop-Box (d = 0.60'' certified safe)
      Step 2 (3.0s - 6.0s): Case 2: Overhead Crane Derailment (k < 365 kN/m no derailment)
      Step 3 (6.0s - 9.0s): Case 3: Automotive ECU Base Isolator (Td <= 10% 90% attenuation)
      Step 4 (9.0s - 12.5s): Triad Certification Glow, University of Tehran & Open for Questions
"""

from manim import *
from manim.utils.rate_functions import ease_out_cubic, ease_in_out_sine, there_and_back
import numpy as np


class MasterSummaryScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        AMBER       = ManimColor("#FFB703")   # Case 1 (Helicopter plate & sizing)
        CYAN        = ManimColor("#58C4DD")   # Case 2 (Crane girder stiffness limit)
        UT_BLUE     = ManimColor("#0097F1")   # Case 3 (ECU isolator & UT brand accent)
        GREEN_PASS  = ManimColor("#83C167")   # Certified safe badges & checkmarks
        TEXT_WHITE  = ManimColor("#FFFFFF")   # Primary equations
        SLATE       = ManimColor("#B0B8C4")   # Secondary annotations / outlines
        BG_DARK     = ManimColor("#0B0F19")   # Symmetrical card background fill
        CARD_STROKE = ManimColor("#1E293B")   # Muted placeholder card border
        PASS_BG     = ManimColor("#06170E")   # Certified badge background fill

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 3 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Master Technical Synthesis}",
            font_size=44,
            color=TEXT_WHITE
        ).move_to([0, 3.45, 0])

        # Helper function for sleek rounded badges with zero text overflow
        def make_badge(tex_str, color, width, height, font_size=23, fill_color=BG_DARK, stroke_width=2.2):
            rect = RoundedRectangle(
                corner_radius=0.15,
                width=width,
                height=height,
                color=color,
                stroke_width=stroke_width,
                fill_color=fill_color,
                fill_opacity=0.94
            )
            tex = MathTex(tex_str, font_size=font_size, color=color)
            tex.move_to(rect.get_center())
            return VGroup(rect, tex)

        # ------------------------------------------------------------------
        # 3. Expanded Base Layout Geometry: 3 Spacious Symmetrical Columns
        # ------------------------------------------------------------------
        x_centers = [-4.55, 0.00, 4.55]
        card_w = 4.35
        card_h = 4.65
        card_y = -0.10

        # Background Cards: Card 1 starts in Amber, Cards 2 & 3 start muted
        card_l = RoundedRectangle(
            corner_radius=0.20, width=card_w, height=card_h,
            color=AMBER, stroke_width=2.6, fill_color=BG_DARK, fill_opacity=0.94
        ).move_to([x_centers[0], card_y, 0])

        card_c = RoundedRectangle(
            corner_radius=0.20, width=card_w, height=card_h,
            color=CARD_STROKE, stroke_width=1.8, fill_color=BG_DARK, fill_opacity=0.90
        ).move_to([x_centers[1], card_y, 0])

        card_r = RoundedRectangle(
            corner_radius=0.20, width=card_w, height=card_h,
            color=CARD_STROKE, stroke_width=1.8, fill_color=BG_DARK, fill_opacity=0.90
        ).move_to([x_centers[2], card_y, 0])

        # ------------------------------------------------------------------
        # CASE 1: HELICOPTER CANTILEVER PLATE (0.0s - 3.0s)
        # ------------------------------------------------------------------
        x1 = x_centers[0]
        c1_header = make_badge(r"\mathbf{Case\ 1:\ Cantilever\ Plate}", AMBER, width=3.95, height=0.54, font_size=23)
        c1_header.move_to([x1, 1.82, 0])

        c1_row1 = MathTex(r"d = 0.60'' \quad (15.2\text{ mm})", font_size=24, color=AMBER).move_to([x1, 1.25, 0])
        c1_row2 = MathTex(r"k = 540\text{ lb/in}, \quad \tau_n = 0.0101\text{ s}", font_size=22, color=CYAN).move_to([x1, 0.72, 0])
        c1_row3 = MathTex(r"t_0/\tau_n = 9.91 \implies \mathbf{DLF} = 1.07", font_size=23, color=TEXT_WHITE).move_to([x1, 0.18, 0])
        c1_row4 = MathTex(r"\sigma_{\max} = 25,664\text{ psi} \le 26\text{ ksi}", font_size=22, color=GREEN_PASS).move_to([x1, -0.36, 0])
        c1_badge = make_badge(r"\checkmark\ \mathbf{CERTIFIED\ SAFE}", GREEN_PASS, width=3.95, height=0.56, font_size=23, fill_color=PASS_BG, stroke_width=2.6)
        c1_badge.move_to([x1, -1.02, 0])
        c1_subbadge = MathTex(r"\text{MIL-STD-810H Compliant}", font_size=19, color=SLATE).move_to([x1, -1.62, 0])

        case1_content = VGroup(c1_header, c1_row1, c1_row2, c1_row3, c1_row4, c1_badge, c1_subbadge)

        # ------------------------------------------------------------------
        # CASE 2: OVERHEAD CRANE SEISMIC DERAILMENT (3.0s - 6.0s)
        # ------------------------------------------------------------------
        x2 = x_centers[1]
        c2_header = make_badge(r"\mathbf{Case\ 2:\ Crane\ Derailment}", CYAN, width=3.95, height=0.54, font_size=23)
        c2_header.move_to([x2, 1.82, 0])

        c2_row1 = MathTex(r"\tau_n > 0.52\text{ s} \implies k < 365\text{ kN/m}", font_size=23, color=CYAN).move_to([x2, 1.25, 0])
        c2_row2 = MathTex(r"S_a = 0.25g < 1.0g \quad (\zeta = 0.02)", font_size=22, color=AMBER).move_to([x2, 0.72, 0])
        c2_row3 = MathTex(r"N(t) = m(g - \ddot{x}) > 0", font_size=24, color=TEXT_WHITE).move_to([x2, 0.18, 0])
        c2_row4 = MathTex(r"N_{\min} = 0.75\,mg > 0 \quad (\text{Safe})", font_size=21, color=GREEN_PASS).move_to([x2, -0.36, 0])
        c2_badge = make_badge(r"\checkmark\ \mathbf{NO\ DERAILMENT}", GREEN_PASS, width=3.95, height=0.56, font_size=23, fill_color=PASS_BG, stroke_width=2.6)
        c2_badge.move_to([x2, -1.02, 0])
        c2_subbadge = MathTex(r"\text{Compliant Girder Survives}", font_size=19, color=SLATE).move_to([x2, -1.62, 0])

        case2_content = VGroup(c2_header, c2_row1, c2_row2, c2_row3, c2_row4, c2_badge, c2_subbadge)

        # ------------------------------------------------------------------
        # CASE 3: AUTOMOTIVE ECU BASE ISOLATOR (6.0s - 9.0s)
        # ------------------------------------------------------------------
        x3 = x_centers[2]
        c3_header = make_badge(r"\mathbf{Case\ 3:\ ECU\ Isolator}", UT_BLUE, width=3.95, height=0.54, font_size=23)
        c3_header.move_to([x3, 1.82, 0])

        c3_row1 = MathTex(r"r \ge \sqrt{11} = 3.32 \implies \omega_{n,\text{iso}} = 15.1\text{ Hz}", font_size=21, color=UT_BLUE).move_to([x3, 1.25, 0])
        c3_row2 = MathTex(r"k_{\text{iso}} = 24.66\text{ kN/m} \quad (4 \times 6.17)", font_size=22, color=CYAN).move_to([x3, 0.72, 0])
        c3_row3 = MathTex(r"c_{\text{iso}} = 5.21\text{ N}\cdot\text{s/m} \quad (\zeta = 0.01)", font_size=22, color=AMBER).move_to([x3, 0.18, 0])
        c3_row4 = MathTex(r"T_d \le 10\% \implies -90\%\ \text{Vibration}", font_size=22, color=GREEN_PASS).move_to([x3, -0.36, 0])
        c3_badge = make_badge(r"\checkmark\ \mathbf{90\%\ ATTENUATION}", GREEN_PASS, width=3.95, height=0.56, font_size=23, fill_color=PASS_BG, stroke_width=2.6)
        c3_badge.move_to([x3, -1.02, 0])
        c3_subbadge = MathTex(r"\text{Solder Fatigue Eliminated}", font_size=19, color=SLATE).move_to([x3, -1.62, 0])

        case3_content = VGroup(c3_header, c3_row1, c3_row2, c3_row3, c3_row4, c3_badge, c3_subbadge)

        # ------------------------------------------------------------------
        # STEP 4: ACADEMIC BRANDING & OPEN FOR QUESTIONS (9.0s - 12.5s)
        # ------------------------------------------------------------------
        ut_header = MathTex(
            r"\text{University of Tehran} \quad \bullet \quad \text{Mechanical Vibrations}",
            font_size=24,
            color=UT_BLUE
        ).move_to([0, -3.45, 0])

        qa_rect = RoundedRectangle(
            corner_radius=0.18,
            width=6.80,
            height=0.70,
            color=UT_BLUE,
            stroke_width=2.8,
            fill_color=ManimColor("#07121E"),
            fill_opacity=0.98
        ).move_to([0, -2.55, 0])

        qa_tex = Tex(
            r"\textbf{Open for Questions}",
            font_size=33,
            color=TEXT_WHITE
        ).move_to(qa_rect.get_center())

        qa_badge = VGroup(qa_rect, qa_tex)

        qa_halo = RoundedRectangle(
            corner_radius=0.22,
            width=7.00,
            height=0.86,
            color=GREEN_PASS,
            stroke_width=2.0,
            fill_opacity=0.0
        ).move_to([0, -2.55, 0])

        # Luminous particle field on outer flanks to protect center text corridor
        np.random.seed(42)
        particles = VGroup()
        for _ in range(28):
            if np.random.rand() > 0.5:
                px = np.random.uniform(-6.8, -3.8)
            else:
                px = np.random.uniform(3.8, 6.8)
            py = np.random.uniform(-3.8, -2.0)
            rad = np.random.uniform(0.025, 0.048)
            col = np.random.choice([AMBER, CYAN, GREEN_PASS, UT_BLUE])
            opac = np.random.uniform(0.35, 0.75)
            dot = Dot(point=[px, py, 0], radius=rad, color=col).set_opacity(opac)
            particles.add(dot)

        # ==================================================================
        # ANIMATION CHOREOGRAPHY & FRAME-ACCURATE TIMESTAMPS
        # ==================================================================

        # --- STEP 1: Case 1 (Helicopter Cantilever Plate) (0.0s to 3.0s) ---
        # 0.0s - 0.7s: Title reveals smoothly
        self.play(
            Write(title),
            run_time=0.7
        )

        # 0.7s - 1.2s: Symmetrical card boxes appear
        self.play(
            FadeIn(card_l, shift=UP * 0.15),
            FadeIn(card_c, shift=UP * 0.15),
            FadeIn(card_r, shift=UP * 0.15),
            run_time=0.5
        )

        # 1.2s - 2.6s: Case 1 content reveals in Left Card
        self.play(
            FadeIn(case1_content, lag_ratio=0.08),
            run_time=1.4
        )

        # 2.6s - 3.0s: Hold for Cuepoint 1
        self.wait(0.4)  # Exact Cuepoint 1 = 3.0s

        # --- STEP 2: Case 2 (Overhead Crane Derailment) (3.0s to 6.0s) ---
        # 3.0s - 3.5s: Center Card illuminates in Cyan
        self.play(
            card_c.animate.set_stroke(color=CYAN, width=2.6),
            run_time=0.5
        )

        # 3.5s - 4.9s: Case 2 content reveals in Center Card
        self.play(
            FadeIn(case2_content, lag_ratio=0.08),
            run_time=1.4
        )

        # 4.9s - 5.6s: Certified badge soft pulse
        self.play(
            c2_badge.animate.scale(1.05),
            rate_func=there_and_back,
            run_time=0.7
        )

        # 5.6s - 6.0s: Hold for Cuepoint 2
        self.wait(0.4)  # Exact Cuepoint 2 = 6.0s

        # --- STEP 3: Case 3 (Automotive ECU Base Isolator) (6.0s to 9.0s) ---
        # 6.0s - 6.5s: Right Card illuminates in UT Blue
        self.play(
            card_r.animate.set_stroke(color=UT_BLUE, width=2.6),
            run_time=0.5
        )

        # 6.5s - 7.9s: Case 3 content reveals in Right Card
        self.play(
            FadeIn(case3_content, lag_ratio=0.08),
            run_time=1.4
        )

        # 7.9s - 8.6s: Certified badge soft pulse
        self.play(
            c3_badge.animate.scale(1.05),
            rate_func=there_and_back,
            run_time=0.7
        )

        # 8.6s - 9.0s: Hold for Cuepoint 3
        self.wait(0.4)  # Exact Cuepoint 3 = 9.0s

        # --- STEP 4: Triad Certification & Open for Questions (9.0s to 12.5s) ---
        # 9.0s - 10.4s: Cards and contents shift up gracefully together as triad illuminates in Pass Green
        self.play(
            card_l.animate.shift(UP * 0.65).set_stroke(color=GREEN_PASS, width=2.8),
            card_c.animate.shift(UP * 0.65).set_stroke(color=GREEN_PASS, width=2.8),
            card_r.animate.shift(UP * 0.65).set_stroke(color=GREEN_PASS, width=2.8),
            case1_content.animate.shift(UP * 0.65),
            case2_content.animate.shift(UP * 0.65),
            case3_content.animate.shift(UP * 0.65),
            FadeIn(ut_header, shift=UP * 0.25),
            FadeIn(qa_badge, shift=UP * 0.25),
            FadeIn(qa_halo, scale=1.05),
            run_time=1.4
        )

        # 10.4s - 11.6s: Luminous particle accent field illuminates gently on flanks
        self.play(
            FadeIn(particles, lag_ratio=0.04),
            qa_halo.animate.set_stroke(color=UT_BLUE, width=2.8),
            run_time=1.2
        )

        # 11.6s - 12.5s: Delicate breathing pulse on Q&A halo
        self.play(
            qa_rect.animate.set_stroke(color=GREEN_PASS, width=3.0),
            particles.animate.set_opacity(0.85),
            rate_func=there_and_back,
            run_time=0.9
        )
        # Exact Cuepoint 4 = 12.5s reached here

        # 12.5s - 13.5s: Clean loop hold & settling buffer
        self.wait(1.0)

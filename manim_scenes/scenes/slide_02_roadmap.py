"""
SLIDE-02: RoadmapOverviewScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Intuition & Foundations)

Dedicated Slide 2: Minimalist 3-speaker curricular overview centered vertically & horizontally.
"""

from manim import *
import numpy as np


class RoadmapOverviewScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black & UT Blue)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # University of Tehran Primary Accent
        PART2_PURP  = ManimColor("#818CF8")   # Spectral Violet for Person 2
        PART3_TEAL  = ManimColor("#2DD4BF")   # Engineering Teal for Person 3
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_OFFWH  = ManimColor("#ECEFF4")
        TEXT_MUTED  = ManimColor("#94A3B8")
        CARD_BG     = ManimColor("#080D1A")
        BORDER_DIM  = ManimColor("#1E293B")
        BORDER_MID  = ManimColor("#334155")

        # ------------------------------------------------------------------
        # 2. Header & Title
        # ------------------------------------------------------------------
        header_tag = Tex(
            r"\textsc{Presentation Architecture}",
            font_size=20,
            color=TEHRAN_BLUE
        ).move_to([0, 3.25, 0])

        main_title = Tex(
            r"\textbf{Three-Act Curricular Roadmap}",
            font_size=38,
            color=TEXT_WHITE
        ).next_to(header_tag, DOWN, buff=0.14)

        header_rule = Line(
            start=LEFT * 4.5,
            end=RIGHT * 4.5,
            color=TEHRAN_BLUE,
            stroke_width=1.5
        ).next_to(main_title, DOWN, buff=0.20)

        header_group = VGroup(header_tag, main_title, header_rule)

        # ------------------------------------------------------------------
        # 3. Centered 3-Speaker Progression Cards
        # ------------------------------------------------------------------
        card_y = -0.45
        card_w = 4.0
        card_h = 2.6

        def make_roadmap_card(part_num, person_num, title_lines, color, is_active=False):
            stroke_w = 2.4 if is_active else 1.2
            border_c = color if is_active else BORDER_DIM

            box = RoundedRectangle(
                width=card_w,
                height=card_h,
                corner_radius=0.18,
                stroke_color=border_c,
                stroke_width=stroke_w,
                fill_color=CARD_BG,
                fill_opacity=0.94
            )

            # Top Badge Pill
            badge_str = rf"\textbf{{PART {part_num}}} \quad $\bullet$ \quad \textsc{{Person {person_num}}}"
            badge = Tex(badge_str, font_size=17, color=color).move_to(box.get_top() + DOWN * 0.42)

            # Divider line inside card
            card_line = Line(
                start=box.get_left() + RIGHT * 0.4,
                end=box.get_right() + LEFT * 0.4,
                color=BORDER_DIM,
                stroke_width=1.0
            ).next_to(badge, DOWN, buff=0.22)

            # Clean 2-4 word focus title
            title = Tex(
                rf"\textbf{{{title_lines}}}",
                font_size=22,
                color=TEXT_WHITE
            ).next_to(card_line, DOWN, buff=0.35)

            elements = [box, badge, card_line, title]

            if is_active:
                pulse_dot = Dot(color=color, radius=0.06).next_to(badge, LEFT, buff=0.2)
                elements.append(pulse_dot)

            return VGroup(*elements)

        card1 = make_roadmap_card(
            1, 1,
            r"Physical Intuition \\ \& SDOF Modeling",
            TEHRAN_BLUE,
            is_active=True
        ).move_to([-4.4, card_y, 0])

        card2 = make_roadmap_card(
            2, 2,
            r"Mathematical Rigor \\ \& SRS Theory",
            PART2_PURP,
            is_active=False
        ).move_to([0.0, card_y, 0])

        card3 = make_roadmap_card(
            3, 3,
            r"Case Studies \\ \& Isolator Sizing",
            PART3_TEAL,
            is_active=False
        ).move_to([4.4, card_y, 0])

        # Connecting Chevron Arrows
        chev1 = Arrow(
            start=[-2.25, card_y, 0],
            end=[-2.05, card_y, 0],
            color=BORDER_MID,
            stroke_width=3,
            tip_length=0.15
        )
        chev2 = Arrow(
            start=[2.05, card_y, 0],
            end=[2.25, card_y, 0],
            color=BORDER_MID,
            stroke_width=3,
            tip_length=0.15
        )

        cards_group = VGroup(card1, card2, card3, chev1, chev2)

        # ------------------------------------------------------------------
        # 4. Animation Choreography
        # ------------------------------------------------------------------
        self.play(
            FadeIn(header_tag, shift=DOWN * 0.2),
            Write(main_title),
            GrowFromCenter(header_rule),
            run_time=1.4
        )
        self.wait(0.2)

        self.play(
            LaggedStart(
                FadeIn(card1, shift=UP * 0.4),
                GrowArrow(chev1),
                FadeIn(card2, shift=UP * 0.4),
                GrowArrow(chev2),
                FadeIn(card3, shift=UP * 0.4),
                lag_ratio=0.22
            ),
            run_time=1.8
        )

        # Subtle emphasis pulse on Card 1 (Person 1 active speaker)
        card1_box = card1[0]
        self.play(
            card1_box.animate.set_stroke(color=TEHRAN_BLUE, width=3.6),
            run_time=0.55
        )
        self.play(
            card1_box.animate.set_stroke(color=TEHRAN_BLUE, width=2.4),
            run_time=0.55
        )

        # Resting hold frame for Person 1 roadmap overview remarks
        self.wait(2.5)

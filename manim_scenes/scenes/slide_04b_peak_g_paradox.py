"""
SLIDE-04B: PeakGParadoxScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 1 (Physical Foundations & Modeling)

3Blue1Brown Full-Screen Dramatic Focus:
  - 90% open dark canvas.
  - Step 0 (0.0s - 2.0s): Paradox question in large, centered typography.
      5000g Pyroshock   --> Harmless
      50g Drop Impact   --> Structural Failure
  - Step 1 (2.0s - 6.0s): Paradox shifts upward + Dimmed; Reason revealed:
      Peak g ignores pulse duration (Delta t vs. tau_n)
  - Step 2 (6.0s - 10.5s): Clean transition to centerpiece equation at screen center:
      S_a(omega_n, zeta) = max_t |x''(t)|
      Label: Shock Response Spectrum
"""

from manim import *


class PeakGParadoxScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & Color Palette Invariants (Pure Black Canvas)
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        TEHRAN_BLUE = ManimColor("#0097F1")   # Accent / SRS Tag
        SPRING_CYAN = ManimColor("#58C4DD")   # Drop Impact
        DANGER_RED  = ManimColor("#FF644E")   # Pyroshock / Failure
        FORCE_GOLD  = ManimColor("#F7CA3B")   # Core Insight & SRS Equation
        TEXT_WHITE  = ManimColor("#FFFFFF")
        TEXT_MUTED  = ManimColor("#94A3B8")

        # ------------------------------------------------------------------
        # 2. Stage Elements: Paradox Statements
        # ------------------------------------------------------------------
        line_pyro = MathTex(
            r"5{,}000g \ \text{Pyroshock}",
            r"\ \longrightarrow \ ",
            r"\text{Harmless}",
            font_size=42
        )
        line_pyro[0].set_color(DANGER_RED)
        line_pyro[1].set_color(TEXT_MUTED)
        line_pyro[2].set_color(TEXT_MUTED)

        line_drop = MathTex(
            r"50g \ \text{Drop Impact}",
            r"\ \longrightarrow \ ",
            r"\textbf{Structural Failure}",
            font_size=42
        )
        line_drop[0].set_color(SPRING_CYAN)
        line_drop[1].set_color(TEXT_WHITE)
        line_drop[2].set_color(DANGER_RED)

        paradox_grp = VGroup(line_pyro, line_drop).arrange(DOWN, buff=0.45).move_to([0, 0.0, 0])

        # ------------------------------------------------------------------
        # 3. Stage Elements: Physical Reason (Pulse Duration Neglect)
        # ------------------------------------------------------------------
        reason_math = MathTex(
            r"\text{Peak } g \text{ ignores pulse duration } (\Delta t \text{ vs. } \tau_n)",
            font_size=38,
            color=FORCE_GOLD
        ).move_to([0, -0.90, 0])

        # ------------------------------------------------------------------
        # 4. Stage Elements: The Centerpiece SRS Mandate
        # ------------------------------------------------------------------
        srs_equation = MathTex(
            r"S_a(\omega_n, \zeta) = \max_t |\ddot{x}(t)|",
            font_size=58,
            color=FORCE_GOLD
        ).move_to([0, 0.35, 0])

        srs_label = Tex(
            r"\textbf{\textsc{Shock Response Spectrum}}",
            font_size=30,
            color=TEHRAN_BLUE
        ).next_to(srs_equation, DOWN, buff=0.45)

        centerpiece_grp = VGroup(srs_equation, srs_label)

        # ------------------------------------------------------------------
        # 5. Step-Controlled Timeline & Cuepoint Choreography
        # ------------------------------------------------------------------
        # --- Step 0: The Paradox (0.0s - 2.0s -> Cuepoint 0 = 2.0s) ---
        self.play(
            FadeIn(line_pyro, shift=DOWN * 0.15),
            FadeIn(line_drop, shift=UP * 0.15),
            run_time=1.2
        )
        self.wait(0.8)  # Rest hold at t = 2.0s

        # --- Step 1: Why Peak-g Fails (2.0s - 6.0s -> Cuepoint 1 = 6.0s) ---
        self.play(
            paradox_grp.animate.shift(UP * 1.35).scale(0.90).set_opacity(0.68),
            FadeIn(reason_math, shift=UP * 0.20),
            run_time=1.2
        )
        self.wait(2.8)  # Rest hold at t = 6.0s

        # --- Step 2: Centerpiece SRS Mandate (6.0s - 10.5s -> Cuepoint 2 = 10.5s) ---
        self.play(
            FadeOut(paradox_grp, shift=UP * 0.25),
            FadeOut(reason_math, shift=DOWN * 0.25),
            run_time=0.7
        )
        self.play(
            Write(srs_equation),
            FadeIn(srs_label, shift=UP * 0.15),
            run_time=1.0
        )
        self.wait(2.8)  # Rest hold at t = 10.5s

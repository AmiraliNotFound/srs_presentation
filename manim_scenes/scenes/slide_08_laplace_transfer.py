"""
SLIDE-08: LaplaceTransferScene
Presentation: Shock Response Spectrum (SRS)
Academic Context: Mechanical Vibrations (Semester 5) — University of Tehran
Speaker: Person 2 (Mathematical Foundations & Derivations)
Allocated Time: 15:00 – 17:00 (120 s)

Strict 3Blue1Brown Fullscreen Aesthetic:
  - 100% borderless, pure dark canvas (#000000)
  - Zero header banners, zero dividing bars, zero bulky cards
  - Under 10 English words total on canvas (Strict 10-Word Rule: Exactly 4 English words total)
      "Laplace Formulation" (2 words)
      "Dynamic Impedance" (2 words)
  - Step 0 (0.0s - 3.0s): Minimal title & Time-domain SDOF ODE (m x'' + c x' + k x = F(t))
  - Step 1 (3.0s - 7.5s): Smooth Laplace glide morph -> (m s^2 + c s + k) X(s) = F(s)
                           -> Canonical damping form m(s^2 + 2*zeta*omega_n*s + omega_n^2) X(s) = F(s)
  - Step 2 (7.5s - 14.0s): Transfer function H(s) = X(s)/F(s) = 1 / [m(s^2 + 2*zeta*omega_n*s + omega_n^2)]
                           & Generalized dynamic impedance Z(s) = 1/H(s)
"""

from manim import *


class LaplaceTransferScene(Scene):
    def construct(self):
        # ------------------------------------------------------------------
        # 1. Canvas & 3Blue1Brown Color Palette Invariants
        # ------------------------------------------------------------------
        self.camera.background_color = ManimColor("#000000")

        CORAL      = ManimColor("#FF644E")   # Inertia / m x'' / m s^2 / s^2
        GREEN      = ManimColor("#83C167")   # Damping / c x' / c s / 2 zeta omega_n s
        CYAN       = ManimColor("#58C4DD")   # Spring / Restoring / k x / k / omega_n^2
        YELLOW     = ManimColor("#F7CA3B")   # Excitation Force / F(t) / F(s) & Impedance Z(s)
        BLUE       = ManimColor("#0097F1")   # Output / Transfer Function H(s) / X(s) (UT Blue)
        TEXT_WHITE = ManimColor("#FFFFFF")
        TEXT_MUTED = ManimColor("#94A3B8")

        # ------------------------------------------------------------------
        # 2. Minimalist Floating Title (Strict 10-Word Rule: Exactly 2 words)
        # ------------------------------------------------------------------
        title = Tex(
            r"\textbf{Laplace Formulation}",
            font_size=48,
            color=TEXT_WHITE
        ).move_to([0, 3.35, 0])

        # ------------------------------------------------------------------
        # 3. Mathematical Equations Configuration (65" TV Large Typography)
        # ------------------------------------------------------------------
        iso_base = [r"m", r"\ddot{x}", r"c", r"\dot{x}", r"k", r"x", r"F(t)", r"s^2", r"s", r"X(s)", r"F(s)", r"="]

        # Step 0: Time-domain SDOF Differential Equation
        eq0 = MathTex(
            r"m \ddot{x} + c \dot{x} + k x = F(t)",
            substrings_to_isolate=iso_base,
            font_size=52
        ).move_to([0, 0.60, 0])
        eq0.set_color_by_tex(r"m", CORAL)
        eq0.set_color_by_tex(r"\ddot{x}", CORAL)
        eq0.set_color_by_tex(r"c", GREEN)
        eq0.set_color_by_tex(r"\dot{x}", GREEN)
        eq0.set_color_by_tex(r"k", CYAN)
        eq0.set_color_by_tex(r"x", CYAN)
        eq0.set_color_by_tex(r"F(t)", YELLOW)

        # Step 1a: Laplace-Domain Algebraic Polynomial
        eq1 = MathTex(
            r"(m s^2 + c s + k) X(s) = F(s)",
            substrings_to_isolate=iso_base,
            font_size=52
        ).move_to([0, 0.60, 0])
        eq1.set_color_by_tex(r"m", CORAL)
        eq1.set_color_by_tex(r"s^2", CORAL)
        eq1.set_color_by_tex(r"c", GREEN)
        eq1.set_color_by_tex(r"s", GREEN)
        eq1.set_color_by_tex(r"k", CYAN)
        eq1.set_color_by_tex(r"X(s)", BLUE)
        eq1.set_color_by_tex(r"F(s)", YELLOW)

        # Step 1b: Canonical Factored Damping Form
        iso_factored = [r"m", r"s^2", r"2\zeta\omega_n s", r"\omega_n^2", r"X(s)", r"F(s)", r"="]
        eq2 = MathTex(
            r"m (s^2 + 2\zeta\omega_n s + \omega_n^2) X(s) = F(s)",
            substrings_to_isolate=iso_factored,
            font_size=52
        ).move_to([0, 0.60, 0])
        eq2.set_color_by_tex(r"m", CORAL)
        eq2.set_color_by_tex(r"s^2", CORAL)
        eq2.set_color_by_tex(r"2\zeta\omega_n s", GREEN)
        eq2.set_color_by_tex(r"\omega_n^2", CYAN)
        eq2.set_color_by_tex(r"X(s)", BLUE)
        eq2.set_color_by_tex(r"F(s)", YELLOW)

        # Step 2a: System Transfer Function H(s)
        eq3 = MathTex(
            r"H(s) = \frac{X(s)}{F(s)} = \frac{1}{m(s^2 + 2\zeta\omega_n s + \omega_n^2)}",
            font_size=50
        ).move_to([0, 1.10, 0])
        eq3.set_color_by_tex(r"H(s)", BLUE)
        eq3.set_color_by_tex(r"X(s)", BLUE)
        eq3.set_color_by_tex(r"F(s)", YELLOW)
        eq3.set_color_by_tex(r"s^2", CORAL)
        eq3.set_color_by_tex(r"2\zeta\omega_n s", GREEN)
        eq3.set_color_by_tex(r"\omega_n^2", CYAN)

        # Highlight frame around the Master Transfer Function
        box_h = SurroundingRectangle(
            eq3,
            buff=0.25,
            corner_radius=0.14,
            stroke_color=BLUE,
            stroke_width=2.5
        )

        # Step 2b: Dynamic Impedance Z(s) = 1 / H(s)
        eq4 = MathTex(
            r"Z(s) = \frac{1}{H(s)} \quad \text{(Dynamic Impedance)}",
            font_size=42
        ).move_to([0, -0.95, 0])
        eq4.set_color_by_tex(r"Z(s)", YELLOW)
        eq4.set_color_by_tex(r"H(s)", BLUE)
        eq4.set_color_by_tex(r"\text{(Dynamic Impedance)}", TEXT_MUTED)

        # ------------------------------------------------------------------
        # 4. Animation Sequence (3 Steps, 2 Cuepoint Pauses)
        # ------------------------------------------------------------------

        # --- STEP 0: Time-Domain SDOF Differential Equation (0.0s - 3.0s) ---
        self.play(FadeIn(title, shift=DOWN * 0.15), run_time=0.6)
        self.play(Write(eq0), run_time=1.4)
        self.wait(1.0)  # Exact Cuepoint 0 = 3.0s

        # --- STEP 1: Smooth Laplace Glide Morph (3.0s - 7.5s) ---
        self.play(
            TransformMatchingTex(
                eq0, eq1,
                key_map={
                    r"\ddot{x}": r"s^2",
                    r"\dot{x}": r"s",
                    r"x": r"X(s)",
                    r"F(t)": r"F(s)",
                },
                transform_mismatches=True
            ),
            run_time=1.5
        )
        self.wait(0.5)

        self.play(
            TransformMatchingTex(
                eq1, eq2,
                key_map={
                    r"c": r"2\zeta\omega_n",
                    r"s": r"s",
                    r"k": r"\omega_n^2",
                },
                transform_mismatches=True
            ),
            run_time=1.5
        )
        self.wait(1.0)  # Exact Cuepoint 1 = 7.5s

        # --- STEP 2: Transfer Function & Dynamic Impedance (7.5s - 14.0s) ---
        self.play(
            FadeTransform(eq2, eq3),
            run_time=1.7
        )
        self.wait(0.3)
        self.play(Create(box_h), run_time=0.8)
        self.play(FadeIn(eq4, shift=UP * 0.15), run_time=1.2)
        self.wait(2.5)  # Exact Cuepoint 2 = 14.0s (Calm resting state for commentary)

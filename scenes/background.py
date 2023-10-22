#!/usr/bin/env python

from manim import *
from manim_slides.slide import Slide
from constants import *
from shared import *

Tex.set_default(font_size=DEFINITION_FONT_SIZE)


class Notation(Slide):
    def construct(self):
        notation_header = get_definition("Review", "Notation")

        self.play(Write(notation_header, run_time=1))
        self.play(notation_header.animate.to_corner(UL))

        self.next_slide()

        norm_tex = Tex(
            r"""
            \begin{align}
                ||\mathbf{A}|| &= \max_{|x|_2 \neq 0} \frac{|\mathbf{Ax}|_2}{|\mathbf{x}|_2} \tag{maximum eigenvalue of $A^H A$} \\ 
                ||\mathbf{x}|| &= \sqrt{\sum_{i=1}^n x_i^2} \tag{$l_2$-norm} \\
                ||\mathbf{A}||_F &= \sqrt{\sum_{i=1}^m \sum_{j=1}^n a_{ij}^2} \tag{Frobenius norm}
            \end{align}
            """,
        )

        self.play(Write(norm_tex, run_time=3))
        self.next_slide()

        self.play(FadeOut(norm_tex))
        self.next_slide()

        sigma_tex = Tex(
            r"Singular values: $\sigma_{max}(\cdot),\sigma_{min}(\cdot),\sigma_i(\cdot)$"
        )
        lambda_tex = Tex(
            r"Eigenvalues: $\lambda_{max}(\cdot),\lambda_{min}(\cdot),\lambda_i(\cdot)$"
        )
        ball_tex = Tex(r"$d$-ball with radius $r$: $B(\mathbf{x}, r)$")

        gradient_tex = Tex(r"Gradient: $\nabla f(\mathbf{x})$")
        hessian_tex = Tex(r"Hessian: $\nabla^2 f(\mathbf{x})$")

        VGroup(sigma_tex, lambda_tex, ball_tex, gradient_tex, hessian_tex).arrange(
            DOWN, buff=0.5
        )

        self.play(
            Write(sigma_tex, run_time=2),
            Write(lambda_tex, run_time=2),
        )
        self.next_slide()

        self.play(
            Write(ball_tex, run_time=1),
        )
        self.next_slide()

        self.play(
            Write(gradient_tex, run_time=1),
            Write(hessian_tex, run_time=1),
        )
        self.next_slide()


class LSG(Slide):
    def construct(self):
        """
        Slides for both l-gradient lipschitz and strongly convex.
        """
        l_definition = get_definition("$l$-gradient Lipschitz")

        self.play(Write(l_definition, run_time=2))
        self.next_slide()

        self.play(l_definition.animate.to_corner(UL))
        self.next_slide()

        l_text = (
            Tex(r"A differentiable function $f$ is $l$-gradient Lipschitz if")
            .next_to(l_definition, DOWN, buff=0.5)
            .align_to(l_definition, LEFT)
        )

        self.play(Write(l_text, run_time=1))

        l_equation = MathTex(
            r"\forall \mathbf{x_1}, \mathbf{x_2}, \ ",
            r"||\nabla f(\mathbf{x_1}) - \nabla f(\mathbf{x_2})|| \leq l ||\mathbf{x_1} - \mathbf{x_2}||",
        )

        self.play(Write(l_equation, run_time=2))
        self.next_slide()

        self.play(
            l_equation.animate.next_to(l_text, DOWN, buff=0.5).align_to(l_text, LEFT)
        )

        convex_definition = get_definition(r"$\alpha$-strongly convex")

        self.play(Write(convex_definition, run_time=2))
        self.next_slide()

        self.play(
            convex_definition.animate.next_to(l_equation, DOWN, buff=0.5).align_to(
                l_equation, LEFT
            )
        )
        self.next_slide()

        text = (
            Tex(r"A twice-differentiable function $f$ is $\alpha$-strongly convex if")
            .next_to(convex_definition, DOWN, buff=0.5)
            .align_to(convex_definition, LEFT)
        )

        self.play(Write(text, run_time=1))

        eq = MathTex(
            r"\forall \mathbf{x}, \ ",
            r"\lambda_{min}(\nabla^2 f(\mathbf{x})) \geq \alpha",
        ).move_to((0, -2, 0))

        self.play(Write(eq, run_time=2))
        self.next_slide()

        self.play(eq.animate.next_to(text, DOWN, buff=0.5).align_to(text, LEFT))

        l_group = VGroup(l_definition, l_text, l_equation)
        convex_group = VGroup(convex_definition, text, eq)

        # Put a brace to the right of each of the groups
        l_brace = Brace(l_group, RIGHT)
        l_brace_text = Tex(r"\textit{Smoothness}\\ guarentee").next_to(l_brace, RIGHT)

        self.play(Write(l_brace, run_time=1), Write(l_brace_text, run_time=1))
        self.next_slide()

        c_brace = Brace(convex_group, RIGHT)
        c_brace_text = Tex(r"Unique stationary \\ point").next_to(c_brace, RIGHT)

        self.play(Write(c_brace, run_time=1), Write(c_brace_text, run_time=1))
        self.next_slide()

        self.play(
            FadeOut(l_group, run_time=2),
            FadeOut(l_brace, run_time=2),
            FadeOut(l_brace_text, run_time=2),
            FadeOut(c_brace, run_time=2),
            FadeOut(c_brace_text, run_time=2),
        )
        self.play(convex_group.animate.to_corner(UL), run_time=2)

        self.next_slide()

        theorem_1_header = get_definition("Convex Convergence", "Theorem 1")

        self.play(Write(theorem_1_header, run_time=2))
        self.next_slide()

        self.play(
            theorem_1_header.animate.next_to(convex_group, DOWN, buff=0.5).align_to(
                convex_group, LEFT
            )
        )

        theorem_1_text = (
            Tex(
                r"For $f$ $l$-smooth and $\alpha$-strongly convex, gradient descent will be $\epsilon$-close to the optimal solution in iterations:"
            )
            .next_to(theorem_1_header, DOWN, buff=0.5)
            .align_to(theorem_1_header, LEFT)
        )
        self.play(Write(theorem_1_text, run_time=2))
        self.next_slide()

        theorem_1_math = MathTex(
            r"\frac{2l}{\alpha} \log \frac{||\mathbf{x_0} - \mathbf{x^*}||}{\epsilon}"
        ).next_to(theorem_1_text, DOWN, buff=0.5)

        self.play(Write(theorem_1_math, run_time=2))
        self.next_slide()

        # Make a brace to the right that says "Not many functions are convex!"
        convex_brace = Brace(theorem_1_math, RIGHT, color=YELLOW)
        convex_brace_text = Tex(r"Only for convex functions!", color=YELLOW).next_to(
            convex_brace, RIGHT
        )

        self.play(Write(convex_brace, run_time=1), Write(convex_brace_text, run_time=1))
        self.next_slide()

        # Strike through the theorem 1 header with a yellow line
        yellow_line = Line(
            theorem_1_header.get_left(),
            theorem_1_header.get_right(),
            color=YELLOW,
        )

        self.play(Write(yellow_line, run_time=2))

        # Add text that says "Too Strong" to the right of the line
        too_strong = (
            Tex(r"Too Strong", color=YELLOW)
            .next_to(yellow_line, RIGHT)
            .next_to(yellow_line, RIGHT)
        )
        self.play(Write(too_strong, run_time=1))
        self.next_slide()

        # Fade out everything
        self.play(
            FadeOut(convex_group, run_time=2),
            FadeOut(theorem_1_header, run_time=2),
            FadeOut(theorem_1_text, run_time=2),
            FadeOut(theorem_1_math, run_time=2),
            FadeOut(yellow_line, run_time=2),
            FadeOut(too_strong, run_time=2),
            FadeOut(convex_brace, run_time=2),
            FadeOut(convex_brace_text, run_time=2),
        )

        self.next_slide()


class GoldStandard(Slide):
    def construct(self):
        theorem_2 = get_definition("Gold Standard", "Theorem 2")

        theorem_2_statement = Tex(
            r"For $f()$ ",
            "$l$-smooth"
            r"""
            , and some $\epsilon > 0$, gradient descent with $\eta = \frac{1}{l}$ will find an $\epsilon$-first order stationary point in iterations:
            """,
            tex_environment=None,
        )

        theorem_2_eq = MathTex(r"\frac{l(f(\mathbf{x_0}) - f^*)}{\epsilon^2}")

        self.play(Write(theorem_2, run_time=2))
        self.play(theorem_2.animate.to_corner(UL))
        self.next_slide()

        theorem_2_statement.next_to(theorem_2, DOWN).align_to(theorem_2, LEFT)

        self.play(Write(theorem_2_statement, run_time=2))
        self.next_slide()

        theorem_2_eq.next_to(theorem_2_statement, DOWN)

        self.play(Write(theorem_2_eq, run_time=2))
        self.next_slide()

        # Make a yellow brace to the right saying "Dimension free!"
        dimension_free_brace = Brace(theorem_2_eq, RIGHT, color=YELLOW)
        dimension_free_text = Tex(r"Dimension free!", color=YELLOW).next_to(
            dimension_free_brace, RIGHT
        )

        self.play(
            Write(dimension_free_brace, run_time=1),
            Write(dimension_free_text, run_time=1),
        )

        self.next_slide()

        # Make a green brace to the left saying "But finds saddle points..."
        saddle_point_brace = Brace(theorem_2_eq, LEFT, color=GREEN)
        saddle_point_text = Tex(r"But finds saddle points...", color=GREEN).next_to(
            saddle_point_brace, LEFT
        )

        self.play(
            Write(saddle_point_brace, run_time=1),
            Write(saddle_point_text, run_time=1),
        )
        self.next_slide()

        next_steps = (
            Tex(
                r"To avoid saddle points, we (probably) need to ",
                r"\textbf{use stronger assumptions} ",
                r"(but not convexity).",
                tex_environment=None,
            )
            .next_to(theorem_2_eq, DOWN, buff=0.5)
            .align_to(theorem_2_statement, LEFT)
        )

        next_steps[1].set_color(GREEN)
        self.play(Write(next_steps, run_time=3))
        self.next_slide()

        hessian_lipschitz = (
            Tex(
                r"Since saddle points rely on Hessian information, we need a ",
                "weak bound on the hessian of $f(\mathbf{x})$.",
                tex_environment=None,
            )
            .next_to(next_steps, DOWN, buff=0.5)
            .align_to(next_steps, LEFT)
        )

        hessian_lipschitz[1].set_color(GREEN)
        self.play(Write(hessian_lipschitz, run_time=2))
        self.next_slide()


class HessianLipschitz(Slide):
    def construct(self):
        hessian_definition = get_definition(r"$\rho$-Hessian Lipschitz")

        self.play(Write(hessian_definition, run_time=2))
        self.play(hessian_definition.animate.to_corner(UL))
        self.next_slide()

        hessian_statement = (
            Tex(
                r"A twice-differentiable function $f(\cdot)$ is $\rho$-Hessian Lipschitz if $\forall \mathbf{x_1}, \mathbf{x_2}$ we have",
                tex_environment=None,
            )
            .next_to(hessian_definition, DOWN, buff=0.5)
            .align_to(hessian_definition, LEFT)
        )

        hessian_equation = MathTex(
            r"|| \nabla^2 f(\mathbf{x_1}) - \nabla^2 f(\mathbf{x_2}) || \leq \rho || \mathbf{x_1} - \mathbf{x_2} ||",
        ).next_to(hessian_statement, DOWN, buff=0.5)

        self.play(Write(hessian_statement, run_time=2))
        self.next_slide()

        self.play(Write(hessian_equation, run_time=2))
        self.next_slide()


class Goal(Slide):
    """
    Slide for for showing a diagram of the
    """

    def construct(self):
        self.next_slide()


class Background(Scene):
    def construct(self):
        Notation.construct(self)

        self.wait()

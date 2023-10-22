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

        norm_tex = MathTex(
            r"""
            \begin{align}
                ||\mathbf{A}|| &= \max_{|x|_2 \neq 0} \frac{|\mathbf{Ax}|_2}{|\mathbf{x}|_2} \ (\text{maximum eigenvalue of } A^H A) \\ 
                ||\mathbf{x}|| &= \sqrt{\sum_{i=1}^n x_i^2} \ (l_2-\text{norm}) \\
                ||\mathbf{A}||_F &= \sqrt{\sum_{i=1}^m \sum_{j=1}^n a_{ij}^2} \ (\text{Frobenius norm}) \\
            \end{align}
            """,
        )

        self.play(Write(norm_tex, run_time=2))
        self.next_slide()

        self.play(
            norm_tex.animate.next_to(notation_header, DOWN, buff=0.5).align_to(
                notation_header, LEFT
            )
        )

        self.play(
            spectral_norm.animate.align_to(
                definition_name.get_corner(DL) + DOWN * 0.1, LEFT + UP
            )
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

        # Make a brace to the right that says "Only for convex functions!"


class Background(Scene):
    def construct(self):
        Notation.construct(self)

        self.wait()

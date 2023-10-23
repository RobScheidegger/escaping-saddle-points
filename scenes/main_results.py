from manim import *
from manim_slides.slide import Slide, ThreeDSlide
from shared import *


class Transition(Slide):
    def construct(self):
        render_outline(self, "Background", "Main Results")


class PGD(Slide):
    def construct(self):
        INDENT_WIDTH = 0.5

        title = Tex(
            r"PGD($\mathbf{x_0}, \ell, \rho, \epsilon, c, \delta, \Delta_f$)",
            color=BLUE,
        )
        # Add a line under title
        Tex.set_default(font_size=32)
        MathTex.set_default(font_size=32)

        self.play(Write(title, run_time=2))
        self.play(title.animate.to_corner(UL), run_time=1)
        line = Line(
            start=title.get_corner(DL) + DOWN * 0.1,
            end=title.get_corner(DR) + DOWN * 0.1,
            color=BLUE,
        )
        self.play(Create(line, run_time=1))
        self.next_slide()

        parameters_complex = (
            Tex(
                r"$\chi \leftarrow 3 \max\{ \log \frac{d\ell \Delta_f}{c\epsilon^2\delta, 4}\}$ \\",
                r"$\eta \leftarrow \frac{c}{\ell}$ \\",
                r"$r \leftarrow \frac{\sqrt{c}}{\chi^2} \cdot \frac{\epsilon}{\ell}$ \\",
                r"$g_{thres} \leftarrow \frac{\sqrt{c}}{\chi^2} \cdot \epsilon$ \\",
                r"$f_{thres} \leftarrow \frac{c}{\chi^3} \cdot \sqrt{\frac{\epsilon^3}{\rho}}$\\",
                r"$t_{thres} \leftarrow \frac{\chi}{c^2} \cdot \frac{\ell}{\sqrt{\rho \epsilon}}$\\",
                tex_environment=None,
            )
            .next_to(title, DOWN, buff=0.5)
            .align_to(title, LEFT)
        )

        self.play(Write(parameters_complex, run_time=2))
        self.next_slide()

        parameters_simple = (
            Tex(
                r"$\chi,\eta,r,g_{thres},f_{thres},t_{thres},t_{noise} \leftarrow ParamGen(\mathbf{x_0}, \ell, \rho, \epsilon, c, \delta, \Delta_f)$"
            )
            .next_to(title, DOWN, buff=0.5)
            .align_to(title, LEFT)
        )

        self.play(parameters_complex.animate.become(parameters_simple), run_time=2)
        self.next_slide()

        loop_text = (
            Tex(r"For $t = 0,1,\ldots$:")
            .next_to(parameters_simple, DOWN, buff=0.25)
            .align_to(parameters_simple, LEFT)
        )

        # Intuition: Use $g_thres$ to say to only add noise when we have a "small" gradient. OTherwise the gradient will do most of the work for us on descent.

        pertubation_condition = (
            Tex(
                r"If $||\nabla f(\mathbf{x_t})|| \leq g_{thres}$ and $t - t_{thres}$ then:",
                tex_environment=None,
            )
            .next_to(loop_text, DOWN, buff=0.25)
            .align_to(loop_text, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )

        pertubation_line_1 = (
            MathTex(
                r"\tilde{\mathbf{x_t}} \leftarrow \mathbf{x_t}, t_{noise} \leftarrow t"
            )
            .next_to(pertubation_condition, DOWN, buff=0.25)
            .align_to(pertubation_condition, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )
        pertubation_line_2 = (
            MathTex(
                r"\tilde{\mathbf{x_t}} \leftarrow \mathbf{x_t} + \xi_t,",
                r"\xi_t \leftarrow \mathbb{B}_0(r)",
            )
            .next_to(pertubation_line_1, DOWN, buff=0.25)
            .align_to(pertubation_line_1, LEFT)
        )

        pertubation_group = VGroup(
            pertubation_condition, pertubation_line_1, pertubation_line_2
        )
        self.play(Write(loop_text, run_time=2))
        self.next_slide()

        self.play(Write(pertubation_group, run_time=2))
        self.next_slide()

        termination_condition = (
            Tex(
                r"If $t - t_{noise} = t_{thres}$ and $f(\mathbf{x_t}) - f(\tilde{\mathbf{x_t}}) > -f_{thres}$ then:"
            )
            .next_to(pertubation_group, DOWN, buff=0.25)
            .align_to(pertubation_group, LEFT)
        )

        termination_return = (
            Tex(r"Return $\tilde{\mathbf{x_{t_{noise}}}}$")
            .next_to(termination_condition, DOWN, buff=0.25)
            .align_to(termination_condition, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )

        termination_group = VGroup(termination_condition, termination_return)

        self.play(Write(termination_condition), Write(termination_return), run_time=2)
        self.next_slide()

        descent = (
            Tex(
                r"$\mathbf{x_{t+1}} \leftarrow \mathbf{x_t} - \eta \nabla f(\mathbf{x_t})$"
            )
            .next_to(termination_return, DOWN, buff=0.25)
            .align_to(termination_condition, LEFT)
        )
        self.play(Write(descent), run_time=2)
        self.next_slide()

        pertubation_brace = Brace(pertubation_group, RIGHT, color=YELLOW)
        pertubation_brace_text = Tex(
            r"Add a small amount of noise\\every $t_{noise}$ steps,\\when the gradient is small",
            color=YELLOW,
        ).next_to(pertubation_brace, RIGHT, buff=0.25)

        self.play(Write(pertubation_brace), Write(pertubation_brace_text), run_time=2)
        self.next_slide()

        convergence_brace = Brace(termination_group, RIGHT, color=YELLOW)
        convergence_brace_text = Tex(
            r"Terminate when the function\\has not decreased enough\\ (converged)",
            color=YELLOW,
        ).next_to(convergence_brace, RIGHT, buff=0.25)

        self.play(Write(convergence_brace), Write(convergence_brace_text), run_time=2)
        self.next_slide()

        gradient_brace = Brace(descent, RIGHT, color=BLUE)
        gradient_brace_text = Tex(
            r"Take a regular gradient step every iteration",
            color=BLUE,
        ).next_to(gradient_brace, RIGHT, buff=0.25)

        self.play(Write(gradient_brace), Write(gradient_brace_text), run_time=2)
        self.next_slide()

        ball_box = SurroundingRectangle(pertubation_line_2[1], color=GREEN)
        self.play(
            Create(ball_box),
            pertubation_line_2[1].animate.set_color(GREEN),
            run_time=2,
        )
        self.next_slide()


class Theorem3(Slide):
    """
    State that from here on out, we assume that f is l-smooth and rho-hessian lipschitz.

    State theorem 3, and highlight the difference parts of the term (original and new log factor).

    Argue that
    """

    def construct(self):
        self.next_slide()


class Theorem3ProofSketch(Slide):
    """
    Give the theorem proof sketch, with different cases for

    End with statement of lemma 10.
    """

    def construct(self):
        self.next_slide()


class PertubationBall(ThreeDSlide):
    """
    Give the pertubation ball visual, and results from the appendix for the integral and why it must be bounded in this way.

    This is a proof sketch of lemma 10.
    """

    def construct(self):
        self.next_slide()


class Theorem3Conclusion(Slide):
    """
    Bring the results together from the pertubation example to conclude that theorem 3 is correct.
    """

    def construct(self):
        self.next_slide()


class Corollary4(Slide):
    """
    Explain the strict saddle point assumption, the 3 possible cases, and why selecting values tells us that when PGD terminats,
    we must be at a local minimum specifically.
    """

    def construct(self):
        self.next_slide()


class LocalStructure(Slide):

    """
    Briefly mention that if we have slightly stronger local structure assumptions, we can get a stronger result.

    By just running PGD and then running a fixed gradient descent afterwards (no proofs).
    """

    def construct(self):
        self.next_slide()

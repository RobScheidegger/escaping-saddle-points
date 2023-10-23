from manim import *
from manim_slides.slide import Slide, ThreeDSlide
from constants import *
from shared import *


class Opening(Slide):
    def construct(self):
        title = Tex(r"How to Escape Saddle Points Efficiently", color=BLUE)
        subtitle_1 = Tex(r"[JGNKN '17]")
        subtitle_2 = Tex(r"Paper Presentation by Robert Scheidegger")
        VGroup(title, subtitle_1, subtitle_2).arrange(DOWN)
        self.play(
            Write(title, run_time=2),
            Wait(2),
            FadeIn(subtitle_1, shift=UP, run_time=3),
            Wait(1),
            FadeIn(subtitle_2, shift=UP, run_time=3),
        )
        self.next_slide()


class GradientDescentIntro(Slide):
    def construct(self):
        Tex.set_default(font_size=DEFINITION_FONT_SIZE)

        definition_name = Tex(
            r"\textbf{Definition (Gradient Descent).} ",
            color=DEFINITION_NAME_COLOR,
        )

        definition_given_f = Tex(
            r"Given $f: \mathbb{R}^{d} \to \mathbb{R}$ and initial point $x_0 \in \mathbb{R}^{d}$,",
        )

        header_group = VGroup(definition_name, definition_given_f).arrange(RIGHT)

        vertical_group = VGroup(header_group).to_edge(LEFT).to_edge(UP)

        self.play(Write(definition_name, run_time=2))
        self.next_slide()
        self.play(Write(definition_given_f, run_time=1.5))
        self.next_slide()

        equation_0 = MathTex(
            r"x_1 = x_0 - ",
            r"\eta",
            r"\nabla f(x_0)",
        )

        self.play(Write(equation_0), run_time=3)
        self.next_slide()

        eta_surrounding_rectangle = SurroundingRectangle(equation_0[1], color=YELLOW)
        self.play(Create(eta_surrounding_rectangle), run_time=1)
        self.next_slide()
        self.play(FadeOut(eta_surrounding_rectangle), run_time=1)
        self.next_slide()

        gradient_surrounding_rectangle = SurroundingRectangle(
            equation_0[2], color=YELLOW
        )
        self.play(Create(gradient_surrounding_rectangle), run_time=1.5)
        self.next_slide()
        self.play(FadeOut(gradient_surrounding_rectangle), run_time=1.5)
        self.next_slide()

        equation_1 = MathTex(
            r"x_{t+1} = x_t - ",
            r"\eta",
            r"\nabla f(x_t)",
        )

        self.play(Transform(equation_0, equation_1), run_time=3)
        self.next_slide()

        vertical_group.add(equation_1)

        goal_text = Tex(
            r"Goal: Find a stationary point of ",
            r"$f(x)$ ",
            r"($\lVert f(x) \rVert = 0$).",
        )
        question_1 = Tex("Q: How many iterations do we need?")
        question_2 = Tex("Q: What about saddle points?")

        group = VGroup(goal_text, question_1, question_2)
        group.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5)
        group.move_to((0, -2, 0))
        self.play(Write(goal_text), run_time=3)
        self.next_slide()
        self.play(Write(question_1), run_time=3)
        self.next_slide()
        self.play(Write(question_2), run_time=3)
        self.next_slide()

        gradient_surrounding_rectangle = SurroundingRectangle(
            goal_text[2], color=YELLOW
        )
        self.play(Create(gradient_surrounding_rectangle), run_time=1)
        self.next_slide()
        self.play(FadeOut(gradient_surrounding_rectangle), run_time=1)
        self.next_slide()

        goal_text_updated = Tex(
            r"Goal: Find a stationary point of ",
            r"$f(x)$ ",
            r"($\lVert f(x) \rVert \leq \epsilon$).",
        )
        goal_text_updated.move_to(goal_text)

        self.play(Transform(goal_text, goal_text_updated), run_time=3)
        self.next_slide()


class GradientDescentDemo(ThreeDSlide):
    def construct(self):
        axes = ThreeDAxes()
        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8)
        z_label = axes.get_z_axis_label(Tex("z")).shift(LEFT * 1.8)

        self.set_camera_orientation(zoom=0.5)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1)

        f_text = Tex(r"$f(x) = x^4 - 4x^2 + 5$", font_size=42)
        self.add_fixed_in_frame_mobjects(f_text)

        # Write the text as an overlay in the 3D scene
        self.play(Write(f_text))
        self.next_slide()
        self.play(f_text.animate.to_corner(UL))
        self.next_slide()

        X_SCALE = 10
        Y_SCALE = 10
        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))
        f_surface = Surface(
            lambda x, y: axes.c2p(
                x * X_SCALE, y * Y_SCALE, np.sin(X_SCALE * x + Y_SCALE * y)
            ),
            resolution=(20, 20),
            u_range=[-1, 1],
            v_range=[-1, 1],
        )
        self.play(FadeIn(f_surface))

        self.next_slide()


class Algorithms(Slide):
    def construct(self):
        INDENT_WIDTH = 0.5
        # Give the original gradient descent algorithm
        algorithm_name = Tex(r"\textbf{Gradient Descent}", color=BLUE)

        self.play(Write(algorithm_name, run_time=2))
        self.play(algorithm_name.animate.to_corner(UL), run_time=2)
        self.next_slide()

        gradient_loop = (
            Tex(r"While not converged, do:")
            .next_to(algorithm_name, DOWN)
            .align_to(algorithm_name, LEFT)
        )

        gradient_iteration = (
            MathTex(r"x_{t+1} = x_t - \eta \nabla f(x_t)")
            .next_to(gradient_loop, DOWN)
            .align_to(gradient_loop, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )

        self.play(Write(gradient_loop, run_time=2))
        self.play(Write(gradient_iteration, run_time=2))

        self.next_slide()

        perturbed_gradient_name = (
            Tex(r"\textbf{Perturbed Gradient Descent}", color=BLUE)
            .align_to((-0.3, 0, 0), LEFT)
            .align_to(algorithm_name, UP)
        )

        self.play(Write(perturbed_gradient_name, run_time=2))
        self.next_slide()

        perturbed_gradient_loop = (
            gradient_loop.copy()
            .next_to(perturbed_gradient_name, DOWN)
            .align_to(perturbed_gradient_name, LEFT)
        )

        perturbation_condition = (
            Tex(r"If \textbf{pertubation condition}:", color=GREEN)
            .next_to(perturbed_gradient_loop, DOWN)
            .align_to(perturbed_gradient_loop, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )

        pertubation_prep = MathTex(r"\xi_t \leftarrow \mathbb{B}_0(r)", color=GREEN)
        pertubation_step = MathTex(r"x_{t+1} = x_t + \xi_t", color=GREEN)
        pertubation_group = (
            VGroup(pertubation_prep, pertubation_step)
            .arrange(DOWN, center=False, aligned_edge=LEFT)
            .next_to(perturbation_condition, DOWN)
            .align_to(perturbation_condition, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )

        perturbed_gradient_iteration = (
            gradient_iteration.copy()
            .next_to(pertubation_group, DOWN)
            .align_to(perturbation_condition, LEFT)
        )

        self.play(
            Write(perturbed_gradient_loop, run_time=2),
            Write(perturbed_gradient_iteration, run_time=2),
        )
        self.next_slide()

        self.play(Write(perturbation_condition, run_time=2))
        self.play(Write(pertubation_group, run_time=2))
        self.next_slide()

        non_convex_text = (
            Tex(
                r"For non-convex functions $f: \mathbb{R}^d \to \mathbb{R}$:",
                color=YELLOW,
            )
            .next_to(perturbed_gradient_iteration, DOWN)
            .align_to(algorithm_name, LEFT)
        )

        self.play(Write(non_convex_text, run_time=2))
        self.next_slide()

        gradient_result = (
            Tex(r"$\epsilon$-second-order \\ stationary point")
            .next_to(non_convex_text, DOWN)
            .shift(LEFT * 2)
            .shift(DOWN * 0.5)
        )
        gradient_result_rectangle = rectangle_around(gradient_result, YELLOW)

        self.play(
            Write(gradient_result, run_time=2),
            Create(gradient_result_rectangle, run_time=2),
        )
        self.next_slide()

        perturbed_result = (
            Tex("Local Minima").next_to(gradient_result, RIGHT).shift(RIGHT * 6)
        )
        perturbed_result_rectangle = rectangle_around(perturbed_result, GREEN)

        self.play(
            Write(perturbed_result, run_time=2),
            Create(perturbed_result_rectangle, run_time=2),
        )
        self.next_slide()

        arrow = Arrow(
            gradient_result_rectangle.get_right(),
            perturbed_result_rectangle.get_left(),
            color=WHITE,
        )
        arrow_above = Tex(r"$\rho$-Hessian Lipschitz").next_to(arrow, UP)
        arrow_below = Tex(r"$(\theta, \gamma, \zeta)-$strict Saddle").next_to(
            arrow, DOWN
        )

        self.play(Create(arrow), run_time=2)
        self.play(Write(arrow_above), Write(arrow_below), run_time=2)
        self.next_slide()

        overhead = Tex(r"$O(\log^4(k))$ overhead", color=GREEN).next_to(
            perturbed_result_rectangle, DOWN
        )

        self.play(Write(overhead), run_time=2)
        self.next_slide()


class PreviousWork(Slide):
    def construct(self):
        algorithm_text = Tex(r"Algorithm", color=BLUE, font_size=DEFINITION_FONT_SIZE)
        iteration_text = Tex(r"Iteration", color=BLUE, font_size=DEFINITION_FONT_SIZE)
        oracle_text = Tex(r"Oracle", color=BLUE, font_size=DEFINITION_FONT_SIZE)

        algorithm_definitions = [
            ("Ge et al. [2015]", [r"O(poly(d/\epsilon))"], "Gradient"),
            ("Levy [2016]", [r"O(d^3 \cdot poly(1 / \epsilon))"], "Gradient"),
            (
                r"\textbf{This Work}",
                [r"\mathbf{O}(", r"\mathbf{\log^4 (d)}", r"/ \mathbf{\epsilon^2})}"],
                "Gradient",
            ),
            (
                "Argawal et al. [2016]",
                [r"O(\log (d) / \epsilon^{7/4})"],
                "Hessian-vector product",
            ),
            (
                "Carmon et al. [2016]",
                [r"O(\log (d) / \epsilon^{7/4})"],
                "Hessian-vector product",
            ),
            (
                "Carmon and Duchi [2016]",
                [r"O(\log (d) / \epsilon^2)"],
                "Hessian-vector product",
            ),
            (
                "Nesterov and Polyak [2006]",
                [r"O(1/\epsilon^{1.5})"],
                "Hessian",
            ),
            (
                "Curtis et al. [2014]",
                [r"O(1/\epsilon^{1.5})"],
                "Hessian",
            ),
        ]

        # Make Tex objects from algorithms
        algorithms = []
        algorithms_grouped = []

        for algorithm, iterations, oracle in algorithm_definitions:
            elements = [
                Tex(algorithm, font_size=DEFINITION_FONT_SIZE),
                MathTex(*iterations, font_size=DEFINITION_FONT_SIZE),
                Tex(oracle, font_size=DEFINITION_FONT_SIZE),
            ]
            algorithms += elements
            algorithms_grouped += [elements]

        group = VGroup(
            algorithm_text, iteration_text, oracle_text, *algorithms
        ).arrange_in_grid(cols=3, rows=1 + len(algorithm_definitions), buff=0.25)

        self.play(
            Write(algorithm_text, run_time=2),
            Write(iteration_text, run_time=2),
            Write(oracle_text, run_time=2),
        )

        self.next_slide()

        def play_index(algorithm_index):
            self.play(
                Write(algorithms_grouped[algorithm_index][0], run_time=1),
                Write(algorithms_grouped[algorithm_index][1], run_time=1),
                Write(algorithms_grouped[algorithm_index][2], run_time=1),
            )

        play_index(0)
        self.next_slide()

        play_index(1)
        self.next_slide()

        play_index(6)
        play_index(7)
        self.next_slide()

        play_index(3)
        play_index(4)
        play_index(5)
        self.next_slide()

        # TODO: Add some visual details about the hessian vector product
        play_index(2)
        self.next_slide()

        # Put a surrounding rectangle around the number of iterations
        rectangle = SurroundingRectangle(algorithms_grouped[2][1][1], color=YELLOW)
        self.play(Create(rectangle), run_time=1)
        self.next_slide()

        self.play(FadeOut(rectangle), run_time=1)
        self.next_slide()

        # Highlight the rows for this work and the Carmon and Duchi paper
        self.play(
            algorithms_grouped[2][0].animate.set_color(GREEN),
            algorithms_grouped[2][1].animate.set_color(GREEN),
            algorithms_grouped[2][2].animate.set_color(GREEN),
            algorithms_grouped[5][0].animate.set_color(GREEN),
            algorithms_grouped[5][1].animate.set_color(GREEN),
            algorithms_grouped[5][2].animate.set_color(GREEN),
        )
        self.next_slide()


class Outline(Slide):
    def construct(self):
        title = Tex(r"Outline", color=BLUE, font_size=HEADER_FONT_SIZE)

        section_names = ["Introduction", "Background", "Main Results", "Takeaways"]
        sections = [
            Tex(str(i + 1) + ". " + name, font_size=HEADER_FONT_SIZE)
            for i, name in enumerate(section_names)
        ]

        group = VGroup(title, *sections).to_edge(LEFT).to_edge(UP)

        group.arrange(DOWN, center=False, aligned_edge=LEFT, buff=1)

        self.play(Write(title, run_time=2))

        for i, section in enumerate(sections):
            self.play(Write(section, run_time=1.5))
            self.next_slide()

            if i == 0:
                self.play(sections[0].animate.set_color(YELLOW))
                self.next_slide()

        # Make a surrounding rectangle for the Background section
        background_surrounding_rectangle = SurroundingRectangle(
            sections[1], color=YELLOW
        )

        self.play(Write(background_surrounding_rectangle), run_time=1)
        self.play(
            sections[1].animate.set_color(YELLOW), sections[0].animate.set_color(WHITE)
        )
        self.play(FadeOut(background_surrounding_rectangle), run_time=1)

        self.next_slide()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.next_slide()

#!/usr/bin/env python

from manim import *
from constants import *


class Opening(Scene):
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
        self.wait()


class GradientDescentIntro(Scene):
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
        self.play(Wait(2))
        self.play(Write(definition_given_f, run_time=1.5))
        self.play(Wait(5))

        equation_0 = MathTex(
            r"x_1 = x_0 - ",
            r"\eta",
            r"\nabla f(x_0)",
        )

        self.play(Write(equation_0), run_time=3)

        eta_surrounding_rectangle = SurroundingRectangle(equation_0[1], color=YELLOW)
        self.play(Create(eta_surrounding_rectangle), run_time=3)
        self.play(FadeOut(eta_surrounding_rectangle), run_time=3)

        gradient_surrounding_rectangle = SurroundingRectangle(
            equation_0[2], color=YELLOW
        )
        self.play(Create(gradient_surrounding_rectangle), run_time=1.5)
        self.play(FadeOut(gradient_surrounding_rectangle), run_time=1.5)

        self.play(Wait(4))
        equation_1 = MathTex(
            r"x_{t+1} = x_t - ",
            r"\eta",
            r"\nabla f(x_t)",
        )

        self.play(Transform(equation_0, equation_1), run_time=3)
        self.play(Wait(4))

        vertical_group.add(equation_1)

        goal_text = Tex(
            r"Goal: Find a local minima of ",
            r"$f(x)$ ",
            r"($\lVert f(x) \rVert = 0$).",
        )
        question_1 = Tex("Q: How many iterations do we need?")
        question_2 = Tex("Q: What about saddle points?")

        group = VGroup(goal_text, question_1, question_2)
        group.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.5)
        group.move_to((0, -2, 0))
        self.play(Write(goal_text), run_time=3)
        self.play(Wait(3))
        self.play(Write(question_1), run_time=3)
        self.play(Wait(3))
        self.play(Write(question_2), run_time=3)
        self.play(Wait(3))

        # Surround rectangle around "local minima"
        local_minima_surrounding_rectangle = SurroundingRectangle(
            goal_text[1], color=YELLOW
        )
        self.play(Write(local_minima_surrounding_rectangle), run_time=1)
        self.play(FadeOut(local_minima_surrounding_rectangle), run_time=1)

        gradient_surrounding_rectangle = SurroundingRectangle(
            goal_text[2], color=YELLOW
        )
        self.play(Create(gradient_surrounding_rectangle), run_time=1)
        self.play(FadeOut(gradient_surrounding_rectangle), run_time=2)

        goal_text_updated = Tex(
            r"Goal: Find a local minima of ",
            r"$f(x)$ ",
            r"($\lVert f(x) \rVert \leq \epsilon$).",
        )
        goal_text_updated.move_to(goal_text)

        self.play(Transform(goal_text, goal_text_updated), run_time=3)
        self.play(Wait(3))

        self.wait()


class GradientDescentDemo(ThreeDScene):
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
        self.play(Wait(3))
        self.play(f_text.animate.to_corner(UL))

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

        self.wait(5)


class PreviousWork(Scene):
    def construct(self):
        algorithm_text = Tex(r"Algorithm", color=BLUE, font_size=DEFINITION_FONT_SIZE)
        iteration_text = Tex(r"Iteration", color=BLUE, font_size=DEFINITION_FONT_SIZE)
        oracle_text = Tex(r"Oracle", color=BLUE, font_size=DEFINITION_FONT_SIZE)

        algorithm_definitions = [
            ("Ge et al. [2015]", [r"O(poly(d/\epsilon))"], "Gradient"),
            ("Levy [2016]", [r"O(d^3 \cdot poly(1 / \epsilon))"], "Gradient"),
            (
                r"\textbf{This Work}",
                [r"\mathbf{O(", r"\log^4 (d)", r"/ \epsilon^2)}"],
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

        self.wait(4)

        def play_index(algorithm_index):
            self.play(
                Write(algorithms_grouped[algorithm_index][0], run_time=1),
                Write(algorithms_grouped[algorithm_index][1], run_time=1),
                Write(algorithms_grouped[algorithm_index][2], run_time=1),
            )

        play_index(0)
        self.wait(2)

        play_index(1)
        self.wait(2)

        play_index(5)
        play_index(6)
        self.wait(5)

        play_index(3)
        play_index(4)
        self.wait(4)

        # TODO: Add some visual details about the hessian vector product
        play_index(2)
        self.wait(4)

        # Put a surrounding rectangle around the number of iterations
        rectangle = SurroundingRectangle(algorithms_grouped[2][1][1], color=YELLOW)
        self.play(Create(rectangle), run_time=1)
        self.wait(5)

        self.play(FadeOut(rectangle), run_time=1)
        self.wait(1)

        # Highlight the rows for this work and the Carmon and Duchi paper
        self.play(
            algorithms_grouped[2][0].animate.set_color(GREEN),
            algorithms_grouped[2][1].animate.set_color(GREEN),
            algorithms_grouped[2][2].animate.set_color(GREEN),
            algorithms_grouped[5][0].animate.set_color(GREEN),
            algorithms_grouped[5][1].animate.set_color(GREEN),
            algorithms_grouped[5][2].animate.set_color(GREEN),
        )
        self.wait(4)


class Outline(Scene):
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
            self.play(Wait(3))

            if i == 0:
                self.play(sections[0].animate.set_color(YELLOW))
                self.play(Wait(3))

        self.wait(5)

        # Make a surrounding rectangle for the Background section
        background_surrounding_rectangle = SurroundingRectangle(
            sections[1], color=YELLOW
        )

        self.play(Write(background_surrounding_rectangle), run_time=1)
        self.play(
            sections[1].animate.set_color(YELLOW), sections[0].animate.set_color(WHITE)
        )
        self.play(FadeOut(background_surrounding_rectangle), run_time=1)

        self.wait()


class Introduction(Scene):
    def construct(self):
        Opening.construct(self)
        self.clear()
        GradientDescentIntro.construct(self)

        self.clear()
        GradientDescentDemo().construct()

        self.clear()
        PreviousWork.construct(self)

        self.clear()
        Outline.construct(self)

        self.wait(2)

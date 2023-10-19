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
            goal_text[3], color=YELLOW
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


class GradientDescentDemo(Scene):
    def construct(self):
        f_text = Tex(r"$f(x) = x^4 - 4x^2 + 5$", font_size=42)

        self.wait()


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

        self.wait()


class Introduction(Scene):
    def construct(self):
        Opening.construct(self)
        self.clear()
        GradientDescentIntro.construct(self)

        self.clear()
        GradientDescentDemo.construct(self)

        self.clear()
        Outline.construct(self)

        self.wait(2)

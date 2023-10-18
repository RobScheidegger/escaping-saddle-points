#!/usr/bin/env python

from manim import *


class Opening(Scene):
    def construct(self):
        title = Tex(r"How to Escape Saddle Points Efficiently")
        subtitle_1 = Tex(r"[JGNKN '17]")
        subtitle_2 = Tex(r"Paper Presentation by Robert Scheidegger")
        VGroup(title, subtitle_1, subtitle_2).arrange(DOWN)
        self.play(
            Write(title, run_time=2),
            Wait(2),
            FadeIn(subtitle_1, shift=DOWN, run_time=3),
            FadeIn(subtitle_2, shift=DOWN, run_time=3),
        )
        self.wait()


class GradientDescentIntro(Scene):
    def construct(self):
        definition_name = Tex(r"\\mathbf{Definition (Gradient Descent).} ")

        self.play(Write(definition_name, run_time=2))

        self.wait()

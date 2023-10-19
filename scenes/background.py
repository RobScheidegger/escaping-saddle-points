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

"""
This file contains the entire presentation written as a single Manim scene, to make compiling easier.
"""

from manim import *
from constants import *
from introduction import Introduction


class EscapingSaddlePointsEfficiently(Scene):
    def construct(self):
        Introduction.construct(self)

        self.clear()

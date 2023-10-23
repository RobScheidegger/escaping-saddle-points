from manim import *
from manim_slides.slide import Slide
from shared import *


class Transition(Slide):
    def construct(self):
        render_outline(self, "Background", "Main Results")

from manim import *
from manim_slides.slide import Slide
from shared import *


class Transition(Slide):
    def construct(self):
        render_outline(self, "Main Results", "Takeaways")


class Takeaways(Slide):
    """
    - Carefully adding additional constraints is often an effective way to get stronger theoretical guarantees
    - Gives a (nearly) dimension free result for gradient descent in the general non-convex setting
    -
    """

    def construct(self):
        self.add_title("Takeaways")
        self.next_slide()

        self.add_bullet("We propose a new attack that is efficient and effective")

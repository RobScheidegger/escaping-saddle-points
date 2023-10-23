from manim import *
from manim_slides.slide import Slide
from constants import *

WRAPPER_BUFFER = 0.3


def get_definition(name: str, type="Definition") -> Tex:
    definition_name = Tex(
        rf"{type} (\textbf{{{name}}}) ",
        color=DEFINITION_NAME_COLOR,
        font_size=48,
    )
    return definition_name


def ellipse_around(mobject, color: str = BLUE):
    return Ellipse(
        color=color,
        fill_opacity=0.2,
        width=mobject.width + WRAPPER_BUFFER * 3,
        height=mobject.height + WRAPPER_BUFFER * 3,
    ).move_to(mobject)


def rectangle_around(mobject, color: str = BLUE):
    return Rectangle(
        color=color,
        fill_opacity=0.2,
        width=mobject.width + WRAPPER_BUFFER,
        height=mobject.height + WRAPPER_BUFFER,
    ).move_to(mobject)


def render_outline(self: Slide, old_section: str, new_section: str):
    """
    Re
    """

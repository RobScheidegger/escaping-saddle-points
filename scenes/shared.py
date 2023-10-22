from manim import *

from constants import *


def get_definition(name: str, type="Definition") -> Tex:
    definition_name = Tex(
        rf"{type} (\textbf{{{name}}}) ",
        color=DEFINITION_NAME_COLOR,
        font_size=48,
    )
    return definition_name

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
    title = Tex(r"Outline", color=BLUE, font_size=HEADER_FONT_SIZE)

    section_names = ["Introduction", "Background", "Main Results", "Takeaways"]
    sections = [
        Tex(str(i + 1) + ". " + name, font_size=HEADER_FONT_SIZE)
        for i, name in enumerate(section_names)
    ]

    old_section_index = section_names.index(old_section)
    new_section_index = section_names.index(new_section)

    sections[old_section_index].set_color(YELLOW)

    group = VGroup(*([title] + sections)).to_edge(LEFT).to_edge(UP)

    group.arrange(DOWN, center=False, aligned_edge=LEFT, buff=0.8)

    self.play(Write(group, run_time=2))
    self.next_slide()

    # Make a surrounding rectangle for the Background section
    surrounding_rectangle = SurroundingRectangle(
        sections[new_section_index], color=YELLOW, buff=0.5
    )

    self.play(Write(surrounding_rectangle), run_time=1)
    self.play(
        sections[new_section_index].animate.set_color(YELLOW),
        sections[old_section_index].animate.set_color(WHITE),
        run_time=2,
    )

    self.play(FadeOut(surrounding_rectangle), run_time=1)
    self.next_slide()

    # Fade everything out
    self.play(FadeOut(group), FadeOut(title), run_time=2)


def place_below(mobject, below_mobject, buff=0.5):
    return mobject.next_to(below_mobject, DOWN, buff=buff).align_to(below_mobject, LEFT)

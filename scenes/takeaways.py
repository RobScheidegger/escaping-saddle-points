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
        header = Tex(r"Takeaways", color=BLUE, font_size=HEADER_FONT_SIZE).to_corner(UL)
        self.play(Write(header))
        self.next_slide()

        tex_list = Tex(
            r"\item Used a stronger condition on $f$ ($\rho$-Hessian Lipschitz) to get a stronger result, and then improved on that using the $(\theta,\gamma,\zeta)$-strict saddle assumption.",
            r"\item Able to achieve a (simple) nearly dimension free algorithm for finding local minima of non-convex functions.",
            r"\item First step towards a more \textbf{general theory} with strong, \textit{almost dimension free} guarantees for non-convex optimization.",
            tex_environment="itemize",
            font_size=DEFINITION_FONT_SIZE,
        ).shift(UP * 0.75)

        self.play(Write(tex_list[0]))
        self.next_slide()
        self.play(Write(tex_list[1]))
        self.next_slide()
        self.play(Write(tex_list[2]))
        self.next_slide()

        pgd = Tex(
            r"""
            Perturbed Gradeint Descent can find an $\epsilon$-second-order stationary point of a non-convex function $f: \mathbb{R}^d \to \mathbb{R}$ in iterations:
            \begin{equation*}
                O \left( \frac{\log^4(d)}{\epsilon^2} \right)
            \end{equation*}
            """,
            font_size=DEFINITION_FONT_SIZE,
            tex_environment=None,
        ).shift(DOWN * 2.5)

        pgd_rectangle = SurroundingRectangle(
            pgd, color=GREEN, fill_color=GREEN, fill_opacity=0.2
        )

        self.play(Write(pgd), Write(pgd_rectangle))
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.next_slide()

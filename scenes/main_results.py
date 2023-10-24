from manim import *
from manim_slides.slide import Slide, ThreeDSlide
from shared import *

Tex.set_default(font_size=36)
MathTex.set_default(font_size=36)


class Transition(Slide):
    def construct(self):
        render_outline(self, "Background", "Main Results")


class PGD(Slide):
    def construct(self):
        INDENT_WIDTH = 0.5

        title = Tex(
            r"PGD($\mathbf{x_0}, \ell, \rho, \epsilon, c, \delta, \Delta_f$)",
            color=BLUE,
        )
        # Add a line under title
        Tex.set_default(font_size=32)
        MathTex.set_default(font_size=32)

        self.play(Write(title, run_time=2))
        self.play(title.animate.to_corner(UL), run_time=1)
        line = Line(
            start=title.get_corner(DL) + DOWN * 0.1,
            end=title.get_corner(DR) + DOWN * 0.1,
            color=BLUE,
        )
        self.play(Create(line, run_time=1))
        self.next_slide()

        parameters_complex = (
            Tex(
                r"$\chi \leftarrow 3 \max\{ \log \frac{d\ell \Delta_f}{c\epsilon^2\delta, 4}\}$ \\",
                r"$\eta \leftarrow \frac{c}{\ell}$ \\",
                r"$r \leftarrow \frac{\sqrt{c}}{\chi^2} \cdot \frac{\epsilon}{\ell}$ \\",
                r"$g_{thres} \leftarrow \frac{\sqrt{c}}{\chi^2} \cdot \epsilon$ \\",
                r"$f_{thres} \leftarrow \frac{c}{\chi^3} \cdot \sqrt{\frac{\epsilon^3}{\rho}}$\\",
                r"$t_{thres} \leftarrow \frac{\chi}{c^2} \cdot \frac{\ell}{\sqrt{\rho \epsilon}}$\\",
                tex_environment=None,
            )
            .next_to(title, DOWN, buff=0.5)
            .align_to(title, LEFT)
        )

        self.play(Write(parameters_complex, run_time=2))
        self.next_slide()

        parameters_simple = (
            Tex(
                r"$\chi,\eta,r,g_{thres},f_{thres},t_{thres},t_{noise} \leftarrow ParamGen(\mathbf{x_0}, \ell, \rho, \epsilon, c, \delta, \Delta_f)$"
            )
            .next_to(title, DOWN, buff=0.5)
            .align_to(title, LEFT)
        )

        self.play(parameters_complex.animate.become(parameters_simple), run_time=2)
        self.next_slide()

        loop_text = (
            Tex(r"For $t = 0,1,\ldots$:")
            .next_to(parameters_simple, DOWN, buff=0.25)
            .align_to(parameters_simple, LEFT)
        )

        # Intuition: Use $g_thres$ to say to only add noise when we have a "small" gradient. OTherwise the gradient will do most of the work for us on descent.

        pertubation_condition = (
            Tex(
                r"If $||\nabla f(\mathbf{x_t})|| \leq g_{thres}$ and $t - t_{thres}$ then:",
                tex_environment=None,
            )
            .next_to(loop_text, DOWN, buff=0.25)
            .align_to(loop_text, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )

        pertubation_line_1 = (
            MathTex(
                r"\mathbf{\tilde{x}_t}} \leftarrow \mathbf{x_t}, t_{noise} \leftarrow t"
            )
            .next_to(pertubation_condition, DOWN, buff=0.25)
            .align_to(pertubation_condition, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )
        pertubation_line_2 = (
            MathTex(
                r"\mathbf{\tilde{x}_t}} \leftarrow \mathbf{x_t} + \xi_t,",
                r"\xi_t \leftarrow \mathbb{B}_0(r)",
            )
            .next_to(pertubation_line_1, DOWN, buff=0.25)
            .align_to(pertubation_line_1, LEFT)
        )

        pertubation_group = VGroup(
            pertubation_condition, pertubation_line_1, pertubation_line_2
        )
        self.play(Write(loop_text, run_time=2))
        self.next_slide()

        self.play(Write(pertubation_group, run_time=2))
        self.next_slide()

        termination_condition = (
            Tex(
                r"If $t - t_{noise} = t_{thres}$ and $f(\mathbf{x_t}) - f(\mathbf{\tilde{x}_t}}) > -f_{thres}$ then:"
            )
            .next_to(pertubation_group, DOWN, buff=0.25)
            .align_to(pertubation_group, LEFT)
        )

        termination_return = (
            Tex(r"Return $\mathbf{\tilde{x}_{t_{noise}}}$")
            .next_to(termination_condition, DOWN, buff=0.25)
            .align_to(termination_condition, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )

        termination_group = VGroup(termination_condition, termination_return)

        self.play(Write(termination_condition), Write(termination_return), run_time=2)
        self.next_slide()

        descent = (
            Tex(
                r"$\mathbf{x_{t+1}} \leftarrow \mathbf{x_t} - \eta \nabla f(\mathbf{x_t})$"
            )
            .next_to(termination_return, DOWN, buff=0.25)
            .align_to(termination_condition, LEFT)
        )
        self.play(Write(descent), run_time=2)
        self.next_slide()

        pertubation_brace = Brace(pertubation_group, RIGHT, color=YELLOW)
        pertubation_brace_text = Tex(
            r"Add a small amount of noise\\every $t_{noise}$ steps,\\when the gradient is small",
            color=YELLOW,
        ).next_to(pertubation_brace, RIGHT, buff=0.25)

        self.play(Write(pertubation_brace), Write(pertubation_brace_text), run_time=2)
        self.next_slide()

        convergence_brace = Brace(termination_group, RIGHT, color=YELLOW)
        convergence_brace_text = Tex(
            r"Terminate when the function\\has not decreased enough\\ (converged)",
            color=YELLOW,
        ).next_to(convergence_brace, RIGHT, buff=0.25)

        self.play(Write(convergence_brace), Write(convergence_brace_text), run_time=2)
        self.next_slide()

        gradient_brace = Brace(descent, RIGHT, color=BLUE)
        gradient_brace_text = Tex(
            r"Take a regular gradient step every iteration",
            color=BLUE,
        ).next_to(gradient_brace, RIGHT, buff=0.25)

        self.play(Write(gradient_brace), Write(gradient_brace_text), run_time=2)
        self.next_slide()

        question = (
            Tex(r"\textbf{Does it still converge?}", color=GREEN)
            .next_to(descent, DOWN, buff=0.25)
            .align_to(title, LEFT)
        )
        self.play(Write(question), run_time=2)
        self.next_slide()

        ball_box = SurroundingRectangle(pertubation_line_2[1], color=GREEN)
        self.play(
            Create(ball_box),
            pertubation_line_2[1].animate.set_color(GREEN),
            run_time=2,
        )
        self.next_slide()


class Theorem3(Slide):
    """
    State that from here on out, we assume that f is l-smooth and rho-hessian lipschitz.

    State theorem 3, and highlight the difference parts of the term (original and new log factor).

    Argue that
    """

    def construct(self):
        theorem_3_title = Tex(
            r"Theorem 3 (PGD $\epsilon$-stationary)", color=BLUE
        ).to_corner(UL)
        self.play(Write(theorem_3_title))
        self.next_slide()

        theorem_3_statement = Tex(
            r"""
            For $f: \mathbb{R}^2 \to \mathbb{R}$ $\ell$-smooth and $\rho$-Hessian Lipschitz, 
            then we can choose $\delta, \epsilon, \Delta_f, c$ such that $PGD(\mathbf{x_0}, \ell, \rho, \epsilon, c, \delta, \Delta_f)$ finds a
            $\epsilon$-second-order stationary point with probability $1 - \delta$ in iterations:
            """,
            tex_environment=None,
        )

        place_below(theorem_3_statement, theorem_3_title)

        self.play(Write(theorem_3_statement), run_time=3)
        self.next_slide()

        theorem_3_iterations = MathTex(
            r"O \left( ",
            r"\frac{\ell (f(\mathbf{x_0}) - f^*)}{\epsilon^2}",
            r"\log^4 \frac{d \ell \Delta_f}{\epsilon^2 \delta}",
            r" \right)",
        ).next_to(theorem_3_statement, DOWN, buff=0.25)

        self.play(Write(theorem_3_iterations), run_time=2)
        self.next_slide()

        # Place a bracket around the gold standard runtime
        gold_standard_bracket = Brace(theorem_3_iterations[1], DOWN, color=YELLOW)
        gold_standard_text = Tex(r"\textbf{Gold Standard}", color=YELLOW).next_to(
            gold_standard_bracket, DOWN, buff=0.25
        )

        self.play(Write(gold_standard_bracket), Write(gold_standard_text), run_time=2)
        self.next_slide()

        # Place another bracket around the new log factor
        new_log_factor_bracket = Brace(theorem_3_iterations[2], DOWN, color=GREEN)
        new_log_factor_text = Tex(r"\textbf{New Log Factor}", color=GREEN).next_to(
            new_log_factor_bracket, DOWN, buff=1
        )

        self.play(Write(new_log_factor_bracket), Write(new_log_factor_text), run_time=2)
        self.next_slide()


class Theorem3ProofSketch(Slide):
    """
    Give the theorem proof sketch, with different cases for

    End with statement of lemma 10.
    """

    def construct(self):
        INDENT_WIDTH = 0.5

        header = Tex(r"Theorem 3 (Intuition)", color=BLUE).to_corner(UL)
        self.play(Write(header))
        self.next_slide()

        cases_header = (
            Tex(
                r"For iterate $\mathbf{x_t}$, if we have not converged, then either:",
                tex_environment=None,
            )
            .next_to(header, DOWN, buff=0.25)
            .align_to(header, LEFT)
        )

        cases_1 = (
            Tex(
                r"(1) the gradient $\nabla f(\mathbf{x_t})$ is large",
                tex_environment=None,
            )
            .next_to(cases_header, DOWN, buff=0.25)
            .align_to(cases_header, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )
        cases_2 = (
            Tex(
                r"(2) the Hessian $\nabla^2 f(\mathbf{x_t})$ has a significant negative eigenvalue",
                tex_environment=None,
            )
            .next_to(cases_1, DOWN, buff=0.25)
            .align_to(cases_1, LEFT)
        )

        self.play(Write(cases_header))
        self.next_slide()

        self.play(Write(cases_1))
        self.next_slide()

        self.play(Write(cases_2))
        self.next_slide()

        self.play(cases_2.animate.to_edge(DOWN), run_time=2)

        lemma_9 = (
            Tex(
                r"\textbf{Lemma.} For every iteration gradient descent with stepsize $\eta < \frac{1}{\ell}$:",
                tex_environment=None,
                color=GREEN,
            )
            .next_to(cases_1, DOWN, buff=0.25)
            .align_to(cases_1, LEFT)
        )
        self.play(Write(lemma_9))
        self.next_slide()

        lemma_9_proof = (
            MathTex(
                r"""
            f(\mathbf{x_{t+1}}) &\leq f(\mathbf{x_t}) + \nabla f(\mathbf{x_t})^T (\mathbf{x_{t+1}} - \mathbf{x_t}) + \frac{\ell}{2} ||\mathbf{x_{t+1}} - \mathbf{x_t}|| \\
                &= f(\mathbf{x_t}) - \eta || \nabla f(\mathbf{x_t})||^2 + \frac{\eta^2 \ell}{2} || \nabla f(\mathbf{x_t})||^2 \\
                &\leq f(\mathbf{x_t}) - \frac{\eta}{2}||\nabla f(\mathbf{x_t})||^2
            """,
                tex_environment="align",
            )
            .next_to(lemma_9, DOWN, buff=0.25)
            .center()
        )
        self.play(Write(lemma_9_proof), run_time=2)
        self.next_slide()

        progress = Tex(
            r"\textbf{Makes progress in function value!}", color=GREEN
        ).next_to(lemma_9_proof, DOWN, buff=0.25)
        self.play(Write(progress))
        self.next_slide()

        checkmark_1 = Tex(r"$\checkmark$", color=GREEN).next_to(
            cases_1, RIGHT, buff=0.25
        )

        self.play(
            FadeOut(lemma_9),
            FadeOut(lemma_9_proof),
            FadeOut(progress),
            Write(checkmark_1),
            cases_1.animate.set_color(GREEN),
            run_time=2,
        )
        self.play(
            cases_2.animate.next_to(cases_1, DOWN, buff=0.25).align_to(cases_1, LEFT),
            run_time=2,
        )
        self.next_slide()

        saddle_idea = (
            Tex(
                r"Idea: When adding pertubation $\xi_t \leftarrow \mathbb{B}_0(r)$, we want to \textit{make progress away from the saddle point} with high probability.",
                tex_environment=None,
            )
            .next_to(cases_2, DOWN, buff=0.25)
            .align_to(cases_2, LEFT)
        )

        self.play(Write(saddle_idea), run_time=2)
        self.next_slide()

        ball_idea = (
            Tex(
                r"Treat the pertubation as a $d$-dimensional \textbf{pertubation ball} $\mathbb{B}_{\mathbf{x}}(r)$.\\",
                r"Separate the volume into two regions: $\chi_{stuck}, \chi_{escape}$.\\",
                r"As long as we can get out of $\chi_{stuck}$ with high probability, then we can escape the saddle point efficiently!",
                tex_environment=None,
                color=GREEN,
            )
            .next_to(saddle_idea, DOWN, buff=0.25)
            .align_to(saddle_idea, LEFT)
        )

        self.play(Write(ball_idea[0]), run_time=2)
        self.play(Write(ball_idea[1]), run_time=2)
        self.play(Write(ball_idea[2]), run_time=2)
        self.next_slide()

        lemma_11 = (
            Tex(
                r"\textbf{Lemma (Paraphrase)}. The region of $\chi_{stuck}$ has ``width'' bounded by $\frac{\delta r}{2 \sqrt{d}}$.",
                tex_environment=None,
                color=BLUE,
            )
            .next_to(ball_idea, DOWN, buff=0.25)
            .align_to(ball_idea, LEFT)
        )
        self.play(Write(lemma_11), run_time=2)
        self.next_slide()


class PertubationBall(ThreeDSlide):
    """
    Give the pertubation ball visual, and results from the appendix for the integral and why it must be bounded in this way.

    This is a proof sketch of lemma 10.
    """

    def construct(self):
        BALL_RADIUS = 2

        axes = ThreeDAxes()
        x_0 = Dot3D(
            radius=0.1,
            color=BLUE,
        ).move_to(ORIGIN)

        self.set_camera_orientation(zoom=0.5)
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1)

        x_0_label = MathTex(r"\mathbf{x_0}").next_to(x_0, DOWN, buff=0.25)

        self.play(Create(x_0))
        self.add_fixed_orientation_mobjects(x_0_label)
        self.next_slide()

        ball = Sphere(
            radius=BALL_RADIUS, color=BLUE, resolution=(20, 20), fill_opacity=0.15
        )
        self.play(Create(ball), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(5)

        stuck_surface_bottom = Surface(
            lambda theta, r: axes.c2p(
                r * np.cos(theta),
                r * np.sin(theta),
                0.5 * np.sin(theta) - 0.1,
            ),
            resolution=(20, 20),
            u_range=[0, 2 * PI],
            v_range=[0, BALL_RADIUS],
            fill_opacity=0.2,
            fill_color=RED,
            stroke_color=RED,
            checkerboard_colors=None,
        )

        stuck_surface_top = stuck_surface_bottom.copy().shift(OUT * 0.2)
        self.play(Create(stuck_surface_bottom), Create(stuck_surface_top), run_time=3)
        self.wait(5)

        self.stop_ambient_camera_rotation()
        self.next_slide()


class PertubationBallProof(Slide):
    def construct(self):
        bound = Tex("Bounding the Stuck Region", color=BLUE).to_corner(UL)
        self.play(Write(bound), run_time=2)
        self.next_slide()

        vol_1 = MathTex(
            r"\text{Vol}(\chi_{stuck})",
            r"=",
            r"\int_{\mathbb{B}_{\tilde{\mathbf{x}}}^{(d)}(r)} d\mathbf{x} \cdot ",
            r"I_{\chi_{stuck}}(\mathbf{x})",
        )

        self.play(Write(vol_1))
        self.next_slide()

        # Put a surrounding rectangle around the last term
        vol_1_rect = SurroundingRectangle(vol_1[3], color=YELLOW)
        self.play(Create(vol_1_rect), run_time=1)
        self.next_slide()
        self.play(FadeOut(vol_1_rect), run_time=1)
        self.next_slide()

        vol_2 = MathTex(
            r"\text{Vol}(\chi_{stuck})",
            r"=",
            r"\int_{\mathbb{B}_{\tilde{\mathbf{x}}}^{(d-1)}(r)} d\mathbf{x}^{(-1)} \cdot ",
            r"\left(\text{dimension d component of } I_{\chi_{stuck}}(\mathbf{x})\right)",
        )
        self.play(vol_1.animate.become(vol_2), run_time=2)
        self.next_slide()

        vol_3 = MathTex(
            r"\text{Vol}(\chi_{stuck})",
            r"\leq",
            r"\int_{\mathbb{B}_{\tilde{\mathbf{x}}}^{(d-1)}(r)} d\mathbf{x}^{(-1)} \cdot ",
            r"\frac{\delta r}{\sqrt{d}}",
        )
        self.play(vol_1.animate.become(vol_3), run_time=2)
        self.next_slide()

        vol_4 = MathTex(
            r"\text{Vol}(\chi_{stuck})",
            r"\leq",
            r"\text{Vol}(\mathbb{B}_0^{(d-1)}(r)) \times ",
            r"\frac{\delta r}{\sqrt{d}}",
        )
        self.play(vol_1.animate.become(vol_4))
        self.next_slide()

        probability = MathTex(
            r"P(\text{escape}) = 1 - \frac{\text{Vol}(\chi_{stuck})}{\text{Vol}(\mathbb{B}_{\tilde{\mathbf{x}}}^{(d)}(r))} \geq 1 - \delta \left( \frac{r}{\sqrt{d}} \frac{\text{Vol}(\mathbb{B}_0^{(d-1)}(r))}{\text{Vol}(\mathbb{B}_0^{(d)}(r))}\right) \geq",
            r"1 - \delta",
        ).next_to(vol_1, DOWN, buff=0.25)

        self.play(Write(probability), run_time=2)
        self.next_slide()

        # Put a brace around the 1 - delta
        probability_brace = Brace(probability[1], DOWN, color=GREEN)
        probability_brace_text = Tex(
            r"Escape $\chi_{stuck}$ with \\high probability!",
            color=GREEN,
        ).next_to(probability_brace, DOWN, buff=0.25)

        self.play(Write(probability_brace), Write(probability_brace_text), run_time=2)
        self.next_slide()


class Theorem3Conclusion(Slide):
    """
    Bring the results together from the pertubation example to conclude that theorem 3 is correct.
    """

    def construct(self):
        INDENT_WIDTH = 0.5

        header = Tex(r"Theorem 3 (Intuition)", color=BLUE).to_corner(UL)
        self.play(Write(header))
        self.next_slide()

        cases_header = (
            Tex(
                r"For iterate $\mathbf{x_t}$, if we have not converged, then either:",
                tex_environment=None,
            )
            .next_to(header, DOWN, buff=0.25)
            .align_to(header, LEFT)
        )

        cases_1 = (
            Tex(
                r"(1) the gradient $\nabla f(\mathbf{x_t})$ is large $\checkmark$",
                tex_environment=None,
                color=GREEN,
            )
            .next_to(cases_header, DOWN, buff=0.25)
            .align_to(cases_header, LEFT)
            .shift(RIGHT * INDENT_WIDTH)
        )
        cases_2 = (
            Tex(
                r"(2) the Hessian $\nabla^2 f(\mathbf{x_t})$ has a significant negative eigenvalue",
                tex_environment=None,
            )
            .next_to(cases_1, DOWN, buff=0.25)
            .align_to(cases_1, LEFT)
        )
        self.play(Write(cases_header), Write(cases_1), Write(cases_2), run_time=1)
        self.next_slide()

        checkmark_2 = Tex(r"$\checkmark$", color=GREEN).next_to(
            cases_2, RIGHT, buff=0.25
        )

        self.play(Write(checkmark_2), cases_2.animate.set_color(GREEN), run_time=2)
        self.next_slide()

        conclusion = (
            Tex(
                r"PGD can find an $\epsilon$-second-order stationary point with only $\tilde{O}(\log^4 (d))$ overhead!",
                color=YELLOW,
                tex_environment=None,
            )
            .next_to(cases_2, DOWN, buff=2)
            .align_to(cases_2, LEFT)
        )
        self.play(Write(conclusion), run_time=2)
        self.next_slide()


class Corollary4(Slide):
    """
    Explain the strict saddle point assumption, the 3 possible cases, and why selecting values tells us that when PGD terminats,
    we must be at a local minimum specifically.
    """

    def construct(self):
        leading_question = Tex(
            r"\textbf{Can we do better? Find a local \textit{local minimum}?}",
            color=BLUE,
        ).to_corner(UL)

        self.play(Write(leading_question))
        self.next_slide()

        strict_saddle = (
            Tex("Definition (Strict Saddle). ", color=BLUE)
            .next_to(leading_question, DOWN, buff=0.25)
            .align_to(leading_question, LEFT)
        )
        self.play(Write(strict_saddle))
        self.next_slide()

        strict_saddle_def = (
            Tex(
                r"A function $f$ is $(\theta, \gamma, \zeta)$-strict saddle if for any $\mathbf{x}$, one of the following holds:",
                tex_environment=None,
            )
            .next_to(strict_saddle, DOWN, buff=0.25)
            .align_to(strict_saddle, LEFT)
        )
        self.play(Write(strict_saddle_def))

        options = MathTex(
            r"||\nabla f(\mathbf{x})|| \geq \theta",
            r",",
            r"\lambda_{min}(\nabla^2 f(\mathbf(x))) \leq -\gamma",
            r",",
            r"\mathbf{x} \text{ is } \zeta-\text{close to } \chi^*",
            tex_environment="equation*",
        ).next_to(strict_saddle_def, DOWN, buff=0.25)

        self.play(Write(options))
        self.next_slide()

        pgd_group = VGroup(options[0], options[2])
        # Put a brace around the group
        pgd_brace = Brace(pgd_group, DOWN, color=YELLOW)
        pgd_brace_text = Tex(
            r"Can choose $\theta, \gamma$ such that \\ PGD terminates with these false.",
            color=YELLOW,
        ).next_to(pgd_brace, DOWN, buff=0.25)

        self.play(Write(pgd_brace), Write(pgd_brace_text))
        self.next_slide()

        # put a brace around the last option and say "must be true at \\ end of PGD!"
        last_brace = Brace(options[4], DOWN, color=GREEN)
        last_brace_text = Tex(r"Must be true \\at end of PGD!", color=GREEN).next_to(
            last_brace, DOWN, buff=0.25
        )

        self.play(Write(last_brace), Write(last_brace_text))
        self.next_slide()

        final_result = Tex(
            r"\textbf{Strict Saddle} $\implies$ \textbf{PGD finds \textit{Local Minimum}}!",
            color=GREEN,
        ).move_to((0, -2, 0))

        self.play(Write(final_result))
        self.next_slide()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.next_slide()

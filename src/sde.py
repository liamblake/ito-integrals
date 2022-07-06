from manim import *


def u(x, y, t):
    pass


class CreateDeterministic(Scene):
    def construct(self):
        title = MathTex(r"\mathrm{d}x_t = u\left(x_t, t\right)\mathrm{d}t")
        self.add(title)

        self.play(Write(title))

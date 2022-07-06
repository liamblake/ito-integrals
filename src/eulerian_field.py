import numpy as np
from manim import *

A = 1
c1 = 0.5
k1 = 1
c2 = np.pi
k2 = 1
l2 = 2
eps = 0.3

rossby_x = (
    lambda x, y, t: c1
    - A * np.sin(k1 * x) * np.cos(y)
    + eps * l2 * np.sin(k2 * (x - c2 * t)) * np.cos(l2 * y)
)
rossby_y = lambda x, y, t: A * k1 * np.cos(k1 * x) * np.sin(y) - eps * k2 * np.cos(
    k2 * (x - c2 * t)
) * np.sin(l2 * y)


class Eulerian(Scene):
    def construct(self):
        self.camera.frame_center = [10, 0]

        func = lambda t: (
            lambda pos: rossby_x(pos[0], pos[1], t) * RIGHT
            + rossby_y(pos[0], pos[1], t) * UP
        )
        vector_field = ArrowVectorField(
            func(0),
            x_range=[0, 20, 0.5],
            y_range=[-5, 5, 0.5],
            length_func=lambda x: x / 5,
        )
        self.add(vector_field)

        for t in np.arange(1, 4, 1):
            new_field = ArrowVectorField(
                func(t),
                x_range=[0, 20, 0.5],
                y_range=[-5, 5, 0.5],
                length_func=lambda x: x / 5,
            )
            self.play(vector_field.animate.become(new_field))
            vector_field = new_field

            self.wait()

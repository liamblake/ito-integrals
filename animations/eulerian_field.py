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
        # self.camera.frame_center = [10, 0]

        vector_field = self.get_vector_field(0)
        self.t = 0

        def update_vector_field(vector_field, dt):
            self.t += 1
            new_field = self.get_vector_field(self.t)
            Transform(vector_field, new_field)
            vector_field.func = new_field.func

        vector_field.add_updater(update_vector_field)
        self.add(vector_field)
        self.wait(1)

    def get_vector_field(self, t):
        func = (
            lambda pos, t=t: rossby_x(pos[0], pos[1], t) * RIGHT
            + rossby_y(pos[0], pos[1], t) * UP
        )
        self.vector_field = ArrowVectorField(func)
        return self.vector_field

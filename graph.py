from manim import *
from math import ceil
class garps(Scene):
    def construct(self):
        ax = Axes(x_range=[-1, ceil(TAU)+1], y_range=[-2, 2])
        t1 = MathTex("y = sin(x)").scale(0.5).to_edge(UP)
        self.play(Create(ax))
        self.wait()
        grap = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, TAU])
        self.play(Create(grap),run_time=1.5, rate_func=linear)
        self.wait()
        d1 = Dot(ax.coords_to_point(PI, 0))
        l1 = MathTex("x = \\pi \\: rad").scale(0.5).next_to(d1, UR)
        d2 = Dot(ax.coords_to_point(TAU, 0))
        l2 = MathTex("x = 2\\pi \\: rad").scale(0.5).next_to(d2, DR)
        self.play(Create(d1), Create(d2), Write(l1), Write(l2))
        self.wait()
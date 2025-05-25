from manim import *

class wikiThing(Scene):
    def construct(self):
        axi = Axes(x_range=(-1.5,1.5), y_range=(-1.5,1.5), x_length=5, y_length=5, tips=False).center()
        circle = Circle(radius=axi.get_x_unit_size(), color=BLUE).center()
        centreDot = Dot(circle.get_center(), color=RED)
        basePoint = ValueTracker(1)
        angle = 1
        dot1 = always_redraw(lambda: Dot(axi.coords_to_point(np.cos(basePoint.get_value()),np.sin(basePoint.get_value())), color=RED))
        dot2 = always_redraw(lambda: Dot(axi.coords_to_point(np.cos(basePoint.get_value() - angle),np.sin(basePoint.get_value() - angle)), color=RED))
        arc = always_redraw(lambda: ArcBetweenPoints(dot2.get_center(), dot1.get_center(),radius=axi.get_x_unit_size(), color=RED))
        self.add(centreDot,dot1,dot2,axi,circle,arc)
        self.wait()
        self.play(
            basePoint.animate.increment_value(1),
            Create(ArcBetweenPoints(dot2.get_center(), dot1.get_center(),radius=axi.get_x_unit_size(), color=GREEN)),
            run_time=1
        )
        self.wait()
        self.play(
            basePoint.animate.increment_value(1),
            Create(ArcBetweenPoints(dot2.get_center(), dot1.get_center(),radius=axi.get_x_unit_size(), color=GREEN)),
            run_time=1
        )
        self.wait()
        
        
        
        self.wait(2)
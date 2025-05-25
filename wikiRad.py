from manim import *
# https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Circle_radians.gif/375px-Circle_radians.gif
class wikiThing(Scene):
    def construct(self):
        axi = Axes(x_range=(-1.5,1.5),y_range=(-1.5,1.5),x_length=5,y_length=5, tips=False).center()
        
        self.add(axi)
        
        cdot = Dot(axi.coords_to_point(0,0),color=WHITE)
        ldot = Dot(ORIGIN,color=RED)
        outerDot = Dot(cdot.get_center(),color=RED)
        radi = always_redraw(lambda: Line(ldot.get_center(),outerDot.get_center(),color=RED))
        self.add(cdot,ldot,outerDot,radi)
        self.wait(0.5)
        self.play(
            outerDot.animate.move_to(axi.coords_to_point(1,0)),
            rate_functions = linear,
            run_time = 0.5,
        )
        self.wait()
        circle = Circle(radius=axi.get_x_unit_size(),color=BLUE).center()
        self.play(
            Create(circle),
            Rotate(outerDot,angle=TAU,about_point=ORIGIN),
            run_time=0.5,
            rate_functions=linear
        )
        self.wait()
        rTex = MathTex("r",color=RED).next_to(radi,UP)
        self.play(
            FadeIn(rTex),
            run_time=0.5
        )
        self.wait()
        self.play(
            FadeOut(rTex),
            run_time=0.5
        )
        self.wait()
        self.play(
            Rotate(ldot,angle=-PI/2,about_point=outerDot.get_center()),
            run_time=0.5
        )
        self.wait()
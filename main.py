from manim import *

class scenify(Scene):
    def construct(self):
        print(config.frame_width, config.frame_height)
        circle = Circle(radius=1, color=WHITE)
        plane = NumberPlane()
        self.play(Create(circle))
        self.wait(0.5)
        self.play(FadeIn(plane), run_time = 0.5)
        
        rad = Line(circle.get_center(),circle.get_right(),color=RED)
        cent = Dot(circle.get_center())
        self.play(
            Create(rad),FadeIn(cent)
        )
        t1 = Text("Radius: 1", color=WHITE).scale(0.3)
        t1.move_to(rad.get_center())
        t1.set_y(rad.get_y()+t1.height)
        t2 = Text("Center: (0,0)", color=WHITE).scale(0.3)
        t2.move_to(cent.get_center())
        t2.set_y(circle.get_y()-t2.height)
        piTracker = ValueTracker(0)
        circText = always_redraw(lambda: 
            MathTex("Circumference = ",f"{np.round(piTracker.get_value(),4)}")
            .scale(0.7)
            .to_corner(UR)
            )
        
        self.play(
            Write(t1),Write(t2)
        )
        
        self.play(
            Unwrite(t1),Unwrite(t2),Write(circText)
        )
        self.play(FadeOut(plane), run_time=0.5)
        self.play(
            Rotate(rad, angle=TAU, about_point=circle.get_center()),
            piTracker.animate.set_value(TAU),
            run_time=2,
        )
        self.wait()

        
        self.play(
            Uncreate(rad),
            Uncreate(cent),
            Uncreate(circle),
        )
        circText_static = MathTex("Circumference =", "6.2832").scale(0.7)
        circText_static.move_to(circText.get_center())
        self.remove(circText)  
        self.add(circText_static)
        self.play(circText_static.animate.move_to(ORIGIN))
        circText_static.move_to(ORIGIN)
        self.wait()

        
        newCircText = MathTex("Circumference =", "6.2832", "= 2\\pi").scale(0.7)
        newCircText.move_to(circText_static.get_center())
        self.play(TransformMatchingTex(circText_static, newCircText))
        self.wait()

        nextCircText = MathTex("Circumference =", "2\\pi").scale(0.7)
        nextCircText.move_to(newCircText.get_center())
        self.play(TransformMatchingTex(newCircText, nextCircText))
        self.wait()
        self.play(Unwrite(nextCircText),run_time = 0.8)
        self.wait()
        t1 = MathTex("Circumference =", " \\pi", "\\times", " d").scale(0.7)
        t2 = MathTex("Circumference =", " \\pi", " \\times", " 2r").scale(0.7)
        backupt2 = MathTex("d = 2r").scale(0.7).next_to(t2,UP)
        t3 = MathTex("Circumference =", " 2\\pi", " \\times", " r").scale(0.7)
        t4 = MathTex("Circumference = ", "2\\pi", " \\times", " 1").scale(0.7)
        t5 = MathTex("Circumference = ", "2\\pi").scale(0.7)
        self.play(Write(t1))
        self.wait()
        self.play(Write(backupt2))
        self.play(TransformMatchingTex(t1, t2))
        self.wait()
        self.play(Unwrite(backupt2), run_time = 0.5)
        self.play(TransformMatchingTex(t2, t3))
        self.wait()
        self.play(TransformMatchingTex(t3, t4))
        self.wait()
        self.play(TransformMatchingTex(t4, t5))
        self.wait()
        self.play(Unwrite(t5))
        self.wait()
        
        
        
        

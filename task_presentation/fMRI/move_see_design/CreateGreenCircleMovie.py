from manim import * 

config.background_color = GRAY

class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(color=GREEN).scale(2.5)
        circle.set_fill(GREEN, opacity=.6)
        
        self.play(GrowFromCenter(circle), run_time=2.0)

from manim import *

class SquareToCircle(Scene):
    def construct(self):
        s = Square()
        c = Circle()
        self.play(Create(s))
        self.play(Transform(s, c))
        self.play(FadeOut(s))

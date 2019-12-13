import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 2.5
        self.dy = 2.5
        self.last_dx = 0
        self.last_dy = 0
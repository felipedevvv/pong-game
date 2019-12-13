import turtle


class Button(turtle.Turtle):

    def __init__(self, gotoX, gotoY):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(gotoX, gotoY)
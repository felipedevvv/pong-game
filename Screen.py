import turtle


class Screen:
    def __init__(self, gameManager):
        self.gameManager = gameManager
        self.p1 = self.gameManager.p1
        self.p2 = self.gameManager.p2
        self.left_paddle = self.gameManager.left_paddle
        self.right_paddle = self.gameManager.right_paddle
        self.display = turtle.Screen()
        self.display.title("Pong Xtreme")
        self.display.bgcolor("black")
        self.display.setup(width=800, height=600)
        self.display.tracer(0)
        self.reset = False
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("{}: {}  ||  {}: {}".format(self.p1.username, self.p1.score, self.p2.username,
                                                   self.p2.score), align="center", font=("Courier", 24, "normal"))
        self.display.listen()
        self.display.onkey(self.gameManager.paddle_L_Up, "w")
        self.display.onkey(self.gameManager.paddle_L_Up, "W")
        self.display.onkey(self.gameManager.paddle_L_Down, "s")
        self.display.onkey(self.gameManager.paddle_L_Down, "S")
        self.display.onkey(self.gameManager.paddle_R_Up, "Up")
        self.display.onkey(self.gameManager.paddle_R_Down, "Down")
        self.display.onkey(self.gameManager.pause_game, "p")
        self.display.onkey(self.gameManager.pause_game, "P")
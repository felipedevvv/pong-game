# Pong Xtreme
"""
    Game of Pong Manager
"""
import turtle
import time
from pygame import mixer
from Player import *
from Paddle import *
from Ball import *
from Screen import *


class PongGameManager:

    def __init__(self):
        self.p1 = Player("Player 1")
        self.p2 = Player("Player 2")
        self.ball = Ball()
        self.left_paddle = Paddle(-350, 0)
        self.right_paddle = Paddle(350, 0)
        self.screen = Screen(self)
        self.playGame = True
        self.play()

    def paddle_L_Up(self):
        y = self.left_paddle.ycor()
        y += 30
        self.left_paddle.sety(y)
        if self.left_paddle.ycor() > 300:
            self.left_paddle.sety(-300)

    def paddle_L_Down(self):
        y = self.left_paddle.ycor()
        y -= 30
        self.left_paddle.sety(y)
        if self.left_paddle.ycor() < -300:
            self.left_paddle.sety(300)


    def paddle_R_Up(self):
        y = self.right_paddle.ycor()
        y += 30
        self.right_paddle.sety(y)
        if self.right_paddle.ycor() > 300:
            self.right_paddle.sety(-300)


    def paddle_R_Down(self):
        y = self.right_paddle.ycor()
        y -= 30
        self.right_paddle.sety(y)
        if self.right_paddle.ycor() < -300:
            self.right_paddle.sety(300)

    def pause_game(self):
        if self.playGame:
            self.ball.last_dx = self.ball.dx
            self.ball.last_dy = self.ball.dy
            self.ball.dx = 0
            self.ball.dy = 0
        else:
            self.ball.dx = self.ball.last_dx
            self.ball.dy = self.ball.last_dy
        self.playGame = not self.playGame

    def play(self):
        while True:
            self.screen.display.update()
            if self.screen.reset:
                self.screen.reset = False
                time.sleep(1)

            # Move Ball
            self.ball.setx(self.ball.xcor() + self.ball.dx)
            self.ball.sety(self.ball.ycor() + self.ball.dy)

            # Top Border
            if self.ball.ycor() > 290:
                self.ball.sety(290)
                self.ball.dy *= -1
                # Bottom Border
            elif self.ball.ycor() < -280:
                self.ball.sety(-280)
                self.ball.dy *= -1

                # Right Border
            if self.ball.xcor() > 380:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.left_paddle.goto(-350, 0)
                self.right_paddle.goto(350, 0)
                self.p1.score += 1
                self.screen.pen.clear()
                self.screen.pen.write("{}: {}  ||  {}: {}".format(self.p1.username, self.p1.score, self.p2.username, self.p2.score), align="center",
                          font=("Courier", 24, "normal"))
                self.screen.reset = True
                # Left Border
            elif self.ball.xcor() < -390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.left_paddle.goto(-350, 0)
                self.right_paddle.goto(350, 0)
                self.p2.score += 1
                self.screen.pen.clear()
                self.screen.pen.write("{}: {}  ||  {}: {}".format(self.p1.username, self.p1.score, self.p2.username, self.p2.score), align="center",
                          font=("Courier", 24, "normal"))
                self.screen.reset = True

                # Bounce Left Paddle
            if (-340 < self.ball.xcor() < -330
                    and (self.ball.ycor() + 10) > (self.left_paddle.ycor() - 50)
                    and (self.ball.ycor() - 10) < (self.left_paddle.ycor() + 50)):
                self.ball.setx(-330)
                self.ball.dx *= -1

                # Bounce Right Paddle
            if (330 < self.ball.xcor() < 340
                    and (self.ball.ycor() + 10) > (self.right_paddle.ycor() - 50)
                    and (self.ball.ycor() - 10) < (self.right_paddle.ycor() + 50)):
                self.ball.setx(330)
                self.ball.dx *= -1

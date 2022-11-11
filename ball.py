from turtle import Turtle
import random

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
color = (r, g, b)
MOVE = 14.14

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.setheading(135)
        self.goto(0, 0)
        self.penup()

    def move(self):
        self.forward(MOVE)

    def collide_wall(self):
        new_heading = - self.heading()
        self.setheading(new_heading)

    def collide_paddle(self):
        new_heading = - self.heading() + 180
        self.setheading(new_heading)

    def reset(self):
        self.setheading(135)
        self.goto(0, 0)
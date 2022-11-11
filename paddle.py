from turtle import Turtle
import random

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
color = (r, g, b)

class Paddle(Turtle):

    def __init__(self, x_and_y):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_and_y)

    def up(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y + 20)

    def down(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x, y - 20)
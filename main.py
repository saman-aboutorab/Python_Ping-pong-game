from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import random
import time
from score import Score

SPEED = 0.1

def background_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    screen.bgcolor(color)

screen = Screen()
screen.colormode(255)
screen.setup(800, 600)
background_change()
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')




game_on = True

while game_on:
    screen.update()
    ball.move()
    time.sleep(SPEED)
    y = ball.ycor()
    x = ball.xcor()

    if y > 280 or y < -280:
        ball.collide_wall()

    if x > 320 and ball.distance(r_paddle) < 50:
        ball.collide_paddle()
        SPEED -= 0.01
    if x < -320 and ball.distance(l_paddle) < 50:
        ball.collide_paddle()
        SPEED -= 0.01

    if x > 380:
        ball.reset()
        score.l_goal()
        SPEED = 0.1
        background_change()
    elif x < -380:
        ball.reset()
        score.r_goal()
        SPEED = 0.1
        background_change()
screen.exitonclick()
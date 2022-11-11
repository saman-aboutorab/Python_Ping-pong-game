from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 50, 'normal'))

    def l_goal(self):
        self.l_score += 1
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 50, 'normal'))

    def r_goal(self):
        self.r_score += 1
        self.clear()
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 50, 'normal'))
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 50, 'normal'))
from turtle import Turtle

class score:
    def __init__(self):
        self.left_point=0
        self.right_point=0
        self.left_score()
        self.right_score()

    def left_score(self):
        self.l_score=Turtle()
        self.l_score.color("white")
        self.l_score.speed('fastest')
        self.l_score.hideturtle()
        self.l_score.penup()
        self.l_score.goto(-30,230)
        self.left_score_update()

    def right_score(self):
        self.r_score = Turtle()
        self.r_score.color("white")
        self.r_score.speed('fastest')
        self.r_score.hideturtle()
        self.r_score.penup()
        self.r_score.goto(30, 230)
        self.right_score_update()

    def left_score_update(self):
        self.l_score.clear()
        self.l_score.write(self.left_point, align="center", font=('Arial', 50, 'normal'))
        self.left_point += 1

    def right_score_update(self):
        self.r_score.clear()
        self.r_score.write(self.right_point, align="center", font=('Arial', 50, 'normal'))
        self.right_point += 1



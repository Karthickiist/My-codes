from turtle import Turtle

class score:
    def __init__(self):
        self.points=0
        self.high_score=0
        with open("high_score.txt",'r') as f:
            self.high_score=int(f.read())
        self.score=Turtle()
        self.score.speed('fastest')
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, 330)
        self.score_update()

    def score_update(self):
        self.score.clear()
        self.score.write(f"Score: {self.points}, High Score: {self.high_score}", align='center', font=('Arial', 12, 'normal'))

    def game_is_over(self):
        if self.points > self.high_score:
            with open("high_score.txt",'w') as f:
                f.write(str(self.points))
        self.end = Turtle()
        self.end.speed('fastest')
        self.end.hideturtle()
        self.end.goto(0,0)
        self.end.write("GAME OVER ", align='center', font=('Arial', 20, 'normal'))
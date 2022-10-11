from turtle import Turtle
class Pedals:
    def __init__(self,x,y):
        self.pedal=Turtle('square')
        self.pedal.color('white')
        self.pedal.speed('fastest')
        self.pedal.penup()
        self.pedal.shapesize(5, 1)
        self.pedal.goto(x,y)



    def up(self):
        y_posi=self.pedal.ycor()+20
        self.pedal.goto(self.pedal.xcor(),y_posi)

    def down(self):
        y_posi=self.pedal.ycor()-20
        self.pedal.goto(self.pedal.xcor(),y_posi)

    def border_line(self):
        self.line=Turtle()
        self.line.color('white')
        self.line.hideturtle()
        self.line.penup()
        self.line.speed('fastest')
        self.line.goto(0,-350)
        while self.line.ycor()<=350:
            self.line.pendown()
            self.line.goto(0,self.line.ycor()+20)
            self.line.penup()
            self.line.goto(0, self.line.ycor() + 20)


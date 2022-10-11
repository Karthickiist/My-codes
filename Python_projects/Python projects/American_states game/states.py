from turtle import Turtle
class States:
    def __init__(self,state_name,x,y):
        self.state=Turtle()
        self.state.hideturtle()
        self.state.penup()
        self.state.goto(x,y)
        self.state.write(state_name,align='center',font=('Arial', 8, 'normal'))
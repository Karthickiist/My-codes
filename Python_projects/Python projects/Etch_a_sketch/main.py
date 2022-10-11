from turtle import Turtle, Screen

charlie=Turtle()
def forword():
    charlie.forward(10)
def backword():
    charlie.backward(10)
def right():
    charlie.right(10)
def left():
    charlie.left(10)


screen=Screen()
def clear():
    screen.resetscreen()
screen.listen()
screen.onkey(forword, 'w')
screen.onkey(backword, 's')
screen.onkey(right, 'd')
screen.onkey(left, 'a')
screen.onkey(clear, 'c')
screen.exitonclick()
import turtle

import colorgram
from turtle import Turtle,Screen
import random
turtle.colormode(255)
colors=colorgram.extract('image.png',30)
all_colors=[]
print(colors)
for i in range(len(colors)):
    rgp=colors[i].rgb
    tup=(rgp.r,rgp.g,rgp.b)
    all_colors.append(tup)

charlie=Turtle()
charlie.pensize(20)
charlie.penup()
x=-200
y=-200
charlie.goto(x,y)
for i in range(10):
    for i in range(10):
            charlie.dot(20, random.choice(all_colors))
            charlie.forward(50)
    y=y+50
    charlie.goto(x,y)
charlie.hideturtle()



screen=Screen()
screen.exitonclick()
import random
import turtle
from turtle import Turtle, Screen
screen=Screen()
screen.setup(500,300)
colors=['red', 'yellow', 'black', 'green', 'blue', 'orange']
turtles=[]
x=-230
y=-80
winner_bet=screen.textinput("BET THE GAME",f"On which turtle you are betting {colors}?: ")
winner_color=''
for i in range(6):
    charlie=Turtle('turtle')
    #charlie.speed('slowest')
    turtles.append(charlie)
    charlie.penup()
    charlie.color(colors[i])
    charlie.goto(x,y)
    y+=30

res=True
def winner():
    for i in turtles:
        if i.xcor()>=220:
            return i


while res:
    for i in turtles:
        i.forward(random.randint(1,10))

    if winner():
        res=False

winner_color=winner().fillcolor()
if winner_bet==winner_color:
    print("Congratzz!!! Your turtle won the game...")
else:
    print(f"Sorry..You lose. The winner is {winner_color} turtle.")
screen.exitonclick()
import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.shapesize(0.5)
        self.penup()
        self.shape('circle')
        self.goto(random.randint(-330, 330), random.randint(-330, 330))

    def move(self):
        self.goto(random.randint(-330, 330), random.randint(-330, 330))

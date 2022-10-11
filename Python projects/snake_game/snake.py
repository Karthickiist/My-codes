from turtle import Turtle
snake_speed=20

class Snake:
    def __init__(self):
        self.blocks = []
        self.createsnake()

    def createsnake(self):
        x=0
        y=0
        for i in range(3):
            block=Turtle('square')
            block.speed('fastest')
            block.penup()
            block.goto(x,y)
            x=x-20
            self.blocks.append(block)
        self.head=self.blocks[0]


    def move(self):
        for i in range(len(self.blocks)-1,0,-1):
            self.blocks[i].goto(self.blocks[i-1].pos())
        self.head.forward(snake_speed)

    def grow(self):
        last_block=len(self.blocks)-1
        go=self.blocks[last_block].pos()
        grows=Turtle('square')
        self.blocks.append(grows)
        grows.penup()
        grows.speed('fastest')
        grows.goto(go)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

import random
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import score

screen=Screen()
screen.setup(700,700)
screen.title("Karthick's Snake Game")
snakes=Snake()
foods=Food()
scores=score()
screen.tracer(0)

#snake control
screen.listen()
screen.onkey(snakes.up,'Up')
screen.onkey(snakes.down,'Down')
screen.onkey(snakes.right,'Right')
screen.onkey(snakes.left,'Left')


game_on=True
while game_on:
    screen.update()
    snakes.move()
    if snakes.head.distance(foods) <15:
        scores.points+=1
        scores.score_update()
        foods.move()
        snakes.grow()
    time.sleep(0.1)
    border1=340
    border2=-340
    if snakes.head.xcor()>border1 or snakes.head.xcor()<border2 or snakes.head.ycor()>border1 or snakes.head.ycor()<border2:
        game_on=False

    for i in snakes.blocks:
        if i != snakes.head:
            if snakes.head.distance(i)<5:
                game_on=False

scores.game_is_over()









screen.exitonclick()
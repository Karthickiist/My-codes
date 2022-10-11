from turtle import Screen
from pedals import Pedals
from ball import ball
import time

screen=Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title("Karthick's Pong game")


screen.tracer(0)
pedal_right=Pedals(350,0)
pedal_left=Pedals(-350,0)
ball=ball()



screen.listen()
screen.onkey(pedal_right.up,'Up')
screen.onkey(pedal_right.down,'Down')
screen.onkey(pedal_left.up,'w')
screen.onkey(pedal_left.down,'s')

pedal_left.border_line()
sleep_time=0.01

game_on=True
while game_on:
    ball.move()
    time.sleep(sleep_time)
    if ball.ball.ycor()>287 or ball.ball.ycor()<-287:
        ball.bounce()
    elif ball.ball.distance(pedal_right.pedal)<50 and ball.ball.xcor()>330:
        ball.pedal_bounce()
        ball.increase_speed()
    elif ball.ball.distance(pedal_left.pedal)<50 and ball.ball.xcor()<-330:
        ball.pedal_bounce()
        ball.increase_speed()
    ball.miss_check()
    screen.update()




screen.exitonclick()
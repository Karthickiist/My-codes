from turtle import Turtle
from scores import score
import time
class ball:
    def __init__(self):
        self.ball_speed=1
        self.scores=score()
        self.ball=Turtle('circle')
        self.ball.color('white')
        self.ball.penup()
        self.direction='straight'
        self.x_movement=self.ball_speed
        self.y_movement=self.ball_speed

    def move(self):
        x=self.ball.xcor()+self.x_movement
        y=self.ball.ycor()+self.y_movement

        self.ball.goto(x,y)

    def bounce(self):
        self.y_movement*=(-1)

    def pedal_bounce(self):
        self.x_movement*=(-1)

    def miss_check(self):
        if self.ball.xcor()>450:
            time.sleep(2)
            self.ball.goto(0,0)
            self.pedal_bounce()
            self.scores.left_score_update()
            self.initialize_speed()

        if self.ball.xcor()<-450:
            time.sleep(2)
            self.ball.goto(0,0)
            self.pedal_bounce()
            self.scores.right_score_update()
            self.initialize_speed()

    def increase_speed(self):
        if self.x_movement>0:
            self.x_movement+=0.5
        else:
            self.x_movement-=0.5
        if self.y_movement>0:
            self.y_movement+=0.5
        else:
            self.y_movement-=0.5

    def initialize_speed(self):
        if self.x_movement > 0:
            self.x_movement = self.ball_speed
        else:
            self.x_movement = -self.ball_speed
        if self.y_movement > 0:
            self.y_movement = self.ball_speed
        else:
            self.y_movement = -self.ball_speed



from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600, bg="black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)




screen.exitonclick()

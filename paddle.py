from turtle import Turtle
STRETCH_W = 5
STRETCH_L = 1
# X_POS_R = 350
DOWN = 270


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_right_paddle()
        self.create_left_paddle()

    def create_right_paddle(self):
        right_paddle = Turtle("square")
        right_paddle.turtlesize(stretch_len=STRETCH_L, stretch_wid=STRETCH_W)
        right_paddle.color("white")
        right_paddle.penup()
        right_paddle.goto(350, 0)

    def create_left_paddle(self):
        right_paddle = Turtle("square")
        right_paddle.turtlesize(stretch_len=STRETCH_L, stretch_wid=STRETCH_W)
        right_paddle.color("white")
        right_paddle.penup()
        right_paddle.goto(-350, 0)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

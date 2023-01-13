from turtle import Turtle
STRETCH_W = 5
STRETCH_L = 1
# X_POS_R = 350
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_len=STRETCH_L, stretch_wid=STRETCH_W)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

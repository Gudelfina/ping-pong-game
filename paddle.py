from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.shape('square')
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_first_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_first_paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
line = Turtle()
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Ping Pong")
screen.tracer(0)


line.penup()
line.goto(x=0, y=-280)
line.setheading(90)

for _ in range(29):
    line.hideturtle()
    line.color("white")
    line.pensize(5)
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(10)


screen.listen()
screen.onkey(paddle1.move_first_paddle_up, "Up")
screen.onkey(paddle1.move_first_paddle_down, "Down")

screen.onkey(paddle2.move_first_paddle_up, "w")
screen.onkey(paddle2.move_first_paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall (top, bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect out of bounds paddle1
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()

    # detect out of bounds paddle2
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()

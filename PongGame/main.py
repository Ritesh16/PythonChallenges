from turtle import Turtle, Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
score_board = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
       ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # when Right paddle missed ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # when Right paddle missed ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()
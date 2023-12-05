import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import  ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
game_is_on = True
def restart():
    snake.reset()
    scoreboard.update_scoreboard()
    game_is_on = True
    start_game(game_is_on)

def exit():
    turtle.Screen().bye()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(restart,"r")
screen.onkey(exit,"e")
def start_game(game_is_on):
    while(game_is_on):
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #    game_is_on = False
         #   scoreboard.game_over()

        snake.check_snake_touches_top()
        snake.check_snake_touches_right()
        snake.check_snake_touches_bottom()
        snake.check_snake_touches_left()

        for segment in snake.segments[1:]:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.reset()
                time.sleep(0.5)
                scoreboard.game_over()
                game_is_on = False

start_game(game_is_on)
screen.exitonclick()
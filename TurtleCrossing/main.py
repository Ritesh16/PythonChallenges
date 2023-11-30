from turtle import Turtle, Screen
import time

from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height= 600)
screen.bgcolor("white")

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect Finish Line Reach
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
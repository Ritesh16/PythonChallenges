import turtle
from turtle import Turtle, Screen

tim = Turtle()

#sample.shape("square")
#sample.shapesize(4, 4)

# drawing rectangle
for _ in range(4):
    tim.forward(100)
    tim.left(90)
screen = Screen()

# drawing dashed arrow line
line = Turtle()
for _ in range(15):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()

screen.exitonclick()


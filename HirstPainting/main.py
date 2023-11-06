import turtle

import colorgram
import turtle as hirst
import random

turtle.colormode(255)
colors = colorgram.extract('images/image.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

screen = hirst.Screen()
hirst.speed("fastest")
hirst.penup()
hirst.hideturtle()
hirst.setheading(225)
hirst.forward(300)
hirst.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    hirst.dot(20, random.choice(rgb_colors))
    hirst.forward(50)

    if dot_count % 10 == 0:
        hirst.setheading(90)
        hirst.setheading(90)
        hirst.forward(50)
        hirst.setheading(180)
        hirst.forward(500)
        hirst.setheading(0)


screen.exitonclick()
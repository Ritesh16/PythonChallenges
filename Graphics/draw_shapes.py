import turtle as t
import random

tim = t.Turtle()

colors= ["Red", "Blue", "Green", "Orange", "Yellow", "Wheat", "Gray"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(n)

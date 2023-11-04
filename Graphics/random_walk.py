import turtle as t
import random

walk = t.Turtle()
t.colormode(255)
walk.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rc = (r,g,b)
    return rc

directions = [0, 90, 270, 360]
walk.pensize(15)

for _ in range(30):
    rc = random_color()
    print(rc)
    walk.color(rc)
    walk.forward(25)
    walk.setheading(random.choice(directions))
import random
import turtle as t

circle = t.Turtle()
t.colormode(255)
circle.speed("fastest")
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    rc = (r,g,b)
    return rc

def draw_spirograph(size):
    for _ in range(int(360/size)):
        circle.color(random_color())
        circle.circle(100)
        circle.setheading(circle.heading() + size)

draw_spirograph(5)
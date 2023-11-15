from turtle import  Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def check_snake_touches_top(self):
        if self.head.ycor() > 280 and self.head.heading() == UP:
            x_cor = self.head.xcor()
            self.head.goto(x_cor, -280)

    def check_snake_touches_right(self):
        if self.head.xcor() > 280 and self.head.heading() == RIGHT:
            y_cor = self.head.ycor()
            self.head.goto(-280, y_cor)

    def check_snake_touches_bottom(self):
        if self.head.ycor() < -280 and self.head.heading() == DOWN:
            x_cor = self.head.xcor()
            self.head.goto(x_cor, 280)

    def check_snake_touches_left(self):
        if self.head.xcor() < -280 and self.head.heading() == LEFT:
            y_cor = self.head.ycor()
            self.head.goto(280, y_cor)
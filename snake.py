from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle(shape="square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(FORWARD_DISTANCE)

    def move_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
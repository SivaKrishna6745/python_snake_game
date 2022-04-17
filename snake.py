from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
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
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def move(self):
        for seg_no in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_no - 1].xcor()
            new_y = self.segments[seg_no - 1].ycor()
            self.segments[seg_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def up(self):
        if self.last_input != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_input != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.last_input != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.last_input != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

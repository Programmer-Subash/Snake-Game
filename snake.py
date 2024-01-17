from turtle import Turtle, Screen


class Snake:

    def __init__(self, color="black"):
        self.color = color
        self.segments = []
        self.distance = 20

    def create_snake(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color(self.color)
        snake.penup()
        snake.goto(position)
        snake.penup()
        self.segments.append(snake)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            segment = self.segments[i]
            new_position = self.segments[i - 1].position()
            segment.goto(new_position)
        self.segments[0].forward(self.distance)

    def up(self):
        head = self.segments[0]
        if head.heading() != 270:
            head.setheading(90)

    def down(self):
        head = self.segments[0]
        if head.heading() != 90:
            head.setheading(270)

    def left(self):
        head = self.segments[0]
        if head.heading() != 0:
            head.setheading(180)

    def right(self):
        head = self.segments[0]
        if head.heading() != 180:
            head.setheading(0)

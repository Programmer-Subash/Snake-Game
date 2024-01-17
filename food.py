from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, width: int, height: int, foodcolor="green"):
        """window width and window height"""
        self.window_width = width
        self.window_height = height
        super().__init__()
        super().shape("circle")
        super().penup()
        super().color(foodcolor)
        super().shapesize(0.5)

    def random_location(self):
        border = 50
        x = random.randint(-self.window_width // 2 + border, self.window_width // 2 - border)
        y = random.randint(-self.window_height // 2 + border, self.window_height // 2 - border)
        return (x, y)

    def move_to_random_location(self):
        super().goto(self.random_location())

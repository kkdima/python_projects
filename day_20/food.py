from random import randint
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("DeepPink")
        self.speed("fastest")
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)

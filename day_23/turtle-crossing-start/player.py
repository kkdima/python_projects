from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player():
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.setheading(90)
        self.turtle.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.turtle.ycor() + MOVE_DISTANCE
        self.turtle.goto(self.turtle.xcor(), new_y)

    def go_to_start(self):
        self.turtle.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.turtle.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
